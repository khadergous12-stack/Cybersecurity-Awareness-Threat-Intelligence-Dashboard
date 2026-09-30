import csv
import random
import hashlib
from datetime import datetime, timedelta

OUTPUT_FILE = "data/threat_intelligence_dataset.csv"

categories = [
    "PHISHING",
    "MALWARE",
    "RANSOMWARE",
    "CREDENTIAL THREATS",
    "WEB THREATS",
    "NETWORK THREATS",
    "VULNERABILITY EXPOSURE",
    "SOCIAL ENGINEERING",
    "DATA EXPOSURE",
    "ACCOUNT SECURITY"
]

indicator_types = [
    "IP ADDRESS",
    "DOMAIN",
    "URL",
    "FILE HASH",
    "EMAIL/SENDER DOMAIN"
]

severities = [
    "INFORMATIONAL",
    "LOW",
    "MEDIUM",
    "HIGH",
    "CRITICAL"
]

sources = [
    "Internal SOC",
    "Security Vendor",
    "Public Threat Feed",
    "Research Report",
    "Community Submission"
]

statuses = [
    "NEW",
    "UNDER_REVIEW",
    "MONITORING",
    "CLOSED",
    "FALSE_POSITIVE"
]

threat_names = [
    "Synthetic Phishing Campaign",
    "Synthetic Malware Observation",
    "Synthetic Credential Threat",
    "Synthetic Ransomware Indicator",
    "Synthetic Web Threat",
    "Synthetic Network Threat",
    "Synthetic Data Exposure",
    "Synthetic Account Security Event"
]

domains = [
    "example.com",
    "example.org",
    "example.net",
    "demo.invalid"
]

ip_ranges = [
    "192.0.2.",
    "198.51.100.",
    "203.0.113."
]


def synthetic_hash():
    value = f"synthetic-{random.random()}".encode()
    return hashlib.sha256(value).hexdigest()


def generate_indicator(indicator_type):
    if indicator_type == "IP ADDRESS":
        return random.choice(ip_ranges) + str(random.randint(1, 254))

    if indicator_type == "DOMAIN":
        return random.choice(domains)

    if indicator_type == "URL":
        return f"https://example.com/demo/{random.randint(1000,9999)}"

    if indicator_type == "FILE HASH":
        return synthetic_hash()

    return f"security@example.{random.choice(['com', 'org', 'net'])}"


def severity_score(severity):
    scores = {
        "INFORMATIONAL": 15,
        "LOW": 30,
        "MEDIUM": 50,
        "HIGH": 75,
        "CRITICAL": 95
    }
    return scores[severity]


records = []

start_date = datetime(2026, 1, 1)

for i in range(2000):

    category = random.choice(categories)
    indicator_type = random.choice(indicator_types)
    severity = random.choice(severities)

    confidence = random.randint(50, 98)
    base_risk = severity_score(severity)

    risk = min(
        100,
        int((base_risk * 0.6) + (confidence * 0.4))
    )

    first_seen = start_date + timedelta(
        days=random.randint(0, 270)
    )

    last_seen = first_seen + timedelta(
        days=random.randint(0, 10)
    )

    records.append({
        "threat_id": f"THR-2026-{i+1:04d}",
        "timestamp": first_seen.isoformat(),
        "threat_name": random.choice(threat_names),
        "threat_category": category,
        "indicator_type": indicator_type,
        "indicator_value": generate_indicator(indicator_type),
        "source_name": random.choice(sources),
        "confidence_score": confidence,
        "severity": severity,
        "risk_score": risk,
        "status": random.choice(statuses),
        "first_seen": first_seen.date().isoformat(),
        "last_seen": last_seen.date().isoformat(),
        "country_or_region_optional": random.choice(
            ["India", "US", "EU", "APAC", "Demo"]
        ),
        "description": "Synthetic defensive cybersecurity observation. DEMO ONLY.",
        "mitre_tactic_optional": random.choice([
            "Initial Access",
            "Credential Access",
            "Discovery",
            "Command and Control",
            "Defense Evasion"
        ]),
        "mitre_technique_optional": "",
        "cve_id_optional": ""
    })


with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:

    writer = csv.DictWriter(
        file,
        fieldnames=records[0].keys()
    )

    writer.writeheader()
    writer.writerows(records)


print(f"Generated {len(records)} synthetic threat records.")
print(f"Saved to: {OUTPUT_FILE}")