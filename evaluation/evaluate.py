"""
evaluate.py

ACARA Performance Evaluation

Author:
G. Sankar
"""

import csv
import os

RESULT_FILE = "results/experiment_results.csv"


def safe_div(a, b):
    if b == 0:
        return 0
    return a / b


def evaluate():

    if not os.path.exists(RESULT_FILE):

        print("Results file not found.")
        return

    TP = TN = FP = FN = 0

    detection_times = []

    risk_scores = []

    with open(RESULT_FILE) as file:

        reader = csv.DictReader(file)

        for row in reader:

            gt = row["Ground Truth"].strip().upper()
            pred = row["Predicted"].strip().upper()

            detection_times.append(
                float(row["Detection Time (ms)"])
            )

            risk_scores.append(
                float(row["Risk Score"])
            )

            if gt == "ATTACK" and pred == "ATTACK":
                TP += 1

            elif gt == "NORMAL" and pred == "NORMAL":
                TN += 1

            elif gt == "NORMAL" and pred == "ATTACK":
                FP += 1

            elif gt == "ATTACK" and pred == "NORMAL":
                FN += 1

    total = TP + TN + FP + FN

    accuracy = safe_div(TP + TN, total)

    precision = safe_div(TP, TP + FP)

    recall = safe_div(TP, TP + FN)

    f1 = safe_div(
        2 * precision * recall,
        precision + recall
    )

    fpr = safe_div(FP, FP + TN)

    avg_detection = safe_div(
        sum(detection_times),
        len(detection_times)
    )

    avg_risk = safe_div(
        sum(risk_scores),
        len(risk_scores)
    )

    print("=" * 60)
    print("ACARA PERFORMANCE EVALUATION")
    print("=" * 60)

    print()

    print("Total Experiments :", total)

    print()

    print("True Positive     :", TP)
    print("True Negative     :", TN)
    print("False Positive    :", FP)
    print("False Negative    :", FN)

    print()

    print("Accuracy          : {:.4f}".format(accuracy))
    print("Precision         : {:.4f}".format(precision))
    print("Recall            : {:.4f}".format(recall))
    print("F1 Score          : {:.4f}".format(f1))
    print("False Positive Rate : {:.4f}".format(fpr))

    print()

    print("Average Detection Time : {:.4f} ms".format(
        avg_detection
    ))

    print("Average Risk Score     : {:.4f}".format(
        avg_risk
    ))


if __name__ == "__main__":
    evaluate()