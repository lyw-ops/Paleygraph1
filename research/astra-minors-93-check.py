"""Arb replay for the two-site exterior Gram and an actual mark-preserving perturbation."""
import json
from pathlib import Path
import runpy

from flint import arb, arb_mat, ctx

previous = runpy.run_path(str(Path(__file__).with_name("astra-velocity-92-check.py")))
ctx.prec = 256
K = previous["K"]
n, size = previous["n"], previous["size"]
mult = previous["mult"]
scales = [arb(m).sqrt() for m in mult]
h = size - 1
native = arb_mat([[scales[i] * K[i, j] / scales[j] for j in range(size)]
                  for i in range(size)])
col = previous["base"]["column"]
eps = arb(10)**-8
T = arb(2031) / 128
w = [n/T] + [1 - eps/2] * h
v, total = previous["positive_sheet"](w, arb("1e-42"), real=True)
A = [(x+y)/2 for x, y in zip(total, v)]
B = [(x-y)/2 for x, y in zip(total, v)]

F = [n*K[i, 0]*K[i, h] + 1/arb(n) for i in range(size)]
KF = (K*col(F)).entries()
assert sum(m*f for m, f in zip(mult, F)).contains(0)
dirs = []
for s in (1, -1):
    k = [((i == 0)-1/arb(n)+s*K[i, 0])/(1-1/arb(n)+s*K[0, 0])
         for i in range(size)]
    u = [s*f+g for f, g in zip(F, KF)]
    d = [y-u[0]*z for y, z in zip(u, k)]
    assert d[0].contains(0) and sum(m*y for m, y in zip(mult, d)).contains(0)
    assert all(z.contains(0) for z in (K*col(d)-s*col(d)).entries())
    dirs.append(d)

bases = []
for s in (1, -1):
    labels = [j for j in range(1, size) if previous["sign"][j] == s]
    basis = arb_mat([[scales[i] * (arb(mult[j])/n).sqrt()
                      * (2*arb.pi()*i*j/n).cos() for j in labels] for i in range(size)])
    assert all(x.contains(0) for x in (native*basis - s*basis).entries())
    bases.append(basis)

def proj(basis, row_scales, exterior=False):
    mat = arb_mat([[scale*basis[i, j] for j in range(basis.ncols())]
                   for i, scale in enumerate(row_scales)])
    gram = mat.transpose()*mat
    P = mat*gram.solve(mat.transpose())
    if exterior:
        rows = arb_mat([[mat[i, j] for j in range(mat.ncols())] for i in range(1, h)])
        S = arb_mat([[basis[i, j] for j in range(mat.ncols())] for i in (0, h)])
        gram_out = rows.transpose()*rows
        L = S*gram_out.solve(S.transpose())
        rho2 = L[0,1]**2/(L[0,0]*L[1,1])
        resid = (1-rho2).sqrt()
        sharp = rho2.sqrt()/(2*(1+resid))
        assert abs(P[h,0]) < sharp
        x = 1/(L[0,0]*resid)
        y = 1/(L[1,1]*resid)
        optimized = row_scales.copy()
        optimized[0], optimized[h] = x.sqrt(), y.sqrt()
        Popt = proj(basis, optimized)
        assert (abs(Popt[h,0])-sharp).contains(0)
        ratio = (1-rho2)
        assert arb(0)<ratio and ratio<1
        return P, ratio, sharp
    return P

def at(u, exterior=False):
    aa = [x+u*y for x, y in zip(A, dirs[0])]
    bb = [x+u*y for x, y in zip(B, dirs[1])]
    assert all(x>0 for x in aa+bb) and (aa[0]*bb[0]-w[0]).contains(0)
    assert all(1-eps < x*y and x*y<1 for x, y in zip(aa[1:], bb[1:]))
    weights = [(y/x).sqrt() for x, y in zip(aa, bb)]
    outs = [proj(bases[0], weights, exterior),
            proj(bases[1], [1/z for z in weights], exterior)]
    if exterior:
        kernels = [z[0] for z in outs]
        for side, (P, ratio, sharp) in zip((1,-1), outs):
            print(json.dumps(dict(kind="two_site_exterior_paley_gram", prime=173,
                precision=ctx.prec, floor="2031/128", sign=side, bulk_index=h,
                determinant_cross_ratio=ratio.str(12), physical_entry=P[h,0].str(12),
                sharp_row_scaling_cap=sharp.str(12), cap_attained_by_rescaling=True),
                sort_keys=True))
    else:
        kernels = outs
    return kernels[0]-kernels[1]

J = at(arb(0), exterior=True)
base_hit = (native*arb_mat([[F[i] if i == j else 0 for j in range(size)]
                           for i in range(size)])*native)[h, 0]
u = eps/64
Jp, Jm = at(u), at(-u)
sec = (Jp[h,0]-Jm[h,0])/(2*u)
dg = [(l/x-r/y)/2 for x,y,l,r in zip(A,B,*dirs)]
vel = sum(J[h,j]*dg[j]*J[j,0] for j in range(size))
assert sec > arb("0.1") and abs(sec-vel)<arb("1e-13")
dir_norm = max(abs(z).upper() for d in dirs for z in d)
dual_test = vel/dir_norm
assert dual_test > arb("0.1")
print(json.dumps(dict(kind="nominated_real_mark_preserving_two_center_perturbation",
    prime=173, precision=ctx.prec, floor="2031/128", baseline_bulk="1-5e-9",
    endpoint_step="1e-8/64", actual_marked_column_secant=sec.str(13),
    exact_derivative=vel.str(13), native_two_center_coefficient=base_hit.str(13),
    lower_test_for_full_derivative_norm=dual_test.str(13),
    endpoints_inside_box=True, mark_and_both_sector_means_preserved=True),sort_keys=True))

residual = 4*(arb(428236)/10**6)**600
M = arb(10)**211
limsup_product_debit = 8*M*residual
assert 4 > 2+arb("4.768")/T.sqrt() and 31/T.sqrt() < 8
assert T*eps/2 < arb(2)**-17 and limsup_product_debit < eps/2
assert 2000 > 2*956
print(json.dumps(dict(kind="nominated_all_direction_perturbation_constants",
    precision=ctx.prec, floor="2031/128", epsilon="1e-8",
    sqrt_n_times_radius="1e211", real_residual_limsup_upper=residual.str(12),
    bulk_product_deviation_limsup_upper=limsup_product_debit.str(12),
    available_strict_slack="5e-9", dual_distance_sum_upper="4e-208"),
    sort_keys=True))
