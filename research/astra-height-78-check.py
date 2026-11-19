"""Enclose infinite one-sided geometric windows on genuine complementary endpoints."""
import json
import runpy
from pathlib import Path

from flint import arb, ctx

prior = runpy.run_path(str(Path(__file__).with_name("endpoint-direction-45-check.py")))
ctx.prec = 512


def interval(value):
    scaled = value * 10**7
    return [int(scaled.lower().floor().unique_fmpz()), int(scaled.upper().ceil().unique_fmpz())]


def measure(p, start, d, allowance_milli):
    arithmetic_sign = prior["paley_sign"](p)
    signs = list(map(int, arithmetic_sign))
    n = len(signs)
    root = arb(n).sqrt()
    pair, error = prior["solve_prime_pair"](arithmetic_sign)
    assert error is None
    side = 1 if pair[1][0] > pair[-1][0] else -1
    assert pair[side][0] > pair[-side][0]
    q = [v/root for v in pair[side]]
    geom = arb(d)/(d+1)
    theta = (1-geom)/(1+geom)
    kept = 140
    eps = arb(allowance_milli)/1000
    state = [arb(0)]*n
    radius = accumulated = arb(0)
    raw = {s: [arb(0)]*n for s in (-1, 1)}
    apply = prior["apply_multiplier"]
    for j in range(start+kept):
        phi = [(4+state[0]**2).sqrt()] + list(map(abs, state[1:]))
        if j == start-1:
            gprev = sum(phi)/(2*root) + arb(0, (radius/2).upper())
        if j >= start:
            w = (1-geom)*geom**(j-start)
            for s in (-1, 1):
                raw[s] = [a+w*root*(f+s*v)/2 for a, f, v in zip(raw[s], phi, state)]
            accumulated += w*root*radius
        updated = apply(phi, signs)
        radius = (radius+sum(v.rad()**2 for v in updated).sqrt()).upper()
        state = [v.mid() for v in updated]
    # On each true time, the counting norm of either positive raw row is <=2 sqrt(n(j+1)).
    tail = 2*root*geom**kept*arb(start+kept+d+1).sqrt()
    remainder = (accumulated+tail).upper()
    row, constants = {}, {}
    for s in (-1, 1):
        projection = [int(v == 0 or v == s) for v in signs]
        projected = [v+arb(0, remainder) for v in apply(raw[s], projection)]
        mean = sum(raw[s])/n+arb(0, (remainder/root).upper())
        mass = projected[0]/root
        col = apply([arb(int(i == 0)) for i in range(n)], [int(v == s) for v in signs])
        pin = [1-v/col[0] for v in col]
        shift = (1+eps)*mass-mean
        row[s] = [v+shift*b for v, b in zip(projected, pin)]
        const = (1-geom)*(mean-gprev)/2
        constants[s] = min((const+shift*b).lower() for b in pin[1:])
        if s == -side:
            assert (sum(q[i]*row[s][i] for i in range(1, n))
                    -mass*(1+eps-pair[side][0])).contains(0)
    s = -side
    u = arb(1)/40
    assert all(v > -u or v < -u for v in row[s][1:])
    mask = [i for i in range(1,n) if row[s][i] < -u]
    selected = [i for i in mask if n*q[i] > 1]
    assert all(n*q[i] > 1 or n*q[i] < 1 for i in mask)
    assert min(constants.values()) > 0 and selected
    assert all(row[-s][i] > u/theta for i in mask)
    ratio = max((-row[s][i]/row[-s][i]).upper() for i in mask)
    return dict(p=p, side=side, start=start, d=d, allowance_milli=allowance_milli, kept=kept, precision=ctx.prec,
                endpoint=interval(pair[side][0]), coordinate_error=interval(remainder),
                paired_constant_lower=interval(min(constants.values())),
                mask_count=len(mask), joint_count=len(selected), theta=interval(theta),
                max_mask_ratio_upper=interval(ratio),
                min_mask_height=interval(min(row[-s][i] for i in mask)),
                joint_defect_price=interval(sum(q[i]*(-row[s][i]) for i in selected)),
                joint_height_price=interval(sum(q[i]*row[-s][i] for i in selected)),
                units="1e-7")


if __name__ == "__main__":
    for case in [(101, 1, 4, 20), (257, 2, 4, 50), (409, 3, 4, 40), (769, 11, 4, 10)]:
        print(json.dumps(measure(*case), sort_keys=True), flush=True)
