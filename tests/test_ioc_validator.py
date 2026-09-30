from backend.services.ioc_validator import validate_indicator


def test_valid_ipv4():
    result = validate_indicator("192.0.2.178")

    assert result["valid"] is True


def test_invalid_indicator():
    result = validate_indicator("not-a-valid-indicator")

    assert result["valid"] is False