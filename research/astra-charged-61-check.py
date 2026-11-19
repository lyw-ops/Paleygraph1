"""Exact optimal-face vertices and root-fixed bulk bottleneck radii at p=97."""

from itertools import combinations
import importlib.util
import json
from math import gcd
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "face54", Path(__file__).with_name("astra-face-54-check.py")
)
face = importlib.util.module_from_spec(spec)
spec.loader.exec_module(face)
n = face.n
mod = face.modulus


def sign(poly):
    if not poly:
        return 0
    value = face.ball(poly)
    assert not value.contains(0), value
    return 1 if value > 0 else -1


def inverse(poly):
    divisor, inverse_poly, _ = poly.xgcd(mod)
    assert divisor == 1
    return inverse_poly


# Round 54 verifies positive complementary rows and the full rank of the
# minus equations even after admitting both shared inactive orbit anchors.
face.faces()
active = face.active[1]
matrix = face.system(1, active)
solution, _ = face.solve(matrix, [-face.one] * len(matrix), mod)
columns = [face.vector(active, solution, face.one)]
for anchor in face.free:
    other = face.system(1, [anchor])
    solution, _ = face.solve(matrix, [-row[0] for row in other], mod)
    columns.append(face.vector(active + [anchor], solution + [face.one], face.zero))
assert all(not (sum(col) % mod) for col in columns[1:])
rows = list(zip(*columns))
facets = [row for row in rows[1:n // 2 + 1] if row[1] or row[2]]


def evaluate(row, x, y):
    return (row[0] + row[1] * x + row[2] * y) % mod


vertices = []
for (a, b, c), (d, e, f) in combinations(facets, 2):
    det = (b * f - c * e) % mod
    if not det:
        continue
    inv = inverse(det)
    x = ((c * d - a * f) * inv) % mod
    y = ((a * e - b * d) * inv) % mod
    if any(x == u and y == v for u, v in vertices):
        continue
    if all(sign(evaluate(row, x, y)) >= 0 for row in facets):
        vertices.append((x, y))
assert len(vertices) >= 3
endpoints = [[evaluate(row, x, y) for row in rows] for x, y in vertices]
assert all(row[0] == face.one for row in endpoints)
assert all((sum(row) - sum(endpoints[0])) % mod == 0 for row in endpoints)


def intervals(row, generator):
    # Keep the marked unit at zero in its own fixed coupling.
    result = []
    cumulative = face.zero
    for position in range(1, n):
        mass = row[(position * pow(generator, -1, n)) % n]
        if mass:
            cumulative = (cumulative + mass) % mod
            result.append((position, cumulative))
    return result


def radius(left, right):
    i = j = 0
    distance = 0
    while i < len(left):
        distance = max(distance, abs(left[i][0] - right[j][0]))
        difference = sign(left[i][1] - right[j][1])
        i += difference <= 0
        j += difference >= 0
    assert j == len(right)
    return distance


radii = {}
for generator in range(1, n):
    if gcd(generator, n) != 1:
        continue
    cdfs = [intervals(row, generator) for row in endpoints]
    radii[generator] = max(radius(a, b) for a, b in combinations(cdfs, 2))
best = min(radii.values())
print(json.dumps(dict(kind="full_even_face_bulk_quantile_radius", field=97, n=n,
                      vertices=len(vertices), distances="nonwrapping",
                      generators_as_powers_of_reference_generator=radii,
                      tight_best_radius=best), sort_keys=True))
