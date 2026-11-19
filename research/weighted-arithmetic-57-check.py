"""Exact tests for the next feedback's boundary table and Mellin determinants."""
from itertools import combinations_with_replacement
import json
from math import factorial, gcd
from pathlib import Path
import runpy

from flint import fmpz_poly

prior = runpy.run_path(str(Path(__file__).with_name("rank-four-arithmetic-56-check.py")))
data = prior["data"]
cycconv = prior["cycconv"]
rank_four_rows = prior["rank_four_rows"]
reduce_at_character = prior["reduce_at_character"]

FAMILIES = (("C", 6, 0), ("D", 5, 1), ("E", 5, -1), ("F", 7, -3))


def boundary_check():
    a = ((-2, -2, 1, 1), (0, 0, 0, 2))
    b = ((0, 0, 0, 0), (-2, -1, -1, 4))
    rows = {}
    signatures = {}
    for (name, dim, exponent), (old, shift) in zip(
        FAMILIES, ((a, -1), (a, 1), (b, -1), (b, 1))
    ):
        before = [[w+shift for w in old[0]], [w-shift for w in old[1]]]
        new = []
        for twist in (0, 1):
            weights = [w for w in before[twist] if w < 0]
            weights += [w for w in before[1-twist] if w > 0]
            weights += [0]*(dim-len(weights))
            weights.sort()
            assert len(weights) == dim
            assert sum(weights) == (-1 if twist == 0 else 1)*exponent
            centered = sorted(dim*w - sum(weights) for w in weights)
            signature = min(tuple(centered), tuple(-w for w in reversed(centered)))
            assert signature not in signatures.setdefault(dim, set())
            signatures[dim].add(signature)
            new.append(weights)
        assert sum(abs(w) for weights in new for w in weights) == 2*dim
        rows[name] = new

    six = rows["C"][0]
    def paired(weights, stride):
        if not weights:
            return True
        pair = weights[0] + stride
        if pair not in weights[1:]:
            return False
        remaining = weights[1:]
        remaining.remove(pair)
        return paired(remaining, stride)

    assert not any(paired(six, d-six[0]) for d in set(six))
    max_eig, min_eig = six[-1], six[0]
    middle = -(max_eig + min_eig)//2
    # Use doubled weights, since the original extremal weights are odd.
    sym_square = sorted(a+b for a,b in combinations_with_replacement(
        [min_eig, 2*middle, max_eig], 2))
    assert sym_square != [2*w for w in six]
    print(json.dumps(dict(kind="new_feedback_boundary_controls", weights=rows,
                          components=8, total_dimension=46), sort_keys=True))


def new_rows(p, d):
    field, ell, triple, _ = data(p, d)
    _, a, b = rank_four_rows(p, d)
    q = field.q
    ell_dual = [(-1)**i*value for i,value in enumerate(ell)]
    b_twisted_sum = sum((-1)**i*value for i,value in enumerate(b))
    corrections = ((sum(a)-triple[0], 0), (triple[0], q), (0, b_twisted_sum-1), (0, 1))
    pairs = ((ell, a), (ell_dual, a), (ell, b), (ell_dual, b))
    rows = []
    for (first, second), (k0, k1) in zip(pairs, corrections):
        product = cycconv(first, second)
        rows.append([value*(-product[i] + k0 + k1*(-1)**i) for i,value in enumerate(ell)])
    return field, rows


def newton_determinant(traces, modulus):
    coeffs = [fmpz_poly([1])]
    for k in range(1, len(traces)+1):
        # Store k! times the kth elementary symmetric polynomial.
        coeff = sum((-1)**(j-1)*(factorial(k-1)//factorial(k-j))
                    * coeffs[k-j]*traces[j-1] for j in range(1,k+1)) % modulus
        coeffs.append(coeff)
    return coeffs[-1]


def phase_check(p, d, families):
    base, ell, _, _ = data(p, d)
    q, n = base.q, base.q-1
    assert q % 4 == 1
    modulus = fmpz_poly.cyclotomic(n)
    folded = {name: [] for name, _, _ in families}
    logs = []
    for e in range(1, 1+max(rank for _, rank, _ in families)):
        field, rows = new_rows(p, d*e)
        norm_generator = field.g ** ((field.q-1)//n)
        embedded = field.embed(base, base.g)
        norm_log = next(k for k in range(n) if embedded**k == norm_generator)
        assert gcd(norm_log,n) == 1
        logs.append(norm_log)
        for (name, rank, exponent), values in zip(FAMILIES, rows):
            if (name, rank, exponent) not in families or e > rank:
                continue
            buckets = [0]*n
            for i,value in enumerate(values):
                buckets[i*norm_log % n] += value
            folded[name].append(buckets)
    for k in range(1,n):
        if k == n//2:
            continue
        j = reduce_at_character(ell, k, modulus, n)
        j_dual = reduce_at_character(ell, (k+n//2)%n, modulus, n)
        for name, rank, exponent in families:
            traces = [reduce_at_character(row,k,modulus,n) for row in folded[name]]
            jacobi = j if exponent >= 0 else j_dual
            target = q**((5*rank-abs(exponent))//2) * (-jacobi)**abs(exponent)
            assert (newton_determinant(traces,modulus) - factorial(rank)*target) % modulus == 0

    _, a, b = rank_four_rows(p, d)
    _, new = new_rows(p, d)
    ell_sum = [(1+(-1)**i)*ell[i] for i in range(n)]
    fourth_sum = [(1+(-1)**i)*(a[i]+a[(-i)%n]+b[i]+b[(-i)%n]) for i in range(n)]
    product = cycconv(ell_sum, fourth_sum)
    correction = sum(a) + sum((-1)**i*value for i,value in enumerate(b)) + q
    for i in range(0,n,2):
        row_sum = sum(row[i]+row[(-i)%n] for row in new)
        assert ell[i]*product[i] + 2*row_sum == 4*ell[i]*correction
    print(json.dumps(dict(kind="new_feedback_exact_determinants", field=q, checked_per_family=q-3,
                          labels=[name for name,_,_ in families], norm_logs=logs,
                          largest_field=q**len(logs), feedback_positions=n//2), sort_keys=True))


if __name__ == "__main__":
    boundary_check()
    phase_check(5, 1, FAMILIES)
    phase_check(3, 2, FAMILIES[1:3])
