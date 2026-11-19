"""Interval replay for aggregated exterior Schur prices on actual terminal windows."""
import json
import runpy
import random
from math import prod
from pathlib import Path

from flint import acb, arb, ctx

base = Path(__file__).parent
prior = runpy.run_path(str(base / "endpoint-direction-45-check.py"))
schur = runpy.run_path(str(base / "astra-schur-77-check.py"))["schur_row"]
ctx.prec = 384


def interval(v):
    v *= 10**8
    return [int(v.lower().floor().unique_fmpz()), int(v.upper().ceil().unique_fmpz())]


def measure(p, b):
    signs = prior["paley_sign"](p)
    pair, err = prior["solve_prime_pair"](signs)
    assert err is None
    side = 1 if pair[1][0] > pair[-1][0] else -1
    assert pair[side][0] > pair[-side][0]
    signs = list(map(int, signs))
    n = len(signs)
    root, root_p = arb(n).sqrt(), arb(p).sqrt()
    q = [v / root for v in pair[side]]
    opposite = [v / root for v in pair[-side]]
    apply = prior["apply_multiplier"]
    state = [arb(0)] * n
    raw = [arb(0)] * n
    for t in range(b + 1):
        phi = [(4 + state[0]**2).sqrt()] + list(map(abs, state[1:]))
        if t:
            w = arb(1 if t == b else 2) / (2*b - 1)
            raw = [v + w*root*(h - side*y)/2 for v, h, y in zip(raw, phi, state)]
        if t == b:
            terminal = apply([root*(h + side*y)/2 for h, y in zip(phi, state)],
                             [int(v == 0 or v == side) for v in signs])
        else:
            state = apply(phi, signs)
    col = [v.real for v in acb.dft([int(t == -side) for t in signs], inverse=True)]
    primary = apply(raw, [int(v == 0 or v == -side) for v in signs])
    increment = (primary[0]/root - sum(raw)/n).max(0)
    primary = [v + increment*(1 - c/col[0]) for v, c in zip(primary, col)]
    u = arb(1)/100
    assert all(v < -u or v > -u for v in primary[1:])
    mask = [i for i in range(1, n) if primary[i] < -u and q[i] > 0]
    assert all(q[i].is_zero() or q[i] > 0 for i in range(n))
    assert mask and all(terminal[i] > (2*b-1)*u for i in mask)
    assert all(opposite[i].is_zero() for i in mask)
    mass = sum(q[i] for i in mask)
    coll = n * sum(q[i]**2 for i in mask)
    x = [(v-arb(1)/n).max(0) for v in q]
    z = [v - w for v, w in zip(q, x)]
    ext = list(range(1, n))
    ext_mass = sum(x[j] for j in ext)
    rho = coll/(root*mass*ext_mass)
    jacobi = [v.real*n/root_p for v in acb.dft(signs, inverse=True)]
    bias = [side*sum(q[i]*jacobi[(j-i) % n] for i in mask)/mass for j in range(n)]
    assert all(v < rho/8 or v > rho/8 for v in bias)
    heads = [j for j in ext if bias[j] > rho/8]
    exposed = [j for j in heads if x[j] > 0]
    assert all(opposite[j].is_zero() for j in exposed)
    rows = {i: schur(col, i, [0]) for i in mask}
    prices = [-n*x[j]*sum((q[i]*rows[i][j] for i in mask if i != j), arb(0))
              for j in ext]
    diag = n*sum(q[i]**2*rows[i][i] for i in mask)
    low = n*sum(q[i]*sum(rows[i][j]*z[j] for j in ext if i != j) for i in mask)
    assert (sum(prices) - diag - low).contains(0)
    assert (sum(v**2 for v in bias)/n - (arb(n)/p) *
            (coll/(n*mass**2)-arb(1)/n)).contains(0)
    jacobi_power = [(v/rho)**4 for v in bias]
    weighted_mean = sum(q[j]*jacobi_power[j] for j in range(n))
    counting_mean = sum(jacobi_power)/n
    power_ft = acb.dft(jacobi_power)
    q_ft = acb.dft(q)
    allowed_corr = sum((q_ft[t]*power_ft[t].conjugate()).real
                       for t in range(1,n) if signs[t] == side)/n
    assert (weighted_mean - counting_mean - allowed_corr).contains(0)
    rng = random.Random(p)
    import numpy as np
    centered_weights = np.array([float(qj.mid()) - 1/n for qj in q])
    midpoint_columns = {i: np.array([float(jacobi[(j-i) % n].mid()) for j in range(n)])
                        for i in mask}
    def scoring(indices):
        return float(centered_weights @ np.prod([midpoint_columns[i] for i in indices], axis=0))
    options = [tuple(sorted(rng.sample(mask, 4))) for _ in range(128)]
    frozen_tuple = max(options, key=scoring)
    monomial = [prod(jacobi[(j-i) % n] for i in frozen_tuple) for j in range(n)]
    tuple_mean = sum(monomial)/n
    tuple_ft = acb.dft(monomial)
    tuple_corr = sum((q_ft[t]*tuple_ft[t].conjugate()).real
                     for t in range(1,n) if signs[t] == side)/n
    assert (sum(q[j]*monomial[j] for j in range(n)) - tuple_mean - tuple_corr).contains(0)
    assert tuple_corr > 0
    inside = sum(prices[j-1] for j in heads)
    outside = sum(prices[j-1].max(0) for j in ext if j not in heads)
    return dict(p=p, b=b, tested_sign=side, S=len(mask), bias_heads=len(heads),
                positive_clipped_heads=len(exposed), collision=interval(coll), rho=interval(rho),
                head_fraction_of_exterior_mass=interval(sum(x[j] for j in heads)/ext_mass),
                total_signed_over_collision=interval(sum(prices)/coll),
                head_signed_over_collision=interval(inside/coll),
                outside_positive_over_collision=interval(outside/coll),
                terminal_height_price=interval(sum(q[i]*terminal[i] for i in mask)),
                quartic_counting_mean=interval(counting_mean), quartic_weighted_mean=interval(weighted_mean),
                quartic_allowed_correlation=interval(allowed_corr), distinct_test_sites=list(frozen_tuple),
                distinct_test_mean=interval(tuple_mean), distinct_test_correlation=interval(tuple_corr),
                scale="1e-8", precision=ctx.prec)


if __name__ == "__main__":
    for p, b in ((101, 4), (257, 5), (409, 6), (769, 7)):
        print(json.dumps(measure(p,b), sort_keys=True), flush=True)
