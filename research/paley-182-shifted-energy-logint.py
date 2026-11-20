"""Round 182 (call ordinary-prime-shifted-level-energy): log-interval evidence.

For primes p = 1 mod 4 near each requested scale, let theta generate Q (the
nonzero squares) and P_N = {theta^k : 1 <= k <= N}, N = floor(sqrt(p)).
Compute exactly (integer counts) the shifted multiplicative energy
    E^x(1 - P_N) = sum_{u in F_p^*} m(u)^2,
    m(u) = #{(x, y) in P_N^2 : 1 - y = u (1 - x)},
and compare it with N^2 (near-sharp scale), N^(8/3) (Lemma SE of the Round 182
report) and N^(36/13) (Round 177).  The same is done for a random subset of Q
of the same size.  Also printed: the largest nontrivial row max_{u != 1} m(u).

The counts are exact for each listed prime, but the table is finite evidence
about an asymptotic question, not a proof.

Replay: python3 -B research/paley-182-shifted-energy-logint.py [max_scale]
(default max_scale 1000000; memory is one array of p unsigned ints, about
4p bytes, i.e. ~16 MB at p ~ 4e6).  Standard library only.
"""
import math
import random
import sys
from array import array


def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def generator(p):
    m = p - 1
    fac = []
    q = 2
    mm = m
    while q * q <= mm:
        if mm % q == 0:
            fac.append(q)
            while mm % q == 0:
                mm //= q
        q += 1
    if mm > 1:
        fac.append(mm)
    return next(a for a in range(2, p) if all(pow(a, m // f, p) != 1 for f in fac))


def shifted_energy(p, S, cnt):
    """Exact E^x(1-S) and max nontrivial row; cnt is a reusable zeroed array."""
    S = list(S)
    invs = [pow((1 - x) % p, -1, p) for x in S]
    touched = []
    for x, ix in zip(S, invs):
        for y in S:
            u = (1 - y) * ix % p
            if cnt[u] == 0:
                touched.append(u)
            cnt[u] += 1
    E = 0
    mx = 0
    for u in touched:
        c = cnt[u]
        E += c * c
        if u != 1 and c > mx:
            mx = c
        cnt[u] = 0
    return E, mx


def main(max_scale):
    rnd = random.Random(182)
    scales = [s for s in (1000, 4000, 16000, 64000, 256000, 1000000, 4000000)
              if s <= max_scale]
    print(" p        N     E/N^2   E/N^(8/3)  E/N^(36/13) maxrow   | random: E/N^2  maxrow")
    for sc in scales:
        p = sc + 1
        while not (p % 4 == 1 and is_prime(p)):
            p += 1
        N = int(p ** 0.5)
        while (N + 1) * (N + 1) <= p:
            N += 1
        while N * N > p:
            N -= 1
        g = generator(p)
        th = g * g % p
        P = []
        t = th
        for _ in range(N):
            P.append(t)
            t = t * th % p
        cnt = array("I", bytes(4 * p))
        E, mx = shifted_energy(p, P, cnt)
        Qlist = [pow(th, k, p) for k in rnd.sample(range(1, (p - 1) // 2), N)]
        Er, mxr = shifted_energy(p, Qlist, cnt)
        print(f"{p:8d} {N:5d} {E/N**2:8.4f} {E/N**(8/3):10.5f} {E/N**(36/13):11.5f} "
              f"{mx:6d}   | {Er/N**2:8.4f} {mxr:6d}")
        del cnt
    print("Subgroup-type models: theta of order d dividing (p-1)/2, P = first N powers.")
    print("  'sub'  : N = d (exact subgroup H, d ~ sqrt p);")
    print("  'half' : d ~ 2 sqrt p, N = d/2 (half of a subgroup: an approximate subgroup).")
    print(" p        d     N    kind   E/N^2   E/(N^2 log N)  maxrow")
    for sc in scales:
        for kind, lo, hi in (("sub", 0.7, 1.3), ("half", 1.6, 2.6)):
            p = sc + 1
            while True:
                if p % 4 == 1 and is_prime(p):
                    n = (p - 1) // 2
                    ds = [d for d in range(int(lo * p ** 0.5), int(hi * p ** 0.5) + 1)
                          if n % d == 0 and d >= 4]
                    if ds:
                        break
                p += 1
            d = ds[0]
            g = generator(p)
            th = pow(g, (p - 1) // d, p)
            N = d if kind == "sub" else d // 2
            P = []
            t = th
            for _ in range(N):
                if t != 1:
                    P.append(t)
                t = t * th % p
            cnt = array("I", bytes(4 * p))
            E, mx = shifted_energy(p, P, cnt)
            M = len(P)
            print(f"{p:8d} {d:5d} {M:5d} {kind:5s} {E/M**2:8.4f} {E/(M**2*math.log(M)):10.4f} {mx:9d}")
            del cnt


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 1000000)
