"""Round 18: signed low-layer root contributions and Schur screening.

All default actual-QP rows are numerical, not support certificates.
--certificate uses Arb for genuine-prime strict KKT and the two-sector
counterexample. --large adds comparisons through q about 150,000.
Prints JSONL and does not modify shared files.
"""
import argparse
import importlib.util
import json
from pathlib import Path

import numpy as np
from scipy.sparse.linalg import LinearOperator, cg

spec = importlib.util.spec_from_file_location(
    "low18_previous", Path(__file__).with_name("astra-preimage-17.py"))
previous = importlib.util.module_from_spec(spec)
spec.loader.exec_module(previous)


def actual_case(p, square=False):
    signs = (previous.source.previous.square_field_sign(p) if square
             else previous.source.previous.paley_sign(p))
    q, n = (p*p if square else p), len(signs)
    r = q**(-1/3)
    eta, beta = r*r/(1-r*r), r/(1+r)
    x, y, _, qp_residual = previous.source.previous.solve(signs, r)
    for side, xx in ((1, x), (-1, y)):
        I = np.flatnonzero(xx[1:] > 1e-8)+1
        v, a = xx[I], xx[0]
        E = float(v@v)
        if not E:
            continue
        def extend(z, idx):
            out = np.zeros(n); out[idx] = z
            return out
        def R(z):
            return np.fft.ifft((signs == -side)*np.fft.fft(z)).real+beta*z.mean()
        def block(idx, z):
            return R(extend(z, idx))[idx]+eta*z
        solve_errors = []
        def solve(idx, z):
            if not len(idx):
                return np.array([])
            op = LinearOperator((len(idx), len(idx)),
                                matvec=lambda zz: block(idx, zz), dtype=float)
            ans, info = cg(op, z, rtol=2e-12, atol=2e-13, maxiter=15000)
            assert info == 0, (q, side, len(idx), info)
            solve_errors.append(float(np.linalg.norm(block(idx, ans)-z)))
            return ans
        e0 = extend([1.], np.array([0]))
        rootcol = R(e0)
        f = -a*rootcol[I]
        error = [float(np.linalg.norm(block(I, v)-f))]
        canonical = solve(I, v/E)
        trials = []
        for lam in (.5, 1., 2., 4.):
            high = v > lam/np.sqrt(n)
            U, L = I[high], I[~high]
            if not len(U) or not len(L):
                trials.append(dict(lambda_=lam, high_size=len(U), low_size=len(L)))
                continue
            EU, EL = float(v[high]@v[high]), float(v[~high]@v[~high])
            forcing = np.where(high, v/EU, 0.)
            w = solve(I, forcing)
            wU, wL, fL = w[high], w[~high], f[~high]
            fullw = extend(w, I)
            d = R(fullw)
            z = solve(L, fL)  # root-only low solve, may have both signs
            Dv = block(L, v[~high]); Dw = block(L, wL)
            Btv = R(extend(v[high], U))[L]
            Btw = R(extend(wU, U))[L]
            h = z-v[~high]  # D^-1 B^T v_U, using the actual primal relation
            nu = float(fL@z)
            leverage_ceiling = float(f@v)
            kroot = r/(1-r*r)
            error += [max(0.,nu-leverage_ceiling),
                      abs(leverage_ceiling-(a*a*(rootcol[0]+eta)-kroot))]
            s = float(wL@Dw)
            ell = float(v[~high]@Dv)
            alpha = float(h@Btv)
            kappa = float(fL@wL)
            # kappa = - <D^-1/2 B^T v_U, D^-1/2 B^T w_U>
            #         + <D^1/2 v_L, D^1/2 w_L>.
            mixed = float(h@Btw)
            low_error = float(v[~high]@Dw)
            denom = np.sqrt(max(0., alpha*s))
            cosine = mixed/denom if denom else None
            schur_bound = np.sqrt(max(0., nu*s))
            triangle_error = np.sqrt(max(0., ell*s))
            corr = kappa/schur_bound if schur_bound else None
            lower = max(0., abs(mixed)-triangle_error)
            upper = abs(mixed)+triangle_error
            normlow = float(np.linalg.norm(wL)/np.linalg.norm(w))
            error += [abs(kappa+float(f[high]@wU)-1),
                      abs(-a*d[0]-1), float(np.linalg.norm(Dw+Btw)),
                      float(np.linalg.norm(block(L, h)-Btv)),
                      abs(kappa+mixed-low_error),
                      max(0.,abs(kappa)-schur_bound),
                      max(0.,abs(low_error)-triangle_error),
                      max(0.,abs(np.sqrt(max(0.,nu))-np.sqrt(max(0.,alpha)))-np.sqrt(max(0.,ell))),
                      max(0.,ell-(1+eta)*EL), max(0.,EL-lam),
                      max(0.,lower-abs(kappa)),max(0.,abs(kappa)-upper)]
            cuts=[]
            for level in (0.,lam/2,lam):
                V=I[v>level/np.sqrt(n)]
                xv=extend(xx[V],V);wv=extend(fullw[V],V)
                flux=float(-wv@R(xx-xv)+xv@R(fullw-wv))
                root_flux=float(-a*wv@rootcol)
                error.append(abs(flux-1))
                cuts.append(dict(level_times_sqrt_n=level,total_current=flux,
                    root_current=root_flux,internal_current=flux-root_flux))
            square_profile=None
            if square and side == 1:
                H=np.arange(0,n,p-1)
                HL=np.intersect1d(H,L)
                lowpot=R(extend(wL,L))
                root_by_H=a*lowpot[H[1:]].sum()-a*beta*len(H)*wL.sum()/n
                error.append(abs(root_by_H-kappa))
                square_profile=dict(subfield_size=len(H),subfield_low_size=len(HL),
                    subfield_high_size=len(np.intersect1d(H,U)),
                    subfield_low_energy=float(xx[HL]@xx[HL]),
                    low_root_via_subfield=float(root_by_H),
                    subfield_high_transfer=float(a*lowpot[H[1:]].sum()),
                    subfield_mean_correction=float(-a*beta*len(H)*wL.sum()/n))
            trials.append(dict(lambda_=lam,high_size=len(U),low_size=len(L),
                high_energy=EU,discarded_energy=EL,discarded_fraction=EL/E,
                low_root_contrast=kappa,high_root_contrast=float(f[high]@wU),
                canonical_low_root_contrast=float(fL@canonical[~high]),
                low_preimage_norm_fraction=normlow,
                root_leverage=nu,root_leverage_ceiling=leverage_ceiling,
                low_response_D_energy=s,
                sharp_schur_bound=schur_bound,root_response_correlation=corr,
                primal_low_D_energy=ell,high_harmonic_D_energy=alpha,
                harmonic_mixed_pairing=mixed,harmonic_cosine=cosine,
                positive_primal_error=low_error,positive_primal_error_bound=triangle_error,
                root_abs_lower=lower,root_abs_upper=upper,
                cuts=cuts,square_profile=square_profile))
        error += solve_errors
        assert max(error)<2e-7,(q,side,max(error))
        yield dict(kind='actual_numerical',q=q,characteristic=p,side=side,r=r,
            energy=E,support_size=len(I),qp_residual=qp_residual,
            identity_error=max(error),trials=trials)


def certify_prime(p, side, lam_string):
    from flint import arb, arb_mat, ctx
    ctx.prec=192
    signs=list(map(int,previous.source.previous.paley_sign(p)))
    n=len(signs);r=arb(p)**(-arb(1)/3)
    eta,beta=r*r/(1-r*r),r/(1+r)
    xp,yp,_,_=previous.source.previous.solve(np.array(signs),p**(-1/3))
    approx=xp if side==1 else yp
    I=[i for i in range(1,n) if approx[i]>1e-8]
    rk=[sum(((2*arb.pi()*((i*j)%n)/n).cos()
             for j,s in enumerate(signs) if s==-side),arb(0))/n+beta/n
        for i in range(n)]
    T=arb_mat([[rk[(i-j)%n]+(eta if i==j else 0) for j in I] for i in I])
    bI=T.solve(arb_mat([[-rk[i]] for i in I]))
    assert all(bI[j,0]>0 for j in range(len(I)))
    b=[arb(0) for _ in range(n)];b[0]=arb(1)
    for j,i in enumerate(I):b[i]=bI[j,0]
    qb=[(sum((rk[(i-j)%n]*b[j] for j in range(n)),arb(0))+eta*b[i])*(1/r-r)
        for i in range(n)]
    inactive=[i for i in range(1,n) if i not in I]
    assert all(qb[i]>0 for i in inactive)
    assert all(abs(qb[i])<arb('1e-43') for i in I)
    a=1/qb[0].sqrt();x=[a*z for z in b]
    E=sum((x[i]**2 for i in I),arb(0));lam=arb(lam_string)
    assert all(abs(x[i]*arb(n).sqrt()-lam)>arb('1e-30') for i in I)
    U=[i for i in I if x[i]*arb(n).sqrt()>lam]
    L=[i for i in I if i not in U]
    EU=sum((x[i]**2 for i in U),arb(0));EL=E-EU
    ww=T.solve(arb_mat([[x[i]/EU if i in U else arb(0)] for i in I]))
    w={i:ww[j,0] for j,i in enumerate(I)}
    f={i:-a*rk[i] for i in I}
    low=sum((f[i]*w[i] for i in L),arb(0))
    high=sum((f[i]*w[i] for i in U),arb(0))
    assert abs(low+high-1)<arb('1e-42')
    D=arb_mat([[rk[(i-j)%n]+(eta if i==j else 0) for j in L] for i in L])
    z=D.solve(arb_mat([[f[i]] for i in L]));wL=arb_mat([[w[i]] for i in L])
    nu=sum((f[i]*z[j,0] for j,i in enumerate(L)),arb(0))
    Dw=D*wL;ss=sum((w[i]*Dw[j,0] for j,i in enumerate(L)),arb(0))
    assert nu*ss-low**2>=0 or abs(nu*ss-low**2)<arb('1e-40')
    if p==257:
        assert EL/E<arb('0.01') and low<arb('-0.26')
        assert low**2>EL/EU
    if p==29 and side==-1:
        assert low<arb('-1')
    print(json.dumps(dict(kind='strict_prime_certificate',p=p,side=side,
        lambda_=lam_string,precision_bits=ctx.prec,support=I,high_set=U,low_set=L,
        discarded_energy_fraction=str(EL/E),low_root_contrast=str(low),
        high_root_contrast=str(high),low_root_schur_bound=str((nu*ss).sqrt()),
        min_active_b=str(min(bI[j,0] for j in range(len(I)))),
        min_inactive_Qb=str(min(qb[i] for i in inactive)))))


def model_certificate():
    """Continuity no-screening example; r=1/10, n=6, sector ranks 3 and 2."""
    from flint import arb, arb_mat, ctx
    ctx.prec=192
    for estr in ('0','0.01','0.000001'):
        eps=arb(estr);n=6;r=arb(1)/10
        b=arb_mat([[1],[arb(1)/2],[arb(1)/4],[eps],[0],[0]])
        total=sum((b[i,0] for i in range(n)),arb(0));mass=total**2/n
        norm=sum((b[i,0]**2 for i in range(n)),arb(0))
        aa=arb(3)*r/2;bb=-(r*total+1+r*r)
        cc=r*(norm+total**2/2-2*mass)+(1+r*r)*mass
        discr=bb*bb-4*aa*cc
        assert discr>0
        z=2*cc/(-bb+discr.sqrt())
        qv=arb_mat([[z],[0],[0],[0],[(total-z)/2],[(total-z)/2]])
        assert z>0 and total-z>0 and z>(total-z)/2
        J=arb_mat([[arb(1)/n for _ in range(n)] for _ in range(n)])
        ident=arb_mat([[int(i==k) for k in range(n)] for i in range(n)])
        h=(qv-r*b-(1-r)*(J*b))*r/(1-r*r)
        hnorm=(h.transpose()*h)[0,0]
        avec=arb_mat([[0],[arb(1)/4-eps],[eps-arb(1)/2],[arb(1)/4],[0],[0]])
        tvec=arb_mat([[0],[0],[0],[0],[1],[-1]])
        N=((h*h.transpose())/hnorm
           +(avec*avec.transpose())/(avec.transpose()*avec)[0,0]
           +(tvec*tvec.transpose())/2)
        P=ident-J-N;Q=J+r*P+N/r
        def small(M):return all(abs(M[i,k])<arb('1e-42') for i in range(M.nrows()) for k in range(M.ncols()))
        assert small(N*N-N) and small(J*N) and small(Q*b-qv)
        x=b/z.sqrt();eta=r*r/(1-r*r);beta=r/(1+r);R=N+beta*J
        I=[1,2,3];U=[1,2]
        EU=sum((x[i,0]**2 for i in U),arb(0))
        T=arb_mat([[R[i,k]+(eta if i==k else 0) for k in I] for i in I])
        w=T.solve(arb_mat([[x[i,0]/EU if i in U else arb(0)] for i in I]))
        low=-x[0,0]*R[3,0]*w[2,0]
        E=EU+x[3,0]**2
        assert low<arb('-9.6') and low>arb('-10')
        if estr=='0':
            assert low<arb('-9.685') and low>arb('-9.686')
            assert abs(480*z*z-3792*z+2233)<arb('1e-42')
        if estr=='0.000001':
            assert x[3,0]**2/E<arb('3.2e-12') and low<arb('-9.68')
        # Fixed actual-level cut at tau=1/10 works for each positive epsilon here.
        assert x[1,0]>arb('0.1') and x[2,0]>arb('0.1') and x[3,0]<arb('0.1')
        print(json.dumps(dict(kind='two_sector_model_certificate',epsilon=estr,
            limiting_face=(estr=='0'),r='1/10',dimension=n,
            discriminant=str(discr),root_Qb=str(z),inactive_Qb=str((total-z)/2),
            rank_N=3,rank_P=2,both_marks_maximal=True,
            discarded_energy_fraction=str(x[3,0]**2/E),low_root_contrast=str(low),
            low_preimage=str(w[2,0]))))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--large',action='store_true')
    parser.add_argument('--certificate',action='store_true')
    args=parser.parse_args()
    if args.certificate:
        for p,side,lam in [(29,-1,'1'),(257,1,'0.5')]:
            certify_prime(p,side,lam)
        model_certificate();return
    cases=[(p,False) for p in (29,97,257,401,1009,4001)]
    cases += [(p,True) for p in (7,19,31,61)]
    if args.large:
        cases += [(p,False) for p in (9413,37253,153649)]
        cases += [(p,True) for p in (97,193,389)]
    for p,square in sorted(cases,key=lambda z:z[0]**(2 if z[1] else 1)):
        for row in actual_case(p,square):
            print(json.dumps(row),flush=True)


if __name__=='__main__':
    main()
