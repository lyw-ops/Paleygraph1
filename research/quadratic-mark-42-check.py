"""Exact compact-probability checks for the quadratic marked bound."""

from json import dumps
from math import comb, factorial

from flint import fmpq, fmpq_mpoly_ctx


def arcsine_moment(j):
    return fmpq(0) if j % 2 else fmpq(comb(j, j//2), 2**j)


def semicircle_moment(j):
    return arcsine_moment(j) / (j//2+1)


def expectation(poly, moments):
    return sum(coeff*moments[0][exponents[0]]*moments[1][exponents[1]]
               for exponents, coeff in poly.terms())


def square_root_bounds(poly, radius, degree, moments, extra_x=False):
    """Bound sqrt(poly) on [0, radius**2] with rational polynomials."""
    shift = 1 - poly/radius**2
    power = shift*0+1
    c = fmpq(1, 2)
    tail = fmpq(1)
    upper = fmpq(1)
    upper_x = fmpq(0)
    x = fmpq_mpoly_ctx.get(["x", "y"]).gens()[0]
    for j in range(1, degree+1):
        power *= shift
        moment = expectation(power, moments)
        upper -= c*moment
        if extra_x:
            upper_x -= c*expectation(x*power, moments)
        tail -= c
        c *= fmpq(2*j-1, 2*j+2)
    return radius*(upper-tail*moment), radius*upper, radius*upper_x


def check_quadratic_bound(x, y, moments):
    a, c = fmpq(19, 20), fmpq(143, 200)
    b, d = fmpq(1, 20), fmpq(9, 100)
    t2 = 2*x*x - 1
    f, g = 1-a*x+b*(t2-y), 1+c*x+d*(t2+y)
    lower, upper, _ = square_root_bounds(f*g, fmpq(5, 4), 60, moments)
    assert lower > fmpq(39713, 50000)
    assert upper < fmpq(79435, 100000)
    boundary = fmpq(22731, 20000)
    lhs = (1-a*boundary/2)*(1-c/(2*boundary))
    assert lhs < fmpq(39713, 50000)**2/2
    assert sum(fmpq(16, 125)**j/factorial(j) for j in range(5)) > boundary
    print(dumps(dict(kind="quadratic_reciprocal_exclusion", degree=60,
                     integral_lower="39713/50000", integral_upper="79435/100000",
                     exponential_threshold=str(boundary), lhs=str(lhs),
                     log_threshold_upper="16/125"), sort_keys=True))


def check_affine_model(x, moments):
    u = fmpq(57, 50)
    v = (u+1/u)*x+fmpq(59, 100)*(2*x*x-1)+fmpq(2, 5)*(4*x*x*x-3*x)
    lower, upper, upper_x = square_root_bounds(
        fmpq(1, 2)+v*v/4, fmpq(7, 4), 60, moments, extra_x=True)
    gap = upper-lower
    a_lower = 1-upper
    c_middle = (u-1/u)/2-2*upper_x
    c_bound = abs(c_middle)+2*gap
    assert a_lower > fmpq(9, 10000)
    assert c_bound < fmpq(1, 5000)
    assert u > fmpq(22731, 20000)
    print(dumps(dict(kind="affine_only_reciprocal_model", degree=60,
                     exponential_mark=str(u), correction_constant_lower="9/10000",
                     correction_slope_absolute_upper="1/5000"), sort_keys=True))


def check_joint_cold_bound(x, y, two_semicircles):
    b, d = fmpq(41, 50), fmpq(11, 100)
    g = 1+b*x+d*(2*x*x-1+y)
    weighted_arcsine = [
        sum(fmpq(comb(j, l)*2**l*(-1)**(j-l), 2*l+1) for l in range(j+1))
        for j in range(161)
    ]
    lower, _, _ = square_root_bounds(
        g, fmpq(3, 2), 80, (weighted_arcsine, two_semicircles))
    rational_lower = fmpq(80747, 100000)
    assert lower > rational_lower
    assert 1-8*rational_lower**2/(fmpq(22, 7)**2*(1-b/2)) < fmpq(21, 200)
    print(dumps(dict(kind="moving_cold_floor_bound", degree=80,
                     weighted_integral_lower=str(rational_lower),
                     pi_upper="22/7", normalized_mark_loss_upper="21/200"),
                sort_keys=True))


if __name__ == "__main__":
    x, y = fmpq_mpoly_ctx.get(["x", "y"]).gens()
    arcsine = [arcsine_moment(j) for j in range(362)]
    semicircle = [semicircle_moment(j) for j in range(121)]
    two_semicircles = [
        sum(comb(j, l)*semicircle[l]*semicircle[j-l] for l in range(j+1))
        for j in range(len(semicircle))
    ]
    moments = arcsine, two_semicircles
    check_quadratic_bound(x, y, moments)
    check_affine_model(x, moments)
    check_joint_cold_bound(x, y, two_semicircles)
