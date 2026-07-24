"""
ddos_attack.py

Experiment 2
ICMP Flood using Mininet + hping3

Author:
G. Sankar
"""

from mininet.net import Mininet
from mininet.topo import SingleSwitchTopo
from mininet.node import OVSBridge
from mininet.cli import CLI
from mininet.log import setLogLevel


def run():

    topo = SingleSwitchTopo(k=2)

    net = Mininet(
        topo=topo,
        switch=OVSBridge,
        controller=None,
    )

    print("=" * 60)
    print("Starting Network")
    print("=" * 60)

    net.start()

    h1 = net.get("h1")
    h2 = net.get("h2")

    print("\nTesting connectivity...")

    net.pingAll()

    print("\nGenerating ICMP Flood...")

    print(
        h1.cmd(
            "timeout 5 hping3 --icmp --flood 10.0.0.2"
        )
    )

    print("\nFlood Finished.")

    CLI(net)

    net.stop()


if __name__ == "__main__":
    setLogLevel("info")
    run()