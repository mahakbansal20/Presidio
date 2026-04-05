# main.py

from analyzer_setup import get_analyzer
from processor import process_text


def run_realtime():
    print("🔍 PII Detection System (Type 'exit' to quit)\n")

    analyzer = get_analyzer()  # load once

    while True:
        text = input("Enter text: ")

        if text.lower() == "exit":
            print("Exiting...")
            break

        if not text.strip():
            print("⚠️ Empty input, try again\n")
            continue

        # Process input
        results = process_text(analyzer, text)

        # Print results
        print("\n✅ Detected PII:")
        if not results:
            print("No PII found.\n")
        else:
            for r in results:
                print(
                    f"{r['type']} → {r['value']} "
                    f"(Risk: {r['risk']}, Confidence: {r['confidence']})"
                )
            print()


if __name__ == "__main__":
    run_realtime()