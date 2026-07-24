"""
experiment_logger.py

Unified ACARA Experiment Logger

Author:
G. Sankar
"""

import csv
import os
from datetime import datetime


RESULT_DIR = "results"
RESULT_FILE = os.path.join(
    RESULT_DIR,
    "experiment_results.csv"
)


class ExperimentLogger:

    def __init__(self):

        os.makedirs(RESULT_DIR, exist_ok=True)

        if not os.path.exists(RESULT_FILE):

            with open(
                RESULT_FILE,
                "w",
                newline=""
            ) as file:

                writer = csv.writer(file)

                writer.writerow([
                    "Timestamp",
                    "Run ID",
                    "Traffic Type",
                    "Ground Truth",
                    "Predicted",
                    "Flows",
                    "Packets",
                    "Bytes",
                    "Entropy",
                    "Risk Score",
                    "Risk Level",
                    "Action",
                    "Detection Time (ms)"
                ])

    def next_run_id(self):

        if not os.path.exists(RESULT_FILE):
            return 1

        with open(RESULT_FILE) as file:

            rows = list(csv.reader(file))

            return len(rows)

    def log(
        self,
        traffic_type,
        ground_truth,
        feature,
        result,
        detection_time_ms
    ):

        predicted = (
            "NORMAL"
            if result.level.value == "LOW"
            else "ATTACK"
        )

        with open(
            RESULT_FILE,
            "a",
            newline=""
        ) as file:

            writer = csv.writer(file)

            writer.writerow([

                datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),

                self.next_run_id(),

                traffic_type,

                ground_truth,

                predicted,

                feature.flow_count,

                feature.packet_count,

                feature.byte_count,

                round(feature.entropy, 4),

                round(result.score, 4),

                result.level.value,

                result.action,

                round(
                    detection_time_ms,
                    4
                )

            ])

        print("\nResult saved to:")
        print(RESULT_FILE)