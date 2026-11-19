"""Positive-cone compression and actual-source checks for Round 27.

The sign arrays use exact finite-field arithmetic. Subgroup constants are
enclosed with 160-bit Arb. Two first-step orbit checks also use Arb; long
orbit and dense-matrix checks are floating-point diagnostics. Writes JSON
to stdout.
"""

from fractions import Fraction
import json
from math import sqrt
from pathlib import Path
import sys

import numpy as np
from flint import acb, arb, ctx

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from smoothing import kernel_action
from square_control import square_field_sign
from theta import paley_sign

ctx.prec = 160


def compression_constant(order, sign, b):
    n = len(sign)
    assert n % b == 0
    m = n // b
    numerator = sum(int(x) for x in sign[::m])
    a = arb(numerator) / b
    r = arb(order).sqrt() / b
    c = ((r*r + a*a)/2).sqrt()
    raw = c - 1/r + (2 - 2*c/r + 1/(r*r)).sqrt()
    # q=1 is always valid by the full K contraction.
    certified_gap = raw < 1
    q = float(np.nextafter(float(raw.upper()), np.inf)) if certified_gap else 1.0
    # For a single subgroup, all eigenvalues of the compression are exactly
    # the positional B-coset means. This independent finite bound is not used
    # by the uniform positive-cone argument or the orbit inequalities below.
    coset_sums = np.asarray(sign, dtype=np.int64).reshape(b, m).sum(axis=0)
    return q, dict(order=order, n=n, positional_subgroup_size=b,
                   frequency_subgroup_size=m,
                   flat_rayleigh_exact=str(Fraction(numerator, b)),
                   size_ratio_interval=str(r), c_interval=str(c),
                   raw_cone_bound_interval=str(raw),
                   full_compression_norm_exact=str(Fraction(int(np.max(np.abs(coset_sums))), b)),
                   certified_strict_cone_bound=bool(certified_gap),
                   cone_bound_used=q)


def norm(v):
    return float(np.linalg.norm(v))


def actual_orbit(order, square_root, b, steps=257, tau=.05):
    sign = paley_sign(order) if square_root is None else square_field_sign(square_root)
    n = len(sign)
    qbound, constant = compression_constant(order, sign, b)
    mask = np.zeros(n, dtype=bool)
    mask[::b] = True
    weight4 = np.full(n, 4*tau/n)
    weight4[0] = 4
    base = np.sqrt(weight4)
    forcing = kernel_action(sign, base)
    v = np.zeros(n)
    increment = forcing.copy()
    max_errors = dict(cumulative_source_identity=0., source_recursion=0.,
                      local_source_bound=0., signed_increment_bound=0.,
                      direct_recurrence=0.)
    h_sum = np.zeros(n)
    envelope = 0.
    rows = []
    for t in range(steps):
        next_v = v + increment
        phi = np.sqrt(v*v + weight4)
        next_phi = np.sqrt(next_v*next_v + weight4)
        # Rationalization avoids cancellation in cumulative sources and increments.
        source = v*v/(phi+base)
        next_source = next_v*next_v/(next_phi+base)
        h = increment*(v+next_v)/(phi+next_phi)
        next_increment = kernel_action(sign, h)
        source_local = norm(source[mask])
        source_tail = norm(source[~mask])
        forcing_local = norm(forcing[mask])
        local_rhs = forcing_local + qbound*source_local + source_tail
        local_lhs = norm(next_source[mask])
        envelope = forcing_local + qbound*envelope + source_tail
        minority = min(norm(np.maximum(h[mask], 0)),
                       norm(np.minimum(h[mask], 0)))
        increment_rhs = (qbound*norm(increment) + 2*minority
                         + norm(h[~mask]) + norm(next_increment[~mask]))
        max_errors['cumulative_source_identity'] = max(
            max_errors['cumulative_source_identity'], norm(h_sum-source))
        max_errors['source_recursion'] = max(
            max_errors['source_recursion'],
            norm(next_v-forcing-kernel_action(sign, source)))
        max_errors['direct_recurrence'] = max(
            max_errors['direct_recurrence'], norm(next_v-kernel_action(sign, phi)))
        max_errors['local_source_bound'] = max(
            max_errors['local_source_bound'], local_lhs-local_rhs)
        max_errors['signed_increment_bound'] = max(
            max_errors['signed_increment_bound'], norm(next_increment)-increment_rhs)
        assert local_lhs <= local_rhs + 2e-12
        assert local_lhs <= envelope + 2e-12
        assert norm(next_increment) <= increment_rhs + 2e-12
        if t in {0, 1, 2, 8, 32, 64, 128, 256}:
            den = norm(increment)
            rows.append(dict(step=t, source_local_norm=source_local,
                             source_exterior_norm=source_tail,
                             forcing_local_norm=forcing_local,
                             source_local_next_norm=local_lhs,
                             one_step_source_upper=local_rhs,
                             cumulative_source_envelope=envelope,
                             source_local_energy_fraction=source_local**2/(norm(source)**2)
                             if norm(source) else 0.,
                             increment_norm=den,
                             increment_ratio=norm(next_increment)/den if den else None,
                             increment_source_minority_over_increment=minority/den if den else None,
                             increment_exterior_fraction=norm(increment[~mask])**2/den**2
                             if den else None,
                             h_exterior_over_increment=norm(h[~mask])/den if den else None,
                             next_increment_exterior_over_increment=norm(next_increment[~mask])/den
                             if den else None,
                             restricted_increment_ratio_upper=increment_rhs/den if den else None,
                             root=float(v[0])))
        h_sum += h
        v, increment = next_v, next_increment
    return dict(kind='floating_actual_orbit', square_root=square_root,
                tau=tau, steps=steps, constant=constant, rows=rows,
                maximum_errors=max_errors)


def dense_checks():
    rng = np.random.default_rng(270018)
    worst = 0.
    count = 0
    details = []
    for order, root in [(61, None), (97, None), (49, 7), (121, 11)]:
        sign = paley_sign(order) if root is None else square_field_sign(root)
        n = len(sign)
        column = kernel_action(sign, np.eye(1, n)[0])
        K = column[(np.arange(n)[:, None]-np.arange(n)[None, :]) % n]
        assert np.max(np.abs(K@K - np.eye(n) + np.ones((n,n))/n)) < 2e-14
        m0 = n/sqrt(order)
        for trial in range(12):
            m = max(1, int(m0) + trial % 3 - 1)
            U = rng.choice(n, m, replace=False)
            C = K[np.ix_(U,U)]
            uniform = np.full(m, 1/sqrt(m))
            a = float(uniform@C@uniform)
            r = m/m0
            c = sqrt((r*r+a*a)/2)
            bound = min(1., c - 1/r + sqrt(2-2*c/r+1/r**2))
            assert norm(C@uniform)**2 <= (r*r+a*a)/2+1e-13
            largest_seen = 0.
            for sample in range(100):
                w = rng.lognormal(sigma=(sample % 7)/2, size=m)
                w /= norm(w)
                value = norm(C@w)
                largest_seen = max(largest_seen, value)
                worst = max(worst, value-bound)
                assert value <= bound + 2e-13
                count += 1
            details.append(dict(order=order, support_size=m, bound=bound,
                                largest_sampled_positive_ratio=largest_seen))
    return dict(kind='floating_dense_checks', positive_vectors_checked=count,
                maximum_violation=worst, details=details)


def square_identities(r):
    sign = square_field_sign(r)
    n = len(sign)
    # Untwisted subfield branch.
    I = np.zeros(n)
    I[::r-1] = 1
    h = (r+1)//2
    err1 = norm(kernel_action(sign, I) - (I-h/n))
    # Norm-one subgroup and its genuine order-two shifted frequency coset.
    A = np.zeros(n)
    A[::r+1] = 1
    T = np.roll(A, (r+1)//2)
    g = (r-1)//2
    sigma = (-1)**((r+1)//2)
    # Verify the positional twist entirely in integers, including the zero.
    pos = [int(x) for x in sign[::g]]
    assert pos[0] == 0
    assert all(pos[j] == sigma*(-1)**j for j in range(1,r+1))
    err2 = norm(kernel_action(sign, A) - sigma*(T-g/n))
    err3 = norm(kernel_action(sign, T) - sigma*(A-g/n))
    assert max(err1, err2, err3) < 1e-12
    return dict(kind='square_exact_formulas_with_fft_crosscheck', root=r,
                square_order=r*r, subfield_cone_ratio_exact=str(1-Fraction(1,r-1)),
                twisted_cross_transfer_ratio_exact=str(1-Fraction(1,r+1)),
                twist_sign=sigma, positional_twist_integer_check=True,
                maximum_fft_error=max(err1, err2, err3))


def first_pair_interval_check(p, b):
    """Certify the restricted theorem on the actual first two steps.

    At t=0, h_0=Phi(v_1)-Phi(0)>=0 exactly, so its minority norm is zero.
    All field entries below are interval enclosures of the true orbit.
    """
    sign = list(map(int, paley_sign(p)))
    n = len(sign)
    m = n//b
    assert n % b == 0
    a = arb(sum(sign[::m]))/b
    r = arb(p).sqrt()/b
    c = ((r*r+a*a)/2).sqrt()
    raw = c-1/r+(2-2*c/r+1/(r*r)).sqrt()
    scale = 10**9
    gamma = Fraction(int((raw*scale).upper().ceil().unique_fmpz()), scale)
    assert gamma < 1

    def ball(x):
        return arb(x.numerator)/x.denominator

    def action(x):
        tx = acb.dft(x)
        return [z.real for z in acb.dft([s*y for s,y in zip(sign,tx)], inverse=True)]

    tau = Fraction(1,20)
    weights4 = [arb(4)] + [ball(4*tau/n)]*(n-1)
    v = [arb(0)]*n
    orbit = [v]
    for _ in range(3):
        v = action([(x*x+w).sqrt() for x,w in zip(v,weights4)])
        orbit.append(v)
    max_endpoint = max(abs(orbit[t][i]).upper()
                       for t in (1,2) for i in range(n) if i % b)
    R = int((max_endpoint*arb(n).sqrt()).upper().ceil().unique_fmpz())
    Delta = 1-gamma
    kappa = 4*tau/(R*R+4*tau)
    epsilon = min(Delta/4, kappa*Delta*Delta/64)
    E0 = sum(x*x for x in orbit[1])
    E2 = sum((x-y)**2 for x,y in zip(orbit[3],orbit[2]))
    assert E2 < ball(1-epsilon)*E0
    return dict(kind='interval_actual_first_pair', prime=p,
                positional_subgroup_size=b, frequency_subgroup_size=m,
                cone_bound_rational=str(gamma), bulk_endpoint_bound_integer=R,
                minority_source_norm_exact='0', epsilon_exact=str(epsilon),
                E0_interval=str(E0), E2_interval=str(E2),
                E2_over_E0_interval=str(E2/E0), two_step_bound_certified=True)


if __name__ == '__main__':
    print(json.dumps(dense_checks()), flush=True)
    for p,b in [(61,10), (4177,72)]:
        print(json.dumps(first_pair_interval_check(p,b)), flush=True)
    for order, b in [(1153,32), (4177,72), (10193,98), (40801,200), (252001,500)]:
        print(json.dumps(actual_orbit(order, None, b)), flush=True)
    for r in (31,97,193):
        print(json.dumps(square_identities(r)), flush=True)
        print(json.dumps(actual_orbit(r*r, r, r-1)), flush=True)
