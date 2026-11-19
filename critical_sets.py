"""Search for critical-size frequency sets with small mean Jacobi deficit."""

import argparse
import csv
from math import ceil, sqrt
import sys

import numpy as np

from square_control import square_field_sign
from theta import paley_sign


def greedy_set(weights, size, second_vertex):
    if size == 1:
        return np.array([0])
    vertices = [0, second_vertex]
    scores = weights + np.roll(weights, second_vertex)
    scores[vertices] = -np.inf
    while len(vertices) < size:
        vertex = int(np.argmax(scores))
        vertices.append(vertex)
        scores += np.roll(weights, vertex)
        scores[vertex] = -np.inf
    return np.array(vertices)


def improve_set(weights, vertices, swaps):
    """Try replacing up to four weakly connected vertices in each step."""
    vertices = vertices.copy()
    scores = np.zeros_like(weights)
    for vertex in vertices:
        scores += np.roll(weights, vertex)

    for _ in range(swaps):
        best_gain = 1e-12
        replacement = None
        for index in np.argsort(scores[vertices], kind="stable")[:4]:
            old = vertices[index]
            candidates = scores - np.roll(weights, old)
            candidates[vertices] = -np.inf
            new = int(np.argmax(candidates))
            gain = candidates[new] - (scores[old] - weights[0])
            if gain > best_gain:
                best_gain = gain
                replacement = (index, old, new)
        if replacement is None:
            break
        index, old, new = replacement
        scores -= np.roll(weights, old)
        scores += np.roll(weights, new)
        vertices[index] = new
    return vertices


def statistics(eigenvalues, weights, vertices):
    n = len(eigenvalues)
    differences = (vertices[:, None] - vertices[None, :]) % n
    compression = eigenvalues[differences] / n
    _, multiplicities = np.unique(differences, return_counts=True)
    energy = int(multiplicities @ multiplicities)
    return (
        1 - weights[differences].mean(),
        np.max(np.abs(np.linalg.eigvalsh(compression))),
        energy,
        energy / differences.size,
        len(multiplicities),
    )


def probe(sign, starts, swaps):
    n = len(sign)
    order = 2 * n + 1
    size = ceil(n / sqrt(order))
    eigenvalues = np.fft.fft(sign).real
    # The kernel is even. Explicit symmetrization keeps ties from shifting due to FFT roundoff.
    eigenvalues[1:] = (eigenvalues[1:] + eigenvalues[:0:-1]) / 2
    weights = eigenvalues ** 2 / order

    interval = np.arange(size)
    yield "interval", 0, statistics(eigenvalues, weights, interval)
    random_set = np.random.default_rng(0).choice(n, size, replace=False)
    yield "random", 0, statistics(eigenvalues, weights, random_set)
    if n % size == 0:
        subgroup = np.arange(size) * (n // size)
        yield "subgroup", 0, statistics(eigenvalues, weights, subgroup)
    if swaps:
        improved = improve_set(weights, interval, swaps)
        yield "interval_swaps", 0, statistics(eigenvalues, weights, improved)

    # Translations and negations preserve the objective. Use only one of each ±h pair.
    second_vertices = 1 + np.argsort(-weights[1 : n // 2 + 1], kind="stable")[:starts]
    for vertex in second_vertices:
        greedy = greedy_set(weights, size, int(vertex))
        yield "greedy", vertex, statistics(eigenvalues, weights, greedy)
        if swaps:
            improved = improve_set(weights, greedy, swaps)
            yield "greedy_swaps", vertex, statistics(eigenvalues, weights, improved)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("primes", nargs="*", type=int)
    parser.add_argument("--square-characteristics", nargs="*", type=int, default=[])
    parser.add_argument("--starts", type=int, default=3)
    parser.add_argument("--swaps", type=int, default=32)
    args = parser.parse_args()
    if not args.primes and not args.square_characteristics:
        parser.error("provide at least one prime or square characteristic")
    if min(args.starts, args.swaps) < 0:
        parser.error("starts and swaps must be nonnegative")

    writer = csv.writer(sys.stdout, lineterminator="\n")
    writer.writerow((
        "field_order", "characteristic", "support_size", "method", "seed_difference",
        "mean_jacobi_deficit", "signed_compression_norm", "additive_energy",
        "energy_over_size_squared", "distinct_differences",
    ))
    orders = [(p, p) for p in args.primes] + [(p * p, p) for p in args.square_characteristics]
    for order, characteristic in sorted(orders):
        sign = paley_sign(characteristic) if order == characteristic else square_field_sign(characteristic)
        size = ceil(len(sign) / sqrt(order))
        for method, seed, stats in probe(sign, args.starts, args.swaps):
            writer.writerow((order, characteristic, size, method, seed, *stats))


if __name__ == "__main__":
    main()
