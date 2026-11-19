"""Exact replay of the physical translated-tail constants and cofactor bound."""
from fractions import Fraction as Q
import json
from pathlib import Path


def record(kind, **fields):
    print(json.dumps({"kind": kind, **fields}, sort_keys=True))


research = Path(__file__).resolve().parent
rows = [json.loads(s) for s in
        (research / "astra-source-88-checks.jsonl").read_text().splitlines()]
prefix, = (v for v in rows if v["kind"] == "uniform_seed_disk_and_true_cold_square")
r = Q(prefix["normalized_residual_upper"])
n_min = int(Q(prefix["n_min"]))
order_ratio_upper = Q("1.415")
assert order_ratio_upper**2 > 2+Q(1, n_min)
assert Q("29.5")**2 > 870
assert 1+Q("29.5")+870*order_ratio_upper*r < 31
inverse_sqrt_n = Q(1, 10**15)
column_denominator = 1-Q(1, n_min)-order_ratio_upper*inverse_sqrt_n
assert (inverse_sqrt_n+order_ratio_upper)/column_denominator < Q("1.42")
assert Q("31.5")*Q("1.42") < 45
floor = Q(2031, 128)
radius = Q(1, 2**17)
assert floor-radius > Q("3.98")**2
assert (floor+radius)**2+radius**2 < Q("3.985")**4
assert radius/(2*(floor-radius)) < Q("1e-6")
assert Q("0.55469")**2 < Q(4, 13)
assert Q("3.98")*(Q("0.55469")-Q("1e-6")) > Q("2.20")
assert Q("3.985")*Q("1.77")+Q("0.0055")+45*r < Q("7.1")
assert Q("29.5")+Q("0.5")+45 < 76
assert 1+Q("0.0055")+45*r < Q("1.01")
assert 870*(1+Q("0.0055")+45*r) < 875
assert 76+875*r < 77
assert Q(76**2+77**2, 2)+(Q("1.01")+Q("7.1"))*875 < 13000
record("translated_physical_opposite_tails", n_min=str(n_min),
       two_floor_cost_per_sum_squared_residuals=13000,
       tail_slope="2.20", tail_subtraction="7.1", same_row_cost=26000)

field_limsup = Q("3.06e-208")
assert 4*Q("0.449922")**600 < field_limsup
sqrt2_upper = Q("1.415")
loss = Q(870)/Q("2.4")
for cost, cofactor in ((r, Q("5.2e345")), (field_limsup, Q("8.6e411"))):
    assert (2+sqrt2_upper)*loss*cost**2*cofactor < 1
record("physical_singular_spread_cofactor", n_min=str(n_min),
       all_order_exclusion_cofactor_upper="5.2e345",
       field_first_exclusion_cofactor_upper="8.6e411")

# p=1997, n=2*499. Exhibit a symmetric positional eigenrow supported
# on the nonidentity coset, so its restriction to H cancels identically.
p, ell = 1997, 499
assert all(p % j for j in range(2, 45))
assert all(ell % j for j in range(2, 23))
n = (p-1)//2
root = next(g for g in range(2, p)
            if pow(g, n, p) != 1 and pow(g, 4, p) != 1)
generator = root**2 % p
group = [pow(generator, j, p) for j in range(n)]
assert len(set(group)) == n
subgroup, coset = group[::2], group[1::2]
x = generator
support = {x, pow(x, -1, p)}
assert support <= set(coset) and not support.intersection(subgroup)


def sign(x):
    return {p-1: -1, 0: 0, 1: 1}[pow(1-x, n, p)]


sigma = sign(x)
assert all(sign(z) == sigma for z in support)
counts = []
for block in (subgroup, coset):
    char_sum = sum(map(sign, block))
    zeros_for_sector = sum(sign(z) != sigma for z in block)
    assert 2*zeros_for_sector == ell+int(1 in block)-sigma*char_sum
    assert char_sum**2 <= p
    counts.append(zeros_for_sector)
# The spectral coefficients are twice a cosine, nonzero as 4 does not
# divide n. All ell residues are represented after folding on the coset.
assert n % 4 == 2 and ell >= counts[1]+1
record("signed_coset_restriction", p=p, subgroup_order=ell, root=root,
       positional_support=sorted(support), sector=sigma,
       nonzero_restriction_coset=1, nonzero_restriction_sector_zeros=counts[1],
       identity_coset_restriction_vanishes=True, folded_nonzero=ell)

L = floor-radius
b, c = Q(2872), Q("1.031e-169")
assert 2**18*r < c
assert Q("0.010954497")*2**18 < b
assert 4+Q("5.768")**2/L < Q("2.5")**2
assert (Q("3.46")-2)**2*L > Q("5.768")**2
D = Q("5.768")*(c+870*b*r**2)
assert (1+D)/(2*L)+(Q("2.5")*c)**2/2 < Q("0.032")
assert (Q("3.46")*b)**2*(870*31)/2 < Q("1.4e12")
assert Q("1.4e12")*Q(108,3125) < Q("5e10")
record("physical_full_force_shrinking_strip", n_min=str(n_min),
       real_and_imag_half_width="2^-18", energy_floor_squared_coefficient="0.032",
       energy_sqrt_n_normalized_residual_cubed_coefficient="5e10",
       residual_upper=str(prefix["normalized_residual_upper"]),
       no_unit_phase_exit_when="n*energy_upper<L/2")
