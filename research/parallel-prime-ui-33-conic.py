"""Small actual-Paley conic optimizations with rigorous primal/dual replay.

SLSQP and LP only propose witnesses. The replay checks exact rational Fourier
supports, positivity, the floor, and the weak-duality formula in the note.
"""

import argparse
from fractions import Fraction
import gzip
import importlib.util
import json
from pathlib import Path
import sys

import numpy as np
from scipy.optimize import LinearConstraint, linprog, minimize

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("prime_ui_33", HERE / "parallel-prime-ui-33.py")
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)


def basis(sign, side):
    n = len(sign)
    columns = [j for j in range(1, n//2+1) if sign[j] == side]
    matrix = np.cos(2*np.pi*np.outer(np.arange(n), columns)/n)
    matrix *= [1 if 2*j == n else 2 for j in columns]
    return columns, matrix


def rounded_fourier(sign, side, spectrum, scale, dc):
    n = len(sign)
    coeff = np.fft.fft(spectrum).real/n
    half = [dc]
    half += [round(float(coeff[j])*scale) if sign[j] == side else 0
             for j in range(1, n//2+1)]
    return half + (half[-2:0:-1] if n % 2 == 0 else half[:0:-1])


def propose(order, root, tau, kappa, output):
    sign = base.signs(order, root)
    n = len(sign)
    cp, bp = basis(sign, 1)
    cm, bm = basis(sign, -1)
    dplus, dminus = len(cp), len(cm)
    constraint = np.zeros((2*n, dplus+dminus))
    constraint[:n, :dplus] = bp
    constraint[n:, dplus:] = bm
    W = 1+(n-1)*float(tau)/n
    m = np.full(n, float(tau)/W)
    m[0] = n/W
    def objective(x):
        p = np.maximum(1+bp@x[:dplus], 1e-12)
        q = np.maximum(1+bm@x[dplus:], 1e-12)
        value = float(2-2*np.mean(np.sqrt(m*p*q)))
        gradient = -np.r_[bp.T@np.sqrt(m*q/p), bm.T@np.sqrt(m*p/q)]/n
        return value, gradient
    fitted = minimize(objective, np.zeros(dplus+dminus), jac=True, method="SLSQP",
                      constraints=[LinearConstraint(constraint, float(kappa)-1, np.inf)],
                      options={"ftol": 2e-14, "maxiter": 2000})
    p, q = 1+bp@fitted.x[:dplus], 1+bm@fitted.x[dplus:]
    # Repair slight LP/SLSQP feasibility errors and provide rounding margin.
    for arr in (p, q):
        shift = max(0., (float(kappa)+1e-10-float(arr.min()))/(1-float(kappa)-1e-10))
        arr[:] = (arr+shift)/(1+shift)
    alpha, beta = np.sqrt(m*q/p), np.sqrt(m*p/q)
    def cover(target, mat):
        fit = linprog(np.r_[1., np.zeros(mat.shape[1])],
                      A_ub=-np.column_stack([np.ones(n), mat]), b_ub=-target,
                      bounds=[(None, None)]*(mat.shape[1]+1), method="highs")
        if not fit.success:
            raise RuntimeError(fit.message)
        return mat@fit.x[1:]
    zm, zp = cover(alpha, bm), cover(beta, bp)
    scale = 2**90
    payload = {"schema": "prime-ui-33-conic-primal-dual-v1", "q": order,
               "square_root": root, "tau": str(tau), "kappa": str(kappa),
               "scale": scale,
               "plus": rounded_fourier(sign, 1, p, scale, scale),
               "minus": rounded_fourier(sign, -1, q, scale, scale),
               "cover_minus": rounded_fourier(sign, -1, zm, scale, 0),
               "cover_plus": rounded_fourier(sign, 1, zp, scale, 0),
               "lambda": [max(1, round(float(x)*scale)) for x in np.sqrt(q/p)],
               "untrusted_optimizer_success": bool(fitted.success),
               "untrusted_optimizer_message": str(fitted.message),
               "untrusted_optimizer_objective": float(fitted.fun)}
    base.save_input(payload, output)
    return payload


def replay(path, precision):
    from flint import acb, arb, ctx
    ctx.prec = precision
    payload = json.loads(gzip.decompress(Path(path).read_bytes()))
    assert payload["schema"] == "prime-ui-33-conic-primal-dual-v1"
    sign = base.signs(payload["q"], payload["square_root"])
    n, scale = len(sign), payload["scale"]
    assert isinstance(scale, int) and scale > 0
    def ball(x):
        x = Fraction(x)
        return arb(x.numerator)/x.denominator
    tau, kappa = ball(payload["tau"]), ball(payload["kappa"])
    assert tau > 0 and 0 < kappa < 1
    W = 1+(n-1)*tau/n
    m = [n/W]+[tau/W]*(n-1)
    spectra = {}
    for key, side, dc in (("plus",1,scale),("minus",-1,scale),
                          ("cover_minus",-1,0),("cover_plus",1,0)):
        coeff = payload[key]
        assert len(coeff) == n and all(isinstance(x, int) for x in coeff)
        assert coeff[0] == dc and coeff[1:] == coeff[:0:-1]
        assert all(x == 0 for j,x in enumerate(coeff) if j and sign[j] != side)
        transform = acb.dft(coeff)
        assert all(x.imag.contains(0) for x in transform)
        spectra[key] = [x.real/scale for x in transform]
    p,q = spectra["plus"], spectra["minus"]
    assert all(x >= kappa for x in p+q)
    gap = sum((mm.sqrt()-(pp*qq).sqrt())**2 for mm,pp,qq in zip(m,p,q))/n
    lam = payload["lambda"]
    assert len(lam) == n and all(isinstance(x,int) and x > 0 for x in lam)
    alpha = [mm.sqrt()*arb(x)/scale for mm,x in zip(m,lam)]
    beta = [mm.sqrt()*scale/x for mm,x in zip(m,lam)]
    # alpha*beta=m exactly by construction, not a midpoint product check.
    margin = arb(2)**(-precision//2)
    aa = max((x-z).upper() for x,z in zip(alpha,spectra["cover_minus"])) + margin
    bb = max((x-z).upper() for x,z in zip(beta,spectra["cover_plus"])) + margin
    assert all(aa+z >= x for x,z in zip(alpha,spectra["cover_minus"]))
    assert all(bb+z >= x for x,z in zip(beta,spectra["cover_plus"]))
    dual = 2-(1-kappa)*(aa+bb)-kappa*(sum(alpha)+sum(beta))/n
    lower = max(arb(0),dual.lower())
    upper = gap.upper()
    assert lower <= upper
    base.emit({"kind": "arb_conic_primal_dual_bracket", "q": payload["q"],
               "square_root": payload["square_root"], "tau": payload["tau"],
               "kappa": payload["kappa"], "precision_bits": precision,
               "optimal_defect_lower": str(lower), "optimal_defect_upper": str(upper),
               "optimal_slope_lower": str((lower/kappa).lower()),
               "optimal_slope_upper": str((upper/kappa).upper()),
               "bracket_width_upper": str((upper-lower).upper()),
               "exact_certificate_input": Path(path).name,
               "untrusted_optimizer_success": payload["untrusted_optimizer_success"]})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--primes", type=int, nargs="*", default=[])
    parser.add_argument("--square-roots", type=int, nargs="*", default=[])
    parser.add_argument("--tau", default="1/20")
    parser.add_argument("--kappa", nargs="+", default=["1/100", "1/20", "1/10"])
    parser.add_argument("--output-prefix", type=Path, default=HERE/"parallel-prime-ui-33-conic")
    parser.add_argument("--replay", type=Path)
    parser.add_argument("--precision", type=int, default=160)
    args = parser.parse_args()
    if args.replay:
        replay(args.replay, args.precision)
        return
    tau = Fraction(args.tau)
    base.prefix_path(args.output_prefix)
    for order,root in ([(x,None) for x in args.primes]+
                       [(x*x,x) for x in args.square_roots]):
        for value in args.kappa:
            kappa = Fraction(value)
            path = Path(f"{args.output_prefix}-q{order}-k{kappa.numerator}_{kappa.denominator}-input.json.gz")
            propose(order, root, tau, kappa, path)
            replay(path, args.precision)


if __name__ == "__main__":
    main()
