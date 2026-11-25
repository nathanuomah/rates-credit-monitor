"""Fixed income toolkit: bond pricing and risk measures."""


def cash_flows(face, coupon_rate, years, freq=1):
    """List of a bond's cash flows, one per coupon period.

    The face value is repaid with the last coupon.
    """
    coupon = face * coupon_rate / freq
    periods = years * freq
    flows = [coupon] * periods
    flows[-1] += face
    return flows


def bond_price(face, coupon_rate, ytm, years, freq=1):
    """Price of a fixed-coupon bond.

    face: face value (e.g. 100)
    coupon_rate: annual coupon as a decimal (0.03125 for 3.125%)
    ytm: yield to maturity as a decimal
    years: years to maturity
    freq: coupon payments per year (1 = annual, 2 = semi-annual)
    """
    flows = cash_flows(face, coupon_rate, years, freq)
    rate = ytm / freq
    return sum([cf / (1 + rate) ** t for t, cf in enumerate(flows, start=1)])
    
