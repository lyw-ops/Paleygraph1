"""Potential, cut, and coordinate-residual checks for astra-sampling-14.md.

Run from the repository root with .venv/bin/python -B. Writes no files.
All optimizer rows are numerical; --certificate verifies a complete small
orthant with Arb at the algebraic width 13**(-1/3).
"""

import argparse
import importlib.util
import json
from math import gcd
from pathlib import Path

import numpy as np

spec = importlib.util.spec_from_file_location(
    "sampling14_previous", Path(__file__).with_name("astra-convolution-11.py")
)
previous = importlib.util.module_from_spec(spec)
spec.loader.exec_module(previous)


def projection(sign, vector, side):
    return np.fft.ifft((sign == side) * np.fft.fft(vector)).real


def longest_run(sign, side, max_length=64):
    """Integer sign/order test; no assumption that the step is a generator."""
    n = len(sign)
    candidates = np.arange(1, n)
    orders = n // np.gcd(candidates, n)
    best = None
    for length in range(1, max_length + 1):
        keep = (sign[(length * candidates) % n] == side) & (orders > 2 * length)
        candidates, orders = candidates[keep], orders[keep]
        if len(candidates) == 0:
            break
        best = (length, int(candidates[0]))
    if best is None:
        raise ValueError("no non-self-inverse one-step run")
    return best


def fejer(n, length, step):
    # Exact finite Fourier formula, with positivity justified by the square.
    modes = np.zeros(n)
    modes[0] = 1
    for k in range(1, length + 1):
        modes[(k * step) % n] = 1 - k / (length + 1)
        modes[(-k * step) % n] = 1 - k / (length + 1)
    return np.fft.ifft(modes).real * np.sqrt(n)


def check(q, characteristic):
    sign = (previous.paley_sign(q) if q == characteristic
            else previous.square_field_sign(characteristic))
    n = len(sign)
    r = q ** (-1 / 3)
    x, y, _, residual = previous.solve(sign, r)
    kernel = np.fft.ifft(sign).real
    rows = []
    for side, xx, yy in ((1, x, y), (-1, y, x)):
        a, c = xx[0], xx.sum() / np.sqrt(n)
        active = np.flatnonzero(xx[1:] > 1e-8) + 1
        if len(active) == 0:
            continue
        L = xx[active].sum()
        mean = L / len(active)
        D = float(np.sum((xx[active] - mean) ** 2))
        A = float(np.sum(projection(sign, xx, side) ** 2))
        B = float(np.sum(projection(sign, yy, -side) ** 2))
        H = D + (1 - r*r) * B
        eta = r*r / (1-r*r)
        t = (1-r) * c / (r*np.sqrt(n))
        witness = (xx - yy/r + t) / H
        Nx = projection(sign, xx, -side)
        contrast = -a*witness[0] - mean*witness[active].sum()
        center = witness[active] - witness[active].mean()
        errors = [
            np.linalg.norm(Nx + eta*H*witness),
            np.linalg.norm(projection(sign, witness, -side)-witness),
            abs(contrast-1),
            abs(np.linalg.norm(center)-np.sqrt(D)/H),
            abs(r*np.linalg.norm(witness)-(1-r*r)*np.sqrt(B)/H),
            max(0., witness.max()-(a+t)/H),
            np.max(np.abs(witness[active]-(xx[active]+t)/H)),
        ]
        cut_rows = []
        for quantile in (0., .25, .5, .75):
            threshold = float(np.quantile(xx[active], quantile))
            U = active[xx[active] >= threshold]
            u = np.zeros(n)
            u[U] = xx[U]
            v = xx-u
            Nu = projection(sign, u, -side)
            mass = u.sum()
            # Directed cross sum: U first, its complement second.
            cross = (side*np.dot(u, np.fft.ifft(sign*np.fft.fft(v)).real)
                     + (1-r)/(1+r) * mass*v.sum()/n)
            qenergy = r*np.dot(u,u)+(1/r-r)*np.dot(Nu,Nu)+(1-r)*mass*mass/n
            cut_error = abs(cross-2*r/(1-r*r)*qenergy)
            errors.append(cut_error)
            cut_rows.append(dict(size=len(U), cross=float(cross),
                                 rhs=float(2*r/(1-r*r)*qenergy)))
        length, step = longest_run(sign, side)
        h = fejer(n, length, step)
        he = length*(2*length+1)/(3*(length+1))
        delta = length ** (-.25)
        qh = r*h+(1-r)/np.sqrt(n)
        raw_x, raw_y = xx+delta*h, yy+delta*qh
        energy = float(raw_x @ raw_y)
        tx, ty = raw_x/np.sqrt(energy), raw_y/np.sqrt(energy)
        overlap = tx[1:]*ty[1:]
        gradient = np.minimum(tx[1:],ty[1:])
        Aprime = float(np.sum(projection(sign, tx, side)**2))
        # Root-anchored objective divided by the true optimal objective.
        anchored_ratio = energy/(raw_x[0]/a)**2
        positive_cap = delta/energy * (a*(1+r*length)+(length+1)/a)/np.sqrt(n)
        positive_cap += delta**2/energy*(length+1)*(1+r*length)/n
        errors += [
            abs(h.sum()/np.sqrt(n)-1),
            abs(h@h-1-he),
            np.linalg.norm(projection(sign,h,-side)),
            max(0., -h.min()),
            max(0., tx.max()-tx[0]),
            max(0., ty.max()-ty[0]),
            max(0., (A+delta*delta*he-2*delta*c)/energy-Aprime),
            max(0., overlap.max()-positive_cap),
            max(0., gradient.max()-delta*(length+1)/np.sqrt(n*energy)),
            max(0., 1-anchored_ratio),
        ]
        Tp = np.floor((1+np.sqrt(1+4*n))/2)
        C2 = float(xx@xx/(c*c))
        threshold = 1/(1+r*(Tp-1))
        if c*c >= threshold:
            errors.append(max(0., C2-Tp))
        assert max(errors) < 2e-6, (q, side, max(errors))
        rows.append(dict(q=q, sign=side, r=r, actual_allowed_energy=A,
                         actual_opposite_energy=B, actual_centered_energy=D,
                         H=H, potential_contrast=float(contrast),
                         potential_centered_leakage=float(np.linalg.norm(center)),
                         potential_scaled_norm=float(r*np.linalg.norm(witness)),
                         potential_positive_cap=float((a+t)/H),
                         cuts=cut_rows, fejer_degree=length, fejer_step=step,
                         fejer_order=n//gcd(step,n), delta=delta,
                         perturbed_allowed_energy=Aprime,
                         anchored_relative_gap=anchored_ratio-1,
                         total_overlap=float(overlap.sum()),
                         coordinate_overlap=float(overlap.max()),
                         coordinate_overlap_over_r=float(overlap.max()/r),
                         l4_overlap_over_r=float(np.linalg.norm(overlap,ord=4)/r),
                         projected_gradient_over_r=float(gradient.max()/r),
                         coordinate_overlap_upper=float(positive_cap),
                         normalized_mass_squared=float(c*c),
                         hp_vacuity_threshold=float(threshold), C2=C2, Tp=float(Tp),
                         qp_residual=residual, identity_error=float(max(errors))))
    return rows


def certificate():
    from flint import arb, arb_mat, ctx
    ctx.prec = 192
    q = 13
    sign = list(map(int, previous.paley_sign(q)))
    n = len(sign)
    r = arb(q) ** (-arb(1)/3)
    d = (1-r)/(1+r)
    numerical, _, _, _ = previous.solve(np.array(sign), q**(-1/3))
    orthant = [1 if numerical[i] > 1e-8 else -1 for i in range(1,n)]
    kernel = [sum((s*(2*arb.pi()*((i*j)%n)/n).cos()
                   for j,s in enumerate(sign)),arb(0))/n for i in range(n)]
    matrix = arb_mat([[int(i==j)-d*kernel[(i-j)%n]*orthant[j-1]
                       for j in range(1,n)] for i in range(1,n)])
    beta = matrix.solve(arb_mat([[d*kernel[i]] for i in range(1,n)]))
    assert all(orthant[i-1]*beta[i-1,0] > 0 for i in range(1,n))
    gamma = d*(kernel[0]+sum((kernel[i]*orthant[i-1]*beta[i-1,0]
                             for i in range(1,n)),arb(0)))
    assert abs(gamma) < 1
    u0 = 2/(1-gamma*gamma).sqrt()
    x = [u0*(1+gamma)/2]+[u0*beta[i-1,0] if orthant[i-1]>0 else arb(0)
                          for i in range(1,n)]
    y = [u0*(1-gamma)/2]+[-u0*beta[i-1,0] if orthant[i-1]<0 else arb(0)
                          for i in range(1,n)]
    for side, xx, yy in ((1,x,y),(-1,y,x)):
        active = [i for i in range(1,n) if xx[i]>0]
        L = sum((xx[i] for i in active),arb(0))
        mean = L/len(active)
        D = sum(((xx[i]-mean)**2 for i in active),arb(0))
        c = sum(xx,arb(0))/arb(n).sqrt()
        Nk = [(int(i==0)-arb(1)/n-side*kernel[i])/2 for i in range(n)]
        Nxx = [sum((Nk[(i-j)%n]*xx[j] for j in range(n)),arb(0)) for i in range(n)]
        B = sum((v*v for v in Nxx),arb(0))/(r*r)
        H = D+(1-r*r)*B
        t = (1-r)*c/(r*arb(n).sqrt())
        w = [(xx[i]-yy[i]/r+t)/H for i in range(n)]
        contrast = -xx[0]*w[0]-mean*sum((w[i] for i in active),arb(0))
        assert abs(contrast-1)<arb('1e-45')
        assert all(w[i]>t/H for i in active)
        assert all(w[i]<t/H for i in range(1,n) if i not in active)
        U = {active[0]}
        cross = sum((xx[i]*xx[j]*(side*kernel[(i-j)%n]+d/n)
                     for i in U for j in range(n) if j not in U),arb(0))
        uv = [xx[i] if i in U else arb(0) for i in range(n)]
        Nu = [sum((Nk[(i-j)%n]*uv[j] for j in range(n)),arb(0)) for i in range(n)]
        qe = r*sum((v*v for v in uv),arb(0))+(1/r-r)*sum((v*v for v in Nu),arb(0))
        qe += (1-r)*sum(uv,arb(0))**2/n
        assert abs(cross-2*r/(1-r*r)*qe)<arb('1e-45')
        print(json.dumps(dict(certificate='strict orthant at p=13, r=13^(-1/3)',
                              sign=side, D=str(D), H=str(H), contrast=str(contrast),
                              cut_cross=str(cross), cut_rhs=str(2*r/(1-r*r)*qe))))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--large',action='store_true')
    parser.add_argument('--certificate',action='store_true')
    args = parser.parse_args()
    if args.certificate:
        certificate()
        return
    cases = [(p,p) for p in [13,17,29,41,61,97,173,257,401,1009,1997,4001]]
    cases += [(h*h,h) for h in [7,11,13,19,31,43,61]]
    if args.large:
        cases += [(p,p) for p in [9413,37253,153649]]
        cases += [(h*h,h) for h in [97,193,389]]
    for q,h in sorted(cases):
        for row in check(q,h):
            print(json.dumps(row),flush=True)


if __name__ == '__main__':
    main()
