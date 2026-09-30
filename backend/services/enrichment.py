MITRE_MAPPING = {
    "PHISHING": {
        "tactic": "Initial Access",
        "technique": "Phishing",
        "technique_id": "T1566"
    },

    "MALWARE": {
        "tactic": "Execution",
        "technique": "User Execution",
        "technique_id": "T1204"
    },

    "RANSOMWARE": {
        "tactic": "Impact",
        "technique": "Data Encrypted for Impact",
        "technique_id": "T1486"
    },

    "CREDENTIAL THREATS": {
        "tactic": "Credential Access",
        "technique": "OS Credential Dumping",
        "technique_id": "T1003"
    },

    "WEB THREATS": {
        "tactic": "Initial Access",
        "technique": "Exploit Public-Facing Application",
        "technique_id": "T1190"
    },

    "NETWORK THREATS": {
        "tactic": "Command and Control",
        "technique": "Application Layer Protocol",
        "technique_id": "T1071"
    },

    "VULNERABILITY EXPOSURE": {
        "tactic": "Initial Access",
        "technique": "Exploitation for Client Execution",
        "technique_id": "T1203"
    },

    "SOCIAL ENGINEERING": {
        "tactic": "Initial Access",
        "technique": "Phishing",
        "technique_id": "T1566"
    },

    "DATA EXPOSURE": {
        "tactic": "Collection",
        "technique": "Data from Local System",
        "technique_id": "T1005"
    },

    "ACCOUNT SECURITY": {
        "tactic": "Credential Access",
        "technique": "Valid Accounts",
        "technique_id": "T1078"
    }
}


SOURCE_RELIABILITY = {
    "Internal SOC": 95,
    "Security Vendor": 90,
    "Public Threat Feed": 80,
    "Research Report": 75,
    "Community Submission": 60
}


def enrich_threat(threat):

    category = str(
        threat.get("threat_category", "")
    ).upper()

    source = threat.get(
        "source_name",
        "Unknown"
    )

    mapping = MITRE_MAPPING.get(
        category,
        {
            "tactic": "Unknown",
            "technique": "Unknown",
            "technique_id": ""
        }
    )

    source_reliability = SOURCE_RELIABILITY.get(
        source,
        50
    )

    confidence = int(
        threat.get("confidence_score", 50)
    )

    risk = int(
        threat.get("risk_score", 0)
    )

    # Enrichment does NOT replace the original risk.
    # It adds contextual information.

    enriched = dict(threat)

    enriched["source_reliability"] = source_reliability

    enriched["mitre_tactic"] = mapping["tactic"]

    enriched["mitre_technique"] = mapping["technique"]

    enriched["mitre_technique_id"] = mapping[
        "technique_id"
    ]

    enriched["enrichment_status"] = "ENRICHED"

    enriched["risk_confidence_summary"] = {
        "risk_score": risk,
        "confidence_score": confidence,
        "source_reliability": source_reliability
    }

    return enriched