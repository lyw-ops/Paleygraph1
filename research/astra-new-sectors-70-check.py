"""Replay the old and independent-factor debits, bounding off-strip maxima separately."""
import json
from math import comb
from pathlib import Path
import runpy

from flint import arb, arb_poly

prior = runpy.run_path(str(Path(__file__).with_name("astra-unary-69-sector.py")))
D, U, caps = (prior[key] for key in ("D", "U", "caps"))
old, rows, costs, errors = (prior[key] for key in ("old", "rows", "costs", "errors"))
new = [arb(0)]*11
five = arb_poly([0,2,0,2,0,16,0,2,0,2,0])*(arb(3)/10**8)
old_tags = list(five.coeffs())+[arb(0)]*(11-len(five))
for (name, sign), sides in old["previous"]["transports"]().items():
    row = old_tags if len(sides[0]) == 6 else new
    for weight in sides[0]:
        row[weight+5] += caps[0 if name.startswith("U") else 1]
a, b = map(arb_poly, (old_tags, new))
new_block = [arb_poly(), arb_poly()]
for h in range(2,D+1):
    new_block.append(comb(h,2)*prior["c6"]*(a**(h-2)).left_shift(10)
                     +sum((comb(h,k)*a**(h-k)*b**k for k in range(3,h+1)),arb_poly()))
extra = []
for r in range(10):
    mid = 5*(D-r)
    def off(poly):
        return max([arb(0)]+[poly[mid+k].upper() for k in range(19,mid+1)])
    new_debit = sum((comb(r+h,r)*U[r+h]*new_block[h] for h in range(2,D-r+1)),arb_poly())
    # Do not assume the old and new sector peaks occur at the same off-strip bin.
    increment = 2*off(new_debit)
    errors[r] += increment
    extra.append(prior["q"]["scaled"](increment,10**15))
height,binary = old["previous"]["escape"](rows,costs,errors)
print(json.dumps(dict(kind="full_old_and_new_independent_sector_collection",floor="2031/128",
                      height=height,binary_times_1e9=prior["q"]["scaled"](binary,10**9),
                      offstrip_splitting_times_1e15=extra,mass_threshold=21,
                      precision=prior["ctx"].prec,shape=[9,18,28])))
