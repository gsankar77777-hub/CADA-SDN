from traffic_statistics import TrafficStatistics, FlowRecord


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

    print("=" * 40)
    print("Traffic Statistics")
    print("=" * 40)

    print("Flows:", stats.total_flows())
    print("Packets:", stats.total_packets())
    print("Bytes:", stats.total_bytes())
    print("Unique Sources:", stats.unique_source_ips())
    print("Unique Destinations:", stats.unique_destination_ips())


if __name__ == "__main__":
    main()