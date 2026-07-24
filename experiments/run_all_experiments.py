"""
run_all_experiments.py

Master Experiment Runner

Runs all ACARA experiments automatically.

Author:
G. Sankar
"""

import subprocess
import time


EXPERIMENTS = [

    (
        "Normal Traffic",
        "experiments/capture_traffic.py",
        "datasets/normal_001.pcap",
    ),

    (
        "ICMP Flood",
        "experiments/capture_icmp_flood.py",
        "datasets/icmp_flood_001.pcap",
    ),

    (
        "TCP SYN Flood",
        "experiments/capture_syn_flood.py",
        "datasets/syn_flood_001.pcap",
    ),

    (
        "UDP Flood",
        "experiments/capture_udp_flood.py",
        "datasets/udp_flood_001.pcap",
    ),

]


def run():

    print("=" * 70)
    print("ACARA AUTOMATED EXPERIMENT SUITE")
    print("=" * 70)

    for name, experiment, pcap in EXPERIMENTS:

        print("\n" + "=" * 70)
        print("Running:", name)
        print("=" * 70)

        # Clean Mininet
        subprocess.run(
            ["sudo", "mn", "-c"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

        # Run traffic generation
        subprocess.run(
            ["sudo", "python3", experiment],
            check=True,
        )

        print("\nAnalyzing PCAP...")

        subprocess.run(
            [
                "python3",
                "experiments/analyze_attack.py",
                pcap,
            ],
            check=True,
        )

        print("\nCompleted:", name)

        time.sleep(2)

    print("\n" + "=" * 70)
    print("ALL EXPERIMENTS FINISHED SUCCESSFULLY")
    print("=" * 70)


if __name__ == "__main__":

    run()