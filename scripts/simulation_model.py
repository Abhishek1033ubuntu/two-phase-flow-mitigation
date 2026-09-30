"""
===============================================================================
Two-Phase Flow Mitigation: 10-Year Pipeline Specific Resistance Simulation
Co-Engineered in Collaboration with Google Gemini
===============================================================================
"""

import os
import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# SIMULATION PARAMETERS
# =============================================================================
years = np.linspace(0, 10, 100)  # 10-Year Operating Horizon

D_nominal = 0.5        # Pipeline Inner Diameter (meters)
L_pipeline = 500000    # Pipeline Length (500 km)
rho_gas = 0.8          # Gas Density (kg/m^3)
Q_v = 100.0            # Volumetric Flow Rate (m^3/s)

def calculate_dp_per_q(plaque_thickness_mm, parasitic_penalty_ratio=0.0):
    """
    Calculates specific pressure resistance: Pa / (m^3/s) using Darcy-Weisbach flow.
    """
    t_m = plaque_thickness_mm / 1000.0
    D_eff = D_nominal - 2 * t_m
    Area = np.pi * (D_eff / 2.0)**2
    velocity = Q_v / Area
    
    # Roughness increases with plaque growth
    roughness = 0.000045 + (t_m * 0.1)
    f_darcy = 0.25 / (np.log10(roughness / (3.7 * D_eff)))**2
    
    # Darcy-Weisbach equation
    dP = f_darcy * (L_pipeline / D_eff) * (rho_gas * velocity**2 / 2.0)
    
    # Apply parasitic penalty for post-cooler and sacrificial spool hardware
    dP_total = dP * (1.0 + parasitic_penalty_ratio)
    
    return dP_total / Q_v

# 1. Baseline Day-1 Clean State
dP_Q_baseline = calculate_dp_per_q(plaque_thickness_mm=0.0, parasitic_penalty_ratio=0.0)

# 2. Unmitigated System: Plaque grows up to 9.00 mm over 10 years
plaque_unmitigated = 9.00 * (years / 10.0)
dP_Q_unmitigated = calculate_dp_per_q(plaque_unmitigated, parasitic_penalty_ratio=0.0)

# 3. Proposed Mitigated System: Main line plaque capped at 0.10 mm + 0.8% initial penalty
plaque_mitigated = 0.10 * (years / 10.0)
dP_Q_mitigated = calculate_dp_per_q(plaque_mitigated, parasitic_penalty_ratio=0.008)

# =============================================================================
# VISUALIZATION GENERATION & SAVING
# =============================================================================
plt.figure(figsize=(10, 6), dpi=150)
plt.plot(years, dP_Q_unmitigated / 1e3, 'r--', linewidth=2.5, label='Unmitigated System (9.00 mm Plaque)')
plt.plot(years, dP_Q_mitigated / 1e3, 'g-', linewidth=2.5, label='Proposed Mitigated Setup (+0.8% Penalty, 0.10 mm Plaque)')
plt.axhline(y=dP_Q_baseline / 1e3, color='blue', linestyle=':', label='Ideal Baseline (Day 1 Clean Pipe)')

plt.title('Open-Loop Compressor & Pipeline Resistance Over 10-Year Span', fontsize=14, fontweight='bold')
plt.xlabel('Operating Lifespan (Years)', fontsize=12)
plt.ylabel(r'Specific Pressure Resistance ($\mathrm{kPa} / (\mathrm{m}^3/\mathrm{s})$)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=11)
plt.tight_layout()

# Auto-create 'docs' directory if it doesn't exist
os.makedirs('docs', exist_ok=True)

# Save output graph image
plt.savefig('docs/compressor_performance_simulation.png', dpi=300, bbox_inches='tight')
plt.show()

# Print Numeric Metrics
print(f"Baseline Specific Resistance: {dP_Q_baseline / 1e3:.2f} kPa/(m^3/s)")
print(f"Mitigated Year 0 Resistance:  {dP_Q_mitigated[0] / 1e3:.2f} kPa/(m^3/s)")
print(f"Mitigated Year 10 Resistance: {dP_Q_mitigated[-1] / 1e3:.2f} kPa/(m^3/s)")
print(f"Unmitigated Year 10 Resistance: {dP_Q_unmitigated[-1] / 1e3:.2f} kPa/(m^3/s)")
