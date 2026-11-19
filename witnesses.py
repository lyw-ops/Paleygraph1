"""Compare low-dimensional, edge-supported theta witness families."""

import argparse
import csv
from math import sqrt
import sys

import numpy as np
from numpy.polynomial.chebyshev import chebvander
from scipy.optimize import linprog

from theta import paley_sign


def restricted_optimum(support, features):
    """Optimize the coefficients of a row 1_{0} + sum c_j * features_j."""
    n = len(support)
    columns = np.column_stack(features) * support[:, None]
    # Remove identically zero columns and so keep the trivial graph well-defined.
    columns = columns[:, np.any(columns != 0, axis=0)]
    if columns.shape[1] == 0:
        return 1.0
    fourier = np.fft.rfft(columns, axis=0).real
    result = linprog(
        -fourier[0], A_ub=-fourier[1:], b_ub=np.ones(n // 2),
        bounds=(None, None), method="highs",
    )
    if not result.success:
        raise RuntimeError(result.message)
    return 1 - result.fun


def compare(prime, degree):
    sign = paley_sign(prime)
    n = len(sign)
    constant = np.ones(n) / sqrt(n)
    spectrum = np.fft.rfft(sign).real / sqrt(prime)
    chebyshev = np.fft.irfft(chebvander(spectrum, degree)[:, 2:], n=n, axis=0).T
    opposite_offset = np.roll(sign, n // 2) / sqrt(n)
    doubled_offset = sign[2 * np.arange(n) % n] / sqrt(n)

    for side, name in ((1, "complement"), (-1, "local")):
        support = sign == side
        # s(x²)=s(x)s(-x), making the doubled feature redundant on each support.
        if not np.array_equal(doubled_offset[support], side * opposite_offset[support]):
            raise ValueError("character duplication identity failed")
        families = {
            "constant": [constant],
            "opposite": [constant, opposite_offset],
            "chebyshev_2": [constant, chebyshev[0]],
            f"chebyshev_{degree}": [constant, *chebyshev],
            f"combined_{degree}": [constant, opposite_offset, *chebyshev],
        }
        for family, features in families.items():
            value = restricted_optimum(support, features)
            yield prime, name, family, value, value / sqrt(n)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("primes", nargs="+", type=int)
    parser.add_argument("--degree", default=8, type=int)
    args = parser.parse_args()
    if args.degree < 3:
        parser.error("degree must be at least 3")

    writer = csv.writer(sys.stdout, lineterminator="\n")
    writer.writerow(("p", "theta_of", "family", "value", "ratio_to_sqrt_n"))
    for prime in args.primes:
        writer.writerows(compare(prime, args.degree))


if __name__ == "__main__":
    main()
