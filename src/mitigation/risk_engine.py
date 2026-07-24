"""
risk_engine.py

Baseline Risk Assessment Engine

Project:
Adaptive Risk-Based Mitigation Algorithm (ARMA)

Author:
G. Sankar
"""

from dataclasses import dataclass
from enum import Enum


class RiskLevel(Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


@dataclass
class RiskResult:
    score: float
    level: RiskLevel
    action: str


class RiskEngine:
    """
    Baseline Rule-Based Risk Assessment
    """

    @staticmethod
    def calculate(feature):

        score = 0.0

        # Feature Contributions
        score += feature.entropy * 30
        score += feature.flow_count * 20
        score += feature.packet_count * 20
        score += feature.unique_sources * 15
        score += feature.average_packet_size * 15

        # Limit score to 100
        score = min(score, 100.0)

        # Decide Risk Level
        if score < 25:
            return RiskResult(
                score=score,
                level=RiskLevel.LOW,
                action="Monitor"
            )

        elif score < 50:
            return RiskResult(
                score=score,
                level=RiskLevel.MEDIUM,
                action="Increase Monitoring"
            )

        elif score < 75:
            return RiskResult(
                score=score,
                level=RiskLevel.HIGH,
                action="Rate Limit"
            )

        else:
            return RiskResult(
                score=score,
                level=RiskLevel.CRITICAL,
                action="Install OpenFlow Rules"
            )