"""Replay the convolution identities in astra-convolution-11.md.

Run from the repository root with .venv/bin/python -B. No files are written.
The optional --certificate run uses Arb to verify a square orthant exactly.
"""

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import numpy as np
from scipy.optimize import nnls

from poisson_weights import weighted_iterate
from square_control import square_field_sign
from theta import paley_sign


def solve(sign, r, initial=None):
    n = len(sign)
    w = np.where(sign == 1, r, 1 / r)
    w[0] = 1
    if n <= 250:
        kernel = np.fft.ifft(np.sqrt(w)).real
        indices = np.arange(n)
        root = kernel[(indices[:, None] - indices[None, :]) % n]
        b = np.r_[1.0, nnls(root[:, 1:], -root[:, 0], maxiter=40*n)[0]]
        qb = np.fft.ifft(w * np.fft.fft(b)).real
        x = b / np.sqrt(b @ qb)
        y = qb / np.sqrt(b @ qb)
        residual = max(float(np.max(np.abs(x[1:] * y[1:]))), -float(y.min()))
        z = x-y
    else:
        weights = np.zeros(n)
        weights[0] = 1
        z, _, residual = weighted_iterate(
            sign, weights, tolerance=2e-11, rounds=96,
            damping=(1-r)/(1+r), initial=initial,
        )
        marker = np.arcsinh(z[0]/2)
        x, y = np.maximum(z, 0), np.maximum(-z, 0)
        x[0], y[0] = np.exp(marker), np.exp(-marker)
    if residual > 2e-8:
        raise RuntimeError(f"QP residual too large: {residual}")
    return x, y, z, residual


def metrics(sign, r, x, y, residual):
    n = len(sign)
    c = x.sum()/np.sqrt(n)
    f, g = np.fft.fft(x)/(c*np.sqrt(n)), np.fft.fft(y)/(c*np.sqrt(n))
    f, g = f.real, g.real
    a = x[0]
    plus, minus = sign == 1, sign == -1
    sp, sm = r*c*c*np.sum(f[plus]**2), r*c*c*np.sum(g[minus]**2)
    h = f*g
    pi = c*c*h
    nu = np.fft.ifft(h).real
    rxx = np.fft.ifft(np.abs(np.fft.fft(x))**2).real
    ryy = np.fft.ifft(np.abs(np.fft.fft(y))**2).real
    rxy = np.fft.ifft(np.fft.fft(x)*np.conj(np.fft.fft(y))).real
    errors = [abs(c*c+sp+sm-1), abs(np.sum(pi)-1),
              abs(np.sum(pi*sign)-(sp-sm)), abs(nu[0]-1/(n*c*c)),
              np.max(np.abs(rxy-r/(1+r*r)*(rxx+ryy)-(1-r)**2/(1+r*r)*c*c))]
    C2 = [np.sum(f*f), np.sum(g*g)]
    C4 = [np.sum(f**4), np.sum(g**4)]
    # At width r^2, the two autocorrelations are reciprocal positive trials.
    p2, q2 = np.fft.ifft(f*f).real, np.fft.ifft(g*g).real
    w2 = np.where(sign == 1, r*r, 1/(r*r))
    w2[0] = 1
    errors.append(np.max(np.abs(np.fft.ifft(w2*np.fft.fft(p2)).real-q2)))
    cross_bulk_fourth = np.sum(h[1:]**2)
    cross4 = 1+cross_bulk_fourth
    bulk_mass=1-c*c
    centered_pi=pi[1:]-bulk_mass/(n-1)
    covariance=np.sum((sign[1:]+1/(n-1))*centered_pi)
    variance=np.sum(centered_pi**2)
    errors += [abs(sp-sm+bulk_mass/(n-1)-covariance),
               abs(variance-c**4*cross_bulk_fourth+bulk_mass**2/(n-1)),
               max(0,abs(covariance)-np.sqrt((n-1-1/(n-1))*variance))]
    squaring_lower = np.log(C2[0]/np.sqrt(n*cross4))
    squaring_upper = np.log(np.sqrt(n*cross4)/C2[1])
    # Self-convolution trial and mixtures with the one-cross-factor trial.
    mixtures = []
    first_order_slack = []
    hp_slack = []
    for side, ff, gg, aa, cc2 in [(1,f,g,a,C2[0]),(-1,g,f,1/a,C2[1])]:
        ww = np.where(sign == side, r, 1/r)
        ww[0] = 1
        roots = []
        energies = []
        for lam in np.linspace(0,1,101):
            zz = (1-lam)*ff*ff + lam*ff*gg
            roots.append(c*np.sum(zz)/np.sqrt(n)/aa)
            energies.append(c*c*np.sum(ww*zz*zz))
        ratios = np.asarray(roots)**2 / np.asarray(energies)
        mixtures.append([float(ratios[0]), float(np.max(ratios)), float(np.argmax(ratios)/100)])
        rho = c*cc2/(aa*np.sqrt(n))
        first_order_slack.append(float(c*c*np.sum(ww*ff**3)-rho))
        D = np.sum(ff[sign == -side]**2)
        threshold = (1+np.sqrt(D))/2
        Tp = np.floor((1+np.sqrt(1+4*n))/2)
        hp_slack.append(float(threshold*cc2+(1-threshold)*Tp-np.sum(ff**4)))
    # Direct convolution uses both signs and is uniformly capped at 1/(n c^2).
    word_max = max(np.max(np.fft.ifft(f**k*g**ell).real)
                   for k,ell in [(1,1),(2,1),(1,2),(3,2),(2,3)])
    errors.append(max(0, word_max-1/(n*c*c)))
    kappa=r*np.sqrt(2*n+1)
    mass_lower=1/(1+kappa*kappa+kappa*np.sqrt(kappa*kappa+6))
    errors += [max(0,mass_lower-c*c),
               max(0,cross_bulk_fourth-r*(1-c*c)/(c*c))]
    return dict(r=float(r), kappa=float(kappa), m=float(np.log(a)),
                c2=float(c*c), S_plus=float(sp), S_minus=float(sm),
                C2=[float(v) for v in C2], C4=[float(v) for v in C4],
                cross_bulk_fourth=float(cross_bulk_fourth), mass_lower=float(mass_lower),
                centered_variance=float(variance), signed_covariance=float(covariance),
                squaring_interval=[float(squaring_lower),float(squaring_upper)],
                squaring_log_defect=float(squaring_upper-squaring_lower),
                mixture=mixtures, first_order_slack=first_order_slack,
                hp_slack=hp_slack, residual=float(residual),
                identity_error=float(max(errors)))


def certificate_case(denominator, positive):
    from flint import acb, arb, arb_mat, ctx
    ctx.prec = 192
    signs = list(map(int, square_field_sign(7)))
    n = len(signs)
    r = arb(1)/denominator
    d = (1-r)/(1+r)
    kernel = [sum((s*(2*arb.pi()*((i*j)%n)/n).cos()
                   for j,s in enumerate(signs)), arb(0))/n for i in range(n)]
    orthant = [1 if i in positive else -1 for i in range(1,n)]
    matrix = arb_mat([[int(i == j)-d*kernel[(i-j)%n]*orthant[j-1]
                       for j in range(1,n)] for i in range(1,n)])
    beta = matrix.solve(arb_mat([[d*kernel[i]] for i in range(1,n)]))
    assert all(orthant[i-1]*beta[i-1,0] > 0 for i in range(1,n))
    gamma = d*(kernel[0]+sum((kernel[i]*orthant[i-1]*beta[i-1,0]
                             for i in range(1,n)),arb(0)))
    assert abs(gamma) < 1
    u0 = 2/(1-gamma**2).sqrt()
    x = [u0*(1+gamma)/2]+[u0*beta[i-1,0] if orthant[i-1]>0 else arb(0)
                          for i in range(1,n)]
    y = [u0*(1-gamma)/2]+[-u0*beta[i-1,0] if orthant[i-1]<0 else arb(0)
                          for i in range(1,n)]
    c2 = sum(x,arb(0))**2/n
    f, g = acb.dft([v/sum(x,arb(0)) for v in x]), acb.dft([v/sum(y,arb(0)) for v in y])
    sp = r*c2*sum((abs(v)**2 for v,s in zip(f,signs) if s == 1),arb(0))
    sm = r*c2*sum((abs(v)**2 for v,s in zip(g,signs) if s == -1),arb(0))
    cross_fourth = sum((abs(v*w.conjugate())**2 for v,w in zip(f,g)),arb(0))-1
    assert sp-sm > arb(11)/100
    C2=[sum((abs(v)**2 for v in ff),arb(0)) for ff in [f,g]]
    D=[sum((abs(v)**2 for v,s in zip(ff,signs) if s == -side),arb(0))
       for ff,side in [(f,1),(g,-1)]]
    if denominator == 28:
        assert cross_fourth < arb(7)/1000
        assert x[0].log() > arb(13)/100
    else:
        assert all(v < 5 for v in C2)
        assert all(v < 1 for v in D)
        assert x[0].log() > arb(3)/100
    print(json.dumps(dict(certificate=f"q=49, r=1/{denominator}, strict actual-QP orthant",
        S_plus=str(sp), S_minus=str(sm), signed_energy=str(sp-sm),
        cross_bulk_fourth=str(cross_fourth), m=str(x[0].log()),
        C2=list(map(str,C2)),D=list(map(str,D)))))


def certificate():
    certificate_case(28,{4,6,12,18,20})
    certificate_case(7,{1,3,4,6,7,12,17,18,20,21,23})


def integral_checks():
    for q, p, maker in [(49,7,square_field_sign),(97,97,paley_sign),(401,401,paley_sign)]:
        sign=maker(p)
        lo,hi=.25/np.sqrt(q),.25
        x0,_,_,_=solve(sign,lo)
        x1,_,_,_=solve(sign,hi)
        exact=2*np.log(x0[0]/x1[0])
        for count in [16,32,64]:
            mesh=np.linspace(np.log(lo),np.log(hi),count+1)
            width=mesh[1]-mesh[0]
            signed=0.
            unsigned=0.
            for t in (mesh[:-1]+mesh[1:])/2:
                r=np.exp(t)
                x,y,_,residual=solve(sign,r)
                row=metrics(sign,r,x,y,residual)
                signed+=width*(row['S_plus']-row['S_minus'])
                unsigned+=width*(row['S_plus']+row['S_minus'])
            error=abs(signed-exact)
            bound=width*(mesh[-1]-mesh[0])/4
            assert error <= bound+1e-10
            print(json.dumps(dict(q=q,interval=[lo,hi],cells=count,signed_integral=signed,
                endpoint_identity=exact,midpoint_error=error,lipschitz_error_bound=bound,
                unsigned_integral=unsigned)),flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--primes", nargs="*", type=int, default=[13,17,29,41,61,97,173,257,401])
    parser.add_argument("--squares", nargs="*", type=int, default=[7,11,13])
    parser.add_argument("--kappas", nargs="*", type=float, default=[.0625,.25,1,4])
    parser.add_argument("--certificate", action="store_true")
    parser.add_argument("--integral", action="store_true")
    args = parser.parse_args()
    if args.certificate:
        certificate()
        return
    if args.integral:
        integral_checks()
        return
    cases = [(p,p,paley_sign) for p in args.primes]+[(p*p,p,square_field_sign) for p in args.squares]
    for q,p,maker in sorted(cases):
        sign = maker(p)
        initial = None
        for kappa in sorted(args.kappas,reverse=True):
            r=kappa/np.sqrt(q)
            if r > 1:
                continue
            x,y,initial,residual=solve(sign,r,initial)
            row=metrics(sign,r,x,y,residual)
            row.update(q=q,characteristic=p)
            assert row["identity_error"] < 2e-8
            assert min(row["first_order_slack"]) > -2e-8
            if p == q and max(row["kappa"],0) <= .25:
                assert min(row["hp_slack"]) > -2e-8
            print(json.dumps(row),flush=True)


if __name__ == "__main__":
    main()
