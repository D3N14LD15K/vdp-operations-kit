#!/usr/bin/env python3
import json, argparse

def decide(i):
    ex = i.get("exploitation","none")
    exp = i.get("exposure","internal")
    saf = i.get("safety","none")
    auto = i.get("automatable","low")
    if saf == "confirmed": return "Act"
    if ex in ("active","poc") and exp == "internet": return "Act"
    if exp == "internet" or (ex in ("active","poc")): return "Attend"
    if exp in ("partner",) or auto == "high": return "Track"
    return "Defer"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="inp", required=True)
    ap.add_argument("--out", default="decision.json")
    args = ap.parse_args()
    with open(args.inp,"r",encoding="utf-8") as f:
        data = json.load(f)
    decision = {"decision": decide(data), "inputs": data}
    with open(args.out,"w",encoding="utf-8") as f:
        json.dump(decision, f, indent=2)
    print(json.dumps(decision, indent=2))

if __name__ == "__main__":
    main()
