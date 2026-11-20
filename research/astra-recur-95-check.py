"""Check the true prime recurrence and the exterior perturbation on a separate prime."""
import json
from pathlib import Path
from random import Random
import runpy
import sys

from flint import acb, arb, ctx

base = Path(__file__).resolve().parent
sys.path.insert(0, str(base.parent))
from theta import paley_sign

prior = runpy.run_path(str(base / "astra-split-83-check.py"))
apply = prior["terminal"]["prior"]["apply_multiplier"]
enclose = prior["interval"]
ctx.prec = 384


def maximum(values):
    result = arb(0)
    for value in values:
        result = result.max(value)
    return result


def true_windows():
    signs = list(map(int, prior["face"]["mask"]))
    n = len(signs)
    root = arb(n).sqrt()
    column = apply([1]+[0]*(n-1), signs)
    x = [root*c for c in column]
    C = list(range(0, n, n//3))
    kernel = [[column[(i-j) % n] for j in C] for i in C]
    contraction = sum(map(abs, kernel[0]))
    assert contraction < arb(2)/3
    rows, _ = prior["face"]["faces"]()
    assert sum(rows[i][0] for i in C) > arb(7)/50
    fields, means, primary, companion, external = [], [], [], [], []
    state = [arb(0)] * n
    bound = arb(0)
    for t in range(34):
        fields.append(state)
        amp = list(map(abs, state))
        beta = (4+(state[0]/root)**2).sqrt()-abs(state[0])/root
        off = apply([u if i not in C else arb(0) for i,u in enumerate(amp)], signs)
        external.append(sum(abs(off[i]) for i in C)/len(C))
        source = amp.copy()
        source[0] += beta*root
        means.append(sum(source)/(2*n))
        primary.append(apply([(a-y)/2 for a,y in zip(source,state)],
                             [int(s <= 0) for s in signs]))
        companion.append(apply([(a+y)/2 for a,y in zip(source,state)],
                               [int(s >= 0) for s in signs]))
        new = apply(source, signs)
        for i,row in zip(C,kernel):
            residual = new[i]-beta*x[i]-off[i]-sum(k*amp[j] for k,j in zip(row,C))
            assert residual.contains(0)
        bound = 2*maximum(abs(x[i]) for i in C)+external[-1]+contraction*bound
        assert sum(abs(new[i]) for i in C)/len(C) < bound
        state = new
    good = [t for t in range(16,31) if all(means[j]<4 for j in (t-1,t,t+1))]
    assert good == list(range(16,31))
    projector = apply([1]+[0]*(n-1), [int(s<0) for s in signs])
    recurrent = dict.fromkeys(C,0)
    for t in good:
        raw = [(2*sum(row[i] for row in primary[1:t])+primary[t][i])/(2*t-1)
               for i in range(n)]
        increment = arb(21)/20*raw[0]/root-sum(raw)/n
        repaired = [v+increment*(1-c/projector[0]) for v,c in zip(raw, projector)]
        for i in C:
            if i == 0:
                continue
            T = arb(1)/100
            assert repaired[i] > -T or repaired[i] < -T
            if repaired[i] < -T:
                assert companion[t][i] > (2*t-1)*T
                recurrent[i] += 1
            upper = 2+abs(fields[t][i])/2+(abs(fields[t-1][i])+abs(fields[t+1][i]))/4
            assert abs(companion[t][i]) < upper
    return dict(prime=97, coset=C, terminal_times=good, physical_mask_visits=recurrent,
                contraction=enclose(contraction), peak_exterior_mean=enclose(maximum(external)),
                peak_true_exterior_height=enclose(maximum(companion[t][i] for t in good
                                                         for i in C if i)))


def perturbation():
    p = 12289
    signs = list(map(int, paley_sign(p)))
    n = len(signs)
    m = 32
    step = n//m
    C = list(range(step//2, n, step))
    members = set(C)
    rng = Random(95)
    half = [-1]*8 + [1]*8
    rng.shuffle(half)
    eta = [arb(0)]*n
    for i, value in zip(C[:m//2],half):
        eta[i] = eta[-i] = arb(value)
    column = apply([1]+[0]*(n-1), signs)
    kernel = [[column[(i-j)%n] for j in C] for i in C]
    kappa = sum(map(abs,kernel[0]))
    lam = sum(kernel[0])
    assert kappa < arb(3)/5
    full = apply(eta, signs)
    cap = arb(5)/32
    source = [arb(0) if i in members else (cap+v.max(-cap).min(cap)).max(0)
              for i,v in enumerate(full)]
    assert all(v >= 0 for v in source)
    drive = apply(source, signs)
    def err(row):
        return (sum(v*v for v in row)/m).sqrt()
    local = [eta[i]+lam for i in C]
    residual = err([drive[i]+sum(k*abs(v) for k,v in zip(row,local))-z
                    for i,row,z in zip(C,kernel,local)])
    error = residual/(1-kappa)
    assert error < arb(1)/3
    z = [arb(0)]*m
    # These steps occur only in the prescribed exterior-input comparison.
    for t in range(80):
        z = [t*drive[i]+sum(k*abs(v) for k,v in zip(row,z)) for i,row in zip(C,kernel)]
    positive = sum(v > 40 for v in z)
    negative = sum(v < -40 for v in z)
    assert min(positive,negative) >= 12
    return dict(prime=p, coset_order=m, coset_offset=C[0],
                contraction=enclose(kappa), source_cap=enclose(maximum(source)),
                mean_eigenvalue=enclose(lam), fixed_point_rms_error_upper=enclose(error),
                time=80, above_half_height=positive, below_negative_half_height=negative)


if __name__ == "__main__":
    for result in (true_windows(), perturbation()):
        print(json.dumps(dict(result, precision_bits=ctx.prec, units="1e-9"), sort_keys=True))
