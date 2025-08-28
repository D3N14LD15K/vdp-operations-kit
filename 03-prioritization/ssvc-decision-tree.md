# SSVC Decision Tree (Simplified)

Inputs:
- Exploitation: {None, PoC, Active}
- Exposure: {Internal, Partner, Internet}
- Safety Impact (devices): {None, Potential, Confirmed}
- Automatable: {Low, High}

Outcome:
- **Act**: Active/PoC + Internet OR any Safety=Confirmed.
- **Attend**: Internet exposure with potential impact.
- **Track**: Internal exposure, no exploitation.
- **Defer**: Low exposure, no exploitation, trivial impact.

Record SSVC outcome alongside EPSS score, KEV flag, and CVSS v4 vector.
