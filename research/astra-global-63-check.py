"""One genuine cold-time certificate using the overlap forest and two tangent columns."""

import importlib.util
import json
from pathlib import Path

from flint import acb, arb, arb_mat

spec = importlib.util.spec_from_file_location("face54", Path(__file__).with_name("astra-face-54-check.py"))
face = importlib.util.module_from_spec(spec)
spec.loader.exec_module(face)
P, N = face.faces()
n = face.n
v = [arb(0)] * n
for t in range(32):
    a = [abs(x) for x in v]
    a[0] = (4 + v[0] ** 2).sqrt()
    f = acb.dft(a)
    v = [x.real for x in acb.dft([int(s) * y for s, y in zip(face.mask, f)], inverse=True)]

Y = [arb(n).sqrt() * x for x in v]
anchor = [arb(1) / 1000, arb(1) / 100]
zero = arb(0)
plus = []
minus = []
for i in range(n // 2 + 1):
    multiplicity = 1 if i in (0, n // 2) else 2
    a, b, c = (multiplicity * x for x in P[i])
    value = a + b * anchor[0] + c * anchor[1]
    if value != 0:
        assert value > 0
        plus.append((Y[i], value, b, c))
    if N[i] != 0:
        assert N[i] > 0
        minus.append((-Y[i], N[i] * multiplicity, zero, zero))

for side in (plus, minus):
    side.sort(key=lambda row: float(row[0]))
    assert all(a[0] < b[0] for a, b in zip(side, side[1:]))


def cuts(rows):
    result = []
    cumulative = [zero, zero, zero]
    for row in rows:
        cumulative = [a + b for a, b in zip(cumulative, row[1:])]
        result.append(cumulative)
    assert all((a - b).contains(0) for a, b in zip(cumulative, [1, 0, 0]))
    result[-1] = [arb(1), zero, zero]
    return result


def forest(first, second):
    cp, cm = cuts(first), cuts(second)
    i = j = 0
    prev = [zero, zero, zero]
    edges = []
    while i < len(cp):
        x, y = first[i][0], second[j][0]
        if i == len(cp) - 1 and j == len(cm) - 1:
            end = cp[i]
            i += 1
            j += 1
        elif cp[i][0] < cm[j][0]:
            end = cp[i]
            i += 1
        else:
            assert cm[j][0] < cp[i][0], "unresolved or coincident internal cut"
            end = cm[j]
            j += 1
        weight, b, c = [a - d for a, d in zip(end, prev)]
        assert weight > 0
        edges.append((weight, b, c, (x + y + abs(x-y))/2))
        prev = end
    assert j == len(cm)
    return edges


edges = forest(plus, minus)
assert len(edges) == len(plus) + len(minus) - 1
G = arb_mat(2, 2, [sum(e[i]*e[j]/e[0] for e in edges) for i in (1, 2) for j in (1, 2)])
rhs = arb_mat(2, 1, [sum(e[i]*e[3] for e in edges) for i in (1, 2)])
coef = G.solve(rhs)
r = [(b*coef[0, 0]+c*coef[1, 0])/w for w, b, c, _ in edges]
peak = max(x.upper() for x in r)
assert peak > 0
lam = arb(1000000) / int((peak*1000000).ceil().unique_fmpz())
assert all(1-lam*x > 0 for x in r)
gain = lam * sum(w*x*x for (w, _, _, _), x in zip(edges, r))
trial_anchor = [x-lam*coef[i, 0] for i, x in enumerate(anchor)]
updated = [(z, w-lam*(b*coef[0, 0]+c*coef[1, 0]), b, c) for z, w, b, c in plus]
trial = forest(updated, minus)
final = sum(e[0]*e[3] for e in trial)
initial = sum(e[0]*e[3] for e in edges)
assert gain > 0 and (initial-final-gain).contains(0)
least_plus = []
for i in range(n // 2 + 1):
    base = P[i][0]
    if base != 0:
        assert base > 0
        multiplicity = 1 if i in (0, n // 2) else 2
        least_plus.append((Y[i], multiplicity*base, zero, zero))
least_plus.sort(key=lambda row: float(row[0]))
assert all(a[0] < b[0] for a, b in zip(least_plus, least_plus[1:]))
least = sum(e[0]*e[3] for e in forest(least_plus, minus))
assert least > initial
charge = sum(x*x for x in v)/4


def nano(x):
    lo = int((x.lower()*10**9).floor().unique_fmpz())
    hi = int((x.upper()*10**9).ceil().unique_fmpz())
    return [lo, hi]


print(json.dumps(dict(field=97, time=32, scale="1e-9", plus_atoms=len(plus), minus_atoms=len(minus),
                      forest_edges=len(edges), tangent_dimension=2, reference_anchor=["1/1000","1/100"],
                      trial_anchor=[nano(x) for x in trial_anchor], improvement=nano(gain),
                      reference_charged=nano(initial-charge), trial_charged=nano(final-charge),
                      gain_over_least_norm=nano(least-final)),
                 sort_keys=True))
