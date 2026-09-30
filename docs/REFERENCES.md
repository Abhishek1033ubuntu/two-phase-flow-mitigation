# Repository References & Citation Index

This document provides the formal mapping for all citation markers used throughout the README, technical report, and simulation documentation in this repository.

---

## Primary Document Citations

### `[1]` / `[cite: 5]` — Master Technical Report
* **Document Title:** Engineering Technical Report: Two-Phase Flow & Contamination Mitigation in Compression Systems
* **Document File:** [`docs/TECHNICAL-REPORT-FINAL.md`](TECHNICAL-REPORT-FINAL.md)
* **Scope & Coverage:** 
  - Comprehensive problem statement for closed-loop and open-loop regimes.
  - Material synthesis & calculations via `subatomic-materials-suite` (FVMQ core, SMPU-G glass transition tuning at $T_g = -5.0^\circ\text{C}$).
  - Hermetic source isolation & dedicated intercooled 20-meter service spool specifications.
  - 98.8% main line plaque reduction efficacy and 48-hour cleaning performance.

---

### `[2]` / `[cite: 2]` — Hydraulic Simulation Data & Analytical Methodology
* **Document Title:** Hydraulic Simulation Data & Analytical Methodology
* **Document File:** [`docs/hydraulic-simulation-data.md`](hydraulic-simulation-data.md)
* **Scope & Coverage:**
  - Darcy-Weisbach fluid flow formulations and Colebrook-White friction factor models.
  - 10-year comparative specific resistance dataset ($12,785\ \text{kPa}/(\text{m}^3/\text{s})$ vs $29,035\ \text{kPa}/(\text{m}^3/\text{s})$).
  - Hydrostatic head loss calculations across $+500\text{ m}$ elevation climbs ($0.039\text{ bar}$ drop).
  - Diaphragm compressor discharge pressure margin analysis ($+46.8\text{ to }+66.8\text{ bar}$).

---

### `[3]` — Python Simulation Source Code
* **Script File:** [`scripts/simulation_model.py`](../scripts/simulation_model.py)
* **Scope & Coverage:**
  - Executable Python model generating 10-year drag resistance and 48-hour closed-loop plaque removal curves.
  - Automated visualization export to `docs/dual_regime_simulation_comparison.png`.
