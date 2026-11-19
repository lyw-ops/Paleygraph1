"""Check the rank-four Mellin determinant identities by exact Newton traces."""
import json
from math import gcd
from pathlib import Path
import runpy

from flint import fmpz_poly

base_code = runpy.run_path(str(Path(__file__).with_name("astra-prime-phase-32-check.py")))
data = base_code["data"]
cycconv = base_code["cycconv"]
reduce_at_character = base_code["reduce_at_character"]


def rank_four_rows(p, d):
    field, ell, triple, r = data(p, d)
    ell_dual = [(-1)**index * value for index, value in enumerate(ell)]
    first = cycconv(ell, r)
    second = cycconv(ell_dual, r)
    a = [value * (first[index] + 1 + field.q * (-1)**index)
         for index, value in enumerate(ell)]
    b = [value * (second[index] + triple[0]) for index, value in enumerate(ell)]
    return field, a, b


def traces_over_extensions(p, d, base):
    n = base.q - 1
    rows = []
    logs = []
    for degree in range(1, 5):
        field, a, b = rank_four_rows(p, d * degree)
        norm_generator = field.g ** ((field.q - 1) // n)
        embedded = field.embed(base, base.g)
        norm_log = next(k for k in range(n) if embedded**k == norm_generator)
        assert gcd(norm_log, n) == 1
        a_folded = [0] * n
        b_folded = [0] * n
        for index, (a_trace, b_trace) in enumerate(zip(a, b)):
            bucket = index * norm_log % n
            a_folded[bucket] += a_trace
            b_folded[bucket] += b_trace
        rows.append((a_folded, b_folded))
        logs.append(norm_log)
    return rows, logs


def determinant_times_24(traces):
    t1, t2, t3, t4 = traces
    return t1**4 - 6 * t1*t1*t2 + 3 * t2*t2 + 8 * t1*t3 - 6 * t4


def check_base(p, d):
    base, ell, triple, r = data(p, d)
    q, n = base.q, base.q - 1
    assert q % 4 == 1
    modulus = fmpz_poly.cyclotomic(n)
    rows, logs = traces_over_extensions(p, d, base)
    checked = 0
    for k in range(1, n):
        if k == n // 2:
            continue
        a_traces = [reduce_at_character(a, k, modulus, n) for a, _ in rows]
        b_traces = [reduce_at_character(b, k, modulus, n) for _, b in rows]
        j = reduce_at_character(ell, k, modulus, n)
        assert (determinant_times_24(a_traces) - 24*q**7*j*j) % modulus == 0
        assert (determinant_times_24(b_traces) - 24*q**8) % modulus == 0
        checked += 1
    assert checked == q - 3
    _, a, b = rank_four_rows(p, d)
    ell_sum = [(1+(-1)**i)*ell[i] for i in range(n)]
    r_sum = [(1+(-1)**i)*(r[i]+r[(-i)%n]) for i in range(n)]
    product = cycconv(ell_sum, r_sum)
    for i in range(0, n, 2):
        j = (-i) % n
        assert 2*(a[i]+a[j]+b[i]+b[j])-ell[i]*product[i] == 4*ell[i]*(1+q+triple[0])
    print(json.dumps(dict(base=q, kind="rank_four_mellin_determinants",
                          norm_generator_logs=logs, characters_per_object=checked,
                          largest_field=q**4, feedback_positions=n//2), sort_keys=True))


if __name__ == "__main__":
    for p, d in ((5, 1), (3, 2), (13, 1)):
        check_base(p, d)
