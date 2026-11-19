"""Certify the first one-sided switch on the larger theta side at p=809."""

from flint import arb, arb_mat, ctx
import numpy as np

from endpoint_norm import even_coordinates, minimum_endpoint
from theta import optimize, paley_sign


def certify():
    p = 809
    side = -1
    release_index = 4
    exit_index = 69
    sign = paley_sign(p)
    n = len(sign)
    reps, sizes = even_coordinates(n)
    double = {s: optimize(sign, s)[1][reps] / np.sqrt(n) for s in (1, -1)}
    supports = {
        s: set(np.flatnonzero(minimum_endpoint(sign, s, double[-s], sizes)[0] > 1e-8))
        for s in (1, -1)
    }
    if supports[1] & supports[-1] != {0} or supports[1] | supports[-1] != set(reps):
        raise RuntimeError("candidate supports do not give strict complementarity")

    ctx.prec = 192
    weights = [arb(int(m)).sqrt() for m in sizes]
    root_n = arb(n).sqrt()
    phases = [(2 * arb.pi() * k / n).cos() for k in range(n)]
    constant = arb_mat([[weight / root_n] for weight in weights])
    endpoints = {}
    for s in (1, -1):
        positions = [int(k) for k in reps if sign[k] == s]
        outside = sorted(set(reps) - supports[s])
        rows = [[weights[i] * weights[k] * phases[int(i * k) % n] / root_n for k in positions] for i in reps]
        basis = arb_mat(rows)
        restricted = arb_mat([rows[i] for i in outside])
        coefficients = restricted.solve(arb_mat([[-constant[i, 0]] for i in outside]))
        endpoint = constant + basis * coefficients
        assert all(endpoint[i, 0] > 0 for i in supports[s])
        for i in outside:
            endpoint[i, 0] = arb(0)
        endpoints[s] = endpoint
        if s == side:
            x, source, source_off, off = endpoint, basis, restricted, outside

    y = endpoints[-side]
    pivot = off.index(release_index)
    losses = [x[0, 0] * y[i, 0] for i in off]
    benefit = source_off.transpose().solve(-(source.transpose() * x))
    assert benefit[pivot, 0] > 0
    u_star = benefit[pivot, 0] / losses[pivot]
    assert all(u_star * cost > benefit[k, 0] for k, cost in enumerate(losses) if k != pivot)
    width = 1 / (2 * u_star)

    tangent = source * source_off.solve(arb_mat([[int(k == pivot)] for k in range(len(off))]))
    direction = tangent * (losses[pivot] / (tangent.transpose() * tangent)[0, 0])
    products = source_off.transpose().solve(source.transpose() * direction)
    slope = -direction[0, 0]

    assert exit_index in supports[side] and direction[exit_index, 0] < 0
    step = -x[exit_index, 0] / direction[exit_index, 0]
    assert u_star * arb(61) / 1000 < step < u_star * arb(62) / 1000
    assert all(x[i, 0] + step * direction[i, 0] > 0 for i in supports[side] if i != exit_index)
    assert all(
        (u_star - step) * cost - benefit[k, 0] + step * products[k, 0] > 0
        for k, cost in enumerate(losses) if k != pivot
    )
    assert x[0, 0] > 1
    assert arb(21) / 10**6 < width * root_n < arb(22) / 10**6
    assert slope * step < arb(11) / 10**9
    print("Scaled tangent width:", width * root_n)
    print("Squared norm:", (x.transpose() * x)[0, 0])
    print("Inverse-penalty mark slope:", slope)
    print("First-piece inverse-penalty length relative to the threshold:", step / u_star)
    print("Mark loss at first-piece end:", slope * step)


if __name__ == "__main__":
    certify()
