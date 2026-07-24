"""
Test Enhanced Experiment Logger
"""

import sys
import os
import time

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

sys.path.append(os.path.join(PROJECT_ROOT, "src", "detection"))
sys.path.append(os.path.join(PROJECT_ROOT, "src", "mitigation"))

from traffic_statistics import TrafficStatistics, FlowRecord
from features import FeatureExtractor
from normalizer import FeatureNormalizer
from adaptive_risk_engine import AdaptiveRiskEngine
from evaluate import ExperimentLogger


stats = TrafficStatistics()

stats.add_flow(
    FlowRecord(
        "10.0.0.1",
        "10.0.0.2",
        50,
        4000,
        "ICMP"
    )
)

stats.add_flow(
    FlowRecord(
        "10.0.0.2",
        "10.0.0.1",
        55,
        4400,
        "ICMP"
    )
)

feature = FeatureExtractor.extract(stats)

normalized = FeatureNormalizer.normalize_features(feature)

start = time.perf_counter()

result = AdaptiveRiskEngine.calculate(normalized)

end = time.perf_counter()

detection_time_ms = (end - start) * 1000

logger = ExperimentLogger()

logger.log(
    experiment="Experiment 1",
    traffic_type="Normal",
    feature=feature,
    result=result,
    detection_time_ms=detection_time_ms
)

print("\nDetection Time: {:.3f} ms".format(detection_time_ms))
print("Experiment Completed Successfully.")