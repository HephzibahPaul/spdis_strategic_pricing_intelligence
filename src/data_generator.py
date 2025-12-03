"""
SPDIS data generator - behavioral e-commerce pricing dataset
Outputs: SPDIS/data/spdis_behavioral_data.csv
"""

import os
from datetime import datetime
import numpy as np
import pandas as pd

def make_behavioral_dataset(n_products=2, months=24, seed=42):
    rng = np.random.default_rng(seed)
    start = pd.to_datetime("2023-01-01")
    dates = pd.date_range(start, periods=months, freq="M")

    products = []
    for pid in range(n_products):
        product_type = "Standard" if pid == 0 else "Premium"
        base_price = 50 if product_type == "Standard" else 90
        base_quality = 0.6 if product_type == "Standard" else 0.85
        for dt in dates:
            # competitor price around base
            competitor_price = base_price + rng.normal(0, 8)

            # behavioral signals (BA-style, interpretable)
            interest_score = float(np.clip(rng.normal(0.6, 0.18), 0.05, 1.0))      # 0-1
            hesitation_time = float(np.clip(rng.normal(12 if product_type=="Standard" else 8, 6), 1, 60)) # seconds
            scroll_depth = float(np.clip(rng.normal(0.45 if product_type=="Standard" else 0.6, 0.2), 0, 1))  # 0-1
            revisit_score = float(np.clip(rng.normal(0.12 if product_type=="Standard" else 0.08, 0.07), 0, 1))
            add_to_cart_rate = float(np.clip(rng.normal(0.08 if product_type=="Standard" else 0.04, 0.04), 0.001, 1.0))
            discount_pref = float(np.clip(rng.normal(0.18 if product_type=="Standard" else 0.10, 0.1), 0, 1.0))

            # base price variations + occasional promo
            price = float(round(base_price + rng.normal(0, base_price*0.12), 2))
            promo = rng.random() < 0.35
            discount_pct = float(round(rng.normal(5, 3), 2)) if promo else 0.0
            effective_price = round(price * (1 - discount_pct/100), 2)

            # quality + brand score
            quality_score = float(np.clip(base_quality + rng.normal(0,0.08), 0, 1.0))
            brand_score = float(np.clip(rng.normal(0.5 if product_type=="Standard" else 0.7, 0.12), 0, 1.0))

            # Value Perception Score (raw, will be refined by VPS engine)
            perceived_value = (quality_score * 0.5 + interest_score * 0.3 + brand_score * 0.2)

            # simple deterministic demand calculation (BA logic, not ML)
            # demand influenced by effective price relative to base_price and perceived value and add_to_cart
            price_factor = (effective_price / base_price)
            demand_base = 2000 if product_type == "Standard" else 1200
            demand = demand_base * (perceived_value / 0.6) * (1 / (price_factor ** 1.4)) \
                     * (1 + 0.2 * np.log1p(add_to_cart_rate*100)) * (1 + 0.06 * np.log1p(1000*revisit_score))

            # season factor for months like Nov/Dec or mid-year sale
            month = dt.month
            season_factor = 1.25 if month in (11, 12) else (1.15 if month in (6,7) else 1.0)
            demand = max(0, demand * season_factor * rng.normal(1, 0.08))
            revenue = round(effective_price * demand, 2)

            products.append({
                "date": dt.strftime("%Y-%m-%d"),
                "product_id": f"P{pid+1}",
                "product_type": product_type,
                "price": round(price,2),
                "discount_pct": round(discount_pct,2),
                "effective_price": effective_price,
                "competitor_price": round(competitor_price,2),
                "interest_score": round(interest_score,3),
                "hesitation_time": round(hesitation_time,2),
                "scroll_depth": round(scroll_depth,3),
                "revisit_score": round(revisit_score,3),
                "add_to_cart_rate": round(add_to_cart_rate,4),
                "discount_pref": round(discount_pref,3),
                "quality_score": round(quality_score,3),
                "brand_score": round(brand_score,3),
                "perceived_value": round(perceived_value,3),
                "season_factor": season_factor,
                "demand": round(demand,0),
                "revenue": revenue
            })

    df = pd.DataFrame(products)
    return df

def save_behavioral_data(output_path=os.path.join("..","data","spdis_behavioral_data.csv")):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df = make_behavioral_dataset(n_products=2, months=24, seed=42)
    df.to_csv(output_path, index=False)
    print(f"Synthetic behavioral data saved to: {output_path}")

if __name__ == "__main__":
    save_behavioral_data()
