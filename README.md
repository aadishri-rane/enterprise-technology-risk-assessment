# Enterprise Technology Risk & Security Assessment Platform

A beginner-friendly cybersecurity portfolio project analyzing a **fictional** IT asset inventory and simulated vulnerability findings. It uses Python and pandas to apply an illustrative risk-prioritization heuristic and exports ranked open findings.

> **Learning project notice:** All data is synthetic. This is not an EY project, not an official EY methodology, and not a substitute for a formal risk assessment.

## Objectives
- Combine asset inventory and vulnerability findings with pandas.
- Prioritize open findings using vulnerability severity, business criticality, and internet exposure.
- Practice SQL table design and joins.
- Prepare data for a Power BI dashboard.
- Document assumptions and limitations.

## Repository structure
```text
enterprise-technology-risk-assessment/
├── data/
│   ├── assets.csv
│   └── vulnerabilities.csv
├── sql/
│   └── schema.sql
├── src/
│   └── analyze_risks.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Requirements
- Python 3.10+ recommended
- pandas
- MySQL Community Server and MySQL Workbench for the SQL component
- Power BI Desktop for the dashboard component (Windows)

## Run the Python analysis

Open a terminal in the repository root folder.

### Windows
```powershell
py -m venv .venv
.venv\Scripts\activate
py -m pip install -r requirements.txt
py src/analyze_risks.py
```
If `py` is unavailable but `python` works, use `python` in place of `py`.

### macOS / Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python src/analyze_risks.py
```

The script prints open findings sorted by score and creates `data/risk_results.csv`.

## Illustrative scoring method
The score combines:
- CVSS: 60%
- Business criticality: 25%
- Internet exposure: 15%

```text
risk_score = (CVSS / 10 × 60)
           + (criticality_points / 4 × 25)
           + (internet_points / 4 × 15)
```

Criticality maps Low=1, Medium=2, High=3, Critical=4. Internet exposure maps Yes=4 and No=1. Example rating thresholds: Critical ≥80, High ≥60, Medium ≥40, otherwise Low.

These weights and thresholds are for learning only. CVSS is a vulnerability severity measure, not a complete business-risk measure. A mature assessment should document rationale and consider exploitability, control effectiveness, and risk-owner input.

## SQL
Open `sql/schema.sql` in MySQL Workbench. Create the tables, import the two CSV files into the matching tables, then run the example join query.

## Power BI dashboard plan
Import `data/risk_results.csv` after running the Python script. Build:
1. KPI cards for open findings and Critical/High ratings.
2. Bar chart of findings by severity.
3. Bar chart of findings by asset criticality.
4. Table of finding, asset, CVSS, risk score, status, and rating.
5. Slicers for status, severity, department, and internet exposure.

Check dashboard totals against the CSV output.

## Responsible use and limitations
- All records are fictional; no real systems are scanned or tested.
- Risk scores are prioritization aids, not proof that a system is secure or insecure.
- Never upload credentials, confidential company data, or real vulnerability reports to a public repository.
- Keep this README accurate about what you have actually implemented and tested.

## Future improvements
- Add validation and automated tests.
- Track finding age and remediation SLAs.
- Document and test a control-effectiveness factor.
- Add a Power BI dashboard and screenshots.
- Add a sample risk register and remediation recommendations.
