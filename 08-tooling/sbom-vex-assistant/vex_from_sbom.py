#!/usr/bin/env python3
import json, csv, argparse, datetime

def parse_args():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sbom", required=True)
    ap.add_argument("--cves", required=True)
    ap.add_argument("--out", default="vex.json")
    return ap.parse_args()

def main():
    a = parse_args()
    with open(a.sbom,"r",encoding="utf-8") as f:
        sbom = json.load(f)
    products = sorted({f"{c.get('name')} {c.get('version')}" for c in sbom.get("components",[])})
    entries = []
    with open(a.cves, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            entries.append({
                "cve": row["cve"].strip(),
                "status": row["status"].strip(),
                "status_justification": row.get("justification","").strip(),
                "products": products
            })
    vex = {"vulnerabilities": entries, "metadata": {"author":"Your Org","timestamp": datetime.datetime.utcnow().isoformat()+"Z"}}
    with open(a.out,"w",encoding="utf-8") as f:
        json.dump(vex, f, indent=2)
    print(f"Wrote {a.out} with {len(entries)} entries.")
if __name__ == "__main__":
    main()
