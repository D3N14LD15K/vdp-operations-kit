#!/usr/bin/env python3
import json, csv, argparse, datetime, sys
from collections import defaultdict

def parse_args():
    ap = argparse.ArgumentParser(description="Offline KEV exposure check")
    ap.add_argument("--assets", required=True)
    ap.add_argument("--sbom", required=True)
    ap.add_argument("--kev", required=True)
    ap.add_argument("--out_report", default="report.csv")
    ap.add_argument("--out_summary", default="summary.json")
    return ap.parse_args()

def load_sbom(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    # Try CycloneDX-like minimal format
    components = []
    if isinstance(data, dict) and "components" in data:
        for c in data["components"]:
            name = c.get("name")
            version = c.get("version")
            cves = [v.get("cve") for v in c.get("vulnerabilities", []) if v.get("cve")]
            components.append({"name": name, "version": version, "cves": cves})
    return components

def load_assets(path):
    rows = []
    with open(path, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            row["internet_exposed"] = str(row.get("internet_exposed","")).lower() in ("1","true","yes")
            rows.append(row)
    return rows

def load_kev(path):
    kev = {}
    with open(path, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            cve = row.get("cve") or row.get("CVE") or row.get("Cve")
            date_added = row.get("date_added") or row.get("Date_Added") or row.get("date")
            if cve:
                kev[cve.strip().upper()] = date_added
    return kev

def main():
    args = parse_args()
    assets = load_assets(args.assets)
    sbom_components = load_sbom(args.sbom)
    kev = load_kev(args.kev)

    # Map CVEs in SBOM to KEV
    kev_cves = set(kev.keys())

    exposed_assets = 0
    total_assets = len(assets)
    total_hits = 0
    earliest = None

    with open(args.out_report, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["asset","version","location","internet_exposed","kev_cve","kev_date_added"])
        for a in assets:
            # naive: check each component's CVEs against KEV
            for c in sbom_components:
                for cve in c.get("cves", []):
                    if cve and cve.upper() in kev_cves:
                        w.writerow([a.get("product"), a.get("version"), a.get("location"), a.get("internet_exposed"), cve.upper(), kev[cve.upper()]])
                        total_hits += 1
                        if a.get("internet_exposed"):
                            exposed_assets += 1
                            try:
                                d = datetime.datetime.fromisoformat(kev[cve.upper()])
                                earliest = d if (earliest is None or d < earliest) else earliest
                            except Exception:
                                pass

    summary = {
        "total_assets": total_assets,
        "assets_with_kev_and_internet_exposed": exposed_assets,
        "kev_exposure_percent": (exposed_assets / total_assets * 100.0) if total_assets else 0.0,
        "total_kev_hits": total_hits,
    }
    if earliest:
        delta = (datetime.datetime.utcnow() - earliest).days
        summary["kev_window_at_risk_days"] = delta

    with open(args.out_summary, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)

    print(json.dumps(summary, indent=2))

if __name__ == "__main__":
    main()
