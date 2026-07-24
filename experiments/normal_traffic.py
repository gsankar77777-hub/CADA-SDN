"""
normal_traffic.py

Experiment 1
Generate normal network traffic using Mininet.

Author:
G. Sankar
"""

from mininet.net import Mininet
from mininet.topo import SingleSwitchTopo
from mininet.node import OVSBridge
from mininet.log import setLogLevel


def run():
    """
    Starts a Mininet network, generates normal ICMP traffic,
    and returns basic experiment statistics.
    """

    # Create topology
    topo = SingleSwitchTopo(k=2)

    # Create Mininet network without a controller
    net = Mininet(
        topo=topo,
        switch=OVSBridge,
        controller=None,
    )

    print("=" * 60)
    print("Starting Mininet")
    print("=" * 60)

    net.start()

    h1 = net.get("h1")
    h2 = net.get("h2")

    print("\n" + "=" * 60)
    print("Connectivity Test")
    print("=" * 60)

    net.pingAll()

    print("\n" + "=" * 60)
    print("Generating Normal Traffic")
    print("=" * 60)

    output = h1.cmd("ping -c 5 10.0.0.2")

    print(output)

    # Basic experiment statistics
    experiment_stats = {
        "src_ip": "10.0.0.1",
        "dst_ip": "10.0.0.2",
        "packet_count": 5,
        "byte_count": 5 * 84,   # Approximate ICMP packet size
        "protocol": "ICMP",
    }

    print("\n" + "=" * 60)
    print("Experiment Statistics")
    print("=" * 60)

    for key, value in experiment_stats.items():
        print(f"{key:15}: {value}")

    print("\nStopping Mininet...")

    net.stop()

    print("Experiment Finished.")

    return experiment_stats


if __name__ == "__main__":

    setLogLevel("info")

    stats = run()

    print("\nReturned Statistics")

    for key, value in stats.items():
        print(f"{key:15}: {value}")