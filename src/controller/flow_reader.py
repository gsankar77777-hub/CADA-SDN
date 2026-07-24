"""
flow_reader.py

Reads live Open vSwitch flow statistics.
"""

import subprocess


class FlowReader:

    @staticmethod
    def read_flows(switch="s1"):

        command = ["sudo", "ovs-ofctl", "dump-flows", switch]

        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
        )

        if result.returncode != 0:

            print("=" * 60)
            print("ERROR")
            print("=" * 60)
            print(result.stderr)

            return None

        return result.stdout


if __name__ == "__main__":

    output = FlowReader.read_flows()

    if output:
        print(output)