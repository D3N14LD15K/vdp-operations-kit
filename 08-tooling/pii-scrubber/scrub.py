#!/usr/bin/env python3
import re, argparse

PATTERNS = [
    (re.compile(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'), '[REDACTED_EMAIL]'),
    (re.compile(r'\b\d{3}-\d{2}-\d{4}\b'), '[REDACTED_SSN]'),
    (re.compile(r'\b(?:\+?\d{1,3})?[\s\-]?\(?\d{3}\)?[\s\-]?\d{3}[\s\-]?\d{4}\b'), '[REDACTED_PHONE]')
]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="inp", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    with open(args.inp,"r",encoding="utf-8") as f:
        txt = f.read()
    for rx, repl in PATTERNS:
        txt = rx.sub(repl, txt)
    with open(args.out,"w",encoding="utf-8") as f:
        f.write(txt)
    print(f"Redacted -> {args.out}")

if __name__ == "__main__":
    main()
