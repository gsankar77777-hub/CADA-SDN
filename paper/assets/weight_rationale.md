# Design Rationale for Adaptive Feature Weights

The proposed ACARA framework employs context-dependent feature weighting to improve adaptive risk assessment under varying network conditions. Instead of assigning identical importance to all traffic features, the framework dynamically adjusts feature weights according to the detected traffic context.

During normal network conditions, entropy is assigned a relatively higher weight because it effectively represents the natural diversity of legitimate traffic. As the traffic context progresses from Normal to Suspicious, High Risk, and Attack, greater emphasis is gradually placed on traffic intensity indicators such as flow count and packet count, which become stronger indicators of volumetric DDoS attacks.

The number of unique source IP addresses is also assigned increased importance under attack conditions because distributed attacks typically involve multiple traffic sources. Average packet size receives a comparatively lower weight since it serves primarily as a complementary traffic characteristic rather than a dominant attack indicator.

This adaptive weighting strategy enables ACARA to modify its decision-making process according to the observed traffic context while maintaining a computationally lightweight risk assessment mechanism suitable for Software-Defined Networking environments.