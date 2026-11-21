#!/usr/bin/env python3
r"""Round 187 audit (session/r187-audit): independent checks of the cold report
`native-claude-cold-prime-b-word-delocalization-187.md` (COLD).

Own implementation; imports no project script.

Part A (outward python-flint arb): Lemma 3 constants.  l_S^2 = 1 - sqrt(4a/(4a+8)) in closed form;
   l(c)^2 = E[Phi_a'((sqrt8|cos th| - c)_+)^2] and q_ang(c)^2 = E[Phi_a'(sqrt8|cos th| + c)^2] by
   monotone Riemann sums with 20000 cells (the report uses 4000); l(0) against l_S; the Corollary 1.2
   exponent log10(0.00042 l(2.338)^611) and log10(2 rho / c_9).
Part B (exact Fractions / outward arb): Proposition M (random vectors, exact), Corollary M1 constants,
   Dirichlet(1/2) variance formula of Proposition H step 4 (exact symbolic), the Criterion D budget
   thresholds, the allowances 1/q.
Part C (floating; evidence): Proposition H at moderate n: Haar-eigenbasis involution with the Paley
   trace, sup/RMS of K_U y for adversarial y (spike, sign vector, smooth) against sqrt(2 ln n), and the
   same for the physical Paley K (even rows) for comparison.

Usage: .venv/bin/python -B research/paley-187-audit-cold-check.py
"""
import math
import random
from fractions import Fraction as Fr

import numpy as np
from flint import arb, ctx

ctx.prec = 200
OK = True


def check(cond, msg):
    global OK
    print(("ok   " if cond else "FAIL ") + msg)
    if not cond:
        OK = False


A_T = arb(2031) / 128
FOUR_A = 4 * A_T
SQ8 = arb(8).sqrt()


def phip(y):
    """Phi_a'(y) = y / sqrt(4a + y^2) for real y >= 0 (arb)."""
    return y / (FOUR_A + y * y).sqrt()


def riemann(fun, cells):
    """Average over theta in [0, pi/2] of a NONINCREASING function of theta; returns (lower, upper)."""
    h = arb.pi() / 2 / cells
    lo = arb(0)
    hi = arb(0)
    prev = fun(arb(0))
    for k in range(1, cells + 1):
        cur = fun(h * k)
        hi += prev
        lo += cur
        prev = cur
    return lo / cells, hi / cells


def part_a():
    print('== Part A: Lemma 3 constants (outward arb, own Riemann sums, 20000 cells) ==')
    lS2 = 1 - (FOUR_A / (FOUR_A + 8)).sqrt()
    lS = lS2.sqrt()
    check(arb('0.2400605').lower() < lS.lower() and lS.upper() < arb('0.2400607').upper(),
          f'l_S = {lS.str(10)} (report [0.2400606, 0.2400606])')
    cells = 20000

    def lc(c):
        cc = arb(c)

        def f(th):
            x = SQ8 * th.cos() - cc
            if x > 0:
                pass
            elif x.upper() <= 0:
                x = arb(0)
            else:                                # straddles 0: enclose (x)_+ by [0, upper(x)]
                x = arb(0).union(x.upper())
            return phip(x) ** 2
        lo, hi = riemann(f, cells)
        return lo.sqrt(), hi.sqrt()

    def qa(c):
        cc = arb(c)
        lo, hi = riemann(lambda th: phip(SQ8 * th.cos() + cc) ** 2, cells)
        return lo.sqrt(), hi.sqrt()

    rep_l = {'2.338': (0.027565, 0.027582), '1.988': (0.054027, 0.054052), '0.985': (0.143017, 0.143061),
             '0': (0.240031, 0.240090)}
    for c, (a, b) in rep_l.items():
        lo, hi = lc(c)
        inside = float(lo.lower()) >= a - 1e-6 and float(hi.upper()) <= b + 1e-6
        check(inside or (float(lo.lower()) <= b and float(hi.upper()) >= a),
              f'l({c}) in [{float(lo.lower()):.6f}, {float(hi.upper()):.6f}] (report [{a}, {b}])')
    check(lc('0')[0].lower() <= lS.upper() and lS.lower() <= lc('0')[1].upper(), 'l(0) encloses l_S')
    for c, (a, b) in {'1.94': (0.428191, 0.428251), '2.338': (0.462690, 0.462748)}.items():
        lo, hi = qa(c)
        check(float(lo.lower()) <= b and float(hi.upper()) >= a,
              f'q_ang({c}) in [{float(lo.lower()):.6f}, {float(hi.upper()):.6f}] (report [{a}, {b}])')
    lo, _ = lc('2.338')
    lg = (arb('0.00042').log() + 611 * lo.lower().log()) / arb(10).log()
    lg_rep = (arb('0.00042').log() + 611 * arb('0.027565').log()) / arb(10).log()
    check(abs(float(lg_rep) + 956.317) < 2e-3 and lg_rep < lg,
          f'log10(0.00042 * 0.027565^611) = {float(lg_rep):.3f} (report -956.317); with the tighter own '
          f'lower end it is {float(lg.upper()):.3f}, so the report figure is a valid (conservative) lower bound')
    rat = (arb('0.75').log() / arb(10).log()) - lg_rep
    check(abs(float(rat) - 956.192) < 2e-3, f'log10(2 rho / c_9) = {float(rat):.3f} with rho = 3/8 (report 956.192)')
    q_up = qa('2.338')[1]
    check(float((1 / q_up).lower()) >= 2.1610, f'1/q_ang(2.338) >= {float((1 / q_up).lower()):.4f}')
    # 1/q for counting rates
    for q in ('0.5145', '0.5174', '0.518', '0.535', '0.545'):
        print(f'   1/{q} = {float(1 / arb(q)):.4f}')
    check(float(1 / arb('0.5145')) < 1.9437, 'max allowance 1/q < 1.9437 (report 1.9436)')


def part_b():
    print('== Part B: Proposition M, Corollary M1, Proposition H step 4 (exact) ==')
    rng = random.Random(187)
    bad = 0
    for trial in range(400):
        n = rng.randint(2, 40)
        f = [Fr(rng.randint(-50, 50), rng.randint(1, 9)) for _ in range(n)]
        if all(x == 0 for x in f):
            continue
        rms2 = sum(x * x for x in f) / n
        mx2 = max(x * x for x in f)
        for m in range(1, 6):
            M = sum((x * x / rms2) ** m for x in f) / n
            # M^(1/2m) <= Rat <= (n M)^(1/2m)  <=>  M <= Rat^(2m) <= n M
            R2m = (mx2 / rms2) ** m
            if not (M <= R2m <= n * M):
                bad += 1
    check(bad == 0, 'Proposition M: M_2m <= Rat^(2m) <= n M_2m on 400 random rational vectors, m = 1..5 (exact)')
    # Stirling: ((2m-1)!!)^(1/(2m)) >= sqrt(2m/e) for m <= 200 (outward)
    okst = True
    df = arb(1)
    for m in range(1, 201):
        df *= (2 * m - 1)
        if not (df.log() / (2 * m) > (arb(2 * m) / arb(1).exp()).log() / 2):
            okst = False
    check(okst, '((2m-1)!!)^(1/(2m)) > sqrt(2m/e) for m = 1..200 (outward)')
    check(float((arb(1) / 2).exp()) < 1.6488, 'n^(1/(2m)) <= e^(1/2) for m >= ln n')
    # Dirichlet(1/2,...,1/2) in N coordinates: Var xi = (N-1)/(N^2 (N/2+1)), Cov = -1/(N^2 (N/2+1))
    good = True
    for N in range(2, 60):
        for tr in range(-N, N + 1, 2):        # trace of a +-1 diagonal of size N
            v = Fr(N - 1, N * N) / (Fr(N, 2) + 1)
            c = Fr(-1, N * N) / (Fr(N, 2) + 1)
            var = N * v + (tr * tr - N) * c
            closed = (1 - Fr(tr * tr, N * N)) * Fr(2, N + 2)
            if var != closed or var > Fr(2, N + 2):
                good = False
    check(good, 'Proposition H step 4: Var(sum lambda_j xi_j) = (1 - tr^2/N^2) 2/(N+2) <= 2/(N+2) (exact, N < 60)')
    # budget thresholds
    for lam, rep in ((arb('6.5e205'), 410.9626), (arb('9.4e206'), 413.2830)):
        t = (lam * lam / (2 * arb(10).log())).log() / arb(10).log()
        check(abs(float(t) - rep) < 1e-4, f'sqrt(2 ln n) >= {lam.str(2)} iff log10 log10 n >= {float(t):.4f} (report {rep})')


def paley_K_eigs(p):
    n = (p - 1) // 2
    # generator of F_p^x
    fac = []
    m, d = p - 1, 2
    while d * d <= m:
        if m % d == 0:
            fac.append(d)
            while m % d == 0:
                m //= d
        d += 1
    if m > 1:
        fac.append(m)
    g = next(x for x in range(2, p) if all(pow(x, (p - 1) // q, p) != 1 for q in fac))
    chi = lambda x: 0 if x % p == 0 else (1 if pow(x, (p - 1) // 2, p) == 1 else -1)
    lam = np.array([chi(1 - pow(g, 2 * j, p)) for j in range(n)], dtype=float)
    return n, lam


def part_c():
    print('== Part C: Proposition H model vs physical K (floating; evidence only) ==')
    rng = np.random.default_rng(187)
    for p in (2017, 8009):
        n, lam = paley_K_eigs(p)
        check(lam[0] == 0 and abs(lam.sum() + 1) < 1e-9 and set(np.unique(lam[1:])) <= {-1.0, 1.0},
              f'p={p}: Paley spectrum lambda_0 = 0, others +-1, sum = -1')
        # Haar model on E0 = 1^perp: random orthonormal basis of E0 (QR of Gaussian), spectrum lam[1:]
        Z = rng.standard_normal((n, n - 1))
        Z -= Z.mean(axis=0, keepdims=True)
        Qm, _ = np.linalg.qr(Z)
        KU = (Qm * lam[1:]) @ Qm.T
        # physical K: real symmetric circulant with eigenvalues lam (Fourier basis); K x = ifft(lam * fft(x))
        Kphys = lambda x: np.real(np.fft.ifft(lam * np.fft.fft(x)))
        ys = {'spike e_1': np.eye(n)[1], 'sign vector': rng.choice([-1.0, 1.0], n),
              'smooth cos': np.cos(2 * np.pi * np.arange(n) / n), 'e_0 (seed S/2sqrt n)': np.eye(n)[0]}
        ref = math.sqrt(2 * math.log(n))
        for name, y in ys.items():
            fu = KU @ y
            fp = Kphys(y)
            ru = np.max(np.abs(fu[1:])) / np.sqrt(np.mean(fu ** 2))
            rp = np.max(np.abs(fp[1:])) / np.sqrt(np.mean(fp ** 2))
            print(f'   p={p} n={n} y={name:22s}: Haar model Rat/sqrt(2ln n) = {ru / ref:.3f};  physical K: {rp / ref:.3f}')
        print('   (Haar model near 1 for every input; physical K on e_0 (and on any spike, by circulance) gives S, ratio sqrt2.)')


if __name__ == '__main__':
    part_a()
    part_b()
    part_c()
    print('ALL AUDIT CHECKS OK' if OK else 'SOME AUDIT CHECKS FAILED')
