"""
analyze_attack.py

Analyze any PCAP file through the
complete ACARA pipeline and
automatically save results.

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
sys.path.append(os.path.join(PROJECT_ROOT, "evaluation"))

from pcap_parser import PCAPParser
from features import FeatureExtractor
from normalizer import FeatureNormalizer
from adaptive_risk_engine import AdaptiveRiskEngine
from experiment_logger import ExperimentLogger


def determine_labels(filename):

    name = filename.lower()

    if "normal" in name:
        return "Normal", "NORMAL"

    elif "icmp" in name:
        return "ICMP Flood", "ATTACK"

    elif "syn" in name:
        return "TCP SYN Flood", "ATTACK"

    elif "udp" in name:
        return "UDP Flood", "ATTACK"

    return "Unknown", "UNKNOWN"


def main():

    filename = "datasets/normal_001.pcap"

    if len(sys.argv) > 1:
        filename = sys.argv[1]

    traffic_type, ground_truth = determine_labels(filename)

    print("=" * 70)
    print("ACARA ATTACK ANALYSIS")
    print("=" * 70)

    print("\nReading:", filename)

    stats = PCAPParser.parse(filename)

    print("\nTraffic Statistics")
    print("-" * 40)

    print("Flows              :", stats.total_flows())
    print("Packets            :", stats.total_packets())
    print("Bytes              :", stats.total_bytes())
    print("Unique Sources     :", stats.unique_source_ips())
    print("Unique Destinations:", stats.unique_destination_ips())

    feature = FeatureExtractor.extract(stats)

    print("\nFeature Vector")
    print("-" * 40)
    print(feature)

    normalized = FeatureNormalizer.normalize_features(feature)

    print("\nNormalized Features")
    print("-" * 40)
    print(normalized)

    start = time.perf_counter()

    result = AdaptiveRiskEngine.calculate(normalized)

    detection_time = (
        time.perf_counter() - start
    ) * 1000

    print("\nACARA Decision")
    print("-" * 40)
    print(result)

    logger = ExperimentLogger()

    logger.log(
        traffic_type=traffic_type,
        ground_truth=ground_truth,
        feature=feature,
        result=result,
        detection_time_ms=detection_time
    )

    print("\nDetection Time : {:.4f} ms".format(detection_time))


if __name__ == "__main__":
    main()