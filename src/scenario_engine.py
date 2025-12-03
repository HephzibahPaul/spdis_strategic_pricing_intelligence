"""
Scenario engine: runs 5 deterministic scenarios and returns BA-style outputs
"""

import pandas as pd
from .vps_engine import add_vps_column
from .sensitivity_matrix import build_sensitivity_matrix
from .price_ladder import generate_price_ladder
from .guardrails import apply_guardrails

def run_scenarios(df_prod, base_price, cost_estimate):
    df = df_prod.copy()
    df = add_vps_column(df)
    # Build three candidate prices from ladder
    ladder = generate_price_ladder(df, base_price)
    scenarios = {}

    # Scenario modifiers (multipliers on demand or competitor price)
    scenario_defs = {
        "Expected": {"demand_mul": 1.0, "competitor_mul": 1.0},
        "Best": {"demand_mul": 1.15, "competitor_mul": 1.0},
        "Worst": {"demand_mul": 0.85, "competitor_mul": 0.95},
        "Competitor_Undercut": {"demand_mul": 0.9, "competitor_mul": 0.85},
        "Festival_Surge": {"demand_mul": 1.25, "competitor_mul": 1.05}
    }

    for name, cfg in scenario_defs.items():
        # use ladder mid price as suggested base
        price_candidate = ladder["mid"]
        comp_price = df["competitor_price"].median() * cfg["competitor_mul"]
        # apply guardrails
        ok, adj_price, reason = apply_guardrails(price_candidate, cost_estimate,
                                                margin_threshold_pct=0.20,
                                                price_floor=base_price*0.6,
                                                price_ceiling=base_price*1.5,
                                                competitor_price=comp_price,
                                                min_competitor_gap=-10)
        # compute deterministic demand estimate: use median vps, price elasticity (from matrix)
        mat = build_sensitivity_matrix(df)
        # pick segment = overall median segment (BA simplification)
        elasticity = mat["elasticity"].median()
        median_vps = df["vps"].median()
        # base demand from last observed average
        base_demand = df["demand"].mean()
        # price factor
        price_factor = (adj_price / base_price) ** elasticity if elasticity is not None else 1.0
        demand_pred = max(0, base_demand * price_factor * cfg["demand_mul"] * (median_vps/0.6))
        revenue_pred = adj_price * demand_pred
        scenarios[name] = {
            "candidate_price": float(round(adj_price,2)),
            "reason": reason,
            "predicted_demand": int(round(demand_pred)),
            "predicted_revenue": float(round(revenue_pred,2))
        }
    return scenarios
