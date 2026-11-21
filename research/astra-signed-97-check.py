"""Outward first-floor erasure prices and a full-site physical Schur replay."""
import json
from pathlib import Path
import runpy

from flint import acb, arb, arb_mat, ctx

r96 = runpy.run_path(str(Path(__file__).with_name("astra-count-96-check.py")))
base = r96["base"]
ctx.prec = 256


def emit(**fields):
    print(json.dumps(fields, sort_keys=True))


def constants():
    T = arb(2031) / 128 - arb(2)**-17
    gap = arb("1e-4")
    d = arb("0.514")
    m = (1-d*d).sqrt()
    size = 500
    kernel = 178
    b = arb("89.158") * arb("8e-12").exp() * arb(3).sqrt() * arb(2)**-17 / (2*T**arb("1.5"))
    q = kernel * (1+d) / size
    hit = gap - b/(1-q)
    pivot = (1-q)*gap-b
    # Every entry of the inverse row minus the corresponding identity row.
    row_constant = kernel*(1+d)/(1-q)/arb(size).sqrt()
    # Sufficiently large n, including n >= 10^30.
    row_norm = 1 + row_constant / arb(10)**arb("7.5")
    trimmed = m*hit/row_norm
    half_log = (2*((1+(trimmed/gap)**2).sqrt()-1)).sqrt()
    growing = (m*hit-arb("5e-5"))/row_constant
    support = (1-b/gap)/(kernel*(1+d))
    assert q < arb("0.539") and b < arb("9.321e-6")
    assert hit > arb("7.978e-5") and trimmed > arb("6.843e-5")
    assert half_log > arb("0.650") and growing > arb("7.05e-7")
    assert m*pivot > arb("3.155e-5") and pivot/kernel > arb("2.066e-7")
    assert support > arb("0.003364") and row_constant < arb("26.143")
    bare = arb("1.415")*arb("9e-12").exp()*arb(3).sqrt()*arb(2)**-17/(2*T**arb("1.5"))
    bare_pivot = (1-arb("1.415")/2)*gap-bare
    bare_support = (1-bare/gap)/arb("1.415")
    assert bare_pivot > arb("2.910e-5") and bare_support > arb("0.7056")
    bare_cut = bare_pivot/gap
    shifted_cut = (1-b/gap)/(1+d)-arb(kernel)/size
    assert bare_cut > arb("0.2910") and shifted_cut > arb("0.2429")
    emit(kind="eventual_first_floor_arbitrary_erasure_bound",max_bulk_cardinality="sqrt(n)/500",
         bare_trimmed_signed_cut_discrepancy=bare_cut.str(15), shifted_trimmed_signed_cut_discrepancy=shifted_cut.str(15),
         bare_peak_signed_exterior_lower=bare_pivot.str(15), bare_paying_sign_support_over_sqrt_n=bare_support.str(15),
         marked_source_bound=b.str(17), internal_rate=q.str(12), inverse_row_l2_error_times_n_to_one_quarter=row_constant.str(15),
         signed_schur_hit_lower=hit.str(16), original_peak_signed_exterior_lower=(m*pivot).str(16),
         paying_sign_support_over_sqrt_n=support.str(15), trimmed_source_second_norm_lower=trimmed.str(15),
         trimmed_source_first_norm_over_sqrt_n=(pivot/kernel).str(15), trimmed_half_log_second_norm_lower=half_log.str(15),
         true_hit_alternative_source_second_norm_over_n_to_one_quarter=growing.str(15))


def physical():
    n, T, y, sign = (base[k] for k in ("n", "x", "y", "sign"))
    s = n/acb(T, y)
    U, total = base["positive_sheet"]([s]+[acb(1)]*(n//2), arb("1e-53"))
    A = [(z+u)/2 for z,u in zip(total,U)]
    B = [(z-u)/2 for z,u in zip(total,U)]
    full = lambda row: [row[min(i,n-i)] for i in range(n)]
    gamma = full([(v.real/w.real).log()/2 for v,w in zip(A,B)])
    w = full([v.real*z.real for v,z in zip(A,B)])
    kernel = acb.dft([int(k) for k in sign], inverse=True)
    K = arb_mat([[kernel[(i-j)%n].real for j in range(n)] for i in range(n)])
    response = r96["reflection"](K,gamma)
    root = abs(s.imag)*arb(3).sqrt()/(2*w[0].sqrt())
    X = [root*response[j,0] for j in range(n)]
    V = [g.cosh()*z for g,z in zip(gamma,X)]
    for j in range(1,n):
        assert (w[j]-1+X[j]**2/3).contains(0)
        assert (V[j]+arb(3).sqrt()*full(U)[j].imag/2).contains(0)
    bare_mark = root*(gamma[0].cosh()+gamma[0].sinh()*response[0,0])
    for j in range(1,n):
        paid = sum((K[j,k]*gamma[k].tanh()*V[k] for k in range(1,n)),arb(0))
        assert (V[j]-bare_mark*K[j,0]-paid).contains(0)
    # A different physical reference exposes the compensated-row correction at small p.
    g = [(arb(n).sqrt()*K[i,0]/(arb(n) if i==0 else T).sqrt()).asinh() for i in range(n)]
    d = [u.tanh() for u in g]
    Z = base["base"]["system"](K,d,False).solve(K)
    E = [u.tanh()-v for u,v in zip(gamma,d)]
    lag0 = gamma[0]-g[0]
    beta = lag0.cosh()+lag0.sinh()*response[0,0]
    b = [root*beta*Z[j,0]/g[0].cosh() for j in range(n)]
    for j in range(1,n):
        defect = V[j]-b[j]-sum((Z[j,k]*E[k]*V[k] for k in range(1,n)),arb(0))
        assert defect.contains(0) and abs(defect).upper() < arb("1e-48")
    def orbit_max(v):
        sites = [i for i in range(1,n//2+1) if all(abs(v[i])>abs(v[k])
                 for k in range(1,n//2+1) if k!=i)]
        assert len(sites)==1
        return sites[0]
    i, peak = orbit_max(X), orbit_max(V)
    # Exact finite layer integration, pooling the two individual inverse partners.
    sites = range(1,n//2+1)
    sign_v = 1 if V[peak] > 0 else -1
    assert sign_v*V[peak]>0
    levels = [abs(u.tanh()) for u in gamma]
    amplitudes = [abs(u)/abs(V[peak]) for u in V]
    def strips(values):
        ordered = sorted(sites,key=lambda j:float(values[j]))
        cuts = [arb(0),*[values[j] for j in ordered]]
        assert all(q>p for p,q in zip(cuts,cuts[1:]))
        return [(cuts[l+1]-cuts[l],set(ordered[l:])) for l in range(len(ordered))]
    signed_coefficients = {}
    for j in sites:
        orient = sign_v*gamma[j]*X[j]
        assert abs(orient)>0
        r = sum((K[peak,k] for k in {j,n-j}),arb(0))
        signed_coefficients[j] = r if orient>0 else -r
    plane = arb(0)
    max_cut = arb(0)
    strips_v = strips(amplitudes)
    for du,J in strips(levels):
        for dv,L_cut in strips_v:
            cut = sum((signed_coefficients[j] for j in sorted(J & L_cut)),arb(0))
            plane += du*dv*cut
            if cut.lower()>max_cut.upper():
                max_cut=cut
    bare_value = sign_v*(V[peak]-bare_mark*K[peak,0])/abs(V[peak])
    assert (plane-bare_value).contains(0) and abs(plane-bare_value).upper()<arb("1e-45")
    assert max_cut>plane
    # Choose six large sources and their partners; enforce exact selection in Arb.
    ranked = sorted(range(1,n//2+1),key=lambda k:float(abs(E[k]*V[k])),reverse=True)
    kept = ranked[:6]
    assert all(abs(E[k]*V[k])>abs(E[j]*V[j]) for k in kept for j in ranked[6:])
    S = sorted({z for k in [i,peak,*kept] for z in (k,n-k)})
    outside = [k for k in range(1,n) if k not in S]
    Ablock = arb_mat([[int(k==j)-Z[k,j]*E[j] for j in S] for k in S])
    unit = arb_mat([[int(j==i)] for j in S])
    f = Ablock.transpose().solve(unit).entries()
    L = [sum((Z[j,k]*E[k]*V[k] for k in outside),arb(0)) for j in S]
    marked = sum((a*b[j] for a,j in zip(f,S)),arb(0))
    signed = sum((a*z for a,z in zip(f,L)),arb(0))
    defect = V[i]-marked-signed
    assert defect.contains(0) and abs(defect).upper()<arb("1e-48")
    correction = signed-L[S.index(i)]
    assert abs(correction).lower()>arb("1e-13")
    emit(kind="true_unit_bulk_physical_erasure_identity",p=173,real="2031/128",imag="1/131072",
         reference="bare_Jacobi",bulk_cutoff_squared=(X[i]**2).str(17),hit_orbit=i,
         physical_imaginary_peak_orbit=peak,erased_individual_sites=S,
         bare_cut_layer_integral=plane.str(17), largest_sampled_bare_signed_cut=max_cut.str(17),
         imaginary_response_at_hit=V[i].str(17),compensated_mark=marked.str(17),
         uncompensated_exterior_in_Z_units=L[S.index(i)].str(17),compensated_exterior_in_Z_units=signed.str(17),
         nonzero_feedback_correction=correction.str(17))


if __name__=="__main__":
    constants()
    physical()
