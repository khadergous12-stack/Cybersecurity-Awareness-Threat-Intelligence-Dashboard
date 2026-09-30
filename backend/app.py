from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

import pandas as pd
from pathlib import Path

from backend.services.ioc_validator import validate_indicator
from backend.services.enrichment import enrich_threat
from backend.services.correlation import (
    load_assets,
    correlate_ioc,
    correlate_all_threats
)

from backend.services.vulnerability import (
    enrich_vulnerability
)


# ============================================================
# PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_FILE = (
    BASE_DIR
    / "data"
    / "threat_intelligence_dataset.csv"
)


# ============================================================
# FASTAPI APPLICATION
# ============================================================

app = FastAPI(
    title="Cybersecurity Awareness & Threat Intelligence Dashboard",
    version="1.0"
)


# ============================================================
# CORS
# ============================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# ============================================================
# DATA LOADER
# ============================================================

def load_data():
    return pd.read_csv(DATA_FILE)


# ============================================================
# HOME
# ============================================================

@app.get("/")
def home():

    return {
        "message": "Cybersecurity Threat Intelligence API",
        "status": "running"
    }


# ============================================================
# DASHBOARD STATISTICS
# ============================================================

@app.get("/api/dashboard/stats")
def dashboard_stats():

    df = load_data()

    severity_counts = (
        df["severity"]
        .value_counts()
        .to_dict()
    )

    category_counts = (
        df["threat_category"]
        .value_counts()
        .to_dict()
    )

    indicator_counts = (
        df["indicator_type"]
        .value_counts()
        .to_dict()
    )

    return {

        "total_threats": len(df),

        "critical_threats": int(
            severity_counts.get(
                "CRITICAL",
                0
            )
        ),

        "high_threats": int(
            severity_counts.get(
                "HIGH",
                0
            )
        ),

        "active_indicators": len(
            df[
                df["status"].isin(
                    [
                        "NEW",
                        "UNDER_REVIEW",
                        "MONITORING"
                    ]
                )
            ]
        ),

        "average_confidence": round(
            df["confidence_score"].mean(),
            2
        ),

        "average_risk": round(
            df["risk_score"].mean(),
            2
        ),

        "severity_distribution":
            severity_counts,

        "category_distribution":
            category_counts,

        "indicator_distribution":
            indicator_counts
    }


# ============================================================
# GET THREATS
# ============================================================

@app.get("/api/threats")
def get_threats(
    limit: int = Query(
        50,
        ge=1,
        le=500
    )
):

    df = load_data()

    records = (
        df.sort_values(
            "risk_score",
            ascending=False
        )
        .head(limit)
        .fillna("")
        .to_dict(
            orient="records"
        )
    )

    return records


# ============================================================
# GET SINGLE THREAT
# ============================================================

@app.get("/api/threats/{threat_id}")
def get_threat(
    threat_id: str
):

    df = load_data()

    result = df[
        df["threat_id"] == threat_id
    ]

    if result.empty:

        return {
            "error": "Threat not found"
        }

    return (
        result
        .iloc[0]
        .fillna("")
        .to_dict()
    )


# ============================================================
# THREAT ENRICHMENT
# ============================================================

@app.get(
    "/api/threats/{threat_id}/enriched"
)
def get_enriched_threat(
    threat_id: str
):

    df = load_data()

    result = df[
        df["threat_id"] == threat_id
    ]

    if result.empty:

        return {
            "error": "Threat not found"
        }

    threat = (
        result
        .iloc[0]
        .fillna("")
        .to_dict()
    )

    enriched = enrich_threat(
        threat
    )

    return enriched


# ============================================================
# IOC SEARCH + VALIDATION
# ============================================================

@app.get("/api/indicators/search")
def search_indicator(
    q: str
):

    validation = validate_indicator(
        q
    )

    df = load_data()

    exact = df[
        df["indicator_value"]
        .astype(str)
        .str.lower()
        == q.lower()
    ]

    return {

        "validation":
            validation,

        "known_in_demo_dataset":
            not exact.empty,

        "results":
            exact
            .fillna("")
            .to_dict(
                orient="records"
            )
    }


# ============================================================
# EXISTING ALERTS
# ============================================================

@app.get("/api/alerts")
def get_alerts():

    df = load_data()

    alerts = (
        df[
            df["risk_score"] >= 70
        ]
        .sort_values(
            "risk_score",
            ascending=False
        )
        .head(50)
    )

    return (
        alerts
        .fillna("")
        .to_dict(
            orient="records"
        )
    )


# ============================================================
# GENERATED CORRELATION ALERTS
# ============================================================

@app.get("/api/alerts/generated")
def generated_alerts():

    df = load_data()

    threats = (
        df
        .fillna("")
        .to_dict(
            orient="records"
        )
    )

    alerts = correlate_all_threats(
        threats
    )

    return {

        "total_alerts":
            len(alerts),

        "alerts":
            alerts[:100]
    }

# ============================================================
# ALERT STATISTICS
# ============================================================

@app.get("/api/alerts/stats")
def alert_stats():

    df = load_data()

    threats = (
        df
        .fillna("")
        .to_dict(orient="records")
    )

    alerts = correlate_all_threats(
        threats
    )

    if not alerts:
        return {
            "total": 0,
            "critical": 0,
            "high": 0,
            "medium": 0,
            "low": 0,
            "new": 0,
            "average_risk": 0
        }

    alert_df = pd.DataFrame(alerts)

    severity_counts = (
        alert_df["severity"]
        .fillna("UNKNOWN")
        .astype(str)
        .str.upper()
        .value_counts()
        .to_dict()
    )

    return {
        "total": len(alerts),

        "critical": int(
            severity_counts.get(
                "CRITICAL",
                0
            )
        ),

        "high": int(
            severity_counts.get(
                "HIGH",
                0
            )
        ),

        "medium": int(
            severity_counts.get(
                "MEDIUM",
                0
            )
        ),

        "low": int(
            severity_counts.get(
                "LOW",
                0
            )
        ),

        "new": int(
            (
                alert_df["status"]
                .astype(str)
                .str.upper()
                == "NEW"
            ).sum()
        ),

        "average_risk": round(
            pd.to_numeric(
                alert_df["risk_score"],
                errors="coerce"
            ).mean(),
            2
        )
    }


# ============================================================
# ALERT FILTER
# ============================================================

@app.get("/api/alerts/filter")
def filter_alerts(
    severity: str = "",
    status: str = "",
    limit: int = Query(
        100,
        ge=1,
        le=500
    )
):

    df = load_data()

    threats = (
        df
        .fillna("")
        .to_dict(orient="records")
    )

    alerts = correlate_all_threats(
        threats
    )

    if severity:

        alerts = [
            alert
            for alert in alerts
            if str(
                alert.get(
                    "severity",
                    ""
                )
            ).upper()
            == severity.upper()
        ]

    if status:

        alerts = [
            alert
            for alert in alerts
            if str(
                alert.get(
                    "status",
                    ""
                )
            ).upper()
            == status.upper()
        ]

    alerts = sorted(
        alerts,
        key=lambda x: float(
            x.get(
                "risk_score",
                0
            )
        ),
        reverse=True
    )

    return {
        "total": len(alerts),
        "alerts": alerts[:limit]
    }
# ============================================================
# CORRELATE ONE THREAT
# ============================================================

@app.get(
    "/api/correlation/{threat_id}"
)
def correlate_threat(
    threat_id: str
):

    df = load_data()

    result = df[
        df["threat_id"] == threat_id
    ]

    if result.empty:

        return {
            "error": "Threat not found"
        }

    threat = (
        result
        .iloc[0]
        .fillna("")
        .to_dict()
    )

    assets = load_assets()

    alerts = correlate_ioc(
        threat,
        assets
    )

    return {

        "threat_id":
            threat_id,

        "alerts_generated":
            len(alerts),

        "alerts":
            alerts
    }


# ============================================================
# VULNERABILITIES
# ============================================================

@app.get("/api/vulnerabilities")
def vulnerabilities():

    df = load_data()

    vulnerabilities = df[
        df["threat_category"]
        == "VULNERABILITY EXPOSURE"
    ]

    records = (
        vulnerabilities
        .fillna("")
        .to_dict(
            orient="records"
        )
    )

    enriched_records = [
        enrich_vulnerability(
            record
        )
        for record in records
    ]

    return {
        "total_vulnerabilities":
            len(enriched_records),

        "vulnerabilities":
            enriched_records
    }

@app.get("/api/vulnerabilities/stats")
def vulnerability_stats():

    df = load_data()

    vulnerabilities = df[
        df["threat_category"]
        == "VULNERABILITY EXPOSURE"
    ]

    if vulnerabilities.empty:
        return {
            "total": 0,
            "critical": 0,
            "high": 0,
            "medium": 0,
            "low": 0,
            "other": 0,
            "average_risk": 0
        }

    severity_counts = (
        vulnerabilities["severity"]
        .fillna("UNKNOWN")
        .astype(str)
        .str.upper()
        .value_counts()
        .to_dict()
    )

    known_count = (
        severity_counts.get("CRITICAL", 0)
        + severity_counts.get("HIGH", 0)
        + severity_counts.get("MEDIUM", 0)
        + severity_counts.get("LOW", 0)
    )

    other_count = (
        len(vulnerabilities) - known_count
    )

    return {
        "total": len(vulnerabilities),

        "critical": int(
            severity_counts.get("CRITICAL", 0)
        ),

        "high": int(
            severity_counts.get("HIGH", 0)
        ),

        "medium": int(
            severity_counts.get("MEDIUM", 0)
        ),

        "low": int(
            severity_counts.get("LOW", 0)
        ),

        "other": int(other_count),

        "average_risk": round(
            vulnerabilities["risk_score"]
            .astype(float)
            .mean(),
            2
        )
    }
# ============================================================
# SECURITY AWARENESS MODULES
# ============================================================

@app.get("/api/awareness/modules")
def awareness_modules():

    return [

        {
            "title":
                "Phishing Awareness",

            "category":
                "Phishing",

            "tip":
                "Check unexpected senders, urgency, links and credential requests.",

            "action":
                "Verify through a trusted channel."
        },

        {
            "title":
                "Password Security",

            "category":
                "Passwords",

            "tip":
                "Use unique long passwords or passphrases.",

            "action":
                "Use a password manager."
        },

        {
            "title":
                "MFA Awareness",

            "category":
                "MFA",

            "tip":
                "Multi-factor authentication adds another protection layer.",

            "action":
                "Enable MFA where available."
        },

        {
            "title":
                "Safe Browsing",

            "category":
                "Web Security",

            "tip":
                "Avoid unexpected links and verify websites before entering information.",

            "action":
                "Use trusted sources."
        },

        {
            "title":
                "Ransomware Awareness",

            "category":
                "Ransomware",

            "tip":
                "Backups, patching and least privilege reduce risk.",

            "action":
                "Keep important data backed up."
        }
    ]


# ============================================================
# SECURITY AWARENESS QUIZ
# ============================================================

@app.get("/api/quiz")
def quiz():

    return [

        {
            "id": 1,

            "question":
                "What does IOC stand for?",

            "options": [
                "Indicator of Compromise",
                "Internet Operations Center",
                "Internal Online Control",
                "Information Operations Channel"
            ],

            "answer": 0
        },

        {
            "id": 2,

            "question":
                "What should you do with an unexpected password request?",

            "options": [
                "Reply immediately",
                "Send your password",
                "Verify through a trusted channel",
                "Forward your password"
            ],

            "answer": 2
        },

        {
            "id": 3,

            "question":
                "What does MFA provide?",

            "options": [
                "Additional authentication protection",
                "Faster internet",
                "File compression",
                "Antivirus scanning only"
            ],

            "answer": 0
        },

        {
            "id": 4,

            "question":
                "What is CVE related to?",

            "options": [
                "Software vulnerabilities",
                "Email formatting",
                "Network speed",
                "Password length"
            ],

            "answer": 0
        },

        {
            "id": 5,

            "question":
                "What is phishing?",

            "options": [
                "A social engineering technique",
                "A backup method",
                "A database",
                "A firewall"
            ],

            "answer": 0
        }
    ]