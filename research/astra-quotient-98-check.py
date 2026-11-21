"""Verify the signed triangular exterior identity on the exact cold prime orbit."""
import json
from pathlib import Path
import runpy

from flint import acb, arb, ctx, fmpq
import numpy as np
from scipy.optimize import linprog


prior = runpy.run_path(str(Path(__file__).with_name("astra-recur-95-check.py")))
apply = prior["apply"]
enclose = prior["enclose"]
ctx.prec = 384


def equal(left, right):
    difference = left - right
    assert difference.contains(0) and abs(difference) < arb(10) ** -55



def signed_minimum(costs, allowed, root_floor):
    """Keep both real Fourier coordinates for the asymmetric erased input."""
    b = len(costs)
    columns = []
    for j in allowed:
        factor = arb(1 if 2*j == b else 2)/b
        angles = [fmpq(2*r*j, b) for r in range(b)]
        columns.append([factor*arb.cos_pi_fmpq(t) for t in angles])
        if 2*j != b:
            columns.append([factor*arb.sin_pi_fmpq(t) for t in angles])
    rows = [list(row) for row in zip(*columns)]
    unit = arb(1)/b
    directions = rows+[rows[0]]
    bounds = [-unit]*b+[root_floor-unit]
    objective = [sum(x*c for x, c in zip(col, costs)) for col in columns]
    base = unit*sum(costs)

    def solve(slack):
        result = linprog(np.array(objective, dtype=float),
                         A_ub=-np.array(directions, dtype=float),
                         b_ub=-np.array(bounds, dtype=float)-slack,
                         bounds=[(-1, 1)]*len(columns), method="highs",
                         options={"primal_feasibility_tolerance": 1e-10,
                                  "dual_feasibility_tolerance": 1e-10})
        assert result.success
        return result

    def rounded(value):
        return arb(round(float(value)*10**12))/10**12

    candidate = [rounded(v) for v in solve(2e-10).x]
    assert all(sum(v*z for v, z in zip(row, candidate)) > lower
               for row, lower in zip(directions, bounds))
    upper = base+sum(v*z for v, z in zip(objective, candidate))
    dual = [rounded(max(0., -v)) for v in solve(0.).ineqlin.marginals]
    assert all(v >= 0 for v in dual)
    remainder = [c-sum(row[k]*v for row, v in zip(directions, dual))
                 for k, c in enumerate(objective)]
    lower = base+sum(t*v for t, v in zip(bounds, dual))-sum(map(abs, remainder))
    assert 0 < upper-lower < arb(1)/10**7
    return [enclose(lower)[0], enclose(upper)[1]]

def replay():
    p, n, m, horizon, sign = 769, 384, 8, 16, 1
    b = n // m
    root = arb(n).sqrt()
    signs = list(map(int, prior["paley_sign"](p)))
    column = apply([1] + [0] * (n-1), signs)
    lam = sum(column[::b])
    clique = [0, 1, 19, 30, 11, 29]
    assert all(signs[m*((i-j) % b)] == sign for i in clique for j in clique if i != j)
    spectrum = acb.dft([int(i in clique) for i in range(b)])
    weights = [(z.real*z.real+z.imag*z.imag)/(b*len(clique)) for z in spectrum]
    w = arb(1)/8
    equal(weights[0], w)
    equal(sum(weights), arb(1))
    q = [weights[i % b]/m for i in range(n)]
    for v, t in zip(apply(q, signs), q):
        equal(v, sign*(t-arb(1)/n))

    triangular = [arb(0)]*n
    signed_costs = [arb(0)]*b
    state = [arb(0)]*n
    weighted_a = weighted_mark = weighted_g = arb(0)
    flat_charge = erased_flat_charge = price_removed = arb(0)
    signed_original = signed_removed = weighted_leak = arb(0)
    signed_flat = signed_price_removed = erased_signed_flat = wrong_reserve = arb(0)
    for j in range(horizon):
        omega = arb(2*(horizon-1-j))/(horizon*(horizon-1))
        amplitude = list(map(abs, state))
        a = sum(amplitude[::b])/m
        ext = [v if i % b else arb(0) for i, v in enumerate(amplitude)]
        f = sign*sum(apply(ext, signs)[::b])/m
        e = sum(qi*v for qi, v in zip(q, ext))
        d = sign*sum(qi*v for i, (qi, v) in enumerate(zip(q, state)) if i % b)
        wrong_reserve += omega*(e-d)
        signed_flat += d/horizon
        at_flat = 2+2*j
        for r in range(1, b):
            block_total = sum(state[r::b])
            if r == at_flat % b:
                block_total -= state[at_flat]
            signed_costs[r] += sign*block_total/(m*horizon)
        signed_price_removed += sign*q[at_flat]*state[at_flat]/horizon
        erased_signed_flat += (d-sign*q[at_flat]*state[at_flat])/horizon
        source = amplitude.copy()
        source[0] = (4*n+state[0]**2).sqrt()
        beta = (source[0]-amplitude[0])/root
        g = sum(source)/(2*n)
        state = apply(source, signs)
        d_next = sign*sum(qi*v for i, (qi, v) in enumerate(zip(q, state)) if i % b)
        equal(w*f, w*(1-sign*lam)*(a+beta*root/m)+e-d_next-2*g)

        # Independent single-coordinate erasures; both avoid the original subgroup.
        at_triangle = 1+2*j
        assert at_triangle % b and at_flat % b
        ext[at_triangle] = arb(0)
        triangular = [total+omega*v for total, v in zip(triangular, ext)]
        removed_multiplier = sum(column[(i-at_triangle) % n] for i in range(0, n, b))/m
        signed_removed += sign*omega*amplitude[at_triangle]*removed_multiplier
        price_removed += q[at_flat]*amplitude[at_flat]/horizon
        erased_flat_charge += (e-q[at_flat]*amplitude[at_flat])/horizon
        weighted_leak += omega*(e-d_next)
        flat_charge += e/horizon
        signed_original += omega*f
        weighted_g += omega*g
        weighted_a += omega*a
        weighted_mark += omega*beta*root/m

    signed_triangle = sign*sum(apply(triangular, signs)[::b])/m
    equal(signed_triangle, signed_original-signed_removed)
    equal(flat_charge-erased_flat_charge, price_removed)
    equal(signed_flat-erased_signed_flat, signed_price_removed)
    equal(sum(v*c for v, c in zip(weights, signed_costs)), erased_signed_flat)
    allowed = [j for j in range(1, b//2+1) if signs[m*j] == sign]
    minimum = signed_minimum(signed_costs, allowed, w)
    equal(weighted_leak, wrong_reserve-2*signed_flat/(horizon-1))
    assert wrong_reserve > 0 and erased_signed_flat < erased_flat_charge
    equal(w*signed_original, w*(1-sign*lam)*(weighted_a+weighted_mark)
          +weighted_leak-2*weighted_g)
    assert weighted_leak > -2*flat_charge/(horizon-1)
    assert 2*weighted_g < 4
    lhs = signed_original+2*flat_charge/(w*(horizon-1))
    rhs = (1-sign*lam)*weighted_a-4/w
    assert lhs > rhs
    transformed = acb.dft(triangular)[::m]
    equal(sum(transformed), acb(0))
    equal(signed_triangle, sign*sum(z*s for z, s in zip(transformed, signs[::m]))/n)
    opposite_fiber = sum(z for z, s in zip(transformed, signs[::m]) if s == -sign)
    equal(signed_triangle, (-2*opposite_fiber-transformed[0])/n)
    return dict(prime=p, group_order=n, block_order=m, horizon=horizon, sign=sign,
                clique=clique, root_mass="1/8", precision_bits=ctx.prec, units="1e-9",
                block_signed_row_sum=enclose(lam), triangular_internal=enclose(weighted_a),
                original_signed_triangular_exterior=enclose(signed_original),
                eroded_signed_triangular_exterior=enclose(signed_triangle),
                original_flat_quotient_exterior=enclose(flat_charge),
                eroded_flat_quotient_exterior=enclose(erased_flat_charge),
                eroded_signed_flat_quotient=enclose(erased_signed_flat),
                triangular_exterior_wrong_reserve=enclose(wrong_reserve),
                minimum_eroded_signed_flat_quotient=minimum,
                erased_normalized_opposite_fiber=enclose(opposite_fiber.real/n),
                exterior_wrong_sign_summation_slack=enclose(weighted_leak+2*flat_charge/(horizon-1)),
                finite_unerased_left=enclose(lhs), finite_unerased_lower=enclose(rhs))


if __name__ == "__main__":
    print(json.dumps(replay(), sort_keys=True))
