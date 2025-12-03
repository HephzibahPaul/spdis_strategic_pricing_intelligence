"""
Shock simulator - deterministic BA rules to apply shocks and see impact
"""

def apply_shock(df_prod, shock_type="festival", intensity=0.25):
    # shock_type: "festival", "competitor_flash", "supply_shortage", "viral"
    # intensity: percent effect on demand
    base_demand = df_prod["demand"].mean()
    if shock_type == "festival":
        demand_new = base_demand * (1 + intensity)
    elif shock_type == "competitor_flash":
        demand_new = base_demand * (1 - intensity)
    elif shock_type == "supply_shortage":
        demand_new = base_demand * (1 - intensity)
    elif shock_type == "viral":
        demand_new = base_demand * (1 + intensity*1.1)
    else:
        demand_new = base_demand
    return int(round(demand_new))
