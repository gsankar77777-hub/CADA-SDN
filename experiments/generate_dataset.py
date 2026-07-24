"""
generate_dataset.py

Automatically generates multiple independent
PCAP datasets for ACARA.

Author:
G. Sankar
"""

import subprocess
import time


RUNS_PER_SCENARIO = 20


EXPERIMENTS = [

    (
        "Normal Traffic",
        "experiments/capture_traffic.py",
    ),

    (
        "ICMP Flood",
        "experiments/capture_icmp_flood.py",
    ),

    (
        "TCP SYN Flood",
        "experiments/capture_syn_flood.py",
    ),

    (
        "UDP Flood",
        "experiments/capture_udp_flood.py",
    ),

]


def clean_mininet():

    subprocess.run(
        [
            "sudo",
            "mn",
            "-c"
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def run():

    total = RUNS_PER_SCENARIO * len(EXPERIMENTS)

    current = 1

    print("=" * 70)
    print("ACARA DATASET GENERATOR")
    print("=" * 70)

    for name, script in EXPERIMENTS:

        print("\n" + "=" * 70)
        print(name)
        print("=" * 70)

        for i in range(RUNS_PER_SCENARIO):

            print(
                f"[{current}/{total}] "
                f"Generating {name} "
                f"({i+1}/{RUNS_PER_SCENARIO})"
            )

            clean_mininet()

            subprocess.run(
                [
                    "sudo",
                    "python3",
                    script,
                ],
                check=True,
            )

            current += 1

            time.sleep(2)

    print("\n" + "=" * 70)
    print("DATASET GENERATION COMPLETED")
    print("=" * 70)

    print("\nGenerated approximately:")

    print(f"{RUNS_PER_SCENARIO} Normal PCAPs")
    print(f"{RUNS_PER_SCENARIO} ICMP Flood PCAPs")
    print(f"{RUNS_PER_SCENARIO} TCP SYN Flood PCAPs")
    print(f"{RUNS_PER_SCENARIO} UDP Flood PCAPs")


if __name__ == "__main__":

    run()