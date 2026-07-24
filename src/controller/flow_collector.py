"""
flow_collector.py

Flow Collector Module

Project:
Adaptive Risk-Based Mitigation Algorithm (ARMA)

Description:
Receives flow information from the SDN controller
and converts it into TrafficStatistics objects.

Author:
G. Sankar
"""

from dataclasses import dataclass
from typing import List

# Import our existing data model
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "detection"))

from traffic_statistics import FlowRecord, TrafficStatistics


@dataclass
class OpenFlowEntry:
    """
    Simplified representation of an OpenFlow flow entry.

    Later, this will be populated directly from the
    SDN controller.
    """

    src_ip: str
    dst_ip: str
    packet_count: int
    byte_count: int
    protocol: str


class FlowCollector:
    """
    Converts OpenFlow entries into TrafficStatistics.
    """

    @staticmethod
    def collect(entries: List[OpenFlowEntry]) -> TrafficStatistics:

        stats = TrafficStatistics()

        for entry in entries:

            flow = FlowRecord(
                src_ip=entry.src_ip,
                dst_ip=entry.dst_ip,
                packet_count=entry.packet_count,
                byte_count=entry.byte_count,
                protocol=entry.protocol,
            )

            stats.add_flow(flow)

        return stats