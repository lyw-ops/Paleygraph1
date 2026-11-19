"""Exact Parseval witness for the geometric rank-six Hom space."""

from fractions import Fraction
import json
from pathlib import Path
import runpy


old = runpy.run_path(str(Path(__file__).with_name("rank-four-arithmetic-56-check.py")))
conv = old["cycconv"]


def witness(q):
    base, ell, _, _ = old["data"](q, 1)
    sign = [(-1)**i for i in range(q-1)]
    inv = [s*l for s, l in zip(sign, ell)]
    n = [l*x for l, x in zip(ell, conv(ell, ell))]
    d = [l*(x+2*(q+1)) for l, x in zip(ell, conv(n, n))]
    z = [l*(1+s-x) for l, s, x in zip(ell, sign, conv(inv, d))]
    _, a, _ = old["rank_four_rows"](q, 1)
    ext, a_ext, _ = old["rank_four_rows"](q, 2)
    norm = ext.g**(q+1)
    gen = ext.embed(base, base.g)
    norm_log = next(i for i in range(q-1) if gen**i == norm)
    folded = [0]*(q-1)
    for i, value in enumerate(a_ext):
        folded[i*norm_log % (q-1)] += value
    newton = [x-y for x,y in zip(conv(a,a), folded)]
    diff = [2*q*q*x+y for x,y in zip(z,conv(inv,newton))]
    assert diff == [diff[i%2] for i in range(q-1)]
    z0 = sum(z)
    zchi = sum(x*s for x,s in zip(z,sign))
    energy = Fraction(sum(x*x for x in z), q**5)
    good = energy - Fraction(z0*z0+zchi*zchi,(q-1)*q**5)
    lower = good - Fraction(72,q-1)
    upper = Fraction(12,20) + Fraction(36,q)
    assert q > 20**2 and lower > upper
    return dict(base=q, norm_log=norm_log, good_characters=q-3,
                two_parity_residues=diff[:2], good_parseval_energy=str(good),
                lower_bound=str(lower), upper_bound_without_Hom=str(upper))


if __name__ == "__main__":
    print(json.dumps(witness(401), sort_keys=True))
