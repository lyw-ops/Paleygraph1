"""Exact prime reductions for complex-twisted cosets of orders 3, 4, 6."""

import json


def legendre(value, prime):
    power = pow(value % prime, (prime - 1) // 2, prime)
    return -1 if power == prime - 1 else power


def transform(values, root, prime):
    return [
        sum(value * pow(root, t*j, prime) for j, value in enumerate(values)) % prime
        for t in range(len(values))
    ]


def check(prime, generator, b, k, e):
    m = (prime - 1) // (2*b)
    period = 2*k*m
    assert b % k == 0 and len({pow(generator, j, prime) for j in range(prime-1)}) == prime-1
    xi = pow(generator, b//k, prime)
    zeta = pow(xi, 2*m, prime)
    subgroup = [pow(generator, 2*m*j, prime) for j in range(b)]
    lower = list(range(e, k*m, k))
    coset_terms = matched_poles = 0

    def evaluate(root):
        return [
            sum(pow(root, e*l, prime) * legendre(1 - pow(generator, j, prime)*x, prime)
                for l, x in enumerate(subgroup)) % prime
            for j in range(period)
        ]

    f = evaluate(zeta)
    conjugate = evaluate(pow(zeta, -1, prime))
    assert all(f[(j+2*m) % period] == pow(zeta, -e, prime)*f[j] % prime
               and f[-j % period] == (-1)**j * conjugate[j] % prime for j in range(period))
    assert sum(f[j]*conjugate[j] for j in range(2*m)) % prime == 0
    full = transform(f, xi, prime)
    for t in range(period):
        if t % k != e:
            assert full[t] == 0
            continue
        jacobi = sum(pow(y, (b//k)*t, prime) * legendre(1-y, prime)
                     for y in range(1, prime)) % prime
        assert full[t] == k*jacobi % prime
        if t < k*m:
            assert jacobi == 0

    for center in (0, m):
        u = [f[(center + 2*h) % period] for h in range(k*m)]
        omega = (-1)**center * pow(zeta, -e*(center//m), prime) % prime
        assert f[center] == omega*conjugate[center] % prime
        transformed = transform(u, xi*xi % prime, prime)
        points = [
            (j, pow(xi, center - j, prime))
            for j in range(1-center % 2, period, 2)
        ]
        for j, z in points:
            assert pow(z, k*m, prime) == prime-1
            rhs = sum(transformed[t]*pow(z, t, prime) for t in lower)
            assert rhs % prime == -k*m*f[j] % prime
            peak = sum(k*f[center]*pow(z, t, prime) for t in lower)
            assert peak % prime == (
                2*k*f[center]*pow(z, e, prime)*pow(1-pow(z, k, prime), -1, prime)
            ) % prime

        for size in (h for h in range(1, k*m+1) if k*m % h == 0):
            for c in range(k*m // size):
                period_step = k*m // size
                support = [
                    (t, sum(pow(xi, 2*t*j, prime) for j in range(c, k*m, period_step)) % prime)
                    for t in lower
                ]
                for _, z in points:
                    total = sum(coeff*pow(z, t, prime) for t, coeff in support) % prime
                    if all(t % size for t in lower):
                        assert total == 0
                    else:
                        first = next(t//size for t in lower if t % size == 0)
                        w = pow(pow(xi, 2*c, prime)*z, size, prime)
                        assert total == (
                            2*size*pow(w, first, prime)*pow(1-pow(w, k, prime), -1, prime)
                        ) % prime
                    coset_terms += 1
                if all(t % size for t in lower):
                    continue
                w0 = pow(xi, 2*c*size, prime)
                if pow(w0, k, prime) == 1:
                    eta = pow(w0, first, prime)
                    for weight, dual in ((1, 1), (zeta, pow(zeta, -1, prime))):
                        pair = weight*eta+omega*dual*pow(eta, -1, prime)
                        mirror = dual*pow(eta, -1, prime)+pow(omega, -1, prime)*weight*eta
                        assert (pair-omega*mirror) % prime == 0
                    matched_poles += 1

    print(json.dumps(dict(kind="exact_lattice_twist_reduction", prime=prime, order=k,
                          twist=e, b=b, m=m, coset_terms=coset_terms,
                          reflected_pole_pairs=matched_poles), sort_keys=True))


if __name__ == "__main__":
    for parameters in ((97, 5, 12), (241, 7, 24)):
        for k, e in ((3, 1), (4, 3), (6, 5)):
            check(*parameters, k, e)
