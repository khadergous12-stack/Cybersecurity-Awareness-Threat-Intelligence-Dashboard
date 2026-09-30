import ipaddress
import re
from urllib.parse import urlparse


def validate_indicator(value: str):

    value = value.strip()

    # IPv4 / IPv6
    try:
        ipaddress.ip_address(value)

        return {
            "valid": True,
            "indicator_type": "IP ADDRESS",
            "normalized_value": value,
            "validation_notes": "Valid IP address format."
        }

    except ValueError:
        pass

    # CVE
    if re.fullmatch(r"CVE-\d{4}-\d{4,}", value, re.IGNORECASE):

        return {
            "valid": True,
            "indicator_type": "CVE ID",
            "normalized_value": value.upper(),
            "validation_notes": "Valid CVE identifier format."
        }

    # Hash
    if re.fullmatch(r"[a-fA-F0-9]{32}", value):

        return {
            "valid": True,
            "indicator_type": "FILE HASH",
            "normalized_value": value.lower(),
            "validation_notes": "Valid MD5-format hash."
        }

    if re.fullmatch(r"[a-fA-F0-9]{40}", value):

        return {
            "valid": True,
            "indicator_type": "FILE HASH",
            "normalized_value": value.lower(),
            "validation_notes": "Valid SHA-1-format hash."
        }

    if re.fullmatch(r"[a-fA-F0-9]{64}", value):

        return {
            "valid": True,
            "indicator_type": "FILE HASH",
            "normalized_value": value.lower(),
            "validation_notes": "Valid SHA-256-format hash."
        }

    # URL
    try:

        parsed = urlparse(value)

        if parsed.scheme in ["http", "https"] and parsed.netloc:

            return {
                "valid": True,
                "indicator_type": "URL",
                "normalized_value": value,
                "validation_notes": "Valid URL syntax."
            }

    except Exception:
        pass

    # Domain
    domain_pattern = r"^(?!-)[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    if re.fullmatch(domain_pattern, value):

        return {
            "valid": True,
            "indicator_type": "DOMAIN",
            "normalized_value": value.lower(),
            "validation_notes": "Valid domain syntax."
        }

    return {
        "valid": False,
        "indicator_type": "UNKNOWN",
        "normalized_value": value,
        "validation_notes": "Indicator format could not be validated."
    }