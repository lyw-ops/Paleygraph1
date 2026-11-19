"""Check compact time coefficients exactly and enclose true finite endpoint profiles."""
import json
import runpy
from pathlib import Path

from flint import arb, ctx

prior = runpy.run_path(str(Path(__file__).with_name("endpoint-direction-45-check.py")))
ctx.prec = 384


def check_coefficients(d):
    # Both omega and theta * nu use denominator d**2.
    tri = [0] + [2 * (d - j) + 1 for j in range(1, d + 1)] + [0, 0, 0]
    companion = [0] + [1] * d + [0, 0, 0]
    for j in range(d + 2):
        def four_a(v):
            return 2 * v[j] + v[j - 1] + v[j + 1]

        def four_b(v):
            return v[j - 1] - v[j + 1]

        negative = four_a(companion) - four_b(tri)
        positive = four_a(tri) - four_b(companion)
        assert negative == (2 * d if j in (0, 1) else 0)
        assert positive >= 0
    assert sum(tri) == d**2 and sum(companion) == d


def interval(value):
    scaled = value * 10**8
    return [int(scaled.lower().floor().unique_fmpz()),
            int(scaled.upper().ceil().unique_fmpz())]


def measure(p, d):
    signs = prior["paley_sign"](p)
    pair, err = prior["solve_prime_pair"](signs)
    assert err is None
    side = 1 if pair[1][0] > pair[-1][0] else -1
    assert pair[side][0] > pair[-side][0]
    n = len(signs)
    root = arb(n).sqrt()
    q = [entry / root for entry in pair[side]]
    apply = prior["apply_multiplier"]
    signs = list(map(int, signs))
    raw = {s: [arb(0)] * n for s in (-1, 1)}
    state = [arb(0)] * n
    weights = {
        -side: [arb(2 * (d - j) + 1) / d**2 for j in range(1, d + 1)],
        side: [arb(1) / d] * d,
    }
    for j in range(d + 1):
        phi = [(4 + state[0]**2).sqrt()] + list(map(abs, state[1:]))
        if j:
            for s in (side, -side):
                factor = weights[s][j - 1] * root / 2
                raw[s] = [a + factor * (f + s * v) for a, f, v in zip(raw[s], phi, state)]
        if j < d:
            state = apply(phi, signs)
    rows = {}
    # Give each finite row the smallest nonnegative pin from zero allowance.
    for s in (side, -side):
        proj = apply(raw[s], [int(v == 0 or v == s) for v in signs])
        mean = sum(raw[s]) / n
        m = proj[0] / root
        shift = (m - mean).max(arb(0))
        col = apply([arb(int(i == 0)) for i in range(n)], [int(v == s) for v in signs])
        rows[s] = [v + shift * (1 - a / col[0]) for v, a in zip(proj, col)]
        if s == -side:
            assert (sum(q[i] * rows[s][i] for i in range(1, n))
                    - (mean + shift - m * pair[side][0])).contains(0)
    primary = rows[-side]
    companion = rows[side]
    lower = min((primary[i] + companion[i] / d).lower() for i in range(1, n))
    assert lower > 0
    u = arb(1) / 100
    assert all(v < -u or v > -u for v in primary[1:])
    mask = [i for i in range(1, n) if primary[i] < -u]
    assert all(companion[i] > d * u for i in mask)
    return dict(p=p, d=d, side=side, mark=interval(pair[side][0]),
                min_paired_bulk=interval(lower), mask_count=len(mask),
                height_min=interval(min(companion[i].lower() for i in mask)) if mask else None,
                mask_deficit_price=interval(sum((q[i] * (-primary[i]) for i in mask), arb(0))),
                mask_height_price=interval(sum((q[i] * companion[i] for i in mask), arb(0))),
                units="1e-8", precision=ctx.prec)


if __name__ == "__main__":
    for d in range(1, 513):
        check_coefficients(d)
    for p, d in ((101, 4), (257, 5), (409, 6), (769, 7)):
        print(json.dumps(measure(p, d), sort_keys=True), flush=True)
