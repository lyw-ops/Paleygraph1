"""Exact nested-kernel reductions and independent floating moment diagnostics.

Run from the repository root with .venv/bin/python -B. Only writes stdout.
Exact checks use Python integer arithmetic in prime and quadratic fields.
Floating tests are not proofs of monodromy or of an error constant.
"""
import json
from fractions import Fraction
from math import sqrt
from pathlib import Path
import sys

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from theta import prime_divisors


class Field:
    def __init__(self, p, degree=1):
        self.p, self.degree, self.q = p, degree, p**degree
        self.leg = [0] + [1 if pow(a, (p-1)//2, p) == 1 else -1
                          for a in range(1, p)]
        self.d = self.leg.index(-1)

    def add(self, a, b):
        p = self.p
        return (a % p + b % p) % p + p*((a//p + b//p) % p)

    def neg(self, a):
        return (-a % self.p) + self.p*((-(a//self.p)) % self.p)

    def sub(self, a, b):
        return self.add(a, self.neg(b))

    def mul(self, a, b):
        p = self.p
        x, y, z, w = a % p, a//p, b % p, b//p
        return (x*z+self.d*y*w) % p + p*((x*w+y*z) % p)

    def power(self, a, k):
        v = 1
        while k:
            if k & 1:
                v = self.mul(v, a)
            a = self.mul(a, a)
            k //= 2
        return v

    def inv(self, a):
        assert a
        return self.power(a, self.q-2)

    def chi(self, a):
        if self.degree == 1:
            return self.leg[a]
        x, y = a % self.p, a//self.p
        return self.leg[(x*x-self.d*y*y) % self.p]

    def cycle(self):
        factors = prime_divisors(self.q-1)
        g = next(a for a in range(1, self.q)
                 if all(self.power(a, (self.q-1)//d) != 1 for d in factors))
        out, a = [], 1
        for _ in range(self.q-1):
            out.append(a)
            a = self.mul(a, g)
        assert a == 1 and len(set(out)) == self.q-1
        return out


def conv(a, b):
    n = len(a)
    return [sum(a[j]*b[(i-j) % n] for j in range(n)) for i in range(n)]


def exact(p, degree):
    f = Field(p, degree)
    q = f.q
    cycle = f.cycle()
    ell = [f.chi(f.sub(1, a)) for a in cycle]
    tcyc = conv(ell, ell)
    bcyc = conv(ell, tcyc)
    # Direct cubic character sums independently check full convolution.
    t = [sum(f.chi(f.mul(f.mul(v, f.sub(v, 1)), f.sub(v, a)))
             for v in range(q)) for a in range(q)]
    assert all(t[a] == tcyc[i] for i, a in enumerate(cycle))
    b = [sum(f.chi(f.mul(v, f.sub(v, a)))*t[v] for v in range(q))
         for a in range(q)]
    assert all(b[a] == bcyc[i] for i, a in enumerate(cycle))
    full_d = conv(ell, [v*t[a] for v, a in zip(ell, cycle)])
    for i, a in enumerate(cycle):
        assert full_d[i] == f.chi(a)*b[f.sub(1, f.inv(a))]+1
    s = ell[::2]
    n = len(s)
    h = conv(s, s)
    tq = [a*v for a, v in zip(s, h)]
    u = [a*v for a, v in zip(s, conv(s, tq))]
    r = [s[i]*b[f.sub(1, a)] for i, a in enumerate(cycle[::2])]
    for i, a in enumerate(cycle[::2]):
        assert 4*u[i] == s[i]*(b[f.sub(1, a)] +
                              b[f.sub(1, f.inv(a))]-2*t[a]+6)
        assert 4*u[i] == r[i]+r[-i]-4*tq[i]+2*s[i]
    # Exact Clausen check at every nonsingular pullback point (optional
    # independent diagnostic; not needed for the monodromy proof).
    inv2 = f.inv(2)
    for a in cycle:
        if a in (1, f.neg(1)):
            continue
        lam = f.mul(f.sub(1, a), inv2)
        assert b[f.sub(1, f.mul(a, a))] == t[lam]**2-q
    uu, ss = conv(u, u), conv(s, s)
    moments = dict(x2z2=Fraction(conv(ss, uu)[0], n**4),
                   z4=Fraction(conv(uu, uu)[0], n**6),
                   xz3=Fraction(conv(conv(s, u), uu)[0], n**5))
    # Raw nine-variable contraction evaluated via exact convolutions;
    # independently compare its three-variable reduced contraction.
    w = [r[i]+r[-i]-4*tq[i]+2*s[i] for i in range(n)]
    assert Fraction(conv(conv(s, w), conv(w, w))[0], 64*n**5) == moments['xz3']
    print(json.dumps(dict(kind='exact_integer_reduction', q=q, p=p,
                          degree=degree, checked_points=q-1,
                          rational_moments={k: str(v) for k, v in moments.items()},
                          full_pfaff=True, subgroup_reduction=True,
                          clausen_pullback=True, mixed_contraction=True)), flush=True)


def floating(p, degree):
    f = Field(p, degree)
    q = f.q
    cycle = f.cycle()
    index = {a: i for i, a in enumerate(cycle)}
    ell = np.array([f.chi(f.sub(1, a)) for a in cycle])
    ef = np.fft.fft(ell)
    b = np.fft.ifft(ef**3).real
    r = ell*b[[index[f.sub(1, a)] if a != 1 else 0 for a in cycle]]
    # r(1)=0 regardless of the placeholder B(0).
    a = np.fft.fft(r)/q**1.5
    j = ef/sqrt(q)
    s = ell[::2]
    n = len(s)
    act = lambda v: np.fft.fft(s*np.fft.ifft(v)).real
    x = np.fft.fft(s).real/sqrt(n)
    y = act(x*x)
    z = act(x*y)
    zp = q**1.5/(4*n**1.5)*(a[:n]+a[n:]).real-y/sqrt(n)+x/(2*n)
    err = float(np.max(abs(z-zp)))
    assert err < 1e-9
    good = np.ones(q-1, dtype=bool)
    good[[0, n]] = False
    aa, bb, jj = a[good], np.roll(a, n)[good], j[good]
    moment = dict(x2z2=float(np.mean(x*x*z*z)),
                  z4=float(np.mean(z**4)), xz3=float(np.mean(x*z**3)))
    stats = dict(abs_a2=float(np.mean(abs(aa)**2)),
                 abs_a4=float(np.mean(abs(aa)**4)),
                 abs_a2_abs_b2=float(np.mean(abs(aa)**2*abs(bb)**2)),
                 a3_j_real=float(np.mean(aa**3*jj).real),
                 a3_conj_j_real=float(np.mean(aa**3*jj.conj()).real))
    print(json.dumps(dict(kind='floating_diagnostic', q=q, p=p, degree=degree,
                          exact_formula_fft_error=err, moments=moment,
                          scaled_errors_proved_moments={
                              'x2z2': sqrt(q)*(moment['x2z2']-.5),
                              'z4': sqrt(q)*(moment['z4']-.75)},
                          new_generator_diagnostics=stats,
                          xz3_status=('square limit 1/8 proved by vertical reality'
                                      if degree % 2 == 0 else
                                      'prime main term c_q/8; c_q in {-1,1}, sign not identified'))),
          flush=True)


def exact_phase_trace(p, degree):
    """The full contraction is rational over every odd field, even q=3 mod 4.

    This finite computation is not a proof that the top-weight sign is +1.
    The proof that its square is +1 uses all extensions, in the note.
    """
    f = Field(p, degree)
    cycle = f.cycle()
    index = {a: i for i, a in enumerate(cycle)}
    ell = [f.chi(f.sub(1, a)) for a in cycle]
    b = conv(conv(ell, ell), ell)
    r = [0 if a == 1 else ell[i]*b[index[f.sub(1, a)]]
         for i, a in enumerate(cycle)]
    coefficient = conv(conv(r, r), conv(r, ell))[0]
    trace = Fraction(coefficient, f.q**5)
    # Independent DFT check of the full, untrimmed contraction.
    aa = np.fft.fft(r)/f.q**1.5
    jj = np.fft.fft(ell)/sqrt(f.q)
    obs = np.mean(aa**3*jj)
    assert abs(obs.imag) < 1e-12 and abs(obs.real-float(trace)) < 1e-12
    print(json.dumps(dict(kind='exact_real_phase_trace', p=p, degree=degree,
                          q=f.q, raw_integer_coefficient=coefficient,
                          rational_full_a3j=str(trace),
                          assertion='rational full contraction; no finite-data sign inference')),
          flush=True)


if __name__ == '__main__':
    for p, d in [(5, 1), (13, 1), (17, 1), (29, 1), (41, 1),
                 (3, 2), (5, 2), (7, 2), (11, 2)]:
        exact(p, d)
    for p, d in [(401, 1), (9413, 1), (37253, 1), (153649, 1),
                 (31, 2), (97, 2), (193, 2), (389, 2)]:
        floating(p, d)
    for p, d in [(3, 1), (7, 1), (11, 1), (19, 1), (3, 2), (7, 2)]:
        exact_phase_trace(p, d)
