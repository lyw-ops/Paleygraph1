#!/usr/bin/env python3
"""Round 182 independent audit (session/r182-audit): cold-prime signed non-seed price report.

Independent of research/paley-182-cold-*.py (written from the report and from
astra-dissipation-80.md lines 82-112, not from those scripts).

Part 1 (Decimal, 60 digits; a numerical cross-check, not an outward certificate):
  kappa*(p0) = sup_{0<u<=3/8} [1 - p0/u - c(M0+u) u], with
  c(M) = (2/sqrt N)(1 + x/2)(1 - x)^(-5/2), x = M^2/N, N = 4(2031/128 - 2^-17), M0 = 4.823,
  by golden-section refinement; the lambda_max(C) and beta_max tables; the crude
  costs 2A/sqrt N, 4A/sqrt N and the Taylor majorant G(y) recomputed from the series
  sum_{l>=1} (2l+2) c_l x^l with c_l = binom(2l,l)/4^l (checked against the closed form);
  the exact check 1.066^80 > 2^7.
Part 2 (exact integers): brute-force of the Round 80 per-simple rule (shift J by
  (-1,+1) or J^-1 by (+1,-1) on the two fibres; keep negative weights on their fibre,
  exchange positive weights; refill each fibre with zeros to r' = sum|w'|/2) over all
  two-fibre configurations of dimension r <= RMAX with sum |w| = 2r.  For pi_alpha =
  r + alpha*Z/2 (Z = zero slots over both fibres) it reports the maximal m-step path
  ratio found, which must not exceed the report's certified G_m upper bounds.
  (Configurations whose refill would be negative are skipped and counted.)

Replay: python3 -B research/paley-182-audit-cold-check.py
Standard library only; modest memory (RMAX = 4).
"""
from decimal import Decimal as D, getcontext
from fractions import Fraction as F
from itertools import combinations_with_replacement
from math import comb

getcontext().prec = 60

N = D(4) * (D(2031) / D(128) - D(1) / D(2 ** 17))
SQN = N.sqrt()
M0 = D("4.823")


def c_of(M):
    x = M * M / N
    return (D(2) / SQN) * (1 + x / 2) / ((1 - x) ** 2 * (1 - x).sqrt())


def phi(u, p0):
    return 1 - p0 / u - c_of(M0 + u) * u


def kstar(p0):
    lo, hi = D("1e-9"), D("0.375")
    # coarse scan then golden section (phi is unimodal on (0, 3/8] here)
    best = max((phi(D(i) / D(20000) * D("0.375"), p0), i) for i in range(1, 20001))
    i = best[1]
    a = D(max(i - 1, 1)) / D(20000) * D("0.375")
    b = D(min(i + 1, 20000)) / D(20000) * D("0.375")
    gr = (D(5).sqrt() - 1) / 2
    for _ in range(200):
        c1 = b - gr * (b - a)
        c2 = a + gr * (b - a)
        if phi(c1, p0) > phi(c2, p0):
            b = c2
        else:
            a = c1
    u = (a + b) / 2
    return phi(u, p0), u


def G_major(y, terms=400):
    x = y * y / N
    s = D(0)
    cl = D(1)
    xl = D(1)
    for l in range(1, terms):
        cl = cl * D(2 * l - 1) / D(2 * l)  # binom(2l,l)/4^l recursively
        xl = xl * x
        s += (2 * l + 2) * cl * xl
    closed = 2 / (1 - x).sqrt() + x / ((1 - x) * (1 - x).sqrt()) - 2
    assert abs(s - closed) < D("1e-30"), (s, closed)
    return (y / SQN) * closed


def part1():
    print(f"N = {N:.12f}, sqrt N = {SQN:.10f}")
    print(f"c(4.936) = {c_of(D('4.936')):.7f} (R181 audit: <= 1.0043, > 1.0042)")
    ks = {}
    for p0 in (D("0.01272"), D("1e-3"), D("1e-6")):
        k, u = kstar(p0)
        ks[p0] = k
        print(f"p0={p0}: kappa* = {k:.9f} at u = {u:.6f}, c(M0+u) = {c_of(M0+u):.7f}")
    k = ks[D("0.01272")]
    # The report prints kappa* in [0.7741471, 0.7741472], [0.9383484, ...], [0.9980707, ...].
    # Those lower ends are round-to-nearest prints of certified lower bounds, not outward:
    # the supremum itself lies below each printed lower end.
    for p0, lo_printed in ((D("0.01272"), D("0.7741471")), (D("1e-3"), D("0.9383484")),
                           (D("1e-6"), D("0.9980707"))):
        print(f"  p0={p0}: sup = {ks[p0]:.10f} < printed lower end {lo_printed}: {ks[p0] < lo_printed}")
    assert D("0.77414706") <= k <= D("0.77414707")
    assert D("0.99807065") <= ks[D("1e-6")] <= D("0.99807066")
    # fixed-ball statement of the R181 audit: c = 1.0043, discriminant (1-k)^2 - 4 c p0
    for k0 in ("0.77394", "0.77395"):
        disc = (1 - D(k0)) ** 2 - 4 * D("1.0043") * D("0.01272")
        print(f"  c=1.0043, kappa0={k0}: discriminant = {disc:.3e}")
    one = 1 - k
    print("lambda_max(C) = 1 - C(1-kappa*):",
          {str(C): f"{1 - D(C) * one:.5f}" for C in ("1", "1.25", "1.5", "2", "3")})
    s8 = 2 * D(2).sqrt()
    seed_dim = 4 * s8 / (2 * SQN)        # 4 * s_p/(4|sqrt t|) with |sqrt t| >= sqrt N/2
    seed_pi1 = 3 * s8 / (2 * SQN)
    print(f"seed rates (limit s_p = 2 sqrt 2): dimension {seed_dim:.5f}, pi_1 {seed_pi1:.5f}")
    for name, lam, C in (("dim 1-step", seed_dim, D(1)), ("dim 8-step", D("0.53618"), D("1.3243")),
                         ("pi_1/2 8-step", D("0.52194"), D("1.1567")), ("pi_1 1-step", seed_pi1, D(1)),
                         ("pi_1 8-step", D("0.51366"), D("1.0749"))):
        print(f"  beta_max {name:14s} = {(1 - lam) / C - one:.5f}")
    A = M0 - s8
    print(f"A(h) <= M0 - 2sqrt2 = {A:.6f}; h-linear crude: dim {2*A/SQN:.5f}, pi_1 {4*A/SQN:.5f}")
    gs, gm = G_major(s8), G_major(M0)
    print(f"Taylor majorant: G(2sqrt2) = {gs:.5f}, G(M0)-G(2sqrt2) = {gm-gs:.5f}")
    print(f"crude dimension total = {seed_dim + 2*A/SQN + gm:.5f}")
    # budget left for h-dependent terms in pi_1 if the seed-only Taylor part is charged
    # at its dimension majorant (lower estimate) or doubled (z' <= r'):
    b = (1 - seed_pi1) - one
    print(f"pi_1 one-step budget {b:.5f}; minus seed-only Taylor at dimension cost: {b-gs:.5f}; "
          f"if doubled: {b-2*gs:.5f}; implied rho*A(h) limit {(b-gs)*SQN:.4f} / {(b-2*gs)*SQN:.4f}")
    assert F(1066, 1000) ** 80 > 2 ** 7
    print("1.066^80 > 2^7 exactly: True")


# ---------------------------------------------------------------- Part 2
def child(f1, f2, e):
    # e=+1: J shifts (-1,+1); e=-1: J^-1 shifts (+1,-1)
    s1 = [w - e for w in f1]
    s2 = [w + e for w in f2]
    tot = sum(abs(w) for w in s1) + sum(abs(w) for w in s2)
    assert tot % 2 == 0
    r2 = tot // 2
    n1 = [w for w in s1 if w < 0] + [w for w in s2 if w > 0]
    n2 = [w for w in s2 if w < 0] + [w for w in s1 if w > 0]
    if len(n1) > r2 or len(n2) > r2:
        return None
    return tuple(sorted(n1 + [0] * (r2 - len(n1)))), tuple(sorted(n2 + [0] * (r2 - len(n2))))


def pi(f1, f2, alpha):
    r = len(f1)
    Z = f1.count(0) + f2.count(0)
    return F(r) + alpha * F(Z, 2)


def configs(r):
    vals = range(-2 * r, 2 * r + 1)
    fib = {}
    for ms in combinations_with_replacement(vals, r):
        s = sum(abs(w) for w in ms)
        if s <= 2 * r:
            fib.setdefault(s, []).append(ms)
    for s, L1 in fib.items():
        for f1 in L1:
            for f2 in fib.get(2 * r - s, []):
                yield f1, f2


def part2(RMAX=4, MMAX=3):
    Gup = {0: {1: F(4), 2: F(12), 3: F(36)}, F(1, 2): {1: F(10, 3), 2: F(10), 3: F(88, 3)},
           1: {1: F(3), 2: F(9), 3: F(26)}}
    best = {a: {m: (F(0), None) for m in range(1, MMAX + 1)} for a in Gup}
    skipped = 0
    total = 0
    for r in range(2, RMAX + 1):
        for f1, f2 in configs(r):
            total += 1
            layer = [(f1, f2)]
            ok = True
            for m in range(1, MMAX + 1):
                nxt = []
                for (a1, a2) in layer:
                    for e in (1, -1):
                        c = child(a1, a2, e)
                        if c is None:
                            ok = False
                            break
                        nxt.append(c)
                    if not ok:
                        break
                if not ok:
                    skipped += 1
                    break
                layer = nxt
                for a in Gup:
                    val = sum(pi(x, y, F(a)) for x, y in layer) / pi(f1, f2, F(a))
                    if val > best[a][m][0]:
                        best[a][m] = (val, (f1, f2))
    print(f"Round 80 rule brute force: {total} parent configurations, r=2..{RMAX}; "
          f"{skipped} stopped early (negative refill)")
    for a in Gup:
        for m in range(1, MMAX + 1):
            v, cfg = best[a][m]
            assert v <= Gup[a][m], (a, m, v, cfg)
            print(f"  alpha={str(F(a)):>3s} m={m}: max ratio found {float(v):8.4f} <= reported G_up "
                  f"{float(Gup[a][m]):8.4f}   argmax {cfg}")


if __name__ == "__main__":
    part1()
    part2()
    print("ALL AUDIT CHECKS OK")
