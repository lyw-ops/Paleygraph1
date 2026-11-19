"""Compare Paley subgroup compressions with the stationary marked response."""

import argparse
import csv
from math import isfinite, isqrt
import sys

import numpy as np

from sensitivity import marked_response
from smoothing import smoothing
from square_control import square_field_sign
from theta import paley_sign


def subgroup_statistics(sign, response):
    q = 2 * len(sign) + 1
    n = len(sign)
    scale = isqrt(q)
    total_energy = np.dot(response, response)
    for b in range(max(1, scale // 2), 2 * scale + 1):
        if n % b:
            continue
        m = n // b
        # Position cosets of the group of order b are residue classes modulo m.
        eigenvalues = sign.reshape(b, m).mean(axis=0)
        # Its annihilator in frequency has cosets indexed modulo b.
        cosets = response.reshape(m, b)
        energies = np.sum(cosets ** 2, axis=0)
        best = np.argmax(energies)
        yield (
            b, m, np.max(np.abs(eigenvalues)), np.dot(eigenvalues, eigenvalues),
            int(best), energies[best] / total_energy,
            np.sum(cosets[:, best]) ** 2 / (m * total_energy),
        )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("primes", nargs="*", type=int)
    parser.add_argument("--square-characteristics", nargs="*", type=int, default=[])
    parser.add_argument("--tau", type=float, default=0.5)
    parser.add_argument("--tolerance", type=float, default=1e-9)
    parser.add_argument("--max-steps", type=int, default=20000)
    args = parser.parse_args()
    if not args.primes and not args.square_characteristics:
        parser.error("provide at least one prime or square characteristic")
    if any(not isfinite(value) or value <= 0 for value in (args.tau, args.tolerance)):
        parser.error("tau and tolerance must be positive and finite")
    if args.max_steps < 3:
        parser.error("max-steps must be at least 3")

    writer = csv.writer(sys.stdout, lineterminator="\n")
    writer.writerow((
        "field_order", "characteristic", "tau", "position_subgroup_order", "frequency_coset_size",
        "compression_norm", "compression_frobenius_squared", "max_energy_coset_index",
        "max_coset_response_energy_share", "constant_on_max_coset_energy_share",
        "inverse_marker_l2", "smoothing_residual_l2", "response_residual_l2", "minres_status",
    ))
    orders = [(p, p) for p in args.primes] + [(p * p, p) for p in args.square_characteristics]
    for order, p in sorted(orders):
        sign = paley_sign(p) if order == p else square_field_sign(p)
        vector, metrics = smoothing(sign, args.tau, args.tolerance, args.max_steps)
        _, _, _, response, _, residual, info = marked_response(
            sign, args.tau, vector, args.tolerance / 10, args.max_steps,
        )
        for stats in subgroup_statistics(sign, response):
            writer.writerow((
                order, p, args.tau, *stats, np.linalg.norm(response), metrics[-2], residual, info,
            ))


if __name__ == "__main__":
    main()
