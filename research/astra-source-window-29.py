"""Replay exact weight algebra and floating actual-orbit source-window identities.

Writes JSON lines to stdout only. No stationary solve is used. Float records
are diagnostics, not interval certificates or an asymptotic prime estimate.
"""
import argparse
from fractions import Fraction as F
import json
from math import acosh, asinh, cosh, log, sqrt
from pathlib import Path
import sys

import numpy as np
from scipy.optimize import minimize_scalar
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from smoothing import kernel_action
from square_control import square_field_sign
from theta import paley_sign


def exact_audit():
    cases = 0
    for h in (F(1), F(1, 2), F(1, 3)):
        for T in (1, 2, 7, 19):
            for raw in ([F(1)]*T, [F(T-t) for t in range(T)],
                        [F(t+1) for t in range(T)]):
                lam = [x/sum(raw) for x in raw]
                kappa = [lam[j]-h*sum(lam[t]*(1-h)**(t-1-j)
                           for t in range(j+1, T)) for j in range(T)]
                # Coefficient of u_j in (1/h) sum lambda_t K(z_(t+1)-z_t).
                direct = []
                for j in range(T):
                    coeff = F(0)
                    for t in range(T):
                        following = h*(1-h)**(t-j) if j <= t else F(0)
                        previous = h*(1-h)**(t-1-j) if j < t else F(0)
                        coeff += lam[t]*(following-previous)/h
                    direct.append(coeff)
                assert kappa == direct
                assert sum(kappa) == sum(lam[t]*(1-h)**t for t in range(T))
                decreasing = all(lam[t] >= lam[t+1] for t in range(T-1))
                if decreasing:
                    assert all(kappa[j] >= lam[j]*(1-h)**(T-1-j)
                               for j in range(T))
                    alpha = [(t+1)*(lam[t]-(lam[t+1] if t+1<T else 0))
                             for t in range(T)]
                    assert min(alpha) >= 0 and sum(alpha) == 1
                    assert all(sum(alpha[k]/(k+1) for k in range(t,T)) == lam[t]
                               for t in range(T))
                # Energy summation by parts checked coefficientwise.
                e = [F((j+1)**3, j+2) for j in range(T+1)]
                direct_e = sum(lam[t]*(e[t]-e[t+1]) for t in range(T))
                abel_e = lam[0]*e[0]-lam[-1]*e[-1]+sum(
                    (lam[t]-lam[t-1])*e[t] for t in range(1,T))
                assert direct_e == abel_e
                cases += 1
    # Picard t=1,...,T: the raw telescope is a conic sum of g_t.
    for T in (1,2,7,19):
        lam = [F(T-t, T*(T+1)//2) for t in range(T)]
        g = [F(0)]+[F(j*j+3, j+1) for j in range(1,T+1)]
        assert sum(lam[t-1]*(g[t]-g[t-1]) for t in range(1,T+1)) == (
            lam[-1]*g[-1]+sum((lam[t-1]-lam[t])*g[t] for t in range(1,T)))
    # Independent rational one-step dynamics: q=9 Paley multiplier
    # (0,-1,+1,-1), not a stationary solve or floating FFT.
    row = [F(-1,4),F(-1,4),F(3,4),F(-1,4)]
    def K(x):
        return [sum(row[(i-j)%4]*x[j] for j in range(4)) for i in range(4)]
    z = [F(0),F(3,8),F(0),F(-3,8)]
    u = [F(2),F(5,8),F(1,2),F(5,8)]
    w = [F(1)]+[F(1,16)]*3
    assert all(u[i]**2-z[i]**2 == 4*w[i] for i in range(4))
    assert K(K(u)) == [x-sum(u)/4 for x in u]
    E, W, S = sum(x*x for x in z),sum(w),sum(u)/2
    r = [x-y for x,y in zip(z,K(u))]
    b = [x-sum(u)/4-y for x,y in zip(u,K(z))]
    assert b == [-x for x in K(r)]
    for h in (F(1),F(1,2),F(1,3)):
        nxt = [x-h*y for x,y in zip(z,r)]
        assert sum(x*x for x in nxt) == E+h*(4*W-S*S)-h*(1-h)*sum(x*x for x in r)
    print(json.dumps(dict(kind='exact rational coefficient and energy audit',
                          coefficient_cases=cases, energy_cases=3,
                          passed=True)), flush=True)


def support(b, q, tau):
    """Same proved root-coupled relaxation as source-tail-28; float only."""
    n = len(b)
    w = tau/n
    W = 1+(n-1)*w
    a = 2*sqrt(w)
    mass = 2*sqrt(n*W)-n*a
    C = (1+sqrt(q))*sqrt(W/n)
    endpoint = min(C+1/C, mass+a)
    def maxroot(threshold):
        excess = np.maximum(b[1:]-threshold, 0).sum()
        L = b[0]-threshold+(1+w)*excess/2
        J = (1-w)*excess/2
        constant = threshold*mass-a*(b[0]-threshold+excess)
        values = [2*L+constant, L*endpoint+J*sqrt(max(0,endpoint**2-4))+constant]
        if J > 0 and L < -J:
            critical = -2*L/sqrt(L*L-J*J)
            if critical <= endpoint:
                values.append(constant-2*sqrt(L*L-J*J))
        return float(max(values))
    lo, hi = float(min(b[1:])), float(max(b[1:]))
    if hi == lo:
        threshold = lo
    else:
        threshold = float(minimize_scalar(maxroot, bounds=(lo,hi), method='bounded',
                          options={'xatol':1e-15}).x)
    return maxroot(threshold), threshold


def top_fractional(values, capacity):
    ordered = np.sort(values)[::-1]
    capacity = min(max(0.0, capacity),len(ordered))
    whole = int(capacity)
    return float(ordered[:whole].sum()+(capacity-whole)*ordered[whole]
                 if whole<len(ordered) else ordered.sum())


def run(q, square_root, tau, h, steps):
    sign = square_field_sign(square_root) if square_root else paley_sign(q)
    n = len(sign)
    c = np.full(n,4*tau/n); c[0] = 4
    W = float(c.sum()/4)
    z = np.zeros(n)
    # Save only the requested prefix; these sizes intentionally stay modest.
    zs, us, bs, rs, energies, scalars, losses = [], [], [], [], [], [], []
    max_energy_error = 0.0
    for t in range(max(steps)):
        u = np.sqrt(z*z+c)
        r = z-kernel_action(sign,u)
        b = u-u.mean()-kernel_action(sign,z)
        nxt = z-h*r
        E, Enext = float(z@z), float(nxt@nxt)
        S = float(u.sum()/sqrt(n))
        scalar = 2*sqrt(W)*S-4*W
        loss = (1-h)*float(r@r)/2+(S-2*sqrt(W))**2/2
        max_energy_error = max(max_energy_error,abs(scalar-(E-Enext)/(2*h)+loss))
        zs.append(z.copy()); us.append(u); bs.append(b); rs.append(r)
        energies.append(E); scalars.append(scalar); losses.append(loss)
        z = nxt
        T=t+1
        if T not in steps:
            continue
        for name, raw in [('uniform',np.ones(T)),('decreasing',np.arange(T,0,-1)),
                          ('increasing',np.arange(1,T+1))]:
            lam = raw/raw.sum()
            bavg = np.einsum('t,ti->i',lam,np.array(bs))
            kappa = np.array([lam[j]-h*sum(lam[k]*(1-h)**(k-1-j)
                              for k in range(j+1,T)) for j in range(T)])
            H = np.einsum('t,ti->i', kappa, np.array(us))
            scalar = float(lam@np.array(scalars))
            reserve = float(lam@np.array(losses))
            energy_boundary = (lam[0]*energies[0]-lam[-1]*Enext+sum(
                (lam[k]-lam[k-1])*energies[k] for k in range(1,T)))/(2*h)
            tail, threshold = support(bavg,q,tau)
            D = max(0.0,scalar+tail)
            markers = np.array([asinh(x[0]/2) for x in zs])
            eta = float(lam@markers)
            root_lower = log((square_root-1)/sqrt(n*W)) if square_root else None
            necessary = (4*(cosh(max(0.,root_lower-eta))-1)
                         if root_lower is not None else None)
            if necessary is not None:
                assert scalar+tail+1e-8 >= necessary
            top_data = {}
            if name == 'uniform':
                bulk_floor = 2*sqrt(tau/n)
                B = 2*sqrt(n*W)-n*bulk_floor
                k = B/(2-bulk_floor)-1
                C = (1+sqrt(q))*sqrt(W/n)
                Cn = C+1/C
                beta = 1-(1-h)**T
                hat_u = H*(h*T)
                hat_g = hat_u-beta*np.sqrt(c)
                actual_top = top_fractional(hat_g[1:],k)
                top_lower = ((h*T/Cn)*(necessary+Enext/(2*h*T)+reserve)
                              -hat_u[0]-k*beta*bulk_floor
                              if necessary is not None and 0 <= k <= n-1 else None)
                if top_lower is not None:
                    assert actual_top+1e-8 >= top_lower
                top_data = dict(terminal_source_top_capacity=k,
                                terminal_source_top_mass=actual_top,
                                square_terminal_source_top_lower=top_lower)
            print(json.dumps(dict(kind='floating actual-orbit diagnostic',order=q,
                square_root=square_root,tau=tau,relaxation=h,steps=T,weights=name,
                scalar=scalar,energy_boundary=energy_boundary,dissipation=reserve,
                source_tail_upper=tail,threshold=threshold,discrepancy_upper=D,
                mean_marker=eta,root_radius=acosh(1+D/4),
                square_root_gap_lower=necessary,minimum_source_coefficient=float(kappa.min()),
                raw_source_min=float(H.min()),
                telescope_max_error=float(np.max(np.abs(bavg-H+H.mean()))),
                scalar_identity_error=abs(scalar-energy_boundary+reserve),
                maximum_step_identity_error=max_energy_error,
                terminal_norm=sqrt(Enext),
                status='float only; not an interval enclosure of the exact orbit', **top_data)),flush=True)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--exact-only',action='store_true')
    p.add_argument('--primes',nargs='*',type=int,default=[61,9413])
    p.add_argument('--square-roots',nargs='*',type=int,default=[7,97])
    p.add_argument('--steps',nargs='+',type=int,default=[8,32,128])
    p.add_argument('--tau',type=float,default=.05)
    p.add_argument('--relaxation',nargs='+',type=float,default=[1.,.5])
    args=p.parse_args()
    exact_audit()
    if args.exact_only:
        return
    assert 0<args.tau<1 and min(args.steps)>0 and all(0<h<=1 for h in args.relaxation)
    for q,r in [(p,None) for p in args.primes]+[(r*r,r) for r in args.square_roots]:
        for h in args.relaxation:
            run(q,r,args.tau,h,args.steps)
if __name__=='__main__':
    main()
