"""
Test Program for AdaptiveRiskEngine (ACARA)

Author:
G. Sankar
"""

from adaptive_risk_engine import AdaptiveRiskEngine


class DummyFeature:
    """
    Simulates a normalized feature vector.
    """

    def __init__(
        self,
        entropy,
        flow_count,
        packet_count,
        unique_sources,
        average_packet_size,
    ):
        self.entropy = entropy
        self.flow_count = flow_count
        self.packet_count = packet_count
        self.unique_sources = unique_sources
        self.average_packet_size = average_packet_size


print("=" * 60)
print("ACARA TEST")
print("=" * 60)

# -----------------------------
# Normal Traffic
# -----------------------------
feature = DummyFeature(
    entropy=0.20,
    flow_count=0.18,
    packet_count=0.15,
    unique_sources=0.10,
    average_packet_size=0.30,
)

result = AdaptiveRiskEngine.calculate(feature)

print("\nScenario 1 : Normal")
print(result)

# -----------------------------
# Suspicious Traffic
# -----------------------------
feature = DummyFeature(
    entropy=0.45,
    flow_count=0.42,
    packet_count=0.30,
    unique_sources=0.25,
    average_packet_size=0.30,
)

result = AdaptiveRiskEngine.calculate(feature)

print("\nScenario 2 : Suspicious")
print(result)

# -----------------------------
# High Risk
# -----------------------------
feature = DummyFeature(
    entropy=0.55,
    flow_count=0.65,
    packet_count=0.70,
    unique_sources=0.40,
    average_packet_size=0.35,
)

result = AdaptiveRiskEngine.calculate(feature)

print("\nScenario 3 : High Risk")
print(result)

# -----------------------------
# Attack
# -----------------------------
feature = DummyFeature(
    entropy=0.85,
    flow_count=0.95,
    packet_count=0.96,
    unique_sources=0.92,
    average_packet_size=0.80,
)

result = AdaptiveRiskEngine.calculate(feature)

print("\nScenario 4 : Attack")
print(result)

print("\n" + "=" * 60)