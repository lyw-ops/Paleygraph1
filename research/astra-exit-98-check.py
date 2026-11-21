"""Outward certificate for quadratic/quartic GL4 returns and positive real exit cuts."""
from collections import Counter, defaultdict
from math import comb
from pathlib import Path
import json
import runpy

from flint import acb, arb

HERE = Path(__file__).resolve().parent
prev = runpy.run_path(str(HERE / "astra-incoming-97-check.py"))
r84 = prev["r84"]
r96 = prev["r96"]
fields = prev["fields"]
p3 = prev["p3"]
unit = prev["unit"]
four = r84["rank_four"]


def return_fiber(twist):
    square = four["four_powers"](2)
    quartic = four["four_powers"](4)
    occurrences = Counter(shape for shape, shift in square)
    weights = Counter()
    for (shape, shift), count in square.items():
        if shape == four["ZERO"] or occurrences[shape] != 1:
            continue
        assert quartic[shape, shift] >= 48 * count
        for w, m in four["four_fiber"](shape, twist).items():
            weights[w + (shift if twist else -shift)] += count * m
    return weights


weights = return_fiber(0)
assert weights == return_fiber(1)
assert weights == Counter({-w:m for w,m in weights.items()})


double_shapes = defaultdict(list)
for (shape, shift), count in four["four_powers"](2).items():
    double_shapes[shape].append((shift, count))
double_shapes = {s: sorted(v) for s,v in double_shapes.items() if len(v)>1}
assert len(double_shapes) == 2
assert all(len(v) == 2 and all(m == 1 for a,m in v) for v in double_shapes.values())


def signed_upper(t):
    rows, pars = prev["signed_upper"](t)
    _, beta, groups, amend = p3["coefficients"](
        t, acb(fields["prev"]["da"]), acb(fields["prev"]["db"]))
    gamma = arb(499)/500 * beta * groups[1, 1][0, 0]
    for tag in [r96["trivial"], *sorted(prev["tags"])]:
        cols = r96["columns"](groups, amend, beta, tag)
        for j in range(7):
            shifted = defaultdict(lambda: arb(0))
            for shape, ((a,_), (b,_)) in double_shapes.items():
                for (u,v,e), first in cols[j+2].items():
                    if tag == r96["trivial"] and u == v == 0:
                        continue
                    second = cols[j+2].get((u,v,e+a-b))
                    if second is None:
                        continue
                    gain = r84["cancellation"](first,second)
                    if gain:
                        for l in range(-2*u,2*u+1,4):
                            for w,m in four["four_fiber"](shape).items():
                                shifted[l+w-e-a] += (v+1)*m*gain
            factor = comb(j+2,2) * abs(gamma)**2 / 64
            debit = defaultdict(lambda: arb(0))
            for x, val in shifted.items():
                for w, multiplicity in p3["pair_fiber"](*tag):
                    debit[x+w] += val * multiplicity * factor
            if j < 5:
                add_quartic(debit, j, gamma, cols, tag)
            for k in range(len(rows[j])):
                saved = 2*min(debit[k].lower(),debit[-k].lower()) if k else debit[0].lower()
                rows[j][k] -= saved
                assert rows[j][k] >= 0
    return rows, pars


def add_quartic(debit, j, gamma, cols, tag):
    base = defaultdict(lambda: arb(0))
    for (u,v,e), first in cols[j+2].items():
        second = cols[j+4].get((u,v,e))
        if second is None:
            continue
        # Both directions carry exactly the same selected square fiber.
        gain = r84["cancellation"](comb(j+2,2)*gamma**2*first,
                                   comb(j+4,4)*gamma**4*arb(3)/4*second)
        if gain:
            for b in range(-2*u,2*u+1,4):
                base[b-e] += (v+1)*gain
    for x, val in base.items():
        for w, multiplicity in p3["pair_fiber"](*tag):
            for l, count in weights.items():
                debit[x+w+l] += val * multiplicity * count/64


r84["envelope"].__globals__["signed_upper"] = signed_upper


def real_cut():
    heights = (100, 250, 275, 300, 600)
    bounds = list(map(arb, (".001180", ".000343", ".000322", ".000312", ".010955")))
    records = [json.loads(line) for line in
               (HERE / "astra-adjoint-82-checks.jsonl").read_text().splitlines()]
    products = {row["height"]: arb(row["segment_residual_bound"]) for row in records
                if row["kind"] == "physical_packet_operator"}
    assert all(products[k] < v for k, v in zip(heights, bounds))
    lag = arb(0)
    for a, b, left, right in zip(heights, heights[1:], bounds, bounds[1:]):
        ratio = ((right / left).log() / (b - a)).exp()
        lag += left * sum(ratio**j for j in range(b - a))
    assert lag < arb("1.011")
    q = arb(".984138")
    coefficients = arb(2).sqrt() * (2 / (1 - q) - 1)
    assert coefficients < 178
    edge = arb(2031)/128
    width = arb(1)/2**17
    interval = arb(edge, width)
    limit = 4*interval.sqrt()
    start = arb("4.768")
    ref = (4*interval + start**2).sqrt()
    defect = (20*interval).sqrt() - ref + start*(limit+start)/ref
    assert defect < arb("19.17")
    assert (limit+start)**2/(4*arb(10)**15) < arb("19.17")
    entrance = 4*(edge-width).sqrt()-start-arb("1.011")-bounds[0]/(1-q)
    margin = entrance-178*arb("19.17")/6000
    assert entrance > arb("10.07") and margin > arb("9.5")
    assert arb(".00278")*178*arb("19.17") < arb("9.5")
    print(json.dumps(dict(kind="positive_real_exit_cuts", initial_packet_lag=str(lag),
        translated_row_price_sum_limsup=str(coefficients), full_signed_lower=str(entrance),
        bulk_defect_upper=str(defect), erased_signed_lower=str(margin),
        cut_threshold=".00278", one_sided_cut_threshold=".00139")), flush=True)


if __name__ == "__main__":
    real_cut()
    caps = json.loads((HERE / "astra-exit-98-caps.json").read_text())
    for row in caps:
        r96["previous"]["verify"](*row)
    r84["envelope"].__globals__["signed_upper"] = prev["signed_upper"]
    lo, hi, nx, cap = caps[0]
    mid, half = (lo+hi)*unit/2, (hi-lo)*unit/2
    data = r84["envelope"](mid, half, unit, nx, 1, arb(1))
    frozen = [arb(x)/10**20 for x in cap]
    overrun = r84["prior"]["image"](mid, half, data, frozen)[0][0]-frozen[0]
    assert overrun > r84["prior"]["EPS"]
    print(json.dumps(dict(kind="previous_first_packet_overrun", excess=str(overrun),
        unique_shift_square_fiber_numerator=sum(weights.values()),
        double_shift_shapes=len(double_shapes))), flush=True)
