# main.py

import time
import json
import os

from analyzer_setup import get_analyzer
from processor import process_text


# 🔹 Benchmark stats
total_requests = 0
total_time = 0


def run_realtime():
    global total_requests, total_time

    print("🔍 PII Detection + Benchmarking (type 'exit' to quit)\n")

    analyzer = get_analyzer()

    # 🔥 Warm-up (important for fair latency)
    process_text(analyzer, "warmup")

    while True:
        text = input("Enter text: ")

        if text.lower() == "exit":
            print("\n📊 Final Summary:")
            if total_requests > 0:
                avg_latency = total_time / total_requests
                throughput = total_requests / total_time

                print(f"Total Requests: {total_requests}")
                print(f"Average Latency: {avg_latency:.5f} sec")
                print(f"Throughput: {throughput:.2f} req/sec")
            print("Exiting...")
            break

        if not text.strip():
            continue

        # 🔴 Measure latency
        start = time.time()

        result = process_text(analyzer, text)

        end = time.time()
        latency = end - start

        # Update stats
        total_requests += 1
        total_time += latency

        entities = result["entities"]

        # 🔹 Print PII results
        print("\n✅ Detected PII:")
        if not entities:
            print("No PII found.")
        else:
            for r in entities:
                print(
                    f"{r['type']} → {r['value']} "
                    f"(Risk: {r['risk']}, Confidence: {r['confidence']})"
                )

        # 🔹 Print risk
        print(f"\n🔴 Risk Level: {result['risk_level']}")

        # 🔴 Benchmark Output
        avg_latency = total_time / total_requests
        throughput = total_requests / total_time

        print("\n⚡ Performance Metrics:")
        print(f"Latency (current): {latency:.5f} sec")
        print(f"Average Latency: {avg_latency:.5f} sec")
        print(f"Throughput: {throughput:.2f} req/sec\n")


if __name__ == "__main__":
    run_realtime()