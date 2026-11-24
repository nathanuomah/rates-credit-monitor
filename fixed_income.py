"""Fixed income toolkit: bond pricing and risk measures."""


def bond_price(face, coupon_rate, ytm, years, freq=1):
    """Price of a fixed-coupon bond.

    face: face value (e.g. 100)
    coupon_rate: annual coupon as a decimal (0.03125 for 3.125%)
    ytm: yield to maturity as a decimal
    years: years to maturity
    freq: coupon payments per year (1 = annual, 2 = semi-annual)
    """
    coupon = face * coupon_rate / freq
    rate = ytm / freq
    periods = years * freq
    pv_coupons = sum([coupon / (1 + rate) ** t for t in range(1, periods + 1)])
    pv_face = face / (1 + rate) ** periods
    return pv_coupons + pv_face
