#!/usr/bin/env python3
"""Round 185 audit: independent checks of the band-autocorrelation report.

Written by the Round 185 auditor; it imports nothing from the report's scripts.

Part A (exact Fractions): every exponent of Theorems 1-2, Corollary 3, the
  Round 182/184 heavy-bound optimisation behind eta(eps), the Stevens-de Zeeuw
  hypothesis at the scales used, and the Warren-Wheeler exponents of section 5.
Part B (exact integers / Fractions, small p): for random integer weights
  B1  C(lambda) (masked rows m(r) = c_h(1-r) 1_Q(1-r)) <= C#(lambda), and the
      quadruple-sum form of C# equals the row form sum_r c_{12}(1-lambda r) c_{34}(1-r);
  B2  the layer-cake identity behind Lemma 4:
      C#[f1..f4] = sum_{t1..t4} I(U1(t1) x U3(t3), lines over U2(t2) x U4(t4)),
      counted with the admissibility masks, for integer-valued f_i;
  B3  the Jensen step sum_t |U(t)|^theta <= a^(1-theta) (sum f)^theta (float check);
  B4  the 81-term split with cuts tau0 < tau1: the terms sum to C#, every term
      with a light slot is <= tau0 * prod(sums of the other three slots);
  B5  Lemma 5: C#[f1..f4]^4 <= prod_i E^x(v_i), v_i(z) = f_i(1-z);
  B6  the Theorem 2 layer cake g_H = tau1*1[g>=tau1] + int_{tau1}^1 1[g>t] dt.
Part C (float, actual-type weights g = |f|^2 from random probabilities nu on
  the characters of Q): Proposition 6, t^k |W|^(2k) <= n max(nu) T_k(W), k = 2, 3,
  for W = S_t at several t; and Lemma 5 / C <= X for the actual-type g.

Usage: .venv/bin/python -B research/paley-185-audit-band-check.py
"""
from fractions import Fraction as F
import itertools
import math
import random
import sys

OK = True


def check(cond, msg):
    global OK
    print(("ok   " if cond else "FAIL ") + msg)
    if not cond:
        OK = False


# ---------------------------------------------------------------- Part A
def part_a():
    print("== A. exponent algebra (exact) ==")
    half = F(1, 2)
    eleven8 = F(11, 8)
    # Round 182 heavy display: N(h_>=) << p^(1/3+5e/3) + p^(1/3+2e/3+d/6) + p^(3/8-3d/4).
    # Balance the last two in d: d = 1/22 - 8e/11, giving 15/44 + 6e/11.
    for e in (F(0), F(1, 214), F(1, 192), F(1, 46), F(1, 16)):
        d = F(1, 22) - F(8, 11) * e
        check(F(1, 3) + F(2, 3) * e + d / 6 == F(3, 8) - F(3, 4) * d == F(15, 44) + F(6, 11) * e,
              f"R182/R184 heavy balance at eps={e}: d={d}, exponent {F(15,44)+F(6,11)*e}")
        check(d >= 0, f"  d >= 0 at eps={e} (R184-P3 range eps <= 1/16)")

    def eta(e):
        return max(F(1, 3) + F(5, 3) * e, F(15, 44) + F(6, 11) * e)

    # Theorem 1: band 11/8 - e/4 against heavy 4 eta(e) (second branch).
    e1 = (eleven8 - F(15, 11)) / (F(1, 4) + F(24, 11))
    check(e1 == F(1, 214), f"Theorem 1 balance eps = {e1}")
    check(4 * eta(e1) == eleven8 - e1 / 4 == F(147, 107) == eleven8 - F(1, 856),
          "Theorem 1: 4 eta(1/214) = 11/8 - 1/856 = 147/107")
    check(F(1, 3) + F(5, 3) * e1 < F(15, 44) + F(6, 11) * e1, "  second branch of eta active")
    check(F(19, 14) < eleven8 - F(1, 856), "  light term 3/2 - 1/7 = 19/14 below")
    # Is 1/214 optimal for Theorem 1 (max over two monotone terms)? check neighbours.
    for e in (e1 - F(1, 10**6), e1 + F(1, 10**6)):
        check(max(eleven8 - e / 4, 4 * eta(e)) > F(147, 107), f"  neighbour eps={float(e):.7f} is worse")

    # Theorem 2.
    e2 = (eleven8 - F(4, 3)) / (F(1, 4) + F(20, 3))
    check(e2 == F(1, 166), f"Theorem 2 balance band = Phase 1 at eps = {e2}")
    target = eleven8 - F(1, 664)
    check(eleven8 - e2 / 4 == target and F(4, 3) + F(20, 3) * e2 == target, "  both equal 11/8 - 1/664 = 114/83")
    check(target == F(114, 83), "  114/83")
    dmin = F(8, 5) * F(1, 664)               # 11/8 - 5d/8 <= target
    dmax = (target - F(4, 3) - F(8, 3) * e2) * F(3, 2)  # Phase 2 <= target
    check(dmin == F(1, 415) and dmax == F(3, 83), f"  delta range [{dmin}, {dmax}]")
    check(F(4, 3) + F(8, 3) * e2 + F(2, 3) * dmin == eleven8 - F(239, 9960), "  Phase 2 at d=1/415: 11/8 - 239/9960")
    check(dmax <= half, "  delta within R182-ext range (0, 1/2]")
    # SdZ hypothesis a*n << p^2 with every set of size <= G/tau, G << p^(1/2).
    check(3 * (half + F(1, 7)) == F(27, 14) and F(27, 14) < 2, "SdZ: Lemma 4 at tau0 = p^(-1/7): (G/tau0)^3 = p^(27/14) = o(p^2)")
    check(3 * (half + e2) < 2, f"SdZ: H-b at tau1 = p^(-1/166): exponent {3*(half+e2)} < 2")
    check(3 * (half + F(1, 16)) < 2, "SdZ: valid for all eps <= 1/16")
    # SdZ combined form: a^(3/4) b^(1/2) <= (ab)^(5/8) iff a <= b; ab^2 > n^3 case: an <= a^(3/4)b^(1/2)n^(3/4).
    random.seed(1)
    good = True
    for _ in range(2000):
        a = random.uniform(1, 1e4); b = random.uniform(a, 1e5); n = random.uniform(1, 1e6)
        good &= a ** 0.75 * b ** 0.5 <= (a * b) ** 0.625 * (1 + 1e-12)
        if a * b * b > n ** 3:
            good &= a * n <= a ** 0.75 * b ** 0.5 * n ** 0.75 * (1 + 1e-12)
    check(good, "SdZ combined form (random a <= b, n): both reductions hold")
    # Lemma 4 total exponent and gains.
    th = [F(5, 8), F(3, 4), F(5, 8), F(3, 4)]
    check(sum(th) * half == eleven8, "Lemma 4: sum theta = 11/4, G^(11/4) = p^(11/8)")
    check(min(1 - t for t in th) == F(1, 4), "  smallest band gain is a^(1/4) (line role)")
    # H-b: point-role leftover p^((1/2-d)5/8) * G^(5/8+3/4+3/4)
    d = F(1, 415)
    check((half - d) * F(5, 8) + half * (F(5, 8) + F(3, 2)) == eleven8 - F(5, 8) * d, "H-b exponent 11/8 - 5d/8")
    # H-a integrals: int_{tau1}^1 t^(-8/3) dt << tau1^(-5/3); 4th power.
    check(4 * (F(1, 3) + F(5, 3) * e2) == F(4, 3) + F(20, 3) * e2, "H-a Phase 1 fourth power")
    # Corollary 3.
    for dC, cov in ((F(1, 664), F(1, 5312)), (F(1, 856), F(1, 6848))):
        Em = 3 + F(3, 8) - dC
        check(F(68, 23) < Em and 3 < Em, f"  dC={dC}: X^2 (68/23) and C(1)^2 <= G^6 (3) below sup C*M1^2 = {Em}")
        sW = 1 + Em / 2
        check(sW == F(43, 16) - dC / 2, f"  sum W^(3/2) <= M1 E^x(m)^(1/2) = p^(43/16 - {dC/2})")
        check(Em - 1 < sW and F(5, 2) < sW, "  R178: sum W^2/p and G log p M1^2 are smaller")
        c = F(9, 8) + sW / 4
        check(c == F(115, 64) - cov, f"  covariance 9/8 + e/4 = 115/64 - {cov}")
        check(c > F(7, 4), "  still above the point-plane floor 7/4")
    check(F(115, 64) - F(1, 5312) == F(1193, 664), "  1193/664")
    # R184-P1(iii) form: eps = 3/8 - dC gives 7/4 + eps/8.
    check(F(7, 4) + (F(3, 8) - F(1, 664)) / 8 == F(1193, 664), "  same via R184-P1(iii) with eps = 3/8 - 1/664")
    # Warren-Wheeler at |A| = |B| = N, |T| = N^2.
    t3a = F(4, 5) + F(3, 5) + 2 * F(4, 5); t3b = F(6, 5) + F(7, 5) + 2 * F(1, 5)
    check(t3a == 3 and t3b == 3, "WW Thm 3: both terms N^3 (trivial)")
    t4 = half + F(7, 10) + 2 * F(3, 5) + F(1, 10) * 4
    check(t4 == F(14, 5) and t4 / 2 > eleven8, "WW Thm 4 with E(T)=|T|^2: N^(14/5) = p^(7/5) > p^(11/8)")
    # height-a: sets sqrt(p)/a, weights a^4: p^(7/5) a^(6/5) < p^(11/8) iff a < p^(-1/48)
    check(F(7, 5) - F(6, 5) * F(1, 48) == eleven8, "  height gain threshold a = p^(-1/48)")


# ---------------------------------------------------------------- Part B helpers
def squares(p):
    return {(x * x) % p for x in range(1, p)}


def setup(p):
    Q = squares(p)
    inv = [0] + [pow(x, p - 2, p) for x in range(1, p)]
    return Q, inv


def cvv(v, w, kappa, p):
    """c_{v,w}(kappa) = sum_z w(z) v(kappa z)."""
    return sum(w[z] * v[(kappa * z) % p] for z in range(1, p))


def shifted(f, p):
    """v(z) = f(1-z) for z != 0; f is a list indexed by x in F_p."""
    v = [0] * p
    for z in range(1, p):
        v[z] = f[(1 - z) % p]
    return v


def Ex(v, p):
    return sum(cvv(v, v, k, p) ** 2 for k in range(1, p))


def adm(p):
    return [x for x in range(p) if x not in (0, 1)]


def Csharp(fs, lam, p):
    """Quadruple sum over admissible tuples of f1(Y1) f2(D1) f3(Y3) f4(D3)."""
    f1, f2, f3, f4 = fs
    A = adm(p)
    tot = 0
    for D1 in A:
        if f2[D1] == 0:
            continue
        for D3 in A:
            if f4[D3] == 0:
                continue
            for Y1 in A:
                if Y1 == D1 or f1[Y1] == 0:
                    continue
                # (Y1-D1)(1-D3) = lam (Y3-D3)(1-D1)  -> Y3 determined
                Y3 = (D3 + (Y1 - D1) * (1 - D3) * pow(lam * (1 - D1) % p, p - 2, p)) % p
                if Y3 in (0, 1) or Y3 == D3:
                    continue
                tot += f1[Y1] * f2[D1] * f3[Y3] * f4[D3]
    return tot


def Csharp_rows(fs, lam, p):
    v = [shifted(f, p) for f in fs]
    return sum(cvv(v[0], v[1], (1 - lam * r) % p, p) * cvv(v[2], v[3], (1 - r) % p, p)
               for r in range(2, p) if (1 - lam * r) % p != 0) if True else None


def incid(U1, U3, U2, U4, lam, p):
    """Admissible incidences between U1 x U3 and the lines l_{D1,D3}, (D1,D3) in U2 x U4."""
    c = 0
    for D1 in U2:
        for D3 in U4:
            for Y1 in U1:
                if Y1 == D1:
                    continue
                Y3 = (D3 + (Y1 - D1) * (1 - D3) * pow(lam * (1 - D1) % p, p - 2, p)) % p
                if Y3 in U3 and Y3 != D3:
                    c += 1
    return c


def rand_weight(p, Q, K, dens=0.6, rng=random):
    f = [0] * p
    for x in Q:
        if x != 1 and rng.random() < dens:
            f[x] = rng.randint(1, K)
    return f


def part_b():
    print("== B. exact small-p replays (integer weights) ==")
    rng = random.Random(185)
    for p in (13, 17, 29, 37, 41):
        Q, inv = setup(p)
        A = adm(p)
        ok1 = ok2 = ok4 = ok5 = ok6 = True
        jensen_ok = True
        # B1: actual-type rows from a single weight g (integer), masked C <= C#.
        g = rand_weight(p, Q, 5, rng=rng)
        h = shifted(g, p)
        for lam in range(2, p):
            m = [0] * p
            for r in range(2, p):  # r != 0, 1
                if (1 - r) % p in Q and (1 - r) % p != 1:
                    m[r] = cvv(h, h, (1 - r) % p, p)
            C = sum(m[r] * m[(lam * r) % p] for r in range(p))
            Cs = Csharp([g, g, g, g], lam, p)
            Cr = Csharp_rows([g, g, g, g], lam, p)
            ok1 &= (C <= Cs) and (Cs == Cr)
        check(ok1, f"p={p}: B1 C(lam) <= C#(lam) = row form, all lam != 0,1")
        # B2, B4, B5 with four different integer weights, a few lambdas.
        for trial in range(2):
            fs = [rand_weight(p, Q, 4, rng=rng) for _ in range(4)]
            for lam in rng.sample(range(2, p), min(4, p - 2)):
                Cs = Csharp(fs, lam, p)
                # B2 layer cake: f = sum_{t=0}^{K-1} 1[f > t]
                K = max(max(f) for f in fs)
                lv = [[{x for x in A if f[x] > t} for t in range(K)] for f in fs]
                tot = 0
                for t1, t2, t3, t4 in itertools.product(range(K), repeat=4):
                    U1, U2, U3, U4 = lv[0][t1], lv[1][t2], lv[2][t3], lv[3][t4]
                    if U1 and U2 and U3 and U4:
                        tot += incid(U1, U3, U2, U4, lam, p)
                ok2 &= (tot == Cs)
                # B5 Lemma 5
                prodE = 1
                for f in fs:
                    prodE *= Ex(shifted(f, p), p)
                ok5 &= Cs ** 4 <= prodE
            # B3 Jensen: sum_{t=0}^{a-1} |U(t)|^th <= a^(1-th) (sum f)^th, a = max f
            for f in fs:
                a = max(f)
                S = sum(f)
                for th in (5 / 8, 3 / 4):
                    lhs = sum(len([x for x in A if f[x] > t]) ** th for t in range(a))
                    jensen_ok &= lhs <= a ** (1 - th) * S ** th * (1 + 1e-12)
        check(ok2, f"p={p}: B2 layer-cake identity C# = sum of admissible incidence counts (exact)")
        check(jensen_ok, f"p={p}: B3 Jensen step with height gain a^(1-theta)")
        check(ok5, f"p={p}: B5 Lemma 5, C#^4 <= prod E^x(v_i) (exact)")
        # B4: 81-term split of one weight g with rational cuts.
        g = [F(0)] * p
        for x in Q:
            if x != 1 and rng.random() < 0.7:
                g[x] = F(rng.randint(1, 12), 12)
        tau0, tau1 = F(3, 12), F(7, 12)
        parts = {
            'L': [gx if gx < tau0 else F(0) for gx in g],
            'B': [gx if tau0 <= gx < tau1 else F(0) for gx in g],
            'H': [gx if gx >= tau1 else F(0) for gx in g],
        }
        Gs = sum(g)
        for lam in rng.sample(range(2, p), min(3, p - 2)):
            total = Csharp([g, g, g, g], lam, p)
            acc = F(0)
            nL = 0
            for cs in itertools.product('LBH', repeat=4):
                fs = [parts[c] for c in cs]
                term = Csharp(fs, lam, p)
                acc += term
                if 'L' in cs:
                    nL += 1
                    i = cs.index('L')
                    others = 1
                    for j in range(4):
                        if j != i:
                            others *= sum(fs[j])
                    ok4 &= term <= tau0 * others <= tau0 * Gs ** 3
            ok4 &= (acc == total) and nL == 65
        check(ok4, f"p={p}: B4 81-term split sums to C#; 65 light terms each <= tau0*G^3 (exact)")
        # B6: layer cake of g_H
        for gx in g:
            if gx >= tau1:
                # tau1 * 1 + measure of t in (tau1, 1) with gx > t = gx - tau1
                ok6 &= (tau1 + (gx - tau1) == gx)
        # do it as a genuine Riemann-free identity on the finite value set
        vals = sorted(set([tau1] + [gx for gx in g if gx > tau1] + [F(1)]))
        for x in range(p):
            gx = g[x]
            gH = gx if gx >= tau1 else F(0)
            integ = tau1 * (1 if gx >= tau1 else 0)
            for lo, hi in zip(vals, vals[1:]):
                if gx > lo:  # 1[g > t] constant on (lo, hi)
                    integ += hi - lo if gx >= hi else 0
            ok6 &= (integ == gH)
        check(ok6, f"p={p}: B6 g_H = tau1*1[g>=tau1] + int_(tau1,1) 1[g>t] dt (exact)")


# ---------------------------------------------------------------- Part C
def part_c():
    print("== C. actual-type g = |f|^2 (float) ==")
    import cmath
    rng = random.Random(1850)
    for p in (29, 37, 41, 53, 61, 73):
        n = (p - 1) // 2
        # generator of F_p^x
        def is_gen(w):
            return all(pow(w, (p - 1) // q, p) != 1 for q in range(2, p) if (p - 1) % q == 0 and all(q % r for r in range(2, q)))
        w = next(x for x in range(2, p) if is_gen(x))
        log = {}
        y = 1
        for k in range(p - 1):
            log[y] = k
            y = y * w % p
        # characters of Q: eta_j(x) = exp(2 pi i j (log x / 2) / n)
        for trial in range(3):
            supp = rng.sample(range(n), rng.randint(3, max(3, n // 3)))
            wts = [rng.random() for _ in supp]
            s = sum(wts)
            nu = {j: wt / s for j, wt in zip(supp, wts)}
            g = [0.0] * p
            for x in range(1, p):
                if log[x] % 2 == 0:
                    k = log[x] // 2
                    fx = sum(v * cmath.exp(2j * math.pi * j * k / n) for j, v in nu.items())
                    g[x] = abs(fx) ** 2
            maxnu = max(nu.values())
            okP6 = True
            for t in (0.05, 0.1, 0.2, 0.4):
                W = [x for x in range(2, p) if g[x] >= t]
                if not W:
                    continue
                for kk in (2, 3):
                    # T_k(W) = #{x1..xk = y1..yk}
                    from collections import Counter
                    prods = Counter()
                    for tup in itertools.product(W, repeat=kk):
                        pr = 1
                        for a in tup:
                            pr = pr * a % p
                        prods[pr] += 1
                    Tk = sum(c * c for c in prods.values())
                    okP6 &= t ** kk * len(W) ** (2 * kk) <= n * maxnu * Tk * (1 + 1e-9)
            check(okP6, f"p={p} trial {trial}: Prop. 6 t^k|W|^2k <= n max(nu) T_k(W), k=2,3")
            # C(lam) <= X <= E^x(h)
            h = [0.0] * p
            for z in range(1, p):
                h[z] = g[(1 - z) % p]
            def c(k):
                return sum(h[z] * h[(k * z) % p] for z in range(1, p))
            Q = squares(p)
            m = [0.0] * p
            for r in range(2, p):
                if (1 - r) % p in Q and (1 - r) % p != 1:
                    m[r] = c((1 - r) % p)
            X = sum(v * v for v in m)
            E = sum(c(k) ** 2 for k in range(1, p))
            supC = max(sum(m[r] * m[(lam * r) % p] for r in range(p)) for lam in range(2, p))
            check(supC <= X * (1 + 1e-9) <= E * (1 + 1e-9), f"p={p} trial {trial}: sup C <= X <= E^x(h)")


if __name__ == "__main__":
    part_a()
    part_b()
    part_c()
    print("ALL AUDIT CHECKS OK" if OK else "SOME CHECKS FAILED")
    sys.exit(0 if OK else 1)
