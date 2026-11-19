"""Verify two feasible Fourier trials for a real cold marked bound."""

import argparse
import json
from pathlib import Path
import runpy

import numpy as np
from flint import arb, ctx
from scipy.optimize import minimize


SUPPORT = runpy.run_path(str(Path(__file__).with_name("astra-strip-45-check.py")))
GRID = 2**42
CASES = [(97, 1, 28), (97, -1, 28), (173, 1, 28), (173, -1, 1)]
UPPER_CASE = (173, -1, 28)


def propose(sign, sigma, warm, reps, pairs, sizes, n, target):
    plus, minus = SUPPORT["approx"](sign, float(warm), 0.0, 0, 80)
    rows = {1: plus[0], -1: minus[0] / np.mean(minus[0])}

    def coefficients(side):
        inverse = np.fft.irfft(rows[side][:n // 2 + 1], n)
        return sizes[pairs[side]] * inverse[pairs[side]]

    same = np.cos(2 * np.pi * reps[:, None] * pairs[sigma] / n)
    opposite = np.cos(2 * np.pi * reps[:, None] * pairs[-sigma] / n)
    reference = coefficients(-sigma)
    reference_row = 1 + opposite @ reference
    reference_mark = reference_row[0] / np.sqrt(n)
    weight = sizes[1:] * np.sqrt(reference_row[1:]) / n
    objective_scale = 0.5 / (1 - target * reference_mark)
    floor_mass = 1 + (n - 1) / (2 * n)

    def value_and_gradient(coefs):
        root = np.sqrt(np.maximum(1 + same[1:] @ coefs, 1e-9))
        overlap = weight @ root
        linear = 1 / (target * np.sqrt(n))
        return (
            -(1 + same[0] @ coefs) * linear - objective_scale * overlap**2,
            -same[0] * linear - objective_scale * overlap * ((weight / root) @ same[1:]),
        )

    branch = floor_mass * reference_mark * target**2 * np.sqrt(n)
    constraints = [
        dict(type="ineq", fun=lambda c: 1 + same @ c - 1e-8, jac=lambda c: same),
        dict(type="ineq", fun=lambda c: 1 + same[0] @ c - branch, jac=lambda c: same[0]),
    ]
    candidate = minimize(
        value_and_gradient, coefficients(sigma), jac=True, method="SLSQP",
        constraints=constraints, options=dict(ftol=1e-11, maxiter=180),
    ).x
    return [[int(round(x * GRID)) for x in coefs] for coefs in (candidate, reference)]


def verify(prime, sigma, warm, saved=None, upper=False):
    sign = SUPPORT["paley_sign"](prime)
    n = len(sign)
    reps = np.arange(n // 2 + 1)
    sizes = np.full(len(reps), 2, dtype=int)
    sizes[[0, -1]] = 1
    assert sizes.sum() == n
    pairs = {side: reps[sign[reps] == side] for side in (1, -1)}
    floor_mass = 1 + arb(n - 1) / (2 * n)
    target = (-arb(17) / 1000).exp() / floor_mass.sqrt()
    if saved is None:
        coefs = propose(sign, sigma, warm, reps, pairs, sizes, n, float(target))
    else:
        assert saved["grid"] == GRID
        coefs = saved["coefficients"]

    def build(side, coeffs):
        modes = [int(j) for j in pairs[side]]
        assert len(modes) == len(coeffs) and 0 not in modes
        return [
            1 + sum(arb(num) / GRID * (arb(2*i*j)/n).cos_pi()
                    for j, num in zip(modes, coeffs))
            for i in range(len(reps))
        ]

    test = build(sigma, coefs[0])
    ref = build(-sigma, coefs[1])
    assert all(y > 0 for y in test + ref)
    f = test[0] / arb(n).sqrt()
    g = ref[0] / arb(n).sqrt()
    h = sum(int(sizes[i]) * (test[i] * ref[i]).sqrt() for i in range(1, len(reps))) / n
    assert target * g < 1
    if upper:
        scale_grid = 2**24
        cost = 1 / (2 * (1 - target*g))
        if saved is None:
            basis = np.column_stack([
                np.ones(len(reps)), np.cos(2*np.pi*reps[:, None]*pairs[-sigma]/n),
            ])
            bulk = basis[1:]
            weights = float(cost) * sizes[1:] * np.array([float(v) for v in ref[1:]]) / n
            root = float(arb(n).sqrt() / target)
            constant = np.zeros(basis.shape[1])
            constant[0] = 1
            constraints = [
                dict(type="ineq", fun=lambda c: basis[0] @ c - root, jac=lambda c: basis[0]),
                dict(type="ineq", fun=lambda c: bulk @ c - 1e-5, jac=lambda c: bulk),
                dict(type="ineq", fun=lambda c: 1 - weights @ (1/np.maximum(bulk @ c, 1e-7)),
                     jac=lambda c: (weights/np.maximum(bulk @ c, 1e-7)**2) @ bulk),
            ]
            proposal = minimize(
                lambda c: c[0], (root+1)*constant, jac=lambda c: constant,
                constraints=constraints, method="SLSQP", options=dict(ftol=1e-11, maxiter=240),
            ).x
            dual_nums = [int(round(float(v) * GRID)) for v in proposal]
        else:
            assert saved["scale_grid"] == scale_grid
            dual_nums = saved["dual"]
        mean = arb(dual_nums[0]) / GRID
        dual = [v + mean - 1 for v in build(-sigma, dual_nums[1:])]
        assert all(v > 0 for v in dual)
        harmonic = cost * sum(int(sizes[i]) * ref[i] / dual[i] for i in range(1, len(reps))) / n
        root_ratio = arb(n).sqrt() / (target * dual[0])
        if saved is None:
            scale_num = int(round(scale_grid * float(max(harmonic.upper(), root_ratio.upper(), arb(1))))) + 2
        else:
            scale_num = saved["scale"]
        scale = arb(scale_num)/scale_grid
        assert scale > harmonic and scale > root_ratio
        gap = floor_mass - scale * mean
        assert gap > arb(3)/1000
        return dict(kind="fixed_reference_deficit", prime=prime, sign=sigma,
                    reference_floor=warm, floor="1/2", log_tolerance="17/1000",
                    deficit_lower=str(gap), grid=GRID, coefficients=coefs,
                    dual=dual_nums, scale=scale_num, scale_grid=scale_grid)
    branch_slack = f - floor_mass * g * target**2
    score_slack = f / target + h*h / (2 * (1 - target*g)) - floor_mass
    assert branch_slack > 0 and score_slack > 0
    return dict(kind="paired_cold_bound", prime=prime, sign=sigma, reference_floor=warm,
                floor="1/2", log_tolerance="17/1000", score_slack=str(score_slack),
                branch_slack=str(branch_slack), grid=GRID, coefficients=coefs)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--replay", type=Path, help="verify the saved rational inputs")
    opts = parser.parse_args()
    saved_rows = {}
    if opts.replay:
        for line in opts.replay.read_text().splitlines():
            row = json.loads(line)
            saved_rows[row["prime"], row["sign"], row["reference_floor"]] = row
    ctx.prec = 160
    for case in CASES:
        print(json.dumps(verify(*case, saved=saved_rows[case] if opts.replay else None),
                         sort_keys=True))
    print(json.dumps(verify(*UPPER_CASE, saved=saved_rows[UPPER_CASE] if opts.replay else None,
                            upper=True), sort_keys=True))
