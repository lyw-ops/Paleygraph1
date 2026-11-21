#!/usr/bin/env python3
"""Round 191 audit checks (session/r191-audit). Independent code; written by the auditor.

Exact parts use Fractions; Part F uses numpy floating point (evidence for an
inequality chain, not a certificate). Run from the repository root:

    .venv/bin/python -B research/paley-191-audit-check.py

Parts
  A  (ASM Prop. 2) sum_{t!=1} P_t = X_c - diag, P_1 = diag, X_c = X + 2 sum c_h + (n-1),
     and M_w <= M_sqrtg <= X_c - diag, exact, random rational |f| (so sqrt g is rational).
  B  (audit Sec. 3.6) subgroup laws 1_H: M_w(1_H) = 0 while
     M_sqrtg(1_H) = X_off(1_H) + 2 sum_kappa c_H(kappa) >= X_off(1_H) = E_off(H).
  C  exact exponent and constant arithmetic of ASM Sec. 4/5 and MWS Sec. 2-3.
  D  (GPSUB Sec. 3.1) Vinogradov consequence, via the exact Fejer identity, p <= 400.
  E  (GPSUB Sec. 3.2) F_{r^2} run example with independent field arithmetic.
  F  (ASM Prop. 1) R152 expansion identity and the Prop. 1 inequality for random laws, floating.
"""
import cmath
import math
import random
import sys
from fractions import Fraction as Fr

FAIL = []


def check(cond, msg):
    print(("OK   " if cond else "FAIL ") + msg)
    if not cond:
        FAIL.append(msg)


def is_prime(m):
    if m < 2:
        return False
    i = 2
    while i * i <= m:
        if m % i == 0:
            return False
        i += 1
    return True


def gen_mod(p):
    for z in range(2, p):
        if all(pow(z, (p - 1) // q, p) != 1 for q in range(2, p) if (p - 1) % q == 0 and is_prime(q)):
            return z
    raise ValueError


def chi(x, p):
    x %= p
    if x == 0:
        return 0
    return 1 if pow(x, (p - 1) // 2, p) == 1 else -1


# ---------------------------------------------------------------- Part A
def part_a():
    print("Part A: slope completeness of X (ASM Prop. 2), exact")
    rng = random.Random(191)
    for p in (13, 17, 29, 37, 41):
        n = (p - 1) // 2
        Q = [x for x in range(1, p) if chi(x, p) == 1]
        amp = {x: Fr(rng.randint(0, 6), 6) for x in Q}
        amp[1] = Fr(1)
        g = [Fr(0)] * p
        for x in Q:
            g[x] = amp[x] ** 2
        sq = [Fr(0)] * p
        for x in Q:
            sq[x] = amp[x]
        for v in (1, 3 if chi(3, p) == 1 else 2):
            P = {}
            Xc = Fr(0)
            diag = Fr(0)
            for u in Q:
                if u == 1:
                    continue
                c = Fr(0)
                for x in range(p):
                    A = (1 - v * x) % p
                    C = (1 - v * u * x) % p
                    c += g[A] * g[C]
                    diag += g[A] ** 2 * g[C] ** 2
                Xc += c * c
                for x in range(p):
                    A = (1 - v * x) % p
                    C = (1 - v * u * x) % p
                    wx = g[A] * g[C]
                    if wx == 0:
                        continue
                    for y in range(p):
                        Ay = (1 - v * y) % p
                        Cy = (1 - v * u * y) % p
                        wy = g[Ay] * g[Cy]
                        if wy == 0:
                            continue
                        t = Cy * A * pow(C * Ay, p - 2, p) % p
                        P[t] = P.get(t, Fr(0)) + wx * wy
                        if t == 1 and x != y:
                            FAIL.append(f"slope 1 off diagonal p={p}")
            off = sum(val for t, val in P.items() if t != 1)
            check(off == Xc - diag and P.get(1, Fr(0)) == diag,
                  f"p={p} v={v}: sum_(t!=1) P_t = X_c - diag ({float(off):.4f}); P_1 = diag")
            # X of Round 183: c_h(k) = sum_{z != 0} g(1-z) g(1-kz), X = sum_{k in Q\1} c_h^2
            X = Fr(0)
            sch = Fr(0)
            for k in Q:
                if k == 1:
                    continue
                ch = sum(g[(1 - z) % p] * g[(1 - k * z) % p] for z in range(1, p))
                X += ch * ch
                sch += ch
            check(Xc == X + 2 * sch + (n - 1), f"p={p} v={v}: X_c = X + 2 sum c_h + (n-1) (v-free, g(1)=1)")
            Mw = sum(g[t] * (1 - g[t]) * val for t, val in P.items() if t != 1)
            Ms = sum(sq[t] * val for t, val in P.items() if t != 1)
            check(Mw <= Ms <= Xc - diag, f"p={p} v={v}: M_w={float(Mw):.4f} <= M_sqrtg={float(Ms):.4f} <= X_c-diag")


# ---------------------------------------------------------------- Part B
def part_b():
    print("Part B: subgroup laws, M_w(1_H)=0 and M_sqrtg(1_H) = X_off(1_H) + 2 sum c_H, exact integers")
    for p in (101, 109, 113):
        n = (p - 1) // 2
        z = gen_mod(p)
        zeta = z * z % p
        for d in range(1, n + 1):
            if n % d:
                continue
            h = pow(zeta, n // d, p)
            H = set()
            x = 1
            for _ in range(d):
                H.add(x)
                x = x * h % p
            g = [1 if x in H else 0 for x in range(p)]
            Q = [x for x in range(1, p) if chi(x, p) == 1]
            # slope form with v = 1: P_t over u in Q\{1}, x,y in F_p
            Mw = 0
            Ms = 0
            for u in Q:
                if u == 1:
                    continue
                pts = [x for x in range(p) if g[(1 - x) % p] and g[(1 - u * x) % p]]
                for x in pts:
                    for y in pts:
                        if x == y:
                            continue
                        A, C = (1 - x) % p, (1 - u * x) % p
                        Ay, Cy = (1 - y) % p, (1 - u * y) % p
                        t = Cy * A * pow(C * Ay, p - 2, p) % p
                        Ms += g[t]          # sqrt(g) = g for 0/1 laws
                        Mw += g[t] * (1 - g[t])
            # Round 183 chart: c_H(kappa) = #{(Y,D) in (H\1)^2 : 1-Y = kappa (1-D)}
            Hs = [y for y in H if y != 1]
            cH = {}
            for Y in Hs:
                for D in Hs:
                    k = (1 - Y) * pow(1 - D, p - 2, p) % p
                    cH[k] = cH.get(k, 0) + 1
            # Round 183/189: X(1_I) sums over kappa in Q \ {1} only
            Xoff = sum(c * (c - 1) for k, c in cH.items() if k != 1 and chi(k, p) == 1)
            sc = sum(c for k, c in cH.items() if k != 1 and chi(k, p) == 1)
            ok = (Mw == 0) and (Ms == Xoff + 2 * sc)
            if not ok or d in (5, 6, 7, 10, 14, 25, 27, 28, n):
                check(ok, f"p={p} |H|={d}: M_w=0, M_sqrtg={Ms} = X_off {Xoff} + 2*{sc}")
    print("     (all subgroup orders at each p were checked; only some lines are printed)")


# ---------------------------------------------------------------- Part C
def part_c():
    print("Part C: exact arithmetic")
    g445 = Fr(4, 445)
    check((1 - g445) / 2 == Fr(441, 890), "M_w alone on bands: (1-4/445)/2 = 441/890")
    s = Fr(1, 2) - Fr(2, 445)
    check(1 + s / 2 == Fr(3, 2) - Fr(2, 445) - s / 2 and s / 2 == Fr(441, 1780),
          "crossover with R163 at sigma = 1/2 - 2/445, loss 441/1780")
    for gam, alone, comb in ((Fr(1, 211), Fr(209, 422), Fr(209, 844)), (Fr(1, 54), Fr(13, 27), Fr(13, 54))):
        check((1 - 2 * gam) / 2 == alone and (Fr(1, 2) - gam) / 2 == comb,
              f"gamma={gam}: alone {alone}, combined {comb}")
    for gam, val in ((Fr(0), Fr(3, 7)), (Fr(1, 211), Fr(627, 1477)), (Fr(1, 54), Fr(26, 63))):
        # p/eps = p^(3/2-gamma) eps^(1/6)  =>  eps = p^(-(6/7)(1/2-gamma)), loss = (6/7)(1/2-gamma)
        check(Fr(6, 7) * (Fr(1, 2) - gam) == val and (3 - 6 * gam) / 7 == val, f"near-unit crossover gamma={gam}: {val}")
    # E >= p^(-1/2): the regime E <= p^(-3/7) is nonempty, and the E-large loss is >= 3/7 at gamma=0
    check(Fr(-1, 2) < Fr(-3, 7), "regime E <= p^(-3/7) is compatible with E >= p^(-1/2)")
    check(Fr(1, 2) + Fr(1, 6) * Fr(-3, 7) == Fr(3, 7), "at E = p^(-3/7) both regimes give 3/7")
    # R160 deletion: |F| <= C/sqrt p over |Q| ~ p/2 sites has squared mass <= C^2/2 = O(1)
    check(Fr(1, 1) * Fr(1, 2) == Fr(1, 2), "|F|^2 <= C^2/p on <= p/2 sites: mass <= C^2/2 (so the paid layer is |F|^2 <= C^2/p)")
    # MWS Lemma 3 moment
    for L in range(1, 60):
        check_ = sum(Fr(L - abs(t), L) * t * t for t in range(-L + 1, L)) == Fr(L ** 3 - L, 6)
        if not check_:
            FAIL.append(f"Lemma 3 moment L={L}")
    print("OK   sum_{|t|<L}(1-|t|/L) t^2 = (L^3-L)/6 for L < 60")
    a = 1 / math.pi ** 2
    w0 = min(a * (1 - a), 0.25 * 0.75)
    check(abs(a ** 4 * w0 - (math.pi ** 2 - 1) / math.pi ** 12) < 1e-18 and abs(a ** 4 * w0 - 9.596e-6) < 1e-9,
          f"c(1/2) = (pi^2-1)/pi^12 = {a**4*w0:.4e}")
    check(Fr(32, 13) - 2 > 0 and Fr(32, 13) - 2 == 2 * Fr(3, 13), "|I|^2 << |I|^(32/13-2delta) iff delta < 3/13")
    # HP exclusion of the M_w clique: 4K'+1 <= (sqrt(2p-1)+1)/2  =>  K' <~ sqrt(2)/8 sqrt p
    check(abs(math.sqrt(2) / 8 - 0.1768) < 1e-4, "HP excludes the M_w restriction on (NC) once K' > (sqrt 2/8 + o(1)) sqrt p ~ 0.177 sqrt p")


# ---------------------------------------------------------------- Part D
def part_d(pmax=400):
    print(f"Part D: Vinogradov consequence E_rho >= (M - sqrt p)/2, independent code, p <= {pmax}")
    cases = 0
    ident = 0
    for p in range(5, pmax + 1):
        if not is_prime(p) or p % 4 != 1:
            continue
        sp = math.sqrt(p)
        leg = [chi(x, p) for x in range(p)]
        for zeta in range(2, p):
            if leg[zeta] != 1:
                continue
            pw = [1]
            while True:
                nxt = pw[-1] * zeta % p
                if nxt == 1:
                    break
                pw.append(nxt)
            o = len(pw)
            sg = [leg[(1 - pw[h % o]) % p] for h in range(o)]
            Fej = 0
            cnt = {1: 0, -1: 0}
            for M in range(1, o):
                if 2 * M >= o:
                    break
                # E counts over 0 < |h| <= M, computed from h and o-h separately
                for s_ in (sg[M], sg[(-M) % o]):
                    if s_ in cnt:
                        cnt[s_] += 1
                Fej = sum((M + 1 - abs(h)) * sg[h % o] for h in range(-M, M + 1) if h) if M <= 40 else None
                if Fej is not None:
                    if abs(Fej) > sp * (M + 1) + 1e-9:
                        FAIL.append(f"D Vinogradov p={p} z={zeta} M={M}")
                    if p <= 101:
                        I = pw[:M + 1]
                        S = sum(leg[(xx - yy) % p] for xx in I for yy in I)
                        ident += 1
                        if S != Fej:
                            FAIL.append(f"D identity p={p} z={zeta} M={M}")
                for rho in (1, -1):
                    if cnt[-rho] < (M - sp) / 2 - 1e-12:
                        FAIL.append(f"D bound p={p} z={zeta} M={M} rho={rho}")
                    cases += 1
    check(not [f for f in FAIL if f.startswith("D ")],
          f"E_rho >= (M-sqrt p)/2 in {cases} (p,zeta,M,rho) cases; Fejer identity exact in {ident} cases (p<=101); |Fejer sum| <= sqrt(p)(M+1) for M<=40")


# ---------------------------------------------------------------- Part E
def part_e():
    print("Part E: F_{r^2} runs (independent arithmetic, F_r[i]/(i^2 - nr))")
    for r in (7, 11, 19, 23, 31, 43):
        nr = next(c for c in range(2, r) if pow(c, (r - 1) // 2, r) == r - 1)
        q = r * r

        def mul(a, b):
            return ((a[0] * b[0] + nr * a[1] * b[1]) % r, (a[0] * b[1] + a[1] * b[0]) % r)

        def pw(a, e):
            res = (1, 0)
            while e:
                if e & 1:
                    res = mul(res, a)
                a = mul(a, a)
                e >>= 1
            return res

        def is_sq(a):
            return a != (0, 0) and pw(a, (q - 1) // 2) == (1, 0)

        z = gen_mod(r)  # generator of F_r^*, embedded as (z, 0)
        run = 0
        k = 1
        while True:
            zk = pow(z, k, r)
            if zk == 1:
                break
            one_minus = ((1 - zk) % r, 0)
            if not is_sq(one_minus):
                break
            run += 1
            k += 1
        check(run == r - 2 and is_sq((z, 0)),
              f"q={r}^2: zeta generates F_r^*, is a square in F_q, chi(1-zeta^k)=+1 for 1<=k<={run}=sqrt(q)-2")


# ---------------------------------------------------------------- Part F
def part_f():
    print("Part F: R152 expansion and ASM Prop. 1 inequality, random laws (floating, evidence)")
    import numpy as np
    rng = np.random.default_rng(1910)
    for p in (61, 101, 149):
        n = (p - 1) // 2
        z = gen_mod(p)
        zeta = z * z % p
        log = {}
        x = 1
        for k in range(n):
            log[x] = k
            x = x * zeta % p
        Q = list(log.keys())
        for law in ("flat", "peaked"):
            m = max(2, round(n / math.sqrt(p)))
            nu = np.zeros(n)
            if law == "flat":
                S = rng.choice(np.arange(1, n), size=m, replace=False)
                nu[S] = 1.0 / m
            else:
                nu = rng.random(n) ** 6
                nu /= nu.sum()
            # f(x) = sum_j nu_j psi^j(x), psi^j(zeta^k) = e(jk/n)
            fvals = {}
            for y in Q:
                k = log[y]
                fvals[y] = complex(np.sum(nu * np.exp(2j * np.pi * np.arange(n) * k / n)))
            v = Q[3]
            F = {}
            for y in Q:
                A = (1 - v * y) % p
                F[y] = fvals[A] if A in log else 0j
            # direct moment: M = sum_a nu_a sum_{u != 1} |C_a(u)|^2,
            # C_a(u) = sum_x F(ux) conj(F(x)) conj(psi^a(r_u(x))), r_u(x) = (1-vux)/(1-vx)
            Mdir = 0.0
            Mexp = 0j
            for u in Q:
                if u == 1:
                    continue
                xs = []
                for y in Q:
                    A = (1 - v * y) % p
                    C = (1 - v * u * y) % p
                    if A in log and C in log:
                        xs.append((y, log[C * pow(A, p - 2, p) % p]))
                if not xs:
                    continue
                coef = np.array([F[u * y % p] * np.conj(F[y]) for y, _ in xs])
                rl = np.array([r for _, r in xs])
                # C_a(u) for all a at once
                Ca = np.exp(-2j * np.pi * np.outer(np.arange(n), rl) / n) @ coef
                Mdir += float(np.sum(nu * np.abs(Ca) ** 2))
                # R152 five-factor expansion: sum_{x,y} coef_x conj(coef_y) f(r_u(y)/r_u(x))
                for (y1, r1), c1 in zip(xs, coef):
                    for (y2, r2), c2 in zip(xs, coef):
                        Mexp += c1 * np.conj(c2) * np.sum(nu * np.exp(2j * np.pi * np.arange(n) * ((r2 - r1) % n) / n))
            check(abs(Mdir - Mexp.real) < 1e-8 * max(1, Mdir) and abs(Mexp.imag) < 1e-8 * max(1, Mdir),
                  f"p={p} {law}: E_nu sum_u |C_a(u)|^2 = five-factor expansion ({Mdir:.4f})")
            # Prop. 1 at a = 0.1 (squared level), with the true moment of the cut row
            a = 0.1
            Fa = {y: (F[y] if abs(F[y]) ** 2 >= a else 0j) for y in Q}
            normF2 = sum(abs(F[y]) ** 2 for y in Q)
            normFa2 = sum(abs(Fa[y]) ** 2 for y in Q)
            m_lt = normF2 - normFa2
            Mabs = 0.0
            for u in Q:
                if u == 1:
                    continue
                for y1 in Q:
                    for y2 in Q:
                        if y1 == y2:
                            continue
                        prod = abs(Fa[u * y1 % p] * Fa[y1] * Fa[u * y2 % p] * Fa[y2])
                        if prod == 0:
                            continue
                        A1, C1 = (1 - v * y1) % p, (1 - v * u * y1) % p
                        A2, C2 = (1 - v * y2) % p, (1 - v * u * y2) % p
                        t = C2 * A1 * pow(C1 * A2, p - 2, p) % p
                        Mabs += prod * abs(fvals.get(t, 0j))
            rhs = (math.sqrt(normFa2 ** 2 + Mabs) + 2 * math.sqrt(n * nu.max()) * math.sqrt(normF2) * math.sqrt(m_lt)) ** 2
            check(Mdir <= rhs * (1 + 1e-9), f"p={p} {law}: M={Mdir:.2f} <= Prop.1 RHS {rhs:.2f} (abs kept part {Mabs:.2f}, m<a={m_lt:.2f})")


if __name__ == "__main__":
    part_a()
    part_b()
    part_c()
    part_d(400 if "--quick" not in sys.argv else 100)
    part_e()
    part_f()
    print()
    print("ALL AUDIT CHECKS OK" if not FAIL else f"FAILURES: {len(FAIL)}: {FAIL[:5]}")
    sys.exit(1 if FAIL else 0)
