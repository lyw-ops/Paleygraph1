"""Interval checks for a clipped exterior row used as the Jacobi source."""
import json
import runpy
from pathlib import Path

from flint import arb, ctx

prior = runpy.run_path(str(Path(__file__).with_name("endpoint-direction-45-check.py")))
ctx.prec = 384


def units(value):
    scaled = value * 10**9
    return [int(scaled.lower().floor().unique_fmpz()),
            int(scaled.upper().ceil().unique_fmpz())]


def indices_above(values, threshold):
    assert all(v > threshold or v < threshold for v in values)
    return {i for i, v in enumerate(values) if v > threshold}


def audit(p, time):
    signs = prior["paley_sign"](p)
    pair, error = prior["solve_prime_pair"](signs)
    assert error is None
    side = 1 if pair[1][0] > pair[-1][0] else -1
    assert pair[side][0] > pair[-side][0]
    signs = list(map(int, signs))
    n = len(signs)
    root, root_p = arb(n).sqrt(), arb(p).sqrt()
    q = [a/root for a in pair[side]]
    apply = prior["apply_multiplier"]
    x = [arb(0)] + [(v - arb(1)/n).max(0) for v in q[1:]]
    z = [v-a for v, a in zip(q,x)]
    mass = sum(x)
    effective = mass**2/sum(a*a for a in x)
    source = [side*n*a/(root_p*mass) for a in apply(x,signs)]
    remainder = [side*n*a+1 for a in apply(z,signs)]
    assert all((n*v-root_p*mass*w-e).contains(0)
               for v,w,e in zip(q,source,remainder))
    energy = sum(w*w for w in source)/n
    assert (energy-arb(n)/p*(1/effective-arb(1)/n)).contains(0)
    err_collision = sum(v*v for v in remainder)/n
    assert (err_collision-(1+n*sum(v*v for v in z)-sum(z)**2)).contains(0)

    state = [arb(0)]*n
    raw = [arb(0)]*n
    for t in range(time+1):
        phi = [(4+state[0]**2).sqrt()]+list(map(abs,state[1:]))
        if t:
            w = arb(1 if t == time else 2)/(2*time-1)
            raw = [a+w*root*(h-side*y)/2 for a,h,y in zip(raw,phi,state)]
        if t < time:
            state = apply(phi,signs)
    spectrum = [int(v in (0,-side)) for v in signs]
    primary = apply(raw,spectrum)
    origin = [arb(1)]+[arb(0)]*(n-1)
    col = apply(origin,[int(v == -side) for v in signs])
    inc = (primary[0]/root-sum(raw)/n).max(0)
    pinned = [v+inc*(1-a/col[0]) for v,a in zip(primary,col)]
    terminal = apply([root*(h+side*y)/2 for h,y in zip(phi,state)],
                     [int(v in (0,side)) for v in signs])
    deficit = [arb(0)]+[(-v).max(0) for v in pinned[1:]]
    pay = indices_above(deficit,arb(1)/100)
    assert all(terminal[i]>(2*time-1)*arb(1)/100 for i in pay)
    alpha = arb(1)/4
    high = indices_above([root*v/mass for v in q],alpha)-{0}
    heads = indices_above(source,alpha*root/(2*root_p))-{0}
    high_cost = high & pay
    kept = high_cost & heads
    bad = high_cost-heads
    assert all(remainder[i]>n*q[i]/2 for i in bad)
    assert sum((n*q[i]**2 for i in bad),arb(0)) < 4*err_collision
    def price(ids, field):
        return sum((q[i]*field[i] for i in ids),arb(0))
    return dict(p=p,terminal_time=time,side=side,B=1,alpha="1/4",
                exterior_mass=units(mass),source_effective_size=units(effective),
                reverse_bias_mean_square=units(energy),remainder_energy=units(err_collision),
                deficit_sites=len(pay),high_paying_sites=len(high_cost),
                reverse_head_sites=len(heads),retained_high_paying_sites=len(kept),
                high_deficit=units(price(high_cost,deficit)),
                retained_high_deficit=units(price(kept,deficit)),
                retained_high_height=units(price(kept,terminal)),
                low_deficit=units(price(pay-high,deficit)),units="1e-9",bits=ctx.prec)


if __name__ == "__main__":
    for field, time in ((101,4),(257,5),(409,6),(769,7)):
        print(json.dumps(audit(field,time),sort_keys=True),flush=True)
