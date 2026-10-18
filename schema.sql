CREATE DATABASE IF NOT EXISTS cyber_risk_lab;
USE cyber_risk_lab;

CREATE TABLE assets (
    asset_id VARCHAR(10) PRIMARY KEY,
    asset_name VARCHAR(100) NOT NULL,
    asset_type VARCHAR(40),
    business_criticality VARCHAR(20),
    environment VARCHAR(30),
    owner_department VARCHAR(60),
    internet_facing VARCHAR(5)
);

CREATE TABLE vulnerabilities (
    vulnerability_id VARCHAR(10) PRIMARY KEY,
    asset_id VARCHAR(10) NOT NULL,
    finding VARCHAR(200),
    cvss_score DECIMAL(3,1),
    severity VARCHAR(20),
    status VARCHAR(30),
    identified_date DATE,
    FOREIGN KEY (asset_id) REFERENCES assets(asset_id)
);

-- Import data/assets.csv and data/vulnerabilities.csv into their respective tables first.
SELECT a.asset_name, a.business_criticality, v.finding, v.cvss_score,
       v.severity, v.status
FROM assets AS a
JOIN vulnerabilities AS v ON a.asset_id = v.asset_id
WHERE v.status <> 'Closed'
ORDER BY v.cvss_score DESC;
