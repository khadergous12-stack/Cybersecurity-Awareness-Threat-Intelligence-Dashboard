# System Architecture

## Architecture Flow

User
  |
  v
Frontend Dashboard
  |
  v
FastAPI Backend
  |
  +--> Threat Intelligence Dataset
  |
  +--> IOC Validator
  |
  +--> Risk Engine
  |
  +--> Threat Enrichment
  |
  +--> Asset Correlation
  |
  +--> Alert Generation
  |
  +--> Vulnerability Management
  |
  +--> Security Awareness
  |
  v
JSON API Responses
  |
  v
Dashboard Visualization

## Data Flow

1. Synthetic threat intelligence records are loaded from the CSV dataset.
2. The FastAPI backend processes the records.
3. IOC values are validated using the IOC validator.
4. Threat risk and confidence values are analyzed.
5. Threats can be enriched with additional information.
6. Indicators are correlated against organizational assets.
7. Correlated threats generate security alerts.
8. Vulnerability records are identified and displayed.
9. Results are exposed through REST API endpoints.
10. The frontend consumes the APIs and displays the results.

## Major Components

### Frontend

Provides the dashboard interface, charts, tables, IOC search, alert management, vulnerability information and awareness content.

### FastAPI Backend

Provides REST APIs for threat intelligence and cybersecurity operations.

### IOC Validator

Validates different indicator types such as IP addresses, domains, URLs, email addresses and hashes.

### Risk Engine

Uses threat attributes to provide risk information used for prioritization.

### Correlation Engine

Matches threat indicators against available organizational asset information.

### Alert Management

Generates alerts from correlated threat information and organizes them by severity and risk.

### Vulnerability Management

Identifies vulnerability exposure and provides risk and patch-priority information.