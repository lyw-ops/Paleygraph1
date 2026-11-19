"""Exact-product obstructions and charged finite intervals on true prime faces."""
import importlib.util
import json
from pathlib import Path
import sys

from flint import arb, ctx

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root))
from theta import certify, cosine_intervals, optimize, paley_sign, prime_divisors

spec = importlib.util.spec_from_file_location(
    "endpoint", root / "research/endpoint-direction-45-check.py")
endpoint = importlib.util.module_from_spec(spec)
spec.loader.exec_module(endpoint)
ctx.prec = 384


def emit(**record):
    print(json.dumps(record, sort_keys=True), flush=True)


def lower_marks(mask):
    scale = 10**12
    cosines = cosine_intervals(len(mask), scale)
    return {s: certify(mask, s, optimize(mask, s)[0], cosines, scale)
            for s in (1, -1)}


def units(x):
    value = x * 10**9
    return [int(value.lower().floor().unique_fmpz()),
            int(value.upper().ceil().unique_fmpz())]


def minimum(values):
    return min(x.lower() for x in values).union(min(x.upper() for x in values))


def joint_max(scores, probabilities):
    # Moving every atom to its certified midpoint costs <= sup radius
    # for both increasing quantiles and so also their pointwise maximum.
    rows = [(s*x.mid(), s, w) for s in (1, -1)
            for x, w in zip(scores, probabilities[s])]
    rows.sort(key=lambda row: row[0])
    last = value = rows[0][0]
    survival = {1: arb(1), -1: arb(1)}
    for position, side, mass in rows:
        a, b = survival.values()
        value += (position-last)*(a+b+abs(a-b))/2
        survival[side] -= mass
        last = position
    return value + arb(0, max(x.rad().upper() for x in scores))


for p in (53, 173, 317):
    mask = paley_sign(p)
    n = len(mask)
    m = n//2
    assert prime_divisors(m) == {m}
    full, folded = lower_marks(mask), lower_marks(mask[::2])
    product = {s: full[s]*folded[-s]/m for s in (1, -1)}
    assert min(product.values()) > 1
    emit(kind="strict_full_vs_quartic_theta", p=p, prime_quotient=m,
         rational_lower_for_cross_product_divided_by_m=
         {s: str(value) for s, value in product.items()})
    if p == 317:
        continue
    pair, error = endpoint.solve_prime_pair(mask)
    assert error is None
    sqrt_n = arb(n).sqrt()
    probabilities = {s: [x/sqrt_n for x in law] for s, law in pair.items()}
    assert all(probabilities[s][0] > probabilities[s][m] for s in (1, -1))
    v = [arb(0)]*n
    charged = []
    for t in range(1, 33):
        activation = [abs(x) for x in v]
        activation[0] = (4+v[0]**2).sqrt()
        v = endpoint.apply_multiplier(activation, mask)
        if t >= 16:
            score = [sqrt_n*x for x in v]
            cost = joint_max(score, probabilities)
            energy = sum(x*x for x in v)
            charged.append((cost-energy/4)/t)
    assert minimum(charged) > 0
    emit(kind="exact_halfturn_dictionary_charged_window", p=p,
         window=[16, 32], precision=ctx.prec,
         minimum_normalized_1e9=units(minimum(charged)),
         terminal_normalized_1e9=units(charged[-1]))

# The one-dimensional branch is attained already at prime 13. Use integer
# sixths for both signs and compute every Fourier zero in Q[z]/Phi_6.
from flint import fmpz_poly

mask = paley_sign(13)
modulus = fmpz_poly.cyclotomic(6)
base = [2, 1, 0, 0, 1, 2]
target = [2, 2, 1, 0, 0, 1]
opposite = [3, 0, 0, 3, 0, 0]
assert mask[0] == 0
for side, row in ((1, base), (1, target), (-1, opposite)):
    assert sum(row) == 6
    for j, sign in enumerate(mask):
        if sign == -side:
            polynomial = sum((fmpz_poly([0]*((i*j) % 6)+[w]) for i, w in enumerate(row)),
                             fmpz_poly())
            assert not polynomial % modulus
assert base[0]*opposite[0] == 6 and target[0]*opposite[0] == 6
assert [a+b for a, b in zip(base[:3], base[3:])] == [2]*3
assert [a+b for a, b in zip(target[:3], target[3:])] == [2]*3
bias = sum((-1)**j*int(x) for j, x in enumerate(mask))
assert bias == -3 and base != target
# Send one sixth from 4 to 1 and one sixth from 5 to 2, both forwards.
origins = (4, 5, 0, 5, 0, 1)
for shift in range(6):
    assert sum(opposite[(x-shift) % 6] for x in origins) == len(origins)
emit(kind="sharp_nonconstant_branch", p=13, attained_dimension=1,
     translated_path_identities=6, halfturn_jacobi=bias, common_pair_masses_in_sixths=[2, 2, 2])
