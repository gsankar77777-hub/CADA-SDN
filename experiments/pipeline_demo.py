"""
pipeline_demo.py

End-to-End Demonstration of the Detection Pipeline

Author:
G. Sankar
"""

import sys
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

sys.path.append(os.path.join(PROJECT_ROOT, "src", "detection"))
sys.path.append(os.path.join(PROJECT_ROOT, "src", "mitigation"))

from traffic_statistics import TrafficStatistics, FlowRecord
from features import FeatureExtractor
from normalizer import FeatureNormalizer
from adaptive_risk_engine import AdaptiveRiskEngine


def build_sample_statistics():

    stats = TrafficStatistics()

    stats.add_flow(
        FlowRecord(
            src_ip="10.0.0.1",
            dst_ip="10.0.0.2",
            packet_count=50,
            byte_count=4000,
            protocol="ICMP",
        )
    )

    stats.add_flow(
        FlowRecord(
            src_ip="10.0.0.2",
            dst_ip="10.0.0.1",
            packet_count=55,
            byte_count=4400,
            protocol="ICMP",
        )
    )

    return stats


def main():

    print("=" * 70)
    print("END-TO-END ACARA PIPELINE")
    print("=" * 70)

    stats = build_sample_statistics()

    print("\nTraffic Statistics")
    print("------------------------------")
    print("Flows :", stats.total_flows())
    print("Packets :", stats.total_packets())
    print("Bytes :", stats.total_bytes())
    print("Sources :", stats.unique_source_ips())
    print("Destinations :", stats.unique_destination_ips())

    feature = FeatureExtractor.extract(stats)

    print("\nFeature Vector")
    print("------------------------------")
    print(feature)

    normalized = FeatureNormalizer.normalize_features(feature)

    print("\nNormalized Features")
    print("------------------------------")
    print(normalized)

    result = AdaptiveRiskEngine.calculate(normalized)

    print("\nACARA Decision")
    print("------------------------------")
    print(result)

    print("\n" + "=" * 70)


if __name__ == "__main__":
    main()