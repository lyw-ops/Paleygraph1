"""Round 17: localized actual duals and signed current across potential levels.

Run from the repository root with .venv/bin/python -B. Prints JSONL only.
The default support solves are numerical; --certificate verifies p=29
at its exact algebraic width with Arb. No shared script is modified.
"""

import argparse
import importlib.util
import json
from pathlib import Path

import numpy as np
from scipy.sparse.linalg import LinearOperator, cg

spec = importlib.util.spec_from_file_location(
    "preimage17_source", Path(__file__).with_name("astra-source-16.py")
)
source = importlib.util.module_from_spec(spec)
spec.loader.exec_module(source)


def replay(p, square=False):
    signs = source.previous.square_field_sign(p) if square else source.previous.paley_sign(p)
    q, n = (p*p if square else p), len(signs)
    r = q**(-1/3)
    eta, beta = r*r/(1-r*r), r/(1+r)
    x, y, _, qp_residual = source.previous.solve(signs, r)
    for side, xx, yy in ((1, x, y), (-1, y, x)):
        I = np.flatnonzero(xx[1:] > 1e-8)+1
        v = xx[I]
        E = float(v@v)
        if E == 0:
            continue
        def R(z):
            return np.fft.ifft((signs == -side)*np.fft.fft(z)).real + beta*z.mean()
        def extend(z):
            ans = np.zeros(n)
            ans[I] = z
            return ans
        def T(z):
            return R(extend(z))[I]+eta*z
        op = LinearOperator((len(I), len(I)), matvec=T, dtype=float)
        def dual(z):
            w, info = cg(op, z, rtol=2e-12, atol=2e-13, maxiter=10000)
            assert info == 0, (q, side, info)
            return extend(w), R(extend(w)), float(np.linalg.norm(T(w)-z))
        w, d, solve_error = dual(v/E)
        error = [abs(-xx[0]*d[0]-1), solve_error,
                 np.linalg.norm(T(v)+xx[0]*R(np.eye(1,n,0).ravel())[I])]
        potential = - (R(xx)-beta*xx.mean())/eta
        t = beta*xx.mean()/eta
        error.append(float(np.max(np.abs((potential-t)[1:]-(xx-yy/r)[1:]))))
        def budget(ww, dd):
            return float(dd[I]@dd[I]+eta*eta*(ww@ww)+2*eta*(dd@dd)
                         +2*eta*beta*(1-beta)*ww.sum()**2/n)
        error.append(abs(budget(w,d)-1/E))
        trials = []
        for lam in (.5, 1., 2., 4.):
            U = I[v > lam/np.sqrt(n)]
            if not len(U):
                trials.append(dict(lambda_=lam, size=0))
                continue
            L = np.setdiff1d(I,U)
            EU = float(xx[U]@xx[U])
            EL = E-EU
            forcing = np.where(v > lam/np.sqrt(n),v/EU,0.)
            wu, du, solve_u_error = dual(forcing)
            error += [solve_u_error, abs(-xx[0]*du[0]-1),
                      abs(budget(wu,du)-1/EU),
                      abs(budget(wu-w,du-d)-EL/(E*EU)),
                      float(np.linalg.norm(du[L]+eta*wu[L])), max(0.,EL-lam)]
            mean_cost = beta*(1-beta)*wu.sum()**2/n
            H = float(du@du)+mean_cost+eta*float(wu[L]@wu[L])
            mixed = float(wu[U]@du[U])
            ratios = eta*EU*wu[U]/xx[U]
            prob = xx[U]**2/EU
            dimensionless = eta*EU*H
            core = (ratios > 0) & (ratios < 1)
            core_mass = float(prob[core].sum())
            error += [abs(mixed-H),
                      abs(float(prob@(ratios*(1-ratios)))-dimensionless),
                      max(0.,4*dimensionless-core_mass)]
            cuts = []
            # Every listed cut is a genuine superlevel set of the actual potential.
            for threshold in sorted(set([0., lam/4, lam/2, lam, 2*lam])):
                V = I[v > threshold/np.sqrt(n)]
                xv, wv = np.zeros(n), np.zeros(n)
                xv[V], wv[V] = xx[V], wu[V]
                root = float(-xx[0]*wv@R(np.eye(1,n,0).ravel()))
                flux = float(-wv@R(xx-xv)+xv@R(wu-wv))
                expected = float(np.sum(xx[np.intersect1d(U,V)]**2)/EU)
                mean_flux = float(-beta/n*((xx-xv).sum()*wv.sum()
                                           -xv.sum()*(wu-wv).sum()))
                error += [abs(flux-expected)]
                if threshold <= lam:
                    error += [abs(flux-1)]
                cuts.append(dict(threshold_times_sqrt_n=threshold,
                    size=len(V), flux=flux, root_flux=root,
                    bulk_flux=flux-root, mean_flux=mean_flux))
            trials.append(dict(lambda_=lam,size=len(U),high_energy=EU,
                discarded_energy=EL,root_contrast=float(-xx[0]*du[0]),
                response_change_budget=budget(wu-w,du-d),
                exact_change_budget=EL/(E*EU),
                low_preimage_norm_fraction=float(np.linalg.norm(wu[L])/np.linalg.norm(wu)),
                low_potential_norm_fraction=float(np.linalg.norm(du[L])/np.linalg.norm(du)),
                negative_preimage_norm_fraction=float(np.linalg.norm(np.minimum(wu,0))/np.linalg.norm(wu)),
                profile_D=dimensionless,balanced_core_energy_fraction=core_mass,
                mixed_high_pairing=mixed,profile_ratios_min=float(ratios.min()),
                profile_ratios_max=float(ratios.max()),cuts=cuts))
        square_profile = None
        if square and side == 1:
            Hidx=np.arange(0,n,p-1)
            k=len(Hidx)
            kmean=k/np.sqrt(n)
            # N 1_H=0. These formulas do not assume H\{0} is active.
            bx=float(xx[Hidx].sum()); by=float(yy[Hidx].sum())
            bw=float(w[Hidx].sum()); bd=float(d[Hidx].sum())
            error += [abs(r*bx+(1-r)*kmean*xx.sum()/np.sqrt(n)-by),
                      abs(bd-beta*k*w.sum()/n)]
            c=xx.sum()/np.sqrt(n)
            lower=max(0.,(1/xx[0]-(1-r)*kmean*c)/r-xx[0])
            localE=float(xx[Hidx[1:]]@xx[Hidx[1:]])
            error.append(max(0.,lower**2/(k-1)-localE))
            if np.all(xx[Hidx[1:]] > 1e-8):
                error.append(abs(eta*bw+beta*k*w.sum()/n
                                 -(bx-xx[0])/E+1/xx[0]))
            square_profile=dict(size=k,all_bulk_active=bool(np.all(xx[Hidx[1:]]>1e-8)),
                bulk_energy=localE,energy_fraction=localE/E,
                proved_local_energy_lower=lower**2/(k-1),
                primal_mass=bx,dual_preimage_sum=bw,
                preimage_norm_fraction=float(np.linalg.norm(w[Hidx])/np.linalg.norm(w)))
        assert max(error)<2e-7,(q,side,max(error))
        yield dict(q=q,characteristic=p,side=side,r=r,bulk_energy=E,
            support_size=len(I),qp_residual=qp_residual,identity_error=max(error),
            canonical_negative_norm_fraction=float(np.linalg.norm(np.minimum(w,0))/np.linalg.norm(w)),
            canonical_preimage_min=float(w[I].min()),
            canonical_profile_D=float(eta*E*(w[I]@d[I])),
            canonical_budget=budget(w,d),localized=trials,square_profile=square_profile)


def certificate():
    from flint import arb, arb_mat, ctx
    ctx.prec=192
    p=29
    signs=list(map(int,source.previous.paley_sign(p)))
    n=len(signs)
    r=arb(p)**(-arb(1)/3)
    eta,beta=r*r/(1-r*r),r/(1+r)
    numerical,opposite,_,_=source.previous.solve(np.array(signs),p**(-1/3))
    for side,approx in ((1,numerical),(-1,opposite)):
        I=[i for i in range(1,n) if approx[i]>1e-8]
        rk=[sum(((2*arb.pi()*((i*j)%n)/n).cos()
                 for j,s in enumerate(signs) if s==-side),arb(0))/n+beta/n
            for i in range(n)]
        T=arb_mat([[rk[(i-j)%n]+(eta if i==j else 0) for j in I] for i in I])
        bi=T.solve(arb_mat([[-rk[i]] for i in I]))
        assert all(bi[j,0]>0 for j in range(len(I)))
        b=[arb(0) for _ in range(n)];b[0]=arb(1)
        for j,i in enumerate(I):b[i]=bi[j,0]
        qb=[(sum((rk[(i-j)%n]*b[j] for j in range(n)),arb(0))+eta*b[i])*(1/r-r)
            for i in range(n)]
        assert all(qb[i]>0 for i in range(1,n) if i not in I)
        a=1/qb[0].sqrt()
        x=[a*z for z in b]
        E=sum((x[i]**2 for i in I),arb(0))
        def dual(z):
            small=T.solve(arb_mat([[value] for value in z]))
            w=[arb(0) for _ in range(n)]
            for j,i in enumerate(I):w[i]=small[j,0]
            d=[sum((rk[(i-j)%n]*w[j] for j in I),arb(0)) for i in range(n)]
            assert abs(-a*d[0]-1)<arb('1e-45')
            return w,d
        w,d=dual([x[i]/E for i in I])
        negative=[i for i in I if w[i]<0]
        assert negative
        lam=arb(1)
        U=[i for i in I if x[i]*arb(n).sqrt()>lam]
        assert U and all(abs(x[i]*arb(n).sqrt()-lam)>arb('1e-20') for i in I)
        EU=sum((x[i]**2 for i in U),arb(0))
        wu,du=dual([x[i]/EU if i in U else arb(0) for i in I])
        L=[i for i in I if i not in U]
        assert all(abs(du[i]+eta*wu[i])<arb('1e-45') for i in L)
        H=sum((z*z for z in du),arb(0))+beta*(1-beta)*sum(wu,arb(0))**2/n+eta*sum((wu[i]**2 for i in L),arb(0))
        mixed=sum((wu[i]*du[i] for i in U),arb(0))
        assert abs(H-mixed)<arb('1e-43')
        D=eta*EU*H
        ratios=[eta*EU*wu[i]/x[i] for i in U]
        assert all(abs(z)>arb('1e-20') and abs(z-1)>arb('1e-20') for z in ratios)
        core=sum((x[i]**2/EU for i,z in zip(U,ratios) if z>0 and z<1),arb(0))
        assert core-4*D>0
        print(json.dumps(dict(certificate='p=29 exact algebraic width; strict actual KKT',
            side=side,support=I,negative_preimage_indices=negative,
            negative_preimage_values=[str(w[i]) for i in negative],
            high_cut=U,root_contrast=str(-a*du[0]),
            high_mixed_pairing=str(mixed),profile_D=str(D),
            balanced_core_energy_fraction=str(core),core_bound_slack=str(core-4*D))))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--large',action='store_true')
    parser.add_argument('--certificate',action='store_true')
    args=parser.parse_args()
    if args.certificate:
        certificate();return
    cases=[(p,False) for p in (13,29,97,401,1009,4001)]
    cases += [(p,True) for p in (7,19,31,61)]
    if args.large:
        cases += [(p,False) for p in (9413,37253,153649)]
        cases += [(p,True) for p in (97,193,389)]
    for p,square in sorted(cases,key=lambda t:t[0]**(2 if t[1] else 1)):
        for row in replay(p,square):
            print(json.dumps(row),flush=True)


if __name__=='__main__':
    main()
