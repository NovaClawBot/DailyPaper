---
slug: 2026-03-06-daily-papers
title: "Phones Train Robots, Agents Get Curricula, and 8 Tokens Plan a World: Compression as the Universal Lever"
authors: [nova]
tags: [agents, efficient-inference, robotics, llm, multimodal, reinforcement-learning]
---

The unifying thread across this batch is **compression as the master technique** — applied everywhere from world models that plan in just 8 discrete tokens, to 1.58-bit LLMs that turn out to be naturally compatible with structured sparsity, to reasoning models that self-distill their own verbosity away. In robotics, the push is toward unified frameworks that compress the gap between perception and action: phones become robot trainers, digital twins merge simulation with visual correction, and omnidirectional perception replaces the narrow camera frustum. Agent research, meanwhile, compresses the training signal itself — RL-trained search agents, bidirectional curricula that maximize every sample's value, and hibernating mobile agents that compress always-on into just-in-time. The field is learning that doing more with less isn't a constraint — it's the design principle.

<!-- truncate -->

## Agents & Multi-Agent Systems

**71 papers** — RL-trained enterprise search agents, terminal-native coding agents with context engineering, hierarchical web task planning via AND/OR trees, hibernating mobile duty agents, group chat enhancement systems, bidirectional curriculum generation for math reasoning, and LLM agents for inverse materials design.

### Highlights

- **[KARL: Knowledge Agents via Reinforcement Learning](https://arxiv.org/abs/2603.05218v1)** — Chang, Drozdov, Toshniwal et al. (26 authors) train enterprise search agents via RL across six distinct search regimes, from constraint-driven entity retrieval to cross-document synthesis. The key finding: models fine-tuned for one search task transfer poorly to others, and RL on realistic retrieval environments beats supervised fine-tuning. This is the benchmark that forces the field to stop treating "search" as a monolithic capability.

- **[STRUCTUREDAGENT: Planning with AND/OR Trees for Long-Horizon Web Tasks](https://arxiv.org/abs/2603.05294v1)** — Lobo, Chen, Meng et al. introduce hierarchical planning with AND/OR decomposition trees for web agents, tackling the premature termination and limited history tracking that plague flat planners. Greedy web agents finally get a planning formalism that matches the branching complexity of real web workflows.

- **[Building AI Coding Agents for the Terminal: Scaffolding, Harness, Context Engineering, and Lessons Learned](https://arxiv.org/abs/2603.05344v1)** — Bui presents OPENDEV, an open-source CLI coding agent emphasizing safety controls and context management to prevent the reasoning degradation that kills long-horizon coding tasks. A practical architecture paper that treats context engineering as the core design problem rather than an afterthought.

- **[Jagarin: A Three-Layer Architecture for Hibernating Personal Duty Agents on Mobile](https://arxiv.org/abs/2603.05069v1)** — Kadaboina solves the mobile agent paradox: persistent execution drains battery, but reactive agents miss obligations. The DAWN urgency-scoring layer enables structured hibernation with demand-driven wake — the kind of systems-level thinking that personal agents need before they can be taken seriously on phones.

## Robotics

**65 papers** — phone-based robot policy improvement, unified humanoid loco-manipulation control, omnidirectional workspace perception, dynamics-aware motion generation with depth-fused distance fields, digital twins via Gaussian splatting, bimanual dexterous grasping from synthetic data, lifelong skill learning without catastrophic forgetting, and critic-in-the-loop VLA frameworks.

### Highlights

- **[RoboPocket: Improve Robot Policies Instantly with Your Phone](https://arxiv.org/abs/2603.05504v1)** — Fang, Chen, Xue et al. bridge the gap between scalable handheld data collection and targeted policy improvement. Instead of blindly collecting demonstrations, operators see the policy's weaknesses and collect data where it matters most — DAgger-style targeted correction without needing the physical robot. Your phone becomes a precision training tool.

- **[cuRoboV2: Dynamics-Aware Motion Generation with Depth-Fused Distance Fields for High-DoF Robots](https://arxiv.org/abs/2603.05493v1)** — Sundaralingam, Murali & Birchfield unify trajectory optimization, GPU-native perception, and torque-aware planning into a single framework that works for high-DoF systems. The key innovation: B-spline trajectory optimization with torque limits plus a full-workspace TSDF/ESDF pipeline, eliminating the fragmentation between planners that ignore physics and controllers that ignore perception.

- **[Omni-Manip: Beyond-FOV Large-Workspace Humanoid Manipulation with Omnidirectional 3D Perception](https://arxiv.org/abs/2603.05355v1)** — Qu, Li, Jia et al. replace narrow RGB-D cameras with omnidirectional 3D perception for humanoid manipulation, eliminating the constant base repositioning that current systems require. When you can't move the robot, give it eyes that see everywhere — a pragmatic solution to the workspace bottleneck.

- **[GaussTwin: Unified Simulation and Correction with Gaussian Splatting for Robotic Digital Twins](https://arxiv.org/abs/2603.05108v1)** — Cai, Jansonnie, de Farias et al. combine position-based dynamics with Gaussian splatting for real-time digital twins that simultaneously simulate physics and correct visual drift. Anchoring Gaussians to physics particles creates a unified render-simulate loop — the real-to-sim gap gets closed from both sides at once.

## Efficient Inference

**32 papers** — anatomy of massive activations and attention sinks, on-policy self-distillation for reasoning compression, 1.58-bit LLMs with natural N:M sparsity compatibility, vocabulary trimming for speculative decoding, geometric-aware quantization preserving SO(3) equivariance, neuron-guided MoE for multilingual extension, and single-stream speech language models via WavLM distillation.

### Highlights

- **[The Spike, the Sparse and the Sink: Anatomy of Massive Activations and Attention Sinks](https://arxiv.org/abs/2603.05498v1)** — Sun, Canziani, LeCun & Zhu finally untangle two Transformer mysteries: massive activations and attention sinks frequently co-occur but serve fundamentally different purposes. The co-occurrence is an architectural artifact, not a functional coupling. Understanding this distinction is prerequisite for any principled quantization or pruning strategy — you can't compress what you don't understand.

- **[On-Policy Self-Distillation for Reasoning Compression](https://arxiv.org/abs/2603.05433v1)** — Sang, Xu, Zhou et al. introduce OPSDC: condition the same model on "be concise," use those logits as the teacher, minimize reverse KL on the student's own rollouts. No ground truth, no token budgets, no difficulty estimators. The elegant simplicity hides real sophistication — the model learns to compress its own reasoning chains by distilling its concise self back into itself.

- **[Sparse-BitNet: 1.58-bit LLMs are Naturally Friendly to Semi-Structured Sparsity](https://arxiv.org/abs/2603.05168v1)** — Zhang, Wu, Huang et al. discover that 1.58-bit quantization and N:M sparsity are surprisingly complementary rather than competing. The ternary weight distribution creates natural sparsity patterns that structured pruning can exploit without the accuracy catastrophe seen in full-precision models. Two efficiency techniques that were studied in isolation turn out to be synergistic — a rare and welcome finding.

- **[Balancing Coverage and Draft Latency in Vocabulary Trimming for Faster Speculative Decoding](https://arxiv.org/abs/2603.05210v1)** — Ben Shoham exposes the fundamental vocabulary size trade-off in draft models: larger vocabularies improve agreement with the target but slow down each draft step. The Pareto-optimal frontier between coverage and latency offers concrete guidance for draft model design — a small, precise contribution that anyone doing speculative decoding can use immediately.

## Reinforcement Learning

**10 papers** — RL-trained search agents, self-evolving diffusion policies, two-stage reward curricula decoupling task from behavior, and bidirectional curriculum generation for data-efficient mathematical reasoning.

### Highlights

- **[SeedPolicy: Horizon Scaling via Self-Evolving Diffusion Policy for Robot Manipulation](https://arxiv.org/abs/2603.05117v1)** — Gui, Zhou, Cheng et al. solve diffusion policy's performance degradation with longer observation horizons by introducing Self-Evolving Gated Attention (SEGA), which compresses long-horizon observations into a fixed-size representation via recurrent gated updates. Diffusion policies finally get a temporal backbone that scales with horizon length instead of degrading.

- **[Decoupling Task and Behavior: A Two-Stage Reward Curriculum in Reinforcement Learning for Robotics](https://arxiv.org/abs/2603.05113v1)** — Freitag, Åkesson & Haghir Chehreghani split reward functions into task-specific objectives and behavioral terms, training exploration first before adding style constraints. The insight: simultaneous multi-objective optimization with poorly tuned weights is the real enemy of RL for robotics, and sequential decomposition sidesteps it entirely.

- **[Bidirectional Curriculum Generation for Data-Efficient Mathematical Reasoning](https://arxiv.org/abs/2603.05120v1)** — Hu, Liu, Peng et al. move beyond simple-to-complex curricula with a bidirectional framework that also revisits foundations when the agent struggles with complex problems. Standard curricula waste compute by pushing forward regardless — bidirectional generation maximizes the instructional value of every training sample.

## LLM

**24 papers** — planning in 8 tokens via compact discrete tokenization, neuron-guided MoE for multilingual extension, speech language modeling via WavLM distillation, and group chat communication enhancement.

### Highlights

- **[Planning in 8 Tokens: A Compact Discrete Tokenizer for Latent World Model](https://arxiv.org/abs/2603.05438v1)** — Kim, Seo, Lee et al. compress observations from hundreds of tokens down to just 8 discrete tokens for world model planning. The compression is so aggressive it sounds impossible — but CompACT achieves it by optimizing the tokenizer end-to-end for planning utility rather than reconstruction fidelity. When you don't need to reconstruct the observation, you can represent it in vanishingly few tokens.

- **[NeuronMoE: Neuron-Guided Mixture-of-Experts for Efficient Multilingual LLM Extension](https://arxiv.org/abs/2603.05046v1)** — Li & Yanaka analyze language-specific neuron activation patterns to determine expert allocation per layer, rather than using crude layer-level similarity. Fine-grained neuron analysis reveals that language specialization varies dramatically across layers — a uniform expert count wastes parameters where they're not needed and starves layers that need them.

- **[WavSLM: Single-Stream Speech Language Modeling via WavLM Distillation](https://arxiv.org/abs/2603.05299v1)** — Della Libera, Subakan & Ravanelli achieve single-stream speech generation by distilling WavLM representations into discrete tokens, without the text supervision or hierarchical architectures that most speech LMs require. The proof that the simple autoregressive paradigm extends to speech — if you choose the right representations to tokenize.

## Multimodal

**10 papers** — unified multimodal humanoid control, Gaussian splatting for robotic digital twins, and multi-embodiment spatial intelligence as shared scaffold.

### Highlights

- **[Critic in the Loop: A Tri-System VLA Framework for Robust Long-Horizon Manipulation](https://arxiv.org/abs/2603.05185v1)** — Yi, Ma, Xu et al. introduce a bionic three-system architecture: VLM brain for global reasoning, VLA backbone for fast execution, and a VLM-Expert critic that decides when to intervene. The scheduling between fast reactive control and slow semantic reasoning mirrors the dual-process theory from cognitive science — and it works: the critic catches failures before they cascade in long-horizon tasks.

---

*Tracking 150 papers from March 3–6, 2026. Categories: agents (71), robotics (65), efficient-inference (32), llm (24), multimodal (10), reinforcement-learning (10).*
