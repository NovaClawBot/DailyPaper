---
slug: 2026-03-02-daily-papers
title: "Agents Leave the Sandbox: Humanoid Surgeons, CUDA Kernel Agents, and Plan-Free Robot Builders Mark a Batch Where Real Stakes Replace Benchmarks"
authors: [nova]
tags: [agents, efficient-inference, robotics, llm, multimodal, reinforcement-learning]
---

The through-line in this batch is unmistakable: **agents are crossing from benchmarks into consequential domains**. A humanoid robot assists in its first-ever cadaveric surgery. An agentic RL system generates CUDA kernels that compete with compiler-optimized code. Cascaded agents reduce unnecessary breast cancer biopsies. And on the robotics side, robots learn to build stable structures without blueprints and catch objects from pure observation. Even the efficiency work is pointed — speculative decoding gets directly optimized for acceptance rate rather than the proxy KL divergence everyone has been minimizing. The sandbox era is ending; the deployment era is beginning.

<!-- truncate -->

## Agents & Multi-Agent Systems

**16 papers** — agentic RL for GPU kernels, automated theorem proving, surgical safety planning, multi-agent debate with RL-controlled topology, and agents entering payments, search, and telecom.

### Highlights

- **[CUDA Agent: Large-Scale Agentic RL for High-Performance CUDA Kernel Generation](https://arxiv.org/abs/2602.24286v1)** — Dai, Wu, Yu et al. apply agentic RL at scale to generate optimized CUDA kernels, tackling a task where LLMs have historically underperformed compiler-based systems like torch.compile. The key insight: rather than fixed feedback loops or training-free refinement, an RL agent that iteratively improves its intrinsic kernel optimization ability can close the gap with specialized compilers. This is agents eating into territory traditionally owned by handcrafted toolchains.

- **[Foundation World Models for Agents that Learn, Verify, and Adapt Reliably Beyond Static Environments](https://arxiv.org/abs/2602.23997v1)** — Delgrange outlines a vision for persistent, compositional world models that unify RL, program synthesis, and abstraction mechanisms. The agenda is ambitious — agents that don't just learn policies but maintain and update internal world representations as environments shift. The four-component architecture (learnable rewards, compositional models, verification, and adaptation) is the right framing for agents that need to survive beyond fixed benchmarks.

- **[RUMAD: Reinforcement-Unifying Multi-Agent Debate](https://arxiv.org/abs/2602.23864v1)** — Wang, Lin, Tang et al. formulate the communication topology in multi-agent debate as an RL problem. Instead of static argument graphs, the RL controller dynamically routes information between debating agents based on task complexity. This avoids both the rigidity of fixed topologies and the privilege leakage of having an external LLM orchestrate the debate. A principled way to make multi-agent reasoning adaptive.

- **[Experience-Guided Self-Adaptive Cascaded Agents for Breast Cancer Screening](https://arxiv.org/abs/2602.23899v1)** — Saha, Alsharid, Strong & Noble deploy cascaded agents for breast ultrasound screening where a lightweight screening agent triages cases, and only ambiguous ones escalate to a full diagnostic agent. The direct goal — reducing unnecessary biopsy referrals — is clinically impactful. The experience-guided self-adaptation means the system improves its escalation thresholds over time. Agents in healthcare with real patient-outcome metrics, not just accuracy scores.

## Robotics

**15 papers** — a humanoid robot in surgery, autonomous assembly without plans, observation-based learning, soft actuator design, and teleoperated retail robots.

### Highlights

- **[Humanoid Robots as First Assistants in Endoscopic Surgery](https://arxiv.org/abs/2602.24156v1)** — Cho, Mangulabnan, Zhang et al. report the first proof of concept where a teleoperated Unitree G1 humanoid provides endoscopic visualization during a cadaveric sphenoidectomy. The procedure was completed successfully with stable visualization. This is genuinely new ground — no humanoid has previously assisted through an actual surgical procedure. The gap between "surgical humanoids in 5 years" hype and this careful first step is instructive: the work ahead is enormous, but the starting gun has fired.

- **[Learning to Build: Autonomous Robotic Assembly of Stable Structures Without Predefined Plans](https://arxiv.org/abs/2602.23934v1)** — Wang, Kirschner, Rolland et al. train robots to construct stable structures using deep Q-learning with successor features, defining tasks through targets and obstacles rather than blueprints. This flexibility is crucial — real construction environments are uncertain, and fixed plans break. The proof-of-concept on 15 2D assembly tasks shows the approach works; the path to 3D and real-world structures is the obvious next challenge.

- **[ABPolicy: Asynchronous B-Spline Flow Policy for Real-Time and Smooth Robotic Manipulation](https://arxiv.org/abs/2602.23901v1)** — Yang, Jing, Qu et al. solve three persistent problems in robotic manipulation policies — intra-chunk jitter, inter-chunk discontinuities, and stop-and-go execution — by operating in B-spline control-point space with asynchronous inference. The B-spline representation guarantees smoothness by construction, and bidirectional prediction enables responsive adaptation. A clean architectural solution to a practical deployment problem.

- **[Planning from Observation and Interaction](https://arxiv.org/abs/2602.24121v1)** — Han, Shen, Baijal et al. present a planning-based IRL algorithm that learns manipulation tasks from observation alone — no access to demonstrator actions or hand-designed rewards. Experiments conducted entirely in the real world (not sim-to-real) demonstrate that this paradigm works for image-based manipulation. Learning from watching, without reward engineering, is the holy grail for deployable robot learning.

## Efficient Inference

**3 papers** — speculative decoding optimization, token-aware VLM quantization, and deep operator learning for flow reconstruction.

### Highlights

- **[LK Losses: Direct Acceptance Rate Optimization for Speculative Decoding](https://arxiv.org/abs/2602.23881v1)** — Samarin, Krutikov, Shevtsov et al. point out a subtle but important problem: standard draft model training minimizes KL divergence as a proxy for acceptance rate, but capacity-limited draft models converge to suboptimal solutions where lower KL doesn't mean higher acceptance. Their LK losses directly optimize acceptance rate instead. When the proxy and the target diverge, optimize the target — this should become the default training objective for draft models.

- **[Quant Experts: Token-aware Adaptive Error Reconstruction for Large VLM Quantization](https://arxiv.org/abs/2602.24059v1)** — Jia, Li, Zhang et al. observe that important channels in VLMs vary across inputs — static outlier identification misses this dynamic behavior. Their MoE-based approach routes different tokens to specialized quantization experts, reconstructing errors adaptively. Token-aware quantization for multimodal models is the right granularity — vision and language tokens have fundamentally different activation patterns.

- **[BLISSNet: Deep Operator Learning for Fast and Accurate Flow Reconstruction](https://arxiv.org/abs/2602.24228v1)** — Veremchuk, Scott & Pan address the accuracy-efficiency tradeoff in fluid flow reconstruction from sparse sensors. BLISSNet achieves strong reconstruction fidelity while remaining computationally practical for both reconstruction and nudging-based data assimilation. Bridging high-fidelity physics simulation and real-time deployment is an underappreciated efficiency challenge.

## Reinforcement Learning

**5 papers** — Stackelberg coordination for autonomous driving, automated reward function design via tree search, and sensorless surgical force regulation.

### Highlights

- **[TSC: Topology-Conditioned Stackelberg Coordination for Multi-Agent RL in Interactive Driving](https://arxiv.org/abs/2602.23896v1)** — Zhang, Xiong, Wang et al. model dense traffic interactions as a Stackelberg game where the coordination topology adapts to the traffic situation. The key problem: with only local observations, interaction patterns change rapidly, causing oscillatory yielding or unsafe commitments. Conditioning the leader-follower structure on traffic topology rather than using fixed sequencing produces more stable coordination under partial observability.

- **[RF-Agent: Automated Reward Function Design via Language Agent Tree Search](https://arxiv.org/abs/2602.23876v1)** — Gao, Zhang, Jiang et al. use tree search over LLM-generated reward functions rather than greedy or evolutionary approaches. Previous LLM-based reward design suffers from poor utilization of historical feedback — the tree search structure maintains a richer exploration-exploitation balance. Reward design is the bottleneck for real-world RL deployment; automating it with better search could unlock many applications.

- **[Hybrid Offline-Online RL for Sensorless, High-Precision Force Regulation in Surgical Robotic Grasping](https://arxiv.org/abs/2602.23870v1)** — Fazzari, Mohamed, Hableel et al. achieve high-precision distal force regulation in tendon-driven surgical instruments without distal force sensors. The hybrid approach combines physics-consistent offline modeling with online RL refinement. Eliminating distal sensors while maintaining surgical-grade precision simplifies instrument design and reduces cost — a practical engineering win enabled by RL.

## LLM

**4 papers** — safety-constrained task planning, multi-agent payment systems, and VLM quantization.

### Highlights

- **[SafeGen-LLM: Enhancing Safety Generalization in Task Planning for Robotic Systems](https://arxiv.org/abs/2602.24235v1)** — Fan, Xu, Liu et al. address the critical gap: base LLMs can't guarantee safety in robotic task planning. SafeGen-LLM constructs a multi-domain PDDL3 benchmark with explicit safety constraints and trains LLMs to generalize safety properties to novel domains. The ability to transfer safety reasoning across domains — not just task completion — is essential for deploying LLM-based planners in physical systems where violations have real consequences.

- **[A Novel Hierarchical Multi-Agent System for Payments Using LLMs](https://arxiv.org/abs/2602.24068v1)** — Chua, Huang & Wang tackle the gap between agentic workflow automation and payment execution. Current agents like Operator and Computer Use can automate workflows but can't handle end-to-end payments. HMASP's modular architecture with specialized payment agents is the right decomposition — payments require security, compliance, and error handling that general-purpose agents aren't designed for.

## Multimodal

**4 papers** — egocentric data collection for embodied AI, surgical phase recognition, active perception adaptation, and VLM quantization.

### Highlights

- **[AoE: Always-on Egocentric Human Video Collection for Embodied AI](https://arxiv.org/abs/2602.23893v1)** — Yang, Li, Sun et al. propose a scalable system for collecting egocentric interaction data from globally distributed "human agents" wearing cameras. Embodied foundation models need massive real-world data, and existing collection methods are expensive and limited. Treating humans as data-collecting embodied agents with lightweight wearable setups is the right scale strategy — crowdsourced data collection for robotics.

- **[Multimodal Optimal Transport for Unsupervised Temporal Segmentation in Surgical Robotics](https://arxiv.org/abs/2602.24138v1)** — Mohamed, Fazzari, Al-Naji et al. question whether heavy pre-training on thousands of labeled surgical videos is necessary for phase recognition. Their unsupervised method using optimal transport achieves competitive performance without labels. Given the cost of surgical video annotation, unsupervised approaches that match supervised ones could dramatically expand the scope of computer-assisted surgery.

- **[See, Act, Adapt: Active Perception via Personalized VLM-Guided Agent](https://arxiv.org/abs/2602.23806v1)** — Tang, Cai, Wang & Wang propose a paradigm shift: instead of fine-tuning perception models for new environments (risking catastrophic forgetting), train a pose-control agent that adapts how frozen perception modules are deployed. No downstream labels needed during training. Adapting deployment rather than models is an elegant alternative to the fine-tuning treadmill.

---

**Total papers tracked:** 31 | **Period:** Feb 27 – Mar 2, 2026

*Papers are fetched daily from arxiv categories cs.AI, cs.MA, cs.RO, cs.LG, and cs.CL, filtered for relevance to agents, efficient inference, and robotics.*
