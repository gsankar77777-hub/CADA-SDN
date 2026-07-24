# Adaptive Context-Aware Risk Assessment (ACARA) Framework for DDoS Detection and Mitigation in Software-Defined Networks

## Overview

This project presents an Adaptive Context-Aware Risk Assessment (ACARA) framework for detecting and mitigating Distributed Denial of Service (DDoS) attacks in Software-Defined Networks (SDN).

The framework combines entropy-based traffic analysis, adaptive risk scoring, and Software-Defined Networking principles to identify abnormal traffic patterns and dynamically mitigate malicious flows.

---

# Objectives

- Detect DDoS attacks using entropy analysis
- Extract statistical network traffic features
- Calculate adaptive risk scores
- Classify network traffic
- Mitigate malicious flows in SDN environments
- Evaluate detection performance using multiple metrics

---

# Technologies Used

- Python
- Software Defined Networking (SDN)
- Mininet
- Open vSwitch (OVS)
- OS-Ken (Ryu Controller)
- Scapy
- NumPy
- Pandas
- Matplotlib
- Scikit-learn

---

# Project Structure

```
CADA-SDN
│
├── docs/
├── evaluation/
├── experiments/
├── graphs/
├── paper/
├── src/
├── datasets/              (Not included in GitHub)
├── public_dataset/        (Not included in GitHub)
├── requirements.txt
├── SETUP.md
└── README.md
```

---

# Source Code

## src/

Contains the main framework implementation.

### controller

Flow collection and parsing.

### detection

Entropy calculation

Feature extraction

Traffic statistics

Packet analysis

### mitigation

Adaptive Risk Engine

Risk Score Calculation

Mitigation Logic

---

# Experiments

The experiments folder contains scripts for

- Normal Traffic
- SYN Flood
- UDP Flood
- ICMP Flood
- Live Detection
- Dataset Generation
- Batch Evaluation
- Pipeline Demonstration

---

# Evaluation

The evaluation module computes

- Accuracy
- Precision
- Recall
- F1 Score
- Detection Time
- Confusion Matrix

---

# Graphs

Generated visualizations include

- Entropy
- Flow Count
- Packet Count
- Byte Count
- Detection Time
- Risk Score
- Classification Metrics

---

# Installation

See **SETUP.md**

---

# Python Dependencies

```bash
pip install -r requirements.txt
```

---

# Run the Project

Activate the virtual environment

```bash
source venv/bin/activate
```

Run

```bash
python experiments/run_experiment.py
```

---

# Research Paper

Adaptive Context-Aware Risk Assessment (ACARA) Framework for DDoS Detection and Mitigation in Software-Defined Networks

---

# Author

G Sankar

---

# License

This repository is intended for academic and research purposes.
