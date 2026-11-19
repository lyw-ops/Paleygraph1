"""Floating-point checks of bounded root-preserving dynamics; not certificates."""
import json
import runpy
import sys
from pathlib import Path
import numpy as np
from scipy.optimize import minimize
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from theta import paley_sign
from square_control import square_field_sign
soft = runpy.run_path(str(Path(__file__).with_name('soft-tail-21.py')))
rows = []
for order, sign in [(61, paley_sign(61)), (97, paley_sign(97)),
                    (49, square_field_sign(7)), (121, square_field_sign(11))]:
    for side in [-1, 1]:
        pin, M, kap, ell, b, _ = soft['geometry'](sign, side)
        n = len(sign)
        L = np.column_stack([pin(e) for e in np.eye(n)])
        eig, vectors = np.linalg.eigh(L)
        Q = vectors[:, eig > .5]
        Y0 = np.ones(n) + (np.sqrt(n)-1)*ell/kap
        for lam in [.5, 4.]:
            lip = np.max(b/M[1:]**2)/lam
            for radius in [.1, .4]:
                R = radius*n**.25
                def evaluate(z):
                    Y = Y0 + Q@z
                    _, val, v = soft['hinge_envelope'](-Y[1:]/M[1:], b, lam)
                    w = np.r_[0., v/M[1:]]
                    return val, -Q.T@w, w, v
                opt = minimize(lambda z: evaluate(z)[0], np.zeros(Q.shape[1]),
                               jac=lambda z: evaluate(z)[1], method='SLSQP',
                               constraints=[dict(type='ineq', fun=lambda z: R*R-z@z,
                                                 jac=lambda z: -2*z)],
                               options=dict(ftol=1e-13, maxiter=1500))
                assert opt.success, opt.message
                val, grad, w, v = evaluate(opt.x)
                dual = -w@Y0-lam/2*np.sum(v*v/b)-R*np.linalg.norm(Q.T@w)
                gap = val-dual
                assert -1e-9 < gap < 3e-6, (order, side, lam, radius, gap)
                z = np.zeros(Q.shape[1])
                for k in range(1, 65):
                    z -= evaluate(z)[1]/lip
                    norm = np.linalg.norm(z)
                    if norm > R:
                        z *= R/norm
                    # A feasible dual gives a stronger numerical check than comparison
                    # against the possibly inexact primal optimum.
                    err_upper = lam*(evaluate(z)[0]-dual)
                    bound = lam*lip*R*R/(2*k)
                    assert err_upper <= bound+3e-6, (k, err_upper, bound)
                rows.append(dict(order=order, side=side, penalty=lam, radius=radius,
                                 primal=val, dual=dual, gap=gap,
                                 scaled_pg_error_upper=err_upper,
                                 scaled_pg_bound=bound,
                                 mark_error=abs(Y0[0]-np.sqrt(n)),
                                 mean_error=abs(Y0.mean()-1)))
print(json.dumps(dict(checks=len(rows), max_duality_gap=max(r['gap'] for r in rows),
                      records=rows), indent=2))
