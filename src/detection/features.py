"""
features.py

Feature Extraction Module
"""

from dataclasses import dataclass

from entropy import EntropyEngine
from traffic_statistics import TrafficStatistics


@dataclass
class FeatureVector:
    entropy: float
    flow_count: int
    packet_count: int
    byte_count: int
    unique_sources: int
    unique_destinations: int
    average_packet_size: float


class FeatureExtractor:

    @staticmethod
    def extract(stats: TrafficStatistics) -> FeatureVector:

        source_ips = [flow.src_ip for flow in stats.flows]

        entropy = EntropyEngine.shannon(source_ips)

        if stats.total_packets() > 0:
            avg_packet_size = (
                stats.total_bytes() /
                stats.total_packets()
            )
        else:
            avg_packet_size = 0.0

        return FeatureVector(
            entropy=entropy,
            flow_count=stats.total_flows(),
            packet_count=stats.total_packets(),
            byte_count=stats.total_bytes(),
            unique_sources=stats.unique_source_ips(),
            unique_destinations=stats.unique_destination_ips(),
            average_packet_size=avg_packet_size,
        )