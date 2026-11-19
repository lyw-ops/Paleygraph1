"""Match the global sharp discount by exact cyclotomic primal and dual data."""
import json
from pathlib import Path
import runpy

from flint import arb, ctx

prior = runpy.run_path(str(Path(__file__).with_name("astra-quartic-89-check.py")))
face = prior["face"]
ctx.prec = 384


def check():
    n = face["n"]
    powers, modulus = face["powers"], face["modulus"]
    zero, one, ball = face["zero"], face["one"], face["ball"]
    solve = face["solve"]
    modes = [i for i in range(1, n // 2 + 1) if face["mask"][i] == -1]
    terminal, masks, _ = prior["delayed_masks"](list(map(int, face["mask"])))
    mask = set(masks[8])
    assert terminal == 11 and mask == {8, 40}

    def divide(value, denominator):
        gcd, inverse, _ = denominator.xgcd(modulus)
        assert gcd == one
        return value * inverse % modulus

    def primary(ids):
        matrix = face["system"](1, ids)
        coeff, rank = solve(matrix, [-one] * len(matrix), modulus)
        assert len(ids) == rank and all(ball(c) > 0 for c in coeff)
        unscaled = face["vector"](ids, coeff, one)
        total = sum(unscaled, zero) % modulus
        return [divide(v, total) for v in unscaled]

    actual = primary(face["active"][1])
    # The inherited exact face computation fixes both masked values on even
    # quartic minimizers. Reflection and strict masked convexity give the full case.
    rows, opp = face["faces"]()
    a = actual[0]
    assert all(rows[i][j].is_zero() for i in mask for j in (1, 2))
    eta = divide(actual[8], a)
    mu = [one / 2 if i in mask else zero for i in range(n)]

    # Interpolation at orbit 24 removes the last scalar repair freedom.
    def cosine(i, j):
        return (powers[i*j % n] + powers[-i*j % n]) / 2

    contacts = face["active"][1] + [24]
    mat = [[cosine(i, j) for j in [0] + modes] for i in contacts]
    coeff, rank = solve(mat, [mu[i] for i in contacts], modulus)
    assert rank == len(contacts)
    potential = [sum((c*cosine(i, j) for c, j in zip(coeff, [0] + modes)), zero) % modulus
                 for i in range(n)]
    b = -potential[0]
    gaps = [mu[i] - potential[i] for i in range(n)]
    assert all(z == zero or ball(z) > 0 for z in gaps[1:])
    assert all(gaps[i] == zero for i in mask)
    assert (sum(potential, zero) / n - a*(eta-b)) % modulus == zero
    assert opp[24] > 0 and gaps[24] == zero

    # The scaled field produces an actual probability with the stated floor.
    floor_numerator = one
    mass = [floor_numerator - w for w in potential]
    assert all(ball(v) > 0 for v in mass)
    total = sum(mass, zero) % modulus
    floor = divide(one, total)
    law = [divide(v, total) for v in mass]
    assert sum(law, zero) % modulus == one
    assert all((floor-law[i]-floor*mu[i]) % modulus == zero for i in mask)
    beta = divide(one, n*a)
    shortfall = sum((floor-law[i] for i in mask), zero) % modulus
    gain = (floor*(divide(one, a)-one) - beta + law[0]) % modulus
    assert (gain-eta*shortfall) % modulus == zero
    assert (law[0]-floor-b*shortfall) % modulus == zero

    challenger = primary([2, 3, 5, 6, 7, 8, 11, 13, 18, 19, 22, 24])
    support = [i for i in range(n) if challenger[i] != zero]
    full_modes = [0] + [i for i in range(1, n) if face["mask"][i] == -1]
    constraints = [[powers[i*j % n] for i in support] for j in full_modes]
    _, vertex_rank = solve(constraints, [zero] * len(full_modes), modulus)
    assert vertex_rank == len(support) == 24
    assert all((x*g) % modulus == zero for x, g in zip(challenger[1:], gaps[1:]))
    step = (a - challenger[0]) % modulus
    price = sum((x*y for x, y in zip(challenger, mu)), zero) % modulus
    secant = divide((a*eta-price) % modulus, step)
    assert ball(step) > 0 and secant == b
    interval = lambda poly: prior["interval"](ball(poly))
    return dict(prime=97, terminal=terminal, length=8, mask=sorted(mask),
                exact_field="Q(zeta_48)", precision_bits=ctx.prec, units="1e-9",
                sharp_efficiency=interval(eta), global_signed_discount=interval(b),
                primal_mark=interval(a), challenger_mark=interval(challenger[0]),
                relative_root_loss=interval(divide(step, a)),
                relative_cubic_loss=interval(divide((a*eta-price) % modulus, a)),
                full_support_rank=vertex_rank,
                challenger_exterior_orbits=[i for i in range(1, 25) if challenger[i] != zero],
                dual_contact_orbits=[i for i in range(1, 25) if gaps[i] == zero])


if __name__ == "__main__":
    print(json.dumps(check(), sort_keys=True))
