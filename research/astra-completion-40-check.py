"""Verify the limiting constants and finite true Picard endpoint identities."""

import json

from flint import arb, arb_mat, ctx


def emit(**fields):
    print(json.dumps(fields, sort_keys=True))


def check_constants():
    m = 2 * arb(2).sqrt() / arb.pi()
    b = 2 * m / 3
    step = 2 * (1 - m**2).sqrt()
    gain = b**2 / (2 * arb.pi() * arb(2).sqrt())
    switching = 2 * b**3 / (3 * arb.pi())
    dissipation = 4 * gain**2 + switching
    gap = (step - (step**2 - dissipation).sqrt()) / 2
    sector = gap / arb(2).sqrt()
    assert gain > arb("0.04054271")
    assert dissipation > arb("0.05245981")
    assert gap > arb("0.01533669") and sector > arb("0.01084468")
    emit(kind="limiting_cold_endpoint_constants", precision=ctx.prec,
         lower_mean_gain=str(gain), lower_squared_step_loss=str(dissipation),
         endpoint_lower=str(gap), each_sector_lower=str(sector))


def finite_orbit(floor):
    # 2 is a generator of F_101^*: its order divides 100, not 50 or 20.
    p, n = 101, 50
    assert pow(2, 50, p) != 1 and pow(2, 20, p) != 1
    signs = []
    for j in range(n):
        symbol = pow((1 - pow(4, j, p)) % p, 50, p)
        signs.append(-1 if symbol == p - 1 else symbol)
    cosines = [(arb(2*j) / n).cos_pi() for j in range(n)]
    col = [sum(s * cosines[i*j % n] for j, s in enumerate(signs))/n
           for i in range(n)]
    kernel = arb_mat([[col[(i-j) % n] for j in range(n)] for i in range(n)])

    def apply(vector):
        result = kernel * arb_mat(n, 1, vector)
        return [result[i, 0] for i in range(n)]

    def diff(left, right):
        return [x-y for x, y in zip(left, right)]

    def dot(left, right):
        return sum(x*y for x, y in zip(left, right))

    tau = arb(1) / 20 if floor == "1/20" else arb(0)
    v = [arb(0)] * n
    vectors, activations, means, steps = [v], [], [], []
    for _ in range(18):
        phi = [abs(x) if i and floor == "0"
               else (x**2 + (4*tau/n if i else 4)).sqrt()
               for i, x in enumerate(v)]
        nxt = apply(phi)
        step = diff(nxt, v)
        steps.append(dot(step, step).sqrt())
        means.append(sum(phi) / (2*arb(n).sqrt()))
        vectors.append(nxt)
        activations.append(phi)
        v = nxt
    assert steps[1] > steps[2]
    assert steps[1]**2-steps[2]**2 > 4*(means[2]-means[1])**2
    for T in (1, 4, 16):
        delta = diff(vectors[T+1], vectors[1])
        source = diff(activations[T], activations[0])
        image = apply(delta)
        avg = sum(source) / n
        assert all((y-(z-avg)).contains(0) for y, z in zip(image, source))
        energy = dot(delta, delta)
        signed = dot(delta, image)
        projected = []
        for sigma in (1, -1):
            part = [(x+sigma*y)/2 for x, y in zip(delta, image)]
            value = dot(part, part)
            assert (value-(energy+sigma*signed)/2).contains(0)
            projected.append(str(value))
        assert energy.sqrt() > (steps[1]-steps[2])/2
        emit(kind="true_finite_orbit_endpoint", q=p, tau=floor, T=T,
             precision=ctx.prec, endpoint_squared=str(energy),
             signed_quadratic_pairing=str(signed), sector_squared=projected,
             finite_nonreturn_lower=str((steps[1]-steps[2])/2))


if __name__ == "__main__":
    ctx.prec = 256
    check_constants()
    finite_orbit("0")
    finite_orbit("1/20")
