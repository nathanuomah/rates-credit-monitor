"""Fixed income toolkit: bond pricing and risk measures."""


def bond_price(face, coupon_rate, ytm, years):
    """Price of a bond with annual coupons.

    face: face value (e.g. 100)
    coupon_rate: annual coupon as a decimal (0.03125 for 3.125%)
    ytm: yield to maturity as a decimal
    years: years to maturity
    """
    coupon = face * coupon_rate
    pv_coupons = sum([coupon / (1 + ytm) ** t for t in range(1, years + 1)])
    pv_face = face / (1 + ytm) ** years
    return pv_coupons + pv_face
