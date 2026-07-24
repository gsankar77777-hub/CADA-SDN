# Adaptive Context-Aware DDoS Detection and Mitigation in Software Defined Networks

Author:
G. Sankar

---

# 1. Problem Statement

Distributed Denial of Service (DDoS) attacks remain one of the most serious
security threats against Software Defined Networks (SDN).

Existing entropy-based detection methods rely mainly on a single statistical
feature and fixed thresholds.

These approaches often suffer from:

- High false positives
- Poor adaptability
- Delayed mitigation
- Performance degradation under dynamic traffic

The objective of this research is to design an adaptive detection and mitigation
framework capable of identifying DDoS attacks in real-time using multiple
network features extracted from SDN flow statistics.

---

# 2. Research Gap

Most existing approaches:

• Use entropy alone.

• Depend on fixed thresholds.

• Ignore overall traffic context.

• Immediately block traffic without evaluating risk.

• Perform only offline dataset evaluation.

---

# 3. Proposed Solution

The proposed framework introduces an adaptive multi-stage detection pipeline.

Instead of relying only on entropy,
multiple flow statistics will be analysed simultaneously.

The system computes an adaptive risk score and
selects an appropriate mitigation strategy.

---

# 4. Research Objectives

Objective 1

Develop a modular SDN DDoS detection framework.

Objective 2

Extract multiple traffic features.

Objective 3

Develop an adaptive risk assessment model.

Objective 4

Implement progressive mitigation.

Objective 5

Evaluate using Mininet.

---

# 5. Current Implementation Status

Completed

✓ Entropy

✓ Traffic Statistics

✓ Feature Extraction

✓ Feature Normalization

✓ Baseline Risk Engine

✓ Flow Collector

Pending

□ SDN Controller Integration

□ Adaptive Risk Engine

□ Progressive Mitigation

□ Experiments

□ Evaluation

---

# 6. Expected Contributions

Contribution 1

Multi-feature traffic analysis.

Contribution 2

Adaptive risk assessment.

Contribution 3

Progressive mitigation strategy.

Contribution 4

Real-time SDN implementation.

---

# End of Version 1