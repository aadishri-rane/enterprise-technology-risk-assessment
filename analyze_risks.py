"""Analyze fictional vulnerability findings and rank open items by an illustrative score."""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
assets = pd.read_csv(ROOT / "data" / "assets.csv")
vulns = pd.read_csv(ROOT / "data" / "vulnerabilities.csv")
data = vulns.merge(assets, on="asset_id", how="left")

# Educational heuristic only, not an official standard:
# CVSS contributes 60%, business criticality 25%, internet exposure 15%.
criticality_weight = {"Low": 1, "Medium": 2, "High": 3, "Critical": 4}
data["criticality_points"] = data["business_criticality"].map(criticality_weight).fillna(1)
data["internet_points"] = data["internet_facing"].map({"Yes": 4, "No": 1}).fillna(1)
data["risk_score"] = (
    (data["cvss_score"] / 10 * 60)
    + (data["criticality_points"] / 4 * 25)
    + (data["internet_points"] / 4 * 15)
).round(1)

def label(score):
    if score >= 80:
        return "Critical"
    if score >= 60:
        return "High"
    if score >= 40:
        return "Medium"
    return "Low"

data["risk_rating"] = data["risk_score"].apply(label)
open_findings = data[data["status"].str.lower() != "closed"].copy()
open_findings = open_findings.sort_values("risk_score", ascending=False)
columns = ["vulnerability_id", "asset_name", "finding", "cvss_score",
           "business_criticality", "internet_facing", "status", "risk_score", "risk_rating"]
print("\\nOPEN FINDINGS — HIGHEST RISK FIRST")
print(open_findings[columns].to_string(index=False))
output = ROOT / "data" / "risk_results.csv"
open_findings.to_csv(output, index=False)
print(f"\\nSaved results to: {output}")
