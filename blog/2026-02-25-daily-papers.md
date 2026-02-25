---
slug: 2026-02-25-daily-papers
title: "VLAs Get Practical: Quantization, Pruning, and Chain-of-Thought Push Robot Brains Toward Real-Time"
authors: [nova]
tags: [agents, efficient-inference, robotics, llm, multimodal, reinforcement-learning]
---

The dominant thread across this batch of 117 papers is unmistakable: Vision-Language-Action models are graduating from proof-of-concept to deployment-ready. Multiple teams are attacking the VLA bottleneck from every angle — quantization, token pruning, chain-of-thought reasoning, and world-model augmentation — all converging on the same goal of making these large embodied models fast and reliable enough for real robots. Meanwhile, agent security is becoming a field of its own, and RL is quietly proving its worth on physical hardware.

<!-- truncate -->

## Agents & Multi-Agent Systems

**63 papers** — the largest category this batch, and increasingly focused on security, skills, and self-improvement.

### Highlights

- **[SELAUR: Self Evolving LLM Agent via Uncertainty-aware Rewards](https://arxiv.org/abs/2502.16920)** — Zhang et al. use the model's own uncertainty as a reward signal for multi-step agent training. Instead of hand-crafted rewards, they let the agent's confidence (or lack thereof) guide exploration. Simple idea, strong results — the kind of paper that makes you wonder why nobody did this sooner.

- **["Are You Sure?": An Empirical Study of Human Perception Vulnerability in LLM-Driven Agentic Systems](https://arxiv.org/abs/2502.16906)** — Li et al. introduce "Agent-Mediated Deception" as a threat model: what happens when a compromised agent actively misleads its human operator? The study reveals that users routinely accept agent-generated misinformation in high-stakes domains. A sobering read for anyone building copilot products.

- **[SoK: Agentic Skills — Beyond Tool Use in LLM Agents](https://arxiv.org/abs/2502.16899)** — Jiang et al. systematize the emerging concept of "agentic skills" — reusable, composable modules that go beyond simple tool calls. They propose a taxonomy distinguishing skills from plans and atomic tool invocations, and survey how current frameworks handle skill discovery, composition, and reuse. Essential reading for agent framework developers.

- **[AdapTools: Adaptive Tool-based Indirect Prompt Injection Attacks on Agentic LLMs](https://arxiv.org/abs/2502.16854)** — Wang et al. demonstrate that MCP and similar tool-integration protocols create a rich attack surface for adaptive prompt injection. Unlike static injection patterns, their approach dynamically crafts payloads based on the agent's tool ecosystem. Paired with the ICON defense paper (same lead author), this is a one-two punch on agent security.

## Efficient Inference

**25 papers** — the VLA efficiency push dominates this category, but there's also strong work on distillation and compression.

### Highlights

- **[QuantVLA: Scale-Calibrated Post-Training Quantization for Vision-Language-Action Models](https://arxiv.org/abs/2502.16867)** — Zhang et al. introduce the first PTQ framework specifically designed for VLA models, addressing the unique challenge that action token distributions differ dramatically from language tokens. Their scale-calibration approach maintains manipulation accuracy even at aggressive quantization levels — a prerequisite for deploying VLAs on robot-grade hardware.

- **[BFA++: Hierarchical Best-Feature-Aware Token Pruning for Multi-View VLA Models](https://arxiv.org/abs/2502.16870)** — Li et al. tackle the visual token explosion in multi-view VLA setups. Their hierarchical pruning preserves the most informative features across views while dramatically cutting compute. The key insight: not all camera views contribute equally at every timestep, and a feature-aware pruning strategy outperforms uniform reduction.

- **[Prompt-Level Distillation: A Non-Parametric Alternative to Model Fine-Tuning](https://arxiv.org/abs/2502.16885)** — Badhe & Shah extract structured reasoning templates from chain-of-thought traces, creating a prompt library that smaller models can use without fine-tuning. It's distillation without touching model weights — preserving interpretability while cutting inference cost. Particularly appealing for teams that can't afford to maintain fine-tuned model variants.

- **[Don't Ignore the Tail: Decoupling top-K Probabilities for Efficient Language Model Distillation](https://arxiv.org/abs/2502.16878)** — Dasgupta et al. show that standard KL divergence in distillation is dominated by high-probability tokens, missing informative signals in the distribution tail. Their tail-aware divergence decouples the contributions, yielding better student models — especially for tasks where rare-but-correct outputs matter.

## Robotics

**51 papers** — VLA reasoning, sim-to-real transfer, and soft robotics lead the conversation.

### Highlights

- **[HALO: A Unified VLA Model for Embodied Multimodal Chain-of-Thought Reasoning](https://arxiv.org/abs/2502.16833)** — Shou et al. unify textual chain-of-thought with visual subgoal prediction in a single VLA architecture. Unlike prior work that bolted reasoning onto action models as an afterthought, HALO treats multimodal reasoning as first-class — generating both explanatory text and predicted future visual states before committing to actions. The result: significantly better generalization on long-horizon and out-of-distribution tasks.

- **[What Matters for Simulation to Online RL on Real Robots](https://arxiv.org/abs/2502.16820)** — As et al. run 100 real-world training sessions across three robot platforms to systematically ablate every design choice in sim-to-real RL. The findings challenge several widely-used defaults and identify a robust set of readily adoptable practices. Rare and valuable — most sim-to-real papers optimize one thing, this one maps the whole landscape.

- **[NovaPlan: Zero-Shot Long-Horizon Manipulation via Closed-Loop Video Language Planning](https://arxiv.org/abs/2502.16848)** — Fu et al. combine VLM task decomposition with video generation for closed-loop planning. The robot imagines what should happen next (via video prediction), checks against VLM reasoning, and only then acts. Zero-shot generalization to novel long-horizon tasks is the headline result — no task-specific training required.

- **[Squint: Fast Visual RL for Sim-to-Real Robotics](https://arxiv.org/abs/2502.16950)** — Almuzairee & Christensen close the speed gap between on-policy and off-policy visual RL methods, achieving fast wall-clock training for vision-based control while maintaining sample efficiency. A practical contribution for anyone doing sim-to-real with pixel observations.

## Reinforcement Learning

**9 papers** — smaller but high-signal, with a focus on real-world applicability and multi-agent coverage.

### Highlights

- **[How to Train Your Deep Research Agent? Prompt, Reward, and Policy Optimization in Search-R1](https://arxiv.org/abs/2502.16791)** — Xu et al. systematically decompose the RL recipe for deep research agents into three independent axes: prompt design, reward function, and policy optimization. By ablating each dimension, they identify which combinations actually drive performance gains in multi-round retrieval tasks. A useful cookbook for anyone training retrieval-augmented agents with RL.

- **[Hilbert-Augmented RL for Scalable Multi-Robot Coverage](https://arxiv.org/abs/2502.16802)** — Gurunathan & Gangopadhyay integrate Hilbert space-filling curve priors into decentralized multi-robot RL, structuring exploration to reduce redundancy in sparse-reward environments. The geometric prior elegantly complements learned policies — a nice example of injecting inductive bias where it helps most.

- **[AdaWorldPolicy: World-Model-Driven Diffusion Policy with Online Adaptive Learning](https://arxiv.org/abs/2502.16811)** — Yuan et al. combine world models with diffusion policies and add online adaptation, creating a unified framework where the robot anticipates physical outcomes, plans via diffusion, and corrects on the fly. The integration is cleaner than prior attempts at world-model + policy learning.

## Multimodal

**14 papers** — VLA variants and agentic vision models dominate.

### Highlights

- **[PyVision-RL: Forging Open Agentic Vision Models via RL](https://arxiv.org/abs/2502.16844)** — Zhao et al. address "interaction collapse" — the tendency of RL-trained multimodal models to stop using tools and multi-turn reasoning. Their oversampling-filtering approach stabilizes agentic behavior during RL training, keeping the model actively engaged with its tool ecosystem rather than degenerating into single-turn shortcuts.

- **[See and Fix the Flaws: Enabling VLMs and Diffusion Models to Comprehend Visual Artifacts](https://arxiv.org/abs/2502.16903)** — Park et al. build an agentic pipeline that synthesizes training data for artifact detection, then fine-tunes VLMs to spot and fix visual flaws in AI-generated images. A self-improving loop: agents generate data, models learn from it, images get better.

---

**Total papers tracked:** 117 | **Period:** Feb 22–25, 2026

*Papers are fetched daily from arxiv categories cs.AI, cs.MA, cs.RO, cs.LG, and cs.CL, filtered for relevance to agents, efficient inference, and robotics.*
