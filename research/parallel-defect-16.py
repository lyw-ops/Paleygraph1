"""Replay positive and signed Fourier repairs of the projected reciprocal row."""

import argparse
import csv
from fractions import Fraction
import json
from math import sqrt
from pathlib import Path
import sys

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from quadratic_theta import damped_trials
from square_control import square_field_sign
from theta import optimize, paley_sign


def repair_tools(sign, side):
    n = len(sign)
    allowed = sign[:n // 2 + 1] == side
    coefficient = 2 / (sqrt(2 * n + 1) + 1)
    height = 1 + coefficient * np.count_nonzero(sign == side)
    kernel = allowed.astype(float) * (n * coefficient / height)
    kernel[0] = n / height
    split = n - 1 - int(height)

    def project(vector):
        return np.fft.irfft(allowed * np.fft.rfft(vector), n)

    def translate(weights):
        return np.fft.irfft(kernel * np.fft.rfft(weights), n)

    def finish(cost, estimate):
        residue = cost - estimate
        threshold = np.partition(residue, split)[split]
        result = estimate + threshold + translate(np.maximum(residue - threshold, 0))
        # The exact formula majorizes the cost. Absorb FFT roundoff in the mean.
        return result + max(0, np.max(cost - result))

    return project, translate, finish


def projected_fit(cost, mass, project, finish, best, sweeps):
    """Use the affine shadow at a proposed mean, then repair its residual."""
    iterate = np.full(len(cost), mass)
    for step in range(sweeps + 1):
        shadow = mass + project(iterate)
        if step % 4 == 0 or step == sweeps:
            candidate = finish(cost, shadow)
            if candidate.mean() < best.mean():
                best = candidate
        if np.max(cost - shadow) <= 1e-12:
            break
        iterate += np.maximum(2 * shadow - iterate, cost) - shadow
    return best


def endpoint_mass(sign, side, root, lp_max):
    n = len(sign)
    if root:
        mass = (root + 1) / (2 * sqrt(n))
        return mass if side == 1 else 1 / mass
    if 2 * n + 1 <= lp_max:
        return sqrt(n) / optimize(sign, side)[1][0]
    return None


def comparisons(sign, side, y, root, sweeps, lp_max):
    n = len(sign)
    root_n = sqrt(n)
    project, translate, finish = repair_tools(sign, -side)
    # Cost and correction are in scaled coordinates. Their ordinary average
    # is the constant Fourier mass in the unscaled normalization.
    scaled_raw = root_n * (y.mean() + project(y))
    c, mark = scaled_raw.mean(), scaled_raw[0] / root_n
    signed = -scaled_raw.copy()
    signed[0] = 0
    positive = np.maximum(signed, 0)
    reserve = 1 - c
    mark_reserve = max(0, mark - c)
    zero = np.zeros(n)

    raw_cap = finish(positive, zero)
    direction = project(positive)
    projected_cap = min(
        (finish(positive, factor * direction) for factor in np.arange(0, 3.01, 0.25)),
        key=np.mean,
    )
    positive_repair = projected_fit(
        positive, (reserve + mark_reserve) / 2, project, finish, projected_cap, sweeps,
    )
    positive_repair = projected_fit(
        positive, mark_reserve, project, finish, positive_repair, sweeps,
    )
    signed_repair = projected_fit(signed, mark_reserve, project, finish, positive_repair, sweeps)

    sparse_lower = sparse_outside_slack = sparse_repair_mean = None
    if root and side == 1:
        subfield = np.arange(n) % (root - 1) == 0
        sparse_lower = positive[subfield].mean()
        sparse = translate(positive * subfield)
        sparse_repair_mean = sparse.mean()
        sparse_outside_slack = np.min((sparse - positive)[~subfield])
        if np.max(np.abs((sparse - positive)[subfield])) > 2e-9:
            raise RuntimeError("subfield translates failed to interpolate their defect")

    mass = endpoint_mass(sign, side, root, lp_max)
    signed_optimum = None if mass is None else mark / mass - c
    positive_optimum = None
    if 2 * n + 1 <= lp_max:
        positive_optimum = float(positive @ optimize(sign, side, positive)[1] / n)
        if not -2e-9 <= positive_repair.mean() - positive_optimum:
            raise RuntimeError("candidate fell below the dense positive majorant LP")

    def endpoint_lower(repair, cost):
        identity_error = np.max(np.abs(repair - repair.mean() - project(repair)))
        if identity_error > 2e-9 or np.min(repair - cost) < -2e-9:
            raise RuntimeError("invalid projected majorant")
        lower = (mark + repair[0] / root_n) / (c + repair.mean())
        if mass is not None and lower > mass + 2e-9:
            raise RuntimeError("repair exceeded endpoint mass")
        return lower

    if sparse_lower is not None and positive_repair.mean() + 2e-9 < sparse_lower:
        raise RuntimeError("repair fell below the subfield obstruction")
    return dict(
        common_mass=c, raw_mark=mark, mean_reserve=reserve, mark_reserve=mark-c,
        raw_cap=raw_cap.mean(), projected_cap=projected_cap.mean(),
        positive_repair=positive_repair.mean(), signed_repair=signed_repair.mean(),
        positive_endpoint_lower=endpoint_lower(positive_repair, positive),
        signed_endpoint_lower=endpoint_lower(signed_repair, signed),
        endpoint_mass=mass, exact_signed_cost=signed_optimum,
        dense_positive_cost=positive_optimum, subfield_cost_lower=sparse_lower,
        subfield_translate_cost=sparse_repair_mean, subfield_outside_slack=sparse_outside_slack,
    ), positive_repair, signed_repair


def reference_balls(sign, width, plus, minus):
    """Enclose a rounded Picard input and its distance to the exact fixed point."""
    from flint import acb, arb, ctx

    ctx.prec = 128
    scale = 10**14
    vector = [arb(round(scale * value)) / scale for value in plus - minus]
    phi = [abs(value) for value in vector]
    phi[0] = (vector[0]**2 + 4).sqrt()
    transform = acb.dft(phi)
    reflected = acb.dft([int(s) * v for s, v in zip(sign, transform)], inverse=True)
    width_fraction = Fraction(width)
    width_ball = arb(width_fraction.numerator) / width_fraction.denominator
    damping = (1 - width_ball) / (1 + width_ball)
    residual_squared = sum((z - damping * v.real)**2 for z, v in zip(vector, reflected))
    error = (residual_squared.sqrt() / (1 - damping)).upper()
    return vector, phi[0], error


def certify(sign, side, balls, candidate, signed, root):
    from flint import acb, arb

    vector, marked_activation, error = balls
    n = len(sign)
    root_n = arb(n).sqrt()
    y = [max(arb(0), -side * value) for value in vector]
    y[0] = (marked_activation - side * vector[0]) / 2
    transformed = acb.dft(y)
    positive_support = (sign == -side) | (sign == 0)
    raw = [v.real for v in acb.dft(
        [v if allowed else acb(0) for v, allowed in zip(transformed, positive_support)],
        inverse=True,
    )]
    c = transformed[0].real / root_n
    mark = raw[0]
    # Round inverse-transform coefficients of the unscaled correction.
    scale = 10**14
    coefficient = np.fft.fft(candidate / sqrt(n)).real
    numerators = [
        round(scale * value) if allowed else 0
        for value, allowed in zip(coefficient, positive_support)
    ]
    for k in range(1, n // 2 + 1):
        numerators[-k] = numerators[k]
    correction = [
        v.real / scale for v in acb.dft(numerators, inverse=True)
    ]
    bulk_slack = min((g + h - error).lower() for g, h in zip(correction[1:], raw[1:]))
    slack = min(correction[0].lower(), bulk_slack)
    if not signed:
        slack = min(slack, min(g.lower() for g in correction))
    bump_units = max(0, int((-slack * scale).upper().ceil().unique_fmpz()))
    bump = arb(bump_units) / scale
    gamma = arb(numerators[0]) / (scale * root_n) + root_n * bump
    lower_mark = mark - error + correction[0] + bump
    if not lower_mark > 0 or not c - error + gamma > 0:
        raise RuntimeError("interval replay did not establish a positive mark and mass")
    bound = lower_mark / (c + error + gamma)
    record = dict(
        reference_l2_error=str(error), bump_units=bump_units, bump_denominator=scale,
        repair_mass=str(gamma), reserve_slack_lower=str((1 - c - error - gamma).lower()),
        endpoint_lower=str(bound.lower()),
    )
    if root and side == 1 and not signed:
        k = (root + 1) // 2
        indices = range(root - 1, n, root - 1)
        negative = min((-raw[i] - error).lower() for i in indices)
        restricted_defect = [arb(0) for _ in range(n)]
        for i in indices:
            restricted_defect[i] = -raw[i]
        coefficients = acb.dft(restricted_defect)
        kernel = [
            v * n * 2 / ((root + 1) * k) if s == -1 else acb(0)
            for s, v in zip(sign, coefficients)
        ]
        kernel[0] = coefficients[0] * n / k
        sparse = acb.dft(kernel, inverse=True)
        # The translates over the subfield annihilator sum to one, so the
        # true sparse repair has coordinate error at most the reference error.
        outside_slack = min(
            (sparse[i].real - error - max(arb(0), (-raw[i] + error).upper())).lower()
            for i in range(n) if i % (root - 1)
        )
        record.update(
            subfield_negative_margin_lower=str(negative),
            subfield_outside_slack_lower=str(outside_slack),
            subfield_excess_over_reserve_lower=str(((mark - error) * root_n / k - 1).lower()),
        )
    return record


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--primes", nargs="*", type=int, default=[401, 9413, 37253, 153649])
    parser.add_argument("--square-roots", nargs="*", type=int, default=[19, 97, 193, 389])
    parser.add_argument("--fixed-width", type=float, default=1 / 16)
    parser.add_argument("--fixed-only", action="store_true")
    parser.add_argument("--sweeps", type=int, default=192)
    parser.add_argument("--lp-max", type=int, default=500)
    parser.add_argument("--certificate", action="store_true", help="emit interval JSONL instead of CSV")
    args = parser.parse_args()
    if not 0 < args.fixed_width <= 1 or args.sweeps < 1:
        parser.error("width must be in (0,1] and sweeps positive")
    cases = [(p, p, None, paley_sign) for p in args.primes]
    cases += [(h * h, h, h, square_field_sign) for h in args.square_roots]
    writer = None
    for order, characteristic, root, get_sign in sorted(cases):
        sign = get_sign(characteristic)
        widths = [args.fixed_width]
        if not args.fixed_only:
            widths.append(order**(-1/4))
        for width, _, plus, minus, residual in damped_trials(sign, widths, 1e-11, 48):
            if residual > 1e-10:
                raise RuntimeError("reference tolerance missed")
            if args.certificate:
                balls = reference_balls(sign, width, plus, minus)
            for side, y in ((1, minus), (-1, plus)):
                results, positive, signed = comparisons(sign, side, y, root, args.sweeps, args.lp_max)
                fields = dict(order=order, field_root=root, side=side, width=width, residual=residual)
                if args.certificate:
                    width_fraction = Fraction(width)
                    fields["width_exact"] = str(width_fraction)
                    fields["positive"] = certify(sign, side, balls, positive, False, root)
                    fields["signed"] = certify(sign, side, balls, signed, True, root)
                    print(json.dumps(fields), flush=True)
                else:
                    row = fields | results
                    if writer is None:
                        writer = csv.DictWriter(sys.stdout, row.keys(), lineterminator="\n")
                        writer.writeheader()
                    writer.writerow(row)
                    sys.stdout.flush()


if __name__ == "__main__":
    main()
