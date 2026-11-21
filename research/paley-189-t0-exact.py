#!/usr/bin/env python3
"""Round 189 (ordinary-prime-intercept-fibre-t0): exact checks of the
kappa-decomposition of T_0, the anharmonic (three-pencil) identities, the
subgroup-law equality T_0 = X and the interval-law transfer inequality.

Exact integers for random inversion-symmetric integer weights at small p
(identities that do not need 0 <= g <= 1); exact 0/1 weights for the
inequalities that drop a factor <= 1; floating point only for the interval
(Fejer) law, flagged as such.

Notation (Round 188 BPP / audit): chart mu(r,b) = g(Y) g(D), Y != D in
F_p minus {0,1}, r = (Y-D)/(1-D), b = D(1-Y)/(Y(1-D)), mask b in Q.
Delta(l,0) = sum_{r,b} mu(r,b) mu(l r, b); T_0 = sum_l g(l) Delta(l,0);
X = sum_r m(r)^2; c = sum mu^2.
psi(x) = g(1+x) (x != 0), psi(0) = 0;
c_e(k) = sum_{chi(z)=e} psi(z) psi(k z);
A_e(k) = sum_{chi(x)=e} psi(x) psi(k x) g((1+k x)/(1+x)).

Run: .venv/bin/python -B research/paley-189-t0-exact.py
"""
import math
import random
import sys

import numpy as np


def legendre_table(p):
    chi = [0] * p
    for x in range(1, p):
        chi[x * x % p] = 1
    return [0] + [1 if chi[x] else -1 for x in range(1, p)]


def chart(p, g, chi):
    inv = [0] + [pow(x, p - 2, p) for x in range(1, p)]
    mu = np.zeros((p, p), dtype=object)
    for Y in range(2, p):
        if g[Y] == 0:
            continue
        for D in range(2, p):
            if D == Y or g[D] == 0:
                continue
            b = D * (1 - Y) % p * inv[Y * (1 - D) % p] % p
            if chi[b] != 1:
                continue
            r = (Y - D) * inv[(1 - D) % p] % p
            mu[r, b] += g[Y] * g[D]
    return mu


def chart_quantities(p, g, chi):
    mu = chart(p, g, chi)
    m = [sum(mu[r, :]) for r in range(p)]
    X = sum(v * v for v in m)
    c = sum(int(v) * int(v) for v in mu.flatten())
    Delta = [0] * p
    for lam in range(1, p):
        s = 0
        for r in range(1, p):
            lr = lam * r % p
            row, row2 = mu[r, :], mu[lr, :]
            s += sum(row[b] * row2[b] for b in range(p))
        Delta[lam] = s
    T0 = sum(g[l] * Delta[l] for l in range(1, p))
    return dict(mu=mu, X=X, c=c, Delta=Delta, T0=T0)


def kappa_side(p, g, chi):
    inv = [0] + [pow(x, p - 2, p) for x in range(1, p)]
    psi = [0] * p
    for x in range(1, p):
        psi[x] = g[(1 + x) % p]
    cE = {1: [0] * p, -1: [0] * p}
    AE = {1: [0] * p, -1: [0] * p}
    for k in range(1, p):
        for z in range(1, p):
            if psi[z]:
                kz = k * z % p
                cE[chi[z]][k] += psi[z] * psi[kz]
                if psi[kz]:
                    ratio = (1 + kz) * inv[(1 + z) % p] % p
                    AE[chi[z]][k] += psi[z] * psi[kz] * g[ratio]
    Z = 0
    for x in range(1, p):
        if not psi[x]:
            continue
        for y in range(1, p):
            if psi[y]:
                Z += psi[x] ** 2 * psi[y] ** 2 * g[(1 + x) * inv[(1 + y) % p] % p]
    return psi, cE, AE, Z


def anharmonic_identities(p, g, chi, psi, AE):
    """A_e(k) re-expressed through the second and third pencils (exact identity,
    any weights): A_e(k) = sum_{chi(z)=e} psi(z) psi((1-k) z) psi(k x(z)) with
    z = -x/(1+x), and = sum over w = -kx/(1+kx) in class chi(k) e of
    psi(w) psi((1-1/k) w) psi(x)."""
    inv = [0] + [pow(x, p - 2, p) for x in range(1, p)]
    ok = True
    for k in range(2, p):
        for e in (1, -1):
            s2 = 0
            s3 = 0
            for x in range(1, p):
                if chi[x] != e or not psi[x]:
                    continue
                kx = k * x % p
                if not psi[kx]:
                    continue
                z = (-x) * inv[(1 + x) % p] % p
                s2 += psi[z] * psi[(1 - k) * z % p] * psi[kx]
                assert chi[z] == e
                w = (-kx) * inv[(1 + kx) % p] % p
                assert chi[w] == chi[k] * e
                kk = (1 - inv[k]) % p
                s3 += psi[w] * psi[kk * w % p] * psi[x]
            if s2 != AE[e][k] or s3 != AE[e][k]:
                ok = False
    return ok


def random_sym_weight(p, chi, rng, density=0.5, top=3):
    inv = [0] + [pow(x, p - 2, p) for x in range(1, p)]
    g = [0] * p
    for x in range(2, p):
        if chi[x] == 1 and g[x] == 0 and rng.random() < density:
            v = rng.randint(1, top)
            g[x] = v
            g[inv[x]] = v
    g[1] = rng.randint(1, top)
    return g


def subgroup(p, d):
    """Subgroup of F_p^* of order d (d | p-1), as a 0/1 weight."""
    for gen in range(2, p):
        if all(pow(gen, (p - 1) // q, p) != 1 for q in prime_factors(p - 1)):
            break
    h = pow(gen, (p - 1) // d, p)
    H = set()
    x = 1
    for _ in range(d):
        H.add(x)
        x = x * h % p
    return H, gen


def prime_factors(n):
    out, q = [], 2
    while q * q <= n:
        if n % q == 0:
            out.append(q)
            while n % q == 0:
                n //= q
        q += 1
    if n > 1:
        out.append(n)
    return out


def main():
    rng = random.Random(189)
    allok = True
    print("Part 1: kappa-decomposition T_0 = sum_k sum_e c_e(k) A_e(k) - Z, c = sum_e c_e(1)^2 - sum psi^4 (exact, integer weights)")
    for p in (13, 17, 29, 37, 41):
        chi = legendre_table(p)
        for trial in range(3):
            g = random_sym_weight(p, chi, rng)
            ch = chart_quantities(p, g, chi)
            psi, cE, AE, Z = kappa_side(p, g, chi)
            rhs = sum(cE[e][k] * AE[e][k] for e in (1, -1) for k in range(1, p)) - Z
            c_rhs = sum(cE[e][1] ** 2 for e in (1, -1)) - sum(v ** 4 for v in psi)
            # X = sum_{beta in Q minus 1} (c_+ + c_-)(beta)^2 (Lemma A1 form)
            X_rhs = sum((cE[1][b] + cE[-1][b]) ** 2 for b in range(2, p) if chi[b] == 1)
            anh = anharmonic_identities(p, g, chi, psi, AE)
            ok = (rhs == ch["T0"]) and (c_rhs == ch["c"]) and (X_rhs == ch["X"]) and anh
            allok &= ok
            print(f"  p={p:3d} t={trial} T0={ch['T0']} X={ch['X']} c={ch['c']} kappa-form={'ok' if rhs == ch['T0'] else 'FAIL'} c={'ok' if c_rhs == ch['c'] else 'FAIL'} X={'ok' if X_rhs == ch['X'] else 'FAIL'} anharmonic identities={'ok' if anh else 'FAIL'}")

    print("Part 2: three-pencil inequality A_e(k) <= min(c_e(k), c_e(1-k), c_{chi(k)e}(1-1/k)) and")
    print("        T_0 - c <= sum_{k!=1} sum_e c_e(k) min(...) (exact, 0/1 inversion-symmetric weights)")
    for p in (29, 37, 41, 53, 61):
        chi = legendre_table(p)
        inv = [0] + [pow(x, p - 2, p) for x in range(1, p)]
        for trial in range(3):
            g = random_sym_weight(p, chi, rng, density=0.6, top=1)
            g[1] = 1
            ch = chart_quantities(p, g, chi)
            psi, cE, AE, Z = kappa_side(p, g, chi)
            okk = True
            bound = 0
            for k in range(2, p):
                for e in (1, -1):
                    m3 = min(cE[e][k], cE[e][(1 - k) % p], cE[chi[k] * e][(1 - inv[k]) % p])
                    if AE[e][k] > m3:
                        okk = False
                    bound += cE[e][k] * m3
            okb = ch["T0"] - ch["c"] <= bound
            allok &= okk and okb
            print(f"  p={p:3d} t={trial} T0-c={ch['T0'] - ch['c']:5d} coupled bound={bound:5d} X-c={ch['X'] - ch['c']:5d} pointwise={'ok' if okk else 'FAIL'} sum={'ok' if okb else 'FAIL'}")

    print("Part 3: subgroup laws g = 1_H (H <= Q): T_0 = X exactly, and c_e(k) = c_e(1-k) = c_{chi(k)e}(1-1/k)")
    for p, d in ((29, 7), (37, 9), (41, 5), (53, 13), (61, 15), (73, 9), (97, 12), (101, 25), (109, 27)):
        if (p - 1) % d or ((p - 1) // 2) % d:
            continue
        chi = legendre_table(p)
        inv = [0] + [pow(x, p - 2, p) for x in range(1, p)]
        H, _ = subgroup(p, d)
        assert all(chi[h] == 1 for h in H)
        g = [1 if x in H else 0 for x in range(p)]
        ch = chart_quantities(p, g, chi)
        psi, cE, AE, Z = kappa_side(p, g, chi)
        inv_ok = all(cE[e][k] == cE[e][(1 - k) % p] == cE[chi[k] * e][(1 - inv[k]) % p] for k in range(2, p) for e in (1, -1))
        ok = ch["T0"] == ch["X"] and inv_ok
        allok &= ok
        print(f"  p={p:3d} |H|={d:3d} T0={ch['T0']} X={ch['X']} equal={'yes' if ch['T0'] == ch['X'] else 'NO'} anharmonic invariance={'ok' if inv_ok else 'FAIL'}")

    print("Part 4: interval (Fejer) law, transfer T_0(g_J) >= (4/pi^2)^5 X(1_I) (floating; g computed in double precision)")
    for p in (101, 197, 257):
        chi = legendre_table(p)
        n = (p - 1) // 2
        # generator of F_p^*, gamma^2 generates Q
        for gen in range(2, p):
            if all(pow(gen, (p - 1) // q, p) != 1 for q in prime_factors(p - 1)):
                break
        g2 = gen * gen % p
        L = max(1, round(n / math.sqrt(p)))
        logq = {}
        x = 1
        for k in range(n):
            logq[x] = k
            x = x * g2 % p
        gF = [0.0] * p
        for x, k in logq.items():
            kk = k if k <= n // 2 else k - n
            if kk == 0:
                gF[x] = 1.0
            else:
                gF[x] = (math.sin(math.pi * L * kk / n) / (L * math.sin(math.pi * kk / n))) ** 2
        K = n // (4 * L)
        I = {x for x, k in logq.items() if min(k, n - k) <= K}
        gI = [1 if x in I else 0 for x in range(p)]
        minI2 = min(gF[x * pow(y, p - 2, p) % p] for x in I for y in I)
        chF = chart_quantities(p, gF, chi)
        chI = chart_quantities(p, gI, chi)
        lhs = chF["T0"]
        rhs = (4 / math.pi ** 2) ** 5 * chI["X"]
        ok = lhs >= rhs and minI2 >= 4 / math.pi ** 2 - 1e-12
        allok &= ok
        print(f"  p={p:3d} L={L} |I|={len(I)} min g on I/I={minI2:.4f} (>= 4/pi^2=0.4053) T0(g_J)={lhs:.3f} X(g_J)={chF['X']:.3f} X(1_I)={chI['X']} T0(1_I)={chI['T0']} ratio T0(g_J)/X(1_I)={lhs / chI['X']:.4f} {'ok' if ok else 'FAIL'}")

    print("ALL EXACT CHECKS OK" if allok else "SOME CHECK FAILED")
    return 0 if allok else 1


if __name__ == "__main__":
    sys.exit(main())
