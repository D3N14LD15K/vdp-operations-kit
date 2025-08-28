# SBOM → VEX Assistant (Offline)

Reads a CycloneDX-like SBOM and a CSV of CVEs with statuses to emit a VEX JSON.

CSV columns: `cve,status,justification`
Statuses: NOT_AFFECTED, AFFECTED, FIXED, UNDER_INVESTIGATION

Run: `python vex_from_sbom.py --sbom sample/sbom.json --cves sample/cves.csv --out vex.json`
