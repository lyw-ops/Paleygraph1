#!/usr/bin/env python3
r"""Round 182 (call ordinary-prime-one-match-operator-norm): model diagnostics.

FLOATING-POINT EVIDENCE ONLY (power iteration); the exact columns (M1, HS2, E2 = sum
sigma^4) are integers.  The weights g are AUXILIARY MODELS, not the actual optimiser.

Chart: actual Round 171 one-match chart, r = (Y-D)/(1-D), b = D(1-Y)/(Y(1-D)),
Y, D in Q \ {1}, Y != D, mask b in Q, mu(r,b) = g(Y) g(D), K(y,x) = sum_{rx+b=y} mu.
pi(mu) = K restricted to mean-zero vectors (K maps 1-perp to 1-perp).

Primes p = q^2 + 1 with q even, so the subgroup H of order q lies in Q.
Models (all 0/1 weights with |supp g| = q ~ sqrt p, so G = q, sum g^2 = q):
  subgroup : g = 1_H, H <= F_p^* of order q
  geom     : g = 1 on {gamma^(2i) : 1 <= i <= q}  (log-interval / approximate subgroup)
  random   : g = 1 on a random q-subset of Q \ {1}  (seed 182)
  interval : g = 1 on the first q squares in [2, p)  (additive structure)
Columns:
  M1, HS2 = p sum mu^2 - sum m^2 = sum sigma^2, E2 = p T_2(mu) - T_2^x(m) = sum sigma^4
  row1   = || K(1,.) - M1/p || / sqrt(1-1/p)  (exact lower bound for sigma_1, Prop. 3)
  s1     = sigma_1(pi(mu))                     (power iteration, 1-perp)
  s1'    = sigma_1(R pi(mu)), R deletes output rows s = 0, 1 (physical criterion)
  ratios to p^(3/4); 'E2^(1/4)' is the k=2 trace-moment upper bound for s1.
Replay:  python3 research/paley-182-opnorm-models.py            (q = 20, 26, 36, 40)
         python3 research/paley-182-opnorm-models.py 20 26 36 40 54
Memory: two dense p x p arrays of doubles (about 136 MB at q = 54).
"""
import math
import random
import sys
from array import array
from operator import mul


def is_prime(n):
    return n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))


def legendre(a, p):
    a %= p
    return 0 if a == 0 else (1 if pow(a, (p - 1) // 2, p) == 1 else -1)


def primitive_root(p):
    fac = [d for d in range(2, p) if (p - 1) % d == 0 and is_prime(d)]
    for g in range(2, p):
        if all(pow(g, (p - 1) // f, p) != 1 for f in fac):
            return g


def model_support(name, p, q):
    Q = [x for x in range(2, p) if legendre(x, p) == 1]
    if name == 'subgroup':
        gam = primitive_root(p)
        h = pow(gam, (p - 1) // q, p)
        S = {pow(h, i, p) for i in range(q)}
        S.discard(1)
        return sorted(S)
    if name == 'geom':
        gam = primitive_root(p)
        return sorted({pow(gam, 2 * i, p) for i in range(1, q + 1)} - {1})
    if name == 'random':
        return sorted(random.Random(182).sample(Q, q))
    if name == 'interval':
        return Q[:q]
    raise ValueError(name)


def build(p, S):
    inv = lambda z: pow(z, p - 2, p)
    Sset = set(S)
    mu = []
    for Y in S:
        for D in S:
            if D == Y:
                continue
            b = D * (1 - Y) * inv(Y * (1 - D) % p) % p
            if legendre(b, p) != 1:
                continue
            r = (Y - D) * inv(1 - D) % p
            mu.append((r, b))
    return mu


def exact_moments(p, mu):
    """M1, HS2 = p T1 - T1x, E2 = p T2 - T2x for 0/1 weight mu (integers)."""
    inv = lambda z: pow(z, p - 2, p)
    M1 = len(mu)
    m = {}
    for r, b in mu:
        m[r] = m.get(r, 0) + 1
    T1 = M1
    T1x = sum(v * v for v in m.values())
    # Delta(h) = #{(j1,j2): j1^{-1} j2 = h}, T2 = sum Delta^2
    Delta = {}
    invs = [(inv(r), (-b * inv(r)) % p) for r, b in mu]
    for (ri, bi) in invs:
        for (r2, b2) in mu:
            k = (ri * r2 % p, (ri * b2 + bi) % p)
            Delta[k] = Delta.get(k, 0) + 1
    T2 = sum(v * v for v in Delta.values())
    C = {}
    for r1, w1 in m.items():
        ir = inv(r1)
        for r2, w2 in m.items():
            k = ir * r2 % p
            C[k] = C.get(k, 0) + w1 * w2
    T2x = sum(v * v for v in C.values())
    return M1, p * T1 - T1x, p * T2 - T2x


def dense(p, mu):
    K = [array('d', bytes(8 * p)) for _ in range(p)]
    for r, b in mu:
        y = b
        for x in range(p):
            K[y][x] += 1.0
            y += r
            if y >= p:
                y -= p
    Kt = [array('d', col) for col in zip(*K)]
    return K, Kt


def top_sv(p, K, Kt, drop, iters=80, seed=1):
    """Power iteration for sigma_1 of R K on 1-perp; R zeroes output rows in drop."""
    rng = random.Random(seed)
    v = [rng.gauss(0, 1) for _ in range(p)]
    hist = []
    for _ in range(iters):
        mbar = sum(v) / p
        v = [x - mbar for x in v]
        nv = math.sqrt(sum(x * x for x in v))
        v = [x / nv for x in v]
        u = [sum(map(mul, row, v)) for row in K]
        for s in drop:
            u[s] = 0.0
        sig = math.sqrt(sum(x * x for x in u))
        hist.append(sig)
        v = [sum(map(mul, col, u)) for col in Kt]
    return hist[-1], hist[-1] - hist[-6], v


def run(q, models):
    p = q * q + 1
    assert is_prime(p) and q % 2 == 0, (q, p)
    P34 = p ** 0.75
    print(f"\np = {p} (q = {q}),  p^(3/4) = {P34:.2f}")
    print(f"{'model':9s} {'M1':>6s} {'HS2/p^2':>8s} {'E2/p^3':>8s} {'E2^(1/4)/p^.75':>14s}"
          f" {'row1/p^.75':>10s} {'s1/p^.75':>9s} {'s1prime/p^.75':>13s} {'conv':>8s}")
    for name in models:
        S = model_support(name, p, q)
        mu = build(p, S)
        M1, HS2, E2 = exact_moments(p, mu)
        K, Kt = dense(p, mu)
        row = K[1]
        row1 = math.sqrt(sum((x - M1 / p) ** 2 for x in row) / (1 - 1 / p))
        s1, d1, _ = top_sv(p, K, Kt, ())
        s1p, d1p, _ = top_sv(p, K, Kt, (0, 1))
        print(f"{name:9s} {M1:6d} {HS2 / p**2:8.4f} {E2 / p**3:8.4f} {E2 ** 0.25 / P34:14.4f}"
              f" {row1 / P34:10.4f} {s1 / P34:9.4f} {s1p / P34:13.4f} {max(d1, d1p):8.1e}")
        del K, Kt


if __name__ == '__main__':
    qs = [int(a) for a in sys.argv[1:]] or [20, 26, 36, 40]
    for q in qs:
        run(q, ['subgroup', 'geom', 'random', 'interval'])
