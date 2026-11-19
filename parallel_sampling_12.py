"""Replay folded support counts and centered leakage on Paley interval samples."""

import argparse
import csv
from math import gcd, isqrt, sqrt
import sys

import numpy as np

from endpoint_norm import even_coordinates, minimum_endpoint
from theta import optimize, paley_sign


def longest_odd_run(sign, side):
    stops = np.flatnonzero(sign != side)
    gaps = np.diff(np.r_[stops, stops[0] + len(sign)]) - 1
    start = int(np.argmax(gaps))
    length = int(gaps[start])
    length -= (length + 1) % 2
    if length < 1:
        raise ValueError("no run of the requested sign")
    return (int(stops[start]) + 1 + length // 2) % len(sign), length


def centered_arc(sign, cofactor, side):
    order = len(sign) // cofactor
    residues = np.arange(order)
    subgroup = sign[::cofactor]
    power = next(
        (exponent for exponent in range(1, order)
         if subgroup[exponent] == side and gcd(exponent, order) == 1),
        None,
    )
    if power is None:
        raise ValueError(f"no generator of sign {side} in the subgroup of order {order}")
    subgroup = subgroup[power * residues % order]
    center, length = longest_odd_run(subgroup, side)
    half_width = length // 2
    run = (center + np.arange(-half_width, half_width + 1)) % order
    if not np.all(subgroup[run] == side):
        raise RuntimeError("chosen run leaves the Paley sector")

    sample = (30 * residues >= 7 * order) & (30 * residues <= 23 * order)
    angles = (2 * np.pi / order) * residues
    cutoff = np.cos(7 * np.pi / 30)
    argument = np.abs(np.cos(angles / 2) / cutoff)
    degree = length - 1
    inside = argument <= 1
    envelope = np.empty(order)
    denominator = np.cosh(degree * np.arccosh(1 / cutoff))
    envelope[inside] = np.cos(degree * np.arccos(argument[inside])) / denominator
    envelope[~inside] = np.cosh(degree * np.arccosh(argument[~inside])) / denominator
    wave = envelope * np.cos((2 * np.pi / order) * (center * residues % order))
    cosine = np.cos(angles)
    correction = wave[sample].sum() / cosine[sample].sum()
    if abs(1 - correction) < 1e-12:
        raise ValueError("the chosen run gives zero mark after centering")
    direction = -(wave - correction * cosine) / (1 - correction)
    if abs(direction[0] + 1) > 1e-12 or abs(direction[sample].sum()) > 1e-10:
        raise RuntimeError("centering or mark check failed")
    sector_error = np.max(np.abs(np.fft.fft(direction)[subgroup != side])) / order
    if sector_error > 1e-12:
        raise RuntimeError("centered sample direction leaves the Paley sector")

    # Positional cosets have the same sizes after changing the subgroup generator.
    maximum_sector_size = max(
        np.count_nonzero(sign[coset::cofactor] == side) for coset in range(cofactor)
    )
    return (
        power, length, int(sample.sum()) * cofactor, maximum_sector_size,
        int(sample.sum()) >= maximum_sector_size,
        sqrt(cofactor) * np.linalg.norm(direction[sample]),
        np.max(np.abs(direction[sample])), sector_error,
    )


def endpoint_folds(sign, side):
    n = len(sign)
    ell = n // 2
    forbidden_even = sign[::2] == -side
    forbidden_odd = sign[(2 * np.arange(ell) + ell) % n] == -side
    minimum_row_count = min(forbidden_even.sum(), forbidden_odd.sum())
    intersection = (forbidden_even & forbidden_odd).sum()
    union = (forbidden_even | forbidden_odd).sum()
    bound = min(union + 1, minimum_row_count + intersection + 2)

    reps, weights = even_coordinates(n)
    opposite = optimize(sign, -side)[1][reps] / sqrt(n)
    x, _ = minimum_endpoint(sign, side, opposite, weights)
    anchored = x / (x[0] * np.sqrt(weights))
    active = anchored > 1e-8
    counts = [int(weights[active & (reps % 2 == parity)].sum()) for parity in (0, 1)]
    occupied = np.r_[reps[active], -reps[active]] % ell
    if sum(counts) < bound:
        raise RuntimeError("numerical support violates the exact cardinality bound")
    if all(counts) and (min(counts) <= intersection or max(counts) <= minimum_row_count):
        raise RuntimeError("numerical support violates the exact fiber bounds")
    if not all(counts) and sum(counts) <= union:
        raise RuntimeError("a single active fiber must meet the exact union bound")

    bulk_mass = weights @ anchored - 1
    density_energy = bulk_mass**2 / (sum(counts) - 1)
    centered_energy = weights @ anchored**2 - 1 - density_energy
    return (
        int(minimum_row_count), int(intersection), int(union), int(bound),
        *counts, len(np.unique(occupied)), density_energy, centered_energy,
    )


def certify_p29():
    """Certify the larger theta endpoint is unique and uses only even frequencies."""
    from flint import arb, ctx, fmpq_poly, fmpz_poly

    from endpoint_extension_certificate import solve

    ctx.prec = 128
    sign = paley_sign(29)
    n = len(sign)
    modulus = fmpq_poly(fmpz_poly.cyclotomic(n))
    zeta = fmpq_poly([0, 1])
    powers = [zeta**k % modulus for k in range(n)]
    cosine = [(2 * arb.pi() * k / n).cos() for k in range(n)]

    def enclose(value):
        return sum(arb(c.numerator) / c.denominator * cosine[k] for k, c in enumerate(value))

    def equations(side, support):
        return [
            [sum(powers[j * k % n] for k in {i, -i % n}) for i in support]
            for j in range(1, n // 2 + 1) if sign[j] == -side
        ]

    def anchored_mass(side, support):
        matrix = equations(side, support)
        values, rank = solve(matrix, [fmpq_poly([-1])] * len(matrix), modulus)
        if rank != len(support) or not all(enclose(x) > 0 for x in values):
            raise RuntimeError("p=29 support or positivity certificate failed")
        return 1 + sum(len({i, -i % n}) * x for i, x in zip(support, values))

    plus_support = (1, 4, 5, 7)
    minus_support = (2, 6)
    if set(plus_support) & set(minus_support):
        raise RuntimeError("p=29 supports are not complementary")
    plus_mass = anchored_mass(1, plus_support)
    minus_mass = anchored_mass(-1, minus_support)
    if (plus_mass * minus_mass) % modulus != n or not enclose(minus_mass) < arb(n).sqrt():
        raise RuntimeError("p=29 paired mark certificate failed")

    allowed_minus = sorted(set(range(1, n // 2 + 1)) - set(plus_support))
    allowed_matrix = equations(-1, allowed_minus)
    _, rank = solve(allowed_matrix, [fmpq_poly()] * len(allowed_matrix), modulus)
    if rank != len(allowed_minus):
        raise RuntimeError("p=29 even minus optimum is not certified unique")
    # If another nonnegative optimizer used an inactive frequency, its even
    # symmetrization would put positive mass there as well. On the resulting
    # even-frequency support the folded prime Fourier matrix has nullity one.
    folded_forbidden = {j % (n // 2) for j, value in enumerate(sign) if value == 1}
    full_support = {0, *minus_support, *(-i % n for i in minus_support)}
    if any(i % 2 for i in full_support) or len(folded_forbidden) != len(full_support) - 1:
        raise RuntimeError("p=29 folded uniqueness certificate failed")
    return arb(n).sqrt() / enclose(minus_mass)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("primes", type=int, nargs="*")
    parser.add_argument("--cofactor", type=int, default=1)
    parser.add_argument("--endpoint-folds", action="store_true")
    parser.add_argument("--certify-p29", action="store_true")
    args = parser.parse_args()
    if args.cofactor < 1:
        parser.error("cofactor must be positive")
    if args.certify_p29:
        print("Certified p=29 larger normalized mark", certify_p29(), file=sys.stderr)
    if not args.primes:
        if not args.certify_p29:
            parser.error("supply prime orders or request the p=29 certificate")
        return

    writer = csv.writer(sys.stdout, lineterminator="\n")
    if args.endpoint_folds:
        writer.writerow((
            "p", "sign", "min_forbidden_row_count", "intersection", "union",
            "support_lower_bound", "even_support", "odd_support", "folded_support",
            "density_energy", "centered_energy",
        ))
    else:
        writer.writerow((
            "p", "cofactor", "opposite_sign", "subgroup_generator_power", "run_length",
            "sample_size", "max_coset_sector_size", "full_column_rank",
            "centered_leakage_l2", "centered_leakage_sup", "sector_error",
        ))

    for prime in args.primes:
        sign = paley_sign(prime)
        if args.endpoint_folds:
            ell = len(sign) // 2
            if len(sign) % 2 or ell < 3 or any(ell % k == 0 for k in range(2, 1 + isqrt(ell))):
                parser.error(f"n must be twice an odd prime for the folding test, got p={prime}")
            for side in (1, -1):
                writer.writerow((prime, side, *endpoint_folds(sign, side)))
        else:
            subgroup_order, remainder = divmod(len(sign), args.cofactor)
            if remainder or gcd(subgroup_order, args.cofactor) != 1:
                parser.error(f"need a cofactor coprime to the subgroup order for p={prime}")
            for side in (1, -1):
                writer.writerow((prime, args.cofactor, side, *centered_arc(sign, args.cofactor, side)))


if __name__ == "__main__":
    main()
