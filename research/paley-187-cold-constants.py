#!/usr/bin/env python3
"""Round 187 cold call `cold-prime-b-word-delocalization`: exact / outward-rounded constants (label (a)).

Own implementation; python-flint arb balls (outward rounding) and exact Fractions.  Nothing here uses floating
evidence except where a line is explicitly marked [float input].

  1. Exact compact seed counting rate: l_S(a)^2 = E_theta[Phi_a'(sqrt8 cos theta)^2] = 1 - sqrt(4a/(4a+8)).
  2. Weighted-test lower rate l(c)^2 = E_theta[Phi_a'((sqrt8|cos theta| - c)_+)^2] (Lemma 3 of the report),
     certified by lower/upper Riemann sums of a monotone integrand, for the inherited cap c = 2.338 and
     comparison caps; the Round 179 indicator-test constant 0.349/8/sqrt5 for comparison.
  3. Theorem 1 real-floor constant: log10 of 0.00042 * rate^611.
  4. Proposition M: ((2m-1)!!)^(1/(2m)) and sqrt(2 ln n / e) lower bounds; the size n at which
     sqrt(2 ln n) reaches the Round 180 Criterion D budgets 6.5e205 and 9.4e206.
  5. Rate comparison behind the heuristic of Section 5: theta = (inherited seed price rate)/l_S against 1/q
     for the certified counting rates, and the coordinate cap v with Phi_a'(v) = 1/theta.
Replay: .venv/bin/python -B research/paley-187-cold-constants.py   (a few seconds)
"""
from fractions import Fraction

from flint import arb, ctx

ctx.prec = 200
a = arb(2031) / 128
four_a = 4 * a
s8 = arb(8).sqrt()
pi = arb.pi()


def dphi(x):
    return x / (four_a + x * x).sqrt()


def fmt(x, d=6):
    return f'[{float(x.lower()):.{d}f}, {float(x.upper()):.{d}f}]'


print('== 1. exact compact seed counting rate at t = a ==')
lS2 = 1 - (four_a / (four_a + 8)).sqrt()
lS = lS2.sqrt()
print('  E[Phi_a\'(S)^2] = 1 - sqrt(4a/(4a+8)) with S = sqrt8 cos(theta), theta Haar  (E 1/(A+B cos^2) = 1/sqrt(A(A+B)))')
print(f'  l_S^2 in {fmt(lS2, 7)};  l_S in {fmt(lS, 7)}')


def lrate(c, N=4000):
    """bracket for l(c)^2 = (2/pi) int_0^{pi/2} g(theta) dtheta, g = Phi_a'((sqrt8 cos theta - c)_+)^2, g nonincreasing."""
    c = arb(c)
    vals = []
    for i in range(N + 1):
        th = pi * i / (2 * N)
        x = s8 * th.cos() - c
        # (x)_+ : treat balls straddling 0 conservatively
        if x.upper() <= 0:
            vals.append((arb(0), arb(0)))
        else:
            xl = x.lower() if x.lower() > 0 else 0
            xu = x.upper()
            vals.append((dphi(arb(xl)) ** 2, dphi(arb(xu)) ** 2))
    lo = sum((vals[i + 1][0] for i in range(N)), arb(0)) / N
    hi = sum((vals[i][1] for i in range(N)), arb(0)) / N
    # (2/pi) * (pi/(2N)) * sum = sum / N
    return arb(lo.lower()), arb(hi.upper())


print('\n== 2. weighted-test compact lower rate l(c) (Lemma 3), t = a, real segments ==')
print('  l(c)^2 = E[Phi_a\'((sqrt8|cos theta| - c)_+)^2]; certified by monotone Riemann sums (4000 cells)')
rates = {}
for c, why in ((Fraction(2338, 1000), 'inherited cap 1.963 + 3/8 (Rounds 177/179)'),
               (Fraction(1988, 1000), 'cap 1.963 + 0.025'),
               (Fraction(985, 1000), '[float input] sup|h| ~ 0.61 plus 3/8'),
               (Fraction(635, 1000), '[float input] sup|h| ~ 0.61 plus 0.025'),
               (Fraction(0), 'c = 0 (no displacement; compare l_S)')):
    lo, hi = lrate(arb(c.numerator) / c.denominator)
    rates[c] = (lo.sqrt(), hi.sqrt())
    print(f'  c = {float(c):.3f} ({why}): l(c) in [{float(lo.sqrt().lower()):.6f}, {float(hi.sqrt().upper()):.6f}]')
r179 = arb('0.349') / 8 / arb(5).sqrt()
print(f'  Round 179 real-floor indicator test 0.349/8/sqrt5 = {float(r179):.6f} (Round 179 rounds it to 0.019)')

print('\n== 3. Theorem 1 constants at the real floor ==')
l2338 = rates[Fraction(2338, 1000)][0]
for name, q in (('Round 179 factor 0.019', arb('0.019')), ('Lemma 3 l(2.338) lower end', l2338)):
    for k in (0, 9):
        lg = (arb('0.00042') * q ** (602 + k)).log() / arb(10).log()
        print(f'  {name}: log10(0.00042 * rate^(602+{k})) <= {float(lg.upper()):.3f}')
print('  Theorem 1 ratio bound 2 rho / c_k with rho = 3/8 (k <= 9): log10 ratio bound >= '
      f'{float(((arb(3) / 4) / (arb("0.00042") * l2338 ** 611)).log().lower() / arb(10).log().upper()):.3f}  (ineffective threshold in p)')

print('\n== 4. Proposition M: moment bounds ==')
df = 1
for m in range(1, 13):
    df *= (2 * m - 1)
    v = arb(df) ** (arb(1) / (2 * m))
    print(f'  m = {m:2d}: (2m-1)!! = {df}, ((2m-1)!!)^(1/(2m)) in {fmt(v, 5)}, sqrt(2m/e) = {float((arb(2 * m) / arb(1).exp()).sqrt()):.5f}')
for lam, L in (('6.5e205', arb(65) * arb(10) ** 204), ('9.4e206', arb(94) * arb(10) ** 205)):
    lg = L * L / 2 / arb(10).log()
    e10 = (lg.log() / arb(10).log())
    print(f'  sqrt(2 ln n) >= {lam} iff log10 n >= Lambda^2/(2 ln 10) = {lg.str(6, radius=False)}'
          f' (log10 of that in {fmt(e10, 4)})')
print('  exact: for m >= ln n, n^(1/(2m)) <= e^(1/2) =', fmt(arb(1).exp().sqrt(), 6))

print('\n== 5. rate comparison (inputs: inherited Round 182 seed price rates; Round 128/173/174/177 counting rates) ==')
for name, r in (('dimension price, one step (Round 182)', arb('0.71006')),
                ('dimension price, 8-step power (Round 182)', arb('0.53618')),
                ('pi_1 price, one step (Round 182)', arb('0.53255')),
                ('leading-field limit 2sqrt2 s/(4 sqrt a) (Round 182, conjectural)', arb('0.50206'))):
    th = r / lS
    print(f'  {name}: rate {float(r):.5f}; theta = rate / l_S in {fmt(th, 4)}')
for qv in ('0.5145', '0.5174', '0.518', '0.535', '0.545'):
    print(f'  counting rate q = {qv}: 1/q in {fmt(1 / arb(qv), 4)}')
for th in ('2.0', '2.0915'):
    t_ = 1 / arb(th)
    # Phi_a'(v) = t_  <=>  v^2 = 4a t_^2/(1 - t_^2)
    v = (four_a * t_ * t_ / (1 - t_ * t_)).sqrt()
    print(f'  Phi_a\'(v) < 1/{th} iff |v| < {fmt(v, 4)} (real t = a)')
print(f'  Phi_a\'(4.8) = {fmt(dphi(arb("4.8")), 5)};  Phi_a\'(3.32) = {fmt(dphi(arb("3.32")), 5)} [3.32 ~ float sup|V_602|]')

print('\n== 6. angular (decoupled) compact upper rate q_ang(b)^2 = E[Phi_a\'(sqrt8|cos theta| + b)^2], real floor ==')
print('  (Round 80 type averaged rate for increments with E(|d|^2 | J) = ||d||^2; upper Riemann sums, integrand nonincreasing)')


def qang(b, N=4000):
    b = arb(b)
    up = arb(0)
    lo = arb(0)
    for i in range(N):
        th0 = pi * i / (2 * N)
        th1 = pi * (i + 1) / (2 * N)
        up += dphi(s8 * th0.cos() + b) ** 2
        lo += dphi(s8 * th1.cos() + b) ** 2
    return arb((lo / N).lower()).sqrt(), arb((up / N).upper()).sqrt()


for b, why in ((Fraction(194, 100), 'Round 80 cap B = 1.94'), (Fraction(2338, 1000), 'cap 1.963 + 3/8'),
               (Fraction(985, 1000), '[float input] 0.61 + 3/8'), (Fraction(0), 'b = 0: equals l_S')):
    lo, hi = qang(arb(b.numerator) / b.denominator)
    print(f'  b = {float(b):.3f} ({why}): q_ang in [{float(lo.lower()):.6f}, {float(hi.upper()):.6f}];'
          f' 1/q_ang >= {float((1 / hi).lower()):.4f}')
