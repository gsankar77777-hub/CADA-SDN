"""
pcap_parser.py

Reads a PCAP file and converts packets into
flow-level TrafficStatistics.

Research Version 3.0

Author:
G. Sankar
"""

from collections import defaultdict
import sys

from scapy.all import rdpcap
from scapy.layers.inet import IP, TCP, UDP, ICMP

from traffic_statistics import (
    TrafficStatistics,
    FlowRecord,
)


class PCAPParser:

    @staticmethod
    def parse(filename):

        packets = rdpcap(filename)

        stats = TrafficStatistics()

        # Dictionary for flow aggregation
        # Key = (Source IP, Destination IP, Protocol)
        flows = defaultdict(
            lambda: {
                "packets": 0,
                "bytes": 0
            }
        )

        for packet in packets:

            # Ignore non-IPv4 packets
            if IP not in packet:
                continue

            ip = packet[IP]

            # Determine protocol
            if ICMP in packet:
                protocol = "ICMP"

            elif TCP in packet:
                protocol = "TCP"

            elif UDP in packet:
                protocol = "UDP"

            else:
                protocol = "OTHER"

            key = (
                str(ip.src),
                str(ip.dst),
                protocol
            )

            flows[key]["packets"] += 1
            flows[key]["bytes"] += len(packet)

        # Convert dictionary to FlowRecord objects
        for key, value in flows.items():

            src_ip, dst_ip, protocol = key

            flow = FlowRecord(
                src_ip=src_ip,
                dst_ip=dst_ip,
                packet_count=value["packets"],
                byte_count=value["bytes"],
                protocol=protocol,
            )

            stats.add_flow(flow)

        return stats


if __name__ == "__main__":

    # Default file
    filename = "datasets/normal_001.pcap"

    # Allow custom PCAP from command line
    if len(sys.argv) > 1:
        filename = sys.argv[1]

    print("=" * 60)
    print("ACARA PCAP FLOW PARSER")
    print("=" * 60)
    print("Reading PCAP :", filename)

    stats = PCAPParser.parse(filename)

    print("\nFlow-Level Statistics")
    print("-" * 60)

    print(f"Total Flows       : {stats.total_flows()}")
    print(f"Total Packets     : {stats.total_packets()}")
    print(f"Total Bytes       : {stats.total_bytes()}")
    print(f"Unique Sources    : {stats.unique_source_ips()}")
    print(f"Unique Destinations : {stats.unique_destination_ips()}")

    print("\nFlow Details")
    print("-" * 60)

    for index, flow in enumerate(stats.flows, start=1):

        print(f"\nFlow {index}")
        print(f"Source IP     : {flow.src_ip}")
        print(f"Destination IP: {flow.dst_ip}")
        print(f"Protocol      : {flow.protocol}")
        print(f"Packets       : {flow.packet_count}")
        print(f"Bytes         : {flow.byte_count}")

    print("\n" + "=" * 60)
    print("Parsing Completed Successfully")
    print("=" * 60)