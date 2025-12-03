"""
3-tier price ladder generator - BA rules
"""

def generate_price_ladder(df, base_price):
    # entry = slightly below median effective, mid = median, premium = somewhat higher
    entry = round(base_price * 0.9, 2)
    mid = round(base_price, 2)
    premium = round(base_price * 1.15, 2)
    return {"entry": entry, "mid": mid, "premium": premium}
