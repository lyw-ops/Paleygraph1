"""Exact checks for the round-32 epsilon-factor determinant calculation.

Run: .venv/bin/python -B research/astra-prime-phase-32-check.py
Requires python-flint. Writes JSONL to stdout only. No floating arithmetic.
The finite checks audit normalizations; the uniform proof is in the note.
"""

import argparse
import json
from functools import lru_cache

from flint import fmpz_poly, fq_default_ctx


def factors(n):
    ans, d = [], 2
    while d * d <= n:
        if n % d == 0:
            ans.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        ans.append(n)
    return ans


def key(x):
    return tuple(int(t) for t in x.to_list())


def cycconv(a, b):
    n = len(a)
    c = fmpz_poly(a) * fmpz_poly(b)
    return [int(c[i] + c[i + n]) for i in range(n)]


class Field:
    def __init__(self, p, d):
        self.p, self.d, self.q = p, d, p**d
        self.ctx = fq_default_ctx(p, d, "x")
        n = self.q - 1
        fs = factors(n)
        for number in range(2, self.q):
            digits, z = [], number
            while z:
                digits.append(z % p)
                z //= p
            g = self.ctx(digits)
            if all(not (g ** (n // t)).is_one() for t in fs):
                break
        else:
            raise AssertionError("primitive element not found")
        self.g = g
        self.cycle, z = [], self.ctx.one()
        for _ in range(n):
            self.cycle.append(z)
            z *= g
        self.index = {key(z): i for i, z in enumerate(self.cycle)}
        assert len(self.index) == n and z.is_one()

    def chi(self, z):
        return 0 if z.is_zero() else 1 if z.is_square() else -1

    def embed(self, base, z):
        if base.d == 1:
            return self.ctx(int(z.to_list()[0]))
        modulus = [int(c) for c in base.ctx.modulus().coeffs()]
        subgroup_generator = self.g ** ((self.q - 1) // (base.q - 1))
        root = self.ctx.one()
        for _ in range(base.q - 1):
            val = self.ctx.zero()
            for c in reversed(modulus):
                val = val * root + c
            if val.is_zero():
                break
            root *= subgroup_generator
        else:
            raise AssertionError("base-field polynomial has no embedded root")
        ans = self.ctx.zero()
        for c in reversed(z.to_list()):
            ans = ans * root + int(c)
        return ans


@lru_cache(None)
def data(p, d):
    f = Field(p, d)
    ell = [f.chi(1 - a) for a in f.cycle]
    B = cycconv(cycconv(ell, ell), ell)
    assert sum(ell) == sum(B) == -1
    r = [0 if a.is_one() else ell[i] * B[f.index[key(1 - a)]]
         for i, a in enumerate(f.cycle)]
    if f.q <= 49:
        def direct(a, b):
            n = len(a)
            return [sum(a[j] * b[(i-j) % n] for j in range(n))
                    for i in range(n)]
        assert B == direct(direct(ell, ell), ell)
    return f, ell, B, r


def reduce_at_character(a, k, modulus, n):
    b = [0] * n
    for i, x in enumerate(a):
        b[(i*k) % n] += x
    return fmpz_poly(b) % modulus


def check_base(p, d):
    base, ell, B, r = data(p, d)
    q, n = base.q, base.q - 1
    eps = base.chi(base.ctx(-1))
    _, _, B_square, _ = data(p, 2*d)
    special_det = (B[0]**2-B_square[0])//2
    assert B[0]**2-B_square[0] == 2*eps*q**2
    assert sum(r) == -eps-B[0]
    orbit_audit = None
    if eps == 1:
        assert (B[0]-(q-3)) % 4 == 0
        domain = {(i,j) for i in range(1,n) for j in range(1,n)
                  if (i+j) % n != 0}
        sizes = {2: 0, 4: 0}
        orbit_sum = 0
        while domain:
            i,j = min(domain)
            orbit = {(i,j), (j,i), ((-i)%n,(-j)%n),
                     ((-j)%n,(-i)%n)}
            assert len(orbit) in (2,4)
            weights = {ell[a]*ell[b]*ell[(-a-b)%n] for a,b in orbit}
            assert len(weights) == 1 and next(iter(weights)) in (-1,1)
            orbit_sum += len(orbit)*next(iter(weights))
            sizes[len(orbit)] += 1
            domain -= orbit
        assert orbit_sum == B[0] and 2*sizes[2] == q-3
        orbit_audit = {"size_2_orbits": sizes[2], "size_4_orbits": sizes[4],
                       "sum": orbit_sum, "mod_4": B[0] % 4}
    traces = []
    extension_metadata = []
    for e in (1, 2, 3):
        f, _, _, r_ext = data(p, d*e)
        if e == 1:
            norm_log = 1
        else:
            embedded_g = f.embed(base, base.g)
            norm_g = f.g ** ((f.q - 1)//n)
            z = f.ctx.one()
            for norm_log in range(n):
                if z == norm_g:
                    break
                z *= embedded_g
            else:
                raise AssertionError("norm not in embedded base field")
        coeffs = [0] * n
        for i, value in enumerate(r_ext):
            # Trace H_c^1 = minus the character-sum trace.
            coeffs[(i*norm_log) % n] -= value
        traces.append(coeffs)
        extension_metadata.append({"e": e, "field_order": f.q,
                                   "norm_generator_log": norm_log,
                                   "modulus": str(f.ctx.modulus())})
    phi = fmpz_poly.cyclotomic(n)
    records = []
    for k in range(1, n):
        if k == n//2:
            continue
        t1, t2, t3 = [reduce_at_character(t, k, phi, n) for t in traces]
        six_det = (t1**3 - 3*t1*t2 + 2*t3) % phi
        assert all(int(c) % 6 == 0 for c in six_det.coeffs())
        det = fmpz_poly([int(c)//6 for c in six_det.coeffs()])
        jac = [0] * n
        original_jac = [0] * n
        for i, value in enumerate(ell):
            jac[(k*i) % n] += (-1 if i % 2 else 1) * value
            original_jac[(k*i) % n] += value
        jac = fmpz_poly(jac) % phi
        original_jac = fmpz_poly(original_jac) % phi
        expected = (-eps * q**4 * jac) % phi
        assert det == expected
        assert (original_jac * jac) % phi == fmpz_poly([eps*q])
        # Equivalent normalized identity, with no square roots:
        # det(H_c^1) * J(alpha,chi) = -q^5.
        assert (det * original_jac) % phi == fmpz_poly([-q**5])
        records.append({"character_exponent": k,
                        "determinant_coefficients": [int(c) for c in det.coeffs()],
                        "jacobi_coefficients": [int(c) for c in jac.coeffs()]})
    print(json.dumps({"kind": "exact_newton_mellin_determinant", "p": p,
                      "degree": d, "q": q, "chi_minus_one": eps,
                      "base_generator": key(base.g),
                      "extension_fields": extension_metadata,
                      "cyclotomic_modulus": [int(c) for c in phi.coeffs()],
                      "good_characters_checked": len(records),
                      "identity": "det(Hc1)*J(alpha,chi)=-q^5",
                      "sum_B": sum(B),
                      "special_stalk": {"B_q_1": B[0],
                                        "B_q_squared_1": B_square[0],
                                        "det": special_det,
                                        "sum_r": sum(r),
                                        "orbit_audit": orbit_audit},
                      "records": records}), flush=True)


def check_positional_determinants(p, d):
    """Check det(B_t)=q^3 chi(1-t) by traces over three extensions."""
    base, _, B, _ = data(p, d)
    q = base.q
    checked = []
    for t in base.cycle:
        if t.is_one():
            continue
        tt = []
        for e in (1, 2, 3):
            f, _, Be, _ = data(p, d*e)
            te = t if e == 1 else f.embed(base, t)
            tt.append(Be[f.index[key(te)]])
        s1, s2, s3 = tt
        numerator = s1**3 - 3*s1*s2 + 2*s3
        assert numerator % 6 == 0
        determinant = numerator//6
        assert determinant == q**3 * base.chi(1-t)
        checked.append({"t": key(t), "traces": tt, "det": determinant})
    print(json.dumps({"kind": "exact_positional_determinant", "q": q,
                      "identity": "det(B_t)=q^3*chi(1-t)",
                      "records": checked}), flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--quick", action="store_true")
    args = ap.parse_args()
    bases = [(5,1), (7,1)] if args.quick else [
        (3,1), (5,1), (7,1), (3,2), (11,1), (13,1), (5,2), (3,3)]
    for p, d in bases:
        check_base(p, d)
        check_positional_determinants(p, d)
    print(json.dumps({"kind": "all_checks_passed", "bases": bases,
                      "arithmetic": "exact integers and cyclotomic quotients",
                      "scope": "finite normalization checks, not the uniform proof"}))


if __name__ == "__main__":
    main()
