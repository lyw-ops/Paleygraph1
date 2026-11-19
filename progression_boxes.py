"""Compare critical-size frequency boxes, intervals, and subfield controls."""

import argparse
import csv
from math import ceil, sqrt
import sys

import numpy as np

from critical_sets import statistics
from square_control import square_field_sign
from theta import paley_sign


def short_relation(n, lengths, step, cutoff=8):
    """Return the shortest scaled relation if its length is within the cutoff."""
    columns = np.arange(1, cutoff * lengths[1] + 1)
    rows = (-step * columns + n // 2) % n - n // 2
    shortest = min(n / lengths[0], np.min(np.maximum(np.abs(rows) / lengths[0], columns / lengths[1])))
    return float(shortest) if shortest <= cutoff else ""


def supports(order, characteristic):
    n = (order - 1) // 2
    target = n / sqrt(order)
    first = ceil(sqrt(target))
    second = max(2, round(target / first))
    size = first * second
    yield "interval", (size, 1), 0, np.arange(size)
    for label, denominator in (("folded_box", second + 1), ("irrational_step_box", sqrt(2) * (second + 1))):
        step = int(n / denominator)
        vertices = (np.arange(first)[None, :] + step * np.arange(second)[:, None]).ravel()
        if step < first or vertices[-1] >= n:
            raise ValueError(f"box is too small to sample independently at field order {order}")
        yield label, (first, second), step, vertices
    if characteristic != order:
        vertices = np.arange(0, n, characteristic - 1)
        yield "subfield_annihilator", (len(vertices), 1), 0, vertices


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("primes", nargs="*", type=int)
    parser.add_argument("--square-characteristics", nargs="*", type=int, default=[])
    args = parser.parse_args()
    if not args.primes and not args.square_characteristics:
        parser.error("provide at least one prime or square characteristic")

    writer = csv.writer(sys.stdout, lineterminator="\n")
    writer.writerow((
        "field_order", "characteristic", "support", "length_1", "length_2", "step_2", "generated_order",
        "short_relation_if_at_most_8", "compression_norm", "mean_jacobi_deficit", "energy_over_size_cubed",
    ))
    orders = [(p, p) for p in args.primes] + [(r * r, r) for r in args.square_characteristics]
    for order, characteristic in sorted(orders):
        n = (order - 1) // 2
        sign = paley_sign(order) if order == characteristic else square_field_sign(characteristic)
        eigenvalues = np.fft.fft(sign).real
        weights = eigenvalues ** 2 / order
        for label, lengths, step, vertices in supports(order, characteristic):
            deficit, norm, energy, _, _ = statistics(eigenvalues, weights, vertices)
            generated = len(vertices) if label == "subfield_annihilator" else n
            relation = short_relation(n, lengths, step) if step else ""
            writer.writerow((
                order, characteristic, label, *lengths, step, generated, relation,
                norm, deficit, energy / len(vertices) ** 3,
            ))


if __name__ == "__main__":
    main()
