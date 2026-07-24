# ACARA-SDN Project Setup Guide

## Project

Adaptive Context-Aware Risk Assessment (ACARA) Framework for DDoS Detection and Mitigation in Software-Defined Networks

---

# Operating System

Ubuntu 22.04 LTS (VMware Workstation)

---

# Update Ubuntu

```bash
sudo apt update
sudo apt upgrade -y
```

---

# Install Git

```bash
sudo apt install git -y
```

---

# Install Python

```bash
sudo apt install python3 python3-pip python3-venv -y
```

---

# Install Mininet

```bash
sudo apt install mininet -y
```

Verify:

```bash
sudo mn --test pingall
```

---

# Install Open vSwitch

```bash
sudo apt install openvswitch-switch -y
```

Verify:

```bash
ovs-vsctl show
```

---

# Install Wireshark (Optional)

```bash
sudo apt install wireshark -y
```

---

# Clone Project

```bash
mkdir -p ~/Research
cd ~/Research

git clone https://github.com/gsankar77777-hub/CADA-SDN.git

cd CADA-SDN
```

---

# Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# Install Python Packages

```bash
pip install -r requirements.txt
```

---

# Restore Datasets

Copy the following folders from the USB backup:

- datasets/
- public_dataset/

into:

~/Research/CADA-SDN/

---

# Verify Installation

Run:

```bash
python experiments/run_experiment.py
```

The project should display the experiment menu and run successfully.

---

# Git Commands

Check status:

```bash
git status
```

Add changes:

```bash
git add .
```

Commit:

```bash
git commit -m "Describe your changes"
```

Push:

```bash
git push
```

---

# Repository

https://github.com/gsankar77777-hub/CADA-SDN
