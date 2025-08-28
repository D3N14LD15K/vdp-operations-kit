#!/usr/bin/env python3
import argparse, yaml, datetime

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True)
    ap.add_argument("--out", default="security.txt")
    args = ap.parse_args()
    with open(args.config,"r",encoding="utf-8") as f:
        cfg = yaml.safe_load(f)
    lines = []
    for k in ["Contact","Encryption","Policy","Acknowledgments","Preferred-Languages"]:
        if cfg.get(k):
            lines.append(f"{k}: {cfg[k]}")
    if cfg.get("ExpiresDays"):
        exp = (datetime.datetime.utcnow()+datetime.timedelta(days=int(cfg["ExpiresDays"]))).strftime("%Y-%m-%dT%H:%M:%SZ")
        lines.append(f"Expires: {exp}")
    with open(args.out,"w",encoding="utf-8") as f:
        f.write("\n".join(lines)+"\n")
    print(f"Wrote {args.out}")
if __name__ == "__main__":
    main()
