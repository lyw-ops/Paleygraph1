"""Signed cut and mass-floor replay for astra-cuts-15.md.

Run from the repository root with .venv/bin/python -B. Output is JSONL;
this script does not itself write files. Supports are numerical unless
--certificate is used (a complete p=13 strict orthant, 192-bit Arb).
"""

import argparse
import importlib.util
import json
from pathlib import Path

import numpy as np

spec = importlib.util.spec_from_file_location(
    "cuts15_previous", Path(__file__).with_name("astra-sampling-14.py")
)
previous = importlib.util.module_from_spec(spec)
spec.loader.exec_module(previous)


def qapply(sign, side, r, v):
    weights = np.where(sign == side, r, 1 / r)
    weights[0] = 1
    return np.fft.ifft(weights * np.fft.fft(v)).real


def check(q, characteristic):
    signs = (previous.previous.paley_sign(q) if q == characteristic
             else previous.previous.square_field_sign(characteristic))
    n = len(signs)
    r = q ** (-1 / 3)
    x, y, _, residual = previous.previous.solve(signs, r)
    kernel = np.fft.ifft(signs).real
    eta, beta = r * r / (1 - r * r), r / (1 + r)
    kappa = (np.sqrt(q) + 1) / (2 * n)
    lam = kappa * np.sqrt(n)
    diag_plus, diag_minus = .5 - 1 / n, .5
    bmass = np.sqrt((diag_plus + kappa) * (diag_minus + kappa))
    eps = .5 * np.sqrt(r * (1 - 1 / n))
    mass_floor = max(0., (bmass - eps) / lam)
    rows = []
    for side, xx, yy in ((1, x, y), (-1, y, x)):
        a, c = xx[0], xx.sum() / np.sqrt(n)
        active = np.flatnonzero(xx[1:] > 1e-8) + 1
        m = len(active)
        if not m:
            continue
        bulk = xx.copy()
        bulk[0] = 0
        E = float(bulk @ bulk)
        L = float(bulk.sum())
        density = L * L / m
        centered = float(np.sum((xx[active] - L / m) ** 2))
        allowed = float(np.sum(previous.projection(signs, xx, side) ** 2))
        Nx = previous.projection(signs, xx, -side)
        Py = previous.projection(signs, yy, side)
        dn = float(np.mean(signs == -side))
        dp = float(np.mean(signs == side))
        err = [max(0., bmass - lam * c - eps * np.sqrt(max(0., 1 - c*c))),
               max(0., mass_floor-c),
               max(0., (dn+kappa)*a-lam*c-Nx[0]),
               max(0., (dp+kappa)/a-lam*c-Py[0]),
               abs(np.dot(Nx,Nx)+np.dot(Py,Py)-r*(1-c*c)),
               abs(E-density-centered)]
        # Uncentered signed source, including the rank-one mean penalty.
        nroot = (np.eye(1, n, 0).ravel()-1/n-side*kernel)/2
        f = -a * (nroot[active] + beta/n)
        Cbulk = previous.projection(signs, bulk, -side)[active] + beta*L/n
        source_residual = float(np.linalg.norm(Cbulk+eta*xx[active]-f))
        err.append(source_residual)
        # All-prefix high cuts on small fields, 32 quantile cuts on large ones.
        sorted_active = active[np.argsort(-xx[active])]
        counts = (np.arange(1, m+1) if n < 260 else
                  np.unique(np.rint(np.linspace(1, m, 32)).astype(int)))
        cuts = []
        for count in counts:
            U = sorted_active[:count]
            u = np.zeros(n)
            u[U] = xx[U]
            v = xx-u
            lu, eu = float(u.sum()), float(u@u)
            Nu = previous.projection(signs, u, -side)
            forbidden = float(Nu@Nu)
            cross = float(side*np.dot(u, np.fft.ifft(signs*np.fft.fft(v)).real)
                          +(1-r)/(1+r)*lu*v.sum()/n)
            surplus = cross-2*forbidden-2*beta*lu*lu/n
            err.append(abs(surplus-2*eta*eu))
            cuts.append(dict(size=int(count), energy=eu, forbidden=forbidden,
                             cut=cross, energy_surplus=surplus,
                             scaled_energy_surplus=surplus/(2*eta)))
        # Tail energy and inverse-density are bounded together by any cut.
        tail_tests = []
        for tscaled in (.25, .5, 1., 2., 4., 8.):
            tau = tscaled/np.sqrt(n)
            high = np.where((xx>tau)&(np.arange(n)!=0),xx,0.)
            eh = float(high@high)
            low_bound = tau*L
            err.append(max(0., E-eh-low_bound))
            tail_tests.append(dict(threshold_times_sqrt_n=tscaled,
                                   high_size=int(np.count_nonzero(high)),
                                   high_energy=eh, low_energy_bound=low_bound))
        length, step = previous.longest_run(signs, side)
        h = previous.fejer(n, length, step)
        qh = r*h+(1-r)/np.sqrt(n)
        ek = length*(2*length+1)/(3*(length+1))
        perturbed = []
        for delta in (length**(-.25), .1, .025):
            u, w = xx+delta*h, yy+delta*qh
            pair_energy = float(u@w)
            omega = float(u[1:]@w[1:])
            # A soft cut 0<=z<=1, with zero root, resolving the added kernel.
            v = delta*h.copy()
            v[0] = 0
            z = np.divide(v,u,out=np.zeros(n),where=u>1e-15)
            potential = u*w
            diagonal = float(np.sum(potential*z*z))
            vqv = float(v@qapply(signs,side,r,v))
            soft_form = vqv-diagonal
            # Direct signed Jacobi Dirichlet form via two FFTs, including diagonal.
            Wv = lambda b: (side*np.fft.ifft(signs*np.fft.fft(b)).real
                            +(1-r)/(1+r)*b.sum()/n)
            signed_sum = float(2*np.dot(u*z*z,Wv(u))-2*np.dot(u*z,Wv(u*z)))
            err.append(abs(soft_form-(1-r*r)/(4*r)*signed_sum))
            cross_mass = float(w@v)
            cauchy_lower = cross_mass*cross_mass/omega if omega>1e-15 else 0.
            err.append(max(0., cauchy_lower-diagonal))
            # The defect in any indicator-cut law is exactly factor*overlap_U.
            # Taking ALL bulk coordinates attains the maximum, no enumeration needed.
            max_cut_defect = 2*r/(1-r*r)*omega
            for which in (np.arange(1,n), active,
                          np.flatnonzero(h > 2/np.sqrt(n))):
                which = which[which != 0]
                cut_u = np.zeros(n)
                cut_u[which] = u[which]
                cut_v = u-cut_u
                lc = cut_u.sum()
                cross = float(cut_u@Wv(cut_v))
                expected = 2*r/(1-r*r)*float(cut_u@qapply(signs,side,r,cut_u))
                defect = expected-cross
                err.append(abs(defect-2*r/(1-r*r)*float(potential[which].sum())))
                err.append(max(0., defect-max_cut_defect))
            # The unscaled opposite potential does not change under h in J+P.
            t0=(1-r)*c/(r*np.sqrt(n))
            t1=(1-r)*(c+delta)/(r*np.sqrt(n))
            z0=xx-yy/r+t0
            z1=u-w/r+t1
            err.append(float(np.max(np.abs(z0-z1))))
            threshold_set=np.flatnonzero((z1>t1+1e-12)&(np.arange(n)!=0))
            expected_set=np.flatnonzero((xx>delta*(1-r)/(r*np.sqrt(n))+1e-12)
                                       &(np.arange(n)!=0))
            assert np.array_equal(threshold_set,expected_set)
            perturbed.append(dict(delta=float(delta), fejer_degree=length,
                allowed_energy=float(np.sum(previous.projection(signs,u,side)**2)/pair_energy),
                bulk_overlap=omega, max_all_cut_defect=max_cut_defect,
                cut_defect_over_r=max_cut_defect/r, soft_q_energy=vqv,
                soft_overlap=diagonal, soft_cauchy_lower=cauchy_lower,
                soft_signed_form=soft_form, signed_jacobi_sum=signed_sum,
                soft_multiplier_min=float(z.min()), soft_multiplier_max=float(z.max()),
                old_support_size=m, potential_level_set_size=len(threshold_set),
                potential_threshold_shift=float(t1-t0),
                relative_rooted_gap=float(pair_energy/(u[0]/a)**2-1)))
        assert max(err)<2e-6,(q,side,max(err))
        rows.append(dict(q=q,characteristic=characteristic,side=side,r=r,
            c2=float(c*c), proved_c2_floor=mass_floor*mass_floor,
            mass_floor_inequality_slack=float(lam*c+eps*np.sqrt(max(0.,1-c*c))-bmass),
            allowed_energy=allowed,bulk_energy=E,density_energy=density,
            centered_energy=centered,support_size=m,source_residual=source_residual,
            qp_residual=residual,identity_error=float(max(err)),cuts=cuts,
            tail_tests=tail_tests,fejer=perturbed))
    return rows


def certificate():
    from flint import arb, arb_mat, ctx
    ctx.prec=192
    q=13
    signs=list(map(int,previous.previous.paley_sign(q)))
    n=len(signs)
    r=arb(q)**(-arb(1)/3)
    damping=(1-r)/(1+r)
    numerical,_,_,_=previous.previous.solve(np.array(signs),q**(-1/3))
    orthant=[1 if numerical[i]>1e-8 else -1 for i in range(1,n)]
    kernel=[sum((s*(2*arb.pi()*((i*j)%n)/n).cos()
                 for j,s in enumerate(signs)),arb(0))/n for i in range(n)]
    matrix=arb_mat([[int(i==j)-damping*kernel[(i-j)%n]*orthant[j-1]
                    for j in range(1,n)] for i in range(1,n)])
    b=matrix.solve(arb_mat([[damping*kernel[i]] for i in range(1,n)]))
    assert all(orthant[i-1]*b[i-1,0]>0 for i in range(1,n))
    gamma=damping*(kernel[0]+sum((kernel[i]*orthant[i-1]*b[i-1,0]
                                 for i in range(1,n)),arb(0)))
    assert abs(gamma)<1
    u0=2/(1-gamma*gamma).sqrt()
    x=[u0*(1+gamma)/2]+[u0*b[i-1,0] if orthant[i-1]>0 else arb(0) for i in range(1,n)]
    y=[u0*(1-gamma)/2]+[-u0*b[i-1,0] if orthant[i-1]<0 else arb(0) for i in range(1,n)]
    eta=r*r/(1-r*r)
    beta=r/(1+r)
    kap=(arb(q).sqrt()+1)/(2*n)
    lam=kap*arb(n).sqrt()
    bm=((arb(1)/2+kap)*(arb(1)/2-arb(1)/n+kap)).sqrt()
    eps=(r*(1-arb(1)/n)).sqrt()/2
    c=sum(x,arb(0))/arb(n).sqrt()
    assert lam*c+eps*(1-c*c).sqrt()-bm>0
    for side,xx in ((1,x),(-1,y)):
        I=[i for i in range(1,n) if xx[i]>0]
        nk=[(int(i==0)-arb(1)/n-side*kernel[i])/2 for i in range(n)]
        C=arb_mat([[nk[(i-j)%n]+beta/n for j in I] for i in I])
        f=arb_mat([[-xx[0]*(nk[i]+beta/n)] for i in I])
        actual=arb_mat([[xx[i]] for i in I])
        for k in range(len(I)):
            assert abs((C*actual)[k,0]+eta*actual[k,0]-f[k,0])<arb('1e-45')
        # A separately rounded rational signed trial; positivity is irrelevant.
        reg=C+arb_mat([[eta/64 if i==j else 0 for j in range(len(I))] for i in range(len(I))])
        trial=reg.solve(f)
        denominator=10**12
        rat=[int(round(float(trial[i,0])*denominator)) for i in range(len(I))]
        h=arb_mat([[arb(v)/denominator] for v in rat])
        error=f-C*h
        hn=sum((h[i,0]**2 for i in range(len(I))),arb(0)).sqrt()
        en=sum((error[i,0]**2 for i in range(len(I))),arb(0)).sqrt()
        bound=(hn+en/eta)**2
        actual_energy=sum((xx[i]**2 for i in I),arb(0))
        assert bound>actual_energy
        print(json.dumps(dict(certificate='p=13 algebraic width, full strict orthant',
            side=side,c2=str(c*c),mass_floor_slack=str(lam*c+eps*(1-c*c).sqrt()-bm),
            bulk_energy=str(actual_energy),signed_source_upper=str(bound),
            rational_trial_numerators=rat,denominator=denominator)))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--large',action='store_true')
    parser.add_argument('--certificate',action='store_true')
    args=parser.parse_args()
    if args.certificate:
        certificate()
        return
    primes=[13,17,29,41,61,97,173,257,401,1009,4001]
    squares=[7,11,13,19,31,43,61]
    if args.large:
        primes += [9413,37253,151337,153649]
        squares += [97,193,389]
    for q,p in sorted([(p,p) for p in primes]+[(p*p,p) for p in squares]):
        for row in check(q,p):
            print(json.dumps(row),flush=True)


if __name__=='__main__':
    main()
