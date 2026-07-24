"""
traffic_statistics.py

Traffic Statistics Module

Project:
    Adaptive Multi-Metric Decision Algorithm (AMDA)

Author:
    G. Sankar
"""

from dataclasses import dataclass
from typing import List


@dataclass
class FlowRecord:
    """
    Represents a single network flow.
    """
    src_ip: str
    dst_ip: str
    packet_count: int
    byte_count: int
    protocol: str


class TrafficStatistics:
    """
    Stores traffic records and computes basic statistics.
    """

    def __init__(self):
        self.flows: List[FlowRecord] = []

    def add_flow(self, flow: FlowRecord):
        self.flows.append(flow)

    def total_flows(self) -> int:
        return len(self.flows)

    def total_packets(self) -> int:
        return sum(flow.packet_count for flow in self.flows)

    def total_bytes(self) -> int:
        return sum(flow.byte_count for flow in self.flows)

    def unique_source_ips(self) -> int:
        return len(set(flow.src_ip for flow in self.flows))

    def unique_destination_ips(self) -> int:
        return len(set(flow.dst_ip for flow in self.flows))