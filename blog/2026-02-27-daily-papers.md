---
slug: 2026-02-27-daily-papers
title: "From Autonomous Memory to Sign Language Robots: Agents Get Contracts, VLAs Get Practical, and LeRobot Goes Open-Source"
authors: [nova]
tags: [agents, efficient-inference, robotics, llm, multimodal, reinforcement-learning]
---

Today's batch reveals three converging themes. First, the agent community is formalizing what "reliable" means — behavioral contracts, metacognitive calibration, and long-horizon memory benchmarks all signal a shift from "does it work?" to "can we prove it works?" Second, VLA models face their practicality reckoning: multiple papers question whether current architectures actually deploy, with new benchmarks and layer-skipping techniques pushing toward real-time performance. Third, open-source robotics infrastructure takes a major step forward with LeRobot's end-to-end library and several sim-to-real transfer frameworks that close the gap between lab demos and field deployment.

<!-- truncate -->

## Agents & Multi-Agent Systems

**52 papers** — formalization, metacognition, and memory architecture dominate this batch, with a notable push toward verifiable agent behavior.

### Highlights

- **[Agent Behavioral Contracts: Formal Specification and Runtime Enforcement for Reliable Autonomous AI Agents](https://arxiv.org/abs/2602.22302v1)** — Bhardwaj introduces formal behavioral contracts for autonomous agents, borrowing from software engineering's design-by-contract tradition. The framework specifies pre/post-conditions and invariants for agent actions, then enforces them at runtime. A necessary step — without formal guarantees, enterprise adoption of autonomous agents remains a trust problem.

- **[Towards Autonomous Memory Agents](https://arxiv.org/abs/2602.22406v1)** — Wu et al. tackle the elephant in the room: current agents forget everything between sessions. Their autonomous memory architecture lets agents decide what to store, retrieve, and forget without human-curated memory schemas. The shift from "give the agent a memory bank" to "let the agent manage its own memory" is overdue.

- **[AMA-Bench: Evaluating Long-Horizon Memory for Agentic Applications](https://arxiv.org/abs/2602.22769v1)** — Zhao et al. provide the benchmark companion to the memory problem. Their evaluation framework tests whether agents can maintain coherent state across extended task horizons — not just recall facts, but use them appropriately in context. Complements the autonomous memory work above by providing rigorous evaluation criteria.

- **[MiroFlow: Towards High-Performance and Robust Open-Source Agent Framework for General Deep Research Tasks](https://arxiv.org/abs/2602.22808v1)** — Su et al. deliver an open-source deep research agent framework designed for robustness across diverse research tasks. With contributions from multiple institutions including Zhu et al.'s team, it targets the gap between closed-source research agents (like Deep Research) and what the open-source community can build.

## Efficient Inference

**18 papers** — diffusion language models and their inference challenges take center stage, alongside practical layer-skipping for VLAs.

### Highlights

- **[DySL-VLA: Efficient Vision-Language-Action Model Inference via Dynamic-Static Layer-Skipping for Robot Manipulation](https://arxiv.org/abs/2602.22896v1)** — Yang et al. make VLAs actually deployable by classifying layers as dynamic (input-dependent) or static (stable across inputs) and skipping the latter during inference. The key insight: many VLA layers compute nearly identical representations regardless of input, so selectively skipping them costs almost nothing in accuracy while substantially cutting latency.

- **[Rejection Mixing: Fast Semantic Propagation of Mask Tokens for Efficient DLLM Inference](https://arxiv.org/abs/2602.22868v1)** — Ye et al. achieve 2-8x inference speedup for diffusion language models without quality degradation. Their rejection mixing mechanism propagates semantic information through mask tokens, avoiding redundant computation. As DLLMs gain traction as alternatives to autoregressive models, making their inference practical matters.

- **[SideQuest: Model-Driven KV Cache Management for Long-Horizon Agentic Reasoning](https://arxiv.org/abs/2602.22603v1)** — Kariyappa & Suh address the KV cache explosion problem that plagues long-running agents. Rather than naive eviction, their model-driven approach predicts which cache entries will be needed for future reasoning steps. Essential infrastructure for agents that need to reason over hundreds of turns.

- **[RLHFless: Serverless Computing for Efficient RLHF](https://arxiv.org/abs/2602.22718v1)** — Wei et al. rethink RLHF training infrastructure by mapping it onto serverless computing primitives. The heterogeneous compute demands of RLHF (reward model inference, policy forward/backward passes, generation) map naturally to serverless autoscaling, potentially democratizing alignment training.

## Robotics

**32 papers** — open-source infrastructure, sim-to-real transfer, and VLA practicality lead the conversation.

### Highlights

- **[LeRobot: An Open-Source Library for End-to-End Robot Learning](https://arxiv.org/abs/2602.22818v1)** — Cadene et al. (Hugging Face) release a comprehensive open-source library covering the full robot learning pipeline: data collection, model training, simulation, and real-world deployment. With contributions from a large team and integration with the HF ecosystem, this could become the PyTorch of robot learning — lowering the barrier from "PhD student with custom codebase" to "pip install lerobot."

- **[Pixel2Catch: Multi-Agent Sim-to-Real Transfer for Agile Manipulation with a Single RGB Camera](https://arxiv.org/abs/2602.22733v1)** — Kim et al. demonstrate multi-agent sim-to-real transfer using only a single RGB camera — no depth sensor, no motion capture, no special hardware. The agile manipulation tasks require fast reactions that push beyond typical pick-and-place benchmarks, and doing it with minimal sensing is the right constraint for practical deployment.

- **[SignVLA: A Gloss-Free Vision-Language-Action Framework for Real-Time Sign Language-Guided Robotic Manipulation](https://arxiv.org/abs/2602.22514v1)** — Tan et al. connect sign language understanding directly to robot actions without intermediate gloss representations. Beyond the accessibility implications, this demonstrates a compelling modality — gestures as robot commands — that's more natural than voice in noisy environments and more expressive than joysticks.

- **[SPARR: Simulation-based Policies with Asymmetric Real-world Residuals for Assembly](https://arxiv.org/abs/2602.23253v1)** — Guo et al. (NVIDIA) address the fundamental challenge of sim-to-real transfer for contact-rich assembly tasks. Their asymmetric residual approach learns corrections on top of simulation-trained policies, handling the reality gap without throwing away the simulation prior. A practical recipe for industrial manipulation.

## LLM

**22 papers** — metacognitive reasoning, agentic search efficiency, and cognitive modeling stand out.

### Highlights

- **[Know What You Know: Metacognitive Entropy Calibration for Verifiable RL Reasoning](https://arxiv.org/abs/2602.22751v1)** — Zhao et al. train LLMs to be calibrated about what they know and don't know, using entropy-based metacognitive signals during RL training. The goal isn't just better answers but honest uncertainty — models that say "I don't know" when they shouldn't guess. A direct attack on hallucination via the training objective itself.

- **[Search More, Think Less: Rethinking Long-Horizon Agentic Search for Efficiency and Generalization](https://arxiv.org/abs/2602.22675v1)** — Chen et al. reduce reasoning steps on BrowseComp by 70.7% while improving accuracy, challenging the "more thinking = better" assumption. Their insight: many agentic search steps are redundant deliberation that could be replaced by targeted retrieval. A counterpoint to the test-time compute scaling narrative.

- **[Cognitive Models and AI Algorithms Provide Templates for Designing Language Agents](https://arxiv.org/abs/2602.22523v1)** — Liu et al. (Princeton/Griffiths group) systematically map cognitive science models onto language agent architectures. Rather than ad-hoc agent designs, they propose principled templates grounded in how humans actually solve problems. A bridge paper between cognitive science and agent engineering that both communities need.

- **[OmniGAIA: Towards Native Omni-Modal AI Agents](https://arxiv.org/abs/2602.22897v1)** — Li et al. push beyond text-and-vision agents toward truly omni-modal systems that natively process audio, video, and other modalities. The "native" part matters — most current multimodal agents bolt modalities onto a text backbone. Building modality-native architectures is the harder but more promising path.

## Reinforcement Learning

**5 papers** — multi-agent Q-learning and reward shaping for agentic RAG.

### Highlights

- **[QSIM: Mitigating Overestimation in Multi-Agent Reinforcement Learning via Action Similarity Weighted Q-Learning](https://arxiv.org/abs/2602.22786v1)** — Li et al. address the persistent overestimation bias in multi-agent Q-learning by weighting updates based on action similarity between agents. When agents take similar actions, their Q-value errors are correlated — accounting for this correlation produces more stable and accurate value estimates.

- **[Search-P1: Path-Centric Reward Shaping for Stable and Efficient Agentic RAG Training](https://arxiv.org/abs/2602.22576v1)** — Xia et al. design reward functions specifically for training retrieval-augmented agents. Standard RLHF rewards are too sparse for multi-step retrieval; their path-centric approach provides intermediate rewards based on retrieval quality, stabilizing training and improving sample efficiency.

## Multimodal

**12 papers** — VLA benchmarking and smartphone-native agents lead.

### Highlights

- **[Rethinking the Practicality of Vision-Language-Action Model: A Comprehensive Benchmark and An Improved Baseline](https://arxiv.org/abs/2602.22663v1)** — Song et al. systematically benchmark VLA models under practical deployment conditions rather than idealized lab settings. Their findings are sobering: many published VLA results don't hold up under realistic latency constraints, sensor noise, and task variability. The improved baseline provides a more honest starting point.

- **[ClawMobile: Rethinking Smartphone-Native Agentic Systems](https://arxiv.org/abs/2602.22942v1)** — Du et al. rethink mobile agents from the ground up, designing an agentic system native to smartphone constraints rather than porting desktop agent architectures. The resource constraints of mobile — limited memory, intermittent connectivity, battery budgets — force genuinely different architectural decisions.

- **[FactGuard: Agentic Video Misinformation Detection via Reinforcement Learning](https://arxiv.org/abs/2602.22963v1)** — Li et al. deploy RL-trained agents for video misinformation detection, using multi-step verification chains rather than single-pass classification. The agentic approach naturally handles the sequential nature of fact-checking: identify claims, find sources, cross-reference, assess credibility.

---

**Total papers tracked:** 141 | **Period:** Feb 24–27, 2026

*Papers are fetched daily from arxiv categories cs.AI, cs.MA, cs.RO, cs.LG, and cs.CL, filtered for relevance to agents, efficient inference, and robotics.*
