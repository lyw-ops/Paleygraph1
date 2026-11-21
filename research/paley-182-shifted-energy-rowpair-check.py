"""Round 182 (call ordinary-prime-shifted-level-energy): exact finite checks.

Part A (exact, Fraction arithmetic, p = 13, 17, 29, 37, 41):
  For random inversion-symmetric g on Q with g(1)=1 and values in [0,1]:
  A1  the Round 178/180 chart sum M_w = sum_s w(s) P_s equals the row-pair
      formula over kappa = 1-r (bijection chart <-> (kappa, P, P'));
  A2  on every row R_kappa the masks b != 1 and s != b are vacuous
      (Y - kappa D = 1 - kappa = A - kappa C), and s = 1 iff P = P';
  A3  on every row, the ratio Y/D determines the pair P (used for the
      Parseval step of the multiplicative Fourier formula for M_w);
  A4  M_w <= (E_Q(h) - diag)/4 <= E^x(h)/4, with h(z) = g(1-z).
  The same identity A1 is also checked with an arbitrary weight in place of w.
Part B (exact modular arithmetic): the incidence encoding of Lemma SE.
  For random B, V in F_p^* \\ {1} (|B| = |V|), the map
  (u, v, x, y) -> (line l_{u,v}: Z = v(uX + 1 - u), point (x, v y))
  over all row solutions 1 - y = u (1 - x), x,y in B, v in V, is injective,
  the point lies on the line, and (u,v) -> (slope, intercept) is injective.
Part C (floating diagnostics only): for g = |f|^2 with f the Fourier row of a
  random probability nu on the character group of Q, the Jacobi bound
  |sum_{x != 0,1} g(x) chi(1-x)| <= sqrt(p) for every nontrivial chi, and the
  Fourier inequality M_w <= G E_Q/(p-1) + max_{chi!=1}|w^(chi)| * Gamma_2^2.

Replay: python3 -B research/paley-182-shifted-energy-rowpair-check.py
Standard library only; memory use is small (p <= 101).
"""
import cmath
import math
import random
from collections import defaultdict
from fractions import Fraction as F
from itertools import product


def inv(a, p):
    return pow(a % p, -1, p)


def squares(p):
    return {x * x % p for x in range(1, p)}


def chart_terms(p, g, wt):
    """Direct chart: s, b in Q\\{1}, r not in {0,1}, s != b, labels in Q\\{1}."""
    Q = squares(p)
    QQ = Q - {1}
    M = 0
    cnt = 0
    for s in QQ:
        for r, b in product(range(2, p), QQ):
            if s == b:
                continue
            A = r * s * inv(s - b, p) % p
            C = r * b * inv((1 - r) * (s - b), p) % p
            Y = r * inv(1 - b, p) % p
            D = r * b * inv((1 - r) * (1 - b), p) % p
            if not {A, C, Y, D} <= QQ:
                continue
            cnt += 1
            M += wt[s] * g[A] * g[C] * g[Y] * g[D]
    return M, cnt


def rows(p):
    Q = squares(p)
    QQ = Q - {1}
    R = defaultdict(list)
    for Y in QQ:
        for D in QQ:
            if Y == D:
                continue
            k = (1 - Y) * inv(1 - D, p) % p
            R[k].append((Y, D))
    return R


def row_terms(p, g, wt):
    Q = squares(p)
    R = rows(p)
    M = 0
    cnt = 0
    for k, L in R.items():
        if k not in Q:
            continue
        for (Y, D) in L:
            # A2: masks vacuous
            assert (Y - k * D) % p == (1 - k) % p and (1 - k) % p != 0
            for (A, C) in L:
                assert (A - k * C) % p == (1 - k) % p
                s = A * D * inv(C * Y, p) % p
                assert (s == 1) == ((A, C) == (Y, D))
                if s == 1:
                    continue
                cnt += 1
                M += wt[s] * g[Y] * g[D] * g[A] * g[C]
        # A3: Y/D injective on the row
        ratios = [Y * inv(D, p) % p for (Y, D) in L]
        assert len(set(ratios)) == len(ratios)
    return M, cnt


def energies(p, g):
    """E_Q(h), its diagonal, and full E^x(h), h(z) = g(1-z) on F_p^*."""
    Q = squares(p)
    h = {z: g[(1 - z) % p] for z in range(1, p)}  # g(0) = 0 convention
    EQ = 0
    Ex = 0
    for k in range(1, p):
        m = sum(h[z] * h[k * z % p] for z in range(1, p))
        Ex += m * m
        if k in Q and k != 1:
            EQ += m * m
    R = rows(p)
    diag = 0
    for k, L in R.items():
        if k in Q:
            diag += sum((g[Y] * g[D]) ** 2 for (Y, D) in L)
    return EQ, diag, Ex


def partA():
    rnd = random.Random(182)
    for p in (13, 17, 29, 37, 41):
        Q = squares(p)
        g = [F(0)] * p
        for x in Q:
            if x == 1:
                g[x] = F(1)
            elif x <= inv(x, p):
                v = F(rnd.randint(0, 8), 8)
                g[x] = v
                g[inv(x, p)] = v
        w = [g[x] * (1 - g[x]) for x in range(p)]
        w2 = [F(rnd.randint(0, 9), 7) if x in Q else F(0) for x in range(p)]
        for wt in (w, w2):
            a, ca = chart_terms(p, g, wt)
            b, cb = row_terms(p, g, wt)
            assert a == b and ca == cb, (p, a, b, ca, cb)
        Mw, cnt = chart_terms(p, g, w)
        EQ, diag, Ex = energies(p, g)
        assert 4 * Mw <= EQ - diag <= Ex
        print(f"A p={p}: chart==rows ({cnt} tuples), masks vacuous, s=1<->P=P', "
              f"Y/D injective, 4M_w={float(4*Mw):.4f} <= E_Q-diag={float(EQ-diag):.4f} "
              f"<= E^x(h)={float(Ex):.4f}  OK")


def partB():
    rnd = random.Random(1822)
    for p in (31, 61, 101):
        pool = list(range(2, p))
        for trial in range(3):
            N = rnd.randint(4, 9)
            B = rnd.sample(pool, N)
            V = rnd.sample(range(1, p), N)
            seen = {}
            lines = {}
            for x in B:
                for y in B:
                    if x == y:
                        continue
                    u = (1 - y) * inv(1 - x, p) % p
                    for v in V:
                        slope, icpt = v * u % p, v * (1 - u) % p
                        key_l = (slope, icpt)
                        assert lines.setdefault(key_l, (u, v)) == (u, v)
                        pt = (x, v * y % p)
                        assert (slope * pt[0] + icpt - pt[1]) % p == 0
                        key = (key_l, pt)
                        assert key not in seen, "incidence map not injective"
                        seen[key] = (u, v, x, y)
        print(f"B p={p}: incidence encoding injective, lines distinct  OK")


def dlog_table(p):
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
    gen = next(a for a in range(2, p) if all(pow(a, m // f, p) != 1 for f in fac))
    lg = [0] * p
    t = 1
    for k in range(m):
        lg[t] = k
        t = t * gen % p
    return gen, lg


def partC():
    rnd = random.Random(18203)
    for p, model in ((29, "random"), (53, "random"), (101, "random"),
                     (29, "interval"), (53, "interval"), (101, "interval")):
        n = (p - 1) // 2
        gen, lg = dlog_table(p)
        # characters of Q = <gen^2>: eta_j(gen^(2k)) = e(jk/n); symmetric nu => real f
        nu = [0.0] * n
        L = max(2, int(math.isqrt(p)))
        if model == "random":
            support = rnd.sample(range(n), L)
        else:  # interval of characters: Fejer-type bump of g on a log-interval
            support = list(range(L))
        for j in support:
            nu[j] += 1.0
            nu[(-j) % n] += 1.0
        tot = sum(nu)
        nu = [x / tot for x in nu]
        g = [0.0] * p
        for x in range(1, p):
            if lg[x] % 2 == 0:
                k = lg[x] // 2
                f = sum(nu[j] * cmath.exp(2j * math.pi * j * k / n) for j in range(n))
                g[x] = abs(f) ** 2
        assert abs(g[1] - 1) < 1e-9
        G = sum(g)
        w = [gx * (1 - gx) for gx in g]
        worst = 0.0
        what = 0.0
        for a in range(1, p - 1):  # nontrivial characters chi_a(gen^k) = e(ak/(p-1))
            hh = sum(g[x] * cmath.exp(2j * math.pi * a * lg[(1 - x) % p] / (p - 1))
                     for x in range(2, p) if g[x] != 0)
            worst = max(worst, abs(hh) ** 2 / p)
            ww = sum(w[s] * cmath.exp(2j * math.pi * a * lg[s] / (p - 1))
                     for s in range(1, p) if w[s] != 0)
            what = max(what, abs(ww))
        Mw, _ = row_terms(p, g, w)
        EQ, diag, Ex = energies(p, g)
        Gam2 = sum(g[x] ** 2 for x in range(2, p))
        rhs = G * EQ / (p - 1) + what * Gam2 ** 2
        print(f"C p={p} {model:8s}: max_chi!=1 |h^(chi)|^2/p = {worst:.4f} (<=1), "
              f"M_w={Mw:.4f} <= Fourier bound {rhs:.4f}; E^x(h)={Ex:.3f} <= "
              f"G^4/(p-1)+p*Gamma_2 = {(G-1)**4/(p-1)+p*Gam2:.3f}")
        assert worst <= 1 + 1e-9 and Mw <= rhs + 1e-9
        assert Ex <= (G - 1) ** 4 / (p - 1) + p * Gam2 + 1e-6


if __name__ == "__main__":
    partA()
    partB()
    partC()
    print("ALL OK")
