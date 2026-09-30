# API Documentation

Base URL:

http://127.0.0.1:8000

## Health Check

GET /

Returns the API status.

## Dashboard Statistics

GET /api/dashboard/stats

Returns:

- Total threats
- Critical threats
- High threats
- Active indicators
- Average confidence
- Average risk
- Severity distribution
- Category distribution
- Indicator distribution

## Threats

GET /api/threats?limit=20

Returns threat intelligence records ordered by risk score.

## Threat Details

GET /api/threats/{threat_id}

Returns details for a specific threat.

## Threat Enrichment

GET /api/threats/{threat_id}/enriched

Returns enriched information for a threat.

## IOC Search

GET /api/indicators/search?q={indicator}

Validates an indicator and checks whether it exists in the demonstration dataset.

## Alerts

GET /api/alerts

Returns high-risk alerts.

## Generated Alerts

GET /api/alerts/generated

Returns correlated security alerts generated from the threat dataset.

## Correlation

GET /api/correlation/{threat_id}

Correlates a threat indicator with available organizational assets.

## Vulnerabilities

GET /api/vulnerabilities

Returns vulnerability exposure records.

## Security Awareness

GET /api/awareness/modules

Returns cybersecurity awareness modules.

## Quiz

GET /api/quiz

Returns cybersecurity awareness quiz questions.