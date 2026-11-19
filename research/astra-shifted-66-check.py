"""Overlapping signed refresh with eight transported Jacobi shifts at round 65's floor."""
from collections import Counter
from math import comb
from pathlib import Path
import json
import runpy

from flint import acb, arb, arb_poly, ctx

prior = runpy.run_path(str(Path(__file__).with_name("astra-joint-65-check.py")))
D = prior["D"]
t = prior["prev"]["t0"]
strip, packets, arities = 18, 28, 9


def transports():
    families = {
        "U": ([-4, 0, 0, 4], [0]*4),
        "Uprime": ([0]*4, [-4, 0, 0, 4]),
        "D": ([-4, 0, 0, 0], [0, 0, 0, 4]),
        "Ddual": ([0, 0, 0, 4], [-4, 0, 0, 0]),
    }
    outputs = {}
    for name, (one, chi) in families.items():
        for sign in (1, -1):
            before = ([w-sign for w in one], [w+sign for w in chi])
            rank = sum(abs(w) for side in before for w in side)//2
            sides = []
            for twist in (0, 1):
                row = [w for w in before[twist] if w < 0]
                row += [w for w in before[1-twist] if w > 0]
                sides.append(sorted(row + [0]*(rank-len(row))))
            assert sum(sides[0]) == -sum(sides[1])
            outputs[name, sign] = sides

    # A geometric Jacobi twist shifts the whole first list and the second by
    # the opposite amount. A quadratic line in a product requires duality.
    for key, sides in outputs.items():
        allowed = []
        for other, peer in outputs.items():
            if len(peer[0]) != len(sides[0]):
                continue
            a = peer[0][0]+sides[0][-1]
            if (peer[0] == sorted(a-w for w in sides[0]) and
                    peer[1] == sorted(-a-w for w in sides[1])):
                allowed.append((other, a))
        name, sign = key
        partner = {"U": "Uprime", "Uprime": "U"}.get(name, name)
        assert allowed == [((partner, sign), 0)]
    return outputs


def compact_feedback():
    source = runpy.run_path(str(Path(__file__).with_name("astra-prime-phase-32-check.py")))
    conv = source["cycconv"]
    fields = []
    for p, k in ((5, 1), (3, 2), (13, 1), (17, 1), (5, 2), (7, 2), (97, 1)):
        _, ell, _, _ = source["data"](p, k)
        q = p**k
        n = q-1
        chi = [(-1)**i for i in range(n)]
        twist = lambda row: [c*x for c, x in zip(chi, row)]
        square = conv(ell, ell)
        U = [l*x for l, x in zip(ell, conv(square, square))]
        N = [l*x for l, x in zip(ell, square)]
        Drow = [l*(x+2*(q+1)) for l, x in zip(ell, conv(N, N))]
        sources = {"U": U, "Uprime": twist(U), "D": Drow, "Ddual": twist(Drow)}
        outputs = {}
        for name, row in sources.items():
            for sign in (1, -1):
                raw = conv(ell if sign == 1 else twist(ell), row)
                both = (name, sign) in (("D", -1), ("Ddual", 1))
                a = int(name=="U" or both)
                b = int(name=="Uprime" or both)
                outputs[name, sign] = [l*(-x+a+b*c) for l, x, c in zip(ell, raw, chi)]
                # Actual source on paired lifts.  Numerators use q^(5/2).
                partner = {"U":"Uprime", "Uprime":"U", "D":"Ddual", "Ddual":"D"}[name]
                raw2 = conv(twist(ell) if sign == 1 else ell, sources[partner])
                assert all(x+y == 0 for i, (x, y) in enumerate(zip(raw, raw2)) if i%2==1)
                for i in range(0, n, 2):
                    signed_pair = 2*outputs[name, sign][i]
                    physical = ell[i]*(raw[i]+raw2[i])
                    assert physical+signed_pair == 2*(a+b)*ell[i]
        for (name, sign), row in outputs.items():
            partner = {"U":"Uprime", "Uprime":"U"}.get(name, name)
            assert row == [outputs[partner, sign][-i % n] for i in range(n)]
        fields.append(q)
    record("eight_actual_compact_shifted_rows", fields=fields,
           denominator="q^(5/2)", correction_in_units_qminus1_over_q_to_5halves={
           "U_and_Uprime_lift_pair":1, "Dplus_Ddualminus":0, "Dminus_Ddualplus":2})


def refresh():
    coefficients = prior["projection_data"]()
    v, _, _, _, little, _, _, large = coefficients
    # The first listed large value applies to all four symplectic sources.
    # The two other values also cover their lift exchanges.
    bare_norm = (2*little[0]**2+2*little[1]**2+little[2]**2).sqrt()
    small_cap = arb(3)/10**8
    limits = [arb(153)/10**6, arb(145)/10**6]
    variance = 4*(limits[0]**2+limits[1]**2)
    rows, pars = prior["upper"](acb(t))
    a, b, c, d, z, w, vabs = pars
    base = prior["kern"]["dim"]+2*a+3*b+4*c+arb(23)*d/4+8*(z+w+vabs)
    extent = base+arb(128).sqrt()*small_cap
    slope = extent/(4*t+extent**2).sqrt()
    drift = slope*small_cap+variance/(4*t.sqrt())
    assert bare_norm+drift < small_cap
    assert abs(large[0])+drift < limits[0]
    assert max(abs(x).upper() for x in large[1:])+drift < limits[1]
    # Lipschitz bound for the joint conditional expectation on the invariant box.
    all_extent = extent+28*sum(limits)
    contract = all_extent/(4*t+all_extent**2).sqrt()
    assert contract < arb(43)/100
    # Uniform signed change to the m^2 sector when the large block is admitted,
    # relative to the same small inputs.  Use the certified seven-center binary.
    _, _, _, selected_binary, _, _, _, _ = coefficients
    seven_h2 = selected_binary/(2*v**2)
    # |f'''| <= 3/(4t) globally, by its explicit formula.
    third = 3/(4*t)
    h2 = seven_h2+arb(0,(third*(8*abs(v)+arb(128).sqrt()*small_cap)/2).upper())
    rem = third*28*sum(limits)/6
    relative = h2+arb(0,rem.upper())
    assert relative < 0
    var_lo = 4*(abs(large[0]).lower()-drift)**2
    var_lo += 4*(min(abs(x).lower() for x in large[1:])-drift)**2
    neg = arb((relative*variance).lower(), 0)
    upper_neg = (relative*var_lo).upper()
    assert neg < upper_neg < 0
    return (v, rows, base, small_cap, limits, variance, bare_norm, slope, drift,
            contract, neg, upper_neg)


def debit(upper, base, small, limits, variance, outputs):
    # Coefficients keyed by signed position. Every one-tag majorant is centered at 5.
    small_row = arb_poly([0, 2, 0, 2, 0, 16, 0, 2, 0, 2, 0])*small
    # From the two (delta_-4 + 6 delta_0 + delta_4) pairs and one Sp8
    # (2 delta_-2 + 4 delta_0 + 2 delta_2), times the component bound.
    weights = [arb(0)]*11
    for (name, _), sides in outputs.items():
        coefficient = limits[0 if name.startswith("U") else 1]
        for k, mult in Counter(sides[0]).items():
            weights[5+k] += mult*coefficient
    assert all(weights[i].overlaps(weights[10-i]) for i in range(11))
    big_row = arb_poly(weights)
    size_small = sum(small_row.coeffs(), arb(0)).upper()
    size = (size_small+sum(weights, arb(0))).upper()
    assert size < arb(9)/1000
    powers_small = [small_row**h for h in range(D+1)]
    powers_big = [big_row**h for h in range(D+1)]
    blocks = [arb_poly()]
    for h in range(1, D+1):
        row = powers_small[h]
        if h >= 2:
            row += powers_small[h-2].left_shift(10)*comb(h, 2)*variance
        for k in range(3, h+1):
            row += powers_small[h-k]*powers_big[k]*comb(h, k)
        blocks.append(row)
    U = []
    for row in upper:
        side = [x/2 for x in row[1:]]
        U.append(arb_poly(side[::-1]+[row[0]]+side))
    rho = (base+2)**2/(4*t)
    assert rho < 1
    binom = arb(1)
    for k in range(1, 16):
        binom *= (arb(3)/2-k)/k
    tail = 2*t.sqrt()*abs(binom)*rho**15/(1-rho)
    offsets = []
    errors = []
    for r in range(arities+1):
        center = 5*(D-r)
        poly = arb_poly()
        for h in range(1, D-r+1):
            poly += U[r+h]*blocks[h]*comb(r+h, r)
        outside = max([arb(0)]+[poly[center+i].upper() for i in range(strip+1, center+1)])
        ratio = (size/2)*(1+arb(r)/4)
        assert ratio < 1
        analytic = tail/2**r*((r+1)*size_small/2+
                  comb(r+2, r)*(size_small**2+variance)/4+
                  comb(r+3, r)*(size/2)**3/(1-ratio))
        offsets.append(arb_poly([(2*poly[center+k]).upper() for k in range(-strip, strip+1)]))
        errors.append((2*(outside+analytic)).upper())
    return offsets, errors, size


def escape(rows, charges, errors):
    kernel = [lower-cost for lower, cost in zip(rows, charges)]
    binary = kernel[2][strip]-errors[2]
    assert binary > arb(1)/20
    h = [arb(0)]*packets
    for height in range(1, 6001):
        sides = [x/2 for x in h]
        b = arb_poly(sides[::-1]+[sum(i*x for i, x in enumerate(h))]+sides)
        mass = sum(b.coeffs(), arb(0)).upper()
        accum = [arb(0)]*packets
        power = arb_poly([1])
        error = arb(0)
        for r, row in enumerate(kernel):
            if r:
                power *= b
            prod = power*row
            error += errors[r]*mass**r
            for k in range(1, packets+1):
                accum[k-1] += 2*prod[strip+r*packets+k]
        h = [max(arb(0), (x-2*error).lower()) for x in accum]
        if sum(k*x for k, x in enumerate(h, 1)) > 21:
            return height, binary
    raise ArithmeticError("overlapping lower map did not escape")


def record(kind, **fields):
    print(json.dumps(dict(kind=kind, **fields), sort_keys=True), flush=True)


def run():
    outputs = transports()
    record("transported_shifted_sources", rank_and_L_determinant={
        name+("+" if s>0 else "-"): [len(side[0]), -sum(side[0])]
        for (name, s), side in outputs.items()}, quadratic_Jacobi_exponents=[0],
        U_dual="Uprime at same sign", D_dual="self at same sign")
    compact_feedback()
    v, up, base, small, limits, var, bare, slope, drift, contract, neg, upper_neg = refresh()
    scaled = prior["scaled"]
    record("overlapping_thirteen_tag_refresh", precision=ctx.prec, floor="2031/128",
           five_L2_radius="3e-8", zero_input_five_norm_times_1e12=scaled(bare, 10**12),
           eight_component_caps_times_1e6=[153, 145], variance_times_1e12=scaled(var, 10**12),
           slope_times_1e6=scaled(slope, 10**6), drift_times_1e12=scaled(drift, 10**12),
           joint_contraction_times_1e6=scaled(contract, 10**6),
           large_m2_change_times_1e12=[scaled(neg, 10**12)[0],scaled(upper_neg, 10**12)[1]])
    rows = prior["lower"](prior["lower_data"](), abs(v))
    charges, errors, mass = debit(up, base, small, limits, var, outputs)
    height, binary = escape(rows, charges, errors)
    record("every_level_thirteen_tag_escape", height=height, floor="2031/128",
           threshold=21, binary_times_1e6=scaled(binary, 10**6),
           tag_mass_upper_times_1e6=scaled(mass, 10**6), shape=[arities, strip, packets])


if __name__ == "__main__":
    run()
