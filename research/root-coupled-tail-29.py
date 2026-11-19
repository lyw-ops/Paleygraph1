"""Replay a reciprocal tail certificate without maximizing over the root first.

The inputs are rational trial payloads from source-tail-28.py. No optimizer,
stationary solver, or assertion about the proposal's convergence is used.
"""

import argparse
from fractions import Fraction
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from square_control import square_field_sign
from theta import paley_sign


def replay(payload):
    from flint import acb, arb, ctx

    ctx.prec = 160
    q, square_root = payload['order'], payload['square_root']
    sign = square_field_sign(square_root) if square_root else paley_sign(q)
    n = len(sign)
    assert q == 2*n+1 and (square_root is None or q == square_root*square_root)
    integers, scale = payload['trial_numerators'], payload['trial_scale']
    assert len(integers) == n and all(isinstance(x, int) for x in integers)
    assert integers[1:] == integers[:0:-1]
    assert isinstance(scale, int) and scale > 0
    tau = Fraction(payload['tau'])
    assert 0 < tau < 1

    def ball(value):
        value = Fraction(value)
        return arb(value.numerator)/value.denominator

    total = sum(integers)
    z = [arb(n*x-total)/(n*scale) for x in integers]
    h = tau/n
    W = ball(1+(n-1)*h)
    floor = 2*ball(h).sqrt()
    phi = [(x*x+c).sqrt() for x, c in zip(z, [arb(4)]+[4*ball(h)]*(n-1))]
    transform = acb.dft(z)
    reflected = [x.real for x in acb.dft(
        [int(s)*x for s, x in zip(sign, transform)], inverse=True)]
    phi_sum = sum(phi)
    b = [u-phi_sum/n-k for u, k in zip(phi, reflected)]
    cost_scale = payload['cost_scale']
    assert isinstance(cost_scale, int) and cost_scale > 0
    upper_cost = [int((x*cost_scale).upper().ceil().unique_fmpz()) for x in b]
    threshold_num = payload['threshold_numerator']
    assert isinstance(threshold_num, int)
    threshold = Fraction(threshold_num, cost_scale)
    excess = Fraction(sum(max(x-threshold_num, 0) for x in upper_cost[1:]), cost_scale)
    root_cost = Fraction(upper_cost[0], cost_scale)
    m = root_cost-threshold
    mass = 2*(n*W).sqrt()-n*floor
    scalar = 2*W.sqrt()*phi_sum/arb(n).sqrt()-4*W
    constant = ball(threshold)*mass-floor*ball(m+excess)
    right = 4+scalar+constant
    C = (1+arb(q).sqrt())*(W/n).sqrt()
    field_lo, field_hi = (1/C).lower(), C.upper()

    def branch(side):
        """Enclose roots of A*x^2-R*x+B <= 0 on the indicated half-line.

        If A is not certified positive, keep the whole branch. When A>0,
        any feasible point lies between the two quadratic roots. A negative
        discriminant excludes the branch. Its outward upper bound gives a
        conservative radical even if its interval straddles zero.
        """
        if side == 'positive':
            A = phi[0]-z[0]-ball(m+excess)
            B = phi[0]+z[0]-ball(m+h*excess)
            lo, hi = arb(1), field_hi
        else:
            A = phi[0]-z[0]-ball(m+h*excess)
            B = phi[0]+z[0]-ball(m+excess)
            lo, hi = field_lo, arb(1)
        result = dict(side=side, coefficient_x2=str(A), coefficient_constant=str(B),
                      coefficient_minus_x=str(right))
        if not A.lower() > 0:
            result.update(status='whole branch: leading coefficient not certified positive',
                          lower=str(lo), upper=str(hi))
            return result, lo, hi
        disc = right*right-4*A*B
        result['discriminant'] = str(disc)
        if disc.upper() < 0:
            result.update(status='excluded: negative discriminant')
            return result, None, None
        radical = max(arb(0), disc.upper()).sqrt()
        # Both expressions use the largest possible radical, giving a
        # lower bound for the smaller root and an upper bound for the larger.
        small = ((right-radical)/(2*A)).lower()
        large = ((right+radical)/(2*A)).upper()
        lo, hi = max(lo, small), min(hi, large)
        if lo > hi:
            result.update(status='excluded: roots miss branch')
            return result, None, None
        result.update(status='quadratic enclosure', lower=str(lo), upper=str(hi))
        return result, lo, hi

    branches = [branch('negative'), branch('positive')]
    surviving = [(lo, hi) for _, lo, hi in branches if lo is not None]
    assert surviving, 'all branches excluded: inspect premises or certificate implementation'
    root_lo = min(lo for lo, _ in surviving)
    root_hi = max(hi for _, hi in surviving)
    return dict(order=q, square_root=square_root, tau=str(tau), steps=payload['steps'],
                threshold=str(threshold), root_cost_upper=str(root_cost),
                positive_excess_upper=str(excess), mass_scalar=str(scalar),
                root_A_lower=str(root_lo), root_A_upper=str(root_hi),
                normalized_theta_lower=str((root_lo/W.sqrt()).lower()),
                normalized_theta_upper=str((root_hi*W.sqrt()).upper()),
                branches=[item for item, _, _ in branches])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('inputs', nargs='+', type=Path)
    args = parser.parse_args()
    for path in args.inputs:
        payload = json.loads(path.read_text())
        result = replay(payload)
        result['certificate_input'] = path.name
        print(json.dumps(result), flush=True)


if __name__ == '__main__':
    main()
