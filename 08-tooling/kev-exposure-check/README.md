# KEV Exposure Check (Offline)

**Purpose:** Calculate exposure to Known Exploited Vulnerabilities (KEV) using local files.

**Inputs:**
- `assets.csv` — product, version, location, internet_exposed (true/false)
- `sbom.json` — SPDX or CycloneDX (minimal OK)
- `kev.csv` — subset of KEV catalog (CVE, date_added)

**Outputs:**
- `report.csv` — per asset exposure
- `summary.json` — metrics including KEV exposure % and estimated dwell time

Run: `python kev_check.py --assets sample/assets.csv --sbom sample/sbom.json --kev sample/kev.csv`
