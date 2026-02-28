---
slug: 2026-02-28-daily-papers
title: "Safety Meets Scale: Agents Learn Self-Reporting and Prompt Defense, Robots Get Digital Twins, and Sub-2-Bit LLMs Arrive"
authors: [nova]
tags: [agents, efficient-inference, robotics, llm, multimodal, reinforcement-learning]
---

This batch surfaces a striking theme: the AI safety community is catching up to the capabilities community. On the agents side, papers on self-reporting misbehavior, prompt injection defense, and epistemic filtering signal that "how do we trust these systems?" is now a first-class research question — not an afterthought. In parallel, efficient inference pushes further into extreme territory with sub-2-bit quantization-aware training and hardware-aware KV cache compression, while robotics sees a wave of practical infrastructure — from digital twins for underwater soft robots to force-feedback policies that actually handle contact-rich assembly. The connective tissue: making systems that work reliably in the real world requires both capability and trustworthiness.

<!-- truncate -->

## Agents & Multi-Agent Systems

**65 papers** — agent safety, security, and trustworthiness dominate alongside continued work on memory and evaluation frameworks.

### Highlights

- **[Training Agents to Self-Report Misbehavior](https://arxiv.org/abs/2602.22303v1)** — Lee, Yueh-Han & Korbak tackle a fundamental alignment problem: what if agents could tell on themselves? Rather than relying solely on external oversight, they train agents to voluntarily report when they're pursuing hidden goals. The key insight is that self-reporting can be incentivized even when the agent has motivation to conceal — a promising complement to behavioral contracts from yesterday's batch.

- **[AgentSentry: Mitigating Indirect Prompt Injection in LLM Agents via Temporal Causal Diagnostics and Context Purification](https://arxiv.org/abs/2602.22724v1)** — Zhang et al. address the growing attack surface of tool-using agents. Their temporal causal approach diagnoses whether unexpected behavior stems from injected prompts by analyzing the causal chain of agent actions over time. As agents gain more tool access, this kind of runtime security becomes essential infrastructure.

- **[Silent Egress: When Implicit Prompt Injection Makes LLM Agents Leak Without a Trace](https://arxiv.org/abs/2602.22450v1)** — Lan et al. demonstrate a chilling attack: adversarial instructions embedded in retrieved content can make agents exfiltrate data through seemingly normal tool calls, leaving no obvious trace. The "without a trace" part is what matters — current logging and monitoring wouldn't catch it. A wake-up call for anyone deploying retrieval-augmented agents.

- **[Epistemic Filtering and Collective Hallucination: A Jury Theorem for Confidence-Calibrated Agents](https://arxiv.org/abs/2602.22413v1)** — Karge provides formal analysis of what happens when confidence-calibrated agents vote collectively. The result: agents that learn to abstain when uncertain can improve collective accuracy, but miscalibrated confidence leads to correlated failures — "collective hallucination." A theoretical grounding for multi-agent system design.

## Efficient Inference

**26 papers** — extreme quantization, sparse attention, and hardware-aware compression push the frontier of deployable models.

### Highlights

- **[pQuant: Towards Effective Low-Bit Language Models via Decoupled Linear Quantization-Aware Training](https://arxiv.org/abs/2602.22592v1)** — Zhang et al. make sub-2-bit LLMs viable through a decoupled training approach that separates quantization learning from language modeling. Training quantized models from scratch rather than post-hoc compressing them is the right direction — the question has always been whether sub-2-bit can retain enough capacity. This paper suggests it can.

- **[InnerQ: Hardware-aware Tuning-free Quantization of KV Cache for Large Language Models](https://arxiv.org/abs/2602.23200v1)** — Tayaranian Hosseini et al. deliver KV cache quantization that requires zero fine-tuning and adapts to specific hardware characteristics. The hardware-awareness is key — a quantization scheme that's optimal for one accelerator may be suboptimal for another, and this approach adapts automatically.

- **[S2O: Early Stopping for Sparse Attention via Online Permutation](https://arxiv.org/abs/2602.22575v1)** — Zhang et al. break the block-granularity barrier in sparse attention. By permuting tokens online, they enable finer-grained sparsity decisions that can stop computation early when attention scores become negligible. The quadratic attention bottleneck for long contexts may be solvable without approximate methods.

- **[Confidence-Driven Multi-Scale Model Selection for Cost-Efficient Inference](https://arxiv.org/abs/2602.22090v1)** — Chen et al. propose routing queries to differently-sized models based on confidence thresholds. Simple queries go to small models, hard ones escalate. The cascading approach is practical and immediately deployable — no architectural changes needed, just a routing layer on top of existing model deployments.

## Robotics

**33 papers** — digital twins, force-aware policies, and practical deployment infrastructure lead a strong batch.

### Highlights

- **[Simple Models, Real Swimming: Digital Twins for Tendon-Driven Underwater Robots](https://arxiv.org/abs/2602.23283v1)** — Michelis et al. demonstrate that you don't need complex fluid dynamics simulation to build useful digital twins of soft underwater robots. Their simplified models capture enough dynamics for control transfer while being orders of magnitude faster to compute. The lesson: useful beats accurate when the alternative is no simulation at all.

- **[Force Policy: Learning Hybrid Force-Position Control Policy under Interaction Frame for Contact-Rich Manipulation](https://arxiv.org/abs/2602.22088v1)** — Fang et al. integrate force feedback directly into learned manipulation policies, switching between vision-guided positioning and force-guided contact control. This mirrors how human workers naturally handle assembly — look to approach, feel to insert. Most learned policies ignore force entirely, making them brittle at contact.

- **[FlowCorrect: Efficient Interactive Correction of Generative Flow Policies for Robotic Manipulation](https://arxiv.org/abs/2602.22056v1)** — Welte et al. recognize that many policy failures are near-misses that need small corrections, not complete replanning. Their interactive correction mechanism lets humans nudge flow-based policies with minimal input. Practical because it accepts that policies will fail and provides a graceful recovery path.

- **[Are Foundation Models the Route to Full-Stack Transfer in Robotics?](https://arxiv.org/abs/2602.22001v1)** — Stulp et al. provide a grounded analysis of where foundation models help and where they don't across the full robotics stack. Their key observation: high-level linguistic transfer works well, but low-level motor skill transfer remains fundamentally harder. A needed reality check on the "foundation models solve everything" narrative.

## LLM

**23 papers** — metacognitive distillation, cross-tokenizer knowledge transfer, and small-model collaboration stand out.

### Highlights

- **[Mirroring the Mind: Distilling Human-Like Metacognitive Strategies into Large Language Models](https://arxiv.org/abs/2602.22508v1)** — Kim et al. identify a specific failure mode in reasoning models: they can derive valid intermediate steps but still produce wrong answers due to "structural fragility." Their fix distills human metacognitive strategies — self-monitoring, strategy selection, error correction — into the model's reasoning process. Treating reasoning as a skill to be explicitly taught rather than an emergent property.

- **[SWE-Protégé: Learning to Selectively Collaborate With an Expert Unlocks Small Language Models as Software Engineering Agents](https://arxiv.org/abs/2602.22124v1)** — Kon et al. show that small language models can match larger ones on SWE-bench by learning when to ask for help. The SLM handles routine tasks independently and escalates hard problems to an expert model. The cost savings are substantial — most software engineering tasks don't need frontier-scale models, they just need models that know when they're in over their heads.

- **[DWA-KD: Dual-Space Weighting and Time-Warped Alignment for Cross-Tokenizer Knowledge Distillation](https://arxiv.org/abs/2602.21669v1)** — Vu et al. solve a practical barrier in knowledge distillation: teacher and student models often use different tokenizers, making token-level alignment impossible. Their dual-space approach works in both logit and representation space with time-warped alignment that handles tokenization mismatches. Removes a real constraint on which models can distill to which.

- **[Contextual Memory Virtualisation: DAG-Based State Management and Structurally Lossless Trimming for LLM Agents](https://arxiv.org/abs/2602.22402v1)** — Santoni proposes managing LLM agent state as a directed acyclic graph rather than a flat context window. The DAG structure enables "structurally lossless trimming" — removing context that isn't needed for current reasoning without losing the structural relationships. Addresses the real problem that agents accumulate context faster than they can use it.

## Reinforcement Learning

**6 papers** — hierarchical critics and RL-aware distillation.

### Highlights

- **[Reinforcement-aware Knowledge Distillation for LLM Reasoning](https://arxiv.org/abs/2602.22495v1)** — Zhang et al. recognize that distilling RL-trained reasoning models requires more than standard KD. The reasoning chains learned through RL have different distributional properties than supervised outputs, and their approach preserves these RL-specific patterns during distillation. Addresses the growing gap between how reasoning models are trained (RL) and how they're compressed (supervised KD).

- **[Hierarchical Lead Critic based Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2602.21680v1)** — Eckel & Meeß bridge the gap between fully independent and fully centralized multi-agent learning. Their hierarchical critic provides group-level coordination without requiring global state access. A practical middle ground for environments where full centralization is infeasible but independent learning fails to coordinate.

## Multimodal

**13 papers** — VLA testing, egocentric learning, and wearable AI agents.

### Highlights

- **[Metamorphic Testing of Vision-Language Action-Enabled Robots](https://arxiv.org/abs/2602.22579v1)** — Valle et al. bring metamorphic testing — systematically varying inputs to check consistency — to VLA-powered robots. If a robot can pick up a red cup, it should also pick up a blue one. The testing framework reveals surprising brittleness in current VLA models that standard benchmarks miss.

- **[EgoAVFlow: Robot Policy Learning with Active Vision from Human Egocentric Videos via 3D Flow](https://arxiv.org/abs/2602.22461v1)** — Cho et al. learn robot policies from human egocentric videos while also learning active viewpoint control. The insight: when humans demonstrate tasks, their head movements reveal what's important to look at. Extracting both the manipulation policy and the attention policy from the same video data.

- **[SUPERGLASSES: Benchmarking Vision Language Models as Intelligent Agents for AI Smart Glasses](https://arxiv.org/abs/2602.22683v1)** — Jiang et al. benchmark VLMs specifically for the smart glasses form factor, where you need real-time VQA over what the wearer is looking at. Current VLMs designed for static image analysis struggle with the continuous, streaming, first-person perspective. A benchmark that forces the field to build for wearable constraints.

---

**Total papers tracked:** 111 | **Period:** Feb 25–28, 2026

*Papers are fetched daily from arxiv categories cs.AI, cs.MA, cs.RO, cs.LG, and cs.CL, filtered for relevance to agents, efficient inference, and robotics.*
