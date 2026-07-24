"""
generate_graphs.py

Publication-quality graph generation
for the ACARA framework evaluation.

Author : G. Sankar
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

RESULT_FILE = "results/cic_results.csv"
GRAPH_DIR = "graphs"

os.makedirs(GRAPH_DIR, exist_ok=True)


def load_results():

    if not os.path.exists(RESULT_FILE):
        raise FileNotFoundError(
            f"{RESULT_FILE} not found."
        )

    return pd.read_csv(RESULT_FILE)


def set_plot_style():

    plt.style.use("default")

    plt.rcParams["figure.figsize"] = (12, 6)
    plt.rcParams["figure.dpi"] = 300

    plt.rcParams["font.family"] = "DejaVu Sans"
    plt.rcParams["font.size"] = 13

    plt.rcParams["axes.titlesize"] = 16
    plt.rcParams["axes.titleweight"] = "bold"

    plt.rcParams["axes.labelsize"] = 13

    plt.rcParams["xtick.labelsize"] = 11
    plt.rcParams["ytick.labelsize"] = 11

    plt.rcParams["axes.grid"] = True
    plt.rcParams["grid.alpha"] = 0.25


def bytes_formatter(value, pos):
    return f"{value/1e6:.0f}"


def save_bar_chart(
    dataframe,
    column,
    title,
    ylabel,
    filename,
    byte_axis=False
):

    fig, ax = plt.subplots()

    ax.bar(
        dataframe["File"],
        dataframe[column]
    )

    ax.set_title(title)

    ax.set_xlabel("PCAP Samples")

    ax.set_ylabel(ylabel)

    plt.xticks(
        rotation=40,
        ha="right"
    )

    if byte_axis:
        ax.yaxis.set_major_formatter(
            FuncFormatter(bytes_formatter)
        )

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            GRAPH_DIR,
            filename
        ),
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()


def save_line_chart(
    dataframe,
    column,
    title,
    ylabel,
    filename
):

    plt.figure()

    plt.plot(
        dataframe["File"],
        dataframe[column],
        marker="o",
        linewidth=2.5,
        markersize=6
    )

    plt.title(title)

    plt.xlabel("PCAP Samples")

    plt.ylabel(ylabel)

    plt.xticks(
        rotation=40,
        ha="right"
    )

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            GRAPH_DIR,
            filename
        ),
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()
def save_feature_comparison(dataframe):

    feature_map = {
        "Entropy": "Entropy",
        "Flows": "Flow Count",
        "Packets": "Packet Count",
        "Bytes": "Byte Count"
    }

    normalized = dataframe[list(feature_map.keys())].copy()

    for column in feature_map.keys():

        minimum = normalized[column].min()
        maximum = normalized[column].max()

        if maximum != minimum:
            normalized[column] = (
                normalized[column] - minimum
            ) / (
                maximum - minimum
            )
        else:
            normalized[column] = 0

    plt.figure(figsize=(12,6))

    for column, label in feature_map.items():

        plt.plot(
            dataframe["File"],
            normalized[column],
            marker="o",
            linewidth=2,
            markersize=5,
            label=label
        )

    plt.title(
        "Normalized Feature Comparison Across Evaluated PCAP Samples"
    )

    plt.xlabel("PCAP Samples")

    plt.ylabel("Normalized Value")

    plt.xticks(
        rotation=40,
        ha="right"
    )

    plt.legend()

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            GRAPH_DIR,
            "feature_comparison.png"
        ),
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()


def main():

    print("=" * 60)
    print("Generating Publication-Quality Graphs")
    print("=" * 60)

    set_plot_style()

    dataframe = load_results()

    save_bar_chart(
        dataframe,
        "Detection Time (ms)",
        "Detection Time Across Evaluated PCAP Samples",
        "Detection Time (ms)",
        "detection_time.png"
    )

    save_bar_chart(
        dataframe,
        "Entropy",
        "Entropy Distribution Across Evaluated PCAP Samples",
        "Entropy",
        "entropy.png"
    )

    save_bar_chart(
        dataframe,
        "Packets",
        "Packet Count Across Evaluated PCAP Samples",
        "Packet Count",
        "packet_count.png"
    )

    save_bar_chart(
        dataframe,
        "Flows",
        "Flow Count Across Evaluated PCAP Samples",
        "Flow Count",
        "flow_count.png"
    )

    save_bar_chart(
        dataframe,
        "Bytes",
        "Traffic Volume Across Evaluated PCAP Samples",
        "Traffic Volume (MB)",
        "byte_count.png",
        byte_axis=True
    )

    save_line_chart(
        dataframe,
        "Risk Score",
        "Risk Score Across Evaluated PCAP Samples",
        "Risk Score",
        "risk_score.png"
    )

    save_feature_comparison(
        dataframe
    )

    print()
    print("=" * 60)
    print("Graphs Generated Successfully")
    print("=" * 60)
    print()
    print("Saved to:")
    print(GRAPH_DIR)


if __name__ == "__main__":
    main()