"""Check the real weighted phase reflection on the genuine prime-173 ray."""

from fractions import Fraction
import json
from pathlib import Path
import runpy

from flint import acb, acb_mat, arb, arb_mat
import numpy as np


phase = runpy.run_path(str(Path(__file__).with_name("astra-phase-86-check.py")))
branch = phase["src"]
n, size = branch["n"], branch["N"]
x, rat = phase["x"], branch["rat"]
mult = [1] + [2] * (size - 2) + [1]
scales = [arb(m).sqrt() for m in mult]
identity = arb_mat([[int(i == j) for j in range(size)] for i in range(size)])
constants = arb_mat([[a * b / n for b in scales] for a in scales])
even_kernel = arb_mat([[scales[i] * branch["Kr"][i, j] / scales[j]
                        for j in range(size)] for i in range(size)])


def make_basis(sign):
    labels = [k for k in range(1, size) if branch["sign"][k] == sign]
    basis = [[s * ((1 if k == n//2 else 2) / arb(n)).sqrt()
              * (2 * arb.pi() * k * i / n).cos() for k in labels]
             for i, s in enumerate(scales)]
    matrix = arb_mat(basis)
    assert all(z.contains(0) for z in (even_kernel * matrix - sign * matrix).entries())
    return basis


plus_basis = make_basis(1)
minus_basis = make_basis(-1)


def preconditioned_inverse(matrix, real=False):
    dimension = matrix.nrows()
    convert = float if real else complex
    dtype = arb_mat if real else acb_mat
    enclosure = (lambda z: arb(float(z))) if real else branch["ac"]
    approximation = np.array([[convert(matrix[i, j]) for j in range(dimension)]
                               for i in range(dimension)])
    inverse = np.linalg.inv(approximation)
    preconditioner = dtype([[enclosure(z) for z in row] for row in inverse])
    unit = dtype([[int(i == j) for j in range(dimension)] for i in range(dimension)])
    error = branch["matnorm"](unit - preconditioner * matrix)
    assert error < rat("0.01"), (dimension, error)
    radius = (error * branch["matnorm"](preconditioner) / (1 - error)).upper()
    entry = arb(0, radius) if real else acb(arb(0, radius), arb(0, radius))
    return preconditioner + dtype([[entry for _ in range(dimension)]
                                  for _ in range(dimension)])


def weighted_projection(basis, scale):
    center = [a.mid() for a in scale]
    columns = arb_mat([[a * coefficient for coefficient in row]
                       for a, row in zip(center, basis)])
    adjoint = columns.transpose()
    projection = columns * preconditioned_inverse(adjoint * columns, real=True) * adjoint
    # Along the log-diagonal interpolation the projector derivative has
    # operator norm at most the sup norm of the log multiplier.
    error = max(abs((a / c).log()).upper() for a, c in zip(scale, center))
    enclosure = arb(0, error)
    return projection + arb_mat([[enclosure] * size for _ in range(size)])


def operator_norm_upper(matrix):
    if matrix.nrows() == 0 or matrix.ncols() == 0:
        return arb(0)
    approximation = np.array([[complex(matrix[i, j]) for j in range(matrix.ncols())]
                               for i in range(matrix.nrows())])
    proposal = arb(float(np.linalg.norm(approximation, ord=2))) + rat("0.001")
    gram = matrix.conjugate().transpose() * matrix
    identity = acb_mat([[int(i == j) for j in range(gram.ncols())]
                        for i in range(gram.nrows())])
    positive = proposal**2 * identity - gram
    floating = np.array([[complex(positive[i, j]) for j in range(positive.ncols())]
                         for i in range(positive.nrows())])
    inverse = np.linalg.inv(np.linalg.cholesky(floating))
    preconditioner = acb_mat([[branch["ac"](z) for z in row] for row in inverse])
    error = branch["matnorm"](
        identity - preconditioner * positive * preconditioner.conjugate().transpose()
    )
    assert error < rat("0.01")
    return proposal


def deviation(matrix, center):
    return sum((abs(x).upper()**2 for x in (matrix - center).entries()),
               arb(0)).sqrt().upper()


def block_midpoint(matrix):
    # Inverse operator norms are at most one for both the exact block
    # and this symmetric midpoint of its imaginary part.
    return acb_mat([[acb(int(i == j), (matrix[i, j].imag.mid()
                                      + matrix[j, i].imag.mid()) / 2)
                     for j in range(matrix.ncols())] for i in range(matrix.nrows())])


def evaluate(y, spectrum, difference):
    t = acb(rat(x), rat(y))
    scale = (t / n).sqrt()
    a = [(s + d) / (2 * scale) for s, d in zip(spectrum, difference)]
    b = [(s - d) / (2 * scale) for s, d in zip(spectrum, difference)]
    assert all(z.real > 0 for z in a + b)
    w = [z.real * u.real for z, u in zip(a, b)]
    diagonal = [(u.real / z.real).sqrt() for z, u in zip(a, b)]
    J = weighted_projection(plus_basis, diagonal) - weighted_projection(
        minus_basis, [1 / d for d in diagonal])
    ν = arb_mat(size, 1, [s * weight.sqrt() for s, weight in zip(scales, w)])
    norm_error = J * J - identity + ν * ν.transpose() / sum(m * h for m, h in zip(mult, w))
    assert all(z.contains(0) for z in norm_error.entries())

    angles_a = [z.imag / z.real for z in a]
    angles_b = [z.imag / z.real for z in b]
    average = [(z + u) / 2 for z, u in zip(angles_a, angles_b)]
    tangent = [(z - u) / 2 for z, u in zip(angles_a, angles_b)]
    marked_weight = n / t
    column_scale = marked_weight.imag / (2 * w[0].sqrt())
    for i in range(size):
        column = J[i, 0] / scales[i]
        assert (w[i].sqrt() * tangent[i] - column_scale * column).contains(0)
        if i:
            assert (w[i] - 1 + (column_scale * column)**2).contains(0)
        else:
            assert (w[i] * (1 + tangent[i]**2 - average[i]**2) - marked_weight.real).contains(0)

    positive = [i for i, entry in enumerate(tangent) if entry > 0]
    negative = [i for i, entry in enumerate(tangent) if entry < 0]
    assert len(positive) + len(negative) == size
    roots = [abs(d).sqrt() for d in tangent]

    def block(rows, columns):
        return acb_mat([[acb(roots[i] * J[i, j] * roots[j]) for j in columns]
                        for i in rows])

    cross = block(positive, negative)
    bplus = -acb(0, 1) * block(positive, positive)
    bminus = acb(0, 1) * block(negative, negative)
    for matrix, indices in [(bplus, positive), (bminus, negative)]:
        for j, site in enumerate(indices):
            correction = average[site] if site == 0 else arb(0)
            matrix[j, j] += acb(1, correction)
    cross_mid = acb_mat([[acb(cross[i, j].real.mid()) for j in range(cross.ncols())]
                        for i in range(cross.nrows())])
    plus_mid, minus_mid = block_midpoint(bplus), block_midpoint(bminus)
    schur_mid = (preconditioned_inverse(minus_mid) * cross_mid.transpose()
                 * preconditioned_inverse(plus_mid) * cross_mid)
    cross_error = deviation(cross, cross_mid)
    cross_mid_norm = operator_norm_upper(cross_mid)
    raw_upper = (cross_mid_norm + cross_error).upper()
    # Use the resolvent identity and contractivity of the diagonal blocks
    # before carrying the interval widths through the four-factor product.
    schur_error = ((deviation(bplus, plus_mid) + deviation(bminus, minus_mid)) * raw_upper**2
                   + (raw_upper + cross_mid_norm) * cross_error)
    damped_upper = (operator_norm_upper(schur_mid) + schur_error).upper()
    print(json.dumps(dict(
        kind="physical_real_phase_projection", prime=173, real=str(x), imag=str(y),
        even_orbits=size, negative_orbits=len(negative),
        marked_reflection_entry=J[0, 0].str(8),
        min_real_bulk_weight=min(weight.lower() for weight in w[1:]).str(8),
        raw_cross_norm_upper=raw_upper.str(8),
        damped_schur_norm_upper=damped_upper.str(8),
        damped_certificate=bool(damped_upper < 1),
    ), sort_keys=True))


def main():
    weights = [arb(4)] + [4 * rat(x) / n] * (size - 1)
    u = branch["base"]["real_root"](branch["Kr"], branch["sign"], rat(x), weights)
    spectrum = [(entry * entry + weight).sqrt() for entry, weight in zip(u, weights)]
    seed = np.array([complex(float(a), 0) for a in spectrum])
    left = branch["anchor"](seed, (x, Fraction(0)))
    assert branch["vmax"]([acb(a) - b for a, b in zip(spectrum, left[0])]) < arb(2)**-40
    first, last = phase["first"], phase["last"]
    seed, left, _ = phase["walk"](Fraction(0), first, seed, left, "before")
    seed, left, _ = phase["walk"](first, last, seed, left, "crossing")
    seed, left, radius = phase["walk"](last, last, seed, left, "crossing")
    s, v, _ = phase["tube_data"](last, last, left, left, radius)
    evaluate(last, s, v)
    after = Fraction(11, 500)
    seed, left, _ = phase["walk"](last, after, seed, left, "after")
    seed, left, radius = phase["walk"](after, after, seed, left, "after")
    s, v, _ = phase["tube_data"](after, after, left, left, radius)
    evaluate(after, s, v)


if __name__ == "__main__":
    main()
