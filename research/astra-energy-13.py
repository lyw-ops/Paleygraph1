"""Current-width centered response checks for astra-energy-13.md.

Run from the repository root with .venv/bin/python -B.  No files are written.
Numerical support detection is not an interval certificate; --certificate
separately verifies two complete small QP orthants using Arb.
"""

import argparse
import importlib.util
import json
from pathlib import Path

import numpy as np
from scipy.linalg import helmert

spec = importlib.util.spec_from_file_location(
    "energy13_previous", Path(__file__).with_name("astra-convolution-11.py")
)
previous = importlib.util.module_from_spec(spec)
spec.loader.exec_module(previous)


def check(q, characteristic, width):
    sign = (previous.paley_sign(characteristic) if q == characteristic
            else previous.square_field_sign(characteristic))
    x, y, _, residual = previous.solve(sign, width)
    n = len(sign)
    rows = []
    for side, xx, yy in [(1, x, y), (-1, y, x)]:
        active = np.flatnonzero(xx[1:] > 1e-8) + 1
        m = len(active)
        if not m:
            continue
        a = xx[0]
        c = xx.sum() / np.sqrt(n)
        L = xx[active].sum()
        mean = L / m
        v = xx[active] - mean
        density = L * L / m
        D = float(v @ v)
        eta = width * width / (1 - width * width)
        kernel = np.fft.ifft((sign == -side).astype(float)).real
        comp = kernel[(active[:, None] - active[None, :]) % n]
        base = a * kernel[active] + mean * comp.sum(axis=1)
        f = -base + base.mean()
        centered = comp - comp.mean(axis=0)[None, :] - comp.mean(axis=1)[:, None] + comp.mean()
        response_error = float(np.linalg.norm(centered @ v + eta * v - f))
        # Helmert removes the artificial constant zero eigenvalue exactly in theory.
        basis = helmert(m, full=False).T
        C = basis.T @ comp @ basis
        force = basis.T @ f
        spectrum, vectors = np.linalg.eigh(C)
        coords = vectors.T @ force
        if spectrum.min(initial=0) < -1e-10:
            raise AssertionError("compression is not positive semidefinite")
        spectrum = np.maximum(spectrum, 0)
        measured_D = np.sum(coords**2 / (spectrum + eta)**2)
        bins = np.floor(np.log2((spectrum + eta) / eta)).astype(int)
        masses = np.bincount(bins, weights=coords**2)
        scale = eta * 2.0 ** np.arange(len(masses))
        dyadic = float(np.sum(masses / scale**2))
        band_energy = np.bincount(bins, weights=coords**2 / (spectrum + eta)**2)
        witness = {}
        witness_error = 0.0
        if measured_D > 1e-12:
            wc = coords/(spectrum+eta)**2/measured_D
            contrast = float(coords @ wc)
            leakage = float(np.linalg.norm(spectrum*wc))
            preimage = float(eta*np.linalg.norm(wc))
            global_size = float(np.sqrt(eta*np.sum(spectrum*wc**2)))
            witness_error = max(abs(contrast-1), max(0.0, leakage-1/np.sqrt(measured_D)),
                                max(0.0, preimage-1/np.sqrt(measured_D)),
                                max(0.0, global_size-1/(2*np.sqrt(measured_D))))
            witness = dict(contrast=contrast, centered_leakage=leakage,
                           ridge_preimage=preimage, sqrt_eta_global_opposite_norm=global_size)
        # One signed source candidate: h=(C+eta)^-1 f, transported back to I.
        hv = vectors @ (coords / (spectrum + eta))
        hnorm = float(np.linalg.norm(hv))
        source_residual = float(np.linalg.norm(force - C @ hv))
        source_bound = (hnorm + source_residual / eta)**2
        ff, gg = np.fft.fft(xx), np.fft.fft(yy)
        allowed = float(np.sum(np.abs(ff[sign == side])**2) / n)
        opposite = float(np.sum(np.abs(gg[sign == -side])**2) / n)
        decomposition = a*a + density + D - c*c - width*width*opposite
        errors = [response_error, abs(measured_D - D), abs(decomposition - allowed),
                  max(0.0, D - dyadic), max(0.0, dyadic/4 - D),
                  max(0.0, D-source_bound), witness_error]
        assert max(errors) < 2e-6, (q, side, width, errors)
        rows.append(dict(q=q, sign=side, r=width, root=a, c2=c*c,
                         support=m, density_term=density, centered_energy=D,
                         allowed_energy=allowed, dyadic_upper=dyadic,
                         spectral_energy=float(measured_D),
                         band_energy=[float(z) for z in band_energy],
                         sampling_witness=witness,
                         min_eigenvalue=float(spectrum.min(initial=1)),
                         response_error=response_error, identity_error=max(errors),
                         qp_residual=residual))
    return rows


def certificate(q, characteristic, denominator, positive):
    from flint import arb, arb_mat, ctx

    ctx.prec = 192
    signs = list(map(int, previous.paley_sign(characteristic) if q == characteristic
                     else previous.square_field_sign(characteristic)))
    n = len(signs)
    r = arb(1) / denominator
    eta = r*r / (1-r*r)
    d = (1-r)/(1+r)
    kernel = [sum((s*(2*arb.pi()*((i*j) % n)/n).cos()
                   for j, s in enumerate(signs)), arb(0))/n for i in range(n)]
    orthant = [1 if i in positive else -1 for i in range(1, n)]
    matrix = arb_mat([[int(i == j)-d*kernel[(i-j) % n]*orthant[j-1]
                       for j in range(1, n)] for i in range(1, n)])
    beta = matrix.solve(arb_mat([[d*kernel[i]] for i in range(1, n)]))
    assert all(orthant[i-1]*beta[i-1, 0] > 0 for i in range(1, n))
    gamma = d*(kernel[0]+sum((kernel[i]*orthant[i-1]*beta[i-1, 0]
                             for i in range(1, n)), arb(0)))
    assert abs(gamma) < 1
    u0 = 2/(1-gamma**2).sqrt()
    x = [u0*(1+gamma)/2] + [u0*beta[i-1, 0] if orthant[i-1] > 0 else arb(0)
                           for i in range(1, n)]
    y = [u0*(1-gamma)/2] + [-u0*beta[i-1, 0] if orthant[i-1] < 0 else arb(0)
                           for i in range(1, n)]
    for side, xx, yy in [(1, x, y), (-1, y, x)]:
        active = [i for i in range(1, n) if (i in positive) == (side == 1)]
        m = len(active)
        a = xx[0]
        L = sum((xx[i] for i in active), arb(0))
        mean = L/m
        v = [xx[i]-mean for i in active]
        density = L**2/m
        D = sum((t*t for t in v), arb(0))
        c2 = sum(xx, arb(0))**2/n
        Nk = [(int(i == 0)-arb(1)/n-side*kernel[i])/2 for i in range(n)]
        C = [[Nk[(i-j) % n] for j in active] for i in active]
        base = [a*Nk[i]+mean*sum(row, arb(0)) for i, row in zip(active, C)]
        f = [-t+sum(base, arb(0))/m for t in base]
        Cv = [sum((u*t for u, t in zip(row, v)), arb(0)) for row in C]
        cvmean = sum(Cv, arb(0))/m
        response = [u-cvmean+eta*t-z for u, t, z in zip(Cv, v, f)]
        assert all(abs(t) < arb("1e-48") for t in response)
        # Build a separate rational source witness, with no spectral cutoff.
        if m == 1:
            # The centered space is {0}; do not take sqrt of a ball around zero.
            D, bound = arb(0), arb(0)
            epsilon_upper = None
        else:
            means = [sum(row, arb(0))/m for row in C]
            grand = sum(means, arb(0))/m
            CC = [[C[i][j]-means[i]-means[j]+grand for j in range(m)] for i in range(m)]
            raw = arb_mat([[CC[i][j]+(eta/64 if i == j else 0)
                            for j in range(m)] for i in range(m)]).solve(arb_mat([[z] for z in f]))
            scale = 10**12
            numerators = [int((raw[i, 0]*scale).mid().floor().unique_fmpz()) for i in range(m)]
            h = [arb(m*k-sum(numerators))/(m*scale) for k in numerators]
            defects = [f[i]-sum((CC[i][j]*h[j] for j in range(m)), arb(0)) for i in range(m)]
            source_error = sum((z*z for z in defects), arb(0)).sqrt()
            hnorm = sum((z*z for z in h), arb(0)).sqrt()
            bound = (hnorm+source_error/eta)**2
            raw_w = arb_mat([[CC[i][j]+(eta if i == j else 0)
                              for j in range(m)] for i in range(m)]).solve(
                                  arb_mat([[t/D] for t in v]))
            wnums = [int((raw_w[i, 0]*scale).mid().floor().unique_fmpz()) for i in range(m)]
            ww = [arb(m*k-sum(wnums))/(m*scale) for k in wnums]
            contrast = sum((z*t for z, t in zip(f, ww)), arb(0))
            assert contrast > arb(999999)/1000000
            cww = [sum((CC[i][j]*ww[j] for j in range(m)), arb(0)) for i in range(m)]
            leak = sum((t*t for t in cww), arb(0)).sqrt()
            ridge = eta*sum((t*t for t in ww), arb(0)).sqrt()
            epsilon_upper = max(leak.upper(), ridge.upper())/contrast.lower()
            assert epsilon_upper < 1/D.sqrt()+arb("1e-8")
        assert bound < 2*D+arb("1e-44")
        if m > 1:
            assert bound > D
        Nxx = [sum((Nk[(i-j) % n]*xx[j] for j in range(n)), arb(0))
               for i in range(n)]
        forbidden = sum((t*t for t in Nxx), arb(0))
        allowed = sum((t*t for t in xx), arb(0))-c2-forbidden
        identity = allowed-(a*a+density+D-c2-forbidden)
        assert abs(identity) < arb("1e-48")
        print(json.dumps(dict(certificate=f"q={q}, r=1/{denominator}, sign={side}",
                              support=m, density_term=str(density),
                              centered_energy=str(D), allowed_energy=str(allowed),
                              source_upper=str(bound),
                              sampling_epsilon_upper=str(epsilon_upper)), ensure_ascii=False))


def dispersed_model():
    """An abstract compression example, explicitly not a Paley optimizer."""
    for count in [8, 16, 32, 64, 128]:
        indices = np.arange(1, count+1)
        eigenvalues = 2.0**(-indices)
        eta = 2.0**(-count)
        weights = eigenvalues**2/indices
        energy = float(np.sum(weights/(eigenvalues+eta)**2))
        harmonic = float(np.sum(1.0/indices))
        assert harmonic/4 <= energy <= harmonic
        for k in range(count):
            assert weights[k:].sum() <= (4/3)*eigenvalues[k]**2/indices[k]*(1+1e-14)
        print(json.dumps(dict(model="abstract dispersed compression, not Paley",
                              bands=count, energy=energy, low_window_scaled=1/count,
                              source_norm_squared=float(np.sum(weights/eigenvalues)))))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--certificate", action="store_true")
    parser.add_argument("--large", action="store_true")
    parser.add_argument("--dispersed-model", action="store_true")
    args = parser.parse_args()
    if args.dispersed_model:
        dispersed_model()
        return
    if args.certificate:
        certificate(13, 13, 4, {1, 2, 4, 5})
        certificate(49, 7, 28, {4, 6, 12, 18, 20})
        return
    cases = [(p, p) for p in [13, 17, 29, 41, 61, 97, 173, 257, 401]]
    cases += [(p*p, p) for p in [7, 11, 13]]
    if args.large:
        cases += [(p, p) for p in [1009, 1997, 4001]]
        cases += [(p*p, p) for p in [19, 31, 43, 61]]
    for q, characteristic in sorted(cases):
        for width in [.25/np.sqrt(q), q**(-1/3)]:
            for row in check(q, characteristic, width):
                print(json.dumps(row), flush=True)


if __name__ == "__main__":
    main()
