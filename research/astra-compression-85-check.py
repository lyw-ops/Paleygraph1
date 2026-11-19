"""Check the physical p=173 phase Schur test and the all-size strip constants."""
from fractions import Fraction
import json
from pathlib import Path
import runpy

import numpy as np
from flint import acb, arb, arb_mat, ctx


source = runpy.run_path(str(Path(__file__).with_name('astra-cold-37-monodromy.py')))
base = source['base']
ctx.prec = 128
rat = base['rat']


def encode(number):
    return number.str(14)


def checked_stationary_row():
    n = source['n']
    x, y = Fraction(1, 50), Fraction(7, 200)
    weights = [arb(4)] + [4 * rat(x) / n] * (source['N'] - 1)
    v = base['real_root'](source['Kr'], source['sign'], rat(x), weights)
    s = [(value**2 + weight).sqrt() for value, weight in zip(v, weights)]
    seed = np.array([complex(float(value), 0) for value in s])
    start, end = (x, Fraction(0)), (x, y)
    anchor = source['anchor'](seed, start)
    assert source['vmax']([acb(value) - a for value, a in zip(s, anchor[0])]) < arb(2)**-40
    segments = 0

    def walk(left_point, right_point, seed, left, depth=0):
        nonlocal segments
        assert depth < 25
        proposal = source['numeric_root'](seed, right_point)
        right = source['anchor'](proposal, right_point)
        certificate = source['tube'](seed, proposal, left, right)
        if certificate:
            radius, _ = certificate
            error = ((1 + source['knorm']) * radius / 2).upper()
            enlargement = acb(arb(0, error), arb(0, error))
            imaginary = rat(left_point[1]).union(rat(right_point[1]))
            bulk_scale = (acb(rat(x), imaginary) / n).sqrt()
            positive_lift = True
            for k in range(source['N']):
                first = (left[0][k] + left[1][k]) / 2
                last = (right[0][k] + right[1][k]) / 2
                chord = acb(first.real.union(last.real), first.imag.union(last.imag))
                factor = (chord + enlargement) / (1 if k == 0 else bulk_scale)
                if not factor.real > 0:
                    positive_lift = False
                    break
            if positive_lift:
                segments += 1
                return proposal, right, radius
        midpoint = source['half_point'](left_point, right_point)
        middle_seed, middle, _ = walk(left_point, midpoint, seed, left, depth + 1)
        return walk(midpoint, right_point, middle_seed, middle, depth + 1)

    seed, anchor, _ = walk(start, end, seed, anchor)
    seed, anchor, radius = walk(end, end, seed, anchor)
    s, v = anchor[:2]
    # Both coordinates of a complex ball of absolute radius r have radius at most r.
    error = ((1 + source['knorm']) * radius / 2).upper()
    factor_error = acb(arb(0, error), arb(0, error))
    t = acb(rat(x), rat(y))
    logs = []
    for j in range(n):
        k = min(j, n - j)
        numerator = (s[k] + v[k]) / 2 + factor_error
        normalized = numerator if k == 0 else numerator / (t / n).sqrt()
        assert normalized.real > 0
        logs.append(normalized.log())
    return t, logs, segments


def schur_record():
    t, logs, segments = checked_stationary_row()
    n = len(logs)
    phi = [z.imag for z in logs]
    tangent = [angle.tan() for angle in phi]
    positive = [j for j, value in enumerate(tangent) if value > 0]
    negative = [j for j, value in enumerate(tangent) if value < 0]
    assert len(positive) + len(negative) == n
    real_diagonal = [z.real.tanh() for z in logs]
    scale = [1 / z.real.cosh() for z in logs]
    kernel = acb.dft([int(s) for s in source['sign']], inverse=True)
    assert all(z.imag.contains(0) for z in kernel)
    K = arb_mat([[kernel[(i-j) % n].real for j in range(n)] for i in range(n)])
    system = arb_mat([[int(i == j) - K[i,j] * real_diagonal[j] for j in range(n)] for i in range(n)])
    X = system.solve(K)
    R = arb_mat([[scale[i] * X[i,j] * scale[j] - (real_diagonal[i] if i == j else 0)
                  for j in range(n)] for i in range(n)])
    def block(left, right):
        return arb_mat([[abs(tangent[i]).sqrt() * R[i,j] * abs(tangent[j]).sqrt()
                         for j in right] for i in left])
    A = block(positive, positive)
    C = block(positive, negative)
    eye = arb_mat([[int(i == j) for j in positive] for i in positive])
    damped = C.transpose() * (eye + A*A).solve(C)
    trace = sum(damped[j,j] for j in range(len(negative)))
    assert trace > rat('7496/10000') and trace < rat('7497/10000')
    # A floating vector only proposes a rational witness against the raw cross norm.
    flat = np.array([[float(C[i,j].mid()) for j in range(C.ncols())] for i in range(C.nrows())])
    trial = np.linalg.svd(flat, full_matrices=False)[2][0]
    q = arb_mat(C.ncols(), 1, [int(np.rint(100000 * entry)) for entry in trial])
    v = C*q
    ratio = ((v.transpose()*v)[0,0] / (q.transpose()*q)[0,0]).sqrt()
    assert ratio > rat('1408/1000')
    phi_min = min(phi, key=lambda value:float(value.mid()))
    phi_max = max(phi, key=lambda value:float(value.mid()))
    # The two even copies can coincide. Check the bounds against every coordinate.
    assert all(angle > rat('-848/1000') and angle < rat('1502/1000') for angle in phi)
    assert phi_min < rat('-847/1000') and phi_max > rat('1501/1000')
    budget = sum((n if j == 0 else abs(t)) * angle.sin()**2 for j, angle in enumerate(phi))
    total = (n + (n-1)*abs(t) - abs(n + (n-1)*t))/2
    assert budget.overlaps(total)
    return dict(kind='actual_stationary_cross_sign_schur', prime=173, working_precision=ctx.prec,
                real='1/50', imag='7/200', validated_segments=segments, all_lifted_phases_in_open_half_plane=True,
                phase_min_example=encode(phi_min), phase_max_example=encode(phi_max),
                positive_sites=len(positive), negative_sites=len(negative), raw_witness_gain=encode(ratio),
                damped_trace=encode(trace), angular_budget=encode(total))


def constants():
    x = rat('2031/128') - arb(2)**-17
    threshold = 2*x*(1+x).sqrt()
    assert threshold > 130
    # |U-X| at a site with |tan phi|>1/3 in the enlarged forcing sector.
    angle = (arb(1)/3).atan()
    outer = (arb(3)/2).atan()
    start = rat('26/100')
    jump = 4 * x.sqrt() * ((outer+start)/2).cos() * ((angle-start)/2).sin()
    density = 870 * rat('3.06e-208')**2 / rat('0.38')**2
    assert jump > rat('0.38') and density < rat('5.65e-412')
    return dict(kind='large_prime_endpoint_and_forcing_constants',
                limiting_cold_width_coefficient_lower=encode(threshold),
                high_phase_displacement_lower=encode(jump), limiting_high_fraction_upper=encode(density))


if __name__ == '__main__':
    for record in [constants(), schur_record()]:
        print(json.dumps(record, sort_keys=True))
