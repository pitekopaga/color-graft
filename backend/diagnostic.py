import json

# Simplified Ishihara-style test data
TEST_PLATES = [
    {"colors": [(255,0,0), (200,50,50)], "correct": "protan", "description": "Red vs dark red"},
    {"colors": [(0,255,0), (50,200,50)], "correct": "deutan", "description": "Green vs dark green"},
    {"colors": [(255,255,0), (200,200,50)], "correct": "tritan", "description": "Yellow vs olive"},
]

def diagnose_user(responses):
    """responses: list of answers from user (e.g., ['protan', 'deutan', 'normal'])"""
    counts = {"protan": 0, "deutan": 0, "tritan": 0, "normal": 0}
    for response in responses:
        if response in counts:
            counts[response] += 1
    # Return most frequent diagnosis
    diagnosed = max(counts, key=counts.get)
    # Estimate severity based on confidence (simplified)
    severity = counts[diagnosed] / len(responses) if responses else 0.5
    return diagnosed, severity
