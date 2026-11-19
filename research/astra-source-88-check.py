"""Replay the finite-prime prefix and contact inequalities with rational bounds."""
from fractions import Fraction as Q
import json
from pathlib import Path


def interval(spec):
    center, radius = map(Q, spec.strip("[]").split(" +/- "))
    return center - radius, center + radius


def record(kind, **values):
    print(json.dumps({"kind": kind, **values}, sort_keys=True))


research = Path(__file__).resolve().parent
rows = [json.loads(line) for line in
        (research / "astra-adjoint-82-checks.jsonl").read_text().splitlines()]
packet, = (row for row in rows if row.get("kind") == "physical_packet_operator"
           and row.get("height") == 600)
first = interval(packet["first_increment_upper"])[1]
last = interval(packet["segment_residual_bound"])[1]
rate_lower = interval(packet["rate_upper"])[0]
floor = Q(2031, 128) - Q(1, 2**17)
seed = Q("2.828428")
disk = Q("1.94")
derivative = Q("0.51358")
assert seed**2 > 4 * (2 + Q(1, 10**30))
assert 2*seed*disk*(4*floor-2*disk**2) > 4*disk**2*(seed+disk)**2
assert (seed+disk)**2 < derivative**2*(4*floor+(seed+disk)**2)
residual = Q("3.932e-175")
assert first < Q("0.169724") and first*derivative**600 < residual
assert residual**2*10**347 < Q(1, 8)**2
cap, imag = Q("5.268"), Q("2.44")
assert cap**2 < Q(2, 3)**2 * (4*floor+cap**2-2*imag**2)
record("uniform_seed_disk_and_true_cold_square", n_min="1e30", n_max="1e347",
       normalized_residual_upper="3.932e-175", complex_prefix_derivative_upper="0.51358",
       counting_residual_upper="1/8", stationary_coordinate_upper="5.268")

assert 16*floor/13 > (Q("2.4")+Q("2.00001"))**2
assert (870*residual**2)**2*10**692 < 2*Q("2.4")**2
assert (3480*residual**2)**2*10**688 < Q(1,100)
record("true_forced_nonsingularity", n_min="1e30", full_cold_square=True,
       first_spread_regular_through_p="1e692", enlarged_sector_regular_through_p="1e688")

preimage = Q("0.005377")
assert derivative*last/rate_lower < preimage
assert derivative*last/rate_lower*2**18 < 1410
delta, h, charge = Q(1,5), Q("0.368"), Q("0.3029")
assert (1+delta)*h**2+delta*h/2 < (1-3*delta)/2
assert (1-delta)**2 > 4*charge**2*(1+delta+delta/h)
assert 4*floor*charge**2 > (448*preimage)**2
assert floor*(224-Q(1,224))**2 > 891**2
assert 16*floor*charge**2 > 13*(1410*Q("0.000947"))**2
assert (891-Q("4.768"))/870 > Q("1.01")
assert (Q(4,27)*residual**2)**2*10**699 < Q("1.01")**2
record("true_signed_amplitude_tails", active_size_ratio_upper="3/2",
       physical_preimage_sup_upper="0.005377", transverse_derivative_upper=1410,
       both_opposite_tail_sizes_strictly_above="n/(2 sqrt(p))",
       both_tail_abs_U_times_q_lower=891,
       one_tail_exp_abs_rho_times_q_abs_im_t_lower="0.0004735",
       no_balanced_ramified_first_contact_through_p="1e699")
