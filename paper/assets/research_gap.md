# Research Gap

Software-Defined Networking (SDN) has become an attractive networking paradigm because of its centralized control, programmability, and simplified network management. However, this centralized architecture also makes SDN highly vulnerable to Distributed Denial-of-Service (DDoS) attacks, which can rapidly exhaust controller resources and degrade network performance.

Numerous DDoS detection approaches have been proposed for SDN environments, including entropy-based detection, statistical traffic analysis, threshold-based methods, and machine learning techniques. Although these approaches have demonstrated promising detection capabilities, many of them rely on fixed thresholds or static feature weighting strategies that do not adapt to changing traffic conditions. Consequently, their ability to accurately assess different attack scenarios may be limited when network behavior changes dynamically.

Furthermore, many existing solutions primarily focus on attack detection while providing limited support for adaptive risk assessment and mitigation decision making. In practical SDN environments, different traffic contexts require different levels of response, making adaptive risk evaluation an important requirement for effective network defense.

Therefore, there is a need for a lightweight and context-aware risk assessment framework that dynamically adjusts feature importance according to the observed traffic context and provides appropriate mitigation recommendations without introducing significant computational complexity.