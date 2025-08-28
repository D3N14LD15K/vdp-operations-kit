# SSVC Calculator (Simple)

Input JSON with:
```
{
  "exploitation": "none|poc|active",
  "exposure": "internal|partner|internet",
  "safety": "none|potential|confirmed",
  "automatable": "low|high"
}
```
Run: `python ssvc_calc.py --in sample/input.json --out decision.json`
