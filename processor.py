# processor.py

from pii_config import get_priority, get_risk_level, get_entity_category


# 🔹 1. Remove low-confidence detections
def filter_low_confidence(results, threshold=0.7):
    return [r for r in results if r.score >= threshold]


# 🔹 2. Resolve overlapping entities using priority
def resolve_conflicts(results):
    # Sort by start position, then higher confidence first
    results = sorted(results, key=lambda x: (x.start, -x.score))

    final = []

    for r in results:
        keep = True

        for f in final:
            # Check overlap
            if not (r.end <= f.start or r.start >= f.end):

                # Compare priority (NOT just score)
                if get_priority(r.entity_type) > get_priority(f.entity_type):
                    final.remove(f)
                    final.append(r)
                else:
                    keep = False

                break

        if keep:
            final.append(r)

    return final


# 🔹 3. Remove duplicate detections
def remove_duplicates(results, text):
    seen = set()
    unique = []

    for r in results:
        value = text[r.start:r.end]
        key = (r.entity_type, value)

        if key not in seen:
            seen.add(key)
            unique.append(r)

    return unique


# 🔹 4. Format results into structured JSON
def format_output(results, text):
    entities = []

    for r in results:
        value = text[r.start:r.end]

        entities.append({
            "type": r.entity_type,
            "value": value,
            "start": r.start,
            "end": r.end,
            "confidence": round(r.score, 2),
            "risk": get_risk_level(r.entity_type),
            "category": get_entity_category(r.entity_type)
        })

    return entities


# 🔹 5. Row-level risk classification
def get_row_risk(entities):
    risks = [e["risk"] for e in entities]

    if "RED" in risks:
        return "HIGH"
    elif "YELLOW" in risks:
        return "MEDIUM"
    elif "GREEN" in risks:
        return "LOW"
    return "NONE"


# 🔹 6. FULL PIPELINE (Main function)
def process_text(analyzer, text):
    # Step 1: Detect PII
    results = analyzer.analyze(text=text, language="en")

    # Step 2: Filter low-confidence noise
    results = filter_low_confidence(results)

    # Step 3: Resolve overlapping entities
    results = resolve_conflicts(results)

    # Step 4: Remove duplicates
    results = remove_duplicates(results, text)

    # Step 5: Format output
    entities = format_output(results, text)

    # Step 6: Row-level risk
    row_risk = get_row_risk(entities)

    return {
        "text": text,
        "risk_level": row_risk,
        "entities": entities
    }