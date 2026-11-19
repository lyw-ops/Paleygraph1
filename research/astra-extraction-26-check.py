"""Exact algebra and Arb checks for astra-extraction-26.md.

Writes only JSON to stdout.  No optimization or floating-point feasibility
test is used.  The finite checks do not assert a prime asymptotic.
"""

from fractions import Fraction as F
import json
from math import isqrt

from flint import acb, arb, ctx


ctx.prec = 160


def ball(x):
    x = F(x)
    return arb(x.numerator) / x.denominator


def factors(n):
    out = []
    for d in range(2, isqrt(n) + 1):
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
    if n > 1:
        out.append(n)
    return out


def square_sign(r):
    """Integer arithmetic in F_r[t]/(t^2-d), followed by norm characters."""
    assert r > 3 and all(r % d for d in range(2, isqrt(r) + 1))
    d = next(x for x in range(2, r) if pow(x, (r - 1) // 2, r) == r - 1)

    def mul(x, y):
        return ((x[0] * y[0] + d * x[1] * y[1]) % r,
                (x[0] * y[1] + x[1] * y[0]) % r)

    def power(x, k):
        y = (1, 0)
        while k:
            if k & 1:
                y = mul(y, x)
            x, k = mul(x, x), k // 2
        return y

    divs = factors(r * r - 1)
    gen = next((a, b) for b in range(1, r) for a in range(r)
               if all(power((a, b), (r * r - 1) // d) != (1, 0)
                      for d in divs))
    step, x, sign = mul(gen, gen), (1, 0), []
    for _ in range((r * r - 1) // 2):
        norm = ((1 - x[0]) ** 2 - d * x[1] ** 2) % r
        sign.append(0 if norm == 0 else
                    (1 if pow(norm, (r - 1) // 2, r) == 1 else -1))
        x = mul(x, step)
    assert x == (1, 0)
    return sign


def square_check(r, beta=F(1, 4)):
    sign = square_sign(r)
    n, h, period = len(sign), (r + 1) // 2, r - 1
    shift = period // 2
    I = list(range(0, n, period))
    C = list(range(shift, n, period))
    assert len(I) == len(C) == h and set(I).isdisjoint(C)
    assert sign[0] == 0 and all(sign[j] == 1 for j in range(h, n, h))
    # The exact transform is zero off h Z and h(1+beta*(-1)^k) at kh.
    # The preceding integer sign check therefore proves exact U_+ membership.
    S, T = h * (1 + beta), h * (1 + beta * beta)
    m0 = F(n, r)
    nu2, e_ratio_limit = S * S / n, (1 + beta * beta) / 2
    collision = S * S / T
    phase = 1 + F(1, r) - m0 / T
    pair_deficit = 1 + F(1, r) - m0 / collision
    delta = collision / m0 * (1 + F(1, r)) - 1
    height = S / m0 * (1 + F(1, r))
    W = [F(0) for _ in range(n)]
    for i in I:
        W[i] = F(1)
    for i in C:
        W[i] = beta
    A = [i for i, w in enumerate(W) if 2 * w >= height]
    A_set = set(A)
    err = sum((W[i] - (height if i in A_set else 0)) ** 2
              for i in range(n)) / T
    tail = sum(W[i] ** 2 for i in range(n) if i not in A_set) / T
    assert err <= delta and tail <= delta
    H2m = height * height * len(A) / T
    assert 1 - delta <= H2m <= 1 + 3 * delta

    allowed = [int(x == -1) for x in sign]
    kappa = F(sum(allowed), n)
    assert kappa == F(1, 2)
    omega = F(1 + r, 2 * n)
    eta = (1 - omega / kappa) / (omega + omega * omega / kappa)
    column = [z.real for z in acb.dft(allowed, inverse=True)]
    lam = [z.real for z in acb.dft(sign)]
    M = [1 - z / ball(kappa) for z in column]
    heights = [M[i] * (1 + ball(eta) * (ball(kappa) + column[i]))
               for i in range(n)]
    energy = sum(M[i] * heights[i] * ball(W[i]) ** 2
                 for i in I[1:] + C) / n
    pairing = sum(M[i] * ball(W[i]) for i in I[1:] + C)
    assert abs(pairing - ball(S)) < arb("1e-35")
    assert energy < ball(nu2)
    for i in I[1:] + C:
        assert heights[i] * ball(W[i]) < ball(S)
    calculated_phase = sum(ball(W[i]) ** 2 * (1 - lam[i] / r)
                           for i in I + C) / ball(T)
    assert abs(calculated_phase - ball(phase)) < arb("1e-35")
    autocorr_beta = 2 * beta / (1 + beta * beta)
    autocorr_S = h * (1 + autocorr_beta)
    assert autocorr_S == collision
    mass_margin = nu2 < F(100, 121)  # epsilon=1/10
    return {
        "r": r, "q": r * r, "beta": str(beta),
        "exact_sector": True, "nu_squared_exact": str(nu2),
        "nu_interval": str(ball(nu2).sqrt()),
        "weighted_energy_interval": str(energy),
        "weighted_energy_limit": str(e_ratio_limit),
        "mass_below_1_over_1_1": mass_margin,
        "effective_size_over_m0_exact": str(collision / m0),
        "rooted_squared_weight_phase_deficit_exact": str(phase),
        "pair_deficit_exact": str(pair_deficit),
        "sweep_delta_exact": str(delta),
        "sweep_layer_size": len(A), "sweep_error_exact": str(err),
        "autocorrelation_nu_interval": str(ball(collision) / arb(n).sqrt()),
        "autocorrelation_mass_above_sqrt_n": collision * collision > n,
    }


# Exact arithmetic in Q(sqrt(2)), stored as pairs a+b sqrt(2).
def add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def mul(x, y):
    return (x[0] * y[0] + 2 * x[1] * y[1],
            x[0] * y[1] + x[1] * y[0])


def scalar(x, c):
    return (c * x[0], c * x[1])


def q2ball(x):
    return ball(x[0]) + ball(x[1]) * arb(2).sqrt()


def pair_json(x):
    return [str(v) for v in x]


def prime17_check():
    zero, one = (F(0), F(0)), (F(1), F(0))
    x, y = (F(2), F(-1)), (F(3), F(-2))
    W = [one, zero, zero, x, y, x, zero, zero]
    cos = [one, (F(0), F(1, 2)), zero, (F(0), F(-1, 2)),
           scalar(one, -1), (F(0), F(-1, 2)), zero, (F(0), F(1, 2))]

    def dft_real(v):
        return [sum_q2(mul(v[j], cos[(j * k) % 8]) for j in range(8))
                for k in range(8)]

    residues = {a * a % 17 for a in range(1, 17)}
    sign = [0 if j == 0 else
            (1 if (1 - pow(3, 2 * j, 17)) % 17 in residues else -1)
            for j in range(8)]
    assert sign == [0, 1, -1, -1, 1, -1, -1, 1]
    forbidden = [j for j in range(8) if sign[j] == 1]
    fw = dft_real(W)
    assert all(fw[j] == zero for j in forbidden)
    assert all(q2ball(w) >= 0 and q2ball(w) <= 1 for w in W)
    S = sum_q2(W)
    assert S == (F(8), F(-4))
    assert q2ball(mul(S, S)) / 8 < ball(F(100, 121))
    W2 = [mul(w, w) for w in W]
    f2 = dft_real(W2)
    assert f2[1] == (F(-8), F(6))
    assert f2[4] == (F(6), F(-4))
    indicator = [one if q2ball(w) >= arb(1) / 2 else zero for w in W]
    assert dft_real(indicator)[1] == (F(1), F(-1))
    # Independent interval evaluation of the repair weights and of (8).
    allowed = [int(s == 1) for s in sign]
    kappa = arb(sum(allowed)) / 8
    omega = (1 + arb(17).sqrt()) / 16
    eta = (1 - omega / kappa) / (omega + omega * omega / kappa)
    column = [z.real for z in acb.dft(allowed, inverse=True)]
    M = [1 - a / kappa for a in column]
    heights = [M[i] * (1 + eta * (kappa + column[i])) for i in range(8)]
    wb = [q2ball(w) for w in W]
    sb, tb, m0 = q2ball(S), q2ball(sum_q2(W2)), arb(8) / arb(17).sqrt()
    energy = sum(M[i] * heights[i] * wb[i] ** 2 for i in range(1, 8)) / 8
    assert energy > 0 and energy < sb * sb / 8
    assert abs(sum(M[i] * wb[i] for i in range(1, 8)) - sb) < arb("1e-35")
    collision_ratio = sb * sb / (tb * m0)
    truncations = []
    for C in (2, 3, 4, 8):
        threshold = sb / (C * m0)
        assert arb(C) > collision_ratio and threshold < 1
        assert all(w < threshold or w > threshold for w in wb)
        keep = [w > threshold for w in wb]
        z = [w if retain else arb(0) for w, retain in zip(wb, keep)]
        spectrum = acb.dft(z)
        projected = acb.dft([value if ok else acb(0)
                             for value, ok in zip(spectrum, allowed)], inverse=True)
        z_norm = sum(a * a for a in z)
        leakage = sum(a.real * a.real for a in projected) / z_norm
        bound = collision_ratio / (C - collision_ratio)
        assert leakage < bound
        assert sum(keep) <= C * m0
        tail_bound = collision_ratio / C * tb
        # Membership is certified above.  Avoid subtracting a ball from
        # itself and then taking a generic real power across zero.
        tail_norm = sum(wb[i] * wb[i] for i in range(8) if not keep[i])
        assert tail_norm < tail_bound, (C, str(tail_norm), str(tail_bound))
        truncations.append({"C": C, "support": [i for i in range(8) if keep[i]],
                            "relative_sector_leakage_interval": str(leakage),
                            "bound_interval": str(bound)})
    return {
        "p": 17, "sign": -1, "exact_sector": True,
        "W_Qsqrt2": [pair_json(w) for w in W],
        "S_Qsqrt2": pair_json(S),
        "nu_interval": str(q2ball(S) / arb(8).sqrt()),
        "weighted_energy_interval": str(energy),
        "truncation_checks": truncations,
        "pointwise_square_forbidden_mode_1": pair_json(f2[1]),
        "pointwise_square_forbidden_mode_4": pair_json(f2[4]),
        "half_level_indicator_forbidden_mode_1": ["1", "-1"],
    }


def sum_q2(values):
    out = (F(0), F(0))
    for v in values:
        out = add(out, v)
    return out


if __name__ == "__main__":
    result = {
        "scope": "Exact algebra and 160-bit Arb finite-field checks; no prime asymptotic.",
        "prime_pointwise_power_failure": prime17_check(),
        "square_mixtures": [square_check(r) for r in (7, 11, 13, 31, 97, 389)],
        "square_pure_controls": [square_check(r, F(0)) for r in (7, 31, 97)],
    }
    print(json.dumps(result, indent=2))
