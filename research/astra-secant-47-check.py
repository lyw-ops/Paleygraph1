"""Verify the quotient Fourier reconstruction, including missing forbidden fibers."""
import importlib.util
import json
from math import gcd
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
for p, b in [(37, 2), (41, 2), (73, 3), (101, 5)]:
    sign = paley_sign(p)
    n = len(sign)
    m = n // b
    assert n == m * b
    sigma = int(sign[m])
    assert all(sign[i] == sigma for i in range(m, n, m))
    tag = [arb(0) for _ in range(n)]
    allowed = []
    for a in range(1, m):
        bad = [i for i in range(a, n, m) if sign[i] == -sigma]
        if bad:
            for i in bad:
                tag[i] = arb(1)/len(bad)
        else:
            allowed.append(a)
    assert (len(allowed)+1)*b*b <= n+b
    column = acb.dft([acb(x) for x in tag])
    cap = (arb(p).sqrt()+1)/b + 10*arb(p)/b**2
    assert all(abs(column[i]) < cap for i in range(n) if i % b)
    pair, error = endpoints.solve_prime_pair(sign)
    assert error is None
    mu = [x/arb(n).sqrt() for x in pair[sigma]]
    outside = [i for i in range(n) if i % b]
    e = sum(mu[i] for i in outside)
    f = acb.dft([acb(mu[b*h]) for h in range(m)])
    truncated = [f[a] if a == 0 or a in allowed else acb(0) for a in range(m)]
    z = acb.dft(truncated, inverse=True)
    for h in range(m):
        discrepancy = (m*(z[h]-mu[b*h])
                       - sum(mu[i]*column[(i-b*h)%n] for i in outside))
        assert discrepancy.contains(0) and abs(discrepancy) < arb('1e-35')
    print(json.dumps(dict(p=p,b=b,sign=sigma,side=("certified_above_one" if pair[sigma][0]>1 else "mark_interval_contains_one" if pair[sigma][0].contains(1) else "certified_below_one"),allowed=allowed,
                          orders=[m//gcd(a,m) for a in allowed],mark=str(pair[sigma][0]),
                          exterior=str(e),verified_coordinates=m),sort_keys=True))
