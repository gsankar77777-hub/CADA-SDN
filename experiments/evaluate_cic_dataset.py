"""
evaluate_cic_dataset.py

Evaluate the CIC-DDoS2019 public dataset
using the complete ACARA pipeline.

Author:
G. Sankar
"""

import os
import csv
import time
import sys

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

sys.path.append(
    os.path.join(PROJECT_ROOT, "src", "detection")
)

sys.path.append(
    os.path.join(PROJECT_ROOT, "src", "mitigation")
)

from pcap_parser import PCAPParser
from features import FeatureExtractor
from normalizer import FeatureNormalizer
from adaptive_risk_engine import AdaptiveRiskEngine


DATASET_DIR = "public_dataset/sample"

OUTPUT_FILE = "results/cic_results.csv"


def main():

    print("=" * 70)
    print("ACARA PUBLIC DATASET EVALUATION")
    print("=" * 70)

    if not os.path.exists(DATASET_DIR):

        print("\nERROR:")
        print("Dataset directory not found:")
        print(DATASET_DIR)
        return

    files = sorted(
        f for f in os.listdir(DATASET_DIR)
        if os.path.isfile(
            os.path.join(DATASET_DIR, f)
        )
    )

    if len(files) == 0:

        print("\nNo PCAP files found.")
        return

    os.makedirs("results", exist_ok=True)

    with open(
        OUTPUT_FILE,
        "w",
        newline=""
    ) as csvfile:

        writer = csv.writer(csvfile)

        writer.writerow([
            "File",
            "Flows",
            "Packets",
            "Bytes",
            "Entropy",
            "Risk Score",
            "Risk Level",
            "Action",
            "Detection Time (ms)"
        ])

        total = len(files)

        for index, filename in enumerate(files, start=1):

            path = os.path.join(
                DATASET_DIR,
                filename
            )

            print("\n" + "-" * 60)
            print(
                f"[{index}/{total}] {filename}"
            )

            try:

                print("Parsing PCAP...")

                stats = PCAPParser.parse(path)

                feature = FeatureExtractor.extract(
                    stats
                )

                normalized = (
                    FeatureNormalizer.normalize_features(
                        feature
                    )
                )

                start = time.perf_counter()

                result = AdaptiveRiskEngine.calculate(
                    normalized
                )

                detection_time = (
                    time.perf_counter() - start
                ) * 1000

                writer.writerow([
                    filename,
                    feature.flow_count,
                    feature.packet_count,
                    feature.byte_count,
                    round(feature.entropy, 4),
                    round(result.score, 4),
                    result.level.value,
                    result.action,
                    round(detection_time, 4)
                ])

                print(
                    f"Packets : {feature.packet_count}"
                )

                print(
                    f"Flows   : {feature.flow_count}"
                )

                print(
                    f"Entropy : {feature.entropy:.4f}"
                )

                print(
                    f"Risk    : {result.level.value}"
                )

                print(
                    f"Score   : {result.score:.4f}"
                )

                print(
                    f"Time    : {detection_time:.4f} ms"
                )

            except Exception as e:

                print(
                    f"ERROR processing {filename}"
                )

                print(e)

    print("\n" + "=" * 70)
    print("PUBLIC DATASET EVALUATION COMPLETED")
    print("=" * 70)

    print("\nResults saved to:")
    print(OUTPUT_FILE)


if __name__ == "__main__":
    main()