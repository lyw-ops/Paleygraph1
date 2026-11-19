"""Small deterministic checks of unequal-rate and time-block comparisons."""

import json
from math import ceil, exp, log, sqrt
from pathlib import Path
import sys

import numpy as np


sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from smoothing import kernel_action
from theta import paley_sign


def two_step_factor(n, a, b, first, second):
    k = 1/n
    r = sqrt(1-1/n-k*k)
    matrix = np.array([
        [a*(second+(b-second)*k*k), abs(b-second)*k*r*sqrt(a*first)],
        [abs(b-second)*k*r*sqrt(a*first), first*(second+(b-second)*r*r)],
    ])
    return max(first*second, float(np.linalg.eigvalsh(matrix)[-1]))


def backward_weights(rates, root_squares, floor=.5):
    length = len(rates)
    u = np.ones(length+1)
    v = np.ones(length+1)
    for t in range(length-1, -1, -1):
        u[t] = root_squares[t]*v[t+1]
        v[t] = max(rates[t], floor)*max(u[t+1], v[t+1])
    return u, v


def cover_cost(rates, floor=.5):
    root_cost, bulk_cost = 0., -log(max(rates[0], floor))
    for rate in rates[1:]:
        root_cost, bulk_cost = bulk_cost, min(root_cost, bulk_cost)-log(max(rate, floor))
    return min(root_cost, bulk_cost)


def compare_small(prime):
    signs = paley_sign(prime)
    n = len(signs)
    rng = np.random.default_rng(prime)
    maximum_two_step_excess = 0.
    tests = 0
    for first, second in ((.1,.9),(.9,.1),(.2,.7),(.7,.2),(0.,.8),(.8,0.)):
        for a in (.1,.9,1.):
            for b in (.1,.9,1.):
                factor = two_step_factor(n, a, b, first, second)
                for _ in range(12):
                    increment = rng.normal(size=n)
                    increment -= increment.mean()
                    h = sqrt(first)*increment
                    h[0] = sqrt(a)*increment[0]
                    next_increment = kernel_action(signs, h)
                    next_h = sqrt(second)*next_increment
                    next_h[0] = sqrt(b)*next_increment[0]
                    final = kernel_action(signs, next_h)
                    bound = (factor*(increment@increment)
                             -second*h.sum()**2/n-next_h.sum()**2/n)
                    excess = float(final@final-bound)
                    maximum_two_step_excess = max(maximum_two_step_excess, excess)
                    if excess > 3e-11:
                        raise RuntimeError("the unequal-rate two-step bound failed")
                    tests += 1
    rates = rng.uniform(.05,1.,size=24)
    root_squares = rng.uniform(.05,1.,size=24)
    u, v = backward_weights(rates, root_squares)
    gamma = n/(n-2)
    increment = rng.normal(size=n)
    increment -= increment.mean()
    initial_energy = float(increment@increment)
    reserve = 0.
    for t, rate in enumerate(rates):
        multiplier = rng.uniform(-sqrt(rate),sqrt(rate),size=n)
        multiplier[0] = sqrt(root_squares[t])
        h = multiplier*increment
        mean_loss = float(h.sum()**2/n)
        new = kernel_action(signs,h)
        potential = u[t]*increment[0]**2+v[t]*float(increment[1:]@increment[1:])
        next_potential = u[t+1]*new[0]**2+v[t+1]*float(new[1:]@new[1:])
        if next_potential > gamma*potential-.5*v[t+1]*mean_loss+3e-11:
            raise RuntimeError("the one-step weighted potential bound failed")
        reserve += .5*gamma**(len(rates)-1-t)*v[t+1]*mean_loss
        increment = new
    block_bound = gamma**len(rates)*max(u[0],v[0])*initial_energy-reserve
    if increment@increment > block_bound+3e-11:
        raise RuntimeError("the retained-reserve block bound failed")
    simple_u,simple_v = backward_weights(rates,np.ones(len(rates)))
    cost=cover_cost(rates)
    if abs(max(simple_u[0],simple_v[0])-exp(-cost))>3e-13:
        raise RuntimeError("the vertex-cover identification failed")
    return dict(kind="small_comparisons", order=prime, two_step_tests=tests,
                maximum_two_step_positive_excess=maximum_two_step_excess,
                final_block_energy=float(increment@increment),
                retained_reserve_block_upper=float(block_bound),
                weighted_cover_cost=cost)


def alternating(prime):
    signs = paley_sign(prime)
    n = len(signs)
    root = np.zeros(n)
    root[0] = 1
    e = root-1/n
    h = kernel_action(signs,root)
    rate = .25
    gamma = 1-(1-sqrt(rate))/n
    pairs = ceil(log(prime))
    increment = e.copy()
    for _ in range(pairs):
        multiplier = np.full(n,sqrt(rate))
        multiplier[0] = 1
        increment = kernel_action(signs,multiplier*increment)
        increment = kernel_action(signs,increment)
    prediction = gamma**pairs*e
    error = float(np.linalg.norm(increment-prediction))
    if error>3e-12:
        raise RuntimeError("the exact-form alternating example failed")
    return dict(kind="alternating_example", order=prime, pairs=pairs,
                good_step_fraction=.5, energy_ratio=float((increment@increment)/(e@e)),
                predicted_energy_ratio=gamma**(2*pairs), vector_error=error,
                cover_cost=cover_cost([rate,1.]*pairs))


def main():
    for prime in (29,61,97):
        print(json.dumps(compare_small(prime)))
    for prime in (61,9413):
        print(json.dumps(alternating(prime)))


if __name__ == "__main__":
    main()
