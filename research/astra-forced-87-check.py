"""Check the forced-contact constants from the certified predictor inputs using rationals."""
from fractions import Fraction as Q
import json
from pathlib import Path


research = Path(__file__).resolve().parent


def records(filename):
    return [json.loads(line) for line in (research / filename).read_text().splitlines()]


def upper(ball):
    midpoint, radius = ball.strip("[]").split(" +/- ")
    return Q(midpoint) + Q(radius)


def report(**row):
    print(json.dumps(row, sort_keys=True))


packet, = (row for row in records("astra-adjoint-82-checks.jsonl")
           if row.get("kind") == "physical_packet_operator" and row.get("height") == 600)
angular, = (row for row in records("astra-dissipation-80-checks.jsonl")
            if "complex_upper_sum" in row)
outer_sup = upper(packet["segment_residual_bound"])
rate_cap = Q("0.44992117")
assert upper(angular["complex_upper_sum"]) < rate_cap
scaled_sup = 2**18 * outer_sup
assert scaled_sup < 2872
assert 2**18 * 4 * rate_cap**600 < Q("7.99e-203")

t_min = Q(2031, 128) - Q(1, 2**17)
tau = Q(1, 5)
max_sine = 2*tau / (1 + tau**2)
charge_factor_squared = 1 / (1-max_sine)
assert max_sine == Q(5, 13) and charge_factor_squared == Q(13, 8)
assert scaled_sup**2 * charge_factor_squared / (4*t_min) < 460**2
report(kind="height_600_transverse_residual", arithmetic="exact rational on prior Arb endpoints",
       half_square="1/262144", cauchy_sup_over_abs_imag_upper=2872,
       limiting_cauchy_normalized_l2_over_abs_imag_upper="7.99e-203",
       signed_charge_l1_factor_over_q_abs_imag_upper=460)

delta = Q(1, 5)
h_lower = Q("0.368")
assert (1+delta)*h_lower**2 + delta*h_lower/2 < (1-3*delta)/2
balanced_squared = 8*t_min/13
ratio_squared = (1-delta)**2 / (1+delta+delta/h_lower)
assert balanced_squared > Q("3.12")**2
assert balanced_squared * ratio_squared > Q("1.89")**2
report(kind="necessary_actual_contact_transverse_rms", arithmetic="exact rational",
       actual_contact_observed=False, all_coranks=True, equal_active_counts_lower="3.12",
       active_counts_within_factor="3/2", corresponding_lower="1.89")

diameter = Q("0.02191")
assert 2*outer_sup < diameter
robust_weight = (Q("1.89")/diameter)**2
assert robust_weight > 7441
assert t_min*(robust_weight-2) > 343**2
assert t_min*((Q("3.12")/diameter)**2 - 2) > 567**2
report(kind="actual_contact_after_two_orbit_deletions", arithmetic="exact rational",
       diameter_upper="0.02191", ratio_three_halves_remaining_weight_over_m_times_q_squared_lower=7441,
       required_distinct_orbits=3, ratio_three_halves_abs_U_times_q_lower=343,
       equal_counts_abs_U_times_q_lower=567)
