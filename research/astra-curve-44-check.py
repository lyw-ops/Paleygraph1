"""Arb certificates for real marked cubic contractions and relative analytic disks."""
from fractions import Fraction
import json
from pathlib import Path
import runpy

from flint import arb, arb_mat, arb_poly, ctx

base = runpy.run_path(str(Path(__file__).with_name("astra-cold-37.py")))
rat, col = base["rat"], base["column"]
ctx.prec = 224


def field(q, prime_square=None):
    sig = base["square_field_sign"](prime_square) if prime_square else base["paley_sign"](q)
    n = len(sig)
    offsets = [j for j in range(1,n//2+1) if sig[j] == 1]
    B = arb_mat([[(arb(2*i*j)/n).cos_pi() for j in offsets] for i in range(n//2+1)])
    return sig, base["even_kernel"](sig), B


def calc(data, floor, N=7):
    sig, K, B = data
    n, d = len(sig), K.nrows()
    x = rat(floor)
    w = [arb(1)]+[x/n]*(d-1)
    v = base["real_root"](K, sig, x, [4*wi for wi in w])
    s = [(vi*vi+4*wi).sqrt() for vi,wi in zip(v,w)]
    A = [(si+vi)/2 for si,vi in zip(s,v)]
    wt = [wi*(1 if i in (0,d-1) else 2) for i,wi in enumerate(w)]
    V = arb_mat([[B[i,j]/A[i] for j in range(B.ncols())] for i in range(d)])
    Vtw = arb_mat([[V[i,j]*wt[i] for i in range(d)] for j in range(B.ncols())])
    P = V*((Vtw*V).solve(Vtw))
    hs = [[arb(0)]*d]
    qs = [[arb(1)]*d]
    for j in range(1,N+1):
        source = [-sum((hs[k][i]*qs[j-k][i] for k in range(1,j)),arb(0)) for i in range(d)]
        g = source.copy()
        g[0] -= qs[j-1][0]
        hj = (P*col(g)).entries()
        hs.append(hj)
        qs.append([si-hi for si,hi in zip(source,hj)])
    c = [-hi for hi in hs[1]]
    c0 = c[0]
    M3 = sum(wi*y**3 for wi,y in zip(wt,c))
    M4 = sum(wi*y**4 for wi,y in zip(wt,c))
    second = sum(wi*y**2 for wi,y in zip(wt,hs[2]))
    b = [-c0,M3-3*c0**2/2,M4-4*c0**3/3-2*second]
    W = sum(wt)
    # m(Te^{-s}) at the chart center. z=1-exp(v).
    physical = [-b[0],-b[0]+2*b[1],-b[0]+6*b[1]-6*b[2]]
    # normalization log[(1+(exp(v)-1)/W)/exp(v)]/2
    a = 1/W
    physical[0] += (a-1)/2
    physical[1] += (a-a*a)/2
    physical[2] += (a-3*a*a+2*a**3)/2
    # Independent scalar Taylor recurrence in v, from s^2-(Ks)^2=4w.
    J = base["system"](K, [u/t for u,t in zip(v,s)], True)
    all_s, all_v = [s],[v]
    mark = [A[0]]
    for k,coef in enumerate([-1,arb(1)/2,-arb(1)/6],1):
        g = [arb(0)] + [4*wi*coef for wi in w[1:]]
        for i in range(d):
            g[i] += sum(all_v[j][i]*all_v[k-j][i]-all_s[j][i]*all_s[k-j][i] for j in range(1,k))
        sk = J.solve(col([gi/(2*si) for gi,si in zip(g,s)])).entries()
        vk = (K*col(sk)).entries()
        all_s.append(sk)
        all_v.append(vk)
        mark.append((sk[0]+vk[0])/2)
    h1,h2,h3 = [mi/mark[0] for mi in mark[1:]]
    direct = [h1,2*h2-h1**2,6*h3-6*h1*h2+2*h1**3]
    assert all(l.overlaps(r) and l.rad()<arb(2)**-60 and r.rad()<arb(2)**-60 for l,r in zip(physical,direct))
    def disk(rat_R):
        R = rat(rat_R)
        norm_h = [sum(abs(hs[k][i])*R**k for k in range(1,N+1)) for i in range(d)]
        sup_h = max(y.upper() for y in norm_h)
        # Weighted radius b gives an entrywise allowance delta.
        delta = arb(1)/64
        bound = sup_h+delta
        if not bound < 1:
            return None
        lip = (1-bound)**-2-1+R/(1-bound)**2
        if not lip < arb(9)/10:
            return None
        residual = []
        for i in range(d):
            tail = sum(abs(sum(hs[k][i]*qs[j-k][i] for k in range(j-N,N+1)))*R**j
                       for j in range(N+1,2*N+1))
            residual.append((1+(R if i==0 else 0))*tail/(1-norm_h[i]))
        err = sum(wi*ri*ri for wi,ri in zip(wt,residual)).sqrt()+R**(N+1)*abs(qs[N][0])
        radius = min(arb(1),x/n).sqrt()*delta
        if err < (1-lip)*radius:
            return lip, err/((1-lip)*radius), err/((1-lip)*(1-bound))
        return None
    # Combine the two signed contributions before real interval evaluation.
    # Polynomial arithmetic avoids cancellation loss throughout the covered path.
    F = arb_poly([arb(1)]+[hs[j][0] for j in range(1,N+1)])
    E = arb_poly([1,-1])
    norm_den = arb_poly([arb(1),-1/W])
    F1 = -E*F.derivative()
    F2 = -E*F1.derivative()
    F3 = -E*F2.derivative()
    log_num = F3*F**2-3*F1*F2*F+2*F1**3
    norm_num = E*(W-1)*(W-1-E)*(1/(2*W**3))
    num = log_num*norm_den**3 + norm_num*F**3
    den = (norm_den*F)**3
    def cubic(v):
        z = 1-v.exp()
        return num(z)/den(z)
    cp2 = (P*col([ci**2 for ci in c])).entries()
    twice_p = 2*sum(wi*y**2 for wi,y in zip(wt,cp2))
    reflection = M4-twice_p
    assert (reflection+4*c0*M3-arb(10)*c0**3/3).overlaps(b[2])
    return disk, cubic, dict(cubic_derivative=physical[2], fourth_moment=M4,
                twice_projection_of_square=twice_p, signed_reflection=reflection,
                twice_second_jet_energy=2*second, marked_cubic_coefficient=b[2])


def show(t):
    return t.str(11)


def main():
    for q,b in [(173,None),(121,11)]:
        data = field(q,b)
        for x in [Fraction(1,20),Fraction(1,4),Fraction(1),Fraction(4)]:
            disk, _, vals = calc(data,x)
            print(json.dumps(dict(kind="fixed_floor",order=q,floor=str(x),**{k:show(v) for k,v in vals.items()}),sort_keys=True), flush=True)
        # A geometric mesh in log floor. A uniform disk is certified at each point.
        R = Fraction(1,10) if q == 173 else Fraction(1,7)
        U = Fraction(9,8)
        centers = [Fraction(1,32)]
        while centers[-1] < 2048:
            centers.append(min(Fraction(2048),centers[-1]*U))
        bounds = []
        lo, hi, sup_lo, sup_hi = arb(0), arb(0), arb(0), arb(0)
        for j,x in enumerate(centers):
            disk,cubic,_ = calc(data,x,N=12)
            result = disk(R)
            if result is None:
                raise ValueError(q, float(x), str(R))
            bounds.append(result)
            left = -(rat(centers[j+1]/x)).log()/2 if j+1<len(centers) else arb(0)
            right = rat(x/centers[j-1]).log()/2 if j else arb(0)
            cauchy = (1+rat(R)).log() - max(abs(left).upper(),abs(right).upper())
            assert cauchy > 0
            error = 6*result[2]/cauchy**3
            step = (right-left)/32
            for k in range(32):
                point = left+(k+arb(1)/2)*step
                enclosure = cubic(point+arb(0,step.upper()/2))+arb(0,error.upper())
                absolute = abs(enclosure)
                lo += step*max(arb(0),absolute.lower())
                hi += step*absolute.upper()
                sup_hi = max(sup_hi,absolute.upper())
                center_abs = abs(cubic(point)+arb(0,error.upper()))
                sup_lo = max(sup_lo,center_abs.lower())
        if q == 173:
            assert lo > rat('0.06082') and hi < rat('0.06189')
            assert sup_lo > rat('0.01973') and sup_hi < rat('0.01993')
        else:
            assert lo > rat('0.18795') and hi < rat('0.19173')
            assert sup_lo > rat('0.10297') and sup_hi < rat('0.10404')
        theta = rat(Fraction(77,1000) if q == 173 else Fraction(1,8))
        ratio_root = rat(U).sqrt()
        assert (ratio_root-1)**2+ratio_root*theta**2 < rat(R)**2
        print(json.dumps(dict(log_strip_half_angle=show(theta),kind="relative_disk_chain",order=q,center_count=len(centers),first=str(centers[0]),
              last=str(centers[-1]),mesh_ratio=str(U),z_disk_radius=str(R),
              contraction_upper=show(max(t[0].upper() for t in bounds)),
              residual_fraction_upper=show(max(t[1].upper() for t in bounds)),
              integrated_abs_cubic_lower=show(lo.lower()), integrated_abs_cubic_upper=show(hi.upper()),
              sup_abs_cubic_lower=show(sup_lo.lower()),sup_abs_cubic_upper=show(sup_hi.upper())),sort_keys=True),flush=True)


if __name__ == "__main__":
    main()
