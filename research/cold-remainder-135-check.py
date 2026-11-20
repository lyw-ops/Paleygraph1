"""Check a positive comparison obstruction and quantitative remainder bounds."""

from contextlib import redirect_stdout
from fractions import Fraction
import io
import json
from pathlib import Path
import runpy


path = Path(__file__).with_name("cold-combined-height-130-check.py")
with redirect_stdout(io.StringIO()):
    inherited = runpy.run_path(str(path))

arb = inherited["arb"]
radius = inherited["N"]
fields = inherited["fields"]
a, b, c, d, z, w, v = inherited["pars"]
center = [arb(0)]*(radius+1)
center[0], center[1], center[2], center[3] = a+b, 3*b/2, a, 3*b/2
for polynomial, coefficient, offset in (
    (fields["kern"]["F"], c, 4),
    (fields["kern"]["G"], d, 5),
    (fields["old"]["R"], z, 2),
    (fields["field"], w+v, 4),
):
    for k in range(offset+1):
        center[k] += coefficient*polynomial[offset+k]*(2 if k else 1)

core, _ = inherited["residual"](inherited["h"])
remainder = inherited["symmetric"](
    [mass+(2 if k else 1)*core[radius+k] for k, mass in enumerate(center)],
    radius,
)
seed = inherited["symmetric"]([arb(0), inherited["seed"]], radius)
floor = 4*inherited["floor"]
cubic = (seed+remainder)**3-seed**3
folded = [
    (2 if k else 1)*(remainder[radius+k]/floor.sqrt()
                   +cubic[3*radius+k]/(2*floor*floor.sqrt()))
    for k in range(3*radius+1)
]
moment = sum(mass*inherited["price"](k) for k, mass in enumerate(folded))
affine_limit = sum(folded)+moment/inherited["slope"]
assert affine_limit > arb("0.6404")
print(json.dumps({
    "kind": "unsigned_remainder_positive_comparison", "height": 601,
    "center": "2031/128", "retained_arities": [1, 3],
    "affine_price_limit_strict_lower": "0.6404",
}, sort_keys=True))

floor = Fraction(2031, 128)
half = Fraction(1, 2**17)
four_floor = 4*(floor-half)
disk = Fraction("1.971573")
seed_amplitude = Fraction("2.828428")
curvature = Fraction("0.139")
assert (4*(floor+2*half))**2 < curvature**2*(four_floor-disk**2)**3
assert disk*curvature < Fraction("0.275")
assert seed_amplitude**2 < Fraction("0.335")**2*(four_floor+seed_amplitude**2)
assert Fraction("0.275")*(Fraction("0.5145")+Fraction("0.335")) < Fraction("0.234")

rho = Fraction("4.8")**2/four_floor
assert 0 < rho < Fraction("0.603")**2
tail = 4*Fraction("0.603")*rho**14*(15/(1-rho)+rho/(1-rho)**2)
assert tail < Fraction("0.0000407")
print(json.dumps({
    "kind": "signed_remainder_counting_and_packet_tail",
    "remainder_step_counting_upper": "0.275",
    "joint_block_counting_upper": "0.234",
    "geometric_tail_start_binomial_index": 14,
    "geometric_translated_tail_upper": "0.0000407",
}, sort_keys=True))
