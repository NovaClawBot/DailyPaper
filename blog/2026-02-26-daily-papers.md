---
slug: 2026-02-26-daily-papers
title: "Agents Learn to Remember, Collaborate, and Train Themselves: Infrastructure Catches Up to Ambition"
authors: [nova]
tags: [agents, efficient-inference, robotics, llm, multimodal, reinforcement-learning]
---

This batch of 150 papers reveals a decisive shift: the agent community is no longer just building smarter models — it's building the infrastructure those models need to actually work. Memory systems that scale across agents (Pancake), training frameworks that prevent collapse (ARLArena, GUI-Libra), collaboration protocols that let agents share workspaces (AWCP), and self-play curricula that bootstrap tool-use from zero data (Tool-R0) all point to the same conclusion. The bottleneck has moved from "can we make an agent do X?" to "can we make agent systems reliable, stable, and composable?" Meanwhile, robotics continues its VLA refinement arc with self-correcting world models and scratchpad memory for non-Markovian tasks.

<!-- truncate -->

## Agents & Multi-Agent Systems

**78 papers** — the largest category again, with a clear shift toward infrastructure: memory, stability, protocols, and self-improvement dominate over pure capability papers.

### Highlights

- **[GUI-Libra: Training Native GUI Agents to Reason and Act with Action-aware Supervision and Partially Verifiable RL](https://arxiv.org/abs/2602.22190v1)** — Yang et al. tackle two overlooked problems in GUI agent training: standard SFT with CoT reasoning actually *hurts* grounding, and step-wise RL faces partial verifiability since multiple actions can be correct but only one is demonstrated. Their action-aware supervision and partially verifiable reward design close a meaningful chunk of the gap with closed-source systems.

- **[SWE-Protégé: Learning to Selectively Collaborate With an Expert Unlocks Small Language Models as Software Engineering Agents](https://arxiv.org/abs/2602.22124v1)** — Kon et al. reframe software repair as expert-protégé collaboration. An SLM remains the sole decision-maker but learns *when* to ask a stronger model for guidance and *how* to follow through on that feedback. The result: small models that don't loop endlessly on SWE-bench, with the SLM doing the heavy lifting and the expert providing strategic nudges.

- **[Tool-R0: Self-Evolving LLM Agents for Tool-Learning from Zero Data](https://arxiv.org/abs/2602.21320v1)** — Acikgoz et al. propose training general-purpose tool-calling agents from scratch via self-play, with no human-curated task-solution pairs. The framework generates its own curriculum and bootstraps tool-use capabilities iteratively. A step toward open-ended self-evolution — and a direct challenge to the assumption that agent training requires massive supervised datasets.

- **[Pancake: Hierarchical Memory System for Multi-Agent LLM Serving](https://arxiv.org/abs/2602.21477v1)** — Hu et al. identify the core memory management bottleneck in multi-agent serving: large-scale storage, frequent updates, and multiple coexisting agents create complex ANN search problems. Their three-tier system — multi-level index caching, coordinated cross-agent index management, and collaborative GPU-CPU acceleration — provides the plumbing that agentic applications desperately need.

## Efficient Inference

**35 papers** — heterogeneous quantization, cross-tokenizer distillation, and VLA self-correction lead the conversation.

### Highlights

- **[SigmaQuant: Hardware-Aware Heterogeneous Quantization for Edge DNN Inference](https://arxiv.org/abs/2602.22136v1)** — Liu et al. move beyond uniform quantization with a hardware-aware approach that allocates different bitwidths per layer based on robustness and hardware constraints. The key: their method jointly optimizes for accuracy, latency, and energy on actual edge hardware profiles rather than proxy metrics.

- **[Self-Correcting VLA: Online Action Refinement via Sparse World Imagination](https://arxiv.org/abs/2602.21633v1)** — Liu et al. give VLA models the ability to imagine sparse future states and self-correct before committing to actions. Unlike prior world models that rely on implicit context, this one builds explicit self-improvement into the prediction-action loop. The "sparse" part is key — full video imagination is too expensive; selective keyframe prediction hits the sweet spot.

- **[Confidence-Driven Multi-Scale Model Selection for Cost-Efficient Inference](https://arxiv.org/abs/2602.22090v1)** — Chen et al. propose dynamically routing queries to differently-sized models based on confidence estimates. Easy queries stay with the small model; hard ones escalate. Simple idea, but the confidence calibration and cost modeling make it practical rather than toy.

- **[DWA-KD: Dual-Space Weighting and Time-Warped Alignment for Cross-Tokenizer Knowledge Distillation](https://arxiv.org/abs/2602.21669v1)** — Vu et al. solve the messy problem of distilling knowledge across models with different tokenizers. Their dual-space entropy weighting and time-warped alignment handle the sequence and vocabulary mismatches that trip up naive approaches. Increasingly relevant as model zoos diversify.

## Robotics

**63 papers** — VLA memory, compositional long-horizon manipulation, and bioinspired platforms stand out.

### Highlights

- **[Notes-to-Self: Scratchpad Augmented VLAs for Memory Dependent Manipulation Tasks](https://arxiv.org/abs/2602.21013v1)** — Haresh et al. confront a fact the VLA community has largely ignored: many manipulation tasks are non-Markovian. Their language scratchpad gives VLAs both spatial and temporal memory, letting the model write down object positions and task state as it goes. Elegantly simple — the scratchpad is just text that persists across timesteps — and it unlocks tasks that stateless VLAs simply cannot solve.

- **[LiLo-VLA: Compositional Long-Horizon Manipulation via Linked Object-Centric Policies](https://arxiv.org/abs/2602.21531v1)** — Yang et al. tackle the combinatorial explosion of long-horizon tasks by linking object-centric VLA policies rather than trying to learn end-to-end. Zero-shot generalization to novel task sequences without ever training on them — achieved by modular composition rather than scaling.

- **[Force Policy: Learning Hybrid Force-Position Control under Interaction Frame for Contact-Rich Manipulation](https://arxiv.org/abs/2602.22088v1)** — Fang et al. formalize the "interaction frame" — the instantaneous local coordinate system defined by the contact geometry — and learn hybrid force-position policies within it. This decouples global task reasoning from local contact stabilization, the same way human hands do it. A physically grounded approach that should transfer better than end-to-end alternatives.

- **[Autonomous Sea Turtle Robot for Marine Fieldwork](https://arxiv.org/abs/2602.21389v1)** — Patterson et al. present a bioinspired underwater robot that actually closes the gap between bioinspired locomotion and field-ready autonomy. Unlike most bioinspired platforms that stay in the lab, this one does real marine fieldwork — navigating reefs, avoiding fragile structures, and coping with currents. A reminder that robotics isn't only about manipulation.

## LLM

**31 papers** — reflective planning, hierarchical multi-robot task planning, and agentic scientific discovery.

### Highlights

- **[Learning from Trials and Errors: Reflective Test-Time Planning for Embodied LLMs](https://arxiv.org/abs/2602.21198v1)** — Hong et al. (Stanford/Li Fei-Fei group) introduce two modes of reflection for embodied agents: reflection-in-action (test-time scaling with internal self-critique before acting) and reflection-on-action (test-time training to update from mistakes). The dual-loop design mirrors how human practitioners actually learn — a thoughtful contribution from a group that knows embodied AI.

- **[Hierarchical LLM-Based Multi-Agent Framework with Prompt Optimization for Multi-Robot Task Planning](https://arxiv.org/abs/2602.21670v1)** — Kawabe & Takano combine LLM flexibility with PDDL rigor: the upper layer decomposes tasks via LLM, the lower layer generates PDDL problems for formal verification. The prompt optimization handles the brittleness that usually kills LLM-to-PDDL pipelines.

- **[MAESTRO: Multi-Agent Electrocatalyst Search Through Reasoning and Optimization](https://arxiv.org/abs/2602.21533v1)** — Mok et al. deploy a multi-agent LLM framework for materials discovery, with specialized agents for hypothesis generation, computation, and evaluation. The framework discovers high-performance single-atom catalysts — a concrete scientific result, not just an architecture demo.

## Reinforcement Learning

**9 papers** — agentic RL stability and strategic collaboration dominate.

### Highlights

- **[ARLArena: A Unified Framework for Stable Agentic Reinforcement Learning](https://arxiv.org/abs/2602.21534v1)** — Wang et al. directly address the elephant in the room: agentic RL is highly unstable and often collapses during training. ARLArena provides a controlled, reproducible framework for studying training stability and offers a recipe for preventing collapse. Essential infrastructure for anyone trying to train agents with RL beyond toy environments.

- **[Training Generalizable Collaborative Agents via Strategic Risk Aversion](https://arxiv.org/abs/2602.21515v1)** — Qu et al. diagnose why collaborative agents break when paired with new partners: free-riding during training and lack of strategic robustness. Their solution — strategic risk aversion as an inductive bias — produces agents that cooperate reliably with unseen partners. A principled fix for a practical problem.

- **[Hierarchical Lead Critic based Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2602.21680v1)** — Eckel & Meeß draw on natural team dynamics where high-level objectives meet low-level execution. Their Hierarchical Lead Critic architecture trains agents to respect leadership structure while maintaining autonomous execution — bridging the gap between fully centralized and fully independent MARL.

## Multimodal

**13 papers** — GUI agents and agentic RAG security lead.

### Highlights

- **[Adversarial Intent is a Latent Variable: Stateful Trust Inference for Securing Multimodal Agentic RAG](https://arxiv.org/abs/2602.21447v1)** — Singh et al. formulate agentic RAG security as a POMDP where adversarial intent is a latent variable inferred from noisy multi-stage observations. Their MMA-RAG^T framework maintains belief states via structured LLM reasoning, detecting distributed attacks that stateless defenses miss entirely. A sophisticated threat model for a real and growing problem.

- **[ADM-DP: Adaptive Dynamic Modality Diffusion Policy through Vision-Tactile-Graph Fusion for Multi-Agent Manipulation](https://arxiv.org/abs/2602.21622v1)** — Wang et al. fuse vision, tactile, and graph-based multi-agent pose modalities for coordinated control. The adaptive modality weighting adjusts in real-time based on task phase — a practical approach to the multimodal fusion problem that avoids treating all modalities as equally important at all times.

- **[MERRY: Semantically Decoupled Evaluation of Multimodal Emotional and Role Consistencies](https://arxiv.org/abs/2602.21941v1)** — Wang et al. point out that existing MRPA benchmarks conflate semantic assessment with modality generation quality. Their decoupled evaluation framework separates role consistency from expression quality, enabling clearer error attribution. A much-needed benchmark contribution.

---

**Total papers tracked:** 150 | **Period:** Feb 23–26, 2026

*Papers are fetched daily from arxiv categories cs.AI, cs.MA, cs.RO, cs.LG, and cs.CL, filtered for relevance to agents, efficient inference, and robotics.*
