"""
flow_parser.py

Parses Open vSwitch flow entries into FlowRecord objects.
"""

import re
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "detection"))

from traffic_statistics import FlowRecord


class FlowParser:

    @staticmethod
    def parse(flow_output):

        flows = []

        if not flow_output:
            return flows

        for line in flow_output.splitlines():

            if "n_packets" not in line:
                continue

            packet_match = re.search(r"n_packets=(\d+)", line)
            byte_match = re.search(r"n_bytes=(\d+)", line)

            src_match = re.search(r"nw_src=([0-9\.]+)", line)
            dst_match = re.search(r"nw_dst=([0-9\.]+)", line)
            proto_match = re.search(r"(tcp|udp|icmp)", line, re.IGNORECASE)

            packets = int(packet_match.group(1))
            bytes_count = int(byte_match.group(1))

            src_ip = src_match.group(1) if src_match else "unknown"
            dst_ip = dst_match.group(1) if dst_match else "unknown"
            protocol = proto_match.group(1).upper() if proto_match else "UNKNOWN"

            flows.append(
                FlowRecord(
                    src_ip=src_ip,
                    dst_ip=dst_ip,
                    packet_count=packets,
                    byte_count=bytes_count,
                    protocol=protocol,
                )
            )

        return flows


if __name__ == "__main__":

    sample = """
cookie=0x0, duration=10.0s, table=0, n_packets=25, n_bytes=2000, priority=0,icmp,nw_src=10.0.0.1,nw_dst=10.0.0.2 actions=NORMAL
cookie=0x0, duration=5.0s, table=0, n_packets=60, n_bytes=4800, priority=0,tcp,nw_src=10.0.0.2,nw_dst=10.0.0.1 actions=NORMAL
"""

    parsed = FlowParser.parse(sample)

    print("=" * 60)

    for flow in parsed:
        print(flow)