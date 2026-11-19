"""Replay warm Fourier tangent trials and flat three-value obstructions."""
import argparse
import json
from pathlib import Path
import runpy

import numpy as np
from flint import arb, acb, ctx

SUPPORT = runpy.run_path(str(Path(__file__).with_name("astra-strip-45-check.py")))
DEN = 2**42


def warm_coefficients(mask, sigma, modes, sizes):
    plus, minus = SUPPORT["approx"](mask, 0.55, 1.0, 1, 60)
    pair = {1: plus, -1: minus}
    h = np.log(1.1)

    def coefficients(side, advance):
        base, dz = pair[side]
        mean = np.mean(base)
        # z reduces the marked weight, so negate the normalized derivative.
        row = base / mean
        derivative = (row * np.mean(dz) - dz) / mean
        proposed = row + advance * derivative
        fourier = np.fft.rfft(proposed).real / len(mask)
        return [int(round(DEN * sizes[k] * fourier[k])) for k in modes[side]]

    return [coefficients(sigma, 2*h), coefficients(-sigma, 0)]


def check(prime, sigma, saved):
    mask = SUPPORT["paley_sign"](prime)
    n = len(mask)
    reps = np.arange(n//2 + 1)
    sizes = np.full(len(reps), 2)
    sizes[[0,-1]] = 1
    modes = {side: [int(k) for k in reps if mask[k] == side] for side in (1,-1)}
    coef = warm_coefficients(mask, sigma, modes, sizes) if saved is None else saved["coef"]
    if saved is not None:
        assert saved["den"] == DEN

    def row(side, nums):
        assert len(nums) == len(modes[side])
        return [1+sum(arb(v)/DEN*(arb(2*int(i)*k)/n).cos_pi()
                      for k,v in zip(modes[side], nums)) for i in reps]

    ell = row(sigma, coef[0])
    ref = row(-sigma, coef[1])
    assert min(ell+ref) > 0
    f,g = ell[0]/arb(n).sqrt(),ref[0]/arb(n).sqrt()
    overlap = sum(int(sizes[i])*(ell[i]*ref[i]).sqrt() for i in reps[1:])/n
    a = arb(1)/2
    c = arb(n-1)/n
    W = 1+c*a
    V = c*(1-f*g)-overlap**2
    total = 1+W*f*g+a*V
    disc = total**2-4*W*f*g
    assert disc > 0
    lower = 2*f/(total+disc.sqrt())
    loglower = (W.sqrt()*lower).log()
    assert loglower > -arb(17)/1000

    # Eigenspace feasibility is exact by construction. At the flat floor
    # witness three distinct bulk Jacobi values without any stationary solve.
    column = [t.real/n for t in acb.dft([acb(int(m)) for m in mask])]
    indices = [1,2,3]
    values = [column[i] for i in indices]
    assert all(abs(x-y)>0 for j,x in enumerate(values) for y in values[j+1:])
    return dict(prime=prime, sign=sigma, a="1/2", b="11/20", den=DEN,
                coef=coef, lower_log_mark=str(loglower), flat_indices=indices,
                flat_column=list(map(str,values)))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--replay", type=Path)
    args = parser.parse_args()
    saved = {}
    if args.replay:
        for line in args.replay.read_text().splitlines():
            r = json.loads(line)
            saved[r["prime"], r["sign"]] = r
    ctx.prec = 192
    for p in (97,173):
        for side in (1,-1):
            record = saved[p,side] if args.replay else None
            print(json.dumps(check(p,side,record),sort_keys=True))
