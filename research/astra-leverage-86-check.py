"""Certify the time-four hinge-source price after removing the frozen head."""
import json
import runpy
from pathlib import Path

from flint import arb, arb_mat, ctx

previous = runpy.run_path(str(Path(__file__).with_name("astra-capacity-84-check.py")))
ctx.prec = 384
dot = previous["dot"]
units = previous["units"]


def calculate(erased):
    n = 48
    sites, basis, height, _, energy, _ = previous["model"]()
    marks = [0] + sites
    base = [row[0] for row in basis]
    root = base[0]
    threshold = (1-root)/(5*arb(n).sqrt())
    mask = [i for i in sites if height[i] > 0]
    assert all(base[i] > threshold or base[i] < threshold for i in mask)
    hinge = [(base[i]-threshold).max(0) if i in mask else arb(0) for i in range(n)]
    v = [value/sum(hinge) for value in hinge]
    assert all(v[i] > 0 for i in erased)
    f = [arb(n).sqrt()*value if i not in erased else arb(0) for i,value in enumerate(v)]

    # The full even slice has two nonnegative anchor parameters.
    beta = dot(f,base)
    slopes = [dot(f,[row[k] for row in basis]) for k in (1,2)]
    assert beta > 0 and all(value > 0 for value in slopes)
    slack = [arb(0)]*n
    for j,k in ((10,1),(21,2)):
        assert basis[j][0].is_zero() and basis[j][3-k].is_zero() and basis[j][k] > 0
        slack[j] = slack[n-j] = slopes[k-1]/(2*basis[j][k])
    residual = [x-z for x,z in zip(f,slack)]
    assert (dot(residual,base)-beta).contains(0)
    assert all(dot(residual,[row[k] for row in basis]).contains(0) for k in (1,2))

    weights = [4*root]*n
    weights[0] = root**2
    for i in mask:
        if i not in erased:
            weights[i] = (energy[i]/5).min(arb(4)/(n*(1+height[i])))
    matrix = arb_mat([[value/weights[i].sqrt() for value in basis[i]] for i in marks])
    gram = matrix.transpose()*matrix
    assert gram.det() > 0 and gram[0,1] > 0 and gram[0,2] > 0
    # Nonnegative anchors and the strictly positive slopes of both linear
    # prices certify the same even exposed row and positive norm minimum.
    assert all(base[i] > 0 or base[i].is_zero() for i in marks)
    ell_pos = 1/gram[0,0]
    unit = arb_mat([[int(i == 0)] for i in marks])
    rootcol = list(matrix*gram.solve(matrix.transpose()*unit))
    ell = rootcol[0]
    y = [arb(0)]*n
    for i,z in zip(marks,rootcol):
        y[i] = weights[i].sqrt()*z/ell
    assert (y[0]-root).contains(0) and (sum(y)-1).contains(0)
    assert all(y[i] < 0 for i in (10,21,27,38))
    signed_cost = dot(y,f)
    signed_slack_debit = dot([(-value).max(0) for value in y],slack)
    assert (signed_slack_debit+signed_cost-beta).contains(0)
    c_f = sum(weights[i]*f[i]**2 for i in sites)
    price_upper = c_f/(c_f+beta**2)
    assert ell_pos < price_upper and price_upper < ell
    cap_allowance = arb(n).sqrt()*root*sum((v[i] for i in erased),arb(0))
    guaranteed = dot([arb(n).sqrt()*value for value in v],base)-cap_allowance
    assert guaranteed < beta if erased else (guaranteed-beta).contains(0)
    return dict(prime=97,time=4,precision=ctx.prec,units="1e-9",
                frozen_head_used=False,freed_mask_sites=erased,
                signed_leverage=units(ell),positive_leverage=units(ell_pos),
                source_face_signed_leverage=units(ell_pos),exact_source_floor=units(beta),
                cap_erasure_floor=units(guaranteed),source_leverage_upper=units(price_upper),
                signed_source_price=units(signed_cost),
                signed_negative_slack_charge=units(signed_slack_debit),
                positive_slack_anchors=[10,21])


if __name__ == "__main__":
    for erase in ([], [5,43]):
        print(json.dumps(calculate(erase),sort_keys=True))
