"""Finite floating-point algebra checks; no asymptotic certification."""
from pathlib import Path
import json
import sys
import numpy as np
from scipy.optimize import minimize
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from theta import paley_sign
from square_control import square_field_sign


def check(order, signs):
    n = len(signs)
    eye = np.eye(n)
    J = np.ones((n, n)) / n
    root = np.sqrt(n)
    output = []
    for sigma in (-1, 1):
        F = np.fft.ifft((signs == sigma)[:, None] * np.fft.fft(eye, axis=0), axis=0).real
        P = eye - J - F
        ell, kappa = P[:, 0], P[0, 0]
        padding = np.ones(n) - ell / kappa
        bs, ds, errors = [], [], []
        for r in (0.2, 0.4, 0.7):
            # Minimize the target-side metric Q_{-sigma} at anchor one.
            Q = J + r * P + F / r
            def fun(t):
                b = np.r_[1., t]
                return b @ Q @ b
            def jac(t):
                return 2 * (Q @ np.r_[1., t])[1:]
            fit = minimize(fun, np.zeros(n-1), jac=jac,
                           bounds=[(0, None)] * (n-1), method='L-BFGS-B',
                           options={'ftol': 1e-15, 'gtol': 1e-11, 'maxiter': 10000,
                                    'maxls': 50})
            assert fit.success, fit.message
            b = np.r_[1., fit.x]
            B = fun(fit.x)
            y = b / np.sqrt(B)
            x = Q @ y
            c = y.sum() / root
            # M_sigma = 1 / B by exact reciprocity; numerical KKT checked.
            M = 1 / B
            scalar = r / (1-r*r) * (1/M-r-(1-r)*c/np.sqrt(n*M))
            d = (F @ b)[0]
            assert np.min(x[1:]) > -2e-7
            assert np.max(np.abs(x[1:] * y[1:])) < 2e-7
            assert abs(scalar-d) < 2e-7
            bs.append(b)
            ds.append(d)
            errors.append(abs(scalar-d))
        for weights in (np.array([.2,.3,.5]), np.array([1.4,-.6,.2])):
            b = np.asarray(bs).T @ weights
            mu = max(1.01, b.sum()/root + .1)
            Z = root*b + (mu-b.sum()/root)*padding
            f = F @ Z
            Y = Z-f+f[0]*ell/kappa
            dist2 = np.dot(Y-Z,Y-Z)
            pred = np.dot(f,f)+f[0]**2/kappa
            assert abs(Y[0]-root) < 1e-10
            assert abs(Y.mean()-mu) < 1e-10
            assert np.linalg.norm(F @ Y) < 1e-10
            # Independent least squares using an orthonormal basis of im L.
            L = P-np.outer(ell,ell)/kappa
            val, vec = np.linalg.eigh(L)
            U = vec[:,val>.5]
            canonical = mu*np.ones(n)+(root-mu)*ell/kappa
            direct = canonical+U @ (U.T @ (Z-canonical))
            assert np.linalg.norm(Y-direct) < 1e-10
            G = np.array([[(F@bi)@(F@bj)+di*dj/kappa
                           for bj,dj in zip(bs,ds)] for bi,di in zip(bs,ds)])
            assert abs(dist2-pred) < 1e-9
            assert abs(dist2-n*weights@G@weights) < 1e-9
        # Exact finite-field two-width root cancellation, with signed weights.
        d0,d1 = ds[0],ds[-1]
        assert 0 < d0 < d1
        w = np.array([d1/(d1-d0), 0, -d0/(d1-d0)])
        mixed = np.asarray(bs).T @ w
        assert abs((F@mixed)[0]) < 1e-10
        assert abs(-w[-1]-min(ds)/(max(ds)-min(ds))) < 1e-10
        output.append(dict(order=order, sign=sigma,
                           max_scalar_error=max(errors), forbidden_roots=ds,
                           signed_negative_weight=float(-w[-1]),
                           signed_min_entry=float(mixed.min()),
                           signed_forbidden_norm=float(np.linalg.norm(F@mixed))))
    return output


if __name__ == '__main__':
    rows = []
    for p in (29,61,97):
        rows.extend(check(p,paley_sign(p)))
    for t in (5,7,11):
        rows.extend(check(t*t,square_field_sign(t)))
    print(json.dumps({'status':'passed', 'cases':rows},indent=2))
