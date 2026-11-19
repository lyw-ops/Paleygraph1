"""Compare an exterior chosen by Jacobi products with a stationary reference."""

import argparse
import csv
from math import sqrt
import sys

import numpy as np

from coset_activation_probe import solve_mark
from poisson_weights import weighted_iterate
from square_control import square_field_sign
from theta import paley_sign


def centered_exterior(values, support, rho):
    exterior = np.ones(len(values), dtype=bool)
    exterior[support] = False
    result = np.zeros(len(values))
    result[exterior] = (rho / 2) * (values[exterior] - values[exterior].mean())
    return result


def compare(sign, tau):
    n = len(sign)
    kernel = np.fft.fft(sign).real / n
    choices = range(1, min(n // 2, 65))

    def pair_product(shift):
        product = kernel * (np.roll(kernel, shift) + np.roll(kernel, -shift)) / sqrt(2)
        product[[0, shift, -shift]] = 0
        return product

    shift = max(choices, key=lambda h: np.abs(pair_product(h)).sum())
    support = [0, shift, n - shift]
    products = pair_product(shift)
    weights = np.full(n, tau / n)
    weights[0] = 1
    vector, total, stationary_residual = weighted_iterate(sign, weights, tolerance=1e-10)
    rhs = np.full(n, -1 / n)
    rhs[0] += 1
    addition = np.zeros(n)
    addition[support[1:]] = 1 / 4
    zero_response = solve_mark(sign, addition, rhs)[1] - kernel[0]
    direction = 1 if kernel[shift] >= 0 else -1
    for kind, values in (("jacobi-product", direction * np.sign(products)), ("scaled-stationary", vector / total)):
        exterior = centered_exterior(values, support, 1 / 16)
        column, base, base_residual, _ = solve_mark(sign, exterior, rhs)
        _, amended, amended_residual, _ = solve_mark(sign, exterior + addition, rhs)
        yield (
            kind, shift, np.abs(products).sum(), np.dot(products, exterior),
            (column[shift] + column[-shift]) / sqrt(2), zero_response,
            amended - base - zero_response, stationary_residual, max(base_residual, amended_residual),
        )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("primes", nargs="*", type=int)
    parser.add_argument("--square-characteristics", nargs="*", type=int, default=[])
    args = parser.parse_args()
    cases = [(p, p) for p in args.primes] + [(r * r, r) for r in args.square_characteristics]
    if not cases or min(q for q, _ in cases) < 9:
        parser.error("provide field orders at least nine")
    writer = csv.writer(sys.stdout, lineterminator="\n")
    writer.writerow((
        "field_order", "characteristic", "exterior", "shift", "overlap", "first_neumann_term",
        "pair_column", "change_at_zero_background", "interaction", "stationary_residual", "inverse_residual",
    ))
    for q, characteristic in sorted(cases):
        sign = paley_sign(q) if q == characteristic else square_field_sign(characteristic)
        writer.writerows((q, characteristic, *row) for row in compare(sign, 0.05))
        sys.stdout.flush()


if __name__ == "__main__":
    main()
