"""Replay exact-form signed extrapolation and anchored finish bounds."""

import json
from math import sqrt
from pathlib import Path
import sys

import numpy as np


sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from square_control import square_field_sign
from theta import paley_sign


def full_paley(prime):
    n = prime
    chi = np.full(n, -1, dtype=int)
    chi[[a*a % n for a in range(n)]] = 1
    chi[0] = 0
    K = chi[(np.arange(n)[:, None] - np.arange(n)) % n]/sqrt(n)
    J = np.ones((n, n))/n
    P = (np.eye(n) - J - K)/2
    F = (np.eye(n) - J + K)/2
    root = np.eye(n)[0]
    negative = (chi == -1).astype(float)
    positive = (chi == 1).astype(float)
    widths = (.2, .7)
    rows, heights, kkt_errors = [], [], []
    for width in widths:
        damping = (1 - width)/(1 + width)
        height = 2*damping/(sqrt(n) + damping)
        y = root + height*negative
        x = root + height*positive
        Q = J + width*P + F/width
        error = float(np.linalg.norm(Q@y - x))
        if error > 3e-11 or abs(y@Q@y - 1) > 3e-11:
            raise RuntimeError("the explicit reciprocal KKT pair failed")
        rows.append(y)
        heights.append(height)
        kkt_errors.append(error)
    endpoint_height = 2/(sqrt(n) + 1)
    alpha = (endpoint_height - heights[1])/(heights[0] - heights[1])
    coefficients = np.array([alpha, 1-alpha])
    extrapolated = np.column_stack(rows)@coefficients
    endpoint = root + endpoint_height*negative
    forbidden = [F@row for row in rows]
    forbidden_roots = [row[0] for row in forbidden]
    gram = np.array([
        [left@right + forbidden_roots[i]*forbidden_roots[j]/P[0, 0]
         for j, right in enumerate(forbidden)]
        for i, left in enumerate(forbidden)
    ])
    error = float(np.linalg.norm(extrapolated-endpoint))
    if error > 3e-12 or np.linalg.norm(F@extrapolated) > 3e-12:
        raise RuntimeError("the signed endpoint cancellation failed")
    if extrapolated.min() < -3e-13 or abs(extrapolated.sum()-sqrt(n)) > 3e-12:
        raise RuntimeError("the endpoint positivity or mass failed")
    return dict(kind="full_paley_signed", order=n, coefficients=coefficients.tolist(),
                max_kkt_error=max(kkt_errors), endpoint_error=error,
                forbidden_norm=float(np.linalg.norm(F@extrapolated)),
                gram_cost_squared=float(coefficients@gram@coefficients),
                normalized_endpoint_mass=float(extrapolated.sum()/sqrt(n)))


def finish_record(order, signs, side):
    n = len(signs)
    eye = np.eye(n)
    J = np.ones((n, n))/n
    P = np.fft.ifft((signs == side)[:, None]*np.fft.fft(eye, axis=0), axis=0).real
    F = eye-J-P
    ell = P[:, 0]
    kappa = P[0, 0]
    L = P - np.outer(ell, ell)/kappa
    M = np.ones(n)-ell/kappa
    omega = (1+sqrt(2*n+1))/(2*n)
    eta = (1-omega/kappa)/(omega+omega**2/kappa)
    heights = M[1:]*(1+eta*(kappa+ell[1:]))
    caps = M[1:]/heights
    mean = 1.05
    source = 1+.3*np.cos(2*np.pi*np.arange(n)/n)
    source[0] = 0
    source *= (n*mean-sqrt(n))/source.sum()
    source[0] = sqrt(n)
    f = F@source
    Y = source-f+f[0]*ell/kappa
    distance = float(np.linalg.norm(Y-source))
    E = np.maximum(-Y[1:], 0)
    scores = E/M[1:]
    order_indices = np.argsort(-scores)
    cumulative = np.cumsum(caps[order_indices])
    threshold = 0.
    if cumulative[-1] >= 1:
        crossing = int(np.searchsorted(cumulative, 1))
        threshold = max(0., float(scores[order_indices[crossing]]))
    w = np.r_[0., np.maximum(E-threshold*M[1:], 0)/heights]
    delta = threshold+w.sum()
    correction = delta*M+eta*(L@w)
    repaired = Y+correction
    H = float(np.min(M[1:]*heights))
    radius_bound_squared = distance**2*((n+1/kappa)/H+eta**2/float(heights.min())**2)
    orthogonality = delta**2*(n+1/kappa)+eta**2*np.linalg.norm(L@w)**2
    if repaired.min() < -3e-11 or np.linalg.norm(F@repaired) > 3e-11:
        raise RuntimeError("the anchored finish was infeasible")
    if abs(repaired[0]-sqrt(n)) > 3e-11 or abs(repaired.mean()-mean-delta) > 3e-11:
        raise RuntimeError("the anchored finish changed its mark or predicted mean")
    if delta > distance/sqrt(H)+3e-11:
        raise RuntimeError("the mean-price bound failed")
    if abs(correction@correction-orthogonality) > 3e-10:
        raise RuntimeError("the exact radius decomposition failed")
    if correction@correction > radius_bound_squared+3e-10:
        raise RuntimeError("the radius bound failed")
    return dict(kind="localized_finish", order=order, side=side,
                source_projection_cost=distance, initial_defect=float(np.linalg.norm(E)),
                added_mean=float(delta), added_mean_upper=distance/sqrt(H),
                correction_norm=float(np.linalg.norm(correction)),
                correction_norm_upper=sqrt(radius_bound_squared),
                repaired_minimum=float(repaired.min()),
                radius_identity_error=abs(float(correction@correction-orthogonality)))


def main():
    for prime in (5, 13, 29, 61, 97, 401):
        print(json.dumps(full_paley(prime)))
    cases = [(p, paley_sign(p)) for p in (29, 61, 97)]
    cases += [(p*p, square_field_sign(p)) for p in (7, 11)]
    for order, signs in cases:
        for side in (-1, 1):
            print(json.dumps(finish_record(order, signs, side)))


if __name__ == "__main__":
    main()
