"""Exact small checks for the mod-four nested determinant-sign proof.

Uses only the already completed round-31 finite-field implementation.
No FFT, high nested contraction, optimizer or stationary solve is used.
The sheaf/purity argument is a mathematical proof in the paired note,
not a conclusion certified by these finite records alone.
"""

from functools import lru_cache
from importlib import import_module
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
Field = import_module('astra-nested-moment-31').Field


def conv(x, y):
    size = len(x)
    return [sum(x[j] * y[(i-j) % size] for j in range(size))
            for i in range(size)]


@lru_cache(None)
def rows(prime, degree):
    field = Field(prime, degree)
    cycle = field.cycle()
    index = {a: i for i, a in enumerate(cycle)}
    sign = [field.chi(field.sub(1, a)) for a in cycle]
    triple = conv(conv(sign, sign), sign)
    reflected = [0 if a == 1 else sign[i] * triple[index[field.sub(1, a)]]
                 for i, a in enumerate(cycle)]
    return field, sign, triple, reflected


def orbit_check(prime, degree):
    field, sign, triple, reflected = rows(prime, degree)
    q, size = field.q, len(sign)
    assert q % 4 == 1
    seen = set()
    orbit_counts = {2: 0, 4: 0}
    weighted = 0
    for i in range(1, size):
        for j in range(1, size):
            k = (-i-j) % size
            point = (i, j, k)
            if k == 0 or point in seen:
                continue
            orbit = {point, (j, i, k),
                     ((-i) % size, (-j) % size, (-k) % size),
                     ((-j) % size, (-i) % size, (-k) % size)}
            assert len(orbit) in orbit_counts
            values = {sign[a] * sign[b] * sign[c] for a, b, c in orbit}
            assert len(values) == 1 and 0 not in values
            seen.update(orbit)
            orbit_counts[len(orbit)] += 1
            weighted += len(orbit) * next(iter(values))
    assert orbit_counts[2] == (q-3)//2
    assert orbit_counts[4] == (q-3)**2//4
    assert weighted == triple[0]
    assert triple[0] % 4 == 2 and triple[0] != 0
    boundary_unit = -sum(reflected)-triple[0]
    assert boundary_unit == 1
    return dict(kind='exact_mod_four_orbit_check', prime=prime, degree=degree,
                order=q, triple_at_one=triple[0], residue_mod_four=triple[0] % 4,
                orbits_size_two=orbit_counts[2], orbits_size_four=orbit_counts[4],
                reflected_sum=sum(reflected), boundary_invariant_eigenvalue=boundary_unit,
                scope='exact finite normalization checks; uniform phase proof is in the note')


def newton_check(prime):
    h1 = rows(prime, 1)[2][0]
    h2 = rows(prime, 2)[2][0]
    numerator = h1*h1-h2
    assert numerator % 2 == 0
    determinant = numerator//2
    assert determinant == prime*prime
    return dict(kind='exact_two_extension_stalk_check', prime=prime,
                trace_degree_one=h1, trace_degree_two=h2,
                determinant_by_newton=determinant, expected_determinant=prime*prime,
                scope='checks the two-dimensional stalk normalization; no high nested contraction')


if __name__ == '__main__':
    for p, degree in [(5, 1), (13, 1), (17, 1), (29, 1), (41, 1),
                      (3, 2), (5, 2), (7, 2), (11, 2)]:
        print(json.dumps(orbit_check(p, degree), sort_keys=True), flush=True)
    for p in (5, 13, 17):
        print(json.dumps(newton_check(p), sort_keys=True), flush=True)
