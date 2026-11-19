"""Certify actual least-norm endpoints and true cold orbit projections."""

import argparse
import json
from pathlib import Path
import sys

from flint import acb, arb, arb_mat, ctx, fmpq_poly, fmpz_poly

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from endpoint_norm import even_coordinates
from endpoint_extension_certificate import solve
from square_control import square_field_sign
from theta import optimize, paley_sign


def norm(row):
    return sum(x*x for x in row).sqrt()


def dot(x, y):
    return sum(a*b for a, b in zip(x, y))


def emit(row):
    print(json.dumps(row, sort_keys=True), flush=True)


def positive_part(x):
    return max(arb(0), x.lower()).union(max(arb(0), x.upper()))


def solve_prime_pair(sign):
    """Arb-check a proposed complementary pair with square even supports."""
    n = len(sign)
    representatives, orbit_sizes = even_coordinates(n)
    supports = {}
    for side in (1, -1):
        _, trial = optimize(sign, side)
        supports[side] = [int(i) for i in representatives if trial[i] > 1e-8]
    if set(supports[1]) & set(supports[-1]) != {0}:
        return None, "proposed supports are not complementary"
    if len(set(supports[1]) | set(supports[-1])) != len(representatives):
        return None, "proposed complementary supports leave common zeros"

    cosine = [(arb(2*j)/n).cos_pi() for j in range(n)]
    result = {}
    for side in (1, -1):
        forbidden = [int(i) for i in representatives if sign[i] == -side]
        active = supports[side][1:]
        if len(active) != len(forbidden):
            return None, "nonsquare active equations"
        matrix = arb_mat([[int(orbit_sizes[k])*cosine[(j*k) % n] for k in active]
                          for j in forbidden])
        try:
            entries = list(matrix.solve(arb_mat([[-1] for _ in forbidden])))
        except ValueError:
            return None, "Arb did not certify invertibility"
        if not all(x > 0 for x in entries):
            return None, "Arb did not certify active positivity"
        row = [arb(0) for _ in range(n)]
        row[0] = arb(1)
        for k, value in zip(active, entries):
            row[k] = row[-k % n] = value
        mass = sum(row)
        result[side] = [arb(n).sqrt()*x/mass for x in row]

    assert (result[1][0]*result[-1][0]).contains(1)
    for row in result.values():
        assert (sum(row)-arb(n).sqrt()).contains(0)
    return result, None


def exact_small_endpoint(sign):
    """Certify the least-norm larger endpoint also on a degenerate face."""
    n = len(sign)
    representatives = list(range(1, n//2+1))
    orbit = {i: {i, (-i) % n} for i in representatives}
    modulus = fmpq_poly(fmpz_poly.cyclotomic(n))
    z = fmpq_poly([0, 1])
    powers = [z**j % modulus for j in range(n)]
    cosines = [(arb(2*j)/n).cos_pi() for j in range(n)]
    one = fmpq_poly([1])
    zero = fmpq_poly()

    def enclose(poly):
        return sum(arb(c.numerator)*cosines[i]/c.denominator
                   for i, c in enumerate(poly))

    def matrix(sigma, active):
        return [[sum(powers[(j*i) % n] for i in orbit[k]) for k in active]
                for j in representatives if sign[j] == -sigma]

    active = {}
    anchored = {}
    masses = {}
    for sigma in (1, -1):
        trial = optimize(sign, sigma)[1]
        active[sigma] = [i for i in representatives if trial[i] > 1e-8]
        system = matrix(sigma, active[sigma])
        vector, rank = solve(system, [-one]*len(system), modulus)
        assert rank == len(active[sigma]) and all(enclose(x) > 0 for x in vector)
        anchored[sigma] = vector
        masses[sigma] = (one+sum(len(orbit[i])*v
                                 for i, v in zip(active[sigma], vector))) % modulus
    assert set(active[1]).isdisjoint(active[-1])
    assert ((masses[1]*masses[-1]) % modulus) == n
    sigma = 1 if enclose(masses[1]) < enclose(masses[-1]) else -1
    assert enclose(masses[sigma]) < enclose(masses[-sigma])

    allowed = [i for i in representatives if i not in active[-sigma]]
    block = matrix(sigma, allowed)
    _, rank = solve(block, [zero]*len(block), modulus)
    if rank < len(allowed):
        # A zero outside the active set can only increase in a feasible direction.
        active_matrix = matrix(sigma, active[sigma])
        for i in set(allowed)-set(active[sigma]):
            rhs = [-v[0] for v in matrix(sigma, [i])]
            change, active_rank = solve(active_matrix, rhs, modulus)
            assert active_rank == len(active[sigma])
            derivative = sum(len(orbit[k])*a*b for k, a, b in
                             zip(active[sigma], anchored[sigma], change)) % modulus
            assert enclose(derivative) > 0

    scale = arb(n).sqrt()/enclose(masses[sigma])
    endpoint = [arb(0) for _ in range(n)]
    endpoint[0] = scale
    for i, value in zip(active[sigma], anchored[sigma]):
        endpoint[i] = endpoint[-i % n] = scale*enclose(value)
    return sigma, endpoint


def apply_multiplier(row, multiplier):
    entries = acb.dft(row)
    return [z.real for z in acb.dft([a*int(k) for a, k in zip(entries, multiplier)],
                                    inverse=True)]


def count_active(endpoint):
    return sum(x > 0 for x in endpoint)


def measure(sign, q, sigma, endpoint, depths, kind):
    n = len(sign)
    root_n = arb(n).sqrt()
    d = [x-1/root_n for x in endpoint]
    excess = dot(d, d)
    alpha = endpoint[0]
    atom = alpha*alpha/(1+excess)
    multipliers = [int(x == sigma) for x in sign]
    state = [arb(0) for _ in range(n)]
    radius = mark_loss = mean_reserve = sign_reserve = arb(0)
    endpoint_norm = (1+excess).sqrt()
    last = None
    emit(dict(kind=kind, order=q, sigma=sigma, precision=ctx.prec,
              active_size=count_active(endpoint), alpha=str(alpha),
              collision_excess=str(excess), marked_atom=str(atom)))

    for t in range(1, max(depths)+1):
        marked = state[0]+arb(0, radius.upper())
        mark_loss += 2-(4+marked*marked).sqrt()+abs(marked)
        activation = [abs(v) for v in state]
        activation[0] = (state[0]*state[0]+4).sqrt()
        g = sum(activation)/(2*root_n)+arb(0, (radius/2).upper())
        g_deficit = 1-g
        mean_reserve += g_deficit*g_deficit
        sign_reserve += dot(endpoint, [abs(v)-sigma*v for v in state]) + arb(
            0, (2*endpoint_norm*radius).upper())
        update = apply_multiplier(activation, sign)
        state = [x.mid() for x in update]
        radius = (radius + sum(x.rad()*x.rad() for x in update).sqrt()).upper()
        if t not in depths:
            continue
        uc = [sigma*z for z in apply_multiplier(state, multipliers)]
        length = norm(uc)+arb(0, radius)
        correlation = dot(d, uc)+arb(0, (excess.sqrt()*radius).upper())
        assert length > 0
        projected = positive_part(correlation)
        direction = (projected*projected)/(length*length)
        total_norm = norm(state)+arb(0, radius)
        energy = total_norm*total_norm
        exact_separation = 2*t*(alpha-1)+energy/4-alpha*mark_loss
        assert (correlation-exact_separation-mean_reserve-sign_reserve).contains(0)
        record = dict(kind="true_cold_direction", order=q, sigma=sigma, T=t,
                      orbit_radius=str(radius), mark_loss_per_depth=str(mark_loss/t),
                      signed_correlation=str(correlation), direction_per_depth=str(direction/t),
                      orbit_energy=str(energy))
        if last is not None:
            (s, previous_u, previous_energy, previous_B, previous_radius,
             previous_A, previous_H) = last
            delta_u = [a-b for a, b in zip(uc, previous_u)]
            margin = radius+previous_radius
            delta = dot(d, delta_u)+arb(0, (excess.sqrt()*margin).upper())
            corrected = delta-(energy-previous_energy)/4+alpha*(mark_loss-previous_B)
            assert (corrected-2*(t-s)*(alpha-1) - (mean_reserve-previous_A)
                    - (sign_reserve-previous_H)).contains(0)
            record.update(secant_start=s, signed_secant_per_depth=str(delta/(t-s)),
                          corrected_secant_per_depth=str(corrected/(t-s)))
        emit(record)
        last = t, uc, energy, mark_loss, radius, mean_reserve, sign_reserve


def prime_case(p, depths):
    signs = paley_sign(p)
    endpoints, reason = solve_prime_pair(signs)
    if endpoints is None:
        if p in (29, 97):
            emit(dict(kind="square_active_system_failure", order=p, reason=reason,
                      fallback="exact cyclotomic rank and feasible directional derivative"))
            sigma, endpoint = exact_small_endpoint(signs)
            measure(signs, p, sigma, endpoint, depths, "actual_degenerate_prime_endpoint")
            return
        emit(dict(kind="endpoint_not_certified", order=p, reason=reason))
        return
    low, high = endpoints[-1][0], endpoints[1][0]
    assert high > low or low > high
    sigma = 1 if high > low else -1
    measure(signs, p, sigma, endpoints[sigma], depths, "actual_prime_endpoint")


def square_case(r, depths):
    signs = square_field_sign(r)
    n = len(signs)
    assert all(signs[j] == 1 for j in range(n//(r-1), n, n//(r-1)))
    endpoint = [arb(r-1)/arb(n).sqrt() if i % (r-1) == 0 else arb(0)
                for i in range(n)]
    measure(signs, r*r, 1, endpoint, depths, "exact_square_endpoint")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("primes", nargs="*", type=int,
                        default=[13, 29, 97, 101, 173, 401, 1009, 1997, 4001, 9413])
    parser.add_argument("--square-roots", nargs="*", type=int, default=[7, 11, 31])
    args = parser.parse_args()
    ctx.prec = 224
    times = (1, 4, 16, 64, 256)
    for prime in args.primes:
        prime_case(prime, times)
    for root in args.square_roots:
        square_case(root, times)
