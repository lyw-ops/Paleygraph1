"""Minimal algebra audits and actual-orbit depth-window diagnostics.

Only stdout JSONL is written. Rational records are exact. Chebyshev and
Paley FFT records are floating consistency checks, not interval certificates,
computed sheaf traces, or a uniform prime estimate.
"""

import argparse
from fractions import Fraction as Q
import json
from math import asinh, ceil, cosh, log, sqrt
from pathlib import Path
import sys

import numpy as np
from scipy.fft import dct
from numpy.polynomial.chebyshev import chebval

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from smoothing import kernel_action
from square_control import square_field_sign
from theta import paley_sign


def emit(**record):
    print(json.dumps(record, sort_keys=True), flush=True)


def top(values, k):
    values = np.sort(np.asarray(values))[::-1]
    k = min(max(float(k), 0.), len(values))
    m = int(k)
    return float(values[:m].sum() + ((k-m)*values[m] if m < len(values) else 0))


def exact_top_audit():
    cases = 0
    for side in (4, 9, 16, 25):
        n, k = side*side, side
        # Error in the *scaled* field, supported on exactly k coordinates.
        e = [Q(3, 7)]*k + [Q(0)]*(n-k)
        top_unscaled = sum(e[:k])/side
        rms_squared = sum(x*x for x in e)/n
        assert top_unscaled**2 == k*rms_squared
        # Mixed uniform/L1 bound, including an unrestricted exceptional vector.
        h = [Q((-1)**j, 19) for j in range(n)]
        sparse = [Q(0)]*n
        sparse[1], sparse[-1] = Q(5, 3), Q(-7, 2)
        total = [x+y for x,y in zip(h,sparse)]
        lhs = sum(sorted(map(abs,total), reverse=True)[:k])/side
        rhs = (k*max(map(abs,h))+sum(map(abs,sparse)))/side
        assert lhs <= rhs
        cases += 1
    # Word dimension/rank inequality, and its squared submultiplicative weight.
    word_cases = 0
    for dims in ((1,1,1), (2,3,5), (3,2,1,4)):
        ranks = tuple(j+1 for j in range(len(dims)))
        D, R, weight = Q(1), Q(0), Q(1)
        for d,r in zip(dims,ranks):
            R, D = R*d+D*r, D*d
            weight *= (d+r)**2
        assert (D+R)**2 <= weight
        assert R <= len(dims)*max(ranks)*max(dims)**(len(dims)-1)
        word_cases += 1
    emit(kind='exact rational top-tail and word audits', top_cases=cases,
         word_cases=word_cases, rms_loss_equality=True, passed=True)


def chebyshev_audit():
    for tau in (.05, .5):
        for U in (2., 8.):
            for epsilon in (.01, .0001):
                radius = 1+sqrt(tau)/U
                M = U+3*sqrt(tau)
                degree = 2*ceil(log(2*M/(epsilon*(radius-1)))/(2*log(radius)))
                analytic_bound = 2*M*radius**(-degree)/(radius-1)
                # Midpoint Chebyshev quadrature approximates exact integral
                # coefficients; oversampling is deliberately generous.
                nodes = max(4096, 16*(degree+1))
                theta = np.pi*(np.arange(nodes)+.5)/nodes
                coeff = dct(np.sqrt(U*U*np.cos(theta)**2+4*tau), type=2)/nodes
                coeff[0] /= 2
                coeff[1::2] = 0
                coeff = coeff[:degree+1]
                grid = np.linspace(-1., 1., 20001)
                measured = float(np.max(np.abs(chebval(grid,coeff)
                              -np.sqrt(U*U*grid*grid+4*tau))))
                assert analytic_bound <= epsilon*(1+1e-12)
                assert measured <= analytic_bound+2e-12
                emit(kind='floating Chebyshev audit', tau=tau, U=U,
                     epsilon=epsilon, even_degree=degree,
                     ellipse_error_upper=analytic_bound, grid_error=measured,
                     log10_monomial_budget_upper=(log(4*M)
                                   +(degree+1)*log(1+sqrt(2)))/log(10),
                     interval_certificate=False)


def orbit(q, square_root, tau, relaxation, horizons):
    sign = square_field_sign(square_root) if square_root else paley_sign(q)
    n = len(sign)
    c = np.full(n,4*tau/n); c[0] = 4
    base = np.sqrt(c)
    W = float(c.sum()/4)
    a = float(base[1])
    B = 2*sqrt(n*W)-n*a
    capacity = B/(2-a)-1
    C = (1+sqrt(q))*sqrt(W/n)
    cap = C+1/C
    z = np.zeros(n)
    hat_u = np.zeros(n)
    eta_sum, loss_sum = 0., 0.
    max_recurrence_split_error = 0.
    x = sqrt(n)*kernel_action(sign,np.eye(1,n,0)[0])
    for t in range(max(horizons)):
        u = np.sqrt(z*z+c)
        residual = z-kernel_action(sign,u)
        eta_sum += asinh(float(z[0])/2)
        S = float(u.sum()/sqrt(n))
        loss_sum += (1-relaxation)*float(residual@residual)/2+(S-2*sqrt(W))**2/2
        hat_u = (1-relaxation)*hat_u+relaxation*u
        V = sqrt(n)*z
        b = sqrt(4+z[0]**2)-sqrt(z[0]**2+4*tau/n)
        split = b*x+kernel_action(sign,np.sqrt(V*V+4*tau))
        direct = sqrt(n)*kernel_action(sign,u)
        split_error = float(np.linalg.norm(split-direct)/sqrt(n))
        max_recurrence_split_error = max(max_recurrence_split_error,split_error)
        assert split_error < 2e-12
        next_z = z-relaxation*residual
        T = t+1
        if T in horizons:
            beta = 1-(1-relaxation)**T
            ghat = hat_u-beta*base
            terminal_top = top(ghat[1:],capacity)
            E = float(next_z@next_z)
            mean_eta = eta_sum/T
            necessity = None
            if square_root:
                ell = log((square_root-1)/sqrt(n*W))
                discrepancy_lower = 4*(cosh(max(ell-mean_eta,0.))-1)
                necessity = relaxation*T/cap*(discrepancy_lower
                             +E/(2*relaxation*T)+loss_sum/T)-hat_u[0]-capacity*beta*a
                assert terminal_top >= necessity-2e-10
            # Stability check at the current actual endpoint, using a
            # deterministic perturbation. This is not a surrogate trajectory.
            pert = np.zeros(n)
            indices = np.argsort(np.abs(V[1:]))[-max(1,int(capacity)):]+1
            pert[indices] = .03*np.where(V[indices] >= 0,1.,-1.)
            g = (np.sqrt(V[1:]**2+4*tau)-2*sqrt(tau))/sqrt(n)
            gp = (np.sqrt((V[1:]+pert[1:])**2+4*tau)-2*sqrt(tau))/sqrt(n)
            observed = abs(top(gp,capacity)-top(g,capacity))
            rms = float(np.linalg.norm(pert[1:])/sqrt(n))
            rms_bound = sqrt(capacity)*rms
            local_bound = top(np.abs(pert[1:]),capacity)/sqrt(n)
            assert observed <= local_bound+1e-12 <= rms_bound+2e-12
            # Increment-weighted cutoff stability, using a Lipschitz ramp.
            D = sqrt(n)*(next_z-z)
            eX = .0001*np.cos(np.arange(n))
            eY = .0002*np.sin(np.arange(n))
            X, Y = V[1:], sqrt(n)*next_z[1:]
            Dt = D[1:]+eY[1:]-eX[1:]
            def norm(v, power=2):
                return float((np.sum(np.abs(v)**power)/n)**(1/power))
            def cutoff(X,Y):
                return np.clip(2-np.maximum(np.abs(X),np.abs(Y)),0,1)
            energy, energyt = norm(D[1:])**2, norm(Dt)**2
            if min(energy,energyt)>1e-25:
                mass = float(np.sum(D[1:]**2*cutoff(X,Y))/(n*energy))
                masst = float(np.sum(Dt**2*cutoff(X+eX[1:],Y+eY[1:]))/(n*energyt))
                weighted_bound = (2*(sqrt(energy)+sqrt(energyt))*norm(Dt-D[1:])
                           +norm(Dt,4)**2*(norm(eX[1:])+norm(eY[1:])))/energy
                assert abs(mass-masst) <= weighted_bound+1e-12
            else:
                mass, masst, weighted_bound = None,None,None
            emit(kind='floating actual orbit and stability audit', q=q,
                 square_root=square_root, tau=tau, relaxation=relaxation,
                 T=T, capacity=capacity, source_top=terminal_top,
                 source_top_per_T=terminal_top/T, square_necessary_lower=necessity,
                 mean_marked_angle=mean_eta, terminal_root=float(next_z[0]),
                 source_stability_error=observed, rms_stability_upper=rms_bound,
                 localized_stability_upper=local_bound,
                 weighted_cutoff_error=None if mass is None else abs(mass-masst),
                 weighted_cutoff_upper=weighted_bound,
                 maximum_split_recurrence_rms_error=max_recurrence_split_error,
                 interval_certificate=False)
        z = next_z


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--exact-only',action='store_true')
    args = parser.parse_args()
    exact_top_audit()
    if args.exact_only:
        return
    chebyshev_audit()
    for q,r in ((61,None),(9413,None),(49,7),(9409,97)):
        for relaxation in (1.,.5):
            orbit(q,r,.05,relaxation,(8,32,64))


if __name__ == '__main__':
    main()
