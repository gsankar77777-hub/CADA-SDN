"""
evaluate_generated_dataset.py

Evaluate every PCAP inside the generated
ACARA dataset.

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


DATASET_DIR = "datasets"

OUTPUT_FILE = "results/generated_dataset_results.csv"


def get_attack_category(filename):

    filename = filename.lower()

    if filename.startswith("normal"):
        return "Normal"

    if filename.startswith("udp"):
        return "UDP Flood"

    if filename.startswith("syn"):
        return "SYN Flood"

    if filename.startswith("icmp"):
        return "ICMP Flood"

    return "Unknown"


def get_pcap_files():

    files = []

    for filename in sorted(os.listdir(DATASET_DIR)):

        if filename.endswith(".pcap"):

            files.append(filename)

    return files
def main():

    files = get_pcap_files()

    os.makedirs("results", exist_ok=True)

    with open(
        OUTPUT_FILE,
        "w",
        newline=""
    ) as f:

        writer = csv.writer(f)

        writer.writerow([
            "File",
            "Category",
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

        print("=" * 70)
        print("ACARA GENERATED DATASET EVALUATION")
        print("=" * 70)

        for index, filename in enumerate(files, start=1):

            filepath = os.path.join(
                DATASET_DIR,
                filename
            )

            category = get_attack_category(
                filename
            )

            print()
            print("-" * 70)
            print(f"[{index}/{total}] {filename}")
            print(f"Category : {category}")

            stats = PCAPParser.parse(
                filepath
            )

            feature = FeatureExtractor.extract(
                stats
            )

            normalized = FeatureNormalizer.normalize_features(
                feature
            )

            start = time.perf_counter()

            result = AdaptiveRiskEngine.calculate(
                normalized
            )

            detection_time = (
                time.perf_counter() - start
            ) * 1000

            print(f"Packets : {feature.packet_count}")
            print(f"Flows   : {feature.flow_count}")
            print(f"Entropy : {feature.entropy:.4f}")
            print(f"Risk    : {result.level.value}")
            print(f"Score   : {result.score:.4f}")
            print(f"Time    : {detection_time:.4f} ms")

            writer.writerow([
                filename,
                category,
                feature.flow_count,
                feature.packet_count,
                feature.byte_count,
                round(feature.entropy, 4),
                round(result.score, 4),
                result.level.value,
                result.action,
                round(detection_time, 4)
            ])

    print()
    print("=" * 70)
    print("GENERATED DATASET EVALUATION COMPLETED")
    print("=" * 70)
    print()
    print("Results saved to:")
    print(OUTPUT_FILE)


if __name__ == "__main__":
    main()