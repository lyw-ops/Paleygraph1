"""Probe least-norm theta endpoints and marked support compressions."""

import argparse
import csv
from fractions import Fraction
from math import sqrt
import sys

import numpy as np
from scipy.optimize import nnls

from square_control import square_field_sign
from theta import optimize, paley_sign


def even_coordinates(n):
    representatives = np.arange(n // 2 + 1)
    orbit_sizes = np.where((representatives == 0) | (2 * representatives == n), 1, 2)
    return representatives, orbit_sizes


def forbidden_gram(sign, side, support, orbit_sizes):
    n = len(sign)
    forbidden = np.flatnonzero(sign[:len(orbit_sizes)] == -side)
    phases = np.multiply.outer(forbidden, support) % n
    rows = (
        np.cos(2 * np.pi * phases / n) * np.sqrt(orbit_sizes[forbidden, None] * orbit_sizes[support] / n)
    )
    return rows.T @ rows


def minimum_endpoint(sign, side, opposite, orbit_sizes):
    """Project the constant onto the nonnegative kernel on a complementary set."""
    n = len(sign)
    support = np.flatnonzero(opposite < 1e-8)
    support = np.r_[0, support[support != 0]]
    gram = forbidden_gram(sign, side, support, orbit_sizes)
    eigenvalues, eigenvectors = np.linalg.eigh(gram)
    basis = eigenvectors[:, eigenvalues < 1e-11]
    if basis.shape[1] == 0:
        raise RuntimeError(f"empty endpoint kernel at order {2 * n + 1}, sign {side}")
    constant = np.sqrt(orbit_sizes[support] / n)
    coefficients = basis.T @ constant
    if np.min(basis @ coefficients) < -1e-9:
        multiplier, _ = nnls(basis.T, -coefficients, maxiter=10 * len(support))
        coefficients += basis.T @ multiplier
    projected = basis @ coefficients
    mass = constant @ projected
    if mass <= 0:
        raise RuntimeError("complementary cone has no positive-mass endpoint")
    result = np.zeros(len(orbit_sizes))
    result[support] = projected / mass
    if np.min(result) < -1e-8:
        raise RuntimeError("nonnegative endpoint projection failed")
    return result, len(support)


def compression_row(sign, side, x, y, orbit_sizes):
    n = len(sign)
    support = np.flatnonzero(x > 1e-8)
    gram = forbidden_gram(sign, side, support, orbit_sizes)
    spectrum, vectors = np.linalg.eigh(gram)
    positive = spectrum > 1e-11
    alpha = x[0]
    constant = np.sqrt(orbit_sizes[support] / n)
    mark = np.zeros(len(support))
    mark[0] = 1
    direction = mark - alpha * constant
    coordinates = vectors.T @ direction
    null_weight = np.linalg.norm(vectors[0, ~positive]) ** 2
    if abs(null_weight * (x @ x) - alpha**2) > 1e-7 or np.linalg.norm(coordinates[~positive]) > 1e-7:
        raise RuntimeError("endpoint compression identity failed")
    eigenvalues = spectrum[positive]
    inverse_weights = coordinates[positive] ** 2 / (alpha**2 * eigenvalues)
    extension = inverse_weights.sum()
    free_energy = y @ y - 1 - extension
    if free_energy < -1e-7:
        raise RuntimeError("opposite energy below marked minimum")
    return (
        support, int(orbit_sizes[support].sum()), np.count_nonzero(~positive),
        eigenvalues[0] if len(eigenvalues) else None, null_weight,
        extension, free_energy,
        inverse_weights[eigenvalues <= 1 / n].sum(),
        inverse_weights[eigenvalues <= 1 / sqrt(n)].sum(),
    )


def certified_norms(sign, supports, orbit_sizes):
    """Certify an exactly complementary pair when both active systems are square."""
    from flint import arb, arb_mat, ctx

    n = len(sign)
    if len(set(supports[1]) | set(supports[-1])) != len(orbit_sizes):
        return {}
    if set(supports[1]) & set(supports[-1]) != {0}:
        return {}
    ctx.prec = 128
    values = {}
    scale = 10**10
    for side in (1, -1):
        support = supports[side][1:]
        forbidden = np.flatnonzero(sign[:len(orbit_sizes)] == -side)
        if len(support) != len(forbidden):
            return {}
        if len(support):
            phi = 2 * arb.pi() / n
            system = arb_mat([
                [int(orbit_sizes[k]) * (phi * (int(j * k) % n)).cos() for k in support]
                for j in forbidden
            ])
            try:
                ext = system.solve(arb_mat([[-1] for _ in forbidden]))
            except ValueError:
                return {}
            entries = [ext[i, 0] for i in range(len(support))]
            if not all(entry > 0 for entry in entries):
                return {}
        else:
            entries = []
        mass = 1 + sum(int(orbit_sizes[k]) * entry for k, entry in zip(support, entries))
        squared_norm = 1 + sum(int(orbit_sizes[k]) * entry**2 for k, entry in zip(support, entries))
        norm = arb(n) * squared_norm / mass**2
        values[side] = (
            Fraction(int((norm * scale).lower().floor().unique_fmpz()), scale),
            Fraction(int((norm * scale).upper().ceil().unique_fmpz()), scale),
        )
    return values


def compare(sign, certify):
    n = len(sign)
    representatives, orbit_sizes = even_coordinates(n)
    lp = {side: optimize(sign, side)[1][representatives] / sqrt(n) for side in (1, -1)}
    endpoints = {}
    set_sizes = {}
    for side in (1, -1):
        endpoints[side], set_sizes[side] = minimum_endpoint(sign, side, lp[-side], orbit_sizes)
        if abs(lp[side][0] - endpoints[side][0]) > 1e-7:
            raise RuntimeError("minimum-norm endpoint has the wrong mark")
    rows = {
        side: compression_row(sign, side, endpoints[side], endpoints[-side], orbit_sizes)
        for side in (1, -1)
    }
    bounds = certified_norms(sign, {side: row[0] for side, row in rows.items()}, orbit_sizes) if certify else {}
    for side, row in rows.items():
        x = endpoints[side]
        yield side, x[0], x @ x, set_sizes[side], *row[1:], *bounds.get(side, (None, None))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("primes", nargs="*", type=int)
    parser.add_argument("--square-characteristics", nargs="*", type=int, default=[])
    parser.add_argument("--certify-max-order", type=int, default=0)
    args = parser.parse_args()
    cases = [(p, p, paley_sign) for p in args.primes]
    cases += [(p**2, p, square_field_sign) for p in args.square_characteristics]
    if not cases:
        parser.error("supply prime or square field orders")
    writer = csv.writer(sys.stdout, lineterminator="\n")
    writer.writerow((
        "field_order", "characteristic", "sign", "mark", "norm_squared", "allowed_even_size",
        "active_size", "even_nullity", "min_positive_eigenvalue", "marked_null_weight",
        "opposite_min_extension_energy", "opposite_free_energy", "inverse_energy_below_1_over_n",
        "inverse_energy_below_1_over_root_n", "certified_norm_lower", "certified_norm_upper",
    ))
    for order, characteristic, make_sign in sorted(cases):
        for row in compare(make_sign(characteristic), order <= args.certify_max_order):
            writer.writerow((order, characteristic, *row))
            sys.stdout.flush()


if __name__ == "__main__":
    main()
