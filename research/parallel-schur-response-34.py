"""Exact small Paley incidence checks and floating actual-source diagnostics.

Only stdout is written. Run with -B. The actual-source records are floating
checks of proved finite identities, not stationary enclosures or uniform bounds.
"""

import argparse
import json
from math import sqrt
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
from poisson_weights import weighted_iterate
from square_control import square_field_sign
from theta import paley_sign, prime_field_generator


def emit(row):
    print(json.dumps(row, sort_keys=True), flush=True)


def exact_incidence(prime):
    signs = paley_sign(prime).astype(int).tolist()
    n = len(signs)
    generator = prime_field_generator(prime)
    squares = {x*x % prime for x in range(1, prime)}

    def chi(x):
        x %= prime
        return 0 if x == 0 else (1 if x in squares else -1)

    checks = 0
    for epsilon in (1, -1):
        E = {j for j in range(n) if signs[j] == epsilon}
        assert len(E) == (prime-3-2*epsilon)//4
        for d in range(1, n):
            t = pow(generator, 2*d, prime)
            L = sum(chi(x*(x-1)*(x-t)) for x in range(prime))
            count = sum((k-d) % n in E for k in E)
            assert 8*count == prime-7-4*epsilon-4*epsilon*signs[d]+L
            assert L*L <= 4*prime
            checks += 1
    emit(dict(kind="exact_prime_incidence", p=prime, checks=checks,
              arithmetic="Python integers; direct cubic Legendre sums",
              all_checks_passed=True))


def analyze(order, root, tau):
    signs = (square_field_sign(root) if root else paley_sign(order)).astype(int)
    n = len(signs)
    c = tau/n
    weights = np.full(n, c)
    weights[0] = 1.
    W, a = float(weights.sum()), sqrt(float(weights.mean()))
    rho = tau/W
    vector, phi, residual = weighted_iterate(signs, weights,
                                            tolerance=2e-12, rounds=128)
    assert residual < 2e-9, (order, tau, residual)
    large = (phi+abs(vector))/2
    small = weights/large
    Aplus = np.where(vector >= 0, large, small)
    Aminus = np.where(vector >= 0, small, large)
    signs_convolution = np.fft.ifft(np.fft.fft(signs)**2).real
    elliptic = 2*signs_convolution+2

    for side, A, B in ((1, Aplus, Aminus), (-1, Aminus, Aplus)):
        u, v = A/a, B/a
        dweight = rho/u
        epsilon = -side
        E = signs == epsilon
        beta = np.fft.fft(v).real/n
        edge_count = int(E.sum())
        incidence = np.fft.ifft(np.fft.fft(E.astype(float))**2).real
        assert max(abs(8*incidence[1:]-(order-7-4*epsilon
                   -4*epsilon*signs[1:]+elliptic[1:]))) < 2e-7
        tmark = (1-c)*v[0]/n
        thresholds = (0., .5, 1., 2., 4.)
        qs, kappas, etas = [], [], []
        for R in thresholds:
            qR = np.maximum(u-R, 0.)
            qR[0] = 0.
            eta = float(qR.mean())
            nu = float(np.mean(qR*qR/u))
            zeta = float(np.mean(qR/u))
            kappa = np.fft.fft(qR).real/n
            qs.append(qR)
            kappas.append(kappa)
            etas.append(eta)
            weighted_coeff = float(np.dot(beta[E]**2, kappa[E]**2))
            slack = nu-eta*eta
            assert weighted_coeff <= slack+1e-10
            trace = float(np.dot(incidence, beta*kappa))
            cubic_correlation = float(np.dot(elliptic[E], beta[E]*kappa[E]))
            main = (order+5)*eta/8+(order-11-4*epsilon)*rho*zeta/8
            predicted = main+cubic_correlation/8
            S = float(np.dot(incidence, kappa))
            corrected_trace = trace-tmark*S
            assert corrected_trace >= -1e-7
            trace_error = abs(trace-predicted)
            assert trace_error < 1e-6*max(1., abs(trace))
            cp_hasse_bound = 2*sqrt(order*edge_count*max(0., slack))
            assert abs(cubic_correlation) <= cp_hasse_bound+1e-5
            kE = np.where(E, kappa, 0.)
            z = a*np.fft.fft(kE).real
            energy = float(np.dot(dweight, z*z))
            diagonal = float(np.dot(z, z))
            signed_triangle = float(np.dot(v-1, z*z))
            marked = float((1-c)*v[0]*z[0]*z[0])
            triangle_error = abs(energy-(diagonal+signed_triangle-marked))
            assert triangle_error < 1e-7*max(1., energy, marked)
            assert energy <= W*eta*corrected_trace+1e-7
            emit(dict(kind="actual_hinge_trace_and_CP", q=order, square_root=root,
                      tau=tau, side=side, R=R, stationary_residual=float(residual),
                      eta=eta, nu=nu, weighted_coefficient_square=weighted_coeff,
                      CP_variance_bound=slack,
                      actual_CP_fraction_of_bound=weighted_coeff/slack if slack > 1e-25 else None,
                      trace=trace, corrected_trace=corrected_trace,
                      normalized_corrected_trace=corrected_trace/n,
                      R0_trace_limit=(1+2*tau)/(4*(1+tau)),
                      incidence_trace_identity_error=trace_error,
                      elliptic_signed_correlation=cubic_correlation,
                      elliptic_CP_Hasse_bound=cp_hasse_bound,
                      trace_mark_subtraction=tmark*S,
                      H_squared=energy, H_squared_over_eta=energy/eta if eta > 1e-25 else None,
                      trace_HR_constant=W*corrected_trace,
                      triangle_diagonal=diagonal, triangle_signed=signed_triangle,
                      triangle_mark_subtraction=marked, triangle_identity_error=triangle_error,
                      scope="floating actual-source diagnostic, not a rigorous enclosure"))

            if R == 2. and eta > 1e-20:
                for cutoff in (.1, .3, 1.):
                    low = E & (abs(beta)*sqrt(n) <= cutoff)
                    lowk = np.where(low, kappa, 0.)
                    lowz = a*np.fft.fft(lowk).real
                    highz = z-lowz
                    LL = float(np.dot(dweight, lowz*lowz))
                    HH = float(np.dot(dweight, highz*highz))
                    mixed = float(2*np.dot(dweight, lowz*highz))
                    assert abs(LL+HH+mixed-energy) < 1e-8
                    emit(dict(kind="actual_beta_small_source_split", q=order,
                              square_root=root, tau=tau, side=side, R=R,
                              normalized_beta_cutoff=cutoff,
                              small_vertex_fraction=float(low.sum()/edge_count),
                              small_source_l2_fraction=float(np.dot(lowk, lowk)/np.dot(kE, kE))
                                  if np.dot(kE, kE) else 0.,
                              low_low_corrected_energy=LL,
                              high_high_corrected_energy=HH,
                              signed_mixed_corrected_energy=mixed,
                              total_corrected_energy=energy,
                              scope="floating split; all pieces retain the marked subtraction"))

        qs, kappas, etas = np.array(qs), np.array(kappas), np.array(etas)
        source_gram = (qs/u) @ qs.T/n-np.outer(etas, etas)
        coefficient_gram = (kappas[:, E]*beta[E]**2) @ kappas[:, E].T
        gap = source_gram-coefficient_gram
        minimum = float(np.linalg.eigvalsh((gap+gap.T)/2)[0])
        assert minimum >= -1e-9
        emit(dict(kind="actual_joint_threshold_CP_Gram", q=order, square_root=root,
                  tau=tau, side=side, thresholds=thresholds,
                  minimum_slack_eigenvalue=minimum,
                  scope="floating check of the proved joint Gram domination"))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--large", action="store_true")
    args = parser.parse_args()
    for p in (13, 101, 401):
        exact_incidence(p)
    cases = [(401, None, .01), (1009, None, .01), (9413, None, .01),
             (361, 19, .01)]
    if args.large:
        cases += [(153649, None, .01), (1000033, None, .01), (151321, 389, .01)]
    for case in cases:
        analyze(*case)
    emit(dict(kind="all_checks_passed", cases=len(cases),
              exact_integer_rows=3, actual_rows_are_floating=True))
