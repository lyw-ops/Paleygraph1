"""Interval replay of complementary mixed Jacobi transport at actual optimal pairs."""
import json
from pathlib import Path
import runpy

from flint import acb, arb, ctx

prior = runpy.run_path(str(Path(__file__).with_name("endpoint-direction-45-check.py")))
ctx.prec = 384


def dot(x, y):
    return sum((a*b for a, b in zip(x, y)), arb(0))


def units(x):
    x = 10**9*x
    return [int(x.lower().floor().unique_fmpz()), int(x.upper().ceil().unique_fmpz())]


def slide(row, h):
    return row[h:] + row[:h]


def terminal_deficit(signs, side, time):
    n = len(signs)
    root = arb(n).sqrt()
    apply = prior["apply_multiplier"]
    state = [arb(0)]*n
    raw = [arb(0)]*n
    for t in range(time+1):
        phi = [(4+state[0]**2).sqrt()] + list(map(abs, state[1:]))
        if t:
            weight = arb(1 if t == time else 2)/(2*time-1)
            raw = [old+weight*root*(g-side*y)/2 for old, g, y in zip(raw, phi, state)]
        if t < time:
            state = apply(phi, signs)
    projection = [int(x == -side) for x in signs]
    column = [z.real for z in acb.dft(projection, inverse=True)]
    projected = apply(raw, [int(x in (0, -side)) for x in signs])
    pin = (projected[0]/root-sum(raw)/n).max(0)
    return [arb(0)]+[(-v-pin*(1-c/column[0])).max(0) for v,c in zip(projected[1:],column[1:])]


def audit(p, time):
    signs = prior["paley_sign"](p)
    pair, error = prior["solve_prime_pair"](signs)
    assert error is None
    n = len(signs)
    side = 1 if pair[1][0] > pair[-1][0] else -1
    assert pair[side][0] > pair[-side][0]
    signs = list(map(int, signs))
    root, root_p = arb(n).sqrt(), arb(p).sqrt()
    q, r = ([v/root for v in pair[t]] for t in (side,-side))
    assert all((q[i]*r[i]).is_zero() for i in range(1,n))
    assert (n*q[0]*r[0]-1).contains(0)
    W, V = ([(n*v-1)/root_p for v in row] for row in (q,r))
    kernel = [z.real*n/root_p for z in acb.dft(signs,inverse=True)]
    apply = prior["apply_multiplier"]
    for row,w,s in ((q,W,side),(r,V,-side)):
        assert all((s*n*a/root_p-b).contains(0) for a,b in zip(apply(row, signs),w))
    x = [(a-side*q[0]*k)/(1-q[0]) for a,k in zip(W,kernel)]
    y = [(a+side*r[0]*k)/(1-r[0]) for a,k in zip(V,kernel)]
    assert (p*dot(x,y)/n-1).contains(0)

    S = [2*root*k*root_p/n for k in kernel]
    L = apply([s*s/2 for s in S],signs)
    f = [v*v for v in L]
    mean = sum(f)/n
    kernel_sq = [k*k for k in kernel]
    delta_q = dot(q,kernel_sq)-sum(kernel_sq)/n
    delta_r = dot(r,kernel_sq)-sum(kernel_sq)/n
    gamma = root*q[0]
    assert (sum(kernel_sq)/n-arb(n-1)/p).contains(0)
    assert (side*dot(q,L)-2*arb(p)*delta_q/n).contains(0)
    assert side*dot(q,L) > 2*(gamma**2-1-2*q[0]+arb(2)/n)
    product = [a*b for a,b in zip(W,V)]
    marked_kernel = p*dot(kernel,product)/n
    assert (-side*marked_kernel-root/root_p*(gamma-1/gamma)-side/root_p).contains(0)
    # Sum the distinct-center cubic by first fixing its counting coordinate.
    exterior = []
    for z in range(n):
        qa = sum(q[i]*kernel[(z-i)%n] for i in range(1,n))
        rb = sum(r[j]*kernel[(z-j)%n] for j in range(1,n))
        exterior.append(kernel[z]*qa*rb)
    distinct = p*sum(exterior)/n
    axes = side*root_p*(q[0]*delta_r-r[0]*delta_q)
    triple_root = p*q[0]*r[0]*sum(k**3 for k in kernel)/n
    assert (marked_kernel+distinct-axes-triple_root).contains(0)
    # Test the displacement conditional law before imposing alignment.
    for a in range(n):
        ra,va = slide(r,a),slide(V,a)
        mu = [n*u*v for u,v in zip(q,ra)]
        assert (sum(mu)-1).contains(0)
        exterior_mass = sum(mu[i] for i in range(1,n) if (i+a)%n)/n
        assert (exterior_mass-arb(1)/n+q[0]*r[a]+r[0]*q[-a]-int(a==0)*q[0]*r[0]).contains(0)
        lhs = p*dot([b*c for b,c in zip(W,va)],f)/n
        assert (lhs-dot(mu,f)+dot(q,f)+dot(ra,f)-mean).contains(0)
    errors, scaled, trimmed_errors = [],[],[]
    kernel_errors = []
    exterior_product = [a*b for a,b in zip(x,y)]
    mass = (1-q[0])*(1-r[0])
    for c in range(n):
        shifted = slide(f,c)
        coefficient = p*dot(shifted,product)/n
        correction = f[c]-mean-coefficient
        assert (correction-dot(q,shifted)-dot(r,shifted)+2*mean).contains(0)
        trimmed = p*dot(shifted,exterior_product)/n
        trimmed_errors.append(mass*(trimmed-mean)-(f[c]-mean))
        errors.append(correction)
        scaled.append(coefficient)
        kernel_error = p*dot(slide(kernel,c),product)/n-kernel[c]
        assert (kernel_error+side*n*(q[-c]-r[-c])/root_p).contains(0)
        kernel_errors.append(abs(kernel_error))
    assert sum(trimmed_errors).contains(0)
    assert (sum(kernel_errors)/n-2*(1-r[0])/root_p).contains(0)
    variance = sum((v-mean)**2 for v in f)/n
    rms_error = (dot(errors,errors)/n).sqrt()
    rms_scaled = (dot(scaled,scaled)/n).sqrt()
    fhat = acb.dft(f)
    qhat = acb.dft(q)
    rhat = acb.dft(r)
    spectral = sum(abs(fhat[i])**2*(abs(qhat[i])**2+abs(rhat[i])**2)
                   for i in range(1,n))/n**2
    assert (rms_error**2-spectral).contains(0)
    max_coeff = max(abs(val) for val in fhat[1:])/n
    bound = max_coeff*(n*(dot(q,q)+dot(r,r))-2).sqrt()
    assert rms_error < bound and variance > 0

    deficit = terminal_deficit(signs,side,time)
    proj = [int(x == side) for x in signs]
    col = [z.real for z in acb.dft(proj,inverse=True)]
    part = apply(deficit,proj)
    price = dot(q,deficit)
    coef = part[0]/col[0]
    h = [v-coef*b for v,b in zip(part,col)]
    pinned_price = (q[0]-arb(1)/n)*coef
    mixed = p*dot(h,product)/n
    assert h[0].contains(0) and sum(h).contains(0) and dot(h,r).contains(0)
    assert (price-sum(deficit)/n-pinned_price+mixed).contains(0)
    return dict(prime=p,time=time,side=side,bits=ctx.prec,units="1e-9",
                displacements_checked=n,common_translations_checked=n,
                first_square_rms_centered=units(variance.sqrt()),first_square_scaled_mixed_rms=units(rms_scaled),
                explicit_stalk_residual_rms=units(rms_error),
                root_trimmed_stalk_residual_rms=units((dot(trimmed_errors, trimmed_errors)/n).sqrt()),spectral_upper_rms=units(bound),
                first_square_max_flatness_scaled=units(root_p*max_coeff),
                fixed_mark_square_residual=units(errors[0]),terminal_deficit_price=units(price),
                terminal_counting_mean=units(sum(deficit)/n),terminal_pin_price=units(pinned_price),
                scaled_marked_kernel=units(marked_kernel),scaled_distinct_center_cubic=units(distinct),
                signed_two_axis_price=units(axes),triple_root_price=units(triple_root),
                primary_jacobi_square_bias=units(delta_q),opposite_jacobi_square_bias=units(delta_r),
                terminal_scaled_root_neutral_mixed=units(mixed))


if __name__ == "__main__":
    for p,b in ((101,4),(257,5),(409,6),(769,7)):
        print(json.dumps(audit(p,b),sort_keys=True),flush=True)
