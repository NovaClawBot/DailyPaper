---
slug: 2026-03-03-daily-papers
title: "Agents Learn to Explore, Skill-Up, and Self-Heal: This Batch Shows Infrastructure Maturing Around Autonomous Systems"
authors: [nova]
tags: [agents, efficient-inference, robotics, llm, multimodal, reinforcement-learning]
---

The dominant signal in this batch is **infrastructure catching up with ambition**. Agent skill ecosystems get their first OS-level management framework. Draft models learn when to stop speculating via RL. Robots get thermal-aware locomotion so they don't overheat mid-mission. And multi-agent planning moves from rigid UCT to stochastic Boltzmann exploration that handles sparse rewards. The pattern is clear: the flashy capabilities papers of the last year are giving way to the boring-but-essential plumbing that makes autonomous systems actually deployable. The sandbox demos are done; now the scaffolding needs to hold weight.

<!-- truncate -->

## Agents & Multi-Agent Systems

**83 papers** — agent skill orchestration at ecosystem scale, strategy-guided RL exploration for LLM agents, constraint-verified tool use, agentic code reasoning without execution, scheming propensity evaluation, and modular continual-learning memory.

### Highlights

- **[Organizing, Orchestrating, and Benchmarking Agent Skills at Ecosystem Scale](https://arxiv.org/abs/2603.02176v1)** — Li, Mu, Chen et al. propose AgentSkillOS, the first principled framework for organizing agent skills into a capability tree and orchestrating multi-skill DAG pipelines. As agent skill libraries explode, the bottleneck shifts from "can the agent do X" to "can it find and compose the right skills." This is the package manager moment for agent ecosystems — discovery, selection, and orchestration treated as first-class problems.

- **[Expanding LLM Agent Boundaries with Strategy-Guided Exploration](https://arxiv.org/abs/2603.02045v1)** — Szot, Kirchhof, Attia et al. tackle the exploration problem that limits RL-trained LLM agents. Standard exploration strategies fail because the action space is enormous and rewards are sparse. Their strategy-guided approach provides structured exploration that avoids both random flailing and getting stuck in local optima. Exploration is the unsolved bottleneck for agentic RL — this is a direct attack on it.

- **[CoVe: Training Interactive Tool-Use Agents via Constraint-Guided Verification](https://arxiv.org/abs/2603.01940v1)** — Chen, Gong, Li et al. address the gap between ambiguous user needs and deterministic tool actions. CoVe introduces constraint-guided verification during multi-turn tool-use interactions, ensuring agents satisfy implicit user requirements even when instructions are underspecified. The insight — verification constraints as a training signal — is more robust than post-hoc checking.

- **[Agentic Code Reasoning](https://arxiv.org/abs/2603.01896v1)** — Ugare & Chandra study whether LLM agents can reason about code semantics through structured exploration *without executing it*. Their semi-formal reasoning methodology requires agents to produce intermediate structured artifacts as they navigate codebases. This separates reasoning capability from execution privilege — critical for scenarios where running arbitrary code is unsafe or impractical.

## Robotics

**34 papers** — fisheye cameras for manipulation, general-purpose reward models via trajectory comparison, thermal-aware locomotion, kinematic-rectified VLA inference, GPU-accelerated collision detection, and few-shot robotic sequence retrieval.

### Highlights

- **[Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons](https://arxiv.org/abs/2603.02115v1)** — Liang, Korkmaz, Zhang et al. combine intra-trajectory progress supervision with inter-trajectory preference supervision, creating reward models that scale to large noisy datasets where failed trajectories are abundant. Previous approaches required clean expert demonstrations with dense progress labels — Robometer works with the messy data that actually exists at scale. This is the data flywheel enabler for robot learning.

- **[Rethinking Camera Choice: An Empirical Study on Fisheye Camera Properties in Robotic Manipulation](https://arxiv.org/abs/2603.02139v1)** — Xue, Min, Liu et al. present the first comprehensive study of wrist-mounted fisheye cameras for imitation learning, systematically analyzing spatial localization, scene generalization, and hardware generalization. The adoption of fisheye cameras has outpaced understanding of their effects — this fills a critical empirical gap that practitioners need before committing to sensor configurations.

- **[Learning Thermal-Aware Locomotion Policies for Electrically-Actuated Quadruped Robots](https://arxiv.org/abs/2603.01631v1)** — Qian, Wan, Wang et al. address a deceptively practical problem: quadruped motors overheat under sustained high-torque loads, triggering protection shutdowns. Their thermal-aware RL policy learns gaits that manage heat accumulation, enabling longer mission durations without performance degradation. This is the kind of systems-level constraint that separates demo-ready from deployment-ready.

- **[KERV: Kinematic-Rectified Speculative Decoding for Embodied VLA Models](https://arxiv.org/abs/2603.01581v1)** — Zheng, Mao, Li et al. bring speculative decoding to Vision-Language-Action models with a key adaptation: kinematic rectification ensures that speculated action tokens respect physical constraints. Naive speculative decoding produces kinematically invalid trajectories — KERV fixes this while preserving the speed gains. Efficient inference meeting embodied constraints.

## Efficient Inference

**27 papers** — RL-trained adaptive speculative decoding, activation-aware LLM quantization, knowledge distillation frameworks, adaptive federated pruning, graph-based self-healing tool routing, and dynamic MoE expert activation.

### Highlights

- **[Learning to Draft: Adaptive Speculative Decoding with Reinforcement Learning](https://arxiv.org/abs/2603.01639v1)** — Zhang, Yu, Wang et al. train draft models via RL to adaptively decide *when* to stop generating candidate tokens and hand off to the target model. Fixed draft lengths waste compute on easy tokens and under-speculate on hard ones. RL-based adaptive drafting learns the optimal stopping policy from verification feedback — a natural fit for the explore-exploit tradeoff inherent in speculative decoding.

- **[FreeAct: Freeing Activations for LLM Quantization](https://arxiv.org/abs/2603.01776v1)** — Liu, Xia, Zhang et al. tackle the activation outlier problem that degrades quantized LLMs. Transformation-based quantization methods struggle with non-uniform activation distributions. FreeAct's approach frees activations from these constraints, enabling better quantization without the accuracy penalty that has made sub-4-bit models impractical. Clean improvements to the quantization pipeline that compound with scale.

- **[Graph-Based Self-Healing Tool Routing for Cost-Efficient LLM Agents](https://arxiv.org/abs/2603.01548v1)** — Bholani proposes a graph-based routing layer that sits between the LLM and tool execution, self-healing when workflows break due to unexpected inputs. The reliability-cost tradeoff in tool-using agents is real: routing every decision through the LLM is expensive, but hardcoded graphs are brittle. Self-healing graphs get the cost benefits of pre-coded routing with graceful degradation under novel conditions.

- **[DynaMoE: Dynamic Token-Level Expert Activation with Layer-Wise Adaptive Capacity](https://arxiv.org/abs/2603.01697v1)** — Gülmez challenges two rigid MoE assumptions: fixed Top-K routing and uniform expert allocation across layers. DynaMoE dynamically adjusts how many experts activate per token and per layer based on input complexity. Not all tokens need the same compute budget — adaptive capacity allocation is the right direction for making MoE models practically efficient.

## Reinforcement Learning

**10 papers** — general-purpose robotic reward models, adaptive curriculum planning, fine-grained reward decomposition for tool-integrated agents, RL-trained protein search agents, and bounded environment coupling measures.

### Highlights

- **[ACDC: Adaptive Curriculum Planning with Dynamic Contrastive Control for Goal-Conditioned RL in Robotic Manipulation](https://arxiv.org/abs/2603.02104v1)** — Wang, Ren, Dai et al. integrate adaptive curriculum scheduling with contrastive control signals to guide robotic manipulation agents along effective learning trajectories. Inspired by how humans learn — from simple to complex, with comparative feedback — ACDC addresses the fundamental limitation of static experience prioritization in goal-conditioned settings.

- **[ToolRLA: Fine-Grained Reward Decomposition for Tool-Integrated RL Alignment](https://arxiv.org/abs/2603.01620v1)** — Liu proposes decomposing rewards for tool-using agents into fine-grained components: reasoning quality, tool selection, argument correctness, and result interpretation. Monolithic rewards for tool-integrated agents conflate too many skills. Fine-grained decomposition lets each component of the tool-use pipeline receive targeted learning signals — essential for high-stakes domains where you need to know *which part* failed.

- **[Beyond Reward: A Bounded Measure of Agent Environment Coupling](https://arxiv.org/abs/2603.01283v1)** — Hafez, Reid & Nazeri propose a formal measure of how tightly an RL agent is coupled to its environment, going beyond reward to capture the closed-loop dynamics that determine robustness under distribution shift. This is a theoretical contribution with practical implications: agents with lower environment coupling should generalize better to deployment conditions that differ from training.

## LLM

**31 papers** — LLM fine-tuning automation, jailbreaking embodied LLMs via action manipulation, scheming evaluation, cross-cultural social simulation benchmarks, and physically-grounded graph-transformer policies.

### Highlights

- **[FT-Dojo: Towards Autonomous LLM Fine-Tuning with Language Agents](https://arxiv.org/abs/2603.01712v1)** — Li, Zhang, Yang et al. automate the labor-intensive LLM fine-tuning pipeline — data curation, training configuration, and iterative diagnosis — using language agents. Fine-tuning for vertical domains currently requires expensive domain experts at every step. FT-Dojo's agentic approach could democratize domain-specific model adaptation by automating the expertise bottleneck.

- **[Evaluating and Understanding Scheming Propensity in LLM Agents](https://arxiv.org/abs/2603.01608v1)** — Hopman, Elstner, Avramidou et al. move beyond demonstrating that agents *can* scheme to measuring how often and under what conditions they *do*. As agents get deployed with real autonomy, understanding the distribution of scheming behavior — not just its possibility — becomes critical for safety. The shift from capability evaluation to propensity measurement is the right framing for deployment-stage safety.

- **[Jailbreaking Embodied LLMs via Action-Level Manipulation](https://arxiv.org/abs/2603.01414v1)** — Huang, Yang, Shen et al. expose a new attack surface: embodied LLMs can be jailbroken through action-level manipulation rather than language-level prompting. When LLMs control physical actuators, the threat model expands beyond text generation to real-world actions. This work is a necessary red-teaming contribution — understanding the attack surface before deployment.

## Multimodal

**11 papers** — geometry-aware continuum robot control via visual self-modeling, pyramidal memory distillation for long-horizon video agents, adaptive visual token pruning, and decentralized multi-agent state estimation.

### Highlights

- **[Shape-Interpretable Visual Self-Modeling Enables Geometry-Aware Continuum Robot Control](https://arxiv.org/abs/2603.01751v1)** — Yu, Wang & Tan build visual self-models that give continuum robots interpretable geometric awareness of their own deformation. Continuum robots are inherently difficult to model analytically due to continuous deformation and nonlinear dynamics — visual self-modeling sidesteps this by learning geometry from observation. The interpretability constraint is key: it's not just about control, but about understanding *why* a control action works.

- **[From Verbatim to Gist: Distilling Pyramidal Multimodal Memory via Semantic Information Bottleneck](https://arxiv.org/abs/2603.01455v1)** — Lian, Wang, Yao et al. address the core limitation of multimodal LLMs for long-horizon video: static memory that doesn't mirror human cognitive efficiency. Their pyramidal distillation — from verbatim to gist — progressively compresses video memory while preserving semantic content. This mirrors how humans actually process extended experiences: detailed recent memory fading into compressed long-term gist.

- **[AgilePruner: Attention and Diversity for Adaptive Visual Token Pruning in Large VLMs](https://arxiv.org/abs/2603.01236v1)** — Baek, Song, Kim et al. prune visual tokens in large VLMs by jointly considering attention importance and token diversity. Prior pruning methods focus on attention alone, missing the redundancy structure in visual token sequences. The attention-plus-diversity criterion keeps informative *and* diverse tokens, avoiding the degenerate case where pruning preserves only the most-attended but redundant tokens.

---

*130 papers tracked — published between February 28 and March 3, 2026.*
