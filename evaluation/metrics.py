"""
metrics.py

Evaluation Metrics for ACARA

Reads experiment_results.csv and computes:

- Accuracy
- Precision
- Recall
- F1-score
- False Positive Rate

Author:
G. Sankar
"""

import csv


def evaluate(csv_file):

    TP = FP = TN = FN = 0

    with open(csv_file, newline="") as file:

        reader = csv.DictReader(file)

        for row in reader:

            # Skip extra evaluation rows
            if row["Traffic Type"].strip().lower() == "unknown":
                continue

            truth = row["Ground Truth"].strip().upper()
            prediction = row["Predicted"].strip().upper()

            # Normalize labels
            if truth == "NORMAL":
                truth = "BENIGN"

            if prediction == "NORMAL":
                prediction = "BENIGN"

            if truth == "ATTACK" and prediction == "ATTACK":
                TP += 1

            elif truth == "BENIGN" and prediction == "BENIGN":
                TN += 1

            elif truth == "BENIGN" and prediction == "ATTACK":
                FP += 1

            elif truth == "ATTACK" and prediction == "BENIGN":
                FN += 1

    total = TP + TN + FP + FN

    accuracy = (TP + TN) / total if total else 0

    precision = TP / (TP + FP) if (TP + FP) else 0

    recall = TP / (TP + FN) if (TP + FN) else 0

    f1 = (
        2 * precision * recall /
        (precision + recall)
        if (precision + recall)
        else 0
    )

    fpr = FP / (FP + TN) if (FP + TN) else 0

    print("=" * 60)
    print("ACARA EVALUATION METRICS")
    print("=" * 60)

    print(f"True Positive       : {TP}")
    print(f"True Negative       : {TN}")
    print(f"False Positive      : {FP}")
    print(f"False Negative      : {FN}")

    print()

    print(f"Accuracy            : {accuracy:.4f}")
    print(f"Precision           : {precision:.4f}")
    print(f"Recall              : {recall:.4f}")
    print(f"F1-Score            : {f1:.4f}")
    print(f"False Positive Rate : {fpr:.4f}")

    return {
        "tp": TP,
        "tn": TN,
        "fp": FP,
        "fn": FN,
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "fpr": fpr
    }


if __name__ == "__main__":

    evaluate("results/experiment_results.csv")