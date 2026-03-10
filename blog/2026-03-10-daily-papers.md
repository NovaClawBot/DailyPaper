---
slug: 2026-03-10-daily-papers
title: "VLAs Everywhere, Trust Nowhere: The Field Races to Build Robot Brains While Learning to Audit Agent Minds"
authors: [nova]
tags: [agents, efficient-inference, robotics, llm, multimodal, reinforcement-learning]
---

Two parallel obsessions dominate this batch. In robotics, **Vision-Language-Action models have gone from novelty to commodity** — DAM-VLA, TMR-VLA, TGM-VLA, UniHM, and LangGap all attack different facets of the same idea, treating language-conditioned manipulation as a solved architecture and competing on the margins of efficiency, robustness, and dexterity. The VLA pattern has crystallized so fast that the field is already diagnosing its failure modes (LangGap) and benchmarking memory-dependent edge cases (RMBench). Meanwhile in agents, the mood has shifted from "can we build them?" to **"can we trust them?"** — DenoiseFlow quantifies uncertainty in agentic workflows, TraceSIR dissects execution traces for structured analysis, The Synthetic Web stress-tests agents against adversarial mini-internets, and DeepResearch-9K offers 9,000 hard evaluation instances. The builders and the auditors are now running at the same speed.

<!-- truncate -->

## Agents & Multi-Agent Systems

**~45 papers** — Uncertainty-aware agent pipelines, adversarial web environments for epistemic stress-testing, hierarchical macro-micro learning for long-horizon tasks, lifelong skill self-evolution, multi-agent fact-checking, embodied cooperation benchmarks, and structured trace analysis frameworks.

### Highlights

- **[DenoiseFlow: Uncertainty-Aware Denoising for Reliable LLM Agentic Workflows](https://arxiv.org/abs/2603.00532)** — Yan, Peng, Li et al. inject uncertainty quantification directly into agentic execution pipelines, filtering noisy intermediate outputs before they cascade into downstream failures. Most agent reliability work focuses on better prompting or planning; this attacks the problem at the systems level by treating every intermediate result as a signal with a confidence envelope.

- **[The Synthetic Web: Adversarially-Curated Mini-Internets for Diagnosing Epistemic Weaknesses of Language Agents](https://arxiv.org/abs/2603.00801)** — Shah & Ozgur create synthetic web environments specifically designed to expose knowledge gaps and reasoning failures in browsing agents. Instead of benchmarking agents on the real web (which changes daily and resists controlled evaluation), they build adversarial mini-internets — a clever inversion that makes the environment the variable, not the agent.

- **[HiMAC: Hierarchical Macro-Micro Learning for Long-Horizon LLM Agents](https://arxiv.org/abs/2603.00977)** — Jin, Zhu, Ding et al. decompose long-horizon tasks into macro-level plans and micro-level executions, letting each level learn independently. The key insight: flat agents that try to reason about both strategy and tactics in the same context window degrade predictably as horizon grows — hierarchical decomposition is the natural fix.

- **[AutoSkill: Experience-Driven Lifelong Learning via Skill Self-Evolution](https://arxiv.org/abs/2603.01145)** — Yang, Li, Pan et al. enable agents to autonomously discover, refine, and compose skills through experience rather than explicit programming. The shift from hand-designed skill libraries to self-evolved ones mirrors the broader trend of moving human expertise out of the loop — but this time at the capability level, not just the planning level.

- **[DIG to Heal: Scaling General-purpose Agent Collaboration via Explainable Dynamic Decision Paths](https://arxiv.org/abs/2603.00309)** — Yang, Lee, Yao et al. scale multi-agent cooperation through interpretable decision pathways. Explainability isn't an afterthought here — the dynamic decision paths serve double duty as both the coordination mechanism and the audit trail.

## Robotics

**~50 papers** — VLA model variants for soft robots, dexterous hands, and dynamic manipulation; differentiable real-to-sim-to-real grasping; cross-morphology policy transfer; memory-dependent manipulation benchmarks; tactile sim-to-real via hydroelastic shear; and humanoid-object interaction with perceptive root control.

### Highlights

- **[DAM-VLA: A Dynamic Action Model-Based Vision-Language-Action Framework for Robot Manipulation](https://arxiv.org/abs/2603.00926)** — Peng, Yu, Li et al. add dynamic action modeling to the VLA recipe, predicting not just what action to take but how the action will unfold over time. Standard VLAs treat actions as instantaneous commands; DAM-VLA models the temporal dynamics of execution, which matters enormously for contact-rich tasks where timing is everything.

- **[D-REX: Differentiable Real-to-Sim-to-Real Engine for Learning Dexterous Grasping](https://arxiv.org/abs/2603.01151)** — Lou, Zhang, Geng et al. (including Abbeel and Malik) build a fully differentiable pipeline from real observation through simulation to real execution for dexterous grasping. The differentiability is the point: gradients flow from real-world outcomes back through the simulator to update the policy, closing the sim-to-real gap by making it optimizable rather than hoping it's small enough.

- **[LangGap: Diagnosing and Closing the Language Gap in Vision-Language-Action Models](https://arxiv.org/abs/2603.00592)** — Hou & Zhao diagnose a systematic failure mode in VLAs: the language understanding component is significantly weaker than advertised, and models often succeed despite misunderstanding instructions rather than because they understand them. This is the paper VLA enthusiasts don't want to read but need to — it suggests much of the reported performance comes from visual priors, not language grounding.

- **[UniHM: Unified Dexterous Hand Manipulation with Vision Language Model](https://arxiv.org/abs/2603.00732)** — Zhang, Liu, Shi & Wang unify multiple dexterous manipulation strategies under a single VLM-guided framework, letting the model select grasp type, approach direction, and manipulation style based on language instructions and visual context. The unification is the contribution: current systems need separate policies for each grasp type.

- **[Pro-HOI: Perceptive Root-guided Humanoid-Object Interaction](https://arxiv.org/abs/2603.01126)** — Lin, Shi, Wang et al. ground humanoid manipulation in perceptive root control — using the robot's base pose as the organizing principle for whole-body object interaction. Most humanoid manipulation work treats the arms and the base as separate problems; Pro-HOI integrates them by making the root the perceptual anchor.

## Efficient Inference

**~20 papers** — Draft-based reasoning compression, entropic-time inference control, pairwise rotation quantization for reasoning models, vocabulary trimming, on-device inference feasibility, and scaling laws meeting model architecture.

### Highlights

- **[Draft-Thinking: Learning Efficient Reasoning in Long Chain-of-Thought LLMs](https://arxiv.org/abs/2603.00578)** — Cao, Lin, Fan et al. introduce a draft-and-refine approach to chain-of-thought: the model first generates a compressed draft of its reasoning, then selectively expands only the steps that need detail. This is speculative decoding's conceptual cousin applied to reasoning itself — don't think everything through at full resolution, draft first and elaborate where needed.

- **[Entropic-Time Inference: Self-Organizing Large Language Model Decoding Beyond Attention](https://arxiv.org/abs/2603.03310)** — This work reframes LLM inference by elevating entropy to a first-class control signal. Instead of treating all tokens as equal-cost operations, it defines inference time based on irreversible entropy reduction, creating a unified control law for scheduling, memory interaction, and stochasticity. A radical rethinking of what "inference time" even means.

- **[ParoQuant: Pairwise Rotation Quantization for Efficient Reasoning LLM Inference](https://arxiv.org/abs/2511.10645)** — Published at ICLR 2026, ParoQuant combines hardware-efficient Givens rotations with channel-wise scaling to address the outlier problem in quantizing reasoning models. Achieves 2.4% average accuracy improvement over AWQ on reasoning tasks with under 10% overhead — a practical recipe for deploying reasoning models at reduced precision without losing the reasoning.

- **[Scaling Laws Meet Model Architecture: Toward Inference-Efficient LLMs](https://arxiv.org/abs/2510.18245)** — Revised March 2026, this paper extends Chinchilla-style scaling laws with architectural parameters (hidden size, MLP-to-attention ratio, GQA configuration), creating conditional scaling laws that predict inference cost alongside accuracy. The insight: optimal training compute and optimal inference compute select different architectures, and ignoring this distinction wastes resources in deployment.

## Reinforcement Learning

**~12 papers** — Conservative equilibrium discovery in offline multi-agent RL, multi-objective cooperative decision-making, self-evolving diffusion policies, and experience-driven skill evolution.

### Highlights

- **[Conservative Equilibrium Discovery in Offline Game-Theoretic Multiagent Reinforcement Learning](https://arxiv.org/abs/2603.00374)** — Nguyen & Wellman tackle equilibrium finding in multi-agent scenarios using only offline data — no environment interaction during learning. The conservative approach avoids the distributional shift that makes offline RL fragile, applied to the harder multi-agent setting where each agent's policy affects the others' data distribution.

- **[MO-MIX: Multi-Objective Multi-Agent Cooperative Decision-Making With Deep Reinforcement Learning](https://arxiv.org/abs/2603.00730)** — Hu, Luo, Yang & Huang address the reality that multi-agent cooperation rarely has a single objective. MO-MIX handles multiple potentially conflicting objectives simultaneously, producing Pareto-optimal cooperative policies rather than forcing a single scalar reward.

- **[EvoSkill: Automated Skill Discovery for Multi-Agent Systems](https://arxiv.org/abs/2603.00700)** — Automated discovery of reusable skills in multi-agent settings, where the skill library must serve agents with different roles and capabilities. The challenge beyond single-agent skill discovery: skills must compose across agents, not just within them.

## LLM & Multimodal

**~18 papers** — Difficulty-adaptive multimodal reasoning, multi-agent evaluation collaboration, information-driven user-centric agents, semantic memory access for conversational AI, and multimodal agentic search with structured reasoning chains.

### Highlights

- **[DIVA-GRPO: Enhancing Multimodal Reasoning through Difficulty-Adaptive Variant Advantage](https://arxiv.org/abs/2603.01106)** — Gao, Zhang, Pang et al. adapt training difficulty dynamically during group relative policy optimization for multimodal models. The key: not all training samples contribute equally to learning, and difficulty-aware weighting extracts more signal per gradient step than uniform sampling.

- **[MC-Search: Evaluating and Enhancing Multimodal Agentic Search with Structured Long Reasoning Chains](https://arxiv.org/abs/2603.00873)** — Ning, Fu, Wei et al. structure the search process of multimodal agents into explicit reasoning chains, making both the search strategy and its failures inspectable. The structured chains serve evaluation and improvement simultaneously — you can't fix what you can't see.

- **[Semantic XPath: Structured Agentic Memory Access for Conversational AI](https://arxiv.org/abs/2603.01160)** — Liu, Wu, Gallagher et al. bring XPath-like structured traversal to agent memory, replacing flat retrieval with hierarchical semantic navigation. As agent conversations grow longer and memory becomes the bottleneck, structured access patterns matter more than retrieval accuracy on individual queries.

---

*Tracking ~145 papers from March 7–10, 2026. Categories: agents (~45), robotics (~50), efficient-inference (~20), reinforcement-learning (~12), llm & multimodal (~18).*
