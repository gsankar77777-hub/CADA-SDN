"""
run_experiment.py

Research Experiment Runner

Version 1.1
"""

import os


def banner():
    print("\n" + "=" * 70)
    print("        ACARA RESEARCH EXPERIMENT RUNNER")
    print("=" * 70)


def menu():
    print("\nSelect Experiment\n")
    print("1. Normal Traffic")
    print("2. ICMP Flood")
    print("3. Run Normal Traffic 10 Times")
    print("4. Exit")


def run_normal():
    print("\nRunning Normal Traffic...\n")
    os.system("sudo python3 experiments/normal_traffic.py")
    os.system("python3 experiments/test_logger.py")


def run_icmp():
    print("\nRunning ICMP Flood...\n")
    os.system("sudo python3 experiments/ddos_attack.py")


def run_normal_multiple():

    for i in range(10):

        print("\n" + "=" * 60)
        print(f"Experiment {i+1}/10")
        print("=" * 60)

        run_normal()


while True:

    banner()

    menu()

    choice = input("\nEnter Choice : ")

    if choice == "1":

        run_normal()

    elif choice == "2":

        run_icmp()

    elif choice == "3":

        run_normal_multiple()

    elif choice == "4":

        print("\nExiting...")
        break

    else:

        print("\nInvalid Choice.")