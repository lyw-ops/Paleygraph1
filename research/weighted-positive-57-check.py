"""Interval check for transferring the leading fourth increment separately."""
import json
from pathlib import Path
import runpy

from flint import arb, ctx

centered = runpy.run_path(str(Path(__file__).with_name("centered-positive-56-check.py")))
nested = centered["nested"]
histogram = centered["histogram"]
warm = centered["warm"]
SEED = centered["SEED"]
activation = centered["activation"]
W_RADIUS = arb(8)
U_RADIUS = 23 / arb(2).sqrt()
Z_RADIUS = centered["Z_RADIUS"]


def cap_a2(a_max, a_var):
    a_min = a_max - 2*a_var
    return (a_max*a_max + a_min*a_min)/2


def second_projection(t, b, variance, tail, first_shift, truncation):
    coef, linear_rms, a_max, a_var, m3, activation_variance = centered["expansion_constants"](t)
    square_rms = (3*variance**2 - b**4/8).sqrt()
    odd_variance = b*b*linear_rms**2/2 + activation_variance*tail**2
    even_variance = cap_a2(a_max, a_var)*(2*variance**2-b**4/8) + (variance*a_var)**2
    remainder = m3*first_shift*square_rms/6
    return 2*b*coef, ((odd_variance + even_variance).sqrt() + remainder + truncation).upper()


def third_projection(t, b, variance, tail, lam, eps, first, first_shift, second_shift, truncation):
    coef, linear_rms, a_max, a_var, m3, _ = centered["expansion_constants"](t)
    midpoint = first + (second_shift + lam*Z_RADIUS)/2
    replacement = midpoint*eps/activation(t, midpoint)
    joint_variance = lam*lam*linear_rms**2/2
    joint_variance += cap_a2(a_max, a_var)*(b*b*lam*lam + lam**4/2)
    joint_variance += lam**3*linear_rms*a_max/4
    centering = lam*lam*a_var/2 + 2*lam*a_max*Z_RADIUS*tail
    gz2 = b*(arb(3)/8).sqrt() + Z_RADIUS**2*tail
    g2z = b*b*arb(5).sqrt()/4 + (first_shift+2*b)*Z_RADIUS*tail
    g2z = min(g2z.upper(), (Z_RADIUS*(3*variance**2-b**4/8).sqrt()).upper())
    z3 = Z_RADIUS*(arb(3)/4).sqrt()
    remainder = m3*lam*(g2z + lam*gz2 + lam*lam*z3/3)/2
    return 2*lam*coef, (replacement + joint_variance.sqrt() + centering
                        + remainder + truncation).upper()


def fourth_projection(t, b, tail, lam, eps, nu, xi, second, third_shift, truncation):
    coef, linear_rms, a_max, a_var, m3, _ = centered["expansion_constants"](t)
    midpoint = second + (third_shift + nu * W_RADIUS) / 2
    replacement = midpoint * xi / activation(t, midpoint)
    replacement += nu * W_RADIUS * (tail + eps) / (2 * t.sqrt())
    a2 = (b*b + lam*lam) / 2
    a4 = 5*b**4/8 + 3*b*b*lam*lam/2 + 3*lam**4/4
    projection = nu / arb(2).sqrt() * ((linear_rms**2 + 4*cap_a2(a_max, a_var)*a2).sqrt()
                                      + m3*a4.sqrt()/2)
    projection += nu*nu * a_max * arb(49).sqrt()/8
    return 2*nu*coef, (replacement + projection + truncation).upper()


def transfer(t, b, tail, lam, eps, nu, xi, mu, zeta, radius, shift, truncation):
    pair_radius = 2*radius + shift
    ideal = t - pair_radius*shift/4
    product = ideal - truncation
    lead_shift = mu * U_RADIUS
    lead_product = t - (2*radius + lead_shift)*lead_shift/4
    assert product > 0 and lead_product > 0
    momentum = 4 + (b*b + lam*lam + nu*nu)/2
    principal = mu * (2*momentum + 3*mu*mu/4).sqrt()
    principal += 2*mu*U_RADIUS*(tail + eps + xi)
    distance = principal / (4*(t.sqrt() + lead_product.sqrt()))
    distance += (pair_radius + lead_shift)*zeta / (4*(ideal.sqrt() + lead_product.sqrt()))
    distance += truncation / (ideal.sqrt() + product.sqrt())
    norm = (t.sqrt() + distance).upper()
    return (distance * norm / (1 + norm*norm).sqrt()).upper(), product.lower()


def trial(t, center=12, order=8):
    center = arb(center)
    modes = histogram["centered_modes"](t, center, order)
    envelope = [[abs(value).upper() for value in row] for row in modes]
    variance = sum(entry**2 for entry in envelope[0][1:]) / 2
    tail = (sum(entry**2 for entry in envelope[0][4:]) / 2).sqrt()
    b = modes[0][2]
    assert b > 0
    radii = [arb(0)] * (histogram["N"] + 2)
    former_error = arb(0)
    for step in range(1, 5):
        core = sum(k*value for k,value in enumerate(radii[:-2], 1))
        radius = (SEED + core + radii[-2]).upper()
        radii, _, _ = histogram["histogram_step"](envelope, radii, arb(1))
        total = sum(k*value for k,value in enumerate(radii[:-2], 1)) + radii[-2]
        shift = (total - core).upper()
        err = nested["remainder"](t, center, order, radius)
        if step == 1:
            first_shift = shift
        elif step == 2:
            first, second_shift = radius, shift
            lam, eps = second_projection(t, b, variance, tail, first_shift, former_error + err)
        elif step == 3:
            second, third_shift = radius, shift
            nu, xi = third_projection(t, b, variance, tail, lam, eps, first,
                                      first_shift, second_shift, former_error + err)
        elif step == 4:
            mu, zeta = fourth_projection(t, b, tail, lam, eps, nu, xi, second,
                                         third_shift, former_error + err)
        former_error = err
    assert 2*t.sqrt() > err
    truncation = (2*activation(t, radius) + err)*err/4
    return transfer(t, b, tail, lam, eps, nu, xi, mu, zeta, radius, shift, truncation)


def certify(first, last, divisions, cap, product_floor):
    for k in range(first, last):
        mark, product = trial(warm.slab(k, divisions))
        assert mark < cap and product > product_floor, (k, mark, product)
    print(json.dumps(dict(kind="weighted_fourth_increment", slab_indices=[first, last],
                          divisions=divisions, mark_cap=str(cap), product_floor=str(product_floor)),
                     sort_keys=True))


if __name__ == "__main__":
    ctx.prec = 192
    certify(31*2048, 25*2560, 10240, arb(1699)/100000, arb(13)/200)
    certify(25*128, 207*16, 512, arb(149)/10000, arb(33)/100)
