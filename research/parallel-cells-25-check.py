"""Exact cell and two-tail checks for parallel-cells-25.md.

Only files with the prefix parallel-cells-25 are written.  Standard library
only; the finite checks do not prove a uniform prime-field estimate.
"""

from collections import Counter
from fractions import Fraction
import json
from pathlib import Path


class Field:
    def __init__(self, p, square=False):
        assert p > 2 and all(p % d for d in range(2, int(p**0.5) + 1))
        self.p, self.square = p, square
        self.q = p * p if square else p
        self.nr = next(x for x in range(2, p) if pow(x, (p - 1) // 2, p) != 1)
        self.inverse = [0] + [self.power(x, self.q - 2) for x in range(1, self.q)]
        self.character = [0] + [1 if self.power(x, (self.q - 1) // 2) == 1 else -1
                                for x in range(1, self.q)]

    def add(self, x, y):
        p = self.p
        return ((x % p + y % p) % p + p * ((x // p + y // p) % p)
                if self.square else (x + y) % p)

    def neg(self, x):
        return self.sub(0, x)

    def sub(self, x, y):
        p = self.p
        return ((x % p - y % p) % p + p * ((x // p - y // p) % p)
                if self.square else (x - y) % p)

    def mul(self, x, y):
        p = self.p
        if not self.square:
            return x * y % p
        a, b, c, d = x % p, x // p, y % p, y // p
        return (a * c + self.nr * b * d) % p + p * ((a * d + b * c) % p)

    def power(self, x, n):
        out = 1
        while n:
            if n & 1:
                out = self.mul(out, x)
            x, n = self.mul(x, x), n // 2
        return out

    def div(self, x, y):
        assert y
        return self.mul(x, self.inverse[y])


def factorial(n, j):
    out = 1
    for i in range(j):
        out *= n - i
    return out


def rational(value):
    return [value.numerator, value.denominator]


def check(p, b=None, square=False, direct_anchors=False):
    f = Field(p, square)
    q = f.q
    b = p + 1 if square else b
    assert b is not None and b % 2 == 0 and (q - 1) % (2 * b) == 0
    B = {x for x in range(1, q) if f.power(x, b) == 1}
    assert len(B) == b and f.neg(1) in B
    d = {x: 1 if f.power(x, b // 2) == 1 else -1 for x in B}
    coordinates = {}
    for x in range(1, q):
        if x not in coordinates:
            coordinates.update({f.mul(x, y): (x, d[y]) for y in B})

    # Affine cells are not the product cells below.
    affine = {}
    for x in range(1, q):
        y = f.sub(1, x)
        if not y or f.character[x] * f.character[y] != -1:
            continue
        cx, dx = coordinates[x]
        cy, dy = coordinates[y]
        n, ell = affine.get((cx, cy), (0, 0))
        affine[cx, cy] = n + 1, ell + dx * dy
    fm = {j: sum(factorial(n, j) for n, _ in affine.values()) for j in range(1, 5)}
    vacancies = sum(n == 1 for n, _ in affine.values())
    excess = sum(n * max(n - 2, 0) for n, _ in affine.values())
    twist = sum(d[x] * f.character[f.sub(1, x)] for x in B - {1})
    untwisted = sum(f.character[f.sub(1, x)] for x in B - {1})
    assert fm[1] == (q - 1) // 2
    assert fm[2] == ((b - 1)**2 - untwisted**2) // 2
    assert vacancies == fm[1] - fm[2] + excess
    assert q == twist**2 + 2 * sum(ell**2 for _, ell in affine.values())
    # Independent affine-ratio construction checks all four moments,
    # including the zero-count ratios that do not occur in a Counter.
    Y = {f.sub(1, x) for x in B - {1}}
    affine_ratios = Counter(f.div(x, y) for x in Y for y in Y if x != y)
    nonsquares = [u for u in range(1, q) if f.character[u] == -1]
    assert vacancies == sum(affine_ratios[u] == 0 for u in nonsquares)
    for j in range(1, 5):
        assert fm[j] == sum(factorial(affine_ratios[u], j - 1) for u in nonsquares)
    denominator = fm[4] + 2 * fm[3]
    certificate = Fraction(fm[3]**2, denominator) if denominator else Fraction(0)
    assert excess >= certificate
    assert vacancies >= fm[1] - fm[2] + certificate
    if square:
        assert all(n == 2 and ell == 0 for n, ell in affine.values())
        assert fm[3] == fm[4] == vacancies == 0

    # Enumerate N_C(gamma), with gamma=(1+1/x)(1+1/z), x,z in C.
    product, fixed = Counter(), Counter()
    shifted_inverse = [f.add(1, f.inverse[x]) for x in range(q)]
    for x in range(1, q):
        cx = coordinates[x][0]
        for a in B:
            z = f.mul(a, x)
            gamma = f.mul(shifted_inverse[x], shifted_inverse[z])
            if gamma in (0, 1):
                continue
            cell = gamma, cx
            product[cell] += 1
            fixed[cell] += x == z
    assert max(fixed.values(), default=0) <= 2
    joint = Counter()
    for cell, n in product.items():
        if n - fixed[cell]:
            assert n >= 2
            joint[n - 2] += n - fixed[cell]

    if direct_anchors:
        direct = Counter()
        for a in B - {1}:
            X = {f.div(f.sub(x, a), f.sub(x, 1)) for x in B - {1, a}}
            assert len(X) == b - 2
            raw = Counter(f.div(x, y) for x in X for y in X)
            for u in range(2, q):
                if u == a or f.mul(u, a) == 1:
                    continue
                direct[raw[u]] += 1
        # Cells only encode pairs with a positive or zero overlap for which
        # a first solution exists.  Missing product cells encode r=0 as well.
        assert {r: n for r, n in direct.items() if r} == {
            r: n for r, n in joint.items() if r}
    denominator_joint = (b - 1) * q
    assert sum(n*n for n in product.values()) <= b**3 + 2*b*(q-1)
    first = sum(r * n for r, n in joint.items())
    tails = []
    for threshold in (1, 2, 4, 8, 16, 32):
        low = sum(r * r * n for r, n in joint.items() if r <= threshold)
        high = sum(r * n for r, n in joint.items() if r > threshold)
        assert first == sum(r * n for r, n in joint.items() if r <= threshold) + high
        tails.append(dict(threshold=threshold,
                          truncated_second=rational(Fraction(low, denominator_joint)),
                          tail_first=rational(Fraction(high, denominator_joint))))
    if square:
        positive = {r: n for r, n in joint.items() if r}
        assert positive == {p - 1: p * (p - 2) - 1}
        assert Fraction(first, denominator_joint) == Fraction(
            p**3 - 3 * p**2 + p + 1, p**3)
    return dict(field_order=q, characteristic=p, square=square, b=b,
                affine_factorial_moments=fm, twist_sum=twist,
                untwisted_sum=untwisted, vacancies=vacancies, excess=excess,
                moment_excess_lower=rational(certificate),
                product_cell_count=len(product),
                product_second_moment=sum(n*n for n in product.values()),
                product_third_moment=sum(n**3 for n in product.values()),
                product_max=max(product.values(), default=0),
                joint_positive_count=sum(n for r, n in joint.items() if r),
                joint_first=rational(Fraction(first, denominator_joint)),
                direct_anchors_checked=direct_anchors, tails=tails)


def check_cap_split():
    """Independent numerical Fourier check of the raw Cauchy/tail split.

    No asymptotic or rounding certificate is inferred from these floats.
    """
    import cmath
    import math
    p, b = 97, 12
    f = Field(p)
    generator = next(g for g in range(2, p)
                     if len({pow(g, j, p) for j in range(p - 1)}) == p - 1)
    n = (p - 1) // 2
    q_generator = generator**2 % p
    Q = [pow(q_generator, j, p) for j in range(n)]
    B = {x for x in range(1, p) if pow(x, b, p) == 1}
    joint_q = []
    for a in B - {1}:
        X = {(x - a) * pow(x - 1, -1, p) % p for x in B - {1, a}}
        R = Counter(x * pow(y, -1, p) % p for x in X for y in X)
        joint_q.extend((u, R[u]) for u in Q if u != 1 and u != a and u*a % p != 1)
    max_excess = 0.0
    comparisons = 0
    for order in (1, 4, 16, 64):
        k = [sum(f.character[(1 - x) % p] * cmath.exp(2j*math.pi*t*j/n)
                 for j, x in enumerate(Q)).real / math.sqrt(p) for t in range(n)]
        assert max(abs(x) for x in k) <= 1 + 1e-12
        for sign in (-1, 1):
            multipliers = [((1 + sign*x)/2)**order for x in k]
            coefficients = {u: sum(multipliers[t] * cmath.exp(-2j*math.pi*t*j/n)
                                   for t in range(n))/n for j, u in enumerate(Q)}
            v = {u: math.sqrt(p)*abs(coefficients[u]) for u in Q if u != 1}
            l2 = math.sqrt(sum(z*z for z in v.values())/p)
            linfty = max(v.values())
            for threshold in (1, 2, 4, 8):
                low = sum(r*r for u, r in joint_q if r <= threshold)/((b-1)*p)
                high = sum(r for u, r in joint_q if r > threshold)/((b-1)*p)
                pairing = sum(v[u]*r for u, r in joint_q)/((b-1)*p)
                upper = l2*math.sqrt(low) + linfty*high
                max_excess = max(max_excess, pairing-upper)
                assert pairing <= upper + 1e-12
                comparisons += 1
    return dict(comparisons=comparisons, max_positive_excess=max_excess,
                status="floating-point algebra check, not an interval certificate")


def check_jacobi_convolution():
    """Check (8) exactly in Z[i], without floating-point roots of unity."""
    p, b, k, generator = 17, 4, 4, 3
    logarithm = {pow(generator, j, p): j for j in range(p - 1)}
    gaussian_units = ((1, 0), (0, 1), (-1, 0), (0, -1))

    def mul(x, y):
        a, c = x
        b, d = y
        return a*b - c*d, a*d + c*b

    def add(x, y):
        return x[0] + y[0], x[1] + y[1]

    jacobi = {}
    for i in range(k):
        for j in range(k):
            value = (0, 0)
            for x in range(2, p):
                exponent = (i*logarithm[x] + j*logarithm[(1-x) % p]) % 4
                value = add(value, gaussian_units[exponent])
            jacobi[i, j] = value
    assert jacobi[0, 0] == (p-2, 0)
    assert jacobi[2, 2] == (-1, 0)
    cells = Counter((logarithm[x] % k, logarithm[(1-x) % p] % k)
                    for x in range(2, p)
                    if (logarithm[x] + logarithm[(1-x) % p]) % 2)
    power = {(0, 0): (1, 0)}
    rows = []
    for moment in range(1, 5):
        out = {}
        for (i, j), a in power.items():
            for (u, v), c in jacobi.items():
                key = (i+u) % k, (j+v) % k
                out[key] = add(out.get(key, (0, 0)), mul(a, c))
        power = out
        first, second = power[0, 0], power[k//2, k//2]
        numerator = first[0] - second[0]
        denominator = 2 * k**(2*moment-2)
        assert first[1] == second[1] == 0 and numerator % denominator == 0
        value = numerator // denominator
        assert value == sum(n**moment for n in cells.values())
        rows.append(dict(moment=moment, nonsquare_cell_power_sum=value))
    return dict(p=p, b=b, coefficient_ring="Z[i]", exact_checks=rows)


if __name__ == "__main__":
    rows = [check(p, b, direct_anchors=True) for p, b in
            ((97, 12), (197, 14), (401, 20), (1153, 32), (2113, 48),
             (4177, 72), (10193, 98), (13217, 112))]
    rows += [check(p, square=True, direct_anchors=True) for p in (7, 11, 13, 31)]
    result = dict(exact_cell_checks=rows,
                  exact_jacobi_convolution=check_jacobi_convolution(),
                  cap_split=check_cap_split())
    path = Path(__file__).with_name("parallel-cells-25-certified.json")
    path.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
