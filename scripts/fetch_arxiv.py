#!/usr/bin/env python3
"""
Fetch recent arxiv papers on agents, efficient inference, and robotics.
Outputs a JSON file with paper metadata for the cron agent to write up.

Usage:
    python3 scripts/fetch_arxiv.py [--days N] [--max-results N] [--output PATH]

Uses the arxiv Atom API (no key required).
"""

import argparse
import json
import re
import sys
import time
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

SCRIPT_DIR = Path(__file__).resolve().parent
BLOG_DIR = SCRIPT_DIR.parent / "blog"

# arxiv categories of interest
CATEGORIES = [
    "cs.AI",   # Artificial Intelligence
    "cs.MA",   # Multi-Agent Systems
    "cs.RO",   # Robotics
    "cs.LG",   # Machine Learning
    "cs.CL",   # Computation and Language (NLP/LLMs)
]

# Keyword queries — these run as OR within each group
QUERY_GROUPS = [
    # Agents
    '(ti:"agent" OR ti:"multi-agent" OR ti:"tool use" OR ti:"planning" OR ti:"agentic")',
    # Efficient inference
    '(ti:"efficient inference" OR ti:"quantization" OR ti:"distillation" OR ti:"speculative decoding" OR ti:"pruning" OR ti:"inference optimization" OR ti:"KV cache" OR ti:"sparse" OR ti:"mixture of experts")',
    # Robotics
    '(ti:"robot" OR ti:"manipulation" OR ti:"locomotion" OR ti:"embodied" OR ti:"sim-to-real")',
]

ARXIV_API = "http://export.arxiv.org/api/query"
ATOM_NS = "{http://www.w3.org/2005/Atom}"
ARXIV_NS = "{http://arxiv.org/schemas/atom}"


def build_query() -> str:
    """Build an arxiv API query combining categories and keywords."""
    cat_filter = " OR ".join(f"cat:{c}" for c in CATEGORIES)
    keyword_filter = " OR ".join(QUERY_GROUPS)
    return f"({cat_filter}) AND ({keyword_filter})"


def fetch_papers(max_results: int = 100) -> list[dict]:
    """Fetch papers from arxiv API."""
    query = build_query()
    params = {
        "search_query": query,
        "start": 0,
        "max_results": max_results,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }
    url = f"{ARXIV_API}?{urlencode(params)}"

    req = Request(url, headers={"User-Agent": "DailyPaper/1.0"})
    with urlopen(req, timeout=30) as resp:
        data = resp.read()

    root = ET.fromstring(data)
    papers = []

    for entry in root.findall(f"{ATOM_NS}entry"):
        paper_id_url = entry.findtext(f"{ATOM_NS}id", "")
        paper_id = paper_id_url.split("/abs/")[-1] if "/abs/" in paper_id_url else paper_id_url

        title = entry.findtext(f"{ATOM_NS}title", "").strip()
        title = re.sub(r"\s+", " ", title)

        summary = entry.findtext(f"{ATOM_NS}summary", "").strip()
        summary = re.sub(r"\s+", " ", summary)
        if len(summary) > 600:
            summary = summary[:597] + "..."

        published = entry.findtext(f"{ATOM_NS}published", "")
        updated = entry.findtext(f"{ATOM_NS}updated", "")

        authors = []
        for author_el in entry.findall(f"{ATOM_NS}author"):
            name = author_el.findtext(f"{ATOM_NS}name", "")
            if name:
                authors.append(name)

        categories = []
        for cat_el in entry.findall(f"{ARXIV_NS}primary_category") + entry.findall(f"{ATOM_NS}category"):
            term = cat_el.get("term", "")
            if term and term not in categories:
                categories.append(term)

        # Get PDF link
        pdf_link = ""
        for link_el in entry.findall(f"{ATOM_NS}link"):
            if link_el.get("title") == "pdf":
                pdf_link = link_el.get("href", "")
                break

        abs_link = f"https://arxiv.org/abs/{paper_id}"

        papers.append({
            "id": paper_id,
            "title": title,
            "authors": authors[:5],  # cap at 5 for readability
            "author_count": len(authors),
            "summary": summary,
            "categories": categories[:5],
            "published": published,
            "updated": updated,
            "abs_url": abs_link,
            "pdf_url": pdf_link or f"https://arxiv.org/pdf/{paper_id}",
        })

    return papers


def classify_paper(paper: dict) -> list[str]:
    """Assign topic tags based on title/categories."""
    tags = []
    title_lower = paper["title"].lower()
    cats = " ".join(paper["categories"]).lower()

    if any(kw in title_lower for kw in ["agent", "multi-agent", "agentic", "tool use", "planning"]):
        tags.append("agents")
    if any(kw in title_lower for kw in ["quantiz", "distill", "pruning", "speculative", "efficient", "kv cache", "sparse", "mixture of experts", "inference"]):
        tags.append("efficient-inference")
    if any(kw in title_lower for kw in ["robot", "manipulat", "locomot", "embodied", "sim-to-real", "grasp"]):
        tags.append("robotics")
    if any(kw in title_lower for kw in ["language model", "llm", "gpt", "transformer", "token"]):
        tags.append("llm")
    if any(kw in title_lower for kw in ["vision", "multimodal", "image", "video", "visual"]):
        tags.append("multimodal")
    if any(kw in title_lower for kw in ["reinforcement", "reward", "rlhf", "ppo", "dpo"]):
        tags.append("reinforcement-learning")

    if "cs.ro" in cats and "robotics" not in tags:
        tags.append("robotics")
    if "cs.ma" in cats and "agents" not in tags:
        tags.append("agents")

    return tags if tags else ["llm"]


def filter_recent(papers: list[dict], days: int) -> list[dict]:
    """Filter papers to those published within the last N days."""
    cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    recent = []
    for p in papers:
        try:
            pub = datetime.fromisoformat(p["published"].replace("Z", "+00:00"))
            if pub >= cutoff:
                recent.append(p)
        except (ValueError, KeyError):
            continue
    return recent


def main():
    parser = argparse.ArgumentParser(description="Fetch recent arxiv papers")
    parser.add_argument("--days", type=int, default=3, help="Look back N days (default: 3)")
    parser.add_argument("--max-results", type=int, default=150, help="Max results from API (default: 150)")
    parser.add_argument("--output", type=str, default=None, help="Output JSON path")
    args = parser.parse_args()

    print(f"Querying arxiv (max {args.max_results} results, last {args.days} days)...")
    papers = fetch_papers(max_results=args.max_results)
    print(f"  Fetched {len(papers)} papers from API")

    papers = filter_recent(papers, args.days)
    print(f"  {len(papers)} papers within last {args.days} days")

    # Classify and deduplicate
    seen_ids = set()
    classified = []
    for p in papers:
        if p["id"] in seen_ids:
            continue
        seen_ids.add(p["id"])
        p["tags"] = classify_paper(p)
        classified.append(p)

    classified.sort(key=lambda p: p["published"], reverse=True)
    print(f"  {len(classified)} unique papers after dedup")

    # Group by topic for summary
    by_topic = {}
    for p in classified:
        for tag in p["tags"]:
            by_topic.setdefault(tag, []).append(p["title"])
    for topic, titles in by_topic.items():
        print(f"    {topic}: {len(titles)} papers")

    output_path = Path(args.output) if args.output else SCRIPT_DIR / "papers.json"
    output_path.write_text(json.dumps(classified, indent=2))
    print(f"\nWrote {len(classified)} papers to {output_path}")


if __name__ == "__main__":
    main()
