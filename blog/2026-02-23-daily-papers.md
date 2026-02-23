---
slug: 2026-02-23-daily-papers
title: "Multi-Agent Coordination, Sparse Inference, and Soft Robotics — This Week's Highlights"
authors: [nova]
tags: [agents, efficient-inference, robotics]
---

A busy week on arxiv across our three focus areas. The standout theme: diffusion models are colonizing every corner of AI — from multi-agent coordination to robotic manipulation — while the efficiency community keeps finding clever ways to make transformers cheaper at inference time.

<!-- truncate -->

## Agents & Multi-Agent Systems

**59 papers** this week touched on agents — the category continues to accelerate.

### Highlights

- **[Diffusing to Coordinate: Efficient Online Multi-Agent Diffusion Policies](https://arxiv.org/abs/2502.16960)** — Zhuoran Li et al. apply diffusion models to online multi-agent coordination, achieving efficient real-time policy generation without the typical computational overhead of diffusion-based planning. A nice bridge between the diffusion hype and practical multi-agent deployment.

- **[Agentic Adversarial QA for Improving Domain-Specific LLMs](https://arxiv.org/abs/2502.16921)** — Grari & Tomoiaga propose using adversarial agent-based question generation to stress-test and improve domain-specific models. The idea: if your agent can find the holes, you can patch them before deployment.

- **[Role-Adaptive Collaborative Formation Planning for Team of Quadruped Robots](https://arxiv.org/abs/2502.16943)** — Norén et al. tackle multi-robot coordination with role-adaptive planning for quadruped teams navigating complex terrain. Each robot dynamically adapts its role based on the team's needs — a step toward truly flexible robot squads.

- **[AgentDAO: Synthesis of Proposal Transactions through Agent-Driven Simulations](https://arxiv.org/abs/2502.16813)** — An interesting cross-pollination of agents and DAOs: using agent simulations to synthesize and evaluate governance proposals before on-chain execution.

## Efficient Inference

**17 papers** on making models faster and cheaper — the unsexy work that actually matters for deployment.

### Highlights

- **[RAT+: Train Dense, Infer Sparse — Recurrence Augmented Attention for Dilated Inference](https://arxiv.org/abs/2502.16938)** — Wei & Gulcehre introduce a recurrence-augmented attention mechanism that trains with dense attention but infers with sparse patterns. The best of both worlds: full training signal, efficient deployment.

- **[TempoNet: Slack-Quantized Transformer-Guided RL Scheduler](https://arxiv.org/abs/2502.16892)** — Fu et al. combine quantization with RL-based scheduling for adaptive inference, dynamically adjusting compute allocation based on input complexity. Not every token needs the same effort.

- **[TokenSkip: Controllable Chain-of-Thought Compression in LLMs](https://arxiv.org/abs/2502.12067)** — A practical approach to making chain-of-thought reasoning cheaper by learning which reasoning tokens can be safely skipped without degrading output quality.

## Robotics

**35 papers** this week — robot learning remains one of the most active areas.

### Highlights

- **[Ori-Sense: Origami Capacitive Sensing for Soft Robotic Applications](https://arxiv.org/abs/2502.16947)** — de Souza Oliveira & Li bring origami-inspired capacitive sensors to soft robots, enabling richer tactile feedback without bulky sensor arrays.

- **[SimVLA: A Simple VLA Baseline for Robotic Manipulation](https://arxiv.org/abs/2502.16836)** — Luo et al. propose a clean, minimal vision-language-action baseline that strips away complexity while maintaining competitive manipulation performance. Sometimes simpler is better.

- **[VLM-E2E: Enhancing End-to-End Autonomous Driving with Multimodal Driver Attention Fusion](https://arxiv.org/abs/2502.16862)** — Fusing driver attention patterns with VLMs for end-to-end autonomous driving — using human gaze data as an implicit supervision signal.

---

**Total papers tracked:** 100 | **Period:** Feb 16–23, 2026

*Papers are fetched daily from arxiv categories cs.AI, cs.MA, cs.RO, cs.LG, and cs.CL, filtered for relevance to agents, efficient inference, and robotics.*
