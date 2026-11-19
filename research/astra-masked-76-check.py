"""Enclose clipped-tail tests on four certified prime endpoints and cold windows."""
import json
import runpy
from fractions import Fraction
from pathlib import Path

from flint import acb, arb, arb_mat, ctx

source = runpy.run_path(str(Path(__file__).with_name("endpoint-direction-45-check.py")))
ctx.prec = 768


def rational(value):
    return arb(value.numerator) / value.denominator


def interval(value):
    scale = 10**7
    return [int((value * scale).lower().floor().unique_fmpz()),
            int((value * scale).upper().ceil().unique_fmpz())]


def positive(value):
    return value.max(0)


def optimal_cost(q, sites, root_p):
    n = len(q)
    lo, hi = Fraction(0), Fraction(n)
    for _ in range(46):
        middle = (lo + hi) / 2
        cutoff = rational(middle)
        active = [q[i] - cutoff / n for i in sites if q[i] > cutoff / n]
        assert all(q[i] > cutoff / n or q[i] < cutoff / n for i in sites)
        derivative = 1 - 2 * root_p * sum(active) * len(active) / n
        assert derivative > 0 or derivative < 0
        if derivative > 0:
            hi = middle
        else:
            lo = middle

    # The first summand increases and the clipped mass decreases on the bracket.
    right = rational(hi)
    mass = sum(positive(q[i] - right / n) for i in sites)
    lower = rational(lo) + root_p * mass**2
    upper = right + root_p * mass**2
    return interval(lower.union(upper))


def check(p, start, exception):
    sign_array = source["paley_sign"](p)
    mask = list(map(int, sign_array))
    n = len(mask)
    pair, error = source["solve_prime_pair"](sign_array)
    assert error is None
    side = 1 if pair[1][0] > pair[-1][0] else -1
    assert pair[side][0] > 1
    q = [v / arb(n).sqrt() for v in pair[side]]
    assert all(q[0] > v for v in q[1:])
    exterior = sorted(set(range(n)) - set(exception))
    assert min(q[i] for i in exception) > max(q[i] for i in exterior)

    def kernel(v):
        transform = acb.dft(v)
        return [a.real for a in acb.dft([s * z for s, z in zip(mask, transform)], inverse=True)]

    s = -side
    root = [arb(i == 0) for i in range(n)]
    kcol = kernel(root)
    denom = 1 - arb(1) / n + s * kcol[0]
    pin = [1 - (a - arb(1) / n + s * b) / denom for a, b in zip(root, kcol)]
    d = 5
    weights = [((j + 1) * (d - j))**2 for j in range(d)]
    proposal = [arb(0)] * n
    state = [arb(0)] * n
    for j in range(start + d):
        phi = [(4 + state[0]**2).sqrt()] + [abs(a) for a in state[1:]]
        if j >= start:
            raw = [arb(n).sqrt() * (a + s * b) / 2 for a, b in zip(phi, state)]
            mean = sum(raw) / n
            z = [(a + mean + s * b) / 2 for a, b in zip(raw, kernel(raw))]
            shift = (1 + arb(1) / 1000) * z[0] / arb(n).sqrt() - mean
            proposal = [r + weights[j-start] * (v + shift * h) / sum(weights)
                        for r, v, h in zip(proposal, z, pin)]
        state = kernel(phi)
    assert all(v > -arb(1)/40 or v < -arb(1)/40 for v in proposal)
    sites = [i for i in range(1, n) if proposal[i] < -arb(1)/40]
    signed_tail = sum(q[i] * (-proposal[i]) for i in sites)
    x = [positive(v - arb(1)/n) for v in q]
    z = [v - u for v, u in zip(q, x)]
    full_hinge = n * sum(x[i]**2 for i in sites)
    masked = [i for i in sites if i in exterior and x[i] > 0]
    exterior_hinge = n * sum(x[i]**2 for i in masked)

    # The Schur complement projects onto forbidden rows zero on the exceptions.
    col = [z.real for z in acb.dft([int(t == -side) for t in mask], inverse=True)]
    principal = arb_mat([[col[(i-j) % n] for j in exception] for i in exception])
    cross = arb_mat([[col[(i-j) % n] for j in exterior] for i in exception])
    coefficients = principal.solve(cross)
    diag = signed = unsigned = residual = arb(0)
    for i in masked:
        h = arb_mat([[col[(i-j) % n] for j in exception]]) * coefficients
        for pos, j in enumerate(exterior):
            entry = col[(i-j) % n] - h[0, pos]
            factor = n * x[i] * entry
            residual += factor * z[j]
            if i == j:
                diag += factor * x[i]
            else:
                signed -= factor * x[j]
                unsigned += positive(-entry) * n * x[i] * x[j]
    assert (diag + residual - signed).contains(0)
    assert 0 < signed < unsigned
    root_p = arb(p).sqrt()
    return dict(p=p, side=side, mark=interval(pair[side][0]), start=start,
                exceptions=exception, mask_sites=len(sites), exterior_hinge_sites=len(masked),
                signed_tail=interval(signed_tail), hinge=interval(full_hinge),
                exterior_hinge=interval(exterior_hinge), schur_diagonal=interval(diag),
                signed_offdiagonal_price=interval(signed), unsigned_offdiagonal_price=interval(unsigned),
                optimal_trimmed_cost=optimal_cost(q, exterior, root_p),
                optimal_untrimmed_cost=optimal_cost(q, list(range(n)), root_p),
                precision=ctx.prec, units="1e-7")


for args in [(101, 24, [0, 10, 40]), (257, 10, [0, 33, 95]),
             (409, 20, [0, 9, 33, 171, 195]), (769, 2, [0, 89, 147, 168, 216, 237, 295])]:
    print(json.dumps(check(*args), sort_keys=True), flush=True)
