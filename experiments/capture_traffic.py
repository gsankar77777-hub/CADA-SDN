"""
capture_traffic.py

Capture real network traffic from Mininet
and save it as a PCAP file.

Research Version 3.0

Author:
G. Sankar
"""

import os
import time
import signal
import subprocess

from mininet.net import Mininet
from mininet.topo import SingleSwitchTopo
from mininet.node import OVSBridge
from mininet.log import setLogLevel


DATASET_DIR = "datasets"


def get_next_filename(prefix):
    """
    Returns the next available PCAP filename.

    Example:
        normal_001.pcap
        normal_002.pcap
        ...
    """

    os.makedirs(DATASET_DIR, exist_ok=True)

    index = 1

    while True:

        filename = os.path.join(
            DATASET_DIR,
            f"{prefix}_{index:03d}.pcap"
        )

        if not os.path.exists(filename):
            return filename

        index += 1


def run():

    os.makedirs(DATASET_DIR, exist_ok=True)

    topo = SingleSwitchTopo(k=2)

    net = Mininet(
        topo=topo,
        switch=OVSBridge,
        controller=None
    )

    print("=" * 60)
    print("Starting Mininet")
    print("=" * 60)

    net.start()

    h1 = net.get("h1")

    # Automatically choose next filename
    pcap_file = get_next_filename("normal")

    print("\nStarting packet capture...")

    capture = subprocess.Popen(
        [
            "sudo",
            "tcpdump",
            "-i",
            "s1-eth1",
            "-n",
            "-U",
            "-w",
            pcap_file,
            "icmp or arp"
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    # Give tcpdump time to initialize
    time.sleep(2)

    print("Generating ICMP Traffic...\n")

    print(
        h1.cmd("ping -c 10 10.0.0.2")
    )

    # Allow remaining packets to be captured
    time.sleep(2)

    print("Stopping packet capture...")

    capture.send_signal(signal.SIGINT)

    try:
        capture.wait(timeout=5)
    except subprocess.TimeoutExpired:
        capture.kill()

    print("\nStopping Mininet...")

    net.stop()

    print("\n" + "=" * 60)
    print("Capture Completed")
    print("=" * 60)

    print("PCAP File :")
    print(pcap_file)

    if os.path.exists(pcap_file):

        size = os.path.getsize(pcap_file)

        print(f"Capture Size : {size} bytes")

    else:

        print("ERROR : PCAP file was not created.")


if __name__ == "__main__":

    setLogLevel("info")

    run()