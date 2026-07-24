"""
generate_generated_graphs.py

Publication-quality graph generation for the
ACARA Generated Dataset.

Author:
G. Sankar
"""

import os

import pandas as pd

import matplotlib.pyplot as plt

from sklearn.metrics import (
    confusion_matrix,
    ConfusionMatrixDisplay,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

RESULT_FILE = "results/experiment_results.csv"

GRAPH_DIR = "graphs/generated"

os.makedirs(
    GRAPH_DIR,
    exist_ok=True
)


def set_plot_style():

    plt.style.use("default")

    plt.rcParams["figure.figsize"] = (10, 6)

    plt.rcParams["figure.dpi"] = 300

    plt.rcParams["font.family"] = "DejaVu Sans"

    plt.rcParams["font.size"] = 13

    plt.rcParams["axes.titlesize"] = 16

    plt.rcParams["axes.titleweight"] = "bold"

    plt.rcParams["axes.labelsize"] = 13

    plt.rcParams["xtick.labelsize"] = 11

    plt.rcParams["ytick.labelsize"] = 11

    plt.rcParams["axes.grid"] = True

    plt.rcParams["grid.alpha"] = 0.15
def load_results():

    """
    Load experiment results and
    perform automatic cleaning.
    """

    if not os.path.exists(RESULT_FILE):

        raise FileNotFoundError(
            f"{RESULT_FILE} not found."
        )

    dataframe = pd.read_csv(
        RESULT_FILE
    )

    # Remove the extra evaluation row
    dataframe = dataframe[
        dataframe["Traffic Type"] != "Unknown"
    ].copy()

    # Standardize traffic labels
    dataframe["Traffic Type"] = (
        dataframe["Traffic Type"]
        .replace(
            {
                "TCP SYN Flood": "SYN Flood"
            }
        )
    )

    traffic_order = [
        "Normal",
        "UDP Flood",
        "SYN Flood",
        "ICMP Flood"
    ]

    dataframe["Traffic Type"] = pd.Categorical(
        dataframe["Traffic Type"],
        categories=traffic_order,
        ordered=True
    )

    dataframe = dataframe.sort_values(
        "Traffic Type"
    )

    return dataframe


def bytes_to_mb(value):

    return value / (1024 * 1024)


def grouped_statistics(
    dataframe,
    column,
    convert_bytes=False
):

    grouped = (
        dataframe
        .groupby(
            "Traffic Type",
            observed=False
        )[column]
        .agg(
            ["mean", "std", "count"]
        )
        .reset_index()
    )

    if convert_bytes:

        grouped["mean"] = grouped["mean"].apply(
            bytes_to_mb
        )

        grouped["std"] = grouped["std"].apply(
            bytes_to_mb
        )

    return grouped
def bar_chart(
    dataframe,
    column,
    title,
    ylabel,
    filename,
    convert_bytes=False
):

    grouped = grouped_statistics(
        dataframe,
        column,
        convert_bytes
    )

    plt.figure()

    if convert_bytes:

        # Traffic volume graph:
        # Mean only (no error bars)
        plt.bar(
            grouped["Traffic Type"],
            grouped["mean"]
        )

    else:

        # All remaining graphs:
        # Mean ± Standard Deviation
        plt.bar(
            grouped["Traffic Type"],
            grouped["mean"],
            yerr=grouped["std"],
            capsize=6
        )

    plt.title(
        title
    )

    plt.xlabel(
        "Traffic Type"
    )

    plt.ylabel(
        ylabel
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

    plt.close("all")


def generate_basic_graphs(dataframe):

    print("Generating Detection Time graph...")

    bar_chart(
        dataframe,
        "Detection Time (ms)",
        "Average Detection Time by Traffic Type",
        "Detection Time (ms)",
        "detection_time.png"
    )

    print("Generating Entropy graph...")

    bar_chart(
        dataframe,
        "Entropy",
        "Average Entropy by Traffic Type",
        "Entropy",
        "entropy.png"
    )

    print("Generating Packet Count graph...")

    bar_chart(
        dataframe,
        "Packets",
        "Average Packet Count by Traffic Type",
        "Packet Count",
        "packet_count.png"
    )

    print("Generating Flow Count graph...")

    bar_chart(
        dataframe,
        "Flows",
        "Average Flow Count by Traffic Type",
        "Flow Count",
        "flow_count.png"
    )

    print("Generating Traffic Volume graph...")

    bar_chart(
        dataframe,
        "Bytes",
        "Average Traffic Volume by Traffic Type",
        "Traffic Volume (MB)",
        "byte_count.png",
        convert_bytes=True
    )

    print("Generating Risk Score graph...")

    bar_chart(
        dataframe,
        "Risk Score",
        "Average Risk Score by Traffic Type",
        "Risk Score",
        "risk_score.png"
    )
def save_feature_comparison(dataframe):

    print("Generating Feature Comparison graph...")

    features = [
        "Entropy",
        "Flows",
        "Packets",
        "Bytes"
    ]

    labels = [
        "Entropy",
        "Flow Count",
        "Packet Count",
        "Traffic Volume"
    ]

    grouped = (
        dataframe
        .groupby(
            "Traffic Type",
            observed=False
        )[features]
        .mean()
        .reset_index()
    )

    normalized = grouped.copy()

    for feature in features:

        minimum = normalized[feature].min()
        maximum = normalized[feature].max()

        if maximum > minimum:

            normalized[feature] = (
                normalized[feature] - minimum
            ) / (
                maximum - minimum
            )

        else:

            normalized[feature] = 0

    plt.figure(figsize=(10, 6))

    markers = [
        "o",
        "s",
        "^",
        "D"
    ]

    for feature, label, marker in zip(
        features,
        labels,
        markers
    ):

        plt.plot(
            normalized["Traffic Type"],
            normalized[feature],
            marker=marker,
            linewidth=2,
            markersize=7,
            label=label
        )

    plt.title(
        "Normalized Feature Comparison"
    )

    plt.xlabel(
        "Traffic Type"
    )

    plt.ylabel(
        "Normalized Value"
    )

    plt.ylim(
        -0.05,
        1.05
    )

    plt.grid(
        alpha=0.25
    )

    plt.legend(
        loc="upper center",
        bbox_to_anchor=(0.5, 1.15),
        ncol=4,
        frameon=False
    )

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            GRAPH_DIR,
            "feature_comparison.png"
        ),
        dpi=300,
        bbox_inches="tight"
    )

    plt.close("all")
def save_confusion_matrix(dataframe):

    print("Generating Confusion Matrix...")

    truth = (
        dataframe["Ground Truth"]
        .astype(str)
        .str.upper()
        .replace({
            "NORMAL": "BENIGN"
        })
    )

    prediction = (
        dataframe["Predicted"]
        .astype(str)
        .str.upper()
        .replace({
            "NORMAL": "BENIGN"
        })
    )

    labels = [
        "BENIGN",
        "ATTACK"
    ]

    matrix = confusion_matrix(
        truth,
        prediction,
        labels=labels
    )

    fig, ax = plt.subplots(
        figsize=(6, 6)
    )

    display = ConfusionMatrixDisplay(
        confusion_matrix=matrix,
        display_labels=[
            "Benign",
            "Attack"
        ]
    )

    display.plot(
        cmap="Blues",
        colorbar=False,
        ax=ax,
        values_format="d"
    )

    ax.set_title(
        "Confusion Matrix",
        fontsize=16,
        fontweight="bold"
    )

    ax.set_xlabel(
        "Predicted Label"
    )

    ax.set_ylabel(
        "Ground Truth"
    )

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            GRAPH_DIR,
            "confusion_matrix.png"
        ),
        dpi=300,
        bbox_inches="tight"
    )

    plt.close("all")
def save_classification_metrics(dataframe):

    print("Generating Classification Metrics graph...")

    truth = (
        dataframe["Ground Truth"]
        .astype(str)
        .str.upper()
        .replace({
            "NORMAL": "BENIGN"
        })
    )

    prediction = (
        dataframe["Predicted"]
        .astype(str)
        .str.upper()
        .replace({
            "NORMAL": "BENIGN"
        })
    )

    accuracy = accuracy_score(
        truth,
        prediction
    )

    precision = precision_score(
        truth,
        prediction,
        pos_label="ATTACK",
        zero_division=0
    )

    recall = recall_score(
        truth,
        prediction,
        pos_label="ATTACK",
        zero_division=0
    )

    f1 = f1_score(
        truth,
        prediction,
        pos_label="ATTACK",
        zero_division=0
    )

    metric_names = [
        "Accuracy",
        "Precision",
        "Recall",
        "F1-Score"
    ]

    metric_values = [
        accuracy,
        precision,
        recall,
        f1
    ]

    plt.figure(figsize=(8, 6))

    bars = plt.bar(
        metric_names,
        metric_values
    )

    plt.title(
        "Classification Performance",
        fontsize=16,
        fontweight="bold"
    )

    plt.ylabel("Score")

    plt.ylim(0, 1.05)

    plt.grid(
        axis="y",
        alpha=0.25
    )

    for bar, value in zip(bars, metric_values):

        plt.text(
            bar.get_x() + bar.get_width() / 2,
            value + 0.015,
            f"{value:.2f}",
            ha="center",
            va="bottom",
            fontsize=11,
            fontweight="bold"
        )

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            GRAPH_DIR,
            "classification_metrics.png"
        ),
        dpi=300,
        bbox_inches="tight"
    )

    plt.close("all")
def generate_all_graphs(dataframe):

    print("\n" + "=" * 70)
    print("GENERATING PUBLICATION-QUALITY FIGURES")
    print("=" * 70)

    # Bar Charts
    generate_basic_graphs(
        dataframe
    )

    # Feature Comparison
    save_feature_comparison(
        dataframe
    )

    # Confusion Matrix
    save_confusion_matrix(
        dataframe
    )

    # Classification Metrics
    save_classification_metrics(
        dataframe
    )

    print("\nAll graphs generated successfully.\n")


def print_summary(dataframe):

    print("=" * 70)
    print("DATASET SUMMARY")
    print("=" * 70)

    summary = (
        dataframe
        .groupby(
            "Traffic Type",
            observed=False
        )
        .size()
    )

    for traffic_type, count in summary.items():

        print(
            f"{traffic_type:<12} : {count} samples"
        )

    print()

    print(
        f"Total Samples : {len(dataframe)}"
    )

    print(
        f"Output Folder : {GRAPH_DIR}"
    )

    print("=" * 70)
def main():

    print("=" * 70)
    print("ACARA GENERATED DATASET GRAPH GENERATOR")
    print("=" * 70)

    try:

        set_plot_style()

        dataframe = load_results()

        print(
            f"\nLoaded {len(dataframe)} experiment records."
        )

        generate_all_graphs(
            dataframe
        )

        print_summary(
            dataframe
        )

        print("\nGenerated graph files:\n")

        for filename in sorted(os.listdir(GRAPH_DIR)):

            print(f"  ✓ {filename}")

        print("\nGraph generation completed successfully.")

    except FileNotFoundError as error:

        print("\nERROR:")
        print(error)

    except Exception as error:

        print("\nUNEXPECTED ERROR:")
        print(error)


if __name__ == "__main__":

    main()