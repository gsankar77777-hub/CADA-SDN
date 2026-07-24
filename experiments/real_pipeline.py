"""
real_pipeline.py

Complete ACARA pipeline using
real packet captures.

Author:
G. Sankar
"""

import os
import sys
import time

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

sys.path.append(os.path.join(PROJECT_ROOT, "src", "detection"))
sys.path.append(os.path.join(PROJECT_ROOT, "src", "mitigation"))

from pcap_parser import PCAPParser
from features import FeatureExtractor
from normalizer import FeatureNormalizer
from adaptive_risk_engine import AdaptiveRiskEngine

from evaluate import ExperimentLogger


def run():

    print("=" * 70)
    print("REAL ACARA PIPELINE")
    print("=" * 70)

    stats = PCAPParser.parse(
        "datasets/normal_001.pcap"
    )

    feature = FeatureExtractor.extract(stats)

    normalized = FeatureNormalizer.normalize_features(feature)

    start = time.perf_counter()

    result = AdaptiveRiskEngine.calculate(normalized)

    detection_time = (
        time.perf_counter() - start
    ) * 1000

    logger = ExperimentLogger()

    logger.log(
        experiment="Real Traffic",
        traffic_type="PCAP",
        feature=feature,
        result=result,
        detection_time_ms=detection_time
    )

    print("\nTraffic Statistics")
    print("-" * 40)

    print("Flows        :", feature.flow_count)
    print("Packets      :", feature.packet_count)
    print("Bytes        :", feature.byte_count)
    print("Entropy      :", round(feature.entropy, 4))

    print("\nDecision")
    print("-" * 40)

    print("Risk Score   :", round(result.score, 4))
    print("Risk Level   :", result.level.value)
    print("Action       :", result.action)

    print("\nDetection Time:",
          round(detection_time, 4),
          "ms")

    print("\nResults saved to results/experiment_results.csv")


if __name__ == "__main__":
    run()