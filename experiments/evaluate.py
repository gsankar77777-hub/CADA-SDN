"""
evaluate.py

Enhanced Experiment Result Logger

Author:
G. Sankar
"""

import csv
import os
from datetime import datetime


class ExperimentLogger:

    def __init__(self):

        self.output_dir = "results"

        os.makedirs(self.output_dir, exist_ok=True)

        self.filename = os.path.join(
            self.output_dir,
            "experiment_results.csv"
        )

        if not os.path.exists(self.filename):

            with open(self.filename, "w", newline="") as file:

                writer = csv.writer(file)

                writer.writerow([
                    "Timestamp",
                    "Experiment",
                    "Traffic Type",
                    "Flows",
                    "Packets",
                    "Bytes",
                    "Entropy",
                    "Risk Score",
                    "Risk Level",
                    "Action",
                    "Detection Time (ms)"
                ])

    def log(
        self,
        experiment,
        traffic_type,
        feature,
        result,
        detection_time_ms
    ):

        with open(self.filename, "a", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                experiment,
                traffic_type,
                feature.flow_count,
                feature.packet_count,
                feature.byte_count,
                round(feature.entropy, 4),
                round(result.score, 4),
                result.level.value,
                result.action,
                round(detection_time_ms, 3)
            ])

        print("\nResults saved to:")
        print(self.filename)