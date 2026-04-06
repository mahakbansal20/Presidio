# evaluation.py

import json
import time

from analyzer_setup import get_analyzer
from processor import process_text


def evaluate(ground_truth_file):
    analyzer = get_analyzer()

    with open(ground_truth_file, "r") as f:
        data = json.load(f)

    TP, FP, FN = 0, 0, 0
    total_time = 0

    for item in data:
        text = item["text"]
        gt_entities = item["entities"]

        start_time = time.time()
        pred_entities = process_text(analyzer, text)
        total_time += (time.time() - start_time)

        gt_set = set((e["type"], e["value"]) for e in gt_entities)
        pred_set = set((e["type"], e["value"]) for e in pred_entities)

        TP += len(gt_set & pred_set)
        FP += len(pred_set - gt_set)
        FN += len(gt_set - pred_set)

    # Metrics
    precision = TP / (TP + FP) if (TP + FP) else 0
    recall = TP / (TP + FN) if (TP + FN) else 0
    accuracy = TP / (TP + FP + FN) if (TP + FP + FN) else 0
    f1 = (2 * precision * recall) / (precision + recall) if (precision + recall) else 0
    avg_time = total_time / len(data)

    print("\n📊 Evaluation Summary:")
    print(f"TP: {TP}, FP: {FP}, FN: {FN}")
    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")
    print(f"Accuracy: {accuracy:.2f}")
    print(f"F1 Score: {f1:.2f}")
    print(f"Avg Inference Time: {avg_time:.4f} sec")


if __name__ == "__main__":
    evaluate("ground_truth.json")