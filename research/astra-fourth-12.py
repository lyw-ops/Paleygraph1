"""Replay the fourth-moment baseline and contact bounds in astra-fourth-12.md.

Run with .venv/bin/python -B research/astra-fourth-12.py [--certificate].
The script writes no files. Small numerical QPs use the previous dense NNLS
solver; --large adds two numerical FFT solves. Certificates use Arb throughout.
"""

import argparse
import importlib.util
import json
from pathlib import Path

import numpy as np


spec = importlib.util.spec_from_file_location(
    "convolution_11", Path(__file__).with_name("astra-convolution-11.py")
)
previous = importlib.util.module_from_spec(spec)
spec.loader.exec_module(previous)


def check(q, characteristic, kappa):
    maker = previous.paley_sign if q == characteristic else previous.square_field_sign
    sign = maker(characteristic)
    n = len(sign)
    r = kappa / np.sqrt(q)
    x, y, _, residual = previous.solve(sign, r)
    row = previous.metrics(sign, r, x, y, residual)
    c2 = row["c2"]
    b = 1 - c2
    t = (n * c2 - 1) / (n - 1)
    heights = (x / x[0] + x[0] * y)[1:]
    correlations = np.fft.ifft(np.fft.fft(x).conj() * np.fft.fft(y)).real
    deviations = correlations[1:] - t
    nv = n * row["centered_variance"]
    positive = np.where(heights - t > 1e-10, heights - t, 0.0)
    count = np.count_nonzero(positive > 1e-10)
    if count == n - 1:
        raise AssertionError("a positive contact excess cannot occupy every shift")
    contact = np.dot(positive, positive) + positive.sum() ** 2 / (n - 1 - count)
    model_deviation = np.full(n - 1, -positive.sum() / (n - 1 - count))
    model_deviation[positive > 1e-10] = positive[positive > 1e-10]
    jacobi = np.fft.fft(sign).real
    covariance_model = np.dot(jacobi[1:], model_deviation) / n
    covariance_error = np.sqrt((n - 1 - 1 / (n - 1)) / n * max(0.0, nv - contact))
    b_lower = 4 * r / (1 + r) ** 2 * (1 - 1 / np.sqrt(n)) ** 2
    B4 = row["cross_bulk_fourth"] / r**2
    raw = c2 * np.sqrt(n * B4)
    raw_lower = 4 * np.sqrt(n / (n - 1)) * (1 - 1 / np.sqrt(n)) ** 2 / (1 + r) ** 2
    errors = [abs(np.dot(deviations, deviations) - nv),
              max(0.0, b_lower - b), max(0.0, contact - nv),
              max(0.0, raw_lower - raw),
              max(0.0, np.max(heights - correlations[1:])),
              max(0.0, abs(row["signed_covariance"] - covariance_model) - covariance_error)]
    assert max(errors) < 2e-8
    return dict(q=q, kappa=kappa, b=b, b_lower=b_lower, B4=B4,
                nV=nv, contact_bound=float(contact), positive_contacts=int(count),
                contact_fraction=float(contact / nv) if nv > 1e-20 else None,
                covariance_model=float(covariance_model), covariance_error=float(covariance_error),
                signed_energy_lower=float(covariance_model - covariance_error - b / (n - 1)),
                raw_density=float(raw), raw_density_lower=float(raw_lower),
                identity_error=float(max(errors)), qp_residual=residual)


def certificate(q, characteristic, denominator, positive, contacts):
    from flint import acb, arb, arb_mat, ctx

    ctx.prec = 192
    maker = previous.paley_sign if q == characteristic else previous.square_field_sign
    signs = list(map(int, maker(characteristic)))
    n = len(signs)
    r = arb(1) / denominator
    d = (1 - r) / (1 + r)
    kernel = [sum((s * (2 * arb.pi() * ((i * j) % n) / n).cos()
                   for j, s in enumerate(signs)), arb(0)) / n for i in range(n)]
    orthant = [1 if i in positive else -1 for i in range(1, n)]
    matrix = arb_mat([[int(i == j) - d * kernel[(i - j) % n] * orthant[j - 1]
                       for j in range(1, n)] for i in range(1, n)])
    beta = matrix.solve(arb_mat([[d * kernel[i]] for i in range(1, n)]))
    assert all(orthant[i - 1] * beta[i - 1, 0] > 0 for i in range(1, n))
    gamma = d * (kernel[0] + sum((kernel[i] * orthant[i - 1] * beta[i - 1, 0]
                                 for i in range(1, n)), arb(0)))
    assert abs(gamma) < 1
    u0 = 2 / (1 - gamma**2).sqrt()
    x = [u0 * (1 + gamma) / 2] + [
        u0 * beta[i - 1, 0] if orthant[i - 1] > 0 else arb(0) for i in range(1, n)]
    y = [u0 * (1 - gamma) / 2] + [
        -u0 * beta[i - 1, 0] if orthant[i - 1] < 0 else arb(0) for i in range(1, n)]
    mass = sum(x, arb(0))
    c2 = mass**2 / n
    b = 1 - c2
    f, g = acb.dft([v / mass for v in x]), acb.dft([v / mass for v in y])
    F = sum((abs(v * w.conjugate())**2 for v, w in zip(f[1:], g[1:])), arb(0))
    nv = n * (c2**2 * F - b**2 / (n - 1))
    t = (n * c2 - 1) / (n - 1)
    excess = [x[i] / x[0] + x[0] * y[i] - t for i in contacts]
    assert all(v > 0 for v in excess)
    bound = sum((v**2 for v in excess), arb(0)) + sum(excess, arb(0))**2 / (n - 1 - len(contacts))
    assert nv > bound
    model_deviation = [-sum(excess, arb(0)) / (n - 1 - len(contacts)) for _ in range(n - 1)]
    for i, value in zip(contacts, excess):
        model_deviation[i - 1] = value
    covariance_model = sum((kernel[i] * model_deviation[i - 1] for i in range(1, n)), arb(0))
    covariance_error = ((arb(n - 1) - arb(1) / (n - 1)) / n * (nv - bound)).sqrt()
    signed_energy_lower = covariance_model - covariance_error - b / (n - 1)
    assert b > 4 * r / (1 + r)**2 * (1 - 1 / arb(n).sqrt())**2
    if q == 49:
        assert bound / nv > arb(965) / 1000
        assert nv > arb(719) / 10000
        assert F / r**2 > 5
        assert signed_energy_lower > arb(8) / 100
    print(json.dumps(dict(certificate=f"q={q}, r=1/{denominator}, strict actual-QP orthant",
        b=str(b), nV=str(nv), contact_bound=str(bound),
        contact_fraction=str(bound / nv), B4=str(F / r**2),
        covariance_model=str(covariance_model), covariance_error=str(covariance_error),
        signed_energy_lower=str(signed_energy_lower)), ensure_ascii=False))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--certificate", action="store_true")
    parser.add_argument("--large", action="store_true")
    args = parser.parse_args()
    if args.certificate:
        certificate(13, 13, 4, {1, 2, 4, 5}, [])
        certificate(49, 7, 28, {4, 6, 12, 18, 20}, [6, 12, 18])
        return
    cases = [(p, p) for p in [13, 17, 29, 41, 61, 97, 173, 257, 401]]
    cases += [(p * p, p) for p in [7, 11, 13]]
    if args.large:
        cases += [(9409, 97), (9413, 9413)]
    for q, p in sorted(cases):
        kappas = [.25] if q > 401 else [.0625, .25, 1.0, 4.0]
        for kappa in kappas:
            if kappa <= np.sqrt(q):
                print(json.dumps(check(q, p, kappa)), flush=True)


if __name__ == "__main__":
    main()
