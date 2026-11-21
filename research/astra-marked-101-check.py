"""Held-initial marked sensitivities and their adjacent defects on the physical square."""
import json
from pathlib import Path
import runpy

from flint import acb, arb, arb_poly, ctx


def main():
    base = Path(__file__).resolve().parent
    old = runpy.run_path(str(base / "astra-predictor-76-check.py"))
    pricing = runpy.run_path(str(base / "newton-contour-98-check.py"))
    ctx.prec = 192
    fields, tilt, eps, symmetric = (old[k] for k in ("fields", "tilt", "eps", "symmetric"))
    size, cut = old["N"], old["KEEP"]
    a, h = arb(2031)/128, arb(2)**-17
    low = a-h
    box = acb(arb(a, h), arb(0, h))
    rows, amps = fields["upper"](box)
    rows = [[v.upper() for v in row] for row in rows]
    assert all(v >= 0 for row in rows for v in row)
    folds = [symmetric(row, cut) for row in rows]
    norms = [sum(v*w for v, w in zip(row, tilt)) for row in rows]
    A, B, C, D, Z, W, V = amps
    seed = fields["kern"]["dim"]
    center_mass = seed+2*A+3*B+4*C+arb(23)*D/4+8*(Z+W+V)

    def tilt_mass(poly, radius):
        return sum(poly[radius+k]*(2 if k else 1)*tilt[k] for k in range(radius+1))

    center_tilt = (seed*tilt[1]+A*(1+tilt[2])+B*(1+3*tilt[1]/2+3*tilt[3]/2)
                   +C*tilt_mass(fields["kern"]["F"], 4)+D*tilt_mass(fields["kern"]["G"], 5)
                   +Z*tilt_mass(fields["old"]["R"], 2)+(W+V)*tilt_mass(fields["field"], 4))
    prices = [arb(i)/10**8 for i in pricing["SCALED_PRICES"]]
    slope = prices[-1]-prices[-2]

    def price(k):
        k = abs(k)
        return prices[k] if k < len(prices) else prices[-1]+(k+1-len(prices))*slope

    # Fixed weights for each input packet's price test.
    weights = [[(price(k+j)+price(k-j))/2 for j in range(size+1)]
               for k in range(1, size+len(prices)+1)]
    bn = arb(1)
    for j in range(1, 16):
        bn *= (arb(3)/2-j)/j
    tail = 2*abs(box).sqrt()*abs(bn)
    nmin = arb(10)**30
    seed_sup = (8+4/nmin).sqrt()
    assert seed_sup < seed.upper() and seed_sup < arb("2.828428")
    source = (2+1/nmin).sqrt()/(low**arb("1.5")*(1-arb("4.8")**2/(4*nmin)).sqrt())
    assert source < arb(".02238")
    # Full physical curvature on the original seed disk and the 0.01 enlargement.
    assert 4*(a+2*h)/(4*low-arb("1.94")**2)**arb("1.5") < arb(".138")
    assert 4*(a+2*h)/(4*low-arb("1.95")**2)**arb("1.5") < arb(".139")
    # |f'(v)|, times sqrt(n), on the slightly enlarged marked segment.
    assert 2*arb("4.8")/(low**arb("1.5")*(4-arb("4.8")**2/nmin)**arb("1.5")) < arb(".02")
    mark_leak = arb(".02")/nmin.sqrt()
    assert 1/(low**arb("1.5")*(1-arb("4.8")**2/(4*nmin)).sqrt()) < arb(".016")
    s = arb("2.828428")
    outer = arb("1.95")
    assert 2*s*(4*low-2*outer**2) > 4*outer*(s+outer)**2
    outer_rate = (s+outer)/(4*low+(s+outer)**2).sqrt()
    inverse = 1/(1-outer_rate)
    assert inverse < arb("2.07")
    nmax = arb("1.7e304")
    root_loss = arb(".169724")
    # Increment of J at zero is exactly one marked column.
    relative = arb(".016")/root_loss
    packets = [arb(0)]*size
    direction = [arb(0)]*size
    error = arb(0)
    prev_cap = arb(0)
    for height in range(518):
        zero = sum(k*x for k, x in enumerate(packets))+arb(14)/5*eps+arb("1e-8")
        core = symmetric([zero]+packets, size)
        norm = zero+sum(x*w for x, w in zip(packets, tilt[1:]))+eps
        total_tilt = center_tilt+norm
        ratio = total_tilt**2/(4*low)
        mass = center_mass+sum(k*x for k, x in enumerate(packets, 1))+4*eps
        assert mass < arb("4.768") and ratio < 1
        # Every ordinate lies within the non-seed packet mass of the real seed.
        disk = (mass-seed.lower()).upper()
        assert disk > 0 and 2*s*(4*low-2*disk**2) > 4*disk*(s+disk)**2
        rate_two = (s+disk)/(4*low+(s+disk)**2).sqrt()
        assert rate_two > arb(".4")
        if height:
            root_loss *= rate_two
            relative += (arb(".138")*prev_cap+mark_leak)/rate_two
        cap = error+sum(k*x for k,x in enumerate(direction, 1))
        if height == 517:
            counting = nmax.sqrt()*root_loss
            displacement = inverse*counting
            assert displacement < arb(".01")
            derivative_error = inverse*(relative*counting
                + (arb(".139")*cap+mark_leak)*displacement)
            stationary = cap+derivative_error
            threshold = 2*arb("1e-4")/arb(3).sqrt()
            assert h*stationary < threshold
            print(json.dumps(dict(
                height=height, precision_bits=ctx.prec, n_max="1.7e304",
                held_sensitivity=cap.str(14), normalized_residual=root_loss.str(14),
                adjacent_defect_over_residual_envelope=relative.str(14),
                counting_displacement=displacement.str(14),
                stationary_derivative_error=derivative_error.str(14),
                rotated_stationary_imaginary=(h*stationary).str(14),
                hitting_threshold=threshold.str(14)), sort_keys=True))
            break
        prev_cap = cap
        power = arb_poly([0]*cut+[1])
        kept, der = arb_poly(), arb_poly()
        for j, kernel in enumerate(folds):
            if j:
                part = kernel*power
                der += arb_poly([j*part[k+2*cut] for k in range(size+1)])
                next_power = power*core
                power = arb_poly([next_power[k+size] for k in range(2*cut+1)])
            part = kernel*power
            kept += arb_poly([part[k+2*cut] for k in range(size+1)])
        inside = kept[0]+2*sum(kept[k]*tilt[k] for k in range(1, size+1))
        assert sum(v*norm**j for j, v in enumerate(norms))-inside+tail*ratio**15/(1-ratio) < eps
        mu = [der[k]*(2 if k else 1) for k in range(size+1)]
        missing = (sum(j*v*norm**(j-1) for j, v in enumerate(norms) if j)
                   -sum(v*w for v, w in zip(mu, tilt))
                   +2*tail*ratio**15/total_tilt*(15/(1-ratio)+ratio/(1-ratio)**2))
        assert missing >= 0
        moment = sum(price(j)*v for j, v in enumerate(mu))
        charges = [((k-1)*moment+sum(v*w for v, w in zip(mu, row)))/price(k)
                   for k, row in enumerate(weights, 1)]
        rate = max(v.upper() for v in charges+[sum(mu)+moment/slope])+10*missing+arb("1e-12")
        # Propagate the single marked column before taking a scalar price.
        vz = sum(k*x for k,x in enumerate(direction))
        motion = symmetric([vz]+direction, size)
        moved = motion*symmetric(mu, size)
        new_direction = [2*moved[2*size+k] for k in range(1, size+1)]
        escaped = sum(2*moved[2*size+k]*price(k) for k in range(size+1, 2*size+1))
        old_price = sum(price(k)*x for k,x in enumerate(direction, 1))
        error = rate*error + escaped + (10*missing+arb("1e-12"))*old_price
        new_direction[0] += source
        direction = new_direction
        nxt = [(2*kept[k]).upper() for k in range(1, size+1)]
        nxt[0] += arb("1e-12")
        assert all(y >= x for x, y in zip(packets, nxt))
        packets = nxt


if __name__ == "__main__":
    main()
