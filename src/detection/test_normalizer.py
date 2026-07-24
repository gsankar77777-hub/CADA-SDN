from traffic_statistics import TrafficStatistics, FlowRecord
from features import FeatureExtractor
from normalizer import FeatureNormalizer


def main():

    stats = TrafficStatistics()

    stats.add_flow(
        FlowRecord(
            "10.0.0.1",
            "10.0.0.2",
            120,
            6000,
            "TCP",
        )
    )

    stats.add_flow(
        FlowRecord(
            "10.0.0.3",
            "10.0.0.2",
            80,
            4000,
            "UDP",
        )
    )

    features = FeatureExtractor.extract(stats)

    normalized = FeatureNormalizer.normalize_features(features)

    print("=" * 50)
    print("Normalized Feature Vector")
    print("=" * 50)
    print(normalized)


if __name__ == "__main__":
    main()