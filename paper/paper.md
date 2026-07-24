<!--
Paper Status

Title: Final
Abstract: Not Started
Introduction: Not Started
Related Work: Not Started

Methodology:
3.1 Draft 1 ✔
3.2 Draft 1 ✔
3.3 Draft 1 ✔
3.4 Not Started
3.5 Not Started
3.6 Not Started
3.7 Not Started
3.8 Not Started

Experiments: Not Started
Results: Not Started
Conclusion: Not Started

Figures:
Figure 1 ✔
Figure 2 ✔
Figure 3 ✔
Figure 4 ✔
Graphs ✔

Tables:
Table 1
Table 2
Table 3

References:
0
-->

# ACARA: An Adaptive Context-Aware Risk Assessment Framework for DDoS Detection and Mitigation in Software-Defined Networks

**Author:** G. Sankar

## Abstract

## Keywords

# 1. Introduction

# 2. Related Work
# 3 Proposed ACARA Framework

## 3.1 System Model

## 3.2 Framework Overview

## 3.3 Algorithm Design

## 3.4 Mathematical Formulation

## 3.5 Traffic Collection

## 3.6 Feature Extraction

## 3.7 Feature Normalization

## 3.8 Traffic Context Detection

## 3.9 Adaptive Weight Selection

## 3.10 Adaptive Risk Score Computation

## 3.11 Adaptive Mitigation Recommendation
# 4. Experimental Setup

## 4.1 Experimental Environment

## 4.2 Datasets

## 4.3 Evaluation Metrics

# 5. Results and Discussion

## 5.1 Detection Performance

## 5.2 Adaptive Risk Assessment Analysis

## 5.3 Classification Performance

## 5.4 Discussion

# 6. Conclusion

# References

## 3.1 Framework Overview
The proposed Adaptive Context-Aware Risk Assessment (ACARA) framework is designed to improve the detection and mitigation of Distributed Denial-of-Service (DDoS) attacks in Software-Defined Networking (SDN) environments. Unlike conventional approaches that rely on fixed thresholds or single-feature analysis, ACARA performs adaptive risk assessment by combining multiple traffic characteristics with context-aware decision making. The framework continuously analyzes network traffic, evaluates the current traffic context, computes an adaptive risk score, and recommends an appropriate mitigation action based on the assessed risk level. This adaptive design enables the framework to respond more effectively to varying network conditions while maintaining accurate traffic classification.

The ACARA framework consists of two major functional stages: adaptive risk assessment and adaptive mitigation recommendation. In the first stage, incoming traffic statistics are processed through feature extraction, feature normalization, traffic context detection, adaptive weight selection, and adaptive risk score computation to determine the current traffic risk level. In the second stage, the assessed risk level is provided to the adaptive mitigation recommendation module, which determines an appropriate mitigation strategy according to the evaluated risk category. This modular architecture enables the framework to separate traffic analysis from mitigation decision making, thereby improving scalability, maintainability, and adaptability in SDN environments.

3.1 Framework Overview

Paragraph 1

Paragraph 2

Figure 3
Adaptive Risk Assessment Workflow

Paragraph 3

Figure 3 illustrates the adaptive risk assessment workflow of the proposed ACARA framework. The workflow begins with the collection of incoming traffic statistics, followed by feature extraction and feature normalization to prepare the traffic data for analysis. The normalized traffic features are subsequently used to identify the current traffic context, enabling the framework to dynamically assign context-dependent feature weights before computing an adaptive risk score. Based on the computed risk score, the framework classifies the traffic into one of four traffic contexts—Normal, Suspicious, High Risk, or Attack—and forwards the assessed risk level to the adaptive mitigation recommendation module for further processing.

**[Insert Figure 3: Adaptive Risk Assessment Workflow of the Proposed ACARA Framework here]**

The adaptive risk assessment workflow provides a structured mechanism for analyzing network traffic and estimating its associated risk level before any mitigation decision is considered. By separating traffic analysis from mitigation recommendation, the proposed framework maintains a modular architecture that simplifies implementation, facilitates future extensions, and supports integration with SDN-based network management systems. The following subsections describe each component of the ACARA framework in detail, beginning with the traffic collection process.

## 3.2 Traffic Collection
The traffic collection stage serves as the entry point of the proposed ACARA framework. Its primary objective is to acquire network traffic information and organize it into a structured format suitable for subsequent analysis. Instead of directly processing live network packets, the current implementation analyzes packet capture (PCAP) files containing both normal and DDoS traffic scenarios. This approach enables controlled experimentation, repeatable evaluations, and consistent comparison of different traffic conditions under identical processing procedures.

The experimental traffic used in this study consists of two complementary datasets. The first dataset is derived from the publicly available CIC-DDoS2019 benchmark, which provides representative DDoS attack traffic for performance evaluation. The second dataset was generated within the experimental SDN environment to validate the proposed framework under controlled network conditions. The generated dataset includes normal traffic, TCP SYN flood traffic, UDP flood traffic, and ICMP flood traffic, enabling comprehensive evaluation across multiple attack scenarios.

**[Insert Figure 4: Experimental Setup of the Proposed ACARA Framework here]**

Figure 4 presents the experimental environment adopted to evaluate the proposed ACARA framework. The experimental platform integrates a Mininet-based SDN topology, Open vSwitch, traffic generation modules, packet capture mechanisms, and the ACARA processing pipeline. Traffic captured during the experiments is stored as PCAP files, which are subsequently analyzed to extract network statistics and traffic features required for adaptive risk assessment. This experimental design ensures repeatability while providing a realistic representation of normal and attack traffic conditions.

## 3.3 Feature Extraction
Feature extraction is a fundamental stage of the proposed ACARA framework, as it transforms raw network traffic statistics into meaningful attributes that can be used for adaptive risk assessment. Instead of relying on a single network characteristic, the framework extracts multiple traffic features that collectively describe the behavior of network flows. This multi-feature approach improves the ability of the framework to distinguish between legitimate traffic and DDoS attack traffic under different network conditions.

The current implementation extracts five primary traffic features from the collected network statistics: entropy, flow count, packet count, unique source IPs, and average packet size. Each feature captures a different aspect of network behavior. Entropy represents the randomness of traffic distribution, while flow count and packet count indicate the traffic intensity. The number of unique source IP addresses reflects the diversity of traffic sources, and the average packet size provides additional information about packet characteristics. Together, these features provide a comprehensive representation of network traffic for subsequent adaptive risk analysis.

The extracted traffic features are subsequently forwarded to the feature normalization stage, where all feature values are transformed into a common numerical scale before adaptive risk computation. This preprocessing step ensures that individual traffic characteristics contribute proportionally during context detection and adaptive risk score calculation, thereby improving the stability and consistency of the overall risk assessment process.

**[Optional Figure: Feature Extraction Process]**
