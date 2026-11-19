"""Exact p=13 central-path discriminant and Arb stationary normalization.

No asymptotic prime estimate is computed. The continuation criterion in
the matching note remains conditional. Uses integer polynomial arithmetic
and validated root isolation; no optimizer or Newton solve.
"""

from fractions import Fraction
import json
from flint import arb, ctx, fmpz_poly


def emit(row):
    print(json.dumps(row, sort_keys=True), flush=True)


def main():
    ctx.prec = 192
    t = fmpz_poly([0, 1])
    a, b, c, d = 6+5*t, t-6, -24-8*t, 24-4*t
    disc = b*b*c*c-4*a*c**3-4*b**3*d-27*a*a*d*d+18*a*b*c*d
    target = fmpz_poly([1944,1728,2754,1926,25])
    assert disc == 96*target
    delta2 = 1926*2754-25*1728
    delta3 = delta2*1728-1926**2*1944
    deltas = [1926,delta2,delta3,1944*delta3]
    assert min(deltas) > 0
    first_column = [Fraction(25),Fraction(1926),Fraction(delta2,1926),
                    Fraction(delta3,delta2),Fraction(1944)]
    emit({"kind":"exact_discriminant_hurwitz", "p":13,
          "cubic_coefficients_in_x_ascending":[str(d),str(c),str(b),str(a)],
          "discriminant_coefficients_ascending":[int(x) for x in disc.coeffs()],
          "hurwitz_determinants":deltas,
          "routh_first_column":[str(x) for x in first_column],
          "all_critical_parameter_values_in_open_left_half_plane":True})
    roots = target.complex_roots()
    assert len(roots) == 4 and all(z.real.upper() < 0 for z,mult in roots)
    emit({"kind":"validated_discriminant_roots", "roots":[str(z) for z,mult in roots],
          "all_real_upper_bounds_negative":True})
    for tau in [Fraction(1,20),Fraction(1,5),Fraction(1),Fraction(6),Fraction(20)]:
        numerator,denominator = tau.numerator,tau.denominator
        polynomial = fmpz_poly([24*denominator-4*numerator,
                               -24*denominator-8*numerator,
                               numerator-6*denominator,
                               6*denominator+5*numerator])
        candidates = [z.real for z,mult in polynomial.complex_roots()
                      if z.imag.is_zero() and z.real > -1 and z.real < 1]
        assert len(candidates) == 1
        x = candidates[0]
        parameter = arb(numerator)/denominator
        average = ((1+5*parameter/6)/6).sqrt()
        u = [1+x,1+x/2,1-x/2,1-x,1-x/2,1+x/2]
        assert all(value > 0 for value in u)
        A = [average*value for value in u]
        weights = [arb(1)]+[parameter/6]*5
        B = [w/value for w,value in zip(weights,A)]
        v,phi = [a-b for a,b in zip(A,B)],[a+b for a,b in zip(A,B)]
        kernel = [arb(value)/6 for value in [-1,3,-1,-3,-1,3]]
        residual = [sum(kernel[(i-j)%6]*phi[j] for j in range(6))-v[i]
                    for i in range(6)]
        assert all(value.contains(0) for value in residual)
        mean_B_error = sum(B)/6-average
        assert mean_B_error.contains(0)
        emit({"kind":"validated_p13_stationary_root", "tau":str(tau),
              "x_interval":str(x),"marked_log_interval":str(A[0].log()),
              "fixed_point_residual_upper":str(max(abs(value).upper() for value in residual)),
              "mean_B_error_interval":str(mean_B_error),
              "positive_spectra_certified":True,
              "scope":"one finite prime; no common prime-domain conclusion"})


if __name__ == '__main__':
    main()
