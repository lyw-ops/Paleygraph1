#!/usr/bin/env python3
"""Round 189 audit (session/r189-audit): independent checks of the T0 report
`native-claude-ordinary-prime-intercept-fibre-t0-189.md`.  Own implementation; imports no report script.

Part A  (exact integers)  chart built directly from pairs (Y, D); Proposition 1 (i)-(iii); r = (1-b)Y.
Part B  (exact Fractions) Lemma 2 identities and inequality, Corollary 2.1 (CPL, ICR), Proposition 5,
                          the half-structured Cauchy-Schwarz identity sum_{kappa != 1, eps} c_eps^2 = X + 2 c_+(1) c_-(1).
Part C  (exact integers)  subgroup laws: T0 = X and anharmonic invariance; F_{r^2} control with H = F_r^x.
Part D  (floating)        interval (Fejer) law: min g on I/I >= 4/pi^2, T0(g_J) >= (4/pi^2)^5 X(1_I);
                          masked X(1_I) against the full energy E^x(I - 1) (the reduction of Corollary 3.1 to
                          the unmasked energy); E^x(I-1)/|I|^2 and /|I|^{5/2} for geometric progressions (evidence).
Part E  (exact Fractions) every exponent used in the audit.
Replay: .venv/bin/python -B research/paley-189-audit-t0-check.py     (about 1 minute)
"""
import math
import random
import sys
from collections import defaultdict
from fractions import Fraction as Fr

OK = True


def check(name, cond):
    global OK
    OK &= bool(cond)
    print(f"  [{'OK' if cond else 'FAIL'}] {name}")


def prim_root(p):
    fac = [q for q in range(2, p) if (p - 1) % q == 0 and all(q % r for r in range(2, int(q ** .5) + 1))]
    for g in range(2, p):
        if all(pow(g, (p - 1) // q, p) != 1 for q in fac):
            return g


# ---------------------------------------------------------------- generic chart over a field given by ops
class Fp:
    def __init__(self, p):
        self.p = p
        self.els = list(range(p))
        self.zero, self.one = 0, 1

    def add(self, a, b): return (a + b) % self.p
    def sub(self, a, b): return (a - b) % self.p
    def mul(self, a, b): return a * b % self.p
    def inv(self, a): return pow(a, self.p - 2, self.p)
    def div(self, a, b): return a * pow(b, self.p - 2, self.p) % self.p
    def is_sq(self, a): return a != 0 and pow(a, (self.p - 1) // 2, self.p) == 1


class Fq2:
    """F_{r^2} = F_r[i]/(i^2 - nr), nr a non-residue mod r; elements (x, y) -> x + y i."""

    def __init__(self, r):
        self.r = r
        self.nr = next(a for a in range(2, r) if pow(a, (r - 1) // 2, r) == r - 1)
        self.els = [(x, y) for x in range(r) for y in range(r)]
        self.zero, self.one = (0, 0), (1, 0)
        self.q = r * r

    def add(self, a, b): return ((a[0] + b[0]) % self.r, (a[1] + b[1]) % self.r)
    def sub(self, a, b): return ((a[0] - b[0]) % self.r, (a[1] - b[1]) % self.r)
    def mul(self, a, b):
        r = self.r
        return ((a[0] * b[0] + self.nr * a[1] * b[1]) % r, (a[0] * b[1] + a[1] * b[0]) % r)

    def pw(self, a, e):
        res, base = self.one, a
        while e:
            if e & 1:
                res = self.mul(res, base)
            base = self.mul(base, base)
            e >>= 1
        return res

    def inv(self, a): return self.pw(a, self.q - 2)
    def div(self, a, b): return self.mul(a, self.inv(b))
    def is_sq(self, a): return a != self.zero and self.pw(a, (self.q - 1) // 2) == self.one


def chart(F, g):
    """mu as dict (r, b) -> g(Y) g(D), built from all pairs Y != D in F minus {0,1} with b = u_Y/u_D a square."""
    mu = {}
    nb = [x for x in F.els if x not in (F.zero, F.one)]
    u = {x: F.div(F.sub(F.one, x), x) for x in nb}
    bad = 0
    for Y in nb:
        gy = g.get(Y, 0)
        if not gy:
            continue
        for D in nb:
            if D == Y:
                continue
            gd = g.get(D, 0)
            if not gd:
                continue
            b = F.div(u[Y], u[D])
            if not F.is_sq(b):
                continue
            r = F.div(F.sub(Y, D), F.sub(F.one, D))
            if r != F.mul(F.sub(F.one, b), Y):
                bad += 1
            key = (r, b)
            assert key not in mu          # the map (Y, D) -> (r, b) is injective
            mu[key] = gy * gd
    return mu, bad


def chart_quantities(F, g, mu):
    """Delta(lambda, 0) for all lambda, T0 = sum g(lambda) Delta, X = sum_b m'(b)^2, c = sum mu^2."""
    byb = defaultdict(dict)
    for (r, b), v in mu.items():
        byb[b][r] = v
    Delta = defaultdict(int)
    X = 0
    for b, row in byb.items():
        items = list(row.items())
        X += sum(v for _, v in items) ** 2
        for r1, v1 in items:
            for r2, v2 in items:
                Delta[F.div(r2, r1)] += v1 * v2
    T0 = sum(g.get(l, 0) * d for l, d in Delta.items())
    c = sum(v * v for v in mu.values())
    return Delta, T0, X, c


def kappa_form(p, g):
    """Proposition 1 right-hand sides, from psi(x) = g(1+x) only."""
    psi = {x: g.get((1 + x) % p, 0) for x in range(1, p)}
    psi = {x: v for x, v in psi.items() if v}
    sq = lambda a: pow(a, (p - 1) // 2, p) == 1
    ce = {}
    for k in range(1, p):
        cp = cm = 0
        for z, v in psi.items():
            w = psi.get(k * z % p, 0)
            if w:
                if sq(z):
                    cp += v * w
                else:
                    cm += v * w
        ce[k] = (cp, cm)
    A = {}
    for k in range(1, p):
        ap = am = 0
        for x, v in psi.items():
            w = psi.get(k * x % p, 0)
            if not w:
                continue
            tri = g.get((1 + k * x) * pow(1 + x, p - 2, p) % p, 0)
            if sq(x):
                ap += v * w * tri
            else:
                am += v * w * tri
        A[k] = (ap, am)
    Z = 0
    for x, v in psi.items():
        for x2, v2 in psi.items():
            Z += v * v * v2 * v2 * g.get((1 + x) * pow(1 + x2, p - 2, p) % p, 0)
    T0k = sum(ce[k][0] * A[k][0] + ce[k][1] * A[k][1] for k in ce) - Z
    ck = ce[1][0] ** 2 + ce[1][1] ** 2 - sum(v ** 4 for v in psi.values())
    Xk = sum((ce[b][0] + ce[b][1]) ** 2 for b in range(2, p) if sq(b))
    return psi, ce, A, Z, T0k, ck, Xk


def random_symmetric_weight(p, rng, vals, density):
    Q = [x for x in range(1, p) if pow(x, (p - 1) // 2, p) == 1]
    g = {}
    for x in Q:
        y = pow(x, p - 2, p)
        if x <= y and rng.random() < density:
            v = rng.choice(vals)
            g[x] = v
            g[y] = v
    g[1] = vals[-1]
    return g


print("Part A: Proposition 1 from an independent chart (exact integers)")
rng = random.Random(18901)
cnt = 0
for p in (13, 17, 29, 37, 41, 53):
    F = Fp(p)
    for trial in range(3):
        g = random_symmetric_weight(p, rng, [1, 2, 3, 5], 0.6)
        mu, bad = chart(F, g)
        Delta, T0, X, c = chart_quantities(F, g, mu)
        psi, ce, A, Z, T0k, ck, Xk = kappa_form(p, g)
        g1 = g[1]
        # (i) is stated with g(1) = 1; for general g(1) the kappa = 1 term carries g(1): check the general form
        # T0 = sum_kappa sum_eps c_eps A_eps - Z directly (it does not use g(1) = 1).
        good = (bad == 0 and T0 == T0k and X == Xk and c == ck and sum(Delta.values()) == X)
        cnt += good
        if not good:
            print("   mismatch", p, trial, bad, T0, T0k, X, Xk, c, ck)
check("r = (1-b)Y on the chart; (i) T0, (ii) c, (iii) X and sum_lambda Delta(lambda,0) = X agree, 18 weights, p <= 53",
      cnt == 18)

print("Part B: Lemma 2, Corollary 2.1, Proposition 5, the CS identity (exact Fractions, 0 <= g <= 1, g(1) = 1)")
nB = 0
okB = True
for p in (29, 37, 41, 53, 61):
    for trial in range(3):
        g = random_symmetric_weight(p, rng, [Fr(1, 3), Fr(1, 2), Fr(3, 4), Fr(1)], 0.5)
        psi, ce, A, Z, T0k, ck, Xk = kappa_form(p, g)
        chi = lambda a: 1 if pow(a, (p - 1) // 2, p) == 1 else -1
        idx = {1: 0, -1: 1}
        cpl = icr = 0
        for k in range(2, p):
            for eps in (1, -1):
                a = A[k][idx[eps]]
                c1 = ce[k][idx[eps]]
                c2 = ce[(1 - k) % p][idx[eps]]
                c3 = ce[(1 - pow(k, p - 2, p)) % p][idx[chi(k) * eps]]
                okB &= a <= c1 and a <= c2 and a <= c3
                cpl += c1 * min(c1, c2, c3)
                icr += c1 * c2
                # identity through the z-parametrization (pair on slope 1 - kappa, third factor psi(kappa x))
                s2 = 0
                for z, v in psi.items():
                    if chi(z) != eps:
                        continue
                    w = psi.get((1 - k) * z % p, 0)
                    if not w:
                        continue
                    x = (-z) * pow(1 + z, p - 2, p) % p            # inverse Moebius map
                    s2 += v * w * psi.get(k * x % p, 0)
                okB &= (s2 == a)
        T0c = T0k - ck
        okB &= (T0c <= cpl <= icr)
        # Proposition 5 for theta: split by g(lambda) >= tau, using Delta from the chart
        mu, _ = chart(Fp(p), g)
        Delta, T0, X, c = chart_quantities(Fp(p), g, mu)
        okB &= (T0 == T0k)
        tau = Fr(1, 2)
        heavy = sum(g.get(l, 0) * d for l, d in Delta.items() if l != 1 and g.get(l, 0) >= tau)
        okB &= (T0 - c <= tau * X + heavy)
        # CS identity
        lhs = sum(ce[k][0] ** 2 + ce[k][1] ** 2 for k in range(2, p))
        okB &= (lhs == X + 2 * ce[1][0] * ce[1][1])
        nB += 1
check(f"Lemma 2 identity (slope 1-kappa) and A <= min(three pencils); T0 - c <= CPL <= ICR; Prop. 5; "
      f"sum_(kappa!=1) c_eps^2 = X + 2c_+(1)c_-(1)  ({nB} weights)", okB and nB == 15)

print("Part C: subgroup laws over F_p and the F_{r^2} control (exact)")
okC = True
for p, d in ((61, 10), (73, 9), (101, 25), (109, 27), (113, 14)):
    if (p - 1) % d or ((p - 1) // 2) % d:
        continue
    gen = prim_root(p)
    h = pow(gen, (p - 1) // d, p)
    H = {pow(h, j, p) for j in range(d)}
    g = {x: 1 for x in H}
    mu, bad = chart(Fp(p), g)
    Delta, T0, X, c = chart_quantities(Fp(p), g, mu)
    psi, ce, A, Z, T0k, ck, Xk = kappa_form(p, g)
    chi = lambda a: 1 if pow(a, (p - 1) // 2, p) == 1 else -1
    inv = True
    for k in range(2, p):
        for e, eps in enumerate((1, -1)):
            c1 = ce[k][e]
            c2 = ce[(1 - k) % p][e]
            c3 = ce[(1 - pow(k, p - 2, p)) % p][0 if chi(k) * eps == 1 else 1]
            inv &= (c1 == c2 == c3)
    print(f"   p={p} |H|={d}: T0={T0} X={X} anharmonic invariance {inv}")
    okC &= (T0 == X) and inv and bad == 0
for r in (7, 11, 13):
    F = Fq2(r)
    H = {(x, 0) for x in range(1, r)}
    okC &= all(F.is_sq(x) for x in H)
    g = {x: 1 for x in H}
    mu, bad = chart(F, g)
    Delta, T0, X, c = chart_quantities(F, g, mu)
    hs = len(H)
    print(f"   F_{{{r}^2}}: |H| = {hs}, T0 = {T0}, X = {X}, X/|H|^3 = {X / hs ** 3:.3f}, c = {c}")
    okC &= (T0 == X) and bad == 0
check("T0 = X for subgroup laws (5 cases) and in the F_{r^2} control with H = F_r^x (r = 7, 11, 13); "
      "anharmonic invariance", okC)

print("Part D: interval (Fejer) law and geometric-progression energies (floating, evidence)")


def fejer_g(p, L):
    n = (p - 1) // 2
    gen = prim_root(p)
    g = {}
    for k in range(n):
        x = pow(gen, 2 * k, p)
        kk = k if k <= n // 2 else k - n
        if kk == 0:
            val = 1.0
        else:
            val = (math.sin(math.pi * L * kk / n) / (L * math.sin(math.pi * kk / n))) ** 2
        g[x] = val
    return g, gen, n


def energies(p, I):
    """masked X(1_I) (ratios in Q minus 1) and full E^x(I-1) (all ratios), I a set of nonzero residues."""
    S = [(x - 1) % p for x in I if x != 1]
    cnt = defaultdict(int)
    for a in S:
        ia = pow(a, p - 2, p)
        for b in S:
            cnt[b * ia % p] += 1
    full = sum(v * v for v in cnt.values())
    masked = sum(v * v for k, v in cnt.items() if k != 1 and pow(k, (p - 1) // 2, p) == 1)
    return masked, full


okD = True
for p in (101, 197, 257, 401):
    n = (p - 1) // 2
    L = max(2, round(n / math.sqrt(p)))
    g, gen, n = fejer_g(p, L)
    K = n // (4 * L)
    I = {pow(gen, 2 * k % (p - 1), p) for k in range(-K, K + 1)}
    II = {x * pow(y, p - 2, p) % p for x in I for y in I}
    ming = min(g[x] for x in II)
    mu, _ = chart(Fp(p), g)
    Delta, T0, X, c = chart_quantities(Fp(p), g, mu)
    XI, EI = energies(p, I)
    mu1, _ = chart(Fp(p), {x: 1 for x in I})
    _, T0I, XI2, _ = chart_quantities(Fp(p), {x: 1 for x in I}, mu1)
    print(f"   p={p} L={L} |I|={len(I)} min g on I/I = {ming:.4f}  T0(g_J) = {T0:.3f}  X(1_I) = {XI2} "
          f"(kappa-form {XI})  ratio {T0 / XI2:.3f}  full E(I-1) = {EI}")
    okD &= ming >= 4 / math.pi ** 2 - 1e-12 and T0 >= (4 / math.pi ** 2) ** 5 * XI2 and XI == XI2
check("interval law: min g on I/I >= 4/pi^2 and T0(g_J) >= (4/pi^2)^5 X(1_I); X(1_I) chart = kappa-form", okD)

print("   geometric progressions I = {gamma^(2k): |k| <= K}, K = floor(sqrt(p)/2) (evidence only):")
okE = True
for p in (1009, 4001, 10009, 40009, 100003):
    if p % 4 != 1:
        continue
    gen = prim_root(p)
    K = int(math.isqrt(p) // 2)
    I = {pow(gen, (2 * k) % (p - 1), p) for k in range(-K, K + 1)}
    XI, EI = energies(p, I)
    N = len(I)
    print(f"   p={p:6d} |I|={N:4d}  masked X(1_I)/|I|^2 = {XI / N ** 2:.3f}  full E(I-1)/|I|^2 = {EI / N ** 2:.3f}  "
          f"E/|I|^2.5 = {EI / N ** 2.5:.4f}  full/masked = {EI / max(XI, 1):.2f}")
    okE &= EI <= 16 * (XI + N * N)       # union bound: full <= 16 * max class energy <= 16 (masked + kappa=1 term)
check("full E^x(I-1) <= 16 (X(1_I) + |I|^2) in every row (masked and unmasked energies are comparable)", okE)

print("Part E: exponents (exact Fractions)")
E = Fr
cov = lambda eT0: E(1, 2) + eT0
checks = [
    ("43/24 threshold on T0 is 31/24", cov(E(31, 24)) == E(43, 24)),
    ("7/4 threshold on T0 is 5/4", cov(E(5, 4)) == E(7, 4)),
    ("T0 <= X << p^(4/3): covariance 11/6", cov(E(4, 3)) == E(11, 6)),
    ("half-structured CS: (5/4 + 4/3)/2 = 31/24 exactly", (E(5, 4) + E(4, 3)) / 2 == E(31, 24)),
    ("CS with sum A^2 <= p^(7/6): (7/6 + 4/3)/2 = 5/4", (E(7, 6) + E(4, 3)) / 2 == E(5, 4)),
    ("Stevens-de Zeeuw ICR: N^(3/4) N^(1/2) (N^2)^(3/4) = N^(11/4) = p^(11/8) > p^(31/24)",
     (E(3, 4) + E(1, 2) + E(3, 2)) / 2 == E(11, 8) and E(11, 8) > E(31, 24)),
    ("SdZ conditions at a = b = N, |L| = N^2: a b^2 <= |L|^3 and a |L| = p^(3/2) <= p^2",
     E(3, 2) <= E(3) and E(3, 2) <= 2),
    ("Szemeredi-Trotter strength: (N^2 N^2)^(2/3) = p^(4/3)", E(2, 3) * 4 / 2 == E(4, 3)),
    ("pencil with t(h) << N^4/h^4: balance 1 + e = 4 - 3e at e = 3/4, value N^(7/4) = p^(7/8)",
     1 + E(3, 4) == 4 - 3 * E(3, 4) and (1 + E(3, 4)) / 2 == E(7, 8)),
    ("pencil with t(h) << N^3/h^3: balance 1 + e = 3 - 2e at e = 2/3, value p^(5/6)",
     1 + E(2, 3) == 3 - 2 * E(2, 3) and (1 + E(2, 3)) / 2 == E(5, 6)),
    ("light-triangle / auditor (ii): W (G X D0*)^(1/2): 1/2 + (1/2 + 4/3 + d)/2 = 17/12 + d/2",
     E(1, 2) + (E(1, 2) + E(4, 3)) / 2 == E(17, 12)),
    ("17/12 + d/2 < 43/24 iff d < 3/4, < 7/4 iff d < 2/3",
     E(17, 12) + E(3, 4) / 2 == E(43, 24) and E(17, 12) + E(2, 3) / 2 == E(7, 4)),
    ("pointwise CS (N X)^(1/2): d = 11/12 at X = p^(4/3), 3/4 at X = p",
     (E(1, 2) + E(4, 3)) / 2 == E(11, 12) and (E(1, 2) + 1) / 2 == E(3, 4)),
    ("heavy set |level| D0*: 1/2 + 1/24 + d < 31/24 iff d < 3/4", E(1, 2) + E(1, 24) + E(3, 4) == E(31, 24)),
    ("Prop. 5 at theta = 1/24: p^(-1/24) X = p^(31/24)", E(4, 3) - E(1, 24) == E(31, 24)),
    ("auditor (i) (T3 G E)^(1/2) with T3 ~ p, G ~ p^(1/2), E ~ p^(4/3): 17/12", (1 + E(1, 2) + E(4, 3)) / 2 == E(17, 12)),
    ("Plancherel floor (Gamma_tot E0)^(1/2) >= (p^(1/2) p^2)^(1/2) = p^(5/4)", (E(1, 2) + 2) / 2 == E(5, 4)),
    ("Cor. 3.1: p^(5/4) = |I|^(5/2) at |I| ~ p^(1/2)", E(5, 4) == E(5, 2) / 2),
    ("MPRRS L33 at A = I, B = I - 1, |AA| ~ |A|: |AA|^(3/2)|B|^(3/2)/|A|^(1/2) = N^(5/2); hypotheses N^3 <= p^2, N <= N^(3/2)",
     E(3, 2) + E(3, 2) - E(1, 2) == E(5, 2) and E(3, 2) <= 2),
    ("GP energy at N^(5/2) = p^(5/4) is below 31/24 (no obstruction at 43/24)", E(5, 4) < E(31, 24)),
    ("F_(r^2) control: X ~ q^(3/2), Theorem A bound exponent 2", cov(E(3, 2)) == 2),
]
for name, cnd in checks:
    check(name, cnd)

print("\nALL AUDIT CHECKS OK" if OK else "\nSOME AUDIT CHECK FAILED")
sys.exit(0 if OK else 1)
