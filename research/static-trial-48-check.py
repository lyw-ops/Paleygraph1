"""Enclose the measure budget and certify opposite-sector harmonic duals."""

import argparse
from fractions import Fraction
import json
from pathlib import Path
import runpy
import sys

import numpy as np
from flint import arb, ctx
from scipy.optimize import minimize

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from square_control import square_field_sign
from theta import paley_sign


def budget():
    degree = 128
    intervals = 16384
    d = arb(1) / 4096
    pole = 1 / (1 - d)
    factors = [arb(i) / (5 * (degree + 1)) for i in range(1, degree + 1)]
    r = arb(63) / 65
    chebyshev = (r**degree + (1 / r)**degree) / 2
    prefactor = (1 - d) / (chebyshev * arb.pi())
    step = arb.pi() / (2 * intervals)
    integral = arb(0)
    for j in range(intervals):
        angle = (j * step).union((j + 1) * step)
        sine = angle.sin()
        cosine = angle.cos()
        z = cosine**2
        ratio = arb(1)
        for factor in factors:
            ratio *= (1 - factor * pole) / (1 - factor * z)
        if j < intervals // 2:
            phase = (32 * sine / cosine).atan()
        else:
            phase = arb.pi() / 2 - (cosine / (32 * sine)).atan()
        value = (
            sine * cosine / (sine**2 + d * z) * abs((2 * degree * angle).cos())
            * ratio * phase
        )
        integral += step * value
    enclosure = prefactor * integral
    assert enclosure > arb("0.017") and enclosure < arb("0.0195")
    return dict(kind="chebyshev_measure_budget", terms=intervals, enclosure=str(enclosure))


def optimize_dual(basis, counts, n, target):
    linear = np.zeros(basis.shape[1])
    linear[0] = 1
    weights = counts[1:] / (2 * n)
    bulk = basis[1:]

    def harmonic(coefs):
        values = np.maximum(bulk @ coefs, 1e-6)
        return 1 - weights @ (1 / values)

    def harmonic_gradient(coefs):
        values = np.maximum(bulk @ coefs, 1e-6)
        return (weights / values**2) @ bulk

    constraints = [
        dict(type="ineq", fun=lambda x: basis[0] @ x - target, jac=lambda x: basis[0]),
        dict(type="ineq", fun=lambda x: bulk @ x - 1e-4, jac=lambda x: bulk),
        dict(type="ineq", fun=harmonic, jac=harmonic_gradient),
    ]
    return minimize(
        lambda x: x[0], linear * (target + 1), jac=lambda x: linear,
        constraints=constraints, method="SLSQP", options=dict(ftol=1e-11, maxiter=240),
    ).x


def verify_dual(order, signs, side, saved=None):
    n = len(signs)
    reps = np.arange(n // 2 + 1)
    sizes = np.full(len(reps), 2, dtype=int)
    sizes[[0, -1]] = 1
    assert sizes.sum() == n
    modes = [int(i) for i in reps if signs[i] == -side]
    w = 1 + arb(n - 1) / (2 * n)
    target = (n * w).sqrt() * (arb(39) / 2000).exp()
    denominator = 2**32
    scale_grid = 2**24
    if saved is None:
        basis = np.column_stack([
            np.ones(len(reps)), np.cos(2 * np.pi * reps[:, None] * modes / n),
        ])
        proposal = optimize_dual(basis, sizes, n, float(target))
        numerators = [int(round(x * denominator)) for x in proposal]
    else:
        assert (saved["order"], saved["side"]) == (order, side)
        assert saved["grid"] == denominator and saved["scale_grid"] == scale_grid
        numerators = saved["coefficients"]
    assert len(numerators) == len(modes) + 1
    coefs = [arb(x) / denominator for x in numerators]
    row = [coefs[0] + sum(c * (arb(2 * i * j) / n).cos_pi()
                         for c, j in zip(coefs[1:], modes)) for i in range(len(reps))]
    assert all(x > 0 for x in row)
    reciprocal = sum(int(sizes[i]) / row[i] for i in range(1, len(reps))) / (2 * n)
    if saved is None:
        correction = max(arb(1), (target / row[0]).upper(), reciprocal.upper())
        multiplier = int(round(float(correction) * scale_grid)) + 2
    else:
        multiplier = saved["multiplier"]
    scale = arb(multiplier) / scale_grid
    assert row[0] * scale > target and reciprocal / scale < 1
    upper = scale * coefs[0]
    assert upper < w
    return dict(kind="harmonic_dual_deficit", order=order, side=side, upper=str(upper),
                deficit_lower=str((w - upper).lower()), grid=denominator,
                coefficients=numerators, multiplier=multiplier, scale_grid=scale_grid)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--replay", type=Path, help="verify saved duals without a floating solve")
    args = parser.parse_args()
    saved_rows = {}
    if args.replay:
        for line in args.replay.read_text().splitlines():
            row = json.loads(line)
            if row["kind"] == "harmonic_dual_deficit":
                saved_rows[row["order"], row["side"]] = row
    ctx.prec = 160
    print(json.dumps(budget(), sort_keys=True))
    for q, sign, sigma in [
        (101, paley_sign(101), 1),
        (173, paley_sign(173), -1),
        (281, paley_sign(281), 1),
        (401, paley_sign(401), 1),
        (121, square_field_sign(11), -1),
    ]:
        saved = saved_rows[q, sigma] if args.replay else None
        print(json.dumps(verify_dual(q, sign, sigma, saved), sort_keys=True))

    from_chain = runpy.run_path(str(Path(__file__).with_name("astra-strip-45-check.py")))
    _, _, _, _, mark = from_chain["disks"](
        paley_sign(173), Fraction(1, 2), Fraction(1, 16), 10, 14,
    )
    assert abs(mark) < arb("0.017")
    print(json.dumps(dict(kind="cold_mark_below_budget_lower", order=173,
                          floor="1/2", enclosure=str(mark)), sort_keys=True))
