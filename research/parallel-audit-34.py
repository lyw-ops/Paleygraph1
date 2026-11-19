"""Independent exact elimination and Arb checks for the p17/q25 branches.

Writes only JSON to stdout. Uses the two actual small Paley multipliers.
No growing-prime continuation or complex growth bound is computed.
"""

from fractions import Fraction
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from flint import acb, arb, ctx, fmpz_mat, fmpz_mpoly_ctx, fmpz_poly
from square_control import square_field_sign
from theta import paley_sign


def emit(row):
    print(json.dumps(row, sort_keys=True), flush=True)


def cyclotomic_transform(a, b, k, n, minimal):
    """Exact DFT at a primitive nth root, coefficients a+b*sqrt(2).

    The second coefficient list is used only at n=8; there sqrt(2)
    equals z+z**7. All answers are polynomials modulo Phi_n.
    """
    first, second = [0]*n, [0]*n
    for i, value in enumerate(a):
        first[(i*k) % n] += value
    for i, value in enumerate(b):
        second[(i*k) % n] += value
    radical = fmpz_poly([0, 1, 0, 0, 0, 0, 0, 1]) if n == 8 else fmpz_poly([0])
    return (fmpz_poly(first)+radical*fmpz_poly(second)) % minimal


def check_templates():
    s17 = paley_sign(17).astype(int).tolist()
    s25 = square_field_sign(5).astype(int).tolist()
    assert s17 == [0, 1, -1, -1, 1, -1, -1, 1]
    assert s25 == [0, -1, 1, 1, -1, -1, 1, -1, -1, 1, 1, -1]
    phi8 = fmpz_poly([1, 0, 0, 0, 1])
    p17_basis = [([2, 0, 0, 0, -2, 0, 0, 0],
                  [0, 1, 0, -1, 0, -1, 0, 1], {1: 8, 7: 8}),
                 ([1, -1, 1, -1, 1, -1, 1, -1], [0]*8, {4: 8})]
    for a, b, expected in p17_basis:
        for k in range(8):
            assert cyclotomic_transform(a, b, k, 8, phi8) == expected.get(k, 0)
    emit({"kind": "exact_actual_sector_template", "q": 17, "side": 1,
          "multiplier": s17, "basis": ["cos(pi*i/4)", "(-1)^i"],
          "cyclotomic_remainders_checked": True})
    phi12 = fmpz_poly([1, 0, -1, 0, 1])
    C = [2, 0, 1, 0, -1, 0, -2, 0, -1, 0, 1, 0]
    D = [2, -1, -1, 2, -1, -1, 2, -1, -1, 2, -1, -1]
    for a, expected in [(C, {1: 6, 5: 6, 7: 6, 11: 6}),
                        (D, {4: 12, 8: 12})]:
        for k in range(12):
            assert cyclotomic_transform(a, [0]*12, k, 12, phi12) == expected.get(k, 0)
    assert all(s25[(5*k) % 12] == s25[k] for k in range(12))
    assert all(C[(5*k) % 12] == C[k] and D[(5*k) % 12] == D[k]
               for k in range(12))
    emit({"kind": "exact_actual_sector_template", "q": 25, "side": -1,
          "multiplier": s25, "extra_automorphism": 5,
          "basis_twice_cos4": D, "basis_cos1_plus_cos5": C,
          "cyclotomic_remainders_checked": True})
    return s17, s25


def univariate(poly):
    assert all(m[0] == 0 for m, c in poly.terms())
    values = {m[1]: int(c) for m, c in poly.terms()}
    return fmpz_poly([values.get(i, 0) for i in range(max(values)+1)])


def exact_case(order):
    C = fmpz_mpoly_ctx.get(["r", "tau"])
    r, tau = C.gens()
    if order == 17:
        Q = (4*tau**2*r**5+(-4*tau**2+32*tau)*r**4
             +(-21*tau**2-144*tau-64)*r**3
             +(-6*tau**2+32*tau+128)*r**2
             +(15*tau**2+144*tau-64)*r+8*tau**2-64*tau)
        L = 8-tau-(8+tau)*r
        N = r*((16+6*tau)-2*(8-tau)*r-4*tau*r*r)
        D = 4*L
        F = L*(2*N*N-r*r*D*D)-4*tau*r*(1-r*r)*D*D
        G = (16+6*tau)*N*N-8*tau*N*D-(8+7*tau)*r*r*D*D
        assert F == 8*r*L*Q
        assert G == 8*r*(3*tau+8)*Q
        factor = 2**18*tau**4
        target_res = -2**20*tau**2*(tau-8)*(3*tau+8)**2
        evals = [8*tau*(tau-8), -4*tau**2, C.constant(256)]
        # Selected core root through (tau,r)=(8,0).
        qr = Q.derivative("r").subs({"r": 0, "tau": 8})
        qt = Q.derivative("tau").subs({"r": 0, "tau": 8})
        assert qr == 2048 and qt == 64
        derivative_r = Fraction(-64, 2048)
        # Along this branch the numerator and denominator both have derivative -2.
        assert N.derivative("r").subs({"r": 0, "tau": 8}) == 64
        assert N.derivative("tau").subs({"r": 0, "tau": 8}) == 0
        assert D.derivative("r").subs({"r": 0, "tau": 8}) == -64
        assert D.derivative("tau").subs({"r": 0, "tau": 8}) == -4
        assert 64*derivative_r == -2 and -64*derivative_r-4 == -2
    else:
        Q = ((5*tau**2+12*tau)*r**5+(-4*tau**2+36*tau+144)*r**4
             +(-34*tau**2-384*tau-864)*r**3
             +(-20*tau**2+144*tau+1152)*r**2
             +(21*tau**2+360*tau-432)*r+16*tau**2-192*tau)
        L = 12-tau-(12+tau)*r
        N = -r*L-8*tau*(1-r*r)
        D = r*L-3*(4+tau)*(1-r*r)
        F = L*(N*N-r*r*D*D)-4*tau*r*(1-r*r)*D*D
        G = (3*(4+tau)*N**3-8*tau*N*N*D
             -(12+7*tau)*r*r*N*D*D+4*tau*r*r*D**3)
        assert F == 4*tau*(r*r-1)*Q
        assert G == -4*tau*(11*tau+12)*r*(r*r-1)*Q
        factor = 2304*(11*tau+12)**4
        target_res = -1728*tau**2*(tau+4)*(11*tau+12)**4
        evals = [16*tau*(tau-12), -8*tau*(2*tau+3), C.constant(2592)]
    assert Q.resultant(D, "r") == target_res
    for value, target in zip([0, 1, -1], evals):
        assert Q.subs({"r": value}) == target
    discriminant = Q.discriminant("r")
    H, remainder = divmod(discriminant, factor)
    assert not remainder
    h = univariate(H)
    assert h.degree() == 10 and h.leading_coefficient() > 0
    descending = [int(h[i]) for i in range(10, -1, -1)]
    hurwitz = [[descending[2*j-i+1] if 0 <= 2*j-i+1 <= 10 else 0
                for j in range(10)] for i in range(10)]
    minors = [int(fmpz_mat([row[:k] for row in hurwitz[:k]]).det())
              for k in range(1, 11)]
    assert all(x > 0 for x in minors)
    emit({"kind": "exact_discriminant_and_hurwitz", "q": order,
          "quintic": str(Q), "discriminant_factor": str(factor),
          "degree10_coefficients_ascending": [int(x) for x in h.coeffs()],
          "hurwitz_leading_minors": minors,
          "all_critical_parameter_values_in_open_left_half_plane": True})
    emit({"kind": "exact_reconstruction_identities", "q": order,
          "numerator": str(N), "denominator": str(D),
          "resultant_of_core_and_denominator": str(target_res),
          "homogenized_first_order_equations_divisible_by_core": True,
          "core_at_r_0_1_minus1": [str(x) for x in evals],
          "special_removable_parameter": 8 if order == 17 else None,
          "special_reconstruction_limit": 1 if order == 17 else None,
          "special_root_derivative": "-1/32" if order == 17 else None})
    roots = h.complex_roots()
    assert len(roots) == 10 and all(z.real.upper() < 0 for z, mult in roots)
    assert all(mult == 1 for z, mult in roots)
    emit({"kind": "validated_discriminant_roots", "q": order,
          "roots": [str(z) for z, mult in roots],
          "all_real_upper_bounds_negative": True})
    return Q


def validate_stationary(order, sign, Q, fraction):
    n, side = len(sign), 1 if order == 17 else -1
    tau = arb(fraction.numerator)/fraction.denominator
    rational_coefficients = []
    for degree in range(6):
        coefficients = {int(m[1]): int(c) for m, c in Q.terms() if m[0] == degree}
        rational_coefficients.append(sum(Fraction(c)*fraction**d
                                         for d, c in coefficients.items()))
    common = 1
    from math import lcm
    for x in rational_coefficients:
        common = lcm(common, x.denominator)
    poly = fmpz_poly([int(x*common) for x in rational_coefficients])
    accepted = []
    for root, mult in poly.complex_roots():
        if not root.imag.is_zero():
            continue
        rr = root.real
        if not (rr > -1 and rr < 1):
            continue
        if order == 17:
            LL = 8-tau-(8+tau)*rr
            if fraction == 8 and rr.is_zero():
                tt = arb(1)
            else:
                tt = rr*((16+6*tau)-2*(8-tau)*rr-4*tau*rr**2)/(4*LL)
            alpha = 2/(1+tt)
            radical = arb(2).sqrt()
            uu = [alpha*(1+rr), alpha*(tt+rr/radical), alpha,
                  alpha*(tt-rr/radical), alpha*(1-rr),
                  alpha*(tt-rr/radical), alpha, alpha*(tt+rr/radical)]
        else:
            LL = 12-tau-(12+tau)*rr
            tt = (-rr*LL-8*tau*(1-rr**2))/(rr*LL-3*(4+tau)*(1-rr**2))
            alpha = 3/(1+tt)
            uu = [alpha*(1+rr), alpha*tt/2, alpha*(tt+rr)/2,
                  alpha, alpha*(tt-rr)/2, alpha*tt/2,
                  alpha*(1-rr), alpha*tt/2, alpha*(tt-rr)/2,
                  alpha, alpha*(tt+rr)/2, alpha*tt/2]
        if all(x > 0 for x in uu):
            accepted.append((rr, tt, uu))
    assert len(accepted) == 1
    rr, tt, uu = accepted[0]
    W = 1+(n-1)*tau/n
    aa = (W/n).sqrt()
    A = [aa*x for x in uu]
    weights = [arb(1)]+[tau/n]*(n-1)
    B = [wi/ai for wi, ai in zip(weights, A)]
    phi = [x+y for x, y in zip(A, B)]
    transformed = acb.dft(phi)
    twice = acb.dft([int(s)*z for s, z in zip(sign, transformed)])
    residual = [z.real/n-side*(x-y) for z, x, y in zip(twice, A, B)]
    assert all(z.imag.contains(0) for z in twice)
    assert all(x.contains(0) for x in residual)
    mean_error = sum(B)/n-aa
    assert mean_error.contains(0)
    emit({"kind": "validated_actual_stationary_branch", "q": order,
          "side": side, "tau": str(fraction), "r_interval": str(rr),
          "t_interval": str(tt),
          "chosen_sector_root_log_interval": str(A[0].log()),
          "plus_sector_root_log_interval": str(side*A[0].log()),
          "all_spectra_positive": True,
          "fixed_point_residual_upper": str(max(abs(x).upper() for x in residual)),
          "mean_opposite_error_interval": str(mean_error),
          "scope": "one finite field; no common growing-prime bound"})


def main():
    ctx.prec = 192
    s17, s25 = check_templates()
    for order, sign in [(17, s17), (25, s25)]:
        Q = exact_case(order)
        for fraction in [Fraction(1, 20), Fraction(1), Fraction(len(sign)), Fraction(20)]:
            validate_stationary(order, sign, Q, fraction)
    emit({"kind": "all_checks_passed", "orders": [17, 25],
          "arithmetic": "exact integer polynomials, cyclotomic remainders, and Arb192"})


if __name__ == "__main__":
    main()
