#!/usr/bin/env python3
r"""Round 187, call ordinary-prime-level-pair-energy: exact checks of Lemma M' (popular-quotient form).

Exact integer / Fraction arithmetic, standard library only.  For small primes p and
random or structured sets R, A in F_p \ {0,1} it checks every combinatorial step of
Lemma M' in research/native-claude-ordinary-prime-level-pair-energy-187.md :

  (1) r(w) = #{(y',y) in R^2 : y/y' = w},  sum r = m^2,  sum r^2 = E^x(R)
      (brute-force count of y1*y2' = y2*y1');
  (2) for the dyadic class F = {rho <= r < 2 rho} chosen with sum_F r^2 >= E/L0:
      |F| <= E/rho^2,  P := sum_F r >= E/(2 rho L0),  P >= m^2/(2 K L0);
  (3) d(y) = #{v in R^{-1} : v y in F} <= min(m,|F|),  sum_y d = P,
      B = {y : d(y) >= P/(2m)}:  sum_B d >= P/2,  |B| >= P/(2 min(m,|F|)),
      |B|^2 >= m^2/(16 L0^2 K)  (i.e. |B| >= m/(4 L0 sqrt K));
  (4) the lines l_{u,v}: Z = v(uX+1-u), u in F_p^*, v in R^{-1}, are pairwise distinct,
      nonvertical and nonhorizontal;
  (5) for every h >= 1, with T_h = {u : m_{A,B}(u) >= h}, t = |T_h|: every tuple
      (u,v,x,y), u in T_h, (x,y) in A x B with 1-y = u(1-x), v y in F, gives the point
      (x, v y) in A x F on l_{u,v}; the map is injective; hence
      I(A x F, {l_{u,v}}) >= h t P/(2m)  -- checked against a brute-force incidence count;
  (6) sum_u m_{A,B}(u) = |A||B| and E(A;B) = sum_u m_{A,B}(u)^2 = E(B;A).

Usage:  .venv/bin/python -B research/paley-187-pair-lemma-check.py [p ...]
Default primes: 13 17 29 37 41 53 61 73 89 97.  Prints EXACT CHECKS OK at the end.
"""
import random
import sys
from fractions import Fraction as Fr

ok = True


def check(cond, msg):
    global ok
    if not cond:
        print("FAIL " + msg)
        ok = False
    return cond


def inv(x, p):
    return pow(x, p - 2, p)


def quotient_counts(R, p):
    r = {}
    for y1 in R:
        for y2 in R:
            w = y2 * inv(y1, p) % p
            r[w] = r.get(w, 0) + 1
    return r


def energy_bruteforce(R, p):
    prods = {}
    for a in R:
        for b in R:
            k = a * b % p
            prods[k] = prods.get(k, 0) + 1
    return sum(c * c for c in prods.values())


def row_counts(A, B, p):
    m = {}
    for x in A:
        ix = inv((1 - x) % p, p)
        for y in B:
            u = (1 - y) * ix % p
            m[u] = m.get(u, 0) + 1
    return m


def lemma_steps(R, A, p, tag):
    m = len(R)
    r = quotient_counts(R, p)
    E = sum(c * c for c in r.values())
    check(sum(r.values()) == m * m, f"{tag}: sum r = m^2")
    check(E == energy_bruteforce(R, p), f"{tag}: sum r^2 = E^x(R)")
    K = Fr(m ** 3, E)
    L0 = m.bit_length()  # floor(log2 m) + 1 dyadic classes 2^j <= r < 2^{j+1}, j = 0..floor(log2 m)
    classes = {}
    for w, c in r.items():
        j = c.bit_length() - 1
        classes.setdefault(j, []).append(w)
    check(len(classes) <= L0, f"{tag}: at most L0 dyadic classes")
    j = max(classes, key=lambda jj: sum(r[w] ** 2 for w in classes[jj]))
    Fset = set(classes[j])
    rho = 1 << j
    sF2 = sum(r[w] ** 2 for w in Fset)
    P = sum(r[w] for w in Fset)
    check(sF2 * L0 >= E, f"{tag}: chosen class has sum r^2 >= E/L0")
    check(len(Fset) * rho * rho <= E, f"{tag}: |F| <= E/rho^2")
    check(2 * rho * L0 * P >= E, f"{tag}: P >= E/(2 rho L0)")
    check(Fr(P) >= Fr(m * m) / (2 * K * L0), f"{tag}: P >= m^2/(2 K L0)")
    V = [inv(y, p) for y in R]
    d = {y: sum(1 for v in V if v * y % p in Fset) for y in R}
    check(sum(d.values()) == P, f"{tag}: sum_y d(y) = P")
    check(max(d.values()) <= min(m, len(Fset)), f"{tag}: d <= min(m,|F|)")
    B = [y for y in R if 2 * m * d[y] >= P]
    sB = sum(d[y] for y in B)
    check(2 * sB >= P, f"{tag}: sum_B d >= P/2")
    check(2 * len(B) * min(m, len(Fset)) >= P, f"{tag}: |B| >= P/(2 min(m,|F|))")
    check(Fr(len(B)) ** 2 * 16 * L0 * L0 * K >= m * m, f"{tag}: |B| >= m/(4 L0 sqrt K)")
    # (4) lines
    lines = {}
    for u in range(1, p):
        for v in V:
            key = (v * u % p, v * (1 - u) % p)  # (slope, intercept)
            check(key[0] != 0, f"{tag}: nonhorizontal")
            check(key not in lines, f"{tag}: lines distinct")
            lines[key] = (u, v)
    # (5)/(6)
    mAB = row_counts(A, B, p)
    check(sum(mAB.values()) == len(A) * len(B), f"{tag}: sum_u m = |A||B|")
    check(sum(c * c for c in mAB.values()) == sum(c * c for c in row_counts(B, A, p).values()),
          f"{tag}: E(A;B) = E(B;A)")
    Aset = set(A)
    hmax = max(mAB.values()) if mAB else 0
    for h in range(1, hmax + 1):
        T = [u for u, c in mAB.items() if c >= h]
        t = len(T)
        seen = set()
        cnt = 0
        for u in T:
            for x in A:
                y = (1 - u * (1 - x)) % p
                if y not in d or y not in set(B):
                    continue
                for v in V:
                    w = v * y % p
                    if w not in Fset:
                        continue
                    # point (x, w) on l_{u,v}?
                    check((v * (u * x + 1 - u) - w) % p == 0, f"{tag}: incidence")
                    key = ((v * u % p, v * (1 - u) % p), (x, w))
                    check(key not in seen, f"{tag}: injective")
                    seen.add(key)
                    cnt += 1
        # brute-force incidence count of A x F with the t*m lines
        Ibf = 0
        for u in T:
            for v in V:
                for x in A:
                    z = v * (u * x + 1 - u) % p
                    if z in Fset:
                        Ibf += 1
        check(cnt <= Ibf, f"{tag}: tuples <= incidences")
        check(2 * m * cnt >= h * t * P, f"{tag}: I >= h t P/(2m) at h={h}")
    return dict(m=m, K=float(K), F=len(Fset), P=P, B=len(B), L0=L0)


def main():
    primes = [int(a) for a in sys.argv[1:]] or [13, 17, 29, 37, 41, 53, 61, 73, 89, 97]
    rng = random.Random(187)
    ncase = 0
    for p in primes:
        base = [x for x in range(2, p)]
        Q = sorted({x * x % p for x in range(1, p)} - {1})
        # a primitive root
        g0 = next(gg for gg in range(2, p) if all(pow(gg, (p - 1) // q, p) != 1
                                                    for q in range(2, p) if (p - 1) % q == 0 and all(q % s for s in range(2, q))))
        cases = []
        for _ in range(4):
            R = rng.sample(base, rng.randint(2, max(2, (p - 2) // 2)))
            A = rng.sample(base, rng.randint(1, max(1, (p - 2) // 2)))
            cases.append(("random", R, A))
        # geometric progressions (multiplicatively structured) and squares
        for L in (3, max(3, p // 4), max(3, p // 3)):
            R = sorted({pow(g0, k, p) for k in range(1, L + 1)} - {1})
            A = rng.sample(base, rng.randint(1, max(1, (p - 2) // 2)))
            cases.append(("GP", R, A))
        cases.append(("Q", Q, Q))
        # GP plus random junk
        GP = {pow(g0, 2 * k, p) for k in range(1, max(3, p // 6))} - {1}
        junk = set(rng.sample(base, max(1, p // 8)))
        cases.append(("GP+junk", sorted(GP | junk), rng.sample(base, max(1, p // 3))))
        for name, R, A in cases:
            R = [x for x in R if x not in (0, 1)]
            A = [x for x in A if x not in (0, 1)]
            if len(R) < 1 or len(A) < 1:
                continue
            info = lemma_steps(R, A, p, f"p={p} {name}")
            ncase += 1
        print(f"p={p}: {len(cases)} cases checked; last: {info}")
    print(f"{ncase} cases")
    print("EXACT CHECKS OK" if ok else "SOME CHECKS FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
