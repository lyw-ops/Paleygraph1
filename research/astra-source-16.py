"""Replay the source-propagation results in astra-source-16.md.

Run from the repository root. Prints JSONL and writes no files itself.
QP supports are numerical. Exact square ranks are also proved in the note;
floating-point FFT zero counts below are only independent finite checks.
The six-point prime construction is evaluated separately with 192-bit Arb.
"""

import importlib.util
import json
from fractions import Fraction
from pathlib import Path

import numpy as np
from scipy.linalg import solve as dense_solve

spec = importlib.util.spec_from_file_location(
    "source16_previous", Path(__file__).with_name("astra-convolution-11.py")
)
previous = importlib.util.module_from_spec(spec)
spec.loader.exec_module(previous)
from theta import prime_divisors, prime_field_generator


def field_data(p, square=False):
    if not square:
        root = prime_field_generator(p)
        positions = np.array([pow(root, 2*j, p) for j in range((p-1)//2)])
        return previous.paley_sign(p), positions, (p,)
    order = p*p-1
    nonresidue = next(d for d in range(2, p) if pow(d, (p-1)//2, p) == p-1)

    def mul(x, y):
        a, b = x
        c, d = y
        return ((a*c+nonresidue*b*d) % p, (a*d+b*c) % p)

    def power(x, k):
        ans = (1, 0)
        while k:
            if k & 1:
                ans = mul(ans, x)
            x = mul(x, x)
            k //= 2
        return ans

    root = next((a, b) for b in range(1, p) for a in range(p)
                if all(power((a, b), order//d) != (1, 0)
                       for d in prime_divisors(order)))
    step = mul(root, root)
    elt = (1, 0)
    positions = []
    for _ in range(order//2):
        positions.append(elt[0]*p+elt[1])
        elt = mul(elt, step)
    return previous.square_field_sign(p), np.array(positions), (p, p)


def lift(v, positions, shape):
    g = np.zeros(np.prod(shape), dtype=complex)
    g[positions] = np.fft.fft(v)/np.sqrt(len(v))
    return g.reshape(shape)


def additive_stats(v, positions, shape):
    g = lift(v, positions, shape)
    eigen = np.fft.fftn(g).ravel()
    return dict(zero_eigenvalue_abs=float(abs(eigen[0])),
                nonzero_frequency_min=float(np.min(np.abs(eigen[1:]))),
                nonzero_frequency_max=float(np.max(np.abs(eigen[1:]))),
                positional_norm=float(np.linalg.norm(g)),
                additive_parseval_error=float(abs(np.sum(abs(eigen)**2)
                                                - g.size*np.sum(abs(g)**2))))


def actual_case(p, square=False):
    signs, positions, shape = field_data(p, square)
    q, n = np.prod(shape).item(), len(signs)
    r = q**(-1/3)
    eta, beta = r*r/(1-r*r), r/(1+r)
    x, y, _, qp_residual = previous.solve(signs, r)
    for side, xx in ((1, x), (-1, y)):
        I = np.flatnonzero(xx[1:] > 1e-8)+1
        if not len(I):
            continue
        a = xx[0]
        energy = float(xx[I] @ xx[I])
        nk = np.fft.ifft((signs == -side).astype(float)).real
        rk = nk + beta/n
        C = rk[(I[:, None]-I[None, :]) % n]
        force = -a*rk[I]
        wsmall = dense_solve(C+eta*np.eye(len(I)), xx[I],
                            assume_a="pos")/energy
        w = np.zeros(n)
        w[I] = wsmall
        d = np.fft.ifft((signs == -side)*np.fft.fft(w)).real + beta*w.mean()
        f = np.zeros(n)
        f[I] = force
        cut = np.where((np.arange(n) != 0) & (xx > 1/np.sqrt(n)), xx, 0.)
        errors = [abs(-a*d[0]-1),
                  np.linalg.norm(C@xx[I]+eta*xx[I]-force),
                  max(0., np.linalg.norm(d[I])*np.sqrt(energy)-1),
                  max(0., eta*np.linalg.norm(w)*np.sqrt(energy)-1),
                  max(0., 2*np.sqrt(eta*energy)*np.linalg.norm(d)-1)]
        # Exact source-dual equivalence: 1/(2 sqrt(E)) <= epsilon <= 1/sqrt(E).
        objective = max(np.linalg.norm(d[I]), eta*np.linalg.norm(w))
        errors.append(max(0., .5-objective*np.sqrt(energy)))
        assert max(errors) < 2e-7, (q, side, errors)
        yield dict(kind="actual_qp", q=q, characteristic=p, side=side, r=r,
                   bulk_energy=energy, support_size=len(I), qp_residual=qp_residual,
                   identity_error=float(max(errors)), contrast=float(-a*d[0]),
                   leakage_scaled=float(np.linalg.norm(d[I])*np.sqrt(energy)),
                   preimage_scaled=float(eta*np.linalg.norm(w)*np.sqrt(energy)),
                   global_scaled=float(2*np.sqrt(eta*energy)*np.linalg.norm(d)),
                   source=additive_stats(f/a, positions, shape),
                   high_cut=additive_stats(cut/a, positions, shape),
                   dual_potential=additive_stats(a*d, positions, shape))


def square_controls(p):
    signs, positions, shape = field_data(p, True)
    q, n = p*p, len(signs)
    # Inversion-even, pure plus sector, zero bulk mark. Its trace-zero
    # additive frequencies vanish exactly (p of them, including zero).
    a, b = 2, 3
    assert len({a, b, pow(a, -1, p), pow(b, -1, p)}) == 4
    g = np.zeros(q)
    for t, value in ((a, 1), (pow(a, -1, p), 1),
                     (b, -1), (pow(b, -1, p), -1)):
        g[t*p] += value
    u = np.fft.ifft(g[positions])*np.sqrt(n)
    additive = np.fft.fftn(g.reshape(shape)).ravel()
    assert max(abs(u.imag)) < 1e-12
    assert abs(u[0]) < 1e-12
    assert np.max(abs(g[positions][signs != 1]), initial=0) == 0
    rank = int(np.count_nonzero(abs(additive) > 1e-9))
    assert rank == q-p
    yield dict(kind="square_pure_sector", q=q, characteristic=p,
               proved_rank=q-p, numerical_rank=rank,
               predicted_zero_count=p, numerical_zero_count=q-rank,
               mark_abs=float(abs(u[0])), imaginary_error=float(max(abs(u.imag))))
    # A nonnegative bulk vector with very small additive translate rank.
    # The positional lift is a linear combination of three square lines.
    index = np.arange(n) % ((p+1)//2)
    f = (index == 0).astype(float)-.5*(index == 1)-.5*(index == (p-1)//2)
    u = np.fft.ifft(f)*np.sqrt(n)
    g = np.zeros(q)
    g[positions] = f
    additive = np.fft.fftn(g.reshape(shape)).ravel()
    rank = int(np.count_nonzero(abs(additive) > 1e-8))
    assert rank == 3*(p-1)
    assert min(u.real) > -1e-12 and abs(u[0]) < 1e-12
    assert max(abs(u.imag)) < 1e-12
    yield dict(kind="square_nonnegative_bulk", q=q, characteristic=p,
               proved_rank=3*(p-1), numerical_rank=rank,
               support_size=int(np.count_nonzero(u.real > 1e-10)),
               bulk_min=float(min(u.real)), mark_abs=float(abs(u[0])))


def prime_small_eigenvalues():
    from flint import acb, arb, ctx
    ctx.prec = 192
    aa, cc, xi = [2, 3, 4], [-11, 21, -10], 12
    assert sum(cc) == 0
    assert sum((Fraction(c)*(a+Fraction(1, a)) for a, c in zip(aa, cc)), Fraction()) == 0
    norm = arb(2*sum(c*c for c in cc)).sqrt()
    constant = 2*arb.pi()**2*sum(abs(c)*((xi*a)**2+(xi//a)**2)
                               for a, c in zip(aa, cc))/norm
    for p in [97, 1009, 10009, 1000033]:
        assert p % 24 == 1
        prime_field_generator(p)  # Includes a primality check.
        points = [t for a in aa for t in [a, pow(a, -1, p)]]
        assert len(set(points)) == 6
        assert all(pow(t, (p-1)//2, p) == 1 and
                   pow((1-t) % p, (p-1)//2, p) == 1 for t in points)
        value = acb(0)
        for a, c in zip(aa, cc):
            for exponent in [xi*a, xi//a]:
                value += c*acb(0, 2*arb.pi()*exponent/p).exp()
        magnitude = abs(value)/norm
        bound = constant/(p*p)
        assert magnitude > 0 and magnitude < bound
        eta = 1/(arb(p)**(arb(2)/3)-1)
        yield dict(kind="prime_six_point_arb", p=p,
                   coefficients=cc, paired_positions=aa, additive_frequency=xi,
                   eigenvalue_magnitude=str(magnitude),
                   taylor_upper_bound=str(bound),
                   eigenvalue_over_eta=str(magnitude/eta),
                   constant=str(constant), precision_bits=ctx.prec)


def main():
    for p in [13, 29, 97, 193, 401, 1009, 2017]:
        for row in actual_case(p):
            print(json.dumps(row), flush=True)
    for p in [7, 11, 19, 31]:
        for row in actual_case(p, True):
            print(json.dumps(row), flush=True)
        for row in square_controls(p):
            print(json.dumps(row), flush=True)
    for row in prime_small_eigenvalues():
        print(json.dumps(row), flush=True)


if __name__ == "__main__":
    main()
