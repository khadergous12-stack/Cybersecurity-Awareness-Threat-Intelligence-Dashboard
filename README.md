# 🛡️ NexusShield
### Cybersecurity Awareness & Threat Intelligence Dashboard

> **A defensive SOC-style platform for synthetic threat intelligence analysis, IOC investigation, risk assessment, asset correlation, security alert generation, vulnerability exposure analysis, and cybersecurity awareness.**

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-REST%20API-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![JavaScript](https://img.shields.io/badge/JavaScript-Frontend-F7DF1E?logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![Chart.js](https://img.shields.io/badge/Chart.js-Visualization-FF6384)](https://www.chartjs.org/)
[![Pytest](https://img.shields.io/badge/Pytest-Testing-0A9EDC?logo=pytest&logoColor=white)](https://pytest.org/)
[![Status](https://img.shields.io/badge/Status-Working%20Demo-22C55E)](#)
[![Security](https://img.shields.io/badge/Security-Defensive%20Only-2563EB)](#security-scope)

---

## 🎯 Overview

**NexusShield** is a defensive cybersecurity dashboard designed to demonstrate how threat intelligence, IOC analysis, risk scoring, asset correlation, alert generation, vulnerability exposure, and security awareness can be brought together into a single analyst-oriented interface.

The platform combines a **FastAPI backend**, Python-based security services, synthetic threat intelligence data, asset information, and an interactive browser dashboard.

The objective is not simply to display security data, but to demonstrate a complete defensive workflow:

```text
Threat Intelligence
        ↓
IOC Validation
        ↓
Threat Enrichment
        ↓
Risk Assessment
        ↓
Asset Correlation
        ↓
Alert Generation
        ↓
Analyst Investigation
        ↓
Security Awareness
```

---

# ✨ Core Capabilities

| Capability | Description |
|---|---|
| 🛰️ Threat Intelligence | Search, filter, analyze and prioritize threat records |
| 🔎 IOC Investigation | Validate and investigate IPs, domains, URLs, hashes and other supported indicators |
| 📊 Risk Analysis | Analyze severity, confidence and calculated risk |
| 🔗 Asset Correlation | Relate threat indicators to organizational assets |
| 🚨 Alert Center | Generate and review defensive security alerts |
| 🛡️ Exposure Management | Identify and review vulnerability/exposure records |
| 🎓 Security Awareness | Provide cybersecurity awareness modules |
| 📝 Awareness Quiz | Interactive cybersecurity knowledge assessment |
| 📈 Executive Overview | Present high-level security posture and operational metrics |
| 📚 API Documentation | Interactive FastAPI documentation through Swagger UI |
| 🧪 Automated Testing | Pytest-based API and IOC validation tests |

---

# 🖥️ Dashboard

The dashboard is organized around the main defensive-security workflow.

### Executive Overview

Provides a high-level security posture view including:

- Total threat records
- Critical and high-risk activity
- Average risk
- Average confidence
- Severity distribution
- Threat categories
- Indicator distribution
- Operational review indicators

### Threat Intelligence

Analysts can:

- Search threat records
- Filter by severity
- Filter by category
- Filter by risk
- Review confidence
- Inspect indicator information
- Open individual threat details
- Prioritize higher-risk records

Supported severity levels include:

```text
CRITICAL
HIGH
MEDIUM
LOW
INFORMATIONAL
```

### IOC Investigation

The IOC investigation workflow provides defensive validation of supported indicators.

Examples of supported categories include:

```text
IPv4 / IPv6
Domain
URL
Email
MD5
SHA-1
SHA-256
CVE
```

The investigation workflow performs local validation and dataset matching.

> **Important:** The demonstration does not automatically contact suspicious external infrastructure.

### Alert Center

The alert workflow provides:

- Severity filtering
- Risk prioritization
- Alert status
- Related indicators
- Asset relationships
- Analyst review information
- Generated correlation alerts

### Exposure Management

Provides a dedicated view for vulnerability/exposure-related records and remediation-oriented review.

### Security Awareness

Includes awareness content covering areas such as:

- Phishing
- Password security
- MFA
- Safe browsing
- Ransomware
- Incident reporting
- Defensive security practices

---

# 🏗️ Architecture

```text
                           ┌─────────────────────┐
                           │    Analyst / User   │
                           └──────────┬──────────┘
                                      │
                                      ▼
                    ┌──────────────────────────────┐
                    │       NexusShield UI         │
                    │      HTML / CSS / JS         │
                    └──────────────┬───────────────┘
                                   │ REST
                                   ▼
                    ┌──────────────────────────────┐
                    │        FastAPI API           │
                    │        backend/app.py        │
                    └──────────────┬───────────────┘
                                   │
             ┌─────────────────────┼─────────────────────┐
             │                     │                     │
             ▼                     ▼                     ▼
      ┌─────────────┐       ┌─────────────┐       ┌─────────────┐
      │ IOC         │       │ Risk        │       │ Threat      │
      │ Validator   │       │ Engine      │       │ Enrichment  │
      └──────┬──────┘       └──────┬──────┘       └──────┬──────┘
             │                     │                     │
             └─────────────────────┼─────────────────────┘
                                   ▼
                         ┌────────────────────┐
                         │ Asset Correlation  │
                         └─────────┬──────────┘
                                   ▼
                         ┌────────────────────┐
                         │ Alert Generation  │
                         └─────────┬──────────┘
                                   ▼
                         ┌────────────────────┐
                         │ Analyst Dashboard  │
                         └────────────────────┘
```

---

# 🔄 Defensive Workflow

```text
             ┌───────────────────────┐
             │ Synthetic Threat Data │
             └───────────┬───────────┘
                         ▼
             ┌───────────────────────┐
             │ IOC Validation        │
             └───────────┬───────────┘
                         ▼
             ┌───────────────────────┐
             │ Threat Enrichment     │
             └───────────┬───────────┘
                         ▼
             ┌───────────────────────┐
             │ Risk Assessment       │
             └───────────┬───────────┘
                         ▼
             ┌───────────────────────┐
             │ Asset Correlation     │
             └───────────┬───────────┘
                         ▼
             ┌───────────────────────┐
             │ Alert Generation      │
             └───────────┬───────────┘
                         ▼
             ┌───────────────────────┐
             │ Analyst Review        │
             └───────────────────────┘
```

---

# 🧠 Security Services

The backend is separated into focused services rather than placing all security logic inside the API layer.

```text
backend/
│
├── app.py
│
└── services/
    ├── correlation.py
    ├── enrichment.py
    ├── ioc_validator.py
    ├── risk_engine.py
    └── vulnerability.py
```

### IOC Validator

Responsible for:

- Indicator format detection
- Indicator validation
- Supported IOC classification
- Validation feedback

### Risk Engine

Provides risk-oriented analysis using threat attributes such as:

- Severity
- Confidence
- Threat characteristics
- Indicator information

### Enrichment

Adds contextual information to threat records for analyst investigation.

### Correlation Engine

Correlates threat indicators with organizational assets using information such as:

- Asset identity
- Department/owner
- Email domain
- Installed software

### Vulnerability Service

Provides vulnerability/exposure-oriented threat records for defensive review.

---

# 📊 Demonstration Dataset

The project uses **synthetic cybersecurity data** for demonstration and testing.

The dataset contains threat intelligence attributes such as:

```text
Threat ID
Threat Name
Threat Category
Indicator Type
Indicator Value
Severity
Risk Score
Confidence Score
Status
Source
```

Organizational asset information is represented using synthetic records such as:

```text
Asset ID
Asset Name
Owner / Department
Email Domain
Installed Software
```

### Why synthetic data?

Synthetic data allows the project to demonstrate:

- IOC validation
- Risk scoring
- Threat correlation
- Alert generation
- Dashboard visualization

without exposing real organizational information or contacting real suspicious infrastructure.

---

# 🚨 Alert Generation

The correlation engine evaluates threat records against the synthetic asset inventory.

A correlation can be generated when relevant relationships exist between threat intelligence and asset information.

Example workflow:

```text
Threat Indicator
       ↓
Indicator Type Match
       ↓
Asset Attribute Match
       ↓
Correlation Rule
       ↓
Risk Evaluation
       ↓
Security Alert
```

Example demonstration metrics may include:

```text
Generated Alerts
Critical Alerts
High Alerts
Medium Alerts
Low Alerts
Average Alert Risk
```

> Demonstration metrics are generated from the local synthetic dataset and may change when the dataset or correlation rules are regenerated.

---

# 🧰 Technology Stack

| Layer | Technology |
|---|---|
| Language | Python |
| Backend | FastAPI |
| Server | Uvicorn |
| Data Processing | Pandas |
| Frontend | HTML5 / CSS3 / JavaScript |
| Visualization | Chart.js |
| Data Format | CSV / JSON |
| Testing | Pytest |
| API Testing | FastAPI TestClient |
| Documentation | Markdown |

---

# 📁 Repository Structure

```text
Cybersecurity-Awareness-Threat-Intelligence-Dashboard/
│
├── awareness/
│   ├── awareness_modules.json
│   └── quiz.json
│
├── backend/
│   ├── __init__.py
│   ├── app.py
│   └── services/
│       ├── __init__.py
│       ├── correlation.py
│       ├── enrichment.py
│       ├── ioc_validator.py
│       ├── risk_engine.py
│       └── vulnerability.py
│
├── data/
│   ├── assets.json
│   ├── generate_threat_data.py
│   └── threat_intelligence_dataset.csv
│
├── docs/
│   ├── api_documentation.md
│   ├── architecture.md
│   └── project_overview.md
│
├── frontend/
│   └── index.html
│
├── reports/
│   └── test_report.md
│
├── screenshots/
│   ├── alerts.png
│   ├── apis.png
│   ├── awareness.png
│   ├── exposure.png
│   ├── home.png
│   ├── investigation.png
│   └── threat_intelligence.png
│
├── tests/
│   ├── test_api.py
│   └── test_ioc_validator.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

# 🚀 Quick Start

## 1. Clone the repository

```powershell
git clone https://github.com/khadergous12-stack/Cybersecurity-Awareness-Threat-Intelligence-Dashboard.git
cd Cybersecurity-Awareness-Threat-Intelligence-Dashboard
```

## 2. Create a virtual environment

```powershell
python -m venv venv
```

## 3. Activate the environment

### Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

## 4. Install dependencies

```powershell
pip install -r requirements.txt
```

## 5. Start the backend

```powershell
uvicorn backend.app:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

---

# 🌐 Access the Application

### API

```text
http://127.0.0.1:8000
```

### Swagger API Documentation

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

### Dashboard

Open:

```text
frontend/index.html
```

The dashboard communicates with the locally running FastAPI service.

---

# 🔌 API Surface

| Endpoint | Purpose |
|---|---|
| `GET /` | API health |
| `GET /api/dashboard/stats` | Dashboard statistics |
| `GET /api/threats` | Threat records |
| `GET /api/threats/{threat_id}` | Threat details |
| `GET /api/threats/{threat_id}/enriched` | Enriched threat |
| `GET /api/indicators/search` | IOC validation/search |
| `GET /api/alerts` | High-risk alerts |
| `GET /api/alerts/generated` | Correlation-generated alerts |
| `GET /api/correlation/{threat_id}` | Threat correlation |
| `GET /api/vulnerabilities` | Vulnerability exposure |
| `GET /api/awareness/modules` | Awareness modules |
| `GET /api/quiz` | Security awareness quiz |

---

# 🧪 Testing

Run the complete test suite:

```powershell
pytest -q
```

The tests cover core functionality including:

- API availability
- Dashboard statistics
- Threat retrieval
- IOC validation
- Awareness modules
- Quiz endpoints

For API-level manual validation, use:

```text
http://127.0.0.1:8000/docs
```

This provides an interactive Swagger interface for testing the available endpoints.

---

# 🔐 Security & Privacy Scope

NexusShield is intentionally designed as a **defensive demonstration platform**.

### The project uses:

- Synthetic threat intelligence
- Synthetic asset information
- Local validation
- Local correlation
- Local risk analysis

### The project does not:

- Attack external systems
- Exploit vulnerabilities
- Perform unauthorized scanning
- Automatically contact suspicious infrastructure
- Collect real employee information
- Require real credentials or secrets

The platform is intended for **academic, educational, demonstration, and defensive security analysis purposes**.

---

# ⚠️ Project Limitations

This is a demonstration-oriented cybersecurity platform.

Current limitations include:

- Threat intelligence data is synthetic.
- Asset information is synthetic.
- Correlation is rule-based.
- No production SIEM integration is included.
- No external threat intelligence feed is required.
- Authentication/RBAC is not implemented in the current demonstration.
- Real-time streaming is outside the current scope.
- Risk scoring is demonstration-oriented rather than a production SOC scoring standard.

These limitations are intentional so the system can operate safely as a self-contained project.

---

# 🔮 Roadmap

Potential future development:

```text
Phase 1
Synthetic Threat Intelligence
        ↓
Phase 2
IOC Validation & Risk Analysis
        ↓
Phase 3
Asset Correlation
        ↓
Phase 4
Alert Management
        ↓
Phase 5
Vulnerability & Exposure Management
        ↓
Phase 6
Security Awareness
        ↓
Future
External Threat Intelligence Feeds
        ↓
Future
Database / SIEM Integration
        ↓
Future
Authentication & RBAC
        ↓
Future
Real-Time Monitoring
```

Potential future integrations include:

- STIX/TAXII-compatible intelligence
- SIEM platforms
- Database-backed persistence
- Role-based access control
- Real-time alerting
- Historical analytics
- ML-assisted risk analysis
- Automated security reporting

---

# 📸 Screenshots

The repository contains screenshots demonstrating the major application areas:

| View | Screenshot |
|---|---|
| Executive Dashboard | `screenshots/home.png` |
| Threat Intelligence | `screenshots/threat_intelligence.png` |
| IOC Investigation | `screenshots/investigation.png` |
| Alert Center | `screenshots/alerts.png` |
| Exposure Management | `screenshots/exposure.png` |
| Security Awareness | `screenshots/awareness.png` |
| API Documentation | `screenshots/apis.png` |

---

# 🎓 Academic Project Context

This project demonstrates the integration of multiple cybersecurity concepts into a single defensive application:

```text
Threat Intelligence
       +
IOC Analysis
       +
Risk Assessment
       +
Asset Correlation
       +
Security Alerts
       +
Vulnerability Awareness
       +
Cybersecurity Education
```

It provides practical exposure to:

- Python security programming
- REST API development
- Data processing
- Threat intelligence concepts
- IOC analysis
- Risk assessment
- Security automation
- Frontend visualization
- API testing
- Defensive cybersecurity workflows

---

# 👨‍💻 Author

## KhaderGouse Savanur

**Cybersecurity Awareness & Threat Intelligence Dashboard**

Built as a defensive cybersecurity project focused on threat intelligence analysis, security monitoring concepts, IOC investigation, risk assessment, and cybersecurity awareness.

---

# ⭐ Project Status

```text
Backend              ✅ Working
Threat Intelligence  ✅ Working
IOC Investigation    ✅ Working
Risk Analysis        ✅ Working
Asset Correlation    ✅ Working
Alert Generation     ✅ Working
Exposure Management  ✅ Working
Security Awareness   ✅ Working
Quiz                 ✅ Working
API Documentation    ✅ Available
Automated Tests      ✅ Included
```

---

## 📜 License

This project is intended for **academic, educational, and defensive cybersecurity purposes**.

---

> **NexusShield — Turning threat intelligence into actionable defensive insight.**

**Made by KhaderGouse**
