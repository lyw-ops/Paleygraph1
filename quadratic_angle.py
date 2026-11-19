"""Certify normalized sector energies using a single larger-width trial."""

import argparse
import csv
from fractions import Fraction
from math import isfinite, sqrt
import sys

import numpy as np
from scipy.optimize import minimize_scalar

from quadratic_gap import (
    binary_ball,
    capped_deficit_upper,
    numeric_bound,
    rounded_trial_sectors,
    trial_metrics,
)
from quadratic_theta import damped_trials
from square_control import square_field_sign
from theta import paley_sign


OBJECTIVES = ((0, 1, 0), (0, 1, -1), (0, -1, 1))


def metric_axes(mean, pure, foreign, r, s, root):
    mark, allowed, forbidden = root(mean), root(r * pure), root(foreign / r)
    return (mark, allowed, forbidden), (mark, s / r * allowed, r / s * forbidden)


def choose_multiplier(primal, reference, contact, weights):
    product = (np.outer(primal, reference) + np.outer(reference, primal)) / 2
    diagonal = np.diag(weights)

    def evaluate(multiplier):
        return np.linalg.eigvalsh(diagonal + multiplier * product)[-1] - multiplier * contact

    high = 1 / max(1, np.linalg.norm(primal) * np.linalg.norm(reference))
    while high < 1e6 and evaluate(2 * high) < evaluate(high):
        high *= 2
    result = minimize_scalar(evaluate, method="bounded", bounds=(0, 2 * high))
    baseline = float(max(weights))
    if result.fun >= baseline:
        return baseline, 0.0, None
    _, vectors = np.linalg.eigh(diagonal + result.x * product)
    positive = np.maximum(np.abs(vectors[:, -1]), 1e-12)
    return float(result.fun), float(result.x), positive


def certified_objective(primal, reference, contact, weights, multiplier, positive):
    from flint import arb

    if multiplier == 0:
        return arb(max(weights))
    multiplier = binary_ball(multiplier)
    direction = list(map(binary_ball, positive))
    bounds = []
    for i, weight in enumerate(weights):
        shifted_row_action = sum(
            ((primal[i] * reference[j] + reference[i] * primal[j]) * direction[j]
             for j in range(len(weights))), arb(0)
        )
        bound = weight + multiplier * (shifted_row_action / (2 * direction[i]) - contact)
        bounds.append(bound.upper())
    return min(arb(max(weights)), max(bounds))


def certify(sign, side, b, r, s, shift, numerical_trials):
    from flint import ctx

    ctx.prec = 128
    r, s = binary_ball(r), binary_ball(s)
    numerators, scale, transform, mean, allowed, forbidden = rounded_trial_sectors(sign, side, b)
    target_cost = mean + r * allowed + forbidden / r
    reference_cost = mean + s * allowed + forbidden / s
    capacity = (len(sign) * target_cost).sqrt() - 1
    deficit = capped_deficit_upper(sign, side, numerators, scale, transform, s, shift, capacity)
    contact = (reference_cost - deficit).lower()
    primal, reference = metric_axes(mean, allowed, forbidden, r, s, lambda value: value.nonnegative_part().sqrt())

    def outward(ball):
        scale_out = 10**8
        return Fraction(int((scale_out * ball).upper().ceil().unique_fmpz()), scale_out)

    bounds = [
        certified_objective(primal, reference, contact, weights, multiplier, positive)
        for weights, (_, multiplier, positive) in zip(OBJECTIVES, numerical_trials)
    ]
    return outward(bounds[0] / r), -outward(bounds[2]), outward(bounds[1])


def probe(sign, r, widths, certify_order):
    trials = list(damped_trials(sign, [*widths, r], tolerance=2e-10, rounds=72))
    target = trials.pop()
    n = len(sign)
    target_energies = [np.abs(np.fft.fft(target[off]))**2 / n for off in (2, 3)]
    for trial in trials:
        s = trial[0]
        for side, off in ((1, 2), (-1, 3)):
            b = np.minimum(trial[off] / trial[off][0], 1.0)
            costs = np.abs(np.fft.fft(b))**2 / n
            mean = costs[0]
            pure, foreign = costs[sign == side].sum(), costs[sign == -side].sum()
            upper, _, move_cost, deficits, shifts = trial_metrics(sign, side, b, r, s)
            contact = mean + s * pure + foreign / s - deficits[1]
            primal, reference = metric_axes(mean, pure, foreign, r, s, sqrt)
            directional = [choose_multiplier(primal, reference, contact, w) for w in OBJECTIVES]
            bounds = certify(sign, side, b, r, s, shifts[1], directional) if certify_order else (None,) * 3
            target_energy = target_energies[off - 2]
            observed = target_energy[sign == side].sum()
            signed = r * observed - target_energy[sign == -side].sum() / r
            yield (
                s, side, trial[-1], target[-1], observed, signed, contact,
                numeric_bound(upper, pure, move_cost, deficits[1], r), directional[0][0] / r,
                -directional[2][0], directional[1][0], *bounds,
            )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("primes", nargs="*", type=int)
    parser.add_argument("--square-characteristics", nargs="*", type=int, default=[])
    parser.add_argument("--width-factors", nargs="+", type=float, default=[1.02, 1.5, 4.0])
    parser.add_argument("--reference-widths", nargs="*", type=float, default=[])
    parser.add_argument("--certify-max-order", type=int, default=0)
    args = parser.parse_args()
    cases = [(p, p, paley_sign) for p in args.primes]
    cases += [(h**2, h, square_field_sign) for h in args.square_characteristics]
    if not cases or any(not isfinite(f) or f < 1 for f in args.width_factors):
        parser.error("provide orders and finite width factors of at least one")
    if any(not isfinite(s) or not 0 < s <= 1 for s in args.reference_widths):
        parser.error("absolute reference widths must lie in (0, 1]")
    writer = csv.writer(sys.stdout, lineterminator="\n")
    writer.writerow((
        "order", "characteristic", "width", "reference_width", "sign", "reference_residual",
        "target_residual", "numerical_target_energy", "numerical_target_derivative", "contact_lower_trial",
        "previous_split_upper", "directional_energy_upper", "directional_derivative_lower",
        "directional_derivative_upper", "certified_energy_upper", "certified_derivative_lower",
        "certified_derivative_upper",
    ))
    for q, h, maker in sorted(cases):
        r = q**(-1/3)
        candidates = [f * r for f in args.width_factors] + args.reference_widths
        widths = sorted({s for s in candidates if r <= s <= 1}, reverse=True)
        for row in probe(maker(h), r, widths, q <= args.certify_max_order):
            writer.writerow((q, h, r, *row))
            sys.stdout.flush()


if __name__ == "__main__":
    main()
