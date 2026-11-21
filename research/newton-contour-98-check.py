"""Outward packet and Cauchy bounds on a contour around the cold square."""

import json
from pathlib import Path
import runpy

from flint import acb, arb, arb_poly, ctx


SCALED_PRICES = (
    0, 100000000, 252200485, 426274040, 611406156, 802387069, 996550741,
    1192477542, 1389393325, 1586868991, 1784663875, 1982641789,
    2180725131, 2378869432, 2577049092, 2775249319, 2973461537,
    3171680760, 3369904083, 3568129809, 3766356945, 3964584907,
    4162813351, 4361042071, 4559270933,
)


def bound_prefix(box, data, compute_rate):
    fields, symmetric, tilt, eps = (data[key] for key in ("fields", "symmetric", "tilt", "eps"))
    n, keep = data["N"], data["KEEP"]
    rows, amplitudes = fields["upper"](box)
    rows = [[value.upper() for value in row] for row in rows]
    assert all(value >= 0 for row in rows for value in row)
    assert all(value < 1 for value in amplitudes)
    upper_folds = [symmetric(row, keep) for row in rows]
    upper_tilts = [sum(v*w for v, w in zip(row, tilt)) for row in rows]
    a, b, c, d, z, w, v = amplitudes
    seed = fields["kern"]["dim"]

    def weighted(poly, radius):
        return sum(poly[radius+k]*(2 if k else 1)*tilt[k] for k in range(radius+1))

    center_mass = seed+2*a+3*b+4*c+arb(23)*d/4+8*(z+w+v)
    center_tilt = (seed*tilt[1]+a*(1+tilt[2])+b*(1+3*tilt[1]/2+3*tilt[3]/2)
                   +c*weighted(fields["kern"]["F"], 4)+d*weighted(fields["kern"]["G"], 5)
                   +z*weighted(fields["old"]["R"], 2)+(w+v)*weighted(fields["field"], 4))
    floor = box.real.lower()
    bn = arb(1)
    for i in range(1, 16):
        bn *= (arb(3)/2-i)/i
    tail_factor = 2*abs(box).sqrt()*abs(bn)
    cap = arb("4.8")
    assert (8+arb(4)/10**30).sqrt() < seed.upper()
    raw = 2*abs(box).sqrt()*(2-(1-cap**2/(4*floor)).sqrt())
    assert 2*raw < 34 and 2*abs(box).sqrt() < 9
    assert (cap**2/(2*arb("1e30").sqrt())
            +2*abs(box).sqrt()*(1-(1-cap**2/(4*floor)).sqrt())) < 11
    assert arb(3)*(34+11+16)/(2*10**15) < arb("1e-12")

    prices = [arb(i)/10**8 for i in SCALED_PRICES]
    slope = prices[-1]-prices[-2]
    assert all(k <= x <= 2*k for k, x in enumerate(prices)) and 1 < slope < 2

    def price(k):
        k = abs(k)
        if k < len(prices):
            return prices[k]
        return prices[-1]+(k+1-len(prices))*slope

    packets = [arb(0)]*n
    residual = arb(1)
    rate = arb(0)
    for height in range(101):
        zero = sum(i*x for i, x in enumerate(packets))+arb(14)/5*eps+arb("1e-8")
        core = symmetric([zero]+packets, n)
        norm = zero+sum(x*w for x, w in zip(packets, tilt[1:]))+eps
        ratio = (center_tilt+norm)**2/(4*floor)
        assert ratio < 1
        assert center_mass+sum(k*x for k, x in enumerate(packets, 1))+4*eps < cap
        power = arb_poly([0]*keep+[1])
        retained, derivative = arb_poly(), arb_poly()
        for j, row in enumerate(upper_folds):
            if j:
                if compute_rate and height:
                    derivative_term = row*power
                    derivative += arb_poly([j*derivative_term[k+2*keep] for k in range(n+1)])
                next_power = power*core
                power = arb_poly([next_power[k+n] for k in range(2*keep+1)])
            product = row*power
            retained += arb_poly([product[k+2*keep] for k in range(n+1)])
        inside = retained[0]+2*sum(retained[k]*tilt[k] for k in range(1, n+1))
        lost = sum(w*norm**j for j, w in enumerate(upper_tilts))-inside
        lost += tail_factor*ratio**15/(1-ratio)
        assert lost < eps

        if compute_rate and height:
            mu = [derivative[k]*(2 if k else 1) for k in range(n+1)]
            lost_derivative = (sum(j*w*norm**(j-1) for j, w in enumerate(upper_tilts) if j)
                               -sum(v*w for v, w in zip(mu, tilt)))
            lost_derivative += 2*tail_factor*ratio**15/(center_tilt+norm)*(
                15/(1-ratio)+ratio/(1-ratio)**2)
            assert lost_derivative >= 0
            mass = sum(mu)
            moment = sum(v*price(k) for k, v in enumerate(mu))
            charge = [((k-1)*moment+sum(v*(price(k+u)+price(k-u))/2
                       for u, v in enumerate(mu)))/price(k) for k in range(1, n+len(prices)+1)]
            rate = max(x.upper() for x in charge+[moment/slope+mass])+10*lost_derivative+arb("1e-12")
            residual *= rate

        new_packets = [(2*retained[k]).upper() for k in range(1, n+1)]
        new_packets[0] += arb("1e-12")
        assert all(before <= after for before, after in zip(packets, new_packets))
        if height == 0:
            residual = sum(price(k)*x for k, x in enumerate(new_packets, 1))+8*eps
        packets = new_packets

    assert 2*abs(box).sqrt()*cap/(4*floor*(1-cap**2/(4*floor)).sqrt()) < 1
    if compute_rate:
        assert rate < 1
        return residual/(1-rate)


def main():
    data = runpy.run_path(str(Path(__file__).with_name("astra-predictor-76-check.py")))
    ctx.prec = 192
    center, half, radius = arb(2031)/128, arb(2)**-17, arb(1)/125
    bound_prefix(acb(arb(center, radius), arb(0, radius)), data, False)
    pieces = 8
    length = 2*radius/pieces
    integral = arb(0)
    for k in range(pieces):
        left = -radius+k*length
        side = arb(left+length/2, length/2)
        distance = max(arb(0), abs(side).lower()-half)
        distance_squared = (radius-half)**2+distance**2
        # Conjugacy gives the same estimate on the lower horizontal edge.
        integral += 2*length*bound_prefix(acb(center+side, radius), data, True)/distance_squared
        integral += length*bound_prefix(acb(center-radius, side), data, True)/distance_squared
        integral += length*bound_prefix(acb(center+radius, side), data, True)/distance_squared
    derivative = integral/(2*arb.pi())
    floor = center-half
    imaginary = half*((21+derivative)/floor.sqrt()+arb("4.843")/(2*floor**arb("1.5")))
    assert derivative < arb("15.811") and imaginary < arb("7.1e-5")
    boundary_scale = (2*arb("1e-4")/arb(3).sqrt()-arb("7.1e-5"))*floor.sqrt()/124600
    assert boundary_scale > arb("1.4e-9")
    print(json.dumps(dict(kind="newton_predictor_full_square_cauchy_contour",
                          contour_half_width="0.008", segments=4*pieces,
                          newton_correction_derivative_upper=derivative.str(14),
                          rotated_nominal_imaginary_upper=imaginary.str(14),
                          full_square_sqrt_n_residual_squared_lower=boundary_scale.str(14)),
                     sort_keys=True))


if __name__ == "__main__":
    main()
