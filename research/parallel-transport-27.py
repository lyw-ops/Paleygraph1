"""Actual-increment signed flat-rectangle diagnostics for Round 27.

The recurrence starts at V_0=0 with the heterogeneous marked activation.
Every trajectory and FFT output is floating point, not an interval proof.
Only the records named integer_normalization use exact integer/rational data.
"""

import argparse
from fractions import Fraction
import json
from math import sqrt
from pathlib import Path
import sys

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from smoothing import kernel_action
from square_control import square_field_sign
from theta import paley_sign


def scalar(x):
    return float(x)


def norm(x):
    return scalar(np.linalg.norm(x))


def signed(x):
    return np.where(x >= 0, 1., -1.)


def checkpoint(order, root, side, tau, step, x, d, c, sign, eta):
    n = len(d)
    m0 = n/sqrt(order)
    y = x+d
    sec = (x+y)/(np.sqrt(x*x+c)+np.sqrt(y*y+c))
    h = sec*d
    nd = kernel_action(sign, h)
    energy = scalar(d @ d)
    un = d/sqrt(energy)
    nu = nd/norm(nd)
    ell = scalar(np.abs(un).sum())
    next_ell = scalar(np.abs(nu).sum())
    sigma = signed(sec)
    sender = sigma*un
    delta = scalar(((1-sec*sec)*un*un).sum())
    mu = scalar(h.sum()**2/(n*energy))
    retention = norm(nd)/sqrt(energy)
    pair = scalar(nu @ kernel_action(sign, sender))
    gamma = max(0., 1-pair)
    gamma_bound = 1-retention+sqrt(max(0., mu*delta))/retention
    cp = ell*next_ell/m0
    cap_error = sqrt(2*gamma)+max(0., cp-1)
    flatten_bound = sqrt(cap_error+cap_error*cap_error)
    half_layer = np.abs(un) >= .5/ell
    saturation = 1-sec*sec <= eta
    selected = half_layer & saturation
    flat = signed(un)*half_layer/ell
    high_flat = signed(un)*selected/ell
    exact_identity_error = abs(retention**2+delta+mu-1)
    if exact_identity_error > 4e-12:
        raise RuntimeError('energy identity failed')
    if gamma > gamma_bound+4e-12:
        raise RuntimeError('signed transport bound failed')
    if norm(un-flat) > flatten_bound+4e-11:
        raise RuntimeError('finite flattening bound failed')
    if norm(un-high_flat) > flatten_bound+2*sqrt(delta/eta)+4e-11:
        raise RuntimeError('high-amplitude flattening bound failed')
    scale = np.sqrt(c)*sqrt((1-eta)/eta)
    if np.any(np.maximum(np.abs(x[selected]), np.abs(y[selected]))+1e-10 < scale[selected]):
        raise RuntimeError('actual endpoint amplitude bound failed')
    high_energy = scalar((un[selected]**2).sum())
    def coherence(weights, mask):
        total = scalar(weights[mask].sum())
        return abs(scalar((weights[mask]*sigma[mask]).sum()))/total if total else None
    rec = dict(kind='increment', order=order, square_root=root, side=side,
               tau=tau, step=step, eta=eta, increment_energy=energy/n,
               energy_ratio=retention**2, activation_loss=delta, mean_loss=mu,
               signed_transport_pair=pair, transport_gap_upper=gamma_bound,
               critical_l1_product=cp, effective_size=ell**2,
               effective_size_over_m0=ell**2/m0,
               next_effective_size_over_m0=next_ell**2/m0,
               half_layer_size=int(half_layer.sum()),
               half_layer_energy=scalar((un[half_layer]**2).sum()),
               half_layer_flat_error=norm(un-flat),
               half_layer_flat_bound=flatten_bound,
               high_layer_size=int(selected.sum()), high_layer_energy=high_energy,
               high_layer_flat_error=norm(un-high_flat),
               high_layer_flat_bound=flatten_bound+2*sqrt(delta/eta),
               saturation_energy=scalar((un[saturation]**2).sum()),
               saturation_energy_lower=1-delta/eta,
               mask_energy_coherence=coherence(un*un, selected),
               mask_count_coherence=coherence(np.ones(n), selected),
               root_energy=scalar(un[0]**2), root_secant_squared=scalar(sec[0]**2),
               direct_recurrence_rms_error=norm(kernel_action(sign, np.sqrt(x*x+c))-y)/sqrt(n),
               identity_error=exact_identity_error)
    if root:
        subfield = np.arange(n) % (root-1) == 0
        rec.update(subfield_high_layer_symmetric_difference=int(np.count_nonzero(selected ^ subfield)),
                   subfield_increment_energy=scalar((un[subfield]**2).sum()),
                   subfield_size=int(subfield.sum()))
    return rec, dict(u=un, sigma=sigma, layer=selected, core=saturation, ell=ell,
                     flat_error=norm(un-high_flat), delta=delta, gamma=gamma,
                     retention=retention, field=x.copy())


def rectangle(sign, m0, first, second):
    a, b = first['layer'], second['layer']
    na, nb = int(a.sum()), int(b.sum())
    if min(na, nb) == 0:
        return dict(source_size=na, receiver_size=nb)
    sa = signed(first['u'])*first['sigma']*a/sqrt(na)
    sb = signed(second['u'])*b/sqrt(nb)
    pair = scalar(sb @ kernel_action(sign, sa))
    size_product = sqrt(na*nb)/m0
    unsigned = scalar((b/sqrt(nb)) @ kernel_action(sign, a/sqrt(na)))
    source_coherence = abs(scalar((signed(first['u'])*first['sigma'])[a].mean()))
    receiver_coherence = abs(scalar(signed(second['u'])[b].mean()))
    result = dict(source_size=na, receiver_size=nb,
                size_product_over_m0=size_product, signed_flat_pair=pair,
                signed_rectangle_deficit=1-pair/size_product,
                best_global_sign_deficit=1-abs(unsigned)/size_product,
                source_sign_coherence=source_coherence,
                receiver_sign_coherence=receiver_coherence,
                source_receiver_symmetric_difference=int(np.count_nonzero(a ^ b)),
                signed_pair_lower=1-first['gamma']-2*first['flat_error']-2*second['flat_error'])
    core_vectors = []
    core_mass = []
    core_ells = []
    layers = []
    for snap in (first, second):
        mass = scalar((snap['u'][snap['core']]**2).sum())
        if mass == 0:
            return result
        vec = snap['u']*snap['core']/sqrt(mass)
        ell = scalar(np.abs(vec).sum())
        core_vectors.append(vec)
        core_mass.append(mass)
        core_ells.append(ell)
        layers.append((np.abs(vec) >= .5/ell) & snap['core'])
    core_pair = scalar(core_vectors[1] @ kernel_action(sign, first['sigma']*core_vectors[0]))
    core_gamma = max(0., 1-core_pair)
    trim_distances = [sqrt(max(0., 2-2*sqrt(m))) for m in core_mass]
    core_gap_upper = .5*(sqrt(2*first['gamma'])+sum(trim_distances))**2
    cp = core_ells[0]*core_ells[1]/m0
    ee = sqrt(2*core_gamma)+max(0., cp-1)
    ff = sqrt(ee+ee*ee)
    errors = [norm(v-signed(v)*s/ell) for v,s,ell in zip(core_vectors,layers,core_ells)]
    if core_gamma > core_gap_upper+4e-12 or max(errors) > ff+4e-11:
        raise RuntimeError('trimmed inverse transport bound failed')
    ka, kb = [int(s.sum()) for s in layers]
    flat_pair = scalar((signed(core_vectors[1])*layers[1]/sqrt(kb)) @
                       kernel_action(sign, first['sigma']*signed(core_vectors[0])*layers[0]/sqrt(ka)))
    size_cp = sqrt(ka*kb)/m0
    core_sizes = [int(snap['core'].sum()) for snap in (first,second)]
    card_cp = sqrt(core_sizes[0]*core_sizes[1])/m0
    card_bound = sqrt(max(0., 2*(1-core_pair/card_cp)))
    card_errors = [norm(v-signed(v)*snap['core']/sqrt(sz))
                   for v,snap,sz in zip(core_vectors,(first,second),core_sizes)]
    if max(card_errors) > card_bound+4e-11:
        raise RuntimeError('cardinality-critical flatness bound failed')
    result['core_inverse'] = dict(core_energy=core_mass, normalized_core_l1_product=cp,
                                 core_signed_transport_pair=core_pair,
                                 core_transport_gap_upper=core_gap_upper,
                                 core_cardinality_product_over_m0=card_cp,
                                 core_uniform_errors=card_errors,
                                 core_uniform_error_bound=card_bound,
                                 flat_errors=errors, flat_error_bound=ff,
                                 flat_source_size=ka, flat_receiver_size=kb,
                                 flat_size_product_over_m0=size_cp,
                                 flat_signed_pair=flat_pair,
                                 flat_signed_rectangle_deficit=1-flat_pair/size_cp,
                                 flat_source_receiver_symmetric_difference=int(np.count_nonzero(layers[0] ^ layers[1])))
    return result


def run(order, root, base_sign, side, tau, depth, starts, window, eta):
    sign = side*base_sign
    n = len(sign)
    c = np.full(n, 4*tau)
    c[0] = 4*n
    x = np.zeros(n)
    d = kernel_action(sign, np.sqrt(c))
    requested = {s+j for s in starts for j in range(window+1)}
    snapshots = {}
    max_identity = max_drift = 0.
    for step in range(depth):
        y = x+d
        sec = (x+y)/(np.sqrt(x*x+c)+np.sqrt(y*y+c))
        nd = kernel_action(sign, sec*d)
        if scalar(d @ d) < 1e-28*n:
            break
        if step in requested:
            rec, snap = checkpoint(order, root, side, tau, step, x, d, c, sign, eta)
            snapshots[step] = snap
            max_identity = max(max_identity, rec['identity_error'])
            max_drift = max(max_drift, rec['direct_recurrence_rms_error'])
            print(json.dumps(rec), flush=True)
        x, d = y, nd
    m0 = n/sqrt(order)
    for start in starts:
        if not all(start+j in snapshots for j in range(window+1)):
            continue
        pairs = [rectangle(sign, m0, snapshots[t], snapshots[t+1])
                 for t in range(start, start+window)]
        two_step = []
        for t in range(start, start+window-1):
            a, b, z = [snapshots[t+j] for j in range(3)]
            pred = kernel_action(sign, b['sigma']*kernel_action(sign, a['sigma']*a['u']))
            entry = dict(step=t, signed_two_step_error=norm(z['u']-pred),
                         two_step_support_symmetric_difference=int(np.count_nonzero(a['layer'] ^ z['layer'])),
                         increment_abs_distance=norm(np.abs(a['u'])-np.abs(z['u'])),
                         width_ratio=z['ell']/a['ell'])
            p0, p1 = pairs[t-start:t-start+2]
            if min(int(a['layer'].sum()),int(b['layer'].sum()),int(z['layer'].sum())):
                ee = sqrt(max(0., p0['size_product_over_m0']**2+1-2*p0['signed_flat_pair']))
                rr = sqrt(np.count_nonzero(z['layer'] & ~a['layer'])/z['layer'].sum())
                lower = p1['signed_flat_pair']-ee-rr
                actual = abs(scalar(b['sigma'][b['layer']].mean()))
                if actual < lower-4e-11:
                    raise RuntimeError('finite return coherence bound failed')
                entry.update(return_rankone_frobenius_upper=ee,
                             return_mask_coherence_lower=lower,
                             return_mask_coherence=actual)
            two_step.append(entry)
        print(json.dumps(dict(kind='window', order=order, square_root=root, side=side,
                              tau=tau, start=start, transitions=window, eta=eta,
                              rectangles=pairs, two_step=two_step)), flush=True)
    print(json.dumps(dict(kind='audit', order=order, square_root=root, side=side,
                          tau=tau, completed_steps=step+1,
                          maximum_checkpoint_identity_error=max_identity,
                          maximum_direct_recurrence_rms_error=max_drift)), flush=True)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--primes', nargs='*', type=int, default=[9413, 153649, 1000033])
    p.add_argument('--square-roots', nargs='*', type=int, default=[97, 389])
    p.add_argument('--sides', nargs='+', type=int, default=[1])
    p.add_argument('--tau', nargs='+', type=float, default=[.05, .001])
    p.add_argument('--depth', type=int, default=260)
    p.add_argument('--starts', nargs='+', type=int, default=[16, 64, 128, 255])
    p.add_argument('--window', type=int, default=3)
    p.add_argument('--eta', type=float, default=.1)
    args = p.parse_args()
    if not 0 < args.eta < 1 or min(args.tau) <= 0 or any(s not in (-1, 1) for s in args.sides):
        p.error('positive floors, eta in (0,1), sides in {-1,1} required')
    cases = [(q, None, paley_sign(q)) for q in args.primes]
    cases += [(r*r, r, square_field_sign(r)) for r in args.square_roots]
    for q, r, sign in cases:
        n = len(sign)
        if sum(map(int, sign)) != -1 or int(sign[0]) != 0 or not np.all(sign[1:]**2 == 1):
            raise RuntimeError('exact normalization failed')
        if not np.array_equal(sign, sign[np.arange(n)*(-1) % n]):
            raise RuntimeError('exact symmetry failed')
        print(json.dumps(dict(kind='integer_normalization', order=q, square_root=r, n=n,
                              kernel_00=str(Fraction(-1,n)), row_energy=str(Fraction(n-1,n)),
                              m0_squared=str(Fraction(n*n,q)))), flush=True)
        if r:
            print(json.dumps(dict(kind='exact_square_shell', order=q, square_root=r,
                                  shell_size=(r-1)//2,
                                  size_ratio=str(Fraction(r,r+1)),
                                  unit_flat_pair=str(Fraction(r*r-3*r-2,r*r-1)),
                                  signed_deficit=str(Fraction(2*(r+1),r*(r-1))))),flush=True)
        for side in args.sides:
            for tau in args.tau:
                run(q, r, sign, side, tau, args.depth, args.starts, args.window, args.eta)


if __name__ == '__main__':
    main()
