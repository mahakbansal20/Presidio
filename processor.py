# processor.py

from pii_config import get_priority, get_risk_level, get_entity_category


# 1. Remove low-confidence noise
def filter_low_confidence(results, threshold=0.6):
    return [r for r in results if r.score >= threshold]


# ✅ 2. Resolve overlapping entities (MOST IMPORTANT)
def resolve_conflicts(results):
    # Sort by start index, then by highest score
    results = sorted(results, key=lambda x: (x.start, -x.score))

    final = []

    for r in results:
        keep = True

        for f in final:
            # Check overlap
            if not (r.end <= f.start or r.start >= f.end):

                # Compare priority (not just score)
                if get_priority(r.entity_type) > get_priority(f.entity_type):
                    final.remove(f)
                    final.append(r)
                else:
                    keep = False
                break

        if keep:
            final.append(r)

    return final


# 3. Convert results → structured JSON format
def format_output(results, text):
    entities = []

    for r in results:
        entity_value = text[r.start:r.end]

        entities.append({
            "type": r.entity_type,
            "value": entity_value,
            "start": r.start,
            "end": r.end,
            "confidence": round(r.score, 2),
            "risk": get_risk_level(r.entity_type),
            "category": get_entity_category(r.entity_type)
        })

    return entities


# 4. Full pipeline (THIS replaces Gemini)
def process_text(analyzer, text):
    # Step 1: Detect
    results = analyzer.analyze(text=text, language="en")

    # Step 2: Remove noise
    results = filter_low_confidence(results)

    # Step 3: Resolve overlaps
    results = resolve_conflicts(results)

    # Step 4: Format output
    structured_output = format_output(results, text)

    return structured_output