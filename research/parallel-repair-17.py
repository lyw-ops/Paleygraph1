"""Four clipped Fourier projections, with a positive Jacobi finish (no theta LP)."""

import argparse
import csv
from fractions import Fraction
import json
from math import sqrt
from pathlib import Path
import runpy
import sys

import numpy as np

RESEARCH = Path(__file__).resolve().parent
sys.path.insert(0, str(RESEARCH.parent))
from quadratic_theta import damped_trials
from square_control import square_field_sign
from theta import paley_sign

DEPTHS = (0, 1, 2, 4, 8, 16)


def sector_tools(sign, side):
    n = len(sign)
    allowed = sign[:n // 2 + 1] == -side
    rank = int(np.count_nonzero(sign == -side))

    def project(vector):
        return np.fft.irfft(allowed * np.fft.rfft(vector), n)

    # Off-diagonal maximum of Q = I - P. Use the Jacobi bound as
    # an independent/universal comparison. All coordinates here are scaled.
    lam = np.fft.rfft(sign).real
    universal_omega = (1 + sqrt(2 * n + 1)) / (2 * n)
    # The empty sector at q=5 needs no projection and uses the constant row.
    omega = (1 + np.max(side * lam[1:])) / (2 * n) if rank else universal_omega
    if not 0 < omega <= universal_omega + 2e-14:
        raise RuntimeError("invalid off-diagonal cap")

    def kernel_info(coherence):
        coeff = 1 / (n * coherence)
        height = 1 + rank * coeff
        kernel = allowed.astype(float) * (n * coeff / height)
        kernel[0] = n / height

        def translate(vector):
            return np.fft.irfft(kernel * np.fft.rfft(vector), n)

        return height, translate

    return project, rank / n, omega, kernel_info(omega), kernel_info(universal_omega)


def cap(residue, height):
    split = max(0, len(residue) - 1 - int(height))
    t = float(np.partition(residue, split)[split])
    weights = np.maximum(residue - t, 0)
    return t + float(weights.sum()) / height, t, weights


def trajectories(cost, b, project, kappa, omega, height, universal_height, reserve, subgroup):
    affine = np.full(len(cost), b)
    w = affine.copy()
    size = len(cost)
    step_size = min(2, 1 / (kappa + omega))
    records = []
    chosen = None
    for step in range(max(DEPTHS) + 1):
        shadow = b + project(w)
        residue = cost - affine
        violation = np.maximum(residue, 0)
        upper = np.maximum(-residue, 0)
        pv = project(violation)
        qv = violation - step_size * pv
        new_affine = affine + step_size * pv
        next_e = np.maximum(cost - new_affine, 0)
        if np.max(np.abs(next_e - np.maximum(qv - upper, 0))) > 2e-12:
            raise RuntimeError("residual recursion failed")
        e2, p2, e_next2 = violation @ violation, pv @ pv, next_e @ next_e
        gap = next_e - qv
        if e_next2 + gap @ gap + step_size * (2 - step_size) * p2 > e2 + 2e-10 * max(1, e2):
            raise RuntimeError("residual energy inequality failed")
        m = float(violation.max())
        row_sum_bound = (max(1 - step_size * (kappa + omega), 0) * m
                         + step_size * omega * violation.sum())
        if next_e.max() > row_sum_bound + 2e-11:
            raise RuntimeError("Jacobi row bound failed")

        if step in DEPTHS:
            excess, _, _ = cap(residue, height)
            old_excess = cap(residue, universal_height)[0]
            dr_excess = cap(cost - shadow, height)[0]
            if subgroup is not None:
                subgroup_deficit = float(cost[subgroup].mean()) - b
                if not (excess >= subgroup_deficit - 2e-10 and
                        violation[subgroup].mean() >= subgroup_deficit - 2e-10):
                    raise RuntimeError("subfield lower bound failed")
            records.append(dict(
                step=step,
                tail=excess,
                reserve_excess=b + excess - reserve,
                old_kernel_reserve_excess=b + old_excess - reserve,
                dr_reserve_excess=b + dr_excess - reserve,
                max_violation=m,
                rms_violation=sqrt(e2 / size),
                active_count=int(np.count_nonzero(violation > 1e-12)),
                mass_over_peak=float(violation.sum() / m) if m else 0,
                projected_energy_fraction=float(p2 / e2) if e2 else None,
            ))
        if step == 4:
            chosen = affine.copy()
        affine = new_affine
        w += np.maximum(2 * shadow - w, cost) - shadow
    return chosen, records


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--primes", nargs="*", type=int,
                        default=[401, 9413, 37253, 153649, 1000033])
    parser.add_argument("--square-roots", nargs="*", type=int, default=[19, 97, 193, 389])
    parser.add_argument("--width", type=float, default=1 / 16)
    parser.add_argument("--fixed-only", action="store_true")
    parser.add_argument("--certify-max-order", type=int, default=0,
                        help="emit depth-four interval JSONL for orders up to this limit")
    args = parser.parse_args()
    if not 0 < args.width <= 1:
        parser.error("width must be in (0, 1]")
    reference_tools = runpy.run_path(str(RESEARCH / "parallel-defect-16.py")) if args.certify_max_order else {}
    cases = [(p, p, None, paley_sign) for p in args.primes]
    cases += [(ell**2, ell, ell, square_field_sign) for ell in args.square_roots]
    writer = None
    for order, characteristic, root, get_sign in sorted(cases):
        if args.certify_max_order and order > args.certify_max_order:
            continue
        sign = get_sign(characteristic)
        n = len(sign)
        source_widths = [args.width] if args.fixed_only else sorted({args.width, order**(-1/4)}, reverse=True)
        for width, _, plus, minus, residual in damped_trials(sign, source_widths, 1e-11, 48):
            if residual > 1e-10:
                raise RuntimeError(f"reference tolerance missed at {order}, {width}")
            if args.certify_max_order:
                balls = reference_tools["reference_balls"](sign, width, plus, minus)
            for side, y in ((1, minus), (-1, plus)):
                project, kappa, omega, (height, translate), (universal_height, _) = sector_tools(sign, side)
                raw = sqrt(n) * (y.mean() + project(y))
                cost = np.maximum(-raw, 0)
                common = float(raw.mean())
                reserve = 1 - common
                subgroup = np.arange(n) % (root - 1) == 0 if root and side == 1 else None
                subgroup_excess = float(cost[subgroup].mean()) - reserve if subgroup is not None else None
                meta = dict(order=order, square_root=root, side=side, width=width,
                            common_mass=common, reserve=reserve, raw_mark=float(raw[0]) / sqrt(n),
                            jacobi_height=height, universal_height=universal_height,
                            step_size=min(2, 1 / (kappa + omega)),
                            subfield_excess=subgroup_excess, reference_residual=residual)
                for fraction in ((0.75,) if args.certify_max_order else (1.0, 0.75)):
                    b = fraction * reserve
                    chosen, rows = trajectories(
                        cost, b, project, kappa, omega, height, universal_height, reserve, subgroup,
                    )
                    mass_add, t, weights = cap(cost - chosen, height)
                    correction = chosen + t + translate(weights)
                    if (np.min(correction - cost) < -2e-10 or
                        np.max(np.abs(correction - correction.mean() - project(correction))) > 2e-10 or
                        abs(correction.mean() - b - mass_add) > 2e-10):
                        raise RuntimeError("positive repair failed its formula checks")
                    if args.certify_max_order:
                        record = reference_tools["certify"](sign, side, balls, correction, False, root)
                        print(json.dumps(meta | dict(width_exact=str(Fraction(width)),
                                                     budget_fraction=fraction, step=4) | record), flush=True)
                    else:
                        for row in rows:
                            record = meta | dict(budget_fraction=fraction) | row
                            if writer is None:
                                writer = csv.DictWriter(sys.stdout, record.keys(), lineterminator="\n")
                                writer.writeheader()
                            writer.writerow(record)
                        sys.stdout.flush()


if __name__ == "__main__":
    main()
