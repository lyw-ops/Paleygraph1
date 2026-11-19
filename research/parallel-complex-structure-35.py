"""Round 35 exact/interval checks for the structural complex-path note.

Uses the already accepted p13 equation, not a new field elimination.
No floating branch tracking and no asymptotic claim from finite samples.
"""

import json
from flint import arb, ctx, fmpq, fmpq_mat, fmpq_poly


def emit(**row):
    print(json.dumps(row, sort_keys=True), flush=True)


def pick_obstructions():
    h = fmpq_poly([0, 1])
    tau = 6 + h
    x = fmpq_poly([])
    order = 6
    for j in range(1, order):
        residual = ((6 + 5*tau)*x**3 + (tau - 6)*x**2
                    - (24 + 8*tau)*x + 24 - 4*tau)
        x += residual[j] / 72 * h**j
    residual = ((6 + 5*tau)*x**3 + (tau - 6)*x**2
                - (24 + 8*tau)*x + 24 - 4*tau)
    assert all(residual[j] == 0 for j in range(order))
    m = fmpq_poly([])
    root = fmpq_poly([1])
    coefficient = fmpq(1)
    for j in range(1, order):
        m += (-1)**(j+1) * (x**j + (5*h/36)**j / 2) / j
        coefficient *= fmpq(3 - 2*j, 2*j)
        root += coefficient * (5*h/36)**j
    marked = root * (1 + x)
    square_residual = marked**2 - (1+5*h/36)*(1+x)**2
    log_derivative_residual = marked.derivative() - marked*m.derivative()
    assert all(square_residual[j] == 0 for j in range(order))
    assert all(log_derivative_residual[j] == 0 for j in range(order-1))
    for name, series in [('marked_log', m), ('marked_spectrum', marked),
                         ('negative_normalized_spectrum', -x)]:
        H = fmpq_mat([[series[i+j+1] for j in range(3)]
                     for i in range(3)])
        H2 = fmpq_mat([[series[i+j+1] for j in range(2)]
                      for i in range(2)])
        b = fmpq_mat([[series[3]], [series[4]]])
        head = -H2.inv() * b
        witness = fmpq_mat([[head[0, 0]], [head[1, 0]], [1]])
        quadratic = (witness.transpose() * H * witness)[0, 0]
        assert series[1] > 0 and H2.det() > 0 and H.det() < 0
        assert quadratic < 0 and quadratic == H.det()/H2.det()
        emit(kind='exact_actual_p13_Pick_obstruction', quantity=name,
             center=6, coefficients_1_through_5=[str(series[i]) for i in range(1, 6)],
             hankel_2_determinant=str(H2.det()), hankel_3_determinant=str(H.det()),
             negative_quadratic_witness=[str(witness[i, 0]) for i in range(3)],
             quadratic_value=str(quadratic),
             scope='excludes global upper-half-plane Pick extension of this actual germ')
    emit(kind='exact_actual_p13_jet_identity', residual_coefficients_0_through_5_zero=True,
         marked_square_identity_through_degree_5=True,
         log_derivative_identity_through_degree_4=True,
         x_coefficients_1_through_5=[str(x[i]) for i in range(1, 6)],
         implicit_derivative_at_base='-72')


def constants():
    ctx.prec = 192
    N, R = arb(1024), arb(6)
    z = arb(9)/1024
    b_correction = 2*R**2/(N*(2 + (4-R**2/N).sqrt()))
    b_lipschitz = 2*R/(N*(4-R**2/N).sqrt())
    S2 = z*(2-z)/((1-z)*(1-z).sqrt())
    S3 = z*(4-2*z+z*z)/((1-z)**2*(1-z).sqrt())
    image_bound = (2+b_correction)*(2+1/N).sqrt() + 4*N.sqrt()*S2
    lipschitz_bound = (b_lipschitz*(2+1/N).sqrt()
                       + 4*N.sqrt()/R*S3)
    assert image_bound < arb(513)/100
    assert lipschitz_bound < arb(78)/100
    assert image_bound < 6 and lipschitz_bound < 1
    emit(kind='validated_uniform_hot_complex_contraction', minimum_n_and_modulus=1024,
         radius=6, image_norm_bound=str(image_bound), lipschitz_bound=str(lipschitz_bound),
         rational_upper_bounds=['513/100', '78/100'],
         scope='uniform constants; proof uses the inherited mixed-product Mellin norm inequality')
    rho, delta = fmpq(1, 8), fmpq(1, 32)
    contraction = (1+delta)/(1-rho)**2-1
    selfmap_ratio = fmpq(1, 4) + contraction
    assert contraction == fmpq(17, 49) and selfmap_ratio == fmpq(117, 196)
    assert selfmap_ratio < 1
    emit(kind='exact_general_barrier_local_constants', coordinate_radius=str(rho),
         parameter_radius_coefficient=str(delta), contraction=str(contraction),
         selfmap_ratio=str(selfmap_ratio),
         scope='dimension-dependent disk; not a common cold domain')


if __name__ == '__main__':
    pick_obstructions()
    constants()
    emit(kind='all_checks_passed', substantive_records=6)
