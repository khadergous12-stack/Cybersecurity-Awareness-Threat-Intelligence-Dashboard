def calculate_threat_risk(
    severity,
    confidence,
    recency,
    observation_frequency,
    source_reliability,
    context
):

    severity_weight = 0.30
    confidence_weight = 0.25
    recency_weight = 0.15
    frequency_weight = 0.10
    reliability_weight = 0.10
    context_weight = 0.10

    score = (
        severity * severity_weight +
        confidence * confidence_weight +
        recency * recency_weight +
        observation_frequency * frequency_weight +
        source_reliability * reliability_weight +
        context * context_weight
    )

    return max(0, min(100, round(score)))


def classify_risk(score):

    if score <= 20:
        return "INFORMATIONAL"

    if score <= 40:
        return "LOW"

    if score <= 60:
        return "MEDIUM"

    if score <= 80:
        return "HIGH"

    return "CRITICAL"