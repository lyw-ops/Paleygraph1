"""Deterministic top-tail checks; no Paley arithmetic or stationary solve."""

from fractions import Fraction
import json
from pathlib import Path
import sys

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from smoothing import kernel_action
from square_control import square_field_sign
from theta import paley_sign


def top(values, capacity):
    """Fractional top sum with negative entries retained."""
    values = sorted(values, reverse=True)
    capacity = Fraction(capacity)
    assert 0 <= capacity <= len(values)
    full = capacity.numerator // capacity.denominator
    result = sum(values[:full])
    if full < len(values):
        result += (capacity-full)*values[full]
    return result


def emit(row):
    print(json.dumps(row, sort_keys=True), flush=True)


def main():
    # Rational checks include fractional capacities and entirely negative rows.
    cases = 0
    for y, z in [([3, -1, -5, 2], [-2, 4, -3, 1]),
                 ([-3, -4, -7, -2], [-8, -2, -9, -4])]:
        for capacity in [Fraction(0), Fraction(1, 2), Fraction(1),
                         Fraction(7, 3), Fraction(4)]:
            difference = abs(top(y, capacity)-top(z, capacity))
            error = [abs(a-b) for a, b in zip(y, z)]
            assert difference <= sum(error)
            assert difference <= capacity*max(error)
            assert difference*difference <= capacity*sum(x*x for x in error)
            cases += 1
    emit(dict(kind='exact rational norm and fractional-capacity audit', cases=cases, passed=True))

    # The exponent example has exact RMS^2=1/s and exact top mass=1.
    for s in (4, 16, 64, 256, 1024):
        n, k = s*s, s
        rms_squared = Fraction(k, n)
        top_mass = Fraction(k, s)
        assert rms_squared == Fraction(1, s) and top_mass == 1
        assert Fraction(k)*rms_squared == 1
        emit(dict(kind='bounded-array sharpness example', n=n, capacity=k,
                  rms_error_squared=str(rms_squared), normalized_top_mass=str(top_mass),
                  empirical_mass_away_from_zero=str(Fraction(k,n)),
                  scope='abstract arrays; not an actual Paley orbit'))

    rng = np.random.default_rng(30)
    cases = 0
    for n in (64, 257, 4096):
        for capacity in (0.5, np.sqrt(n), 1.7*np.sqrt(n)):
            for _ in range(12):
                y, z = rng.normal(size=(2,n))
                difference = abs(float(top(y, Fraction(float(capacity))))-
                                 float(top(z, Fraction(float(capacity)))))
                delta = y-z
                for p in (1, 2, 3, np.inf):
                    norm = np.linalg.norm(delta, ord=p)
                    bound = capacity**(1-(0 if np.isinf(p) else 1/p))*norm
                    assert difference <= bound+1e-10
                cases += 1
    emit(dict(kind='floating Holder consistency audit', cases=cases, passed=True,
              scope='diagnostic, not interval arithmetic'))

    # F(theta)=1+cos(theta), M=2, with two bounded exceptional rows.
    eps, B, B0, N0 = .05, 5., 2., 2
    for n in (256, 1024, 4096):
        theta = 2*np.pi*np.arange(n-1)/(n-1)
        formal = 1+np.cos(theta)
        actual = formal+eps*np.sin(3*theta)
        actual[:N0] = (5., -5.)
        k = np.sqrt(n)
        good = np.arange(n-1)>=N0
        near = int(np.sum((formal>=2-eps)&good))
        assert near>=k
        value = float(top(actual, Fraction(float(k))))/np.sqrt(n)
        lower = k/np.sqrt(n)*(2-2*eps)
        upper = k/np.sqrt(n)*(2+eps)+N0*(B+B0+eps)/np.sqrt(n)
        assert lower <= value <= upper
        emit(dict(kind='compact-grid deterministic lemma check', n=n,
                  near_maximum_samples=near, fractional_capacity=float(k),
                  top_mass=value, lower=lower, upper=upper, passed=True,
                  scope='prescribed grid; no arithmetic equidistribution claim'))

    # These are arbitrary mean-zero even errors, not generated activation errors.
    # Their propagation uses the actual Paley reflection and its square controls.
    fields = [(p, None) for p in (61, 9413, 153649, 1000033)]
    fields += [(r*r, r) for r in (97, 389)]
    for q, root in fields:
        sign = square_field_sign(root) if root else paley_sign(q)
        n = len(sign)
        k = 2*(int(np.sqrt(n))//2)
        pairs = rng.choice(np.arange(1,(n+1)//2),size=k//2,replace=False)
        concentration = 4*np.sqrt(k*np.log(4*n)/n)  # coherence mu=2, paired signs
        for attempt in range(32):
            y = np.zeros(n)
            signs = rng.choice([-1.,1.],size=k//2)
            y[pairs] = signs
            y[-pairs] = signs
            error = kernel_action(sign,y)
            if np.max(np.abs(error)) <= concentration:
                break
        else:
            raise AssertionError('no bounded realization found in the prescribed deterministic replay')
        propagated = kernel_action(sign,error)
        expected = y-y.mean()
        reflection_error = float(np.max(np.abs(propagated-expected)))
        assert reflection_error < 1e-10
        before = float(top(np.abs(error[1:]),k))
        after = float(top(np.abs(propagated[1:]),k))
        lower = (1-k/n)/concentration
        assert after/before >= lower-1e-10
        emit(dict(kind='actual-kernel arbitrary-error propagation diagnostic',
                  order=q,square_root=root,n=n,capacity=k,attempts=attempt+1,
                  input_top_norm=before,output_top_norm=after,ratio=after/before,
                  analytic_ratio_lower=lower,reflection_max_error=reflection_error,
                  input_mean=float(error.mean()),
                  scope='floating diagnostic; arbitrary errors, not an actual nonlinear trajectory'))


if __name__ == '__main__':
    main()
