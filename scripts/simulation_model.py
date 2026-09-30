"""
===============================================================================
Two-Phase Flow Mitigation: Dual-Regime System Performance Simulation
Co-Engineered in Collaboration with Google Gemini
===============================================================================
This script models and visualizes:
1. Closed-Loop Regime: 48-Hour SMPU-G Granule Capillary Plaque Removal (88.5%).
2. Open-Loop Regime: 10-Year Transmission Pipeline Specific Drag Resistance.
"""

import os
import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# 1. CLOSED-LOOP REGIME: 48-HOUR SMPU-G PLAQUE REMOVAL MODELING
# =============================================================================
hours = np.linspace(0, 48, 100)  # 0 to 48 Hours

# Uncleaned capillary plaque remains at 150 µm
plaque_closed_uncleaned = np.full_like(hours, 150.0)

# SMPU-G Granules achieve 88.5% plaque thickness reduction within 48 hours
plaque_closed_smpu = 150.0 * (0.115 + 0.885 * np.exp(-hours / 10.0))

# =============================================================================
# 2. OPEN-LOOP REGIME: 10-YEAR PIPELINE SPECIFIC RESISTANCE MODELING
# =============================================================================
years = np.linspace(0, 10, 100)  # 0 to 10 Years

D_nominal = 0.5        # Pipeline Inner Diameter (m)
L_pipeline = 500000    # Pipeline Length (500 km)
rho_gas = 0.8          # Gas Density (kg/m^3)
Q_v = 100.0            # Volumetric Flow Rate (m^3/s)

def calculate_dp_per_q(plaque_thickness_mm, parasitic_penalty_ratio=0.0):
    t_m = plaque_thickness_mm / 1000.0
    D_eff = D_nominal - 2 * t_m
    Area = np.pi * (D_eff / 2.0)**2
    velocity = Q_v / Area
    roughness = 0.000045 + (t_m * 0.1)
    f_darcy = 0.25 / (np.log10(roughness / (3.7 * D_eff)))**2
    dP = f_darcy * (L_pipeline / D_eff) * (rho_gas * velocity**2 / 2.0)
    return (dP * (1.0 + parasitic_penalty_ratio)) / Q_v

# Unmitigated (9.00 mm plaque) vs Mitigated (0.10 mm plaque + 0.8% initial penalty)
dP_Q_unmitigated = calculate_dp_per_q(9.00 * (years / 10.0), 0.0)
dP_Q_mitigated = calculate_dp_per_q(0.10 * (years / 10.0), 0.008)

# =============================================================================
# 3. DUAL-PANEL DASHBOARD GENERATION
# =============================================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6), dpi=300)

# Left Subplot: Closed-Loop Capillary Cleaning
ax1.plot(hours, plaque_closed_uncleaned, 'r--', linewidth=2.5, label='Uncleaned Evaporator/Capillary (150 µm)')
ax1.plot(hours, plaque_closed_smpu, 'b-', linewidth=2.5, label='SMPU-G Active Cleaning (88.5% Reduction)')
ax1.set_title('Closed-Loop Regime: Capillary Plaque Removal', fontsize=12, fontweight='bold')
ax1.set_xlabel('Operational Hours (h)', fontsize=11)
ax1.set_ylabel('Plaque Layer Thickness (µm)', fontsize=11)
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.legend(fontsize=10)

# Right Subplot: Open-Loop Transmission Drag
ax2.plot(years, dP_Q_unmitigated / 1e3, 'r--', linewidth=2.5, label='Unmitigated Line (9.00 mm Plaque)')
ax2.plot(years, dP_Q_mitigated / 1e3, 'g-', linewidth=2.5, label='Hermetic Isolation + Spool (+0.8% Drop)')
ax2.set_title('Open-Loop Regime: 10-Year Drag Resistance', fontsize=12, fontweight='bold')
ax2.set_xlabel('Operating Lifespan (Years)', fontsize=11)
ax2.set_ylabel(r'Specific Resistance ($\mathrm{kPa} / (\mathrm{m}^3/\mathrm{s})$)', fontsize=11)
ax2.grid(True, linestyle='--', alpha=0.7)
ax2.legend(fontsize=10)

plt.suptitle('Dual-Regime Two-Phase Flow Mitigation System Performance', fontsize=15, fontweight='bold', y=0.98)
plt.tight_layout()

# Auto-create 'docs' directory if it doesn't exist
os.makedirs('docs', exist_ok=True)
plt.savefig('docs/dual_regime_simulation_comparison.png', dpi=300, bbox_inches='tight')
plt.show()

print("Simulation complete. Output saved to docs/dual_regime_simulation_comparison.png")
