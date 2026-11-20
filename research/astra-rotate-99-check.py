"""Outward physical predictor, complex-square and first-contact coefficients."""

import json
from pathlib import Path
import runpy

from flint import acb, arb, arb_poly, ctx


def packet_snapshot(box, data, prices):
    """Repeat the R98 forward comparison and price only the last derivative."""
    fields, tilt = data["fields"], data["tilt"]
    n, keep, eps, symmetric = (data[k] for k in ("N", "KEEP", "eps", "symmetric"))
    rows, pars = fields["upper"](box)
    rows = [[x.upper() for x in row] for row in rows]
    assert all(x >= 0 for row in rows for x in row)
    folds = [symmetric(row, keep) for row in rows]
    norms = [sum(v*w for v, w in zip(row, tilt)) for row in rows]
    assert all(v < 1 for v in pars)
    a, b, c, d, z, w, v = pars
    seed = fields["kern"]["dim"]

    def weighted(poly, radius):
        return sum(poly[radius+k]*(2 if k else 1)*tilt[k] for k in range(radius+1))

    cap, floor = arb("4.8"), box.real.lower()
    assert (8+arb(4)/10**30).sqrt() < seed.upper()
    raw = 2*abs(box).sqrt()*(2-(1-cap**2/(4*floor)).sqrt())
    assert 2*raw < 34 and 2*abs(box).sqrt() < 9
    assert (cap**2/(2*arb("1e30").sqrt())
            +2*abs(box).sqrt()*(1-(1-cap**2/(4*floor)).sqrt())) < 11
    assert arb(3)*(34+11+16)/(2*10**15) < arb("1e-12")
    assert 2*abs(box).sqrt()*cap/(4*floor*(1-cap**2/(4*floor)).sqrt()) < 1
    mass = seed+2*a+3*b+4*c+arb(23)*d/4+8*(z+w+v)
    center = (seed*tilt[1]+a*(1+tilt[2])+b*(1+3*tilt[1]/2+3*tilt[3]/2)
              +c*weighted(fields["kern"]["F"], 4)+d*weighted(fields["kern"]["G"], 5)
              +z*weighted(fields["old"]["R"], 2)+(w+v)*weighted(fields["field"], 4))
    slope = prices[-1]-prices[-2]

    def price(k):
        k = abs(k)
        return prices[k] if k < len(prices) else prices[-1]+(k+1-len(prices))*slope

    binomial = arb(1)
    for k in range(1, 16):
        binomial *= (arb(3)/2-k)/k
    tail = 2*abs(box).sqrt()*abs(binomial)
    packets = [arb(0)]*n
    for height in range(101):
        zero = sum(i*x for i, x in enumerate(packets))+arb(14)/5*eps+arb("1e-8")
        core = symmetric([zero]+packets, n)
        norm = zero+sum(v*w for v, w in zip(packets, tilt[1:]))+eps
        ratio = (center+norm)**2/(4*box.real.lower())
        assert ratio < 1 and mass+sum(k*x for k, x in enumerate(packets, 1))+4*eps < arb("4.8")
        power = arb_poly([0]*keep+[1])
        kept, der = arb_poly(), arb_poly()
        for j, row in enumerate(folds):
            if j:
                if height == 100:
                    term = row*power
                    der += arb_poly([j*term[k+2*keep] for k in range(n+1)])
                next_power = power*core
                power = arb_poly([next_power[k+n] for k in range(2*keep+1)])
            term = row*power
            kept += arb_poly([term[k+2*keep] for k in range(n+1)])
        discarded = (sum(v*norm**j for j, v in enumerate(norms))
                     -kept[0]-2*sum(kept[k]*tilt[k] for k in range(1, n+1))
                     +tail*ratio**15/(1-ratio))
        assert discarded < eps
        if height == 100:
            mu = [der[k]*(2 if k else 1) for k in range(n+1)]
            missing = (sum(j*v*norm**(j-1) for j, v in enumerate(norms) if j)
                       -sum(v*w for v, w in zip(mu, tilt))
                       +2*tail*ratio**15/(center+norm)*(15/(1-ratio)+ratio/(1-ratio)**2))
            assert missing >= 0
            moment = sum(price(k)*v for k, v in enumerate(mu))
            charges = [((k-1)*moment+sum(v*(price(k+j)+price(k-j))/2
                       for j, v in enumerate(mu)))/price(k) for k in range(1, n+len(prices)+1)]
            rate = max(x.upper() for x in charges+[sum(mu)+moment/slope])+10*missing+arb("1e-12")
            return rate, initial_price
        next_packets = [(2*kept[k]).upper() for k in range(1, n+1)]
        next_packets[0] += arb("1e-12")
        assert all(x <= y for x, y in zip(packets, next_packets))
        packets = next_packets
        if height == 0:
            initial_price = sum(price(k)*x for k, x in enumerate(packets, 1))+8*eps


def main():
    base = Path(__file__).resolve().parent
    data = runpy.run_path(str(base/"astra-predictor-76-check.py"))
    contour = runpy.run_path(str(base/"newton-contour-98-check.py"))
    ctx.prec = 192
    prices = [arb(i)/10**8 for i in contour["SCALED_PRICES"]]
    a, h = arb(2031)/128, arb(2)**-17
    radius = arb("0.006")
    length = radius/4
    integral = arb(0)
    max_rate = arb(0)
    for k in range(8):
        tangential = arb(-radius+(k+arb(1)/2)*length, length/2)
        distance = max(arb(0), abs(tangential).lower()-h)
        squared = (radius-h)**2+distance**2
        for box, multiplicity in [(acb(a+tangential, radius), 2),
                                  (acb(a-radius, tangential), 1),
                                  (acb(a+radius, tangential), 1)]:
            rate, _ = packet_snapshot(box, data, prices)
            assert rate < 1
            max_rate = max(max_rate, rate.upper())
            translated = arb(2).sqrt()*(2/(1-rate)-1)
            integral += multiplicity*length*translated/squared
    imaginary_entry = h*integral/(2*arb.pi())
    assert imaginary_entry < arb("0.283")
    print(json.dumps(dict(kind="translated_imaginary_entry",
                          contour_radius=radius.str(10), max_rate=max_rate.str(12),
                          scaled_imaginary_entry=imaginary_entry.str(12))), flush=True)

    floor = a-h
    d, first, res_sup = arb("0.51358"), arb("0.169724"), arb("0.001180")
    time = arb(9)*arb("0.984138")**100+arb(".36")*(1-arb("0.984138")**100)/(1-arb("0.984138"))
    assert time < 21
    predictor_phase = (h*(21/(2*floor.sqrt())+arb("4.768")/(4*floor**arb("1.5")))).asin()
    mark_phase = (h/floor).atan()/2
    assert predictor_phase < arb(".000021")
    total_phase = arb(".00008")
    assert (arb(".0001")/arb(3).sqrt()).asin()+predictor_phase < total_phase
    assert mark_phase+predictor_phase < total_phase
    kappa = 2*mark_phase+predictor_phase+total_phase
    assert kappa < arb(".000106")
    cosine = total_phase.cos()
    weight = 1/(4*floor*arb(".000021").cos()*cosine)
    cosh = (1+arb(".6")**2).sqrt()
    A = cosh/cosine.sqrt()
    C = (cosh+arb(".6"))/(4*floor.sqrt()*cosine)
    den = 1-2*C*res_sup
    M = (A+(A**2-den).sqrt())/den
    assert M*M < arb("3.122")
    mixing = total_phase.tan()/2
    b = (A*A-1).sqrt()
    k = mixing+C*res_sup
    k2 = k+max((A*k/b).upper(), (k*k+mixing**2).sqrt().upper())
    source_pure = weight*M**2*(kappa+2*k2)
    source_mixed = 2*weight*M*(A+b)
    assert source_pure < arb(".000055") and source_mixed < arb(".09834")
    assert weight*M**2 < arb(".04919")
    assert M**2/(4*floor.sqrt()*arb(".000021").cos()*cosine) < arb(".197")
    diagonal = weight*(arb(".283")+178*kappa)*M**2
    pure = diagonal+weight*356*M**2*k2
    cross = weight*356*M*(A+b)
    assert pure < arb(".024") and cross < arb("17.51") and diagonal < arb(".015")
    margin = 2*arb("1e-4")/arb(3).sqrt()-arb("7.1e-5")
    assert margin > arb("4.4470e-5") and margin/(weight*178*M**2) > arb("5.07e-6")
    dh = (4*(a+2*h)*21+2*arb("4.768"))/(4*floor-4)**arb("1.5")
    residual_phase = h*(42/first+100*dh/d)
    assert residual_phase < arb(".00624")
    calibrated = margin/(arb(".024")+arb("17.51")*arb(".00624"))
    assert calibrated > arb(".000333")
    assert margin-arb(".015")*arb(".0001") > arb("4.297e-5")
    print(json.dumps(dict(kind="rotated_actual_first_hit_quadratic", precision_bits=ctx.prec,
                          scaled_source_modulus=(weight*M**2).str(12),
                          scaled_source_phase_pure=source_pure.str(12),
                          scaled_source_phase_mixed=source_mixed.str(12),
                          energy_rms_factor=M.str(12), signed_mixed_error=diagonal.str(12),
                          pure_residual_coefficient=pure.str(12),
                          imaginary_residual_coefficient=cross.str(12),
                          residual_imaginary_over_prefix_cap=residual_phase.str(12),
                          sqrt_n_actual_r2_lower=(margin/(weight*178*M**2)).str(12),
                          sqrt_n_prefix_cap_squared_lower=calibrated.str(12)), sort_keys=True))


if __name__ == "__main__":
    main()
