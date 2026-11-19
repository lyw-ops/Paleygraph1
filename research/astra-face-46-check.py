"""Certify reciprocal forbidden-count columns and two exact complementary endpoints."""
import importlib.util
import json
from math import isqrt
from pathlib import Path
import sys

from flint import acb, arb, ctx

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root))
from theta import paley_sign

spec = importlib.util.spec_from_file_location("endpoints", root / "research/endpoint-direction-45-check.py")
endpoints = importlib.util.module_from_spec(spec)
spec.loader.exec_module(endpoints)
ctx.prec = 192

for p, b in [(41, 4), (101, 5), (193, 6), (337, 8), (541, 9), (1289, 14)]:
    sign = list(map(int, paley_sign(p)))
    n = len(sign)
    h = (1 + isqrt(1 + 4*n)) // 2
    m = n // b
    assert b*m == n and h < 2*b <= 2*h
    sigma = sign[m]
    assert all(sign[t] == sigma for t in range(m, n, m))
    tag = [arb(0) for _ in range(n)]
    forbidden_counts = []
    for a in range(1, m):
        forbidden = [t for t in range(a, n, m) if sign[t] == -sigma]
        assert forbidden
        forbidden_counts.append(len(forbidden))
        for t in forbidden:
            tag[t] = arb(1) / len(forbidden)
    columns = acb.dft([acb(t) for t in tag])
    assert all(x.imag.contains(0) for x in columns)
    assert columns[0].real.contains(m-1)
    assert all(columns[i].real.contains(-1) for i in range(b, n, b))
    upper = max(abs(x.real).upper() for i, x in enumerate(columns) if i % b)
    theoretical = (arb(p).sqrt()+1)/b + arb(10*p)/b**2
    assert upper < theoretical
    result = {"p":p, "subgroup_order":b, "sigma":sigma, "forbidden_min":min(forbidden_counts),
              "column_max_abs_upper":str(upper), "kind":"certified_prime_interpolant"}
    if p in (41, 101):
        pair, error = endpoints.solve_prime_pair(paley_sign(p))
        assert error is None
        mu = [x/arb(n).sqrt() for x in pair[sigma]]
        outside = [i for i in range(n) if i % b]
        mass = sum(mu[i] for i in outside)
        tail_energy = sum(mu[i]**2 for i in outside)
        residual = m*mu[0] - (1-mass) + sum(mu[i]*columns[i].real for i in outside)
        assert residual.contains(0) and residual.rad() < arb("1e-35")
        result.update(kind="certified_prime_endpoint_and_interpolant", mark=str(pair[sigma][0]),
                      exterior_mass=str(mass), exterior_effective_support=str(mass**2/tail_energy))
    print(json.dumps(result, sort_keys=True))
