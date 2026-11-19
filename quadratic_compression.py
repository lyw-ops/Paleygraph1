"""Measure the two marked compression costs on the actual quadratic support."""

import argparse
import csv
from fractions import Fraction
from math import isfinite, sqrt
import sys

import numpy as np
from scipy.linalg import cho_factor, cho_solve

from endpoint_norm import even_coordinates, forbidden_gram
from quadratic_theta import damped_trials
from square_control import square_field_sign
from theta import paley_sign


def reconstruct(sign, width, side, support, sizes):
    n = len(sign)
    constant = np.sqrt(sizes[support] / n)
    mark = np.zeros(len(support))
    mark[0] = 1
    gram = forbidden_gram(sign, side, support, sizes)
    metric = width**2 * np.eye(len(support)) + (1 - width**2) * gram
    factor = cho_factor(metric)
    inverse_mark, inverse_constant = cho_solve(factor, np.column_stack((mark, constant))).T
    mean_inverse = constant @ inverse_constant
    center = (constant @ inverse_mark) / mean_inverse
    centered_mark = mark - center * constant
    marked_energy = centered_mark @ cho_solve(factor, centered_mark)
    mean_weight = width**2 * mean_inverse
    ridge = width * (1 - width) * mean_inverse
    rooted_inverse = width * (inverse_mark - center * ridge / (1 + ridge) * inverse_constant)
    a = sqrt(rooted_inverse[0])
    restricted = rooted_inverse / a
    c = constant @ restricted
    full = np.zeros(n)
    full[support] = restricted / np.sqrt(sizes[support])
    full[-support] = full[support]
    transformed = np.fft.fft(full)
    weights = np.where(sign == side, width, 1 / width)
    weights[0] = 1
    other = np.fft.ifft(weights * transformed).real
    if (not np.all(full[support] > 0) or other.min() < -1e-8
            or np.max(np.abs(full[1:] * other[1:])) > 1e-8):
        raise RuntimeError("support reconstruction failed its quadratic optimality checks")
    mean_cost = c * c / mean_weight
    mark_cost = marked_energy / (a * a)
    total = (1 - c * c) / width
    if abs(mean_cost + mark_cost - c * c - total) > 1e-7:
        raise RuntimeError("compression energy disagrees with mass identity")
    return a, c, mean_weight, mean_cost, mark_cost, total


def certified_costs(sign, width, side, support, sizes):
    from flint import acb, arb, arb_mat, ctx

    ctx.prec = 160
    n = len(sign)
    ratio = Fraction(width)
    r = arb(ratio.numerator) / ratio.denominator
    orbit_roots = [arb(int(sizes[i])).sqrt() for i in support]
    root_n = arb(n).sqrt()
    constant = arb_mat([[m / root_n] for m in orbit_roots])
    mark = arb_mat([[int(i == 0)] for i in support])
    forbidden = np.flatnonzero(sign == -side)
    cosine = [(2 * arb.pi() * t / n).cos() for t in range(n)]
    kernel = [
        sum((cosine[int(t * k) % n] for t in forbidden), arb(0)) / n
        for k in range(n)
    ]
    matrix = arb_mat([
        [r * r * int(i == j) + (1 - r * r) * wi * wj * (kernel[(i - j) % n] + kernel[(i + j) % n]) / 2
         for j, wj in zip(support, orbit_roots)]
        for i, wi in zip(support, orbit_roots)
    ])
    inverse_mark = matrix.solve(mark)
    inverse_constant = matrix.solve(constant)
    mean_inverse = (constant.transpose() * inverse_constant)[0, 0]
    center = (constant.transpose() * inverse_mark)[0, 0] / mean_inverse
    mean_weight = r * r * mean_inverse
    ridge = r * (1 - r) * mean_inverse
    rooted_inverse = (inverse_mark - inverse_constant * (center * ridge / (1 + ridge))) * r
    a = rooted_inverse[0, 0].sqrt()
    restricted = rooted_inverse * (1 / a)
    assert all(restricted[i, 0] > 0 for i in range(len(support)))
    c = (constant.transpose() * restricted)[0, 0]
    full = [arb(0) for _ in range(n)]
    for row, (i, w) in enumerate(zip(support, orbit_roots)):
        full[int(i)] = full[-int(i)] = restricted[row, 0] / w
    active = {int(i) % n for rep in support for i in (rep, -rep)}
    modes = [
        z if s == 0 else z * r if s == side else z / r
        for s, z in zip(sign, acb.dft(full))
    ]
    other = acb.dft(modes, inverse=True)
    assert all(other[i].real > 0 for i in range(n) if i not in active)
    residual_mark = mark - constant * center
    residual_inverse = inverse_mark - inverse_constant * center
    marked_energy = (residual_mark.transpose() * residual_inverse)[0, 0]

    scale = 10**9

    def bounds(value):
        return (
            Fraction(int((value * scale).lower().floor().unique_fmpz()), scale),
            Fraction(int((value * scale).upper().ceil().unique_fmpz()), scale),
        )

    return *bounds(c * c / mean_weight), *bounds(marked_energy / (a * a)), *bounds((1 - c * c) / r)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("primes", nargs="*", type=int)
    parser.add_argument("--square-characteristics", nargs="*", type=int, default=[])
    parser.add_argument("--scaled-widths", nargs="+", type=float, default=[0.25, 1, 4])
    parser.add_argument("--certify-max-order", type=int, default=0)
    args = parser.parse_args()
    if any(x <= 0 or not isfinite(x) for x in args.scaled_widths):
        parser.error("provide positive finite scaled widths")
    cases = [(p, p, paley_sign) for p in args.primes]
    cases += [(h**2, h, square_field_sign) for h in args.square_characteristics]
    if not cases:
        parser.error("provide prime or square orders")

    writer = csv.writer(sys.stdout, lineterminator="\n")
    writer.writerow((
        "field_order", "characteristic", "sign", "width", "scaled_width", "support_size", "trial_residual",
        "mark", "common_mass", "mean_spectral_weight", "mean_energy", "mark_energy", "total_allowed_energy",
        "certified_mean_lower", "certified_mean_upper", "certified_mark_lower", "certified_mark_upper",
        "certified_total_lower", "certified_total_upper",
    ))
    for q, h, maker in sorted(cases):
        sign = maker(h)
        reps, sizes = even_coordinates(len(sign))
        widths = sorted({scale / sqrt(q) for scale in args.scaled_widths if scale < sqrt(q)}, reverse=True)
        if not widths:
            parser.error(f"no width lies in (0,1) at field order {q}")
        for width, _, plus, minus, residual in damped_trials(sign, widths, 2e-12, 160):
            for side, trial in ((1, plus), (-1, minus)):
                support = reps[trial[reps] > 0]
                terms = reconstruct(sign, width, side, support, sizes)
                bounds = certified_costs(sign, width, side, support, sizes) if q <= args.certify_max_order else (None,) * 6
                writer.writerow((q, h, side, width, width * sqrt(q), sizes[support].sum(), residual, *terms, *bounds))
                sys.stdout.flush()


if __name__ == "__main__":
    main()
