"""Replay the first graph-shape moments on the actual Paley localization."""

import csv
from itertools import permutations
from pathlib import Path
import sys

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from square_control import square_field_sign
from theta import paley_sign


def exact_small_check(sign, fourth, cycle, triangle, mixed):
    n = len(sign)
    points = np.arange(n)
    matrix = sign[(points[:, None] - points) % n].astype(np.int64)
    squared = matrix @ matrix
    triangle_matrix = matrix * squared
    joined = matrix @ triangle_matrix
    assert np.array_equal(joined, triangle_matrix @ matrix)
    assert abs(fourth - int(np.sum(squared * squared)) / n**3) < 1e-12
    assert abs(triangle - int(np.sum(triangle_matrix**2)) / n**3) < 1e-12
    assert abs(mixed - int(np.sum(joined**2)) / n**4) < 1e-12
    if n <= 14:
        signed_cycles = sum(
            int(matrix[i, j] * matrix[j, k] * matrix[k, l] * matrix[l, i])
            for i, j, k, l in permutations(range(n), 4)
        )
        assert abs(cycle - signed_cycles / n**3) < 1e-12


def moments(sign):
    n = len(sign)
    spectrum = np.fft.fft(sign).real
    adjacency = spectrum / np.sqrt(n)
    triangle_column = sign * np.fft.ifft(spectrum**2).real / n
    triangle = np.fft.fft(triangle_column).real
    second = float(np.mean(adjacency**2))
    fourth = float(np.mean(adjacency**4))
    triangle_second = float(np.mean(triangle**2))
    mixed = float(np.mean((adjacency * triangle)**2))
    repeated_cycle = (2*n*(n-1)**2 - n*(n-1)) / n**3
    cycle = fourth - repeated_cycle
    chebyshev_defect = fourth - 3*second + 1
    assert abs(triangle_second - (fourth - (1-1/n)**2)) < 1e-12
    if n <= 200:
        exact_small_check(sign, fourth, cycle, triangle_second, mixed)
    return second, fourth, triangle_second, mixed, cycle, chebyshev_defect


def main():
    writer = csv.writer(sys.stdout, lineterminator="\n")
    writer.writerow((
        "order", "square_root", "n", "adjacency_second", "adjacency_fourth",
        "triangle_second", "mixed_fourth", "simple_c4_over_n3", "chebyshev_p4_mean",
    ))
    cases = [(p, None, paley_sign(p)) for p in (13, 29, 97, 401, 9413, 153649, 1000033)]
    cases += [(h*h, h, square_field_sign(h)) for h in (19, 97, 389)]
    for q, h, sign in sorted(cases):
        writer.writerow((q, h, len(sign), *moments(sign)))


if __name__ == "__main__":
    main()
