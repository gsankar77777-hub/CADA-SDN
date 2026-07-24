from traffic_statistics import TrafficStatistics, FlowRecord
from features import FeatureExtractor


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

    print("=" * 50)
    print("Feature Vector")
    print("=" * 50)

    print(features)


if __name__ == "__main__":
    main()