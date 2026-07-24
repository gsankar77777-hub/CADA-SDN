"""
adaptive_risk_engine.py

Adaptive Context-Aware Risk Assessment Algorithm (ACARA)

Project:
Adaptive Risk-Based Mitigation Algorithm (ARMA)

Author:
G. Sankar
"""

from dataclasses import dataclass
from enum import Enum


class TrafficContext(Enum):
    NORMAL = "NORMAL"
    SUSPICIOUS = "SUSPICIOUS"
    HIGH_RISK = "HIGH_RISK"
    ATTACK = "ATTACK"


class RiskLevel(Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


@dataclass
class AdaptiveRiskResult:
    score: float
    context: TrafficContext
    level: RiskLevel
    action: str


class AdaptiveRiskEngine:
    """
    Adaptive Context-Aware Risk Assessment Algorithm (ACARA)
    """

    # -----------------------------
    # Step 1: Determine Context
    # -----------------------------
    @staticmethod
    def determine_context(feature):

        if (
            feature.flow_count > 0.80
            or feature.packet_count > 0.80
            or feature.unique_sources > 0.80
        ):
            return TrafficContext.ATTACK

        elif (
            feature.flow_count > 0.60
            or feature.packet_count > 0.60
        ):
            return TrafficContext.HIGH_RISK

        elif (
            feature.entropy > 0.40
            or feature.flow_count > 0.40
        ):
            return TrafficContext.SUSPICIOUS

        else:
            return TrafficContext.NORMAL

    # -----------------------------
    # Step 2: Adaptive Weights
    # -----------------------------
    @staticmethod
    def get_weights(context):

        if context == TrafficContext.NORMAL:

            return {
                "entropy": 0.35,
                "flow_count": 0.20,
                "packet_count": 0.15,
                "unique_sources": 0.15,
                "average_packet_size": 0.15,
            }

        elif context == TrafficContext.SUSPICIOUS:

            return {
                "entropy": 0.30,
                "flow_count": 0.25,
                "packet_count": 0.20,
                "unique_sources": 0.15,
                "average_packet_size": 0.10,
            }

        elif context == TrafficContext.HIGH_RISK:

            return {
                "entropy": 0.20,
                "flow_count": 0.25,
                "packet_count": 0.25,
                "unique_sources": 0.20,
                "average_packet_size": 0.10,
            }

        else:

            return {
                "entropy": 0.15,
                "flow_count": 0.25,
                "packet_count": 0.30,
                "unique_sources": 0.20,
                "average_packet_size": 0.10,
            }

    # -----------------------------
    # Step 3: Risk Calculation
    # -----------------------------
    @staticmethod
    def calculate(feature):

        context = AdaptiveRiskEngine.determine_context(feature)

        weights = AdaptiveRiskEngine.get_weights(context)

        score = (
            feature.entropy * weights["entropy"]
            + feature.flow_count * weights["flow_count"]
            + feature.packet_count * weights["packet_count"]
            + feature.unique_sources * weights["unique_sources"]
            + feature.average_packet_size * weights["average_packet_size"]
        )

        score = min(score, 1.0)

        if score < 0.25:

            return AdaptiveRiskResult(
                score=score,
                context=context,
                level=RiskLevel.LOW,
                action="Monitor"
            )

        elif score < 0.50:

            return AdaptiveRiskResult(
                score=score,
                context=context,
                level=RiskLevel.MEDIUM,
                action="Increase Monitoring"
            )

        elif score < 0.75:

            return AdaptiveRiskResult(
                score=score,
                context=context,
                level=RiskLevel.HIGH,
                action="Rate Limit"
            )

        else:

            return AdaptiveRiskResult(
                score=score,
                context=context,
                level=RiskLevel.CRITICAL,
                action="Install OpenFlow Drop Rule"
            )