"""Rotated marked source, physical prefix products and first-hit caps on Q."""
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
    radius = arb(1)/125-h
    # Initial rotated derivative by Cauchy on the R98 square.
    initial_derivative = 2*arb("4.8")/((a-arb(1)/125).sqrt()*radius)
    root_loss = arb(".169724")
    flat = root_loss*arb(".51358")**100
    packets = [arb(0)]*size
    direction = [arb(0)]*size
    error = initial_derivative
    for height in range(601):
        zero = sum(k*x for k, x in enumerate(packets))+arb(14)/5*eps+arb("1e-8")
        core = symmetric([zero]+packets, size)
        norm = zero+sum(x*w for x, w in zip(packets, tilt[1:]))+eps
        total_tilt = center_tilt+norm
        ratio = total_tilt**2/(4*low)
        mass = center_mass+sum(k*x for k, x in enumerate(packets, 1))+4*eps
        assert mass < arb("4.768") and ratio < 1
        # Every ordinate lies within the non-seed packet mass of the real seed.
        disk = (mass-seed.lower()).upper()
        s = arb("2.828428")
        assert disk > 0 and 2*s*(4*low-2*disk**2) > 4*disk*(s+disk)**2
        rate_two = (s+disk)/(4*low+(s+disk)**2).sqrt()
        assert rate_two > arb(".4")
        if height:
            root_loss *= rate_two
        if height in (100, 510, 600):
            actual_dir = error+sum(k*x for k, x in enumerate(direction, 1))
            rec = dict(height=height, marked_column_derivative=actual_dir.str(12),
                       precision_bits=ctx.prec, normalized_increment=root_loss.str(12),
                       prefix_coordinate_cap=mass.str(12))
            if height == 100:
                eta = root_loss/flat
                multiplier_speed = (4*(a+2*h)*21+2*arb("4.768"))/(4*low-4)**arb("1.5")
                phase = h*(42/arb(".169724")+100*multiplier_speed/arb(".4"))
                factor = 206*(arb(".000055")+arb(".09834")*phase)+arb(".380")*arb(".04919")
                exterior = factor*(arb(".025")*eta)**2
                cutoff = (arb(".0000341")/factor).sqrt()/eta
                assert eta < arb(".012739") and phase < arb(".007472")
                assert exterior < arb("1.84e-8") and cutoff > arb("1.076")
                rec.update(ratio_to_round_99=eta.str(12), imaginary_over_new_bound=phase.str(12),
                           anisotropic_over_sqrt_n=exterior.str(12), calibrated_cutoff=cutoff.str(12))
            if height == 510:
                counting = root_loss*arb(10)**148
                rotated_upper = h*actual_dir+3*counting/low.sqrt()
                assert actual_dir < arb("14.835") and 3*counting < arb("8e-6")
                assert rotated_upper < arb(".00011518") < 2*arb(".0001")/arb(3).sqrt()
                rec.update(n_max="1e296", rotated_stationary_imaginary=rotated_upper.str(12))
            if height == 600:
                assert root_loss*arb(10)**179 < arb(1)/8
                rec.update(n_max_stationary="1e358")
            print(json.dumps(rec, sort_keys=True), flush=True)
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
