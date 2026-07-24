"""
batch_evaluation.py

Automatically evaluates every PCAP dataset
generated for ACARA.

Author:
G. Sankar
"""

import os
import glob
import subprocess


DATASET_DIR = "datasets"


def sort_key(filename):

    name = os.path.basename(filename)

    prefix = name.split("_")[0]

    number = int(
        name.split("_")[-1]
        .replace(".pcap", "")
    )

    return (prefix, number)


def main():

    print("=" * 70)
    print("ACARA DATASET EVALUATION")
    print("=" * 70)

    csv_file = "results/experiment_results.csv"

    if os.path.exists(csv_file):

        os.remove(csv_file)

        print("Old experiment log removed.")

    pcap_files = sorted(
        glob.glob(
            os.path.join(DATASET_DIR, "*.pcap")
        ),
        key=sort_key
    )

    total = len(pcap_files)

    print(f"\nFound {total} PCAP files.\n")

    for index, pcap in enumerate(pcap_files, start=1):

        print(
            f"[{index}/{total}] "
            f"{os.path.basename(pcap)}"
        )

        subprocess.run(
            [
                "python3",
                "experiments/analyze_attack.py",
                pcap
            ],
            check=True,
            stdout=subprocess.DEVNULL
        )

    print("\n" + "=" * 70)
    print("EVALUATION COMPLETED")
    print("=" * 70)

    print("\nResults saved to:")

    print(csv_file)

    print("\nTotal Evaluated :", total)


if __name__ == "__main__":

    main()