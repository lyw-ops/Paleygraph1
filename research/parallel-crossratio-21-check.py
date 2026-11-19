"""Exact finite checks for parallel-crossratio-21.md; Python standard library only."""

from collections import Counter
from math import isqrt, sqrt
from random import Random


def ratio_hist(p, values):
    inverse = [pow(y, -1, p) for y in values]
    out = [0] * p
    for inv in inverse:
        for x in values:
            out[x * inv % p] += 1
    return out


def cell_moments(p, B):
    coset = {}
    for x in range(1, p):
        if x not in coset:
            coset.update((x * y % p, x) for y in B)
    cells = Counter()
    for x, label in coset.items():
        x_inv = pow(x, -1, p)
        for s in B:
            lam = ((s - 1) * x + s) * x_inv * x_inv % p
            if lam not in (0, 1):
                cells[lam, label] += 1
    b = len(B)
    second = sum(n * n for n in cells.values())
    assert second <= b**3 + 2 * b * (p - 1)
    return coset, cells, second


def dickson_check(p, B, rr):
    b = len(B)
    S = [x for x in range(1, p) if pow(x, 2 * b, p) == 1]
    assert len(S) == 2 * b
    out = [0] * p
    for D in (B, set(S) - B):
        delta = {x: (x - pow(x, -1, p)) % p for x in D}
        for v, dv in delta.items():
            if not dv:
                continue  # x=y
            inv_v = pow(v, -1, p)
            inv_dv = pow(dv, -1, p)
            for w, dw in delta.items():
                if w * v % p in (1, p - 1) or w * inv_v % p in (1, p - 1):
                    continue
                h = dw * inv_dv % p
                assert h not in (1, p - 1)
                u = (h - 1) * pow(h + 1, -1, p) % p
                out[u] += 1
    assert all(out[u] == 2 * rr[u] for u in range(2, p))


def check_prime(p, b):
    assert all(p % d for d in range(2, isqrt(p) + 1)) and (p - 1) % (2 * b) == 0
    B = {x for x in range(1, p) if pow(x, b, p) == 1}
    assert len(B) == b
    reciprocals = {x: pow(x - 1, -1, p) for x in B if x != 1}
    all_anchors = sorted(B - {1, p - 1})
    rng = Random(21)
    anchors = [p - 1] + (all_anchors if b < 100 else rng.sample(all_anchors, 40))
    if b <= 72:
        coset, cells, second = cell_moments(p, B)
    total = [0] * p
    individual_max = 0
    for a in anchors:
        X = [(x - a) * inv % p for x, inv in reciprocals.items() if x != a]
        rr = ratio_hist(p, X)
        t = reciprocals[a]
        dd = ratio_hist(p, [(z - t) % p for x, z in reciprocals.items() if x != a])
        assert rr == dd and sum(rr[2:]) == (b - 2) * (b - 3)
        if a == p - 1:
            assert rr[p - 1] == b - 2
            assert all((-x) % p in X and pow(x, -1, p) in X for x in X)
            dickson_check(p, B, rr)
        individual_max = max(individual_max, *(rr[u] for u in range(2, p)
                                                if (a, u) != (p - 1, p - 1)))
        for u in (range(2, p) if b <= 12 else rng.sample(range(2, p), 10)):
            F, G, D = a * (1 - u) % p, (u - 1) % p, (1 - u * a) % p
            A = (u - a) % p
            count = 0
            for x in B:
                denom = (G * x + D) % p
                if denom and (A * x + F) * pow(denom, -1, p) % p in B:
                    count += 1
            assert count == rr[u] + 2
            if b <= 72 and A and D:
                alpha = G * pow(D, -1, p) % p
                lam = A * D * pow(F * G, -1, p) % p
                assert cells[lam, coset[alpha]] == count
        for u in range(2, p):
            total[u] += rr[u]

    avg = [r / len(anchors) for r in total[2:]]
    second_label = f"{second / b**3:.3f}" if b <= 72 else "-"
    print(f"| {p} | {b} | {len(anchors)} | {individual_max} | "
          f"{sum(r**1.5 for r in avg) / p:.3f} | "
          f"{sum(r*r for r in avg) / p:.3f} | {second_label} |")


def check_square(ell):
    n = next(a for a in range(1, ell) if pow(a, (ell - 1) // 2, ell) == ell - 1)

    def add(x, y):
        return ((x % ell + y % ell) % ell
                + ell * ((x // ell + y // ell) % ell))

    def neg(x):
        return (-x % ell) + ell * (-(x // ell) % ell)

    def mul(x, y):
        a, b = x % ell, x // ell
        c, d = y % ell, y // ell
        return (a * c + n * b * d) % ell + ell * ((a * d + b * c) % ell)

    def norm(x):
        return ((x % ell)**2 - n * (x // ell)**2) % ell

    def inv(x):
        return mul(pow(norm(x), -1, ell), x % ell + ell * (-(x // ell) % ell))

    def power(x, k):
        z = 1
        while k:
            if k % 2:
                z = mul(z, x)
            x = mul(x, x)
            k //= 2
        return z

    b = ell + 1
    B = {x for x in range(1, ell**2) if norm(x) == 1}
    assert len(B) == b
    sigma = (-1)**(b // 2)
    for x in B - {1}:
        chi = pow(norm(add(1, neg(x))), (ell - 1) // 2, ell)
        assert chi == sigma * power(x, b // 2) % ell
    for a in B - {1}:
        X = {mul(add(x, neg(a)), inv(add(x, neg(1)))) for x in B - {1, a}}
        v = next(iter(X))
        assert X == {mul(v, c) for c in range(1, ell)}
        rr = Counter(mul(x, inv(y)) for x in X for y in X)
        assert rr == {c: ell - 1 for c in range(1, ell)}
    moment = (ell - 2) * (ell - 1) * sqrt(ell - 1) / ell**2
    print(f"ell={ell}: exact twist (sign {sigma:+d}), all {ell} anchors, moment={moment:.3f}")


if __name__ == "__main__":
    for p, b in ((97, 12), (1153, 32), (4177, 72), (10193, 98),
                 (40801, 200), (252001, 500)):
        check_prime(p, b)
    for ell in (7, 11, 13, 31):
        check_square(ell)
