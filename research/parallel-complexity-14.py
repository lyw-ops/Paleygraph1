"""Replay the marked contraction loss and the first harmonic cutoff."""

from math import expm1, hypot, pi, sqrt
from pathlib import Path
import sys

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from smoothing import kernel_action
from square_control import square_field_sign
from theta import paley_sign, prime_field_generator


def activation(v):
    out = np.abs(v)
    out[0] = hypot(v[0], 2)
    return out


def replay_loss(sign, width, depth):
    n = len(sign)
    d = (1 - width) / (1 + width)

    def step(v):
        return d * kernel_action(sign, activation(v))

    z = np.zeros(n)
    for _ in range(10000):
        next_z = step(z)
        if np.linalg.norm(next_z - z) < 5e-14:
            break
        z = next_z
    else:
        raise RuntimeError("fixed point did not converge")

    residual = np.linalg.norm(step(z) - z)
    phi_z = activation(z)
    m = np.arcsinh(z[0] / 2)
    c = phi_z.sum() / (2 * sqrt(n))
    np.testing.assert_allclose(
        z @ z, 4 * d**2 * (1 - c**2) / (1 - d**2), rtol=2e-12, atol=2e-12,
    )
    marks = []
    max_identity_error = 0.0
    v = np.zeros(n)
    for _ in range(depth):
        mt = np.arcsinh(v[0] / 2)
        marks.append(mt)
        a = activation(v)
        new_v = step(v)
        w, new_w = z - v, z - new_v
        lhs = w @ w - (new_w @ new_w) / d**2
        mark_loss = 16 * np.sinh((m - mt) / 2)**2
        bulk_loss = 4 * np.maximum(-z[1:] * v[1:], 0).sum()
        mean_loss = ((phi_z - a).sum() / sqrt(n))**2
        max_identity_error = max(max_identity_error, abs(lhs - mark_loss - bulk_loss - mean_loss))
        v = new_v

    weights = d ** (2 * np.arange(depth - 1, -1, -1, dtype=float))
    weights /= weights.sum()
    mean_gap = abs(m - weights @ marks)
    rms_gap = sqrt(weights @ (m - np.array(marks))**2)
    bound = sqrt((1 - c**2) / expm1(-2 * depth * np.log(d)))
    assert max_identity_error < 2e-12
    assert rms_gap <= bound + 2e-12
    return max_identity_error, mean_gap, rms_gap, bound, residual


def replay_harmonics(p, cutoff):
    n = (p - 1) // 2
    root = prime_field_generator(p)
    chi = np.full(p, -1, dtype=int)
    chi[0] = 0
    chi[(np.arange(1, n + 1, dtype=np.int64)**2) % p] = 1
    full_sign = np.array([chi[(1 - pow(root, j, p)) % p] for j in range(2 * n)])
    sign = full_sign[::2]
    z = -np.fft.fft(full_sign) / sqrt(p)
    np.testing.assert_allclose(abs(z[1:n]), 1, atol=2e-14, rtol=0)
    np.testing.assert_allclose(z[:n].conj(), z[n:], atol=2e-14, rtol=0)
    x = np.fft.fft(sign).real / sqrt(n)
    np.testing.assert_allclose(x, -sqrt(p / n) * z[:n].real, atol=2e-14, rtol=0)

    # Match the exact |x| at the bad character 0 to isolate the Fourier tail.
    theta = np.angle(z[1:n])
    fit = np.abs(x)
    fit[1:] = 2 / pi
    for h in range(1, cutoff + 1):
        fit[1:] += (4 / pi) * (-1)**(h + 1) * np.cos(2 * h * theta) / (4 * h**2 - 1)
    fit[1:] *= sqrt(p / n)
    sup_error = np.max(np.abs(fit - abs(x)))
    feedback_error = np.linalg.norm(kernel_action(sign, fit - abs(x))) / sqrt(n)
    tail = 2 * sqrt(p / n) / (pi * (2 * cutoff + 1))
    assert feedback_error <= sup_error + 2e-14
    assert sup_error <= tail + 2e-14
    return sup_error, feedback_error, tail


if __name__ == "__main__":
    print("loss: q,r,T,max_identity_error,mean_gap,rms_gap,upper,residual")
    orders = [(5, paley_sign(5)), (409, paley_sign(409)), (961, square_field_sign(31))]
    for q, sign in orders:
        for width, depth in [(0.01, 32), (0.03, 64), (0.08, 96)]:
            values = replay_loss(sign, width, depth)
            print(f"{q},{width},{depth},", ",".join(f"{v:.8g}" for v in values), sep="")
    print("harmonics: p,H,sup_error,normalized_feedback_error,tail")
    for p in [97, 1009, 9413]:
        for cutoff in [8, 32, 128]:
            values = replay_harmonics(p, cutoff)
            print(f"{p},{cutoff},", ",".join(f"{v:.8g}" for v in values), sep="")
