"""
normalizer.py

Feature Normalization Module

Project:
Adaptive Risk-Based Mitigation Algorithm (ARMA)
"""

from dataclasses import dataclass


@dataclass
class NormalizedFeatureVector:
    entropy: float
    flow_count: float
    packet_count: float
    byte_count: float
    unique_sources: float
    unique_destinations: float
    average_packet_size: float


class FeatureNormalizer:

    @staticmethod
    def normalize(value: float, minimum: float, maximum: float) -> float:

        if maximum == minimum:
            return 0.0

        return (value - minimum) / (maximum - minimum)

    @classmethod
    def normalize_features(cls, feature):

        return NormalizedFeatureVector(

            entropy=cls.normalize(
                feature.entropy,
                0,
                4
            ),

            flow_count=cls.normalize(
                feature.flow_count,
                0,
                1000
            ),

            packet_count=cls.normalize(
                feature.packet_count,
                0,
                100000
            ),

            byte_count=cls.normalize(
                feature.byte_count,
                0,
                10000000
            ),

            unique_sources=cls.normalize(
                feature.unique_sources,
                0,
                1000
            ),

            unique_destinations=cls.normalize(
                feature.unique_destinations,
                0,
                1000
            ),

            average_packet_size=cls.normalize(
                feature.average_packet_size,
                0,
                1500
            )
        )