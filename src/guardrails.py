"""
Pricing guardrails: enforce price floor, ceiling, margin threshold, competitor gap
"""

def apply_guardrails(price, cost, margin_threshold_pct=0.20, price_floor=None, price_ceiling=None, competitor_price=None, min_competitor_gap= -999):
    # price: candidate price
    # cost: product cost (for simplicity we assume cost = price * (1 - margin_threshold))
    # The function returns (is_valid, adjusted_price, reason)
    # Enforce floor/ceiling
    if price_floor is not None and price < price_floor:
        return False, price_floor, "price < floor"
    if price_ceiling is not None and price > price_ceiling:
        return False, price_ceiling, "price > ceiling"

    # enforce margin
    margin = (price - cost) / price if price > 0 else -1
    if margin < margin_threshold_pct:
        # adjust up to meet margin (simple)
        req_price = cost / (1 - margin_threshold_pct)
        return False, req_price, "margin below threshold"

    # enforce competitor gap (avoid being too far above competitor)
    if competitor_price is not None:
        gap = price - competitor_price
        if gap < min_competitor_gap:
            return False, competitor_price + min_competitor_gap, "competitor gap"
    return True, price, "ok"
