# VDP Operations Kit (Life-Sciences: Medical Devices + Cloud)

This open-source kit helps internal security teams and infosec leaders stand up a **Vulnerability Disclosure Program (VDP)** that is:
- **Aligned with U.S. policy expectations** (BOD 20-01 style) and modern disclosure standards.
- **Secure-by-Design**: transparent advisories (CSAF/VEX), SBOM hygiene, and measurable **KEV exposure** reduction.
- **Sector-aware**: guardrails and workflows for **medical devices** and **cloud** platforms.

## Quick start
1. Copy this repo and publish a VDP page using `/01-policy/vdp-policy-template.md` (and deploy `/.well-known/security.txt`).
2. Configure intake & triage: `/02-intake-handling/triage-playbook.md` and mailbox/PGP.
3. Adopt the combined **SSVC + EPSS + KEV + CVSS v4** prioritization in `/03-prioritization/`.
4. Use `/04-remediation-and-disclosure/` for SLAs, checklists, and CSAF/VEX templates.
5. Ship SBOM + VEX practices from `/05-sbom-transparency/`.
6. Enforce **safety-first** device testing in `/06-medical-devices/` and **bounded cloud testing** in `/07-cloud-infrastructure/`.
7. Run the offline tools in `/08-tooling/` to baseline KEV exposure and generate VEX stubs.
8. Track metrics in `/09-metrics/` and run the workshop in `/10-workshops/`.
9. Document results as anonymized case studies in `/11-case-studies/`.

## Licensing
- **Code:** Apache-2.0 (see `LICENSES/LICENSE-APACHE`)
- **Docs:** CC-BY-4.0 (see `LICENSES/LICENSE-CC-BY`)
See root `LICENSE` for dual-license notice.

## Audience
Internal security teams, PSIRT leads, and infosec leadership at life-sciences organizations (medical devices + cloud).
