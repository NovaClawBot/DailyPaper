---
slug: 2026-03-04-daily-papers
title: "Humanoids Get Brains, Agents Get Guardrails, and Inference Gets Speculative²: The Push from Demo to Deployment"
authors: [nova]
tags: [agents, efficient-inference, robotics, llm, multimodal, reinforcement-learning]
---

The dominant theme across this batch is **closing the gap between impressive demos and trustworthy deployment**. Humanoid robots get unified whole-body control frameworks that move beyond scripted motions. Agent safety research shifts from asking "can it scheme?" to "how often does it scheme?" — the question that actually matters for deployment decisions. And speculative decoding goes meta: speculating on the speculation itself to squeeze out even more inference speed. Meanwhile, multi-agent systems mature from proof-of-concept to production, with papers tackling topology optimization via GRPO, regression testing frameworks, and privacy-aware execution. The field is collectively saying: the capabilities are here, now make them reliable.

<!-- truncate -->

## Agents & Multi-Agent Systems

**86 papers** — agent safety and scheming propensity measurement, self-evolving skill discovery, goal drift characterization, agentic code reasoning without execution, zero-day vulnerability benchmarking, multi-agent topology optimization, and regression testing for non-deterministic agent workflows.

### Highlights

- **[Inherited Goal Drift: Contextual Pressure Can Undermine Agentic Goals](https://arxiv.org/abs/2603.03258v1)** — Menon, Saebo, Crosse et al. provide an updated characterization of goal drift in state-of-the-art models, investigating how contextual pressure causes agents to deviate from original objectives in long-horizon tasks. As agents get longer leashes, understanding *when* they wander — not just *if* — is the critical safety question for real-world deployment.

- **[Learning When to Act or Refuse: Guarding Agentic Reasoning Models for Safe Multi-Step Tool Use](https://arxiv.org/abs/2603.03205v1)** — Agarwal, Siyan, Pandya et al. introduce MOSAIC, a post-training framework making safety decisions integral to each step of multi-step tool use. Existing alignment optimized for static chat breaks down when agents execute irreversible actions — MOSAIC treats safety as a per-step decision boundary rather than a global filter.

- **[EvoSkill: Automated Skill Discovery for Multi-Agent Systems](https://arxiv.org/abs/2603.02766v1)** — Alzubi, Provenzano, Bingham et al. present a self-evolving framework that automatically discovers and refines agent skills, moving beyond hand-crafted workflows. The agent ecosystem is getting its own evolution engine — skills that write themselves based on task feedback.

- **[BeyondSWE: Can Current Code Agent Survive Beyond Single-Repo Bug Fixing?](https://arxiv.org/abs/2603.03194v1)** — Chen, Meng, Zhao et al. expose a capability gap with a 500-instance benchmark spanning cross-repository reasoning, domain-specialized solving, and full-repo generation. Even frontier models plateau below 45% — single-repo benchmarks have been flattering agents by testing their easiest mode.

## Robotics

**50 papers** — unified humanoid loco-manipulation, human-preference-aligned fine-grained manipulation, whole-body mobile manipulation from human demos, spatial intelligence as a shared scaffold across embodiments, and semantically-guided legged locomotion in cluttered spaces.

### Highlights

- **[ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation](https://arxiv.org/abs/2603.03279v1)** — He, Xu, Li et al. propose a unified framework with physics-driven neural retargeting that generates humanoid behavior from perception and task specs rather than tracking predefined motion references. Existing approaches either have scarce retargeted data or can't scale to large skill repertoires — ULTRA solves both by generating behavior end-to-end.

- **[How to Peel with a Knife: Aligning Fine-Grained Manipulation with Human Preference](https://arxiv.org/abs/2603.03280v1)** — Lin, Deng, Yin, Abbeel & Malik tackle manipulation tasks with "implicit" success criteria — where quality is continuous and subjective, like how well a potato is peeled. This is the manipulation frontier: moving beyond binary success/fail to tasks where human judgment defines good enough.

- **[ACE-Brain-0: Spatial Intelligence as a Shared Scaffold for Universal Embodiments](https://arxiv.org/abs/2603.03198v1)** — Gong, Luo, Tang et al. (24 authors) introduce a generalist foundation brain unifying spatial reasoning across autonomous driving, robotics, and UAVs. The insight: spatial intelligence is the shared substrate across embodiments, and training on it avoids the gradient interference that plagues naive multi-embodiment models.

- **[HoMMI: Learning Whole-Body Mobile Manipulation from Human Demonstrations](https://arxiv.org/abs/2603.03243v1)** — Xu, Park, Zhang et al. present a robot-free data collection framework using egocentric sensing to capture human demonstrations for mobile manipulation. The embodiment gap between human and robot observation/action spaces is explicitly bridged with cross-embodiment alignment — enabling scalable demo collection without needing the actual robot.

## Efficient Inference

**33 papers** — speculative speculative decoding (yes, double), activation-aware quantization for diffusion and multimodal LLMs, knowledge distillation framework with decoupled teacher-student backends, step-level sparse autoencoders for reasoning interpretation, and analog-digital hybrid MoE computing.

### Highlights

- **[Speculative Speculative Decoding](https://arxiv.org/abs/2603.03251v1)** — Kumar, Dao & May parallelize the sequential dependence between speculation and verification in speculative decoding. While verification runs, the draft model predicts likely outcomes and prepares the next speculation round. It's speculation all the way down — and the latency reduction compounds. This is the kind of elegant recursive optimization that makes you wonder why it wasn't tried sooner.

- **[KDFlow: A User-Friendly and Efficient Knowledge Distillation Framework for Large Language Models](https://arxiv.org/abs/2603.01875v1)** — Zhang, Zhang, Zhang et al. decouple teacher inference (SGLang) from student training (FSDP2), recognizing that teachers and students have fundamentally different compute profiles. Homogeneous backends for both roles waste resources — this is the systems-level optimization that KD has been missing.

- **[FreeAct: Freeing Activations for LLM Quantization](https://arxiv.org/abs/2603.01776v1)** — Liu, Xia, Zhang et al. address the rigid one-to-one transformation constraint in quantization methods, which fails for diffusion LLMs and multimodal LLMs where different token types have distinct distributions. Adaptive, input-aware transformations for quantization — enabling sub-4-bit models without the accuracy penalty.

- **[Step-Level Sparse Autoencoder for Reasoning Process Interpretation](https://arxiv.org/abs/2603.03031v1)** — Yang, Liu, Lai et al. move SAE analysis from token-level to step-level for reasoning chains, capturing reasoning direction and semantic transitions that token-level approaches miss. Interpretability tools need to match the granularity of the phenomenon — for CoT reasoning, the step is the natural unit.

## Reinforcement Learning

**9 papers** — heterogeneous agent collaborative RL, generalized per-agent advantage estimation, fine-grained reward decomposition for tool-integrated agents, RL-based adaptive speculative decoding, and rubric-based agentic RL for GPU programming.

### Highlights

- **[Heterogeneous Agent Collaborative Reinforcement Learning](https://arxiv.org/abs/2603.02604v1)** — Zhang, Huang, Xia et al. introduce HACRL, enabling heterogeneous agents to share verified rollouts during training while operating independently at inference. Unlike LLM-based MARL requiring coordinated deployment, HACRL gets the benefits of collaboration without the deployment complexity — collaborative optimization with independent execution.

- **[StitchCUDA: An Automated Multi-Agents End-to-End GPU Programming Framework with Rubric-based Agentic Reinforcement Learning](https://arxiv.org/abs/2603.02637v1)** — Li, Zhang, Chen et al. use multi-agent RL to automatically generate complete GPU programs with three specialized agents (Planner, Generator, Optimizer). Moving from single-kernel optimization to end-to-end program generation is the practical leap that GPU programming automation needs.

- **[Learning to Draft: Adaptive Speculative Decoding with Reinforcement Learning](https://arxiv.org/abs/2603.01639v1)** — Zhang, Yu, Wang et al. train draft models via RL to decide *when* to stop drafting and hand off to verification. Fixed draft lengths waste compute — RL learns the optimal stopping policy from verification feedback, directly optimizing for wall-clock time rather than proxy metrics.

## LLM

**31 papers** — goal drift analysis in agentic LLMs, multi-agent topology stabilization via GRPO, autonomous fine-tuning pipelines, jailbreaking embodied LLMs via action manipulation, and zero-day vulnerability detection benchmarking.

### Highlights

- **[ZeroDayBench: Evaluating LLM Agents on Unseen Zero-Day Vulnerabilities for Cyberdefense](https://arxiv.org/abs/2603.02297v1)** — Lau, Sloot, Raj et al. benchmark frontier agents on 22 novel critical vulnerabilities in open-source codebases. Frontier LLMs can't yet reliably find and patch zero-days — establishing the baseline for where autonomous security actually stands versus the hype.

- **[Graph-GRPO: Stabilizing Multi-Agent Topology Learning via Group Relative Policy Optimization](https://arxiv.org/abs/2603.02701v1)** — Cang, Zhang, Zhao et al. tackle the severe gradient variance in learning communication topologies for multi-agent LLM systems. Single-sample policy gradients with binary rewards provide non-informative signals — GRPO's group-relative baselines stabilize topology optimization in ways that matter for production MAS.

- **[Contextualized Privacy Defense for LLM Agents](https://arxiv.org/abs/2603.02983v1)** — Wen, Zhang, Lian et al. move beyond static privacy defenses to context-aware, step-specific privacy guidance during agent execution. Static rules can't handle the nuanced privacy decisions agents face in multi-step workflows — CDI proactively shapes actions rather than reactively constraining them.

## Multimodal

**14 papers** — unified humanoid multimodal control, multi-agent consistent video generation for shared worlds, visual grounding for web navigation agents, brand integration in text-to-video generation, and geometry-aware continuum robot control via visual self-modeling.

### Highlights

- **[ShareVerse: Multi-Agent Consistent Video Generation for Shared World Modeling](https://arxiv.org/abs/2603.02697v1)** — Zhu, Zhang, Yang et al. tackle the gap in multi-agent shared world construction for video generation. ShareVerse generates consistent multi-view videos across agents interacting in shared environments — the foundation for video world models that understand multi-agent interaction, not just single-camera perspectives.

- **[See and Remember: A Multimodal Agent for Web Traversal](https://arxiv.org/abs/2603.02626v1)** — Wang, Wang, Zhou & Hao introduce V-GEMS, combining visual grounding with explicit memory stacks for web navigation. Spatial disorientation and navigation loops are the failure modes that kill web agents in practice — visual grounding plus state tracking directly addresses both.

- **[APRES: An Agentic Paper Revision and Evaluation System](https://arxiv.org/abs/2603.03142v1)** — Zhao, Zhang, Whitehouse et al. build a multi-agent system that updates scientific papers based on peer review feedback. The system goes beyond generating review responses to actually revising the manuscript — closing the loop from feedback to action in scientific communication.

---

*Tracking 150 papers from March 1–3, 2026. [Source: arXiv](https://arxiv.org/)*
