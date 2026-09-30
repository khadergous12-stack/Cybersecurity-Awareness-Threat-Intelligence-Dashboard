# 🛡️ Cybersecurity Awareness & Threat Intelligence Dashboard

> A defensive cybersecurity platform for analyzing synthetic threat intelligence, validating Indicators of Compromise (IOCs), assessing risk, correlating threats with organizational assets, generating security alerts, and promoting cybersecurity awareness.

---

## 📌 Project Overview

The **Cybersecurity Awareness & Threat Intelligence Dashboard** is a web-based defensive security platform developed to provide a centralized view of threat intelligence and cybersecurity awareness information.

The system processes a synthetic dataset containing **2,000 threat intelligence records** and provides functionality for IOC validation, threat analysis, risk assessment, asset correlation, alert generation, vulnerability identification, and security awareness.

The project combines a **FastAPI backend** with a browser-based dashboard to present cybersecurity information in an easy-to-understand format.

---

## 🎯 Objectives

- Analyze and visualize threat intelligence records.
- Validate and search Indicators of Compromise (IOCs).
- Analyze threat severity, confidence, and risk.
- Correlate threat indicators with organizational assets.
- Generate security alerts from correlated threats.
- Identify vulnerability exposure.
- Provide cybersecurity awareness content.
- Provide an interactive cybersecurity awareness quiz.

---

## 🏗️ System Architecture

```text
                    ┌─────────────────────┐
                    │   User / Analyst    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  Web Dashboard      │
                    │ HTML/CSS/JavaScript │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   FastAPI Backend   │
                    └──────────┬──────────┘
                               │
          ┌────────────────────┼────────────────────┐
          │                    │                    │
          ▼                    ▼                    ▼
   ┌─────────────┐     ┌─────────────┐     ┌──────────────┐
   │ IOC         │     │ Risk        │     │ Threat       │
   │ Validator   │     │ Analysis    │     │ Enrichment   │
   └─────────────┘     └─────────────┘     └──────────────┘
          │                    │                    │
          └────────────────────┼────────────────────┘
                               ▼
                    ┌─────────────────────┐
                    │ Asset Correlation   │
                    └──────────┬──────────┘
                               ▼
                    ┌─────────────────────┐
                    │ Alert Generation    │
                    └──────────┬──────────┘
                               ▼
                    ┌─────────────────────┐
                    │ Dashboard Results   │
                    └─────────────────────┘
```

---

## ⚙️ Main Features

### 🔍 Threat Intelligence

Displays and analyzes synthetic threat intelligence records based on:

- Threat category
- Indicator type
- Indicator value
- Severity
- Risk score
- Confidence score
- Status

### 🔎 IOC Search & Validation

The system supports validation and searching of Indicators of Compromise.

Supported indicator categories include:

- IP addresses
- Domains
- URLs
- Email addresses
- Hashes

The search also determines whether an indicator is present in the demonstration dataset.

### 📊 Risk Analysis

Threat records contain risk and confidence information that can be used to prioritize potentially significant threats.

### 🔗 Asset Correlation

Threat indicators are correlated against organizational asset information such as:

- Asset ID
- Asset name
- Department/owner
- Email domain
- Installed software

### 🚨 Alert Generation

The correlation engine generates alerts from relevant threat and asset relationships.

Current demonstration result:

```text
Total Generated Alerts: 1,089
Critical:                 529
High:                     364
Medium:                    76
Low:                       60
Average Risk:            76.3
```

### 🛡️ Vulnerability Management

The system identifies records associated with vulnerability exposure and provides them through the API.

### 🎓 Security Awareness

The platform includes cybersecurity awareness modules covering:

- Phishing
- Password security
- Multi-factor authentication
- Safe browsing
- Ransomware awareness

### 📝 Security Quiz

An interactive quiz provides cybersecurity awareness questions covering topics such as:

- IOC
- MFA
- Phishing
- CVE
- Password security

---

## 🧰 Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming |
| FastAPI | Backend REST API |
| Uvicorn | Application server |
| Pandas | Data processing |
| HTML | Dashboard structure |
| CSS | Dashboard styling |
| JavaScript | Frontend functionality |
| Chart.js | Data visualization |
| JSON | Configuration and awareness data |
| CSV | Threat intelligence dataset |
| Pytest | Automated testing |

---

## 📁 Project Structure

```text
Cybersecurity-Awareness-Threat-Intelligence-Dashboard/
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
├── frontend/
│   └── index.html
│
├── awareness/
│   ├── awareness_modules.json
│   └── quiz.json
│
├── docs/
│   ├── project_overview.md
│   ├── architecture.md
│   └── api_documentation.md
│
├── reports/
│   └── test_report.md
│
├── screenshots/
│   ├── 01_dashboard.png
│   ├── 02_threat_intelligence.png
│   ├── 03_ioc_search.png
│   ├── 04_alert_management.png
│   ├── 05_vulnerability_management.png
│   ├── 06_swagger_api.png
│   └── 07_security_awareness.png
│
├── tests/
│   ├── test_api.py
│   └── test_ioc_validator.py
│
├── requirements.txt
└── README.md
```

---

## 🚀 Installation & Setup

### 1. Clone or download the project

Open the project directory in a terminal.

### 2. Create a virtual environment

```powershell
python -m venv venv
```

### 3. Activate the virtual environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```powershell
pip install -r requirements.txt
```

If required for testing:

```powershell
pip install pytest httpx2
```

### 5. Start the FastAPI server

From the project root:

```powershell
uvicorn backend.app:app --reload
```

The backend will run at:

```text
http://127.0.0.1:8000
```

---

## 🌐 Dashboard

Open the frontend dashboard:

```text
frontend/index.html
```

The dashboard communicates with the FastAPI backend running on:

```text
http://127.0.0.1:8000
```

---

## 📖 API Documentation

FastAPI automatically provides interactive API documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

Available API areas include:

```text
/
 /api/dashboard/stats
 /api/threats
 /api/threats/{threat_id}
 /api/threats/{threat_id}/enriched
 /api/indicators/search
 /api/alerts
 /api/alerts/generated
 /api/correlation/{threat_id}
 /api/vulnerabilities
 /api/awareness/modules
 /api/quiz
```

---

## 🧪 Testing

The project includes automated tests for core functionality.

Run:

```powershell
pytest -q
```

Testing covers:

- API health
- Dashboard statistics
- Threat retrieval
- IOC validation
- Awareness modules
- Quiz API

Manual API testing was also performed using the FastAPI interactive documentation.

---

## 📈 Demonstration Results

The working demonstration successfully processed:

```text
Threat Records:       2,000
Generated Alerts:     1,089
Critical Alerts:       529
High Alerts:           364
Medium Alerts:          76
Low Alerts:             60
Average Alert Risk:    76.3
```

These values are based on the project's synthetic demonstration dataset.

---

## 🔐 Security Scope

This project is designed for **defensive cybersecurity and educational purposes**.

The threat intelligence data used in the demonstration is synthetic and is intended for:

- Security analysis
- Threat visualization
- IOC validation demonstrations
- Asset correlation
- Alert generation
- Cybersecurity awareness

The project does not perform offensive actions against external systems.

---

## 📸 Project Screenshots

Screenshots demonstrating the working system are available in:

```text
screenshots/
```

The collection includes dashboard, threat intelligence, IOC search, alerts, vulnerabilities, API documentation, and security awareness views.

---

## 🔮 Future Scope

Possible future improvements include:

- Integration with trusted external threat intelligence feeds.
- Database-backed threat storage.
- Authentication and role-based access control.
- Advanced threat correlation.
- Real-time alert notifications.
- Historical threat trend analysis.
- Machine-learning-based risk prediction.
- Improved SOC-style visualization.
- Automated report generation.

---

## 👨‍💻 Project

**Cybersecurity Awareness & Threat Intelligence Dashboard**

Developed as a cybersecurity-focused academic project demonstrating threat intelligence analysis, defensive security monitoring, and cybersecurity awareness.
