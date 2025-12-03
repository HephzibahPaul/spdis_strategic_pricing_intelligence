"""
Sensitivity matrix - BA logic to compute elasticity zones
This uses discrete bins of behavior & competitor action to provide interpretable elasticity.
"""

import numpy as np
import pandas as pd

def compute_elasticity(df_segment):
    # BA heuristic: elasticity increases with hesitation & competitor undercut
    # baseline elasticity by product_type
    base = -1.2 if df_segment["product_type"].iloc[0] == "Standard" else -1.0

    # take median vps and median hesitation
    vps = df_segment["vps"].median()
    hesitation = df_segment["hesitation_time"].median()
    competitor_gap = (df_segment["competitor_price"] - df_segment["effective_price"]).median()

    # rule-based elasticity modifier
    mod = 0.0
    if vps < 0.5:
        mod -= 0.4
    if hesitation > 15:
        mod -= 0.3
    if competitor_gap < -3:  # competitor much cheaper
        mod -= 0.6
    if competitor_gap > 5:  # competitor more expensive
        mod += 0.2

    elasticity = base + mod
    return float(round(elasticity, 3))

def build_sensitivity_matrix(df):
    # segments: Bargain, Loyal, Premium by vps quantiles
    df = df.copy()
    q = df["vps"].quantile([0.33, 0.66]).values
    def label_row(row):
        if row["vps"] <= q[0]:
            return "Bargain"
        if row["vps"] <= q[1]:
            return "Loyal"
        return "Premium"
    df["segment_vps"] = df.apply(label_row, axis=1)

    rows = []
    for seg in df["segment_vps"].unique():
        sub = df[df["segment_vps"] == seg]
        # competitor action bins: undercut, neutral, premium
        sub_undercut = sub[sub["competitor_price"] < sub["effective_price"] - 3]
        sub_neutral = sub[np.abs(sub["competitor_price"] - sub["effective_price"]) <= 3]
        sub_premium = sub[sub["competitor_price"] > sub["effective_price"] + 3]
        rows.append({"segment": seg, "competitor_action": "undercut", "elasticity": compute_elasticity(sub_undercut) if len(sub_undercut)>0 else None})
        rows.append({"segment": seg, "competitor_action": "neutral", "elasticity": compute_elasticity(sub_neutral) if len(sub_neutral)>0 else None})
        rows.append({"segment": seg, "competitor_action": "premium", "elasticity": compute_elasticity(sub_premium) if len(sub_premium)>0 else None})
    mat = pd.DataFrame(rows)
    return mat
