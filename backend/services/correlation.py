import json
from pathlib import Path


# ============================================================
# PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent.parent

ASSET_FILE = (
    BASE_DIR
    / "data"
    / "assets.json"
)


# ============================================================
# LOAD ASSETS
# ============================================================

def load_assets():

    if not ASSET_FILE.exists():
        return []

    with open(
        ASSET_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


# ============================================================
# CORRELATE ONE THREAT
# ============================================================

def correlate_ioc(
    threat,
    assets
):

    alerts = []

    indicator_type = str(
        threat.get(
            "indicator_type",
            ""
        )
    ).upper()

    indicator_value = str(
        threat.get(
            "indicator_value",
            ""
        )
    ).lower()

    threat_id = str(
        threat.get(
            "threat_id",
            "UNKNOWN"
        )
    )

    risk = int(
        float(
            threat.get(
                "risk_score",
                0
            )
        )
    )

    severity = str(
        threat.get(
            "severity",
            "LOW"
        )
    )

    confidence = int(
        float(
            threat.get(
                "confidence_score",
                0
            )
        )
    )

    # --------------------------------------------------------
    # DOMAIN / EMAIL DOMAIN CORRELATION
    # --------------------------------------------------------

    for asset in assets:

        email_domain = str(
            asset.get(
                "email_domain",
                ""
            )
        ).lower()

        if (
            indicator_type == "DOMAIN"
            and email_domain
            and (
                indicator_value == email_domain
                or indicator_value.endswith(
                    "." + email_domain
                )
            )
        ):

            alerts.append({

                "alert_id":
                    f"ALT-{threat_id}-{asset['asset_id']}",

                "threat_id":
                    threat_id,

                "asset_id":
                    asset["asset_id"],

                "asset_name":
                    asset["asset_name"],

                "kind":
                    "IOC CORRELATION",

                "title":
                    f"IOC matched asset domain: "
                    f"{indicator_value}",

                "severity":
                    severity,

                "risk_score":
                    risk,

                "confidence_score":
                    confidence,

                "reason":
                    f"Indicator {indicator_value} "
                    f"matches the email domain "
                    f"associated with "
                    f"{asset['asset_name']}.",

                "recommended_action":
                    "Review the indicator and "
                    "verify whether the asset "
                    "has observed related activity.",

                "status":
                    "NEW"
            })

    # --------------------------------------------------------
    # HIGH RISK CORRELATION
    # --------------------------------------------------------

    if risk >= 70:

        alerts.append({

            "alert_id":
                f"ALT-{threat_id}-RISK",

            "threat_id":
                threat_id,

            "asset_id":
                None,

            "asset_name":
                "Multiple / Unknown",

            "kind":
                "HIGH RISK IOC",

            "title":
                f"High-risk indicator: "
                f"{indicator_value}",

            "severity":
                severity,

            "risk_score":
                risk,

            "confidence_score":
                confidence,

            "reason":
                f"Risk score {risk} "
                f"is above the alert threshold.",

            "recommended_action":
                "Investigate the indicator, "
                "review affected assets, "
                "and follow the organization's "
                "incident-response procedure.",

            "status":
                "NEW"
        })

    return alerts


# ============================================================
# CORRELATE ALL THREATS
# ============================================================

def correlate_all_threats(
    threats
):

    assets = load_assets()

    all_alerts = []

    for threat in threats:

        alerts = correlate_ioc(
            threat,
            assets
        )

        all_alerts.extend(
            alerts
        )

    return all_alerts