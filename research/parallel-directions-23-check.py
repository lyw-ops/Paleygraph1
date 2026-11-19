"""Exact checks for parallel-directions-23.md, using only the standard library."""

from collections import Counter
from math import isqrt


def check(order, B, sub, mul, inv, chi, d, *, projected=False, ell=None):
    b = len(B)
    units = B - {1}
    neg = lambda x: sub(0, x)
    sum_pairs = lambda histogram: sum(n * (n - 1) for n in histogram.values())

    sigma = d(neg(1))
    numerator = {x: sub(1, x) for x in units}
    denominators = {x: inv(y) for x, y in numerator.items()}
    labels = {x: chi(y) for x, y in numerator.items()}
    E = {1} | {x for x in units if labels[x] != sigma * d(x)}
    e = len(E)

    R = Counter()
    rho = Counter()
    bad_orientation = 0
    for x in units:
        for y in units - {x}:
            u = mul(numerator[x], denominators[y])
            R[u] += 1
            if labels[x] == -1 and labels[y] == 1:
                rho[u] += 1
                bad_orientation += chi(sub(1, u)) != -sigma
    fibers = Counter(mul(sub(x, a), inv(sub(x, 1)))
                     for a in units for x in units - {a})
    assert R == fibers
    assert all(R[u] == R[sub(1, u)] == R[inv(u)] for u in range(2, order))
    nonsquares = [u for u in range(2, order) if chi(u) == -1]
    rich_mass = sum(R[u] for u in nonsquares if R[u] >= 2)
    assert rich_mass <= 8 * e * b
    missing = sum(not R[u] for u in nonsquares)
    mismatch = sum(abs(rho[u] - (chi(sub(1, u)) == -sigma)) for u in nonsquares)
    assert mismatch <= sum(abs(R[u] - 1) for u in nonsquares) + 2 * bad_orientation
    if ell is not None:
        assert e == 1
        assert not missing and not rich_mass and not mismatch
        assert all(R[u] == (u >= ell) for u in range(2, order))

    if projected:
        grid = {(mul(mul(r, sub(1, s)), inv(sub(mul(r, s), 1))),
                 mul(mul(s, sub(1, r)), inv(sub(mul(r, s), 1))))
                for r in units for s in units if mul(r, s) != 1}
        D = {inv(sub(x, 1)) for x in units}
        assert len(grid) == len(D) * (len(D) - 1)
        J = sum(sum_pairs(Counter(sub(y, mul(m, x)) for x, y in grid)) for m in B)
        diagonal = 2 * len(D) * (len(D) - 1) * (len(D) - 2)
        parallel = sum_pairs(Counter(sub(z, w) for z in D for w in D if z != w))
        pinned = 0
        for t in D:
            offsets = {sub(z, t) for z in D - {t}}
            h = Counter(mul(z, inv(w)) for w in offsets for z in offsets - {w})
            pinned += sum_pairs(h)
            if ell is not None:
                assert h == {u: ell - 1 for u in range(2, ell)}
        assert J == diagonal + parallel + pinned
        if ell is not None:
            assert parallel == ell * (ell - 1)**2
            assert J == ell**2 * (ell - 1) * (ell - 2) + parallel
        return J, parallel, missing, len(nonsquares), rich_mass, e
    return None, None, missing, len(nonsquares), rich_mass, e


def prime_case(p, b):
    assert all(p % i for i in range(2, isqrt(p) + 1)) and (p - 1) % (2 * b) == 0
    B = {x for x in range(1, p) if pow(x, b, p) == 1}
    assert len(B) == b
    squares = {x * x % p for x in range(1, (p + 1) // 2)}
    return check(p, B, lambda x, y: (x - y) % p, lambda x, y: x * y % p,
                 lambda x: pow(x, -1, p), lambda x: (1 if x in squares else -1) if x else 0,
                 lambda x: 1 if pow(x, b // 2, p) == 1 else -1, projected=b <= 72)


def square_case(ell):
    nr = next(x for x in range(2, ell) if pow(x, (ell - 1) // 2, ell) != 1)

    def sub(x, y):
        return (x % ell - y % ell) % ell + ell * ((x // ell - y // ell) % ell)

    def mul(x, y):
        a, b = x % ell, x // ell
        c, d = y % ell, y // ell
        return (a * c + nr * b * d) % ell + ell * ((a * d + b * c) % ell)

    def norm(x):
        return ((x % ell)**2 - nr * (x // ell)**2) % ell

    def inv(x):
        return mul(pow(norm(x), -1, ell), x % ell + ell * (-(x // ell) % ell))

    def power(x, k):
        out = 1
        while k:
            if k % 2:
                out = mul(out, x)
            x, k = mul(x, x), k // 2
        return out

    B = {x for x in range(1, ell**2) if norm(x) == 1}
    assert len(B) == ell + 1
    return check(ell**2, B, sub, mul, inv,
                 lambda x: (1 if pow(norm(x), (ell - 1) // 2, ell) == 1 else -1) if x else 0,
                 lambda x: 1 if power(x, (ell + 1) // 2) == 1 else -1, projected=True, ell=ell)


if __name__ == "__main__":
    for p, b in ((97, 12), (1153, 32), (4177, 72), (10193, 98), (40801, 200), (252001, 500)):
        J, parallel, missing, n, rich, e = prime_case(p, b)
        print(f"p={p:6d} b={b:3d}: nonsquare vacancies {missing:6d}/{n:<6d} "
              f"({missing/n:.3%}), rich mass={rich}, E={e}, J_B={J}, parallel={parallel}")
    for ell in (7, 11, 13, 31):
        J, parallel, missing, n, rich, e = square_case(ell)
        print(f"ell={ell:2d}: nonsquare vacancies {missing}/{n}, rich mass={rich}, "
              f"E={e}, J_B={J}, parallel={parallel}")
