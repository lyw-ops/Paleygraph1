"""Compare the first one-sided penalty switch and its mark sensitivity."""

import argparse
import csv
from math import sqrt
import sys

import numpy as np
from scipy.linalg import lu_factor, lu_solve
from scipy.optimize import linprog

from endpoint_norm import even_coordinates, minimum_endpoint
from square_control import square_field_sign
from theta import optimize, paley_sign


def sector_basis(sign, side, orbit_sizes):
    """Orthonormal Fourier columns in real even orbit coordinates."""
    positions = np.flatnonzero(sign[:len(orbit_sizes)] == side)
    phases = np.multiply.outer(np.arange(len(orbit_sizes)), positions) % len(sign)
    return np.cos((2 * np.pi / len(sign)) * phases) * np.sqrt(
        orbit_sizes[:, None] * orbit_sizes[positions] / len(sign)
    )


def general_width(basis, x, outside):
    """Find the tangent ratio directly when the outside restriction is not square."""
    if basis.shape[1] == 0:
        return np.inf
    result = linprog(
        -basis[0] / 2,
        A_ub=-basis[outside],
        b_ub=np.zeros(len(outside)),
        A_eq=[-x @ basis],
        b_eq=[1],
        bounds=(None, None),
        method="highs",
    )
    if result.status == 2:
        return np.inf
    if not result.success or result.fun <= 0:
        raise RuntimeError(f"tangent LP failed: {result.message}")
    return result.fun


def first_change_from_generators(basis, x, y, outside):
    """Use the tangent generators when each outside coordinate is free."""
    factor = lu_factor(basis[outside])
    if np.min(np.abs(np.diag(factor[0]))) < 1e-10:
        return None

    benefit = lu_solve(factor, -(x @ basis), trans=1)
    loss = x[0] * y[outside]
    if np.min(loss) <= 1e-8 or np.max(benefit) <= 1e-8:
        return None
    eligible = np.flatnonzero(benefit > 1e-8)
    ratios = loss[eligible] / (2 * benefit[eligible])
    best = np.argmin(ratios)
    released = eligible[best]
    width = ratios[best]
    if np.count_nonzero(np.abs(ratios - width) <= 1e-7 * width) != 1:
        return None

    unit = np.zeros(len(outside))
    unit[released] = 1
    tangent = basis @ lu_solve(factor, unit)
    if abs(tangent[0] + loss[released]) > 1e-7:
        raise RuntimeError("tangent mark and complementary charge disagree")

    slope = loss[released] ** 2 / (tangent @ tangent)
    change = loss[released] / (tangent @ tangent) * tangent
    u_star = 1 / (2 * width)

    # In u=1/(2t), the initial continuation is x + (u_star-u)*change.
    # Stop when an old positive coordinate or another slack reaches zero.
    gradient_slope = loss - lu_solve(factor, change @ basis, trans=1)
    competitors = np.flatnonzero(gradient_slope > 1e-9)
    competitors = competitors[competitors != released]
    inside = np.flatnonzero((x > 1e-8) & (change < -1e-9))
    next_slack = (u_star * loss[competitors] - benefit[competitors]) / gradient_slope[competitors]
    next_zero = -x[inside] / change[inside]
    step = min(u_star, np.min(next_slack, initial=np.inf), np.min(next_zero, initial=np.inf))
    if not step > 0:
        raise RuntimeError("empty first affine continuation")
    return width, int(outside[released]), loss[released], slope, step / u_star, slope * step


def compare(sign, check):
    n = len(sign)
    reps, orbit_sizes = even_coordinates(n)
    ordinary = {side: optimize(sign, side)[1][reps] / sqrt(n) for side in (1, -1)}
    endpoints = {side: minimum_endpoint(sign, side, ordinary[-side], orbit_sizes)[0] for side in (1, -1)}
    for side in (1, -1):
        x, y = endpoints[side], endpoints[-side]
        basis = sector_basis(sign, side, orbit_sizes)
        outside = np.flatnonzero(x <= 1e-8)
        result = None
        if 0 < len(outside) == basis.shape[1]:
            result = first_change_from_generators(basis, x, y, outside)
        if result is None:
            width = general_width(basis, x, outside)
            row = (width, None, None, None, None, None)
        else:
            width = result[0]
            row = result
            if check:
                independent = general_width(basis, x, outside)
                if abs(width / independent - 1) > 1e-6:
                    raise RuntimeError("two tangent width calculations disagree")
        norm = x @ x
        cap = (x[0] - 1 / sqrt(n)) / (2 * (norm - 1)) if norm > 1 + 1e-10 else np.inf
        if np.isfinite(cap) and width > cap + 1e-7:
            raise RuntimeError("tangent width exceeds the constant trial bound")
        yield side, x[0], norm, row[0] * sqrt(n), cap * sqrt(n), *row


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("primes", nargs="*", type=int)
    parser.add_argument("--square-characteristics", nargs="*", type=int, default=[])
    parser.add_argument("--check-max-order", type=int, default=0)
    args = parser.parse_args()
    cases = [(p, p, paley_sign) for p in args.primes]
    cases += [(h**2, h, square_field_sign) for h in args.square_characteristics]
    if not cases:
        parser.error("supply prime or square field orders")
    writer = csv.writer(sys.stdout, lineterminator="\n")
    writer.writerow((
        "field_order", "characteristic", "sign", "mark", "norm_squared", "scaled_width",
        "scaled_constant_bound", "width", "release_even_index", "release_mark_cost",
        "inverse_penalty_mark_slope", "relative_first_step", "first_piece_mark_loss",
    ))
    for order, h, make_sign in sorted(cases):
        for row in compare(make_sign(h), order <= args.check_max_order):
            writer.writerow((order, h, *row))
            sys.stdout.flush()


if __name__ == "__main__":
    main()
