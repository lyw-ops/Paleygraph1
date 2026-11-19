"""Small actual-Paley checks for Schur clipping and precision sign mass.

Floating diagnostics only. No stationary-point enclosure or HR theorem
is inferred. All mathematical statements are proved in the paired note.
"""

import json
from math import sqrt
from pathlib import Path
import sys

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from poisson_weights import weighted_iterate
from square_control import square_field_sign
from theta import paley_sign


def emit(row):
    print(json.dumps(row, sort_keys=True), flush=True)


def analyze(q, root, tau):
    sign = square_field_sign(root) if root else paley_sign(q)
    n = len(sign)
    weights = np.full(n, tau/n)
    weights[0] = 1.
    c, W = tau/n, float(weights.sum())
    a, rho = sqrt(W/n), tau/W
    vec, phi, residual = weighted_iterate(sign, weights,
                                         tolerance=2e-12, rounds=64)
    assert residual < 2e-9
    large = (phi+abs(vec))/2
    small = weights/large
    plus = np.where(vec >= 0, large, small)
    minus = np.where(vec >= 0, small, large)

    for side, A, B in ((1, plus, minus), (-1, minus, plus)):
        u, v = A/a, B/a
        fA = np.fft.fft(u).real/n
        beta = np.fft.fft(v).real/n
        edge = sign == -side
        assert max(abs(beta[~(edge | (np.arange(n) == 0))])) < 1e-8
        precision = np.fft.fft(1/u).real/n
        kappa = (1-c)*v[0]/n
        expected_precision = (beta-kappa)/rho
        inverse_error = float(max(abs(precision-expected_precision)))
        hadamard = fA*beta
        hadamard[0] -= 1
        epsA = float(np.maximum(-fA, 0).sum()/u[0])
        epsB = float(np.maximum(-beta, 0).sum()/v[0])
        TA, TB = fA/u[0], beta/v[0]
        posA, posB = np.maximum(TA, 0), np.maximum(TB, 0)
        posA /= posA.sum()
        posB /= posB.sum()
        eig_target = np.full(n, c)
        eig_target[0] = 1
        markov_product_error = float(max(abs(np.fft.fft(TA) *
                                              np.fft.fft(TB)-eig_target)))
        near_error = float(max(abs(np.fft.fft(posA) *
                                   np.fft.fft(posB)-eig_target)))
        positive_off_mass = float(np.maximum(precision[1:], 0).sum())
        lower = max(0., (v[0]-1-edge.sum()*kappa)/rho)
        assert inverse_error < 1e-8 and max(abs(hadamard)) < 1e-8
        assert markov_product_error < 1e-8
        assert near_error <= 2*(epsA+epsB)+1e-8
        assert positive_off_mass+1e-8 >= lower
        emit(dict(kind='actual_pair_kernel_check', q=q, square_root=root,
                  tau=tau, side=side, stationary_residual=float(residual),
                  schur_inverse_identity_error=float(max(abs(hadamard))),
                  ordinary_inverse_error=inverse_error,
                  markov_product_error=markov_product_error,
                  normalized_negative_position_mass_A=epsA,
                  normalized_negative_position_mass_B=epsB,
                  positive_markov_product_error=near_error,
                  positive_markov_product_bound=2*(epsA+epsB),
                  precision_positive_off_mass=positive_off_mass,
                  precision_positive_off_mass_lower=lower,
                  precision_diagonal=float(precision[0]),
                  scope='floating actual-pair normalization check; no interval certificate'))

        for R in (0., 1., 2., 4.):
            hinge = np.maximum(u-R, 0.)
            hinge[0] = 0.
            eta = float(hinge.mean())
            nu = float(np.mean(hinge*hinge/u))
            kernel = np.fft.fft(hinge).real/n
            X_eig = np.fft.fft(beta*kernel).real
            Y_row = beta*(np.fft.fft(hinge*hinge/u).real/n)
            Y_eig = np.fft.fft(Y_row).real
            violations = max(0., -float(min(X_eig)),
                             float(max(X_eig))-1.,
                             -float(min(Y_eig-X_eig*X_eig)),
                             -float(min(X_eig-Y_eig)))
            lhs = float(np.sum(abs(beta[edge]*a*kernel[edge])**2))
            rhs = a*a*(nu-eta*eta)
            assert violations < 1e-8 and lhs <= rhs+1e-8
            masked_eig = np.fft.fft(kernel*edge).real
            if R == 0:
                assert min(masked_eig) < -1e-5 and max(masked_eig) > 1e-5
            projected_hinge = a*masked_eig
            energy = float(np.sum((rho/u)*projected_hinge**2))
            emit(dict(kind='actual_bulk_hinge_schur_check', q=q, square_root=root,
                      tau=tau, side=side, threshold=R, eta=eta, nu=nu,
                      schur_Loewner_max_violation=violations,
                      weighted_position_square_sum=lhs,
                      weighted_position_square_bound=rhs,
                      support_mask_min_eigenvalue=float(min(masked_eig)),
                      support_mask_max_eigenvalue=float(max(masked_eig)),
                      actual_H_squared=energy,
                      actual_H_squared_over_eta=energy/eta if eta else None,
                      scope='floating actual hard-hinge check; no HR or prime limit assertion'))


if __name__ == '__main__':
    for q, root, tau in ((101, None, .05), (401, None, .05),
                         (361, 19, .05), (401, None, .01)):
        analyze(q, root, tau)
