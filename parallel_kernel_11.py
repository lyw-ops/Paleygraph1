"""Replay marked endpoint norm bounds using the paired-support linear programs."""

import argparse
import csv
from math import sqrt
import sys

import numpy as np
from scipy.optimize import linprog
from scipy.sparse import csr_matrix, eye, hstack, kron, vstack

from endpoint_norm import even_coordinates, minimum_endpoint
from square_control import square_field_sign
from theta import optimize, paley_sign


TOL = 2e-7


def solve_lp(cost, **constraints):
    result = linprog(cost, method="highs", **constraints)
    if not result.success:
        raise RuntimeError(result.message)
    return result


def chord_bounds(cosines, weights, n):
    """Bracket the anchored bulk energy by one LP and replay its opposite dual."""
    size = len(weights)
    if not size:
        return 0.0, 0.0, 0.0

    ratio = 1.5
    first = 0.05 / sqrt(n)
    knots = [0.0, first]
    while knots[-1] < 1:
        knots.append(min(1, ratio * knots[-1]))
    knots = np.array(knots)
    left, right = knots[:-1], knots[1:]
    identity = eye(size, format="csr")
    chords = hstack([
        kron((left + right)[:, None], identity),
        kron(-np.ones((len(left), 1)), identity),
    ], format="csr")
    equations = hstack([cosines * weights, csr_matrix((len(cosines), size))], format="csr")
    result = solve_lp(
        np.r_[np.zeros(size), weights],
        A_ub=chords,
        b_ub=np.repeat(left * right, size),
        A_eq=equations,
        b_eq=-np.ones(len(cosines)),
        bounds=[(0, 1)] * size + [(0, None)] * size,
    )
    opposite_coefficients = result.eqlin.marginals
    opposite_samples = cosines.T @ opposite_coefficients
    dual = -opposite_coefficients.sum() - weights @ np.max(
        opposite_samples[:, None] * knots - knots**2, axis=1,
    )
    dual_error = abs(dual - result.fun)
    if dual_error > TOL:
        raise RuntimeError(f"opposite chord dual gap {dual_error:g}")

    distortion = (ratio + 1)**2 / (4 * ratio)
    first_interval_error = weights.sum() * first**2 / 4
    return max(0.0, (dual - first_interval_error) / distortion), result.fun, dual_error


def check_drifts(cosines, active, b, weights, bulk_energy, length):
    """Recover the clipped dual by linear feasibility and test the exact equality case."""
    if not active.any():
        return True, 0.0
    rows = cosines.T
    equations = np.vstack([np.ones(rows.shape[1]), rows[active]])
    rhs = np.r_[-bulk_energy, b[active]]
    shared = rows[~active]
    bounds = (None, None)
    result = solve_lp(
        np.zeros(rows.shape[1]), A_eq=equations, b_eq=rhs,
        A_ub=shared, b_ub=np.zeros(len(shared)), bounds=bounds,
    )
    clipped = np.maximum(rows @ result.x, 0)
    clipping_error = np.max(np.abs(clipped - b))

    # Subtract the paired constant direction before measuring sample energy.
    centered = rows[active] @ result.x - length / weights[active].sum()
    centered_mark = result.x.sum() + length**2 / weights[active].sum()
    if abs(weights[active] @ centered) > TOL or abs(weights[active] @ centered**2 + centered_mark) > TOL:
        raise RuntimeError("centered leakage identity failed")
    if clipping_error > TOL:
        raise RuntimeError(f"opposite clipping residual {clipping_error:g}")

    if not len(shared):
        return True, 0.0
    # Minimize the maximum residual at the shared zeros.
    # This reports an explicit linear gap instead of relying on solver infeasibility.
    relax = np.ones((len(shared), 1))
    test = solve_lp(
        np.r_[np.zeros(rows.shape[1]), 1],
        A_eq=np.column_stack([equations, np.zeros(len(equations))]), b_eq=rhs,
        A_ub=np.vstack([np.hstack([shared, -relax]), np.hstack([-shared, -relax])]),
        b_ub=np.zeros(2 * len(shared)),
        bounds=[bounds] * rows.shape[1] + [(0, None)],
    )
    return test.fun < TOL, test.fun


def compare(sign, characteristic, square):
    n = len(sign)
    reps, orbit_sizes = even_coordinates(n)
    if square:
        plus = (reps % (characteristic - 1) == 0) * ((characteristic - 1) / sqrt(n))
        minus = (
            characteristic - np.fft.fft(sign).real[reps]
        ) / ((characteristic + 1) * sqrt(n))
        minus[0] = (characteristic + 1) / (2 * sqrt(n))
        endpoints = {1: plus * np.sqrt(orbit_sizes), -1: minus * np.sqrt(orbit_sizes)}
        opposite_witnesses = {1: plus, -1: minus}
    else:
        opposite_witnesses = {side: optimize(sign, side)[1][reps] / sqrt(n) for side in (1, -1)}
        endpoints = {
            side: minimum_endpoint(sign, side, opposite_witnesses[-side], orbit_sizes)[0]
            for side in (1, -1)
        }

    if abs(endpoints[1][0] * endpoints[-1][0] - 1) > TOL:
        raise RuntimeError("unpaired endpoint marks")
    for side in (1, -1):
        x = endpoints[side]
        alpha = x[0]
        zeros = np.flatnonzero(endpoints[-side][1:] < 1e-8) + 1
        weights = orbit_sizes[zeros]
        b = x[zeros] / (alpha * np.sqrt(weights))
        active = b > 1e-8
        forbidden = reps[sign[reps] == -side]
        cosine_rows = np.cos(2 * np.pi * (np.multiply.outer(forbidden, reps) % n) / n)
        cosines = cosine_rows[:, zeros]
        if abs(weights @ b - (sqrt(n) / alpha - 1)) > TOL:
            raise RuntimeError("wrong paired bulk mass")
        if len(forbidden) and np.max(np.abs(cosines @ (weights * b) + 1)) > TOL:
            raise RuntimeError("endpoint lies outside the claimed sector")

        length = weights @ b
        bulk_energy = weights @ b**2
        actual_size = weights[active].sum()
        density_term = length**2 / actual_size if actual_size else 0.0
        variance_term = bulk_energy - density_term
        lp_zeros = np.flatnonzero(opposite_witnesses[-side][1:] < 1e-8) + 1
        lower, upper, dual_error = chord_bounds(cosine_rows[:, lp_zeros], orbit_sizes[lp_zeros], n)
        if not lower - TOL <= bulk_energy <= upper + TOL:
            raise RuntimeError("candidate outside the opposite LP bounds")
        true_equality, shared_residual = check_drifts(
            cosines, active, b, weights, bulk_energy, length,
        )
        yield (
            side, alpha, x @ x, actual_size, weights[~active].sum(),
            density_term, variance_term, lower, upper, dual_error, true_equality, shared_residual,
        )


def certify_p97_gap():
    """Enclose the gap lower bound from the shared-zero direction at 10."""
    from flint import arb, ctx, fmpq_poly, fmpz_poly

    from endpoint_extension_certificate import solve

    ctx.prec = 160
    sign = paley_sign(97)
    n = len(sign)
    active = (2, 3, 5, 6, 7, 8, 11, 13, 14, 18, 19, 22)
    modulus = fmpq_poly(fmpz_poly.cyclotomic(n))
    generator = fmpq_poly([0, 1])
    powers = [generator**i % modulus for i in range(n)]
    cosines = [(2 * arb.pi() * i / n).cos() for i in range(n)]
    forbidden = np.flatnonzero(sign[:n // 2 + 1] == -1)

    def entry(j, i):
        return powers[int(j * i) % n] + powers[-int(j * i) % n]

    def enclose(poly):
        return sum(arb(c.numerator) / c.denominator * cosines[i] for i, c in enumerate(poly % modulus))

    matrix = [[entry(j, i) for i in active] for j in forbidden]
    b, rank = solve(matrix, [fmpq_poly([-1]) for _ in forbidden], modulus)
    h, direction_rank = solve(matrix, [-entry(j, 10) for j in forbidden], modulus)
    if rank != len(active) or direction_rank != rank:
        raise RuntimeError("unexpected rank for the certified p=97 support")
    cross = enclose(sum(2 * x * y for x, y in zip(b, h)))
    energy = enclose(2 + sum(2 * y**2 for y in h))
    lower_bound = cross**2 / energy
    if not lower_bound > arb(17097) / 100000:
        raise RuntimeError("failed to certify the p=97 leakage gap")
    return lower_bound


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("primes", nargs="*", type=int)
    parser.add_argument("--square-characteristics", nargs="*", type=int, default=[])
    parser.add_argument("--certify-p97-gap", action="store_true")
    args = parser.parse_args()
    cases = [(p, p, False) for p in args.primes]
    cases += [(p * p, p, True) for p in args.square_characteristics]
    if args.certify_p97_gap:
        print("Certified lower bound on the p=97 plus squared leakage gap", certify_p97_gap(), file=sys.stderr)
    if not cases:
        if not args.certify_p97_gap:
            parser.error("supply prime or square field orders, or request the exact p=97 gap check")
        return
    writer = csv.writer(sys.stdout, lineterminator="\n")
    writer.writerow((
        "order", "characteristic", "sign", "mark", "norm_squared", "actual_bulk_size", "shared_zeros",
        "density_term", "variance_term", "bulk_lp_lower", "bulk_lp_upper", "chord_dual_error",
        "true_leak_equality", "shared_zero_residual",
    ))
    for order, characteristic, square in sorted(cases):
        sign = square_field_sign(characteristic) if square else paley_sign(characteristic)
        for row in compare(sign, characteristic, square):
            writer.writerow((order, characteristic, *row))
            sys.stdout.flush()


if __name__ == "__main__":
    main()
