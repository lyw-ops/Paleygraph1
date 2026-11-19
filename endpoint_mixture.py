"""Combine projected reference trials and selected Fourier tests at the theta endpoint."""

import argparse
import csv
from fractions import Fraction
from math import isfinite, sqrt
import sys

import numpy as np
from scipy.optimize import linprog

from quadratic_gap import binary_ball, threshold
from quadratic_theta import damped_trials
from square_control import square_field_sign
from theta import paley_sign


def raw_margin(vector, root):
    n = len(vector)
    capacity = root * sqrt(n) - 1
    shift = threshold(vector[1:], capacity)
    return vector[0] - root * vector.sum() / sqrt(n) - shift * capacity - np.maximum(-vector[1:] - shift, 0).sum()


def projected_references(sign, widths, side):
    off = 3 if side == 1 else 2
    keep = sign != side
    return np.asarray([
        np.fft.ifft(keep * np.fft.fft(trial[off])).real
        for trial in damped_trials(sign, widths, tolerance=2e-10, rounds=72)
    ])


def solve_relaxation(raw, gauges, root, penalty):
    count, n = raw.shape
    k = len(gauges)
    rows = np.zeros((1 + count + 2 * k, n + k))
    limits = np.zeros(len(rows))
    rows[0, :n - 1] = 1
    limits[0] = root * sqrt(n) - 1
    rows[1:count + 1, :n - 1] = raw[:, 1:]
    rows[1:count + 1, n - 1] = -1
    limits[1:count + 1] = root * raw.sum(axis=1) / sqrt(n) - raw[:, 0]
    for index, vector in enumerate(gauges):
        line = 1 + count + 2 * index
        rows[line:line + 2, :n - 1] = (vector[1:], -vector[1:])
        rows[line:line + 2, n + index] = -1
        limits[line:line + 2] = (-vector[0], vector[0])
    objective = np.r_[np.zeros(n - 1), 1, np.full(k, penalty)]
    bounds = [(0, 1)] * (n - 1) + [(None, None)] + [(0, None)] * k
    result = linprog(objective, A_ub=rows, b_ub=limits, bounds=bounds, method="highs")
    if not result.success:
        raise RuntimeError(result.message)
    coefficients = -result.ineqlin.marginals
    reference_weights = coefficients[1:count + 1]
    gauge_constraints = coefficients[count + 1:].reshape(k, 2)
    gauge_weights = gauge_constraints[:, 0] - gauge_constraints[:, 1]
    combined = reference_weights @ raw
    if k:
        combined += gauge_weights @ np.asarray(gauges)
    bulk = np.r_[1.0, result.x[:n - 1]]
    return combined, (bulk + np.r_[1.0, bulk[:0:-1]]) / 2, result.fun


def certified_margin(sign, side, vector, root):
    from flint import acb, arb, ctx

    ctx.prec = 128
    n = len(sign)
    scale = 10**12
    rounded = [round(scale * float(value)) for value in vector]
    transform = acb.dft(rounded)
    for i in np.flatnonzero(sign == side):
        transform[i] = acb(0)
    sector = [value.real / scale for value in acb.dft(transform, inverse=True)]
    shift = binary_ball(threshold(vector[1:], root * sqrt(n) - 1))
    root = binary_ball(root)
    root_n = arb(n).sqrt()
    capacity = root * root_n - 1
    constant = arb(sum(rounded)) / (scale * root_n)
    if not (capacity >= 0 and constant >= 0):
        return None
    deficit = sum((max(arb(0), (-value - shift).upper()) for value in sector[1:]), arb(0))
    margin = sector[0] - root * constant - shift * capacity - deficit
    output_scale = 10**10
    return Fraction(int((output_scale * margin).lower().floor().unique_fmpz()), output_scale)


def probe(sign, side, widths, root, budget, penalty, certify, gauge_kind):
    n = len(sign)
    raw = projected_references(sign, widths, side)
    single = max(raw_margin(vector, root) for vector in raw)
    opposite = sign == -side
    kernel = np.fft.ifft(opposite).real
    gauges = []
    selected = []
    stages = {0, 1, 4, 12, budget}
    for step in range(budget + 1):
        mixture, bulk, optimum = solve_relaxation(raw, gauges, root, penalty)
        margin = raw_margin(mixture, root)
        if abs(margin - optimum) > 2e-7:
            raise RuntimeError(f"mixture margin {margin} differs from LP optimum {optimum}")
        residual = np.fft.ifft(opposite * np.fft.fft(bulk)).real
        if gauge_kind == 'coordinate':
            residual[np.asarray(selected, dtype=int)] = 0
            residual[1 + n // 2:] = 0
            coord = int(np.argmax(np.abs(residual)))
            remaining = abs(residual[coord])
        else:
            for vector in gauges:
                residual -= np.dot(residual, vector) * vector
            remaining = np.linalg.norm(residual)
        if step in stages or remaining < 1e-10:
            rigorous = certified_margin(sign, side, mixture, root) if certify else None
            yield step, single, margin, rigorous, float(remaining), ' '.join(map(str, selected))
        if step == budget or remaining < 1e-10:
            break
        if gauge_kind == 'coordinate':
            selected.append(coord)
            gauges.append((np.roll(kernel, coord) + np.roll(kernel, -coord)) / 2)
        else:
            gauges.append(residual / remaining)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("primes", nargs="*", type=int)
    parser.add_argument("--square-characteristics", nargs="*", type=int, default=[])
    parser.add_argument("--target-root", type=float, default=.97)
    parser.add_argument("--budget", type=int, default=24)
    parser.add_argument("--penalty", type=float, default=1)
    parser.add_argument("--gauge", choices=('coordinate', 'residual'), default='coordinate')
    parser.add_argument("--widths", nargs="+", type=float)
    parser.add_argument("--certify-max-order", type=int, default=0)
    args = parser.parse_args()
    cases = [(p, p, paley_sign) for p in args.primes]
    cases += [(h * h, h, square_field_sign) for h in args.square_characteristics]
    if not cases or args.budget < 0 or not 0 < args.target_root <= 1:
        parser.error("provide field orders, a nonnegative budget and a target root in (0, 1]")
    if args.penalty <= 0 or not isfinite(args.penalty):
        parser.error("the penalty must be positive and finite")
    if args.widths and any(not 0 < width <= 1 for width in args.widths):
        parser.error("widths must be in (0, 1]")
    writer = csv.writer(sys.stdout, lineterminator="\n")
    writer.writerow(("order", "characteristic", "sign", "target_root", "gauge", "used_columns", "best_single_margin",
                     "mixture_margin", "certified_margin_lower", "next_projection_residual", "columns"))
    for q, h, make_sign in sorted(cases):
        if args.target_root * sqrt((q - 1) / 2) < 1:
            parser.error(f"target root below the universal bound at {q}")
        sign = make_sign(h)
        widths = sorted(set(args.widths or [.5, .3, .2, .1, q**(-1 / 6), q**(-1 / 4), q**(-1 / 3)]), reverse=True)
        for side in (1, -1):
            for row in probe(sign, side, widths, args.target_root, args.budget, args.penalty,
                             q <= args.certify_max_order, args.gauge):
                writer.writerow((q, h, side, args.target_root, args.gauge, *row))
                sys.stdout.flush()


if __name__ == "__main__":
    main()
