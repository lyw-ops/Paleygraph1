"""Round 182 cold price: FLOATING diagnostic (evidence only, label (c)).

Physical cold map in the cold normalization: V -> K sqrt(4 t + V^2), with
t_i = t off the mark and t_0 = n at the mark (t0 = n), K the real symmetric
circulant with Fourier multiplier the Paley sign row (as in smoothing.py:
kernel_action).  Seed S = 2 sqrt(n) K e_0.  At real t = a = 2031/128 the
iteration contracts in counting norm, so after ~150 steps the row is the
stationary row V_* to double precision; V_602 equals V_* to far below double
precision (Round 180: ||R_602||_{2,n} < 1e-208), so V_* stands in for V_602.

Printed per prime: sup|h|, RMS(h) with h = V_* - S; sup|Phi'(V_*)|; and for the
frozen L = K diag Phi'(V_*) the sup-norm ratios ||L^m v||_inf / ||v||_inf and
sup/RMS for structured inputs v = h and v = S.  Physical coordinates are a
sample of the arithmetic coset, so sup|h| is only a heuristic proxy for the
coset supremum, which lower-bounds the Fourier-algebra price A(h).
Double precision numpy; no rigorous statement depends on this output.
Needs numpy: run with an interpreter that has it, e.g.
   /usr/bin/python3 -B research/paley-182-cold-fixedpoint-diagnostic.py
"""
import numpy as np


def paley_sign(prime):
    """Same row as theta.paley_sign (copied: theta.py imports scipy)."""
    order = prime - 1
    fac, m, d = [], order, 2
    while d * d <= m:
        if m % d == 0:
            fac.append(d)
            while m % d == 0:
                m //= d
        d += 1
    if m > 1:
        fac.append(m)
    root = next(g for g in range(2, prime) if all(pow(g, order // f, prime) != 1 for f in fac))
    character = np.full(prime, -1, dtype=np.int8)
    character[0] = 0
    character[[x * x % prime for x in range(1, prime // 2 + 1)]] = 1
    n = (prime - 1) // 2
    return np.array([character[(1 - pow(root, 2 * j, prime)) % prime] for j in range(n)])


def is_prime(q):
    if q < 2:
        return False
    i = 2
    while i * i <= q:
        if q % i == 0:
            return False
        i += 1
    return True


def run(p, t=2031 / 128, steps=400):
    sign = paley_sign(p).astype(float)
    n = len(sign)
    mult = sign[: n // 2 + 1]

    def K(v):
        return np.fft.irfft(mult * np.fft.rfft(v), n)

    tt = np.full(n, float(t))
    tt[0] = n
    e0 = np.zeros(n)
    e0[0] = 1.0
    S = 2 * np.sqrt(n) * K(e0)
    V = S.copy()
    for _ in range(steps):
        Vn = K(np.sqrt(4 * tt + V * V))
        res = np.sqrt(np.mean((Vn - V) ** 2))
        V = Vn
        if res < 1e-14:
            break
    h = V - S
    d = V / np.sqrt(4 * tt + V * V)          # Phi'(V)
    out = dict(p=p, n=n, res=res, sup_h=np.max(np.abs(h)), rms_h=np.sqrt(np.mean(h * h)),
               sup_S=np.max(np.abs(S)), sup_V=np.max(np.abs(V)), sup_d=np.max(np.abs(d)))
    ratios = {}
    for name, v0 in (("h", h), ("S", S)):
        v = v0.copy()
        r = []
        for m in range(1, 13):
            v = K(d * v)
            r.append((np.max(np.abs(v)) / np.max(np.abs(v0)),
                      np.max(np.abs(v)) / np.sqrt(np.mean(v * v))))
        ratios[name] = r
    return out, ratios


primes = [q for q in (1013, 10009, 100049, 400009) if q % 4 == 1 and is_prime(q)]
for p in primes:
    out, ratios = run(p)
    print(f"p={out['p']} n={out['n']} final RMS step={out['res']:.1e}")
    print(f"  sup|S|={out['sup_S']:.4f} sup|V|={out['sup_V']:.4f} sup|h|={out['sup_h']:.4f} "
          f"RMS(h)={out['rms_h']:.4f} sup|Phi'(V)|={out['sup_d']:.4f}")
    for name, r in ratios.items():
        rates = [r[m][0] ** (1 / (m + 1)) for m in range(len(r))]
        print(f"  v={name}: ||L^m v||_inf/||v||_inf ^(1/m) at m=1,2,4,8,12:",
              " ".join(f"{rates[m - 1]:.3f}" for m in (1, 2, 4, 8, 12)),
              "| sup/RMS at m=1,4,12:", " ".join(f"{r[m - 1][1]:.2f}" for m in (1, 4, 12)))
