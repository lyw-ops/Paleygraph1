"""Certify truncated layer constants and signed Jacobi cuts on actual cold rows."""
import json
from math import isqrt
from pathlib import Path
import runpy

from flint import acb, arb, ctx

base = runpy.run_path(str(Path(__file__).with_name("astra-cold-37.py")))
ctx.prec = 256


def emit(**row):
    print(json.dumps(row, sort_keys=True))


def layer_bounds():
    h = arb(2)**-17
    lower = arb(2031)/128-h
    pred = arb(3).sqrt()*h*(21/lower.sqrt()+arb("4.768")/(2*lower**arb("1.5")))/2
    phase = arb("1e-4")
    a, b = arb("0.52"), arb("0.4")
    scale = arb(3).sqrt()/(2*lower.sqrt()*phase)
    margin = b-pred/phase
    coeff = 1/(a-arb("0.514"))+a*462*scale**2/(4*margin)
    area = a*b
    mu = arb("1.415")
    paid = 1-arb("1.480e-7")/phase
    clipped = paid-mu*coeff*arb("1e-6")**2
    tested = clipped/area-mu/2
    tail = paid-area*(1+mu/2)
    remaining = tail-(1-area)*mu/2
    payers = tail/((1-area)*mu)
    resist = (tail/(mu*coeff)).sqrt()
    assert pred < arb("3.52e-5") and scale**2/(4*margin)>1
    assert tested > arb("4.0538") and remaining > arb("0.0830")
    assert payers > arb("0.5740") and resist > arb("8.874e-6")
    emit(kind="first_floor_paired_cut_rectangle_or_signed_excess", real_amplitude_cut_cap="0.52",
         imaginary_row_fraction_cap="0.4", predictor_imaginary_absolute=pred.str(15),
         excess_weight_counting_l1_over_n_r_squared=coeff.str(16),
         max_trimmed_signed_discrepancy_lower=tested.str(15),
         residual_condition="n^(1/4) * normalized_complex_residual <= 1e-6",
         if_every_low_cut_minimum_at_most_one_signed_excess=tail.str(15),
         surviving_signed_excess_after_erasures=remaining.str(15),
         aligned_outliers_over_sqrt_n=payers.str(15),
         necessary_scaled_residual_if_low_cut_bound_one=resist.str(15))


def physical_tube(prime):
    sign = base["paley_sign"](prime)
    n = len(sign)
    kernel = acb.dft([int(z) for z in sign], inverse=True)
    assert all(z.imag.contains(0) for z in kernel)
    K = base["even_kernel"](sign)
    N = K.nrows()
    column = base["column"]
    center_t = arb(2031)/128
    h = arb(2)**-17
    weights = [n/center_t]+[arb(1)]*(N-1)
    mult = [1]+[2]*(N-2)+[1]
    norm = lambda z: sum((m*abs(v).upper()**2 for m,v in zip(mult,z)),arb(0)).sqrt()
    u = column([arb(0)]*N)
    for _ in range(100):
        total = [(x*x+4*w).sqrt() for x,w in zip(u.entries(),weights)]
        u = column([v.mid() for v in (K*column(total)).entries()])
    uc = u.entries()
    total = [(x*x+4*w).sqrt() for x,w in zip(uc,weights)]
    base_error = norm((K*column(total)-u).entries())
    assert base_error < arb("1e-60")
    # Enclose the analytic real-start solution on the entire nominated square
    # in a fixed full-counting second-norm ball centered on this real vector.
    t = acb(center_t+arb(0,h),arb(0,h))
    ws = [n/t]+[acb(1)]*(N-1)
    radius = arb("1e-5")
    box = acb(arb(0,radius),arb(0,radius))
    orbit = [v+box for v in uc]
    phi = [(v*v+4*w).sqrt() for v,w in zip(orbit,ws)]
    assert all(z.real > 0 for z in phi)
    d = [v/z for v,z in zip(orbit,phi)]
    q = max(abs(v).upper() for v in d)
    residual = base_error+abs((uc[0]**2+4*ws[0]).sqrt()-total[0]).upper()
    assert residual < (1-q)*radius
    # Differentiate the normalized equation, reusing the real center's
    # derivative as a test vector for the complex inhomogeneous linear system.
    dc = [v/z for v,z in zip(uc,total)]
    src = [-2*n/(center_t**2*total[0])]+[arb(0)]*(N-1)
    deriv = base["system"](K,dc,False).solve(K*column(src)).entries()
    deriv_resid = norm((column(deriv)-K*column([v*z+w for v,z,w in zip(dc,deriv,src)])).entries())
    terms = [(a-b)*v for a,b,v in zip(d,dc,deriv)]
    terms[0] += -2*n/(t**2*phi[0])-src[0]
    deriv_radius = (deriv_resid+norm(terms))/(1-q)
    assert deriv_radius < arb("1e-4")
    # For y != 0 the row here is Im U/y, by integration on the vertical line.
    imag = [v+arb(0,deriv_radius.upper()) for v in deriv]
    # tanh(gamma)=(Re A-Re B)/(Re A+Re B).
    amplitude = [v.real/z.real for v,z in zip(orbit,phi)]
    assert all((z+v).real>0 and (z-v).real>0 for z,v in zip(phi,orbit))
    return n, N, kernel, h, imag, amplitude, deriv_radius, q


def optimal_debit(prices, budget):
    positive = [v for v in prices if v>0]
    assert all(v>0 or v<0 for v in prices)
    # Directed endpoints allow equal Jacobi prices at the erasure boundary.
    lo = sum(sorted((v.lower() for v in positive),reverse=True)[:budget],arb(0))
    hi = sum(sorted((v.upper() for v in positive),reverse=True)[:budget],arb(0))
    return lo.union(hi)


def all_cuts():
    prime = 173
    n,N,kernel,h,imag,amplitude,deriv_radius,q = physical_tube(prime)
    def ranked(values):
        ranks = sorted(range(1,N),key=lambda i:float(abs(values[i])),reverse=True)
        assert all(abs(values[i])>abs(values[j]) for i,j in zip(ranks,ranks[1:]))
        assert abs(values[ranks[-1]])>0
        return ranks
    amp_rank,imag_rank = ranked(amplitude), ranked(imag)
    k = imag_rank[0]
    assert k==16
    def cuts(order):
        result = [set()]
        for i in order:
            result.append(result[-1] | {i,n-i})
        return result
    prices = {}
    for j in range(1,n):
        i = min(j,n-j)
        direction = imag[k]*imag[i]*amplitude[i]
        assert direction>0 or direction<0
        prices[j] = kernel[(k-j)%n].real*(1 if direction>0 else -1)
    m = isqrt(n)//2
    rectangles = [(a,b) for a in cuts(amp_rank) for b in cuts(imag_rank)]
    maxima = []
    rawmax = []
    for a,b in rectangles:
        terms = [prices[i] for i in sorted(a&b)]
        total = sum(terms,arb(0))
        rawmax.append(total)
        maxima.append(total-optimal_debit(terms,m))
    def largest(values):
        return max(v.lower() for v in values).union(max(v.upper() for v in values))
    result = largest(maxima)
    raw = largest(rawmax)
    phase_sq = [3*h*h*v*v*(1-z*z)/4 for v,z in zip(imag,amplitude)]
    assert phase_sq[k]>arb("2e-14") and all(v<arb("2.3e-14") for v in phase_sq[1:])
    assert result>arb("0.1794952") and result<arb("0.1794953")
    emit(kind="exhaustive_genuine_punctured_cold_square_discrepancy",p=prime,n=n,
         real_center="2031/128",square_halfwidth="1/131072",exact_level_rectangle_count=len(rectangles),
         imaginary_peak_inversion_orbit=k, first_floor_cutoff_squared="2e-14",
         uniform_edge_peak_phase_squared_lower=phase_sq[k].lower().str(14),
         uniform_square_phase_squared_upper=max(z.upper() for z in phase_sq[1:]).str(14),
         max_individual_erasures=m, maximum_over_all_minimized_cuts=result.str(16),
         maximum_over_all_untrimmed_cuts=raw.str(16), derivative_error_counting=deriv_radius.str(14),
         contraction_factor_upper=q.str(14))


def physical_obstruction():
    prime = 181
    n, N, kernel, h, imag, amplitude, deriv_radius, q = physical_tube(prime)
    k = 26
    assert all(abs(imag[k])>abs(imag[j]) for j in range(1,N) if j!=k)
    site = lambda j: min(j,n-j)
    cut_u = arb(16324)/100000
    cut_v = arb(3)/4
    pay = []
    for j in range(1,n):
        jj = site(j)
        if abs(amplitude[jj]) < cut_u or abs(imag[jj]) < cut_v*abs(imag[k]):
            continue
        assert abs(amplitude[jj]) > cut_u and abs(imag[jj]) > cut_v*abs(imag[k])
        orientation = imag[k]*amplitude[jj]*imag[jj]
        assert orientation>0 or orientation<0
        pay.append((j, kernel[(k-j)%n].real * (1 if orientation>0 else -1)))
    m = isqrt(n)//2
    prices = [z for _,z in pay]
    debit = optimal_debit(prices,m)
    raw = sum(prices,arb(0))
    trimmed = raw-debit
    assert trimmed > arb("0.87339") and trimmed < arb("0.87340")
    # X=V/cosh(gamma); at |y|=h the nominated branch crosses the
    # tailored threshold on every real floor, while no site reaches 1e-8.
    phase_sq = [arb(3)*h*h*v*v*(1-a*a)/4 for v,a in zip(imag,amplitude)]
    end_lower = phase_sq[k].lower()
    all_upper = max(z.upper() for z in phase_sq[1:])
    assert end_lower>arb("2e-14") and all_upper<arb("2.5e-14")
    emit(kind="genuine_punctured_cold_square_signed_cut",p=prime,n=n,
         real_center="2031/128",square_halfwidth="1/131072", both_vertical_half_rays=True,
         imaginary_peak_inversion_orbit=k, first_floor_cutoff_squared="2e-14",
         uniform_edge_peak_phase_squared_lower=end_lower.str(14), uniform_square_phase_squared_upper=all_upper.str(14),
         real_amplitude_threshold="16324/100000", imaginary_fraction_threshold="3/4",
         retained_cut_sites=[j for j,_ in pay], max_individual_erasures=m,
         untrimmed=raw.str(16), optimal_erasure_debit=debit.str(16),
         minimized=trimmed.str(16), derivative_error_counting=deriv_radius.str(14),
         contraction_factor_upper=q.str(14))


if __name__ == "__main__":
    layer_bounds()
    all_cuts()
    physical_obstruction()
