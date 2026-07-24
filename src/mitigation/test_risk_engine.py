import sys
import os

# Add the detection folder to Python's search path
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "detection"))

from traffic_statistics import TrafficStatistics, FlowRecord
from features import FeatureExtractor
from normalizer import FeatureNormalizer

from risk_engine import RiskEngine


def main():

    stats = TrafficStatistics()

    # Sample Flow 1
    stats.add_flow(
        FlowRecord(
            src_ip="10.0.0.1",
            dst_ip="10.0.0.2",
            packet_count=120,
            byte_count=6000,
            protocol="TCP"
        )
    )

    # Sample Flow 2
    stats.add_flow(
        FlowRecord(
            src_ip="10.0.0.3",
            dst_ip="10.0.0.2",
            packet_count=80,
            byte_count=4000,
            protocol="UDP"
        )
    )

    # Complete Pipeline
    features = FeatureExtractor.extract(stats)

    normalized = FeatureNormalizer.normalize_features(features)

    result = RiskEngine.calculate(normalized)

    print("=" * 50)
    print("RISK ASSESSMENT RESULT")
    print("=" * 50)
    print(f"Risk Score : {result.score:.2f}")
    print(f"Risk Level : {result.level.value}")
    print(f"Action     : {result.action}")
    print("=" * 50)


if __name__ == "__main__":
    main()