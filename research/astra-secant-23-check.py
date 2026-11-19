"""Numerical formula checks only; no asymptotic or interval certificate."""

from pathlib import Path
import json
import sys

import numpy as np
from scipy.optimize import linprog, minimize, minimize_scalar

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from theta import paley_sign
from square_control import square_field_sign


def quadratic(matrix, mass_cap=None):
    n = len(matrix)

    def unpack(x):
        return np.r_[1.0, x]

    def fun(x):
        b = unpack(x)
        return b @ matrix @ b

    def jac(x):
        return 2 * (matrix @ unpack(x))[1:]

    constraints = []
    if mass_cap is not None:
        constraints = [{"type": "ineq",
                        "fun": lambda x: mass_cap - 1 - x.sum(),
                        "jac": lambda x: -np.ones(n - 1)}]
    result = minimize(fun, np.zeros(n - 1), jac=jac,
                      bounds=[(0, None)] * (n - 1),
                      constraints=constraints, method="SLSQP",
                      options={"ftol": 2e-12, "maxiter": 2000})
    if not result.success:
        raise RuntimeError(result.message)
    return result.fun


def check_case(order, sign):
    n = len(sign)
    eye = np.eye(n)
    root = np.sqrt(n)
    J = np.ones((n, n)) / n
    rows = []
    for side in (-1, 1):
        mask = sign == side
        P = np.fft.ifft(mask[:, None] * np.fft.fft(eye, axis=0), axis=0).real
        assert np.linalg.norm(P @ P - P) < 1e-12
        # Exact-sector opposite endpoint: minimize mass with P b = 0.
        endpoint = linprog(np.ones(n), A_eq=np.vstack((P, eye[0])),
                           b_eq=np.r_[np.zeros(n), 1],
                           bounds=(0, None), method="highs")
        assert endpoint.success
        min_mass = endpoint.fun / root
        for fraction in (0.45, 0.8, 1.1):
            c = 1 / root + fraction * (min_mass - 1 / root)
            primal = quadratic(root * P, c * root)

            if fraction > 1:
                # The endpoint LP supplies a feasible zero-energy row.
                # Its mean is strictly below c, so the dual supremum is
                # exactly zero at R=0. Avoid ill-conditioned tiny-R QPs.
                assert abs(primal) < 2e-8
                rows.append(dict(order=order, sign=side, c=c, primal=primal,
                                 dual=0.0, error=abs(primal),
                                 dual_method="zero-energy endpoint"))
                continue

            def dual(R):
                return quadratic(root * P + R * J) - R * c * c

            upper = 1.0
            while dual(upper) > 0:
                upper *= 2
                assert upper < 1e6
            opt = minimize_scalar(lambda R: -dual(R), bounds=(0, upper),
                                  method="bounded",
                                  options={"xatol": 2e-8})
            dual_value = max(0.0, -opt.fun)
            error = abs(primal - dual_value)
            assert error < 2e-7, (order, side, c, primal, dual_value)
            rows.append(dict(order=order, sign=side, c=c, primal=primal,
                             dual=dual_value, error=error))
    return rows


def main():
    mixing_error = 0.0
    for beta in (0.3, 1 / np.sqrt(2), 1.0):
        for gap in (0.1, 0.4, 0.8):
            for energy in (0.2, np.sqrt(2), 2.0):
                for factor in (1, 2, 10):
                    R = factor * gap / (beta * energy)
                    u = gap / (beta * energy * R)
                    value = (beta + u * gap) ** 2 / (1 + R * energy * u * u)
                    formula = beta * beta + gap * gap / (energy * R)
                    mixing_error = max(mixing_error, abs(value - formula))
    assert mixing_error < 3e-15
    artificial_error = 0.0
    for m in (3, 7, 31):
        for R in (0.25, 1.0, float(m)):
            x = np.linspace(0, 1, 10001)
            energies = m / (m - 1) * (x - 1 / m) ** 2
            maximum = np.max(x * x / (1 + R * energies))
            formula = 1 / (1 + R * (1 - 1 / m))
            artificial_error = max(artificial_error, abs(maximum - formula))
    assert artificial_error < 1e-15
    rows = []
    for p in (29, 61):
        rows.extend(check_case(p, paley_sign(p)))
    for t in (5, 7):
        rows.extend(check_case(t * t, square_field_sign(t)))
    print(json.dumps(dict(mixing_checks=81, mixing_max_error=mixing_error,
                          artificial_checks=9,
                          artificial_max_error=artificial_error,
                          dual_checks=len(rows),
                          dual_max_error=max(row["error"] for row in rows),
                          square_scaled_tail_lower=1.5 - np.sqrt(2),
                          square_secant_limsup_lower=3 / np.sqrt(2) - 2,
                          records=rows), indent=2))


if __name__ == "__main__":
    main()
