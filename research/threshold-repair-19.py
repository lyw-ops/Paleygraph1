"""Repair a clipped Fourier shadow through its positive transfer matrix."""

import argparse
import json
from math import sqrt
from pathlib import Path
import runpy

import numpy as np
from scipy.linalg import eigh, solve


RESEARCH = Path(__file__).resolve().parent
REPAIR = runpy.run_path(str(RESEARCH / 'parallel-repair-17.py'))


def obstacle(floor, transfer, column, maximum_support):
    """Solve the positive majorant off the origin by an increasing active set."""
    n = len(floor)
    weights = np.zeros(n)
    active = np.zeros(n, dtype=bool)
    positive_column_fft = np.fft.rfft(column)
    initial_support = int(np.count_nonzero(floor[1:] > 0))
    radius = 0.0
    for iteration in range(1, 65):
        majorant = np.fft.irfft(positive_column_fft * np.fft.rfft(weights), n)
        violated = (floor + majorant > 5e-12) & ~active
        violated[0] = False
        record = dict(initial_support=initial_support, active_support=int(active.sum()),
                      rounds=iteration, active_radius=radius)
        if not violated.any():
            error = floor + majorant - weights
            if error[1:].max() > 2e-9 or weights.min() < -2e-9:
                raise RuntimeError('positive obstacle inequalities failed')
            if (floor - (weights - transfer(weights)))[1:].max() > 2e-9:
                raise RuntimeError('signed correction failed its obstacle bound')
            return weights, record | dict(status='feasible')
        active |= violated
        indices = np.flatnonzero(active)
        size = len(indices)
        if size > maximum_support:
            return None, record | dict(status='support_limit', active_support=size, active_radius=None)
        block = column[(indices[:, None] - indices) % n]
        radius = float(eigh(block, eigvals_only=True, subset_by_index=(size - 1, size - 1),
                            check_finite=False)[0])
        if radius >= 1 - 1e-10:
            return None, record | dict(status='spectral_limit', active_support=size, active_radius=radius)
        matrix = -block
        matrix.flat[::size + 1] += 1
        updated = solve(matrix, floor[indices], assume_a='pos', check_finite=False)
        if (updated - weights[indices]).min() < -2e-9:
            raise RuntimeError('active majorant was not monotone')
        weights[indices] = updated
    return None, record | dict(status='iteration_limit')


def trials(sign, side, raw, depth, maximum_support, signed_steps):
    n = len(raw)
    project, kappa, omega, (height, translate), _ = REPAIR['sector_tools'](sign, side)
    reserve = 1 - raw.mean()
    mean = .75 * reserve
    alpha = min(2, 1 / (kappa + omega))
    cost = np.maximum(0, -raw)
    affine = np.full(n, mean)
    unit = np.zeros(n)
    unit[0] = 1

    def transfer(weights):
        return weights - alpha * project(weights)

    column = np.maximum(transfer(unit), 0)
    column = (column + np.r_[column[0], column[:0:-1]]) / 2
    for _ in range(depth):
        affine += alpha * project(np.maximum(cost - affine, 0))
    residue = cost - affine
    baseline_tail, baseline_cutoff, baseline_weights = REPAIR['cap'](residue, height)
    baseline = affine + baseline_cutoff + translate(baseline_weights)

    def endpoint(correction):
        row = raw + correction
        return float(row[0] / (sqrt(n) * row.mean()))

    yield baseline, dict(method='translated', status='feasible', cutoff=baseline_cutoff,
                         repair_mass=float(baseline.mean()), endpoint_ratio=endpoint(baseline),
                         tail=baseline_tail, reserve=reserve)
    for method, cutoff in (('budget', reserve / 4), ('same', baseline_cutoff),
                           ('four_fifths', .8 * baseline_cutoff), ('half', .5 * baseline_cutoff)):
        weights, diagnostics = obstacle(residue - cutoff, transfer, column, maximum_support)
        record = dict(method=method, cutoff=cutoff, reserve=reserve, **diagnostics)
        if weights is None:
            yield None, record
            continue
        correction = affine + cutoff + alpha * project(weights)
        missing = np.maximum(cost - correction, 0)
        patch = float(missing[0] / height)
        correction += translate(missing)
        if (correction - cost).min() < -2e-9:
            raise RuntimeError('round-off or mark patch was insufficient')
        yield correction, record | dict(repair_mass=float(correction.mean()), endpoint_ratio=endpoint(correction),
                                        mark_charge=patch, majorant_mass=float(weights.sum()/height))

    if signed_steps:
        for fraction in (1.0, .8, .5):
            cutoff = fraction * baseline_cutoff
            adjustment = np.zeros(n)
            initial_support = int(np.count_nonzero(residue[1:] > cutoff))
            for _ in range(signed_steps):
                excess = np.maximum(residue - adjustment - cutoff, 0)
                excess[0] = 0
                adjustment += alpha * project(excess)
            new_residue = residue - adjustment
            tail, final_cutoff, remaining = REPAIR['cap'](new_residue, height)
            correction = affine + adjustment + final_cutoff + translate(remaining)
            if (correction - cost).min() < -2e-9:
                raise RuntimeError('signed-iteration finish missed a defect')
            yield correction, dict(method='signed_iteration', status='feasible', cutoff=cutoff,
                                   initial_support=initial_support, rounds=signed_steps,
                                   active_support=int(np.count_nonzero(new_residue[1:] > cutoff)),
                                   final_cutoff=final_cutoff, tail=tail, reserve=reserve,
                                   repair_mass=float(correction.mean()), endpoint_ratio=endpoint(correction))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--primes', nargs='*', type=int, default=[401, 9413, 37253, 153649, 1000033])
    parser.add_argument('--square-roots', nargs='*', type=int, default=[19, 97, 193, 389])
    parser.add_argument('--width', type=float, default=1/16)
    parser.add_argument('--fixed-only', action='store_true')
    parser.add_argument('--depth', type=int, default=4)
    parser.add_argument('--maximum-support', type=int, default=1400)
    parser.add_argument('--certify-max-order', type=int, default=0)
    parser.add_argument('--signed-steps', type=int, default=0)
    args = parser.parse_args()
    if not 0 < args.width < 1 or min(args.depth, args.signed_steps) < 0 or args.maximum_support < 1:
        parser.error('width must lie in (0,1), depths must be nonnegative, and the support limit must be positive')
    cert = runpy.run_path(str(RESEARCH / 'parallel-defect-16.py')) if args.certify_max_order else None
    cases = [(p, p, None, REPAIR['paley_sign']) for p in args.primes]
    cases += [(h*h, h, h, REPAIR['square_field_sign']) for h in args.square_roots]
    for order, characteristic, square_root, maker in sorted(cases):
        sign = maker(characteristic)
        n = len(sign)
        widths = [args.width] if args.fixed_only else sorted({args.width, order**(-1/4)}, reverse=True)
        for width, _, plus, minus, residual in REPAIR['damped_trials'](sign, widths, 1e-11, 48):
            balls = cert['reference_balls'](sign, width, plus, minus) if order <= args.certify_max_order else None
            for side, y in ((1, minus), (-1, plus)):
                raw = sqrt(n) * np.fft.ifft((sign != side)*np.fft.fft(y)).real
                rows = list(trials(sign, side, raw, args.depth, args.maximum_support, args.signed_steps))
                best = min((i for i, (correction, _) in enumerate(rows) if correction is not None),
                           key=lambda i: rows[i][1]['repair_mass'])
                for i, (correction, record) in enumerate(rows):
                    if balls is not None and i in (0, best):
                        record |= cert['certify'](sign, side, balls, correction, False, square_root)
                    print(json.dumps(dict(order=order, square_root=square_root, side=side, width=width,
                                          reference_residual=residual) | record), flush=True)


if __name__ == '__main__':
    main()
