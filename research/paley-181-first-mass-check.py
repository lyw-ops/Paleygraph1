"""Round 181 candidate checks for the weighted first mass M_w = sum_s w(s) P_s.

Part 1 (exact, Fractions): the chart sum over (s,r,b) equals the row-pair
(energy) formula over kappa=1-r, on random inversion-symmetric g on Q.
Part 2 (floating diagnostics): subgroup-mixture models g = 1_H + 1/4 1_{xH u x^-1 H}
that satisfy the proved cap n*max(nu) <= 2|H|, versus random sets of equal mass.
Plain python3 standard library only.
"""
import random
import sys
from fractions import Fraction as F
from itertools import product
from collections import defaultdict


def inv(a, p):
    return pow(a % p, -1, p)


def squares(p):
    return {x * x % p for x in range(1, p)}


def chart_mass(p, g):
    """Direct Round 178/180 chart: s,b in Q\\{1}, r not in {0,1}, s!=b, labels in Q\\{1}."""
    Q = squares(p)
    w = {x: g[x] * (1 - g[x]) for x in g}
    M = 0
    for s in Q - {1}:
        Ps = 0
        for r, b in product(range(2, p), Q - {1}):
            if s == b:
                continue
            A = r * s * inv(s - b, p) % p
            C = r * b * inv((1 - r) * (s - b), p) % p
            Y = r * inv(1 - b, p) % p
            D = r * b * inv((1 - r) * (1 - b), p) % p
            if not {A, C, Y, D} <= Q - {1}:
                continue
            Ps += g[A] * g[C] * g[Y] * g[D]
        M += w[s] * Ps
    return M


def row_mass(p, g, wfun=None, kappa_in_Q=True):
    """Row-pair formula: sum over kappa in Q\\{1} of pairs (Y,D),(A,C) on the row
    1-Y=kappa(1-D), 1-A=kappa(1-C), weight g(Y)g(D)g(A)g(C)w(AD/(CY)), mask kappa*D != Y.
    Returns (M_w, E_masked, rowmass_total) where E_masked drops w (w<=1)."""
    Q = squares(p)
    supp = [x for x in g if x != 1 and g[x] > 0]
    rows = defaultdict(list)
    for Y in supp:
        for D in supp:
            if Y == D:
                continue
            k = (1 - Y) * inv(1 - D, p) % p
            if kappa_in_Q and k not in Q:
                continue
            rows[k].append((Y, D, g[Y] * g[D]))
    M = 0
    E = 0
    tot = 0
    for k, L in rows.items():
        good = [(Y, D, m) for (Y, D, m) in L if k * D % p != Y]  # b != 1
        for (Y, D, m) in good:
            tot += m
            for (A, C, m2) in good:
                s = A * D * inv(C * Y, p) % p
                E += m * m2
                if wfun is not None:
                    M += m * m2 * wfun(s)
    return M, E, tot


def part1():
    rnd = random.Random(181)
    for p in (13, 17, 29, 37, 41):
        Q = squares(p)
        g = {x: F(0) for x in range(1, p)}
        for x in Q:
            if x == 1:
                g[x] = F(1)
            elif x < inv(x, p):
                v = F(rnd.randint(0, 8), 8)
                g[x] = v
                g[inv(x, p)] = v
            elif x == inv(x, p):
                g[x] = F(rnd.randint(0, 8), 8)
        M1 = chart_mass(p, g)
        M2, _, _ = row_mass(p, g, wfun=lambda s: g[s] * (1 - g[s]))
        assert M1 == M2, (p, M1, M2)
        print(f"part1 p={p}: chart sum == row-pair formula == {float(M1):.4f}")


def subgroup_model(p, d, rnd):
    """Return g on F_p^* for H<Q of order d and x in Q with x^2 not in H."""
    Q = squares(p)
    n = (p - 1) // 2
    # generator of F_p^*
    fac = []
    m = p - 1
    q = 2
    while q * q <= m:
        if m % q == 0:
            fac.append(q)
            while m % q == 0:
                m //= q
        q += 1
    if m > 1:
        fac.append(m)
    gen = next(a for a in range(2, p) if all(pow(a, (p - 1) // f, p) != 1 for f in fac))
    h = pow(gen, (p - 1) // d, p)
    H = set()
    t = 1
    for _ in range(d):
        H.add(t)
        t = t * h % p
    assert len(H) == d and H <= Q
    while True:
        x = pow(gen, 2 * rnd.randrange(1, n), p)
        if x * x % p not in H and x not in H:
            break
    g = {y: 0.0 for y in range(1, p)}
    for y in H:
        g[y] = 1.0
        g[y * x % p] = 0.25
        g[y * inv(x, p) % p] = 0.25
    return g, H, x


def model_stats(p, g, label):
    G = sum(g.values())
    w = {y: g[y] * (1 - g[y]) for y in g}
    M, E, tot = row_mass(p, g, wfun=lambda s: w[s])
    print(f"  {label:9s} p={p:7d} G={G:8.1f} G/sqrt(p)={G/p**0.5:5.2f} "
          f"M_w={M:11.1f} M_w/p={M/p:7.3f} M_w/G^2={M/G**2:6.3f} "
          f"E_rows/p={E/p:7.3f} mu-mass/G^2={tot/G**2:5.3f}")
    return M


def part2(maxp, scales=(1000, 4000, 16000, 64000, 256000)):
    rnd = random.Random(1810)
    for sc in scales:
        part2_scale(sc, rnd, 2)


def part2_scale(lo, rnd, want):
    print("part2: subgroup-mixture model (cap n*max nu <= 2|H|) vs random sets of the same sizes")
    done = 0
    for p in range(lo, 10 * lo):
        if p % 4 != 1 or any(p % q == 0 for q in range(2, int(p**0.5) + 1)):
            continue
        n = (p - 1) // 2
        ds = [d for d in range(int(0.7 * p**0.5), int(1.3 * p**0.5) + 1) if n % d == 0]
        if not ds:
            continue
        d = ds[0]
        if n // d < 5:
            continue
        g, H, x = subgroup_model(p, d, rnd)
        model_stats(p, g, f"subgp d={d}")
        # random comparison with identical value multiset, inversion symmetric
        Q = sorted(squares(p) - {1})
        pairs = []
        seen = set()
        for y in Q:
            if y not in seen:
                seen.add(y)
                seen.add(inv(y, p))
                pairs.append((y, inv(y, p)))
        vals = sorted([v for y, v in g.items() if y != 1 and v > 0], reverse=True)
        gr = {y: 0.0 for y in range(1, p)}
        gr[1] = 1.0
        rnd.shuffle(pairs)
        i = 0
        for (a, b) in pairs:
            if i >= len(vals):
                break
            gr[a] = vals[i]
            gr[b] = vals[i]
            i += 1 if a == b else 2
        model_stats(p, gr, "random")
        done += 1
        if done >= want:
            break


if __name__ == "__main__":
    part1()
    part2(int(sys.argv[1]) if len(sys.argv) > 1 else 60000)
