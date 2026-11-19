"""Recheck the collision comparison and deterministic sparse square control."""

from math import exp, expm1, log, sqrt

import numpy as np
from scipy.integrate import quad
from scipy.special import ive, xlogy

from poisson_weights import log_bounds
from square_control import square_field_sign


def collision_check(c):
    m = c / -expm1(-c)

    def density_difference(x):
        if x == 0:
            return 1 - m * c / expm1(c)
        y = m * x
        t = 2 * sqrt(c * y)
        return exp(-x) - m * exp(t - y) * sqrt(c / y) * ive(1, t) / expm1(c)

    def integrals(sign):
        return [
            quad(lambda x: max(sign * density_difference(x), 0) * f(x), 0, np.inf,
                 epsabs=2e-12, epsrel=1e-10, limit=200)[0]
            for f in (lambda _: 1, lambda x: x, lambda x: x * log(x))
        ]

    left, right = integrals(1), integrals(-1)
    balance = max(abs(left[j] - right[j]) for j in (0, 1))
    assert balance < 2e-10
    gap = sum(phi - p * xlogy(first / p, first / p) for p, first, phi in (left, right))
    assert gap >= 0
    print(f"c={c:g}: balance={balance:.2g}, residual entropy bound / c^2={gap / c**2:.6f}")


def square_check(r, j):
    n, b, m = (r * r - 1) // 2, r - 1, (r + 1) // 2
    k = j * j
    profile = np.cumsum(1 / np.arange(k, 0, -1, dtype=float)).reshape(j, j)
    rows = np.arange(j)[None, :]
    cols = np.arange(j)[:, None]
    labels = rows + b * (((cols - rows) * pow(b, -1, m)) % m)
    assert np.unique(labels).size == k

    w = np.zeros(n)
    w[labels] = profile / k
    w /= w.sum()
    a1 = log(b / m)
    d_all = xlogy(profile, profile).mean()
    col_means = profile.mean(axis=1)
    delta = d_all - xlogy(col_means, col_means).mean()
    assert 0 <= delta <= np.sum(1 / np.arange(1, k + 1)) / j

    theoretical = (a1 - d_all, a1 - d_all + 2 * delta)
    sign = square_field_sign(r)
    lo, hi, residual = log_bounds(sign, w, floor_mass=1e-4)
    assert theoretical[0] - 2e-8 <= lo <= hi <= theoretical[1] + 2e-8
    flat = labels.ravel()
    kernel = np.fft.fft(sign).real[(flat[:, None] - flat) % n] / n
    norm = np.max(np.abs(np.linalg.eigvalsh(kernel)))
    print(f"r={r}, j={j}, k={k}: theory=[{theoretical[0]:.8f}, {theoretical[1]:.8f}], "
          f"FFT=[{lo:.8f}, {hi:.8f}], residual={residual:.2g}, ||K_SS||={norm:.4f}")


if __name__ == "__main__":
    for c in (0.0001, 0.001, 0.01, 0.1, 0.25, 0.5):
        collision_check(c)
    for r, j in ((13, 3), (29, 5), (37, 6), (97, 10)):
        square_check(r, j)
