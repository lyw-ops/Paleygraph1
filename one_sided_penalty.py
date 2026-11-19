"""Measure and enclose marks at fixed inverse penalties along the one-sided path."""

import argparse
import csv
from fractions import Fraction
from math import sqrt
import sys

import numpy as np

from square_control import square_field_sign
from theta import paley_sign


def projection_trial(mask, u, tolerance=1e-5, iterations=40_000):
    n = len(mask)
    constant = 1 / sqrt(n)
    mark_weight = np.count_nonzero(mask) / n

    def project(values):
        return np.fft.ifft(mask * np.fft.fft(values)).real

    base = constant + u * np.fft.ifft(mask).real
    dual = np.zeros(n)
    search = dual.copy()
    momentum = 1.0
    for step in range(1, iterations + 1):
        new_dual = np.maximum(search - (base + project(search)), 0.0)
        new_momentum = (1 + sqrt(1 + 4 * momentum**2)) / 2
        search = new_dual + ((momentum - 1) / new_momentum) * (new_dual - dual)
        dual, momentum = new_dual, new_momentum
        if step % 100 == 0 or step == iterations:
            signed = base + project(dual)
            shift = max(0.0, -signed.min())
            trial = (signed + shift) / (1 + shift / constant)
            gap = np.linalg.norm(trial - signed)**2 + 2 * np.dot(dual, trial)
            mark_error = sqrt(gap * mark_weight)
            if mark_error <= tolerance:
                break
    return dual, trial, mark_error, step


def certified_mark(mask, u, dual):
    """Enclose the mark using an exact feasible repair and a nonnegative dual."""
    from flint import acb, arb, ctx

    n = len(mask)
    ctx.prec = 128
    constant = 1 / arb(n).sqrt()
    multipliers = [arb(float(value)) for value in dual]
    assert all(value >= 0 for value in multipliers)
    source = multipliers.copy()
    source[0] += u
    modes = [value if keep else acb(0) for value, keep in zip(acb.dft(source), mask)]
    signed = [constant + value.real for value in acb.dft(modes, inverse=True)]
    shift = max([arb(0), *[(-value).upper() for value in signed]])
    denominator = 1 + shift / constant
    trial = [(value + shift) / denominator for value in signed]
    gap = arb(0)
    for x, z, y in zip(trial, signed, multipliers):
        difference = shift * (1 - z / constant) / denominator
        gap += difference * difference + 2 * y * x
    mark_error = (gap.upper() * np.count_nonzero(mask) / n).sqrt()
    scale = 10**10
    low = ((trial[0] - mark_error) * scale).lower().floor().unique_fmpz()
    high = ((trial[0] + mark_error) * scale).upper().ceil().unique_fmpz()
    return Fraction(int(low), scale), Fraction(int(high), scale)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("primes", nargs="*", type=int)
    parser.add_argument("--square-characteristics", nargs="*", type=int, default=[])
    parser.add_argument("--inverse-penalties", nargs="+", type=int, default=[4, 16, 64])
    parser.add_argument("--certify-max-order", type=int, default=0)
    args = parser.parse_args()
    cases = [(p, p, paley_sign) for p in args.primes]
    cases += [(h**2, h, square_field_sign) for h in args.square_characteristics]
    if not cases:
        parser.error("supply prime or square field orders")
    if min(args.inverse_penalties) <= 0:
        parser.error("inverse penalties must be positive")
    writer = csv.writer(sys.stdout, lineterminator="\n")
    writer.writerow((
        "field_order", "characteristic", "sign", "inverse_penalty", "trial_mark",
        "trial_norm_squared", "estimated_mark_error", "iterations", "certified_mark_lower",
        "certified_mark_upper",
    ))
    for order, h, make_sign in sorted(cases):
        sign = make_sign(h)
        for side in (1, -1):
            mask = sign == side
            for u in args.inverse_penalties:
                dual, trial, error, steps = projection_trial(mask, u)
                bounds = certified_mark(mask, u, dual) if order <= args.certify_max_order else (None, None)
                writer.writerow((order, h, side, u, trial[0], trial @ trial, error, steps, *bounds))
                sys.stdout.flush()


if __name__ == "__main__":
    main()
