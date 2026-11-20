"""Replay a floating-point sweep of the round-117 stationary-weighted excess."""

import argparse
import json
from math import isfinite, sqrt
from pathlib import Path
import sys

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from poisson_weights import weighted_iterate
from smoothing import kernel_action
from theta import paley_sign


def capped_point(sign, roots, cap, initial, tolerance):
    """Solve the capped equation in physical units, including at the mark."""
    u = initial
    q = cap / np.hypot(cap, roots[1])
    for step in range(20001):
        a = np.hypot(np.clip(u, -cap, cap), roots)
        update = kernel_action(sign, a)
        residual = np.linalg.norm(update - u)
        # The counting L2 residual divided by 1-q also controls max error.
        error = residual / (1 - q)
        clear_of_cap = error <= 0.01 and np.abs(u).max() + error < cap
        if clear_of_cap or error <= tolerance:
            return u, a, error, step
        u = update
    raise RuntimeError(f"cap {cap} failed to converge, max error estimate {error:g}")


def measure(sign, t, cap, y, b, stationary_residual):
    n = len(sign)
    roots = np.full(n, 2 * sqrt(t))
    roots[0] = 2 * sqrt(n)
    u, a, error, steps = capped_point(sign, roots, cap, y, tolerance=1e-5)
    nu = 2 * sqrt(1 + t - t / n)
    mu = a.mean()
    deficit = np.maximum(u * u - cap * cap, 0).mean()
    if abs(nu**2 - mu**2 - deficit) > 1e-8:
        raise ArithmeticError("capped mean identity failed")

    larger = (b + np.abs(y)) / 2
    smaller = (roots / 2)**2 / larger
    for side in (1, -1):
        factor = np.where(side * y >= 0, larger, smaller)
        z = a - side * u
        spill = np.maximum(-z, 0)
        flow = side * kernel_action(sign, spill)
        v = np.maximum(z, 0) - flow
        excess = np.maximum(-v, 0)
        d = z[0] / sqrt(n)
        ell = max(flow[0], 0) / sqrt(n)
        weight = (factor * excess).mean()
        transport = (factor * np.maximum(flow, 0)).mean()
        identity_error = abs((factor * v).mean() - (mu + spill.mean()) * nu / 2)
        if abs(factor.mean() - nu / 2) > 1e-8 or identity_error > 1e-8:
            raise ArithmeticError("stationary mean or opposite-sector identity failed")
        if z[0] <= 0 or d <= ell:
            raise ArithmeticError("round 117 requires a positive marked denominator")
        mark = factor[0] / sqrt(n)
        mean_completed = mu + spill.mean()
        direct_bound = (nu * mean_completed / 2 + weight) / (d - ell)
        if mark > direct_bound + 1e-8:
            raise ArithmeticError("weighted marked bound failed")
        bound = None
        if mean_completed <= nu * (1 - ell / 2) + 1e-9:
            bound = nu**2 / 4 + (weight + (nu**2 / 4) * (2 - d)) / (d - ell)
            if mark > bound + 1e-8:
                raise ArithmeticError("round-117 inequality (2) failed")
        if cap == 10 and bound is None:
            raise ArithmeticError("round-117 cap budget failed")

        yield dict(
            p=2 * n + 1, n=n, t=t, cap=cap, sign=side,
            weighted_excess=weight, normalized_excess=weight / (d - ell),
            weighted_positive_transport=transport, max_excess=excess.max(),
            excess_sites=int(np.count_nonzero(excess)),
            spill_sites=int(np.count_nonzero(spill)), mean_spill=spill.mean(),
            signed_bulk_peak=(side * u[1:]).max(), min_bulk_slack=z[1:].min(),
            max_abs_u=np.abs(u).max(), cap_deficit=deficit,
            d=d, ell=ell, stationary_mark=mark, eq2_bound=bound,
            stationary_residual=stationary_residual, capped_error_estimate=error,
            capped_steps=steps, orthogonality_error=identity_error,
        )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("primes", type=int, nargs="+")
    parser.add_argument("--floors", type=float, nargs="+", default=[0.05, 0.01, 0.002, 0.0005])
    parser.add_argument("--caps", type=float, nargs="+", default=[10.0])
    args = parser.parse_args()
    if any(not isfinite(t) or not 0 < t <= 1 for t in args.floors):
        parser.error("floors must lie in (0, 1]")
    if any(not isfinite(cap) or cap < 2 for cap in args.caps):
        parser.error("caps must be finite and at least two")

    stationary_tolerance = 2e-11
    for p in sorted(set(args.primes)):
        sign = paley_sign(p)
        n = len(sign)
        initial = None
        for t in sorted(set(args.floors), reverse=True):
            weights = np.full(n, t / n)
            weights[0] = 1
            initial, total, residual = weighted_iterate(
                sign, weights, stationary_tolerance, initial=initial
            )
            if residual > stationary_tolerance:
                raise RuntimeError(f"stationary solver did not converge at p={p}, t={t}: {residual:g}")
            for cap in sorted(set(args.caps), reverse=True):
                for row in measure(sign, t, cap, sqrt(n) * initial, sqrt(n) * total, residual):
                    print(json.dumps(row, allow_nan=False), flush=True)


if __name__ == "__main__":
    main()
