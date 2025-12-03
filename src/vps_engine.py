"""
VPS Engine - Value Perception Score
BA-friendly deterministic formula to compute VPS used in SPDIS
"""

import numpy as np
import pandas as pd

def compute_vps(row):
    # Simple BA formula - weights chosen for interpretability
    w_quality = 0.45
    w_interest = 0.30
    w_brand = 0.15
    w_discount_pref = 0.10

    vps = (w_quality * row["quality_score"] +
           w_interest * row["interest_score"] +
           w_brand * row["brand_score"] -
           w_discount_pref * row["discount_pref"])
    # normalize roughly to 0-1
    return float(np.clip(vps, 0.0, 1.0))

def add_vps_column(df):
    df = df.copy()
    df["vps"] = df.apply(compute_vps, axis=1)
    return df
