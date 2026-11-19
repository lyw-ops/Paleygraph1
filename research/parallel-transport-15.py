"""Replay one-sided Fourier deflation and nonnegative repair across growing ratios."""

import argparse
import csv
from math import sqrt
from pathlib import Path
import sys

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from quadratic_theta import damped_trials
from square_control import square_field_sign
from theta import optimize, paley_sign


def jacobi_transform(q, sign, side):
    allowed = sign == side
    count = np.count_nonzero(allowed)
    coefficient = 2 / (sqrt(q) + 1)
    height = 1 + coefficient * count
    transform = allowed.astype(float) * (len(sign) * coefficient / height)
    transform[0] = len(sign) / height
    return transform


def energy(sign, side, width, transform):
    n = len(sign)
    constant = abs(transform[0]) ** 2 / n
    allowed = np.sum(np.abs(transform[sign == side]) ** 2) / n
    if width == 0:
        return constant
    forbidden = np.sum(np.abs(transform[sign == -side]) ** 2) / n
    return constant + width * allowed + forbidden / width


def repair(sign, side, width, raw_hat, kernel_hat):
    n = len(sign)
    raw = np.fft.ifft(raw_hat).real
    defect = np.maximum(-raw, 0)
    kernel_norm = sqrt(energy(sign, side, width, kernel_hat))
    rank = min(n - 1, int(sqrt(n) / kernel_norm))
    threshold = np.partition(defect, n - 1 - rank)[n - 1 - rank]
    excess = np.maximum(defect - threshold, 0)
    correction_hat = kernel_hat * np.fft.fft(excess)
    correction_hat[0] += n * threshold
    repaired_hat = raw_hat + correction_hat
    repaired = np.fft.ifft(repaired_hat).real
    budget = sqrt(n) * threshold + kernel_norm * excess.sum()
    correction_norm = sqrt(energy(sign, side, width, correction_hat))
    if repaired.min() < -1e-12 or correction_norm > budget + 1e-11:
        raise RuntimeError("repair failed its nonnegativity or metric check")
    return defect, repaired[0], sqrt(energy(sign, side, width, repaired_hat)), budget


def endpoint_mass(sign, side, field_root):
    if field_root:
        value = (field_root + 1) / (2 * sqrt(len(sign)))
        return value if side == 1 else 1 / value
    if len(sign) <= 250:
        _, spectrum = optimize(sign, side)
        return sqrt(len(sign)) / spectrum[0]
    return None


def probe(q, sign, field_root, exponent):
    n = len(sign)
    r, s = q ** (-1 / 3), q ** (-exponent)
    ref, target = damped_trials(sign, [s, r], tolerance=2e-10, rounds=48)
    for side, slot, opposite_slot in ((1, 2, 3), (-1, 3, 2)):
        ref_opposite = ref[opposite_slot]
        target_chosen = target[slot]
        ref_opposite_hat = np.fft.fft(ref_opposite)
        target_chosen_hat = np.fft.fft(target_chosen / target_chosen[0])
        u_hat = np.where(sign == side, ref_opposite_hat / s, 0)
        u_norm = np.linalg.norm(u_hat) / sqrt(n)
        u = np.fft.ifft(u_hat).real
        kernel_hat = jacobi_transform(q, sign, -side)
        reference_norm = sqrt(energy(sign, -side, s, ref_opposite_hat))
        c = ref_opposite.sum() / sqrt(n)
        target_upper = energy(sign, side, r, target_chosen_hat)
        target_allowed = np.sum(np.abs(target_chosen_hat[sign == side]) ** 2) / (n * target_upper)
        target_dual = target[opposite_slot]
        target_lower = target_dual[0] ** 2 / energy(sign, -side, r, np.fft.fft(target_dual))
        frozen_hat = np.fft.fft(ref[slot] / ref[slot][0])
        frozen_energy = energy(sign, side, r, frozen_hat)
        frozen_forbidden = np.linalg.norm(frozen_hat[sign == -side]) / sqrt(n)
        frozen_lower_gap = max(0, frozen_forbidden / sqrt(r) - sqrt(target_upper)) ** 2
        allowed_rank = np.count_nonzero(sign == side) / n
        forbidden_rank = np.count_nonzero(sign == -side) / n
        frozen_forbidden_mark = frozen_hat[sign == -side].real.sum() / n
        target_mark_cap = r * (target_upper + sqrt(r * allowed_rank * target_upper))
        marked_lower_gap = 0.0
        if forbidden_rank > 0:
            marked_lower_gap = max(0, frozen_forbidden_mark - target_mark_cap) ** 2 / (r * forbidden_rank)
        if max(frozen_lower_gap, marked_lower_gap) > frozen_energy - target_upper + 1e-8:
            raise RuntimeError("frozen trial gap exceeds the tightly bracketed gap")
        for rho in (0.0, r):
            raw_hat = ref_opposite_hat - (s - rho) * u_hat
            defect, mark, norm, budget = repair(sign, -side, rho, raw_hat, kernel_hat)
            raw_mark = ref_opposite[0] - (s - rho) * u[0]
            raw_norm_bound = sqrt(c * c + (rho / s) * (reference_norm ** 2 - c * c))
            lower = (mark / norm) ** 2
            triangle_lower = (max(raw_mark, 0) / (raw_norm_bound + budget)) ** 2
            if triangle_lower > lower + 1e-10:
                raise RuntimeError("triangle bound exceeds the repaired certificate")
            energy_upper = None
            if rho > 0:
                energy_upper = (u_norm / norm + sqrt(max(0, 1 - lower / target_upper) / r)) ** 2
                if lower > target_upper + 1e-10 or target_allowed > energy_upper + 1e-7:
                    raise RuntimeError("target solve falls outside the transport bounds")
            mass = endpoint_mass(sign, side, field_root)
            if rho == 0 and mass is not None and lower > mass ** 2 + 1e-10:
                raise RuntimeError("endpoint solve falls outside the repair bound")
            # The subfield annihilator is present only on the plus side.
            subfield_loss = None
            if field_root and side == 1:
                indices = slice(field_root - 1, None, field_root - 1)
                subfield_loss = raw_mark - c * mass - rho * (u[0] + u[indices].sum())
                if defect[indices].sum() + 1e-10 < subfield_loss:
                    raise RuntimeError("subfield defect is below its signed sum")
            yield dict(
                order=q, field_root=field_root, sign=side, reference_exponent=exponent,
                target_width=r, reference_width=s, repair_width=rho, width_ratio=s / r,
                reference_residual=ref[-1], target_residual=target[-1],
                reference_mass=c, reference_chosen_energy=u_norm ** 2,
                frozen_trial_energy=frozen_energy, frozen_gap=frozen_energy - target_upper,
                frozen_gap_lower=frozen_lower_gap, marked_gap_lower=marked_lower_gap, repair_budget=budget,
                repaired_root_lower=sqrt(lower), triangle_root_lower=sqrt(triangle_lower),
                subfield_loss=subfield_loss, endpoint_root=mass,
                target_value_upper=target_upper, target_value_lower=target_lower,
                target_chosen_energy=target_allowed, transported_energy_upper=energy_upper,
            )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--primes", nargs="+", type=int, default=[401, 9413, 37253, 153649])
    parser.add_argument("--square-roots", nargs="+", type=int, default=[19, 97, 193, 389])
    args = parser.parse_args()
    cases = [(q, q, None, paley_sign) for q in args.primes]
    cases += [(h * h, h, h, square_field_sign) for h in args.square_roots]
    writer = None
    for q, characteristic, field_root, sign_function in sorted(cases):
        sign = sign_function(characteristic)
        # The second path is below sqrt(r), where the norm-only bound can vanish.
        for exponent in (1 / 12, 1 / 4):
            for row in probe(q, sign, field_root, exponent):
                if writer is None:
                    writer = csv.DictWriter(sys.stdout, row.keys(), lineterminator="\n")
                    writer.writeheader()
                writer.writerow(row)
                sys.stdout.flush()


if __name__ == "__main__":
    main()
