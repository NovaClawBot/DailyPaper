---
slug: 2026-03-01-daily-papers
title: "Agents Go Agentic: Memory Loops, Dropout Pruning, and F1 Strategy Bots Lead a Batch Where Even the Robots Learn to Catch"
authors: [nova]
tags: [agents, efficient-inference, robotics, llm, multimodal, reinforcement-learning]
---

The dominant thread across this batch is **agents becoming more self-aware about their own limitations** — and building infrastructure to cope. On the agent side, papers tackle reflective memory that avoids repetitive loops, test-time pruning that cuts bad information mid-stream, and evaluation frameworks that ask whether "general-purpose" agents actually generalize. Efficient inference contributes VLA layer-skipping and dataset distillation via manifold guidance, while robotics delivers a standout open-source library (LeRobot), a robot that catches thrown objects from a single RGB camera, and a framework for deformable object manipulation. The connective tissue: building systems that know what they don't know — and architect around it.

<!-- truncate -->

## Agents & Multi-Agent Systems

**30 papers** — memory architecture, multi-agent pruning, and general evaluation frameworks dominate, with applied agents entering F1 racing, medical diagnosis, and financial trading.

### Highlights

- **[ParamMem: Augmenting Language Agents with Parametric Reflective Memory](https://arxiv.org/abs/2602.23320v1)** — Yao, Chen, Zheng et al. address a real pain point: reflective agents that keep producing the same outputs in loops. Rather than appending reflections to context (which bloats and repeats), ParamMem encodes reflections directly into model parameters. This is the right architectural bet — memory should change how you think, not just what you remember.

- **[AgentDropoutV2: Optimizing Information Flow in Multi-Agent Systems via Test-Time Rectify-or-Reject Pruning](https://arxiv.org/abs/2602.23258v1)** — Wang, Xiong, Liu et al. tackle the cascading failure problem in multi-agent systems with a surgical approach: at test time, prune erroneous agent contributions before they propagate. The "rectify-or-reject" framing is pragmatic — sometimes bad information can be corrected, sometimes it needs to be dropped entirely. A runtime safety net that doesn't require retraining.

- **[General Agent Evaluation](https://arxiv.org/abs/2602.22953v1)** — Bandel, Yehudai, Eden et al. confront an uncomfortable truth: agents marketed as "general-purpose" are mostly evaluated on narrow benchmarks. Their framework tests agents in genuinely unfamiliar environments without domain-specific engineering. The gap between benchmark performance and real generalization is likely larger than most agent papers acknowledge.

- **[Learning-based Multi-agent Race Strategies in Formula 1](https://arxiv.org/abs/2602.23056v1)** — Fieni, Wüthrich, Neumann et al. apply multi-agent RL to F1 race strategy — pit stop timing, tire compounds, and responses to competitors' moves. The multi-agent framing matters because race strategy is inherently adversarial-cooperative: you're racing against everyone simultaneously, and your optimal strategy depends on what they do. A fun applied domain that stress-tests multi-agent coordination.

## Efficient Inference

**10 papers** — hardware-aware quantization, VLA layer-skipping, and dataset distillation push toward deploying large models on constrained hardware.

### Highlights

- **[DySL-VLA: Efficient Vision-Language-Action Model Inference via Dynamic-Static Layer-Skipping](https://arxiv.org/abs/2602.22896v1)** — Yang, Qi, Xie et al. observe that VLA models have massive redundancy during inference — not all layers contribute equally for every input. Their dynamic-static skipping decides at runtime which layers to skip based on input complexity while keeping certain "static" layers always active for stability. Practical speedup for robot manipulation without retraining.

- **[Bitwise Systolic Array Architecture for Runtime-Reconfigurable Multi-precision Quantized Multiplication](https://arxiv.org/abs/2602.23334v1)** — Liu, Ullah & Kumar go to the hardware level, designing systolic arrays that can switch precision at runtime. Mixed-precision quantization needs hardware that can actually exploit different bit-widths per layer — this architecture closes the gap between algorithmic flexibility and silicon reality.

- **[ManifoldGD: Training-Free Hierarchical Manifold Guidance for Diffusion-Based Dataset Distillation](https://arxiv.org/abs/2602.23295v1)** — Roy, Lee, Chakraborty et al. use diffusion models to distill datasets without any training loop. The manifold guidance steers generation toward samples that maximally preserve the original dataset's knowledge structure. Training-free distillation is appealing because it removes the meta-optimization overhead that makes most distillation methods expensive.

- **[Spatio-Temporal Token Pruning for Efficient High-Resolution GUI Agents](https://arxiv.org/abs/2602.23235v1)** — Xu, Zhou, Wang et al. solve the efficiency bottleneck for vision-based GUI agents: high-resolution screenshots across many timesteps create massive token sequences. Their spatio-temporal pruning removes redundant tokens both within frames (spatial) and across frames (temporal). Essential for making pure-vision GUI agents practical.

## Robotics

**14 papers** — open-source tooling, sim-to-real catching, deformable objects, and maritime research infrastructure.

### Highlights

- **[LeRobot: An Open-Source Library for End-to-End Robot Learning](https://arxiv.org/abs/2602.22818v1)** — Cadene, Aliberts, Capuano et al. release a comprehensive open-source library spanning data collection, policy training, and deployment for robot learning. The field desperately needs shared infrastructure — too many labs rebuild the same pipelines from scratch. LeRobot covering the full pipeline from demonstration collection through real-world deployment could accelerate research the way PyTorch accelerated deep learning.

- **[Pixel2Catch: Multi-Agent Sim-to-Real Transfer for Agile Manipulation with a Single RGB Camera](https://arxiv.org/abs/2602.22733v1)** — Kim, Cho, Lee et al. train a robot to catch thrown objects using only a single RGB camera — no depth sensor, no motion capture. The multi-agent sim-to-real approach jointly trains perception and control, transferring directly from simulation. Catching requires sub-200ms reaction times, making this a genuine test of whether sim-to-real can handle dynamic, time-critical tasks.

- **[A Perspective on Open Challenges in Deformable Object Manipulation](https://arxiv.org/abs/2602.22998v1)** — McKenna & Oyekan survey the state of deformable object manipulation across healthcare, manufacturing, and food processing. The honest assessment: despite significant progress, the gap between rigid and deformable manipulation remains large. Modeling, sensing, and planning for objects that change shape during interaction is fundamentally harder — and the paper maps where the biggest opportunities lie.

- **[InCoM: Intent-Driven Perception and Structured Coordination for Whole-Body Mobile Manipulation](https://arxiv.org/abs/2602.23024v1)** — Liu, Wenbo, Li et al. propose intent-driven coordination between a mobile base and manipulator. The key insight: what the robot needs to perceive depends on what it intends to do, so perception and planning should be tightly coupled rather than sequential. Whole-body coordination that's aware of task intent is more sample-efficient than treating navigation and manipulation as independent problems.

## LLM

**8 papers** — financial multi-agent systems, citation trustworthiness, and deanonymization risks through stylometry.

### Highlights

- **[Toward Expert Investment Teams: A Multi-Agent LLM System with Fine-Grained Trading Tasks](https://arxiv.org/abs/2602.23330v1)** — Miyazaki, Kawahara, Roberts et al. decompose financial trading into fine-grained subtasks handled by specialized agents. Rather than one LLM doing everything, you get analyst agents, risk agents, and execution agents that mirror how real trading desks operate. The question is whether the inter-agent communication overhead is worth the specialization — this paper suggests it is.

- **[Assessing Deanonymization Risks with Stylometry-Assisted LLM Agent](https://arxiv.org/abs/2602.23079v1)** — Zhang & Zhang demonstrate that LLM agents equipped with stylometric analysis can deanonymize text at concerning rates. The combination of traditional stylometry features with LLM-powered reasoning creates an authorship inference capability that should make anyone posting "anonymously" nervous. Important for understanding the real privacy implications of capable language models.

- **[CiteLLM: An Agentic Platform for Trustworthy Scientific Reference Discovery](https://arxiv.org/abs/2602.23075v1)** — Hong, Jiang, Zhang et al. build an agentic system specifically for finding and verifying scientific citations. LLM hallucination of references is a well-documented problem — CiteLLM addresses it by making citation discovery an agentic workflow with verification steps rather than one-shot generation. The right architecture for a task where precision matters more than recall.

## Multimodal

**5 papers** — emotion recognition, video misinformation detection, and fairness-aware quantization.

### Highlights

- **[A Mixture-of-Experts Model for Multimodal Emotion Recognition in Conversations](https://arxiv.org/abs/2602.23300v1)** — Dutta, Balaji & Ganapathy apply MoE architecture to conversational emotion recognition, routing different modality combinations to specialized experts. The conversational setting is harder than single-utterance emotion detection because emotional context shifts across turns — the MoE routing needs to capture these dynamics.

- **[FactGuard: Agentic Video Misinformation Detection via Reinforcement Learning](https://arxiv.org/abs/2602.22963v1)** — Li, Yu, Jiang et al. use RL to train an agent that adaptively decides how deeply to analyze video content for misinformation. Fixed-depth analysis wastes compute on obvious cases and may miss subtle manipulations. The RL-trained agent learns to allocate verification effort where it matters — spending more time on ambiguous or suspicious content.

- **[FairQuant: Fairness-Aware Mixed-Precision Quantization for Medical Image Classification](https://arxiv.org/abs/2602.23192v1)** — Woergaard & Selvan reveal that standard quantization can amplify fairness disparities in medical imaging models — compressing a model that's slightly biased can make it significantly more biased. Their fairness-aware approach considers demographic performance gaps when selecting per-layer precision. A critical consideration as compressed models reach clinical deployment.

## Reinforcement Learning

**2 papers** — Q-value overestimation in multi-agent settings and RL for video analysis.

### Highlights

- **[QSIM: Mitigating Overestimation in Multi-Agent Reinforcement Learning via Action Similarity Weighted Q-Learning](https://arxiv.org/abs/2602.22786v1)** — Li, Zhang, Chen et al. address the persistent overestimation problem in value decomposition methods for cooperative MARL. Their insight: similar joint actions should have similar Q-values, and violations of this principle indicate overestimation. Using action similarity as a regularization signal is elegant and doesn't require the double-estimator overhead of twin critics.

---

**Total papers tracked:** 47 | **Period:** Feb 26 – Mar 1, 2026

*Papers are fetched daily from arxiv categories cs.AI, cs.MA, cs.RO, cs.LG, and cs.CL, filtered for relevance to agents, efficient inference, and robotics.*
