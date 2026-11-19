"""Measure the bulk excess transfer of the actual Round 17 repair orbit."""

import argparse
import csv
from math import sqrt
from pathlib import Path
import runpy
import sys

import numpy as np

HERE = Path(__file__).resolve().parent
R17 = runpy.run_path(str(HERE / "parallel-repair-17.py"))


def transfer_rows(cost, reserve, project, column, kappa, omega, height,
                  width, bulk_limit, depth, exception_count, subfield):
    n = len(cost)
    mean = .75 * reserve
    alpha = min(2, 1 / (kappa + omega))
    z = -alpha * column
    z[0] += 1
    z_pos_fft = np.fft.rfft(np.maximum(z, 0))
    coefficient = np.maximum(z, 0) / (alpha * omega)
    coefficient[0] = 0
    coefficient_mean = float(coefficient.mean())
    coefficient_std = float(coefficient.std())
    jacobi_cap = (z >= .75 * alpha * omega).astype(float)
    jacobi_cap[0] = 0
    jacobi_cap_size = int(np.count_nonzero(jacobi_cap))
    residue = cost - mean
    energy_bound = float(np.linalg.norm(np.maximum(residue, 0)) / height)
    reciprocal_bound = sqrt(n * width * max(0., 1 - (1-reserve)**2)) / height
    square_deficit = float(cost[subfield].mean()) - mean if subfield is not None else None
    tol = 2e-9

    def transfer(vector):
        return vector - alpha * project(vector)

    def split(r):
        excess = np.maximum(r - bulk_limit, 0)
        # Always include the mark, then remove the largest few other entries.
        count = min(exception_count - 1, n-1)
        indices = 1 + np.argpartition(excess[1:], -count)[-count:] if count else np.empty(0, int)
        indices = np.r_[0, indices]
        paid = float(excess[indices].sum() / height)
        excess[indices] = 0
        return excess, paid, indices

    def gain(target, peak, load, cap_info=False):
        source = peak > 0
        if not np.any(target) or not np.any(source):
            return 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
        target_fft = np.fft.rfft(target.astype(float))
        sums = np.fft.irfft(target_fft * z_pos_fft, n)
        out = float(np.max(sums[source]))
        average = float(sums @ peak / load)
        if not cap_info:
            return out, average, 0.0, 0.0, 0.0, 0.0
        count = np.count_nonzero(target)
        pair_fft = target_fft * np.conj(np.fft.rfft(peak)) / (count * load)
        pair = np.fft.irfft(pair_fft, n)
        energy = float(pair @ pair)
        cap_fraction = float(pair @ jacobi_cap)
        cap_bound = z[0] + alpha * omega * count * (.75 + .25 * cap_fraction)
        moment_bound = z[0] + alpha * omega * count * (
            coefficient_mean + coefficient_std * sqrt(max(0., n * energy - 1)))
        if (average > min(cap_bound, moment_bound) + tol
                or cap_fraction > sqrt(jacobi_cap_size * energy) + tol):
            raise RuntimeError("weighted Jacobi cap incidence did not bound the gain")
        return out, average, cap_bound, moment_bound, n * energy, cap_fraction

    for k in range(depth):
        violation = np.maximum(residue, 0)
        peak, _, _ = split(residue)
        core = violation - peak
        load = float(peak.sum())
        forcing = transfer(core) + np.minimum(residue, 0) - bulk_limit
        next_residue = transfer(violation) + np.minimum(residue, 0)
        next_peak, next_paid, next_exception = split(next_residue)
        next_bulk = next_peak > 0
        # Infer a guard from the current clipped core, before using Z peak.
        # Cost uses the coherence bound, with the diagonal counted only once.
        guard = forcing + alpha * omega * load + (z[0] - alpha * omega) * peak >= -1e-12
        guard[0] = False
        if np.any(next_bulk & ~guard):
            raise RuntimeError("guard missed a crossing")
        actual_gain, weighted_gain, cap_bound, moment_bound, pair_energy, cap_mass = gain(
            next_bulk, peak, load, True)
        guard_gain, guard_weighted_gain, _, _, _, _ = gain(guard, peak, load)
        noise = np.maximum(forcing[next_bulk], 0).sum()
        noise_predict = np.maximum(forcing[1:], 0).sum()
        next_load = next_peak.sum()
        mark = max(float(next_residue[0]), 0.) / height
        actual_tail = R17["cap"](next_residue, height)[0]
        observed_bound = bulk_limit + next_paid + (weighted_gain * load + noise) / height
        predictive_bound = bulk_limit + next_paid + (guard_weighted_gain * load + noise_predict) / height
        if (next_load > weighted_gain * load + noise + tol * height
                or next_load > guard_weighted_gain * load + noise_predict + tol * height
                or actual_tail > observed_bound + tol or actual_tail > predictive_bound + tol
                or next_paid > sqrt(exception_count) * energy_bound + tol or energy_bound > reciprocal_bound + tol):
            raise RuntimeError("one-step excess or mark bound failed")
        exact_subfield_face = None
        if subfield is not None:
            expected = subfield.copy()
            expected[next_exception] = False
            exact_subfield_face = np.array_equal(next_bulk, expected)
            if (actual_tail < square_deficit - tol
                    or next_load/height + next_paid < square_deficit - bulk_limit - tol):
                raise RuntimeError("square lower bound failed")
            if exact_subfield_face and np.all(peak[~subfield] == 0) and np.any(peak):
                if abs(weighted_gain - np.count_nonzero(expected)/height) > tol:
                    raise RuntimeError("the square block does not act by averaging")
        yield dict(
            step=k+1, bulk_limit=bulk_limit, source_count=int(np.count_nonzero(peak)),
            next_count=int(next_bulk.sum()), guard_count=int(guard.sum()),
            input_load=load/height, output_load=next_load/height,
            column_gain=actual_gain, weighted_gain=weighted_gain,
            cap_gain_bound=cap_bound, moment_gain_bound=moment_bound,
            pair_energy_times_n=pair_energy, cap_pair_mass=cap_mass,
            guard_gain=guard_gain, guard_weighted_gain=guard_weighted_gain,
            core_injection=noise/height, guard_injection=noise_predict/height,
            next_mark=mark, exception_charge=next_paid,
            exact_subfield_face=exact_subfield_face, square_tail_lower_bound=square_deficit,
            initial_energy_bound=energy_bound, reciprocal_energy_bound=reciprocal_bound, tail=actual_tail,
            split_tail_bound=observed_bound, guard_tail_bound=predictive_bound,
            available_tail_budget=reserve-mean,
        )
        residue = next_residue


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--primes", type=int, nargs="*", default=[401, 9413, 37253, 153649, 1000033])
    parser.add_argument("--square-roots", type=int, nargs="*", default=[19, 97, 193, 389])
    parser.add_argument("--depth", type=int, default=12)
    parser.add_argument("--exceptions", type=int, default=8)
    parser.add_argument("--width", type=float, default=1/16)
    parser.add_argument("--fixed-only", action="store_true")
    args = parser.parse_args()
    if args.exceptions < 1 or args.depth < 1 or not 0 < args.width < 1:
        parser.error("use positive depth, at least one exception and width in (0, 1)")
    cases = [(p, p, None, R17["paley_sign"]) for p in args.primes]
    cases += [(r*r, r, r, R17["square_field_sign"]) for r in args.square_roots]
    writer = None
    for order, characteristic, root, sign_factory in sorted(cases):
        sign = sign_factory(characteristic)
        n = len(sign)
        widths = [args.width] if args.fixed_only else sorted({args.width, order**(-1/4)}, reverse=True)
        for width, _, plus, minus, residual in R17["damped_trials"](sign, widths, 1e-12, 64):
            if residual > 1e-10:
                raise RuntimeError("inaccurate reciprocal reference")
            for side, y in ((1, minus), (-1, plus)):
                project, kappa, omega, (height, _), _ = R17["sector_tools"](sign, side)
                unit = np.zeros(n)
                unit[0] = 1
                column = project(unit)
                reserve = 1 - sqrt(n) * float(y.mean())
                cost = sqrt(n) * np.maximum(-y.mean() - project(y), 0)
                subfield = np.arange(n) % (root-1) == 0 if root and side == 1 else None
                for mode, limit in (("sqrt_width", sqrt(width)/8), ("budget", reserve/5)):
                    for row in transfer_rows(cost, reserve, project, column, kappa, omega,
                                             height, width, limit, args.depth, args.exceptions, subfield):
                        record = dict(order=order, square_root=root, side=side, width=width,
                                      limit_mode=mode, exceptions=args.exceptions,
                                      height=height, reference_residual=residual) | row
                        if writer is None:
                            writer = csv.DictWriter(sys.stdout, record.keys(), lineterminator="\n")
                            writer.writeheader()
                        writer.writerow(record)
            sys.stdout.flush()


if __name__ == "__main__":
    main()
