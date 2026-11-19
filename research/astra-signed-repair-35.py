"""Round 35: actual Paley quadratic scatter and first nested repair audit.

Exact rational identities at F_13 and floating diagnostics at specified
fields. No optimization, stationary solver, or claimed interval certificate.
All output is stdout; the caller chooses a permitted round-35 path.
"""
import argparse
from fractions import Fraction as F
import json
from math import sqrt
from pathlib import Path
import sys

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from theta import paley_sign
from square_control import square_field_sign
from smoothing import kernel_action


def emit(row):
    print(json.dumps(row, sort_keys=True), flush=True)


def exact():
    n = 6
    signs = [int(s) for s in paley_sign(13)]
    cosine = [F(1), F(1, 2), F(-1, 2), F(-1), F(-1, 2), F(1, 2)]
    k = [sum(signs[j]*cosine[i*j % n] for j in range(n))/n for i in range(n)]
    K = [[k[(i-j) % n] for j in range(n)] for i in range(n)]
    def mv(M, v):
        return [sum(a*b for a, b in zip(row, v)) for row in M]
    def mean(v):
        return sum(v)/n
    # x = sqrt(n)*k; xx=x^2; h=xy/sqrt(n); kz=z/sqrt(n).
    xx = [n*t*t for t in k]
    y = mv(K, xx)
    h = [a*b for a, b in zip(k, y)]
    kz = mv(K, h)
    assert mean(xx) == F(n-1, n)
    assert mean(h) == F(2-n, n*n)
    assert y[0] == sum(n*t**3 for t in k)
    assert kz[0] == mean([a*b for a, b in zip(xx, y)])
    for side in [1, -1]:
        P = [[(F(i == j)-F(1, n)+side*K[i][j])/2
              for j in range(n)] for i in range(n)]
        ell = [row[0] for row in P]
        a = F(n-1-side, 2*n)
        L = [[P[i][j]-ell[i]*ell[j]/a for j in range(n)] for i in range(n)]
        R = [[2*L[i][j]-F(i == j) for j in range(n)] for i in range(n)]
        assert mv(L, k) == [F(0)]*n
        assert mv(R, k) == [-t for t in k]
        rxx = mv(R, xx)
        expected = [side*y[i]-mean(xx)-ell[i]/a*(F(2, n)-1+side*y[0])
                    for i in range(n)]
        assert rxx == expected
        ph = mv(P, h)
        assert ph[0] == (h[0]-mean(h)+side*kz[0])/2
        # Root resetting changes Rf only at the root, for both rational
        # components of f=(x-t)^2. This checks all t by coefficients.
        for f in [xx, k, [F(1)]*n, h]:
            d = f.copy(); d[0] = 0
            assert mv(R, d)[1:] == mv(R, f)[1:]
        emit(dict(kind="exact_actual_Paley_polynomial_scatter", order=13,
                  side=side, x_scale="sqrt(6)", k=list(map(str, k)),
                  y=list(map(str, y)), z_over_sqrt_n=list(map(str, kz)),
                  annihilates_x=True, quadratic_reflection=True,
                  nested_mark_identity=True, root_reset_identity=True))
    # The corner penalty becomes a rational piecewise-linear inequality
    # in (b,r), where r=sqrt(2)*c. Split on r and t=b-r.
    # penalty = |t|-t/2 + r (r>=0), or |t|-t/2-5r/4 (r<0).
    # The stronger bound .5|t|+|r| implies .5(|b|+|c|).
    for sr in [-1, 1]:
        for st in [-1, 1]:
            t_coeff = 1-F(st, 2)
            r_coeff = F(1) if sr == 1 else F(5, 4)
            assert t_coeff >= F(1, 2) and r_coeff >= 1
    emit(dict(kind="exact_corner_penalty_audit", four_linear_regions=True,
              penalty_lower="|b-sqrt(2)c|/2 + sqrt(2)|c|",
              weaker_lower="(|b|+|c|)/2", uses_compact_law_for_transfer=True))


def diagnostic(order, root, shifts, coefficients):
    sign = square_field_sign(root) if root else paley_sign(order)
    n = len(sign)
    e0 = np.zeros(n); e0[0] = 1
    x = sqrt(n)*kernel_action(sign, e0)
    y = kernel_action(sign, x*x)
    z = kernel_action(sign, x*y)
    def P(side, f):
        return (f-f.mean()+side*kernel_action(sign, f))/2
    bx = sqrt(order/n)
    by = order/n+bx/sqrt(n)
    bentry = (1+sqrt(order))/(2*n)
    for side in [1, -1]:
        ell = P(side, e0)
        aa = (n-1-side)/(2*n)
        def L(f):
            return P(side, f)-ell*(ell@f)/aa
        assert np.max(np.abs(L(x))) < 2e-10
        for t in shifts:
            d = (x-t)**2; d[0] = 0
            rd = 2*L(d)-d
            identity = side*y-(1-1/n)+2*t*x-t*t
            identity -= ell/aa*(2/n-1+side*y[0])
            error = np.max(np.abs(rd[1:]-identity[1:]))
            assert error < 2e-9
            bound = t*t+1-1/n+2*abs(t)*bx+by
            bound += bentry/aa*abs(2/n-1+side*y[0])
            spill = max(0., -float(rd[1:].min()))
            assert spill <= bound+1e-10
            emit(dict(kind="floating_quadratic_scatter", order=order,
                      square_root=root, side=side, t=t, spill=spill,
                      finite_upper_formula=bound,
                      proved_asymptotic_spill=3+t*t+2*sqrt(2)*abs(t),
                      identity_error=float(error), y0=float(y[0]),
                      scope="floating identity check; not an interval certificate"))
        for mu, a, b, c in coefficients:
            proposal = mu+(a*sqrt(n)-mu)*ell/aa+b*L(x*x)+c*L(x*y)
            limiting = mu+a*side*x+b*(x*x-1+side*y)/2+c*(x*y+side*z)/2
            corner = mu-sqrt(2)*a+b/2-abs(b-sqrt(2)*c)
            corner += -3*c/sqrt(2) if c >= 0 else 3*c/(2*sqrt(2))
            emit(dict(kind="floating_first_nested_trial", order=order,
                      square_root=root, side=side, coefficients=[mu,a,b,c],
                      affine_mean_error=float(abs(proposal.mean()-mu)),
                      affine_mark_error=float(abs(proposal[0]-a*sqrt(n))),
                      bulk_min=float(proposal[1:].min()),
                      compact_corner_upper=corner,
                      weaker_corner_upper=mu-sqrt(2)*a-(abs(b)+abs(c))/2,
                      bulk_alias_max_error=float(np.max(np.abs(proposal[1:]-limiting[1:]))),
                      scope="floating diagnostic, no finite inequality to limiting corner asserted"))


def averaged(order, root):
    """Main-line suggested average, with exact formula and floating orbit."""
    sign = square_field_sign(root) if root else paley_sign(order)
    n = len(sign); tau = .05; kappa = .001
    w = np.full(n, tau/n); w[0] = 1
    e0 = np.zeros(n); e0[0] = 1
    def P(side, f):
        return (f-f.mean()+side*kernel_action(sign, f))/2
    v = kernel_action(sign, 2*np.sqrt(w))  # v_1; average starts at t=1
    mean_sum = 0.; psum = [np.zeros(n),np.zeros(n)]
    for t in range(1,129):
        phi = np.hypot(v,2*np.sqrt(w))
        mu = phi.mean()/2
        mean_sum += mu
        for j,side in enumerate([1,-1]):
            psum[j] += P(side,(phi+side*v)/2)
        if t in [16,32,64,128]:
            M = mean_sum/t
            for j,side in enumerate([1,-1]):
                raw = 1+psum[j]/(t*M)
                d = np.maximum(2*kappa-raw,0); d[0] = 0
                ell = P(side,e0); aa=(n-1-side)/(2*n)
                ld = P(side,d)-ell*(ell@d)/aa
                out=raw+2*ld; spill=max(0.,float(np.max(d-2*ld)))
                gamma=(1+sqrt(order))/n+(1+sqrt(order))**2/(2*n*n*aa)
                emit(dict(kind="floating_averaged_Picard_repair",order=order,
                          square_root=root,side=side,steps=t,tau="1/20",kappa="1/1000",
                          average_scale=float(n*M*M),
                          scale_upper=float(w.sum()+(1-sqrt(tau/n))**2*(1-1/n)/t),
                          raw_bulk_min=float(raw[1:].min()),
                          normalized_mark=float(raw[0]/sqrt(n)),
                          deficit_mass=float(d.sum()),active=int(np.count_nonzero(d)),
                          signed_spill=spill,absolute_spill=float(gamma*d.sum()),
                          repaired_min=float(out.min()),
                          scope="floating diagnostics only; no certified positivity or uniform claim"))
        v=kernel_action(sign,phi)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--exact", action="store_true")
    ap.add_argument("--constants", action="store_true")
    ap.add_argument("--averaged", action="store_true")
    ap.add_argument("--primes", nargs="*", type=int, default=[])
    ap.add_argument("--square-roots", nargs="*", type=int, default=[])
    args = ap.parse_args()
    if args.exact:
        exact()
    if args.constants:
        from flint import arb, ctx
        ctx.prec = 192
        tau = arb(1)/20
        gap = 2-arb(2).sqrt()*(1+tau.sqrt())/(1+tau).sqrt()
        assert gap > arb(".31126218139110774388555")
        assert gap < arb(".31126218139110774388556")
        emit(dict(kind="arb_compact_gap_constant", precision_bits=192,
                  exact_tau="1/20", gap=str(gap),
                  lower=".31126218139110774388555",
                  upper=".31126218139110774388556",
                  scope="constant in an asymptotic theorem; no finite field or trajectory certified"))
        # Actual F_13, first genuine zero-Picard update; rational K.
        n = 6
        signs = [int(s) for s in paley_sign(13)]
        co = [F(1),F(1,2),F(-1,2),F(-1),F(-1,2),F(1,2)]
        kr = [sum(signs[j]*co[i*j % n] for j in range(n))/n for i in range(n)]
        def ball(r):
            return arb(r.numerator)/r.denominator
        weights = [arb(1)]+[tau/n]*(n-1)
        phi0 = [2*w.sqrt() for w in weights]
        v1 = [sum(ball(kr[(i-j) % n])*phi0[j] for j in range(n)) for i in range(n)]
        phi1 = [(v*v+4*w).sqrt() for v,w in zip(v1,weights)]
        c1 = sum(phi1)**2/(4*n)
        excess = c1-sum(weights)
        assert excess > arb(".22369121") and excess < arb(".22369122")
        emit(dict(kind="arb_actual_Paley_C1_exceeds_W", order=13,
                  exact_tau="1/20", exact_start="v0=0", depth=1,
                  precision_bits=192, excess=str(excess),
                  lower=".22369121", upper=".22369122",
                  scope="refutes all-field all-depth C_t<=W; not its prime-limsup version"))
    # These fixed rational inputs are tests of formulas, not an optimizer.
    shifts = [0., .5, -.5]
    coefficients = [(1.,1.,0.,0.),(1.,1.,.25,.125),
                    (1.,1.,-.25,-.125),(1.,1.,.25,-.125)]
    for p in args.primes:
        if args.averaged:
            averaged(p,None)
        else:
            diagnostic(p, None, shifts, coefficients)
    for r in args.square_roots:
        if args.averaged:
            averaged(r*r,r)
        else:
            diagnostic(r*r, r, shifts, coefficients)


if __name__ == "__main__":
    main()
