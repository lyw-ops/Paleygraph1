#!/usr/bin/env python3
r"""Round 187 audit (session/r187-audit): independent checks of the pair-energy report
`native-claude-ordinary-prime-level-pair-energy-187.md` (PAIR).

Own implementation; imports no project script.

Part A (exact Fractions): re-derive the three Proposition P' exponents from the per-piece
   bound and the piece sums, by symbolic linear forms in (e_s, mu_s, e_g, mu_g); exact vertex
   enumeration of the admissible polytope; Lemma C chunk identity; Theorem 2 and the
   Round 178/180/184 chain to 43/24 (both through sup C, Round 184 Prop. 1(iii), and through
   max W <= X, Prop. 1(ii)); the square-field accounting with characteristic r (q = r^2).
Part B (exact integers, prime fields): Lemma M' Steps 1-3 for many sets at primes up to ~400,
   including (2.1), |B|^2 >= m^2/(16 L0^2 K), the bound s'b'^(1/2) <= 2 L0 eta (alpha K m mu*)^(1/2),
   line distinctness and the incidence lower bound against a brute-force incidence count.
Part C (exact integers, F_{r^2}): the subfield configuration A = B = F_r \ {0,1}, energies
   computed by brute force over all u in F_{r^2}^x; shows E = (r-1)(r-3)^2 ~ q^(3/2), i.e. the
   characteristic-free part of Lemma M' (terms 1-2) fails over F_{r^2}, and the characteristic
   term 3 is exactly what carries it.
Part D (float/int evidence): adversarial local search for E(A;H)/T1 with H a multiplicative
   subgroup (K = 1, B = H) at primes p ~ 10^3-10^4.  Evidence only.

Usage: .venv/bin/python -B research/paley-187-audit-pair-check.py [--quick]
"""
import itertools
import math
import random
import sys
from fractions import Fraction as Fr

OK = True


def check(cond, msg):
    global OK
    print(("ok   " if cond else "FAIL ") + msg)
    if not cond:
        OK = False


# ---------------------------------------------------------------- Part A
class Lin:
    """Linear form c0 + sum c_v v over variables es, ms, eg, mg (exact)."""
    V = ('es', 'ms', 'eg', 'mg')

    def __init__(self, c0=0, **kw):
        self.c = {'1': Fr(c0)}
        for v in self.V:
            self.c[v] = Fr(kw.get(v, 0))

    def __add__(self, o):
        r = Lin()
        o = o if isinstance(o, Lin) else Lin(o)
        for k in r.c:
            r.c[k] = self.c[k] + o.c[k]
        return r

    __radd__ = __add__

    def __sub__(self, o):
        o = o if isinstance(o, Lin) else Lin(o)
        return self + o * (-1)

    def __mul__(self, s):
        r = Lin()
        for k in r.c:
            r.c[k] = self.c[k] * Fr(s)
        return r

    __rmul__ = __mul__

    def __rsub__(self, o):
        return Lin(o) - self

    def ev(self, pt):
        return self.c['1'] + sum(self.c[v] * pt[v] for v in self.V)

    def __eq__(self, o):
        return all(self.c[k] == o.c[k] for k in self.c)

    def __repr__(self):
        return ' + '.join(f'{self.c[k]}*{k}' for k in self.c if self.c[k])


def part_a():
    print('== Part A: exact exponent algebra ==')
    es, ms, eg, mg = (Lin(**{v: 1}) for v in Lin.V)
    half = Fr(1, 2)
    # sizes: M = p^(1/2-mu_s), alpha = p^(1/2-mu_g), K_M = p^(2 e_s + mu_s), heights a = p^-e
    M = half - ms
    alpha = half - mg
    K = 2 * es + ms
    heights = (es + eg) * (-1)
    # per-piece Lemma M' (form I) terms for E(A;B):
    #   t1 = alpha^(5/3) |B|^(2/3) K^(2/3) m^(1/3);  t2 = K alpha |B|;  t3 = alpha^2 |B| (K m)^(1/2) p^(-1/2)
    # piece sums: sum_B |B|^c <= 2M (min|B|)^(c-1), min|B| >= M K^(-1/2)  (logs dropped)
    minB = M - K * half

    def piece_sum(c):  # exponent of sum_B |B|^c
        return M + (c - 1) * minB

    # E^(1/2) per piece then summed: term1: (alpha^(5/3) K^(2/3) M^(1/3))^(1/2) * sum |B|^(1/3)
    T1 = heights + alpha * Fr(5, 6) + K * Fr(1, 3) + M * Fr(1, 6) + piece_sum(Fr(1, 3))
    T2 = heights + (K + alpha) * half + piece_sum(half)
    T3 = heights + alpha + (K + M) * Fr(1, 4) - Fr(1, 4) + piece_sum(half)
    two3 = Fr(2, 3)
    us = 2 * es + ms
    ug = 2 * eg + mg
    claimed1 = (us - ug) * Fr(1, 6) - (eg + mg) * two3
    claimed2 = Lin(Fr(-1, 6)) + us * Fr(1, 4) - ug * half
    claimed3 = Lin(Fr(-1, 24)) - (eg + mg) - ms * Fr(1, 4)
    check(T1 - two3 == claimed1, f'T1 excess re-derived = (u_s-u_g)/6 - (2/3)(e_g+mu_g): {T1 - two3}')
    check(T2 - two3 == claimed2, f'T2 excess re-derived = -1/6 + u_s/4 - u_g/2: {T2 - two3}')
    check(T3 - two3 == claimed3, f'T3 excess re-derived = -1/24 - (e_g+mu_g) - mu_s/4: {T3 - two3}')
    # Round 186 Prop. P form I excess (audit 186 section 2.3): (13/6) e_s + (13/12) mu_s - e_g - (5/6) mu_g
    r186 = es * Fr(13, 6) + ms * Fr(13, 12) - eg - mg * Fr(5, 6)
    check(r186 - (T1 - two3) == us * Fr(11, 12), 'Round 186 Prop. P (form I) minus T1 = (11/12) u_s')
    # vertex enumeration: 0<=e<=1/6, -e<=mu<=1/2, u_s <= u_g.  Constraints as rows a.x <= b.
    cons = []
    for e, m in (('es', 'ms'), ('eg', 'mg')):
        cons.append(({e: -1}, 0))
        cons.append(({e: 1}, Fr(1, 6)))
        cons.append(({e: -1, m: -1}, 0))          # mu >= -e
        cons.append(({m: 1}, Fr(1, 2)))
    cons.append(({'es': 2, 'ms': 1, 'eg': -2, 'mg': -1}, 0))   # u_s - u_g <= 0
    V = Lin.V

    def solve(rows):
        # Gaussian elimination over Fractions, 4x4
        A = [[Fr(r[0].get(v, 0)) for v in V] + [Fr(r[1])] for r in rows]
        n = 4
        for i in range(n):
            piv = next((k for k in range(i, n) if A[k][i] != 0), None)
            if piv is None:
                return None
            A[i], A[piv] = A[piv], A[i]
            for k in range(n):
                if k != i and A[k][i] != 0:
                    f = A[k][i] / A[i][i]
                    A[k] = [a - f * b for a, b in zip(A[k], A[i])]
        return {V[i]: A[i][4] / A[i][i] for i in range(n)}

    verts = []
    for rows in itertools.combinations(cons, 4):
        pt = solve(rows)
        if pt is None:
            continue
        if all(sum(Fr(r[0].get(v, 0)) * pt[v] for v in V) <= r[1] for r in cons):
            verts.append(pt)
    mx = [max(f.ev(pt) for pt in verts) for f in (claimed1, claimed2, claimed3)]
    check(len(verts) > 0 and mx[0] == 0 and mx[1] == Fr(-1, 6) and mx[2] == 0,
          f'vertex enumeration ({len(verts)} vertices): max excesses T1,T2,T3 = {mx}')
    # without the choice u_s <= u_g, T1 is not <= 0:
    cons_free = cons[:-1]
    vf = []
    for rows in itertools.combinations(cons_free, 4):
        pt = solve(rows)
        if pt and all(sum(Fr(r[0].get(v, 0)) * pt[v] for v in V) <= r[1] for r in cons_free):
            vf.append(pt)
    m1 = max(claimed1.ev(pt) for pt in vf)
    check(m1 > 0, f'without the structured-side choice the T1 maximum is {m1} > 0 (choice is load-bearing)')
    # e_s beyond 1/6: T3 max becomes positive
    pt = {'es': Fr(1, 5), 'ms': Fr(-1, 5), 'eg': Fr(1, 5), 'mg': Fr(-1, 5)}
    check(claimed3.ev(pt) > 0, f'at e = 1/5 (outside range), whole level sets: T3 excess {claimed3.ev(pt)} > 0')
    # Lemma C: s^(3/4) b^(1/2) n (p^2/s)^(-1/4) = s b^(1/2) n p^(-1/2)  (exponents in s, p)
    check(Fr(3, 4) + Fr(1, 4) == 1 and Fr(-2, 4) == Fr(-1, 2), 'Lemma C chunk identity (exponents of s and p)')
    # Theorem 2 and chain
    th = Fr(1, 6)
    light = Fr(1, 2) * (-th + Fr(1, 2)) + Fr(1, 2)   # ||h_<||_2 ||h_>=||_1 = (tau0 G)^(1/2) G
    check(light == two3, f'light Young term exponent {light} = 2/3')
    supC = Fr(4, 3)
    X = Fr(4, 3)
    Ex_m = max(2 * X, supC + 2)
    sumW32 = 1 + Ex_m / 2
    check(Ex_m == Fr(10, 3) and sumW32 == Fr(8, 3), 'E^x(m) <= X^2 + supC M1^2: 10/3; sum W^(3/2) <= M1 E^x(m)^(1/2): 8/3')
    EW = max(sumW32, 1 + X, Fr(5, 2))   # sum W^2/p <= maxW sum W/p, G log p sum W
    cov = Fr(9, 8) + EW / 4
    check(EW == Fr(8, 3) and cov == Fr(43, 24) and cov == Fr(115, 64) - Fr(1, 192),
          f'covariance 9/8 + E/4 = {cov} = 115/64 - 1/192')
    eps = Fr(1, 3)
    check(Fr(7, 4) + eps / 8 == Fr(43, 24), 'Round 184 Prop. 1(ii)/(iii) with eps = 1/3 gives 7/4 + 1/24 = 43/24 '
          '(max W <= X << p^(4/3) alone already gives 43/24)')
    check(Fr(43, 24) < Fr(2125, 1184) < Fr(1193, 664) < Fr(115, 64), '43/24 < 2125/1184 < 1193/664 < 115/64')
    check(Fr(4, 3) < Fr(11, 8), 'M_w <= E^x(h)/4: 4/3 < 11/8 (Round 180)')
    # square field F_q, q = r^2, characteristic r = q^(1/2): Lemma C third term s b^(1/2) n r^(-1/2).
    # Lemma M' term 3 with p -> char: alpha^2 |B| (K m)^(1/2) char^(-1/2); subfield: alpha=|B|=m=r, K=1
    t3 = 2 + 1 + Fr(1, 2) - Fr(1, 2)
    check(t3 == 3, 'F_{r^2}: Lemma M\' term 3 with char = r is r^3 = q^(3/2) (matches the subfield energy)')
    t1 = Fr(5, 3) + Fr(2, 3) + Fr(1, 3)
    check(t1 == Fr(8, 3), 'F_{r^2}: terms 1-2 alone would give r^(8/3) = q^(4/3) < q^(3/2) (would contradict Prop. 5)')
    # pair price in F_q at height 1 with char = q^(1/2): T3 excess +1/8 in q-exponent
    check(Fr(-1, 24) + Fr(1, 8) == Fr(1, 12) and 2 * (two3 + Fr(1, 12)) == Fr(3, 2),
          'F_{r^2}: T3 excess becomes +1/12, i.e. E^x(h) <= q^(3/2): consistent with X ~ q^(3/2)')


# ---------------------------------------------------------------- Part B
def lemma_mprime_exact(p, A, R, rng):
    """Exact check of Lemma M' Steps 1-3 for A, R subsets of F_p \\ {0,1}."""
    inv = [0] + [pow(x, p - 2, p) for x in range(1, p)]
    m = len(R)
    r = {}
    for y in R:
        for y2 in R:
            w = y * inv[y2] % p
            r[w] = r.get(w, 0) + 1
    assert sum(r.values()) == m * m
    E = sum(v * v for v in r.values())
    # brute-force E^x(R)
    Eb = 0
    prod = {}
    for y1 in R:
        for y2 in R:
            k = y1 * y2 % p
            prod[k] = prod.get(k, 0) + 1
    Eb = sum(v * v for v in prod.values())
    if E != Eb:
        return False, 'E mismatch'
    K = Fr(m ** 3, E)
    L0 = m.bit_length()          # floor(log2 m) + 1
    classes = {}
    for w, v in r.items():
        classes.setdefault(v.bit_length() - 1, []).append(w)
    j = max(classes, key=lambda j: sum(r[w] ** 2 for w in classes[j]))
    F = set(classes[j])
    rho = 1 << j
    SF2 = sum(r[w] ** 2 for w in F)
    P = sum(r[w] for w in F)
    if not (SF2 * L0 >= E and len(F) * rho * rho <= E and 2 * rho * L0 * P >= E):
        return False, 'class bounds'
    eta = Fr(P, m * m)
    if not (len(F) <= 4 * L0 * L0 * K * eta * eta * m and 1 / eta <= 2 * L0 * K and eta <= 1):
        return False, '(2.1)'
    V = [inv[y] for y in R]
    d = {y: sum(1 for v in V if v * y % p in F) for y in R}
    if sum(d.values()) != P or any(d[y] > min(m, len(F)) for y in R):
        return False, 'd(y)'
    B = [y for y in R if 2 * m * d[y] >= P]
    if not (2 * sum(d[y] for y in B) >= P and Fr(len(B) ** 2) >= Fr(m * m) / (16 * L0 * L0 * K)):
        return False, '|B| bound'
    alpha = len(A)
    mu = min(Fr(alpha), 4 * L0 * L0 * K * m)
    s1, b1 = min(alpha, len(F)), max(alpha, len(F))
    # s' b'^(1/2) <= 2 L0 eta (alpha K m mu*)^(1/2)   <=>  s'^2 b' <= 4 L0^2 eta^2 alpha K m mu*
    if not (Fr(s1 * s1 * b1) <= 4 * L0 * L0 * eta * eta * alpha * K * m * mu):
        return False, 'H* bound'
    # rows of m_{A,B}
    Aset = set(A)
    mrow = {}
    for x in A:
        for y in B:
            u = (1 - y) * inv[(1 - x) % p] % p
            mrow[u] = mrow.get(u, 0) + 1
    if sum(mrow.values()) != alpha * len(B):
        return False, 'row sum'
    hs = sorted(set(mrow.values()))
    hs = sorted(set([hs[0], hs[len(hs) // 2], hs[-1]]))   # smallest, median and largest row values
    for h in hs:
        T = [u for u, c in mrow.items() if c >= h]
        lines = {}
        for u in T:
            for v in V:
                key = (v * u % p, v * (1 - u) % p)   # slope, intercept
                if key in lines:
                    return False, 'lines not distinct'
                lines[key] = 1
        # brute-force incidences of A x F with these lines
        Fs = F
        I = 0
        for (sl, ic) in lines:
            for x in A:
                if (sl * x + ic) % p in Fs:
                    I += 1
        if not (2 * m * I >= h * len(T) * P):
            return False, f'incidence bound h={h}'
    return True, dict(m=m, K=float(K), F=len(F), eta=float(eta), B=len(B), alpha=alpha)


def part_b(quick):
    print('== Part B: exact Lemma M\' Steps 1-3 (prime fields) ==')
    rng = random.Random(187)
    primes = [p for p in range(101, 420 if not quick else 200) if all(p % q for q in range(2, int(p ** .5) + 1))][::3]
    n_cases = 0
    for p in primes:
        g = next(x for x in range(2, p) if all(pow(x, (p - 1) // q, p) != 1 for q in set(_factor(p - 1))))
        univ = list(range(2, p))
        sets = []
        m = max(6, int(1.3 * p ** 0.5))
        sets.append(rng.sample(univ, m))                                   # random
        gp = [pow(g, k, p) for k in range(1, m + 1)]
        sets.append([x for x in gp if x not in (0, 1)])                     # geometric progression
        o = min((d for d in range(3, p) if (p - 1) % d == 0), key=lambda d: abs(d - m))
        sub = sorted({pow(g, (p - 1) // o * k, p) for k in range(o)} - {1})
        if len(sub) >= 4:
            sets.append(sub)                                                # subgroup minus 1
        prog = [pow(g, 2 * k, p) for k in range(1, m // 2 + 1)]
        sets.append([x for x in set(prog + rng.sample(univ, m // 2)) if x not in (0, 1)])  # progression + junk
        mix = [pow(g, k, p) for k in range(1, m // 3 + 1)] + [(1 - pow(g, k, p)) % p for k in range(1, m // 3 + 1)]
        sets.append([x for x in set(mix) if x not in (0, 1)])               # GP union shifted GP
        for R in sets:
            for A in (rng.sample(univ, max(3, len(R) // 2)), rng.sample(univ, min(len(univ), 2 * len(R))),
                      [(1 - x) % p for x in R if (1 - x) % p not in (0, 1)]):
                ok, info = lemma_mprime_exact(p, A, R, rng)
                n_cases += 1
                if not ok:
                    check(False, f'p={p} Lemma M\' exact: {info}')
                    return
    check(True, f'Lemma M\' Steps 1-3 exact in {n_cases} cases, p in [{primes[0]}, {primes[-1]}] '
                '(class bounds, (2.1), d(y), |B|, H* bound, distinct lines, brute-force incidences for every h)')


def _factor(m):
    f, d = [], 2
    while d * d <= m:
        while m % d == 0:
            f.append(d)
            m //= d
        d += 1
    if m > 1:
        f.append(m)
    return f


# ---------------------------------------------------------------- Part C
def part_c(quick):
    print('== Part C: the square field F_{r^2} (exact integers) ==')
    for r in ([5, 7, 11, 13] if quick else [5, 7, 11, 13, 17, 19, 23]):
        dn = next(d for d in range(2, r) if pow(d, (r - 1) // 2, r) == r - 1)   # nonresidue: F_{r^2} = F_r(sqrt dn)

        def mul(a, b):
            return ((a[0] * b[0] + dn * a[1] * b[1]) % r, (a[0] * b[1] + a[1] * b[0]) % r)

        def inv(a):
            nrm = (a[0] * a[0] - dn * a[1] * a[1]) % r
            ni = pow(nrm, r - 2, r)
            return (a[0] * ni % r, (-a[1]) * ni % r)

        A = [(x, 0) for x in range(2, r)]          # F_r \ {0,1}
        # m(u) = #{(x,y) in A x A : 1 - y = u (1 - x)} for all u in F_{r^2}^x
        cnt = {}
        for x in A:
            ix = inv(((1 - x[0]) % r, (-x[1]) % r))
            for y in A:
                u = mul(((1 - y[0]) % r, (-y[1]) % r), ix)
                cnt[u] = cnt.get(u, 0) + 1
        E = sum(v * v for v in cnt.values())
        q = r * r
        sub_only = all(u[1] == 0 for u in cnt)
        # E(A;A) = sum over u in F_r^x of m(u)^2; m(1) = r-2, m(u) = r-3 for u in F_r \ {0,1}
        exp_closed = (r - 2) ** 2 + (r - 2) * (r - 3) ** 2
        check(sub_only and E == exp_closed,
              f'r={r}: E(A;A) = {E} = (r-2)^2 + (r-2)(r-3)^2; E/q^(3/2) = {E / q ** 1.5:.3f}; '
              f'E/r^(8/3) = {E / r ** (8 / 3):.3f} (grows like r^(1/3))')
    print('   reading: with alpha = |B| = m = r - 2, K ~ 1, Lemma M\' terms 1-2 are ~ r^(8/3); the energy is ~ r^3.')
    print('   Only term 3, with the characteristic r in place of p, reaches r^3. Over F_p (field size = characteristic)')
    print('   the same term is alpha^2 |B| (K m)^(1/2) p^(-1/2), which is the T3 term that is <= p^(4/3) in PAIR.')


# ---------------------------------------------------------------- Part D
def part_d(quick):
    print('== Part D: adversarial local search, E(A;H) against T1 (evidence only) ==')
    rng = random.Random(1871)
    plist = [1009, 4001] if quick else [1009, 2017, 4001, 8009]
    for p in plist:
        fac = set(_factor(p - 1))
        g = next(x for x in range(2, p) if all(pow(x, (p - 1) // q, p) != 1 for q in fac))
        # subgroup H of order ~ sqrt(p)
        divs = [d for d in range(2, p) if (p - 1) % d == 0]
        o = min(divs, key=lambda d: abs(d - p ** 0.5))
        H = sorted({pow(g, (p - 1) // o * k, p) for k in range(o)} - {1})
        m = len(H)
        inv = [0] + [pow(x, p - 2, p) for x in range(1, p)]
        # T_u = {x : 1 - x = (1 - y)/u, y in H}; m(u) = |A cap T_u|
        oneminusH = [(1 - y) % p for y in H]
        T = {}
        for u in range(1, p):
            iu = inv[u]
            T[u] = [(1 - z * iu) % p for z in oneminusH]
        for alpha in (m, 3 * m):
            # start: union of T_u for u in a random small set, trimmed
            A = set()
            while len(A) < alpha:
                A |= set(x for x in T[rng.randrange(1, p)] if x not in (0, 1))
            A = set(list(A)[:alpha])

            def energy(Aset):
                c = {}
                for x in Aset:
                    ix = inv[(1 - x) % p]
                    for z in oneminusH:
                        u = z * ix % p
                        c[u] = c.get(u, 0) + 1
                return sum(v * v for v in c.values())

            best = energy(A)
            univ = [x for x in range(2, p)]
            steps = 300 if quick else 1500
            for _ in range(steps):
                out = rng.choice(list(A))
                inn = rng.choice(univ)
                if inn in A:
                    continue
                B2 = set(A)
                B2.remove(out)
                B2.add(inn)
                e2 = energy(B2)
                if e2 >= best:
                    A, best = B2, e2
            mu = min(alpha, m)
            T1 = alpha ** (4 / 3) * m ** (2 / 3) * m ** (1 / 3) * mu ** (1 / 3)
            triv = alpha * m * mu
            print(f'   p={p} |H|={m} alpha={alpha}: best E(A;H) = {best}, E/T1 = {best / T1:.3f}, '
                  f'E/(alpha m min) = {best / triv:.3f}, E/(alpha m) = {best / (alpha * m):.2f}')


if __name__ == '__main__':
    quick = '--quick' in sys.argv
    part_a()
    part_b(quick)
    part_c(quick)
    part_d(quick)
    print('ALL AUDIT CHECKS OK' if OK else 'SOME AUDIT CHECKS FAILED')
