# Problem 26: a joint obstruction to opposite and triangle weights

For both theta signs, the constant, opposite-point, and triangle weights **together** have limiting restricted optimum $1/\sqrt2$ after division by $\sqrt n$. The three coefficients can depend arbitrarily on the field size. In fact, in the normalization below an asymptotically optimal row has coefficients tending to $(2,0,0)$. This extends the [opposite-point restriction](fourier.md) and gives a Legendre-family proof of the [triangle restriction draft](chatgpt-2026-11-17.md#findings-compared-with-the-local-routes). The joint constraint comes from the *even* Fourier modes. It is an obstruction to these certificates, not an upper bound on the full theta LP.

## Setup and the exact three-parameter row

Let $q\equiv1\pmod4$ be an odd field order (take $q=p$ for [Randomstrasse101 Problem 26](https://randomstrasse101.math.ethz.ch/posts/PaleyGraph/)). Set $r=\sqrt q$, $Q=\mathbb F_q^{\times 2}$, $n=(q-1)/2$, $s(a)=\chi(1-a)$, and $D_\sigma=\{a\in Q:s(a)=\sigma\}$. Here $\chi(0)=0$. Use the unnormalized Fourier transform $F$ on $Q$ and the conventions $\theta_+=\vartheta(\overline H)$, $\theta_-=\vartheta(H)$. A row $f$ must have $f(1)=1$, vanish off $\{1\}\cup D_\sigma$, be real and inversion-even, and satisfy $Ff\ge0$; its value is $Ff(0)$. Averaging the theta SDP gives this LP, and transitivity gives $\theta_+\theta_-=n$ as in [fourier.md](fourier.md).

Write $\lambda=Fs$, $X=\lambda/r$, $K=F\operatorname{diag}(s)F^{-1}$, and
\[
T_2(x)=2x^2-1,\qquad
g_2=F^{-1}T_2(X)=\frac{2}{q}(s*s)-\delta_1,\qquad Y=KT_2(X).
\]
Convolution here is the unnormalized multiplicative convolution on $Q$. The row being optimized is
\[
 f=\delta_1+1_{D_\sigma}\left(\frac{a+b\,s(-x)}{r}+2c\,g_2(x)\right),
 \qquad a,b,c\in\mathbb R.                                             \tag{1}
\]
This is exactly the degree-two restriction of the combined basis in [witnesses.py](../witnesses.py), up to coefficient scaling. The $T_1$ term is redundant on either support, as is $s(x^2)=s(x)s(-x)$. The triangle interpretation follows from
\[
 4(1_{D_\sigma}*1_{D_\sigma})(x)=n-4-2\sigma+(s*s)(x)
 \quad (x\in D_\sigma).
\]
Indeed, expand the convolution square of $2\,1_{D_\sigma}=\mathbf1+\sigma s-\delta_1$, using $\sum s=-1$. The left side counts common neighbors in the Cayley graph with difference set $D_\sigma$, multiplied by four. Thus ordinary common-neighbor weights and centered common-neighbor weights give the same family when the constant column is included.

For $k=2\ell\ne0$, put $U=X_\ell$ and $V=X_{\ell+n/2}$. The constraint is exactly
\[
 (Ff)(2\ell)=1+\frac{\sigma a+b}{2}X_{2\ell}
              +\frac{\sigma b}{2}(U+V)
              +c\big[T_2(X_{2\ell})+\sigma Y_{2\ell}\big]
              -\frac{a+b\,s(-1)}{2r}+\frac{3c}{q}.                       \tag{2}
\]
In detail, $2\,1_{D_\sigma}s(-x)=s(-x)+\sigma s(x^2)-s(-1)\delta_1$; the two transforms at $2\ell$ are $\lambda_{2\ell}$ and $\lambda_\ell+\lambda_{\ell+n/2}$. Also $g_2(1)=2(n-1)/q-1=-3/q$, since $s$ is inversion-even, has square 1 off the identity, and vanishes there. Masking $g_2$ therefore gives $2F(1_{D_\sigma}g_2)=T_2(X)+\sigma Y+3/q$ at **all** modes.

## The four coordinates have independent limiting support

For uniformly sampled $\ell$ modulo $n$, the law of $(X_{2\ell},X_\ell,X_{\ell+n/2},Y_{2\ell})$ tends to that of
\[
 (\operatorname{Re}z_1,\operatorname{Re}z_2,\operatorname{Re}z_3,
                 (\operatorname{tr}h_1+\operatorname{tr}h_2)/2),          \tag{3}
\]
where the $z_i$ are independent Haar circles, the $h_i$ are independent Haar $SU(2)$ matrices, and the two groups of variables are independent. This is a field-size limit, with a uniform estimate for each fixed test moment. In particular every neighborhood of each of the 16 corners of $[-1,1]^3\times[-2,2]$ is hit for all sufficiently large $q$, even after removing $k=0$.

**The three Jacobi coordinates.** Extend all multiplicative characters by zero at zero. Write $z(\alpha)=J(\alpha,\chi)/r$ and choose a character $\rho$ of order four. For an $\alpha$ restricting to $\eta_\ell$ on $Q$, the three coordinates are the real parts of $z(\alpha^2),z(\alpha),z(\alpha\rho)$ off the four characters of order dividing four. For example, $X_\ell=(J(\alpha,\chi)+J(\alpha\chi,\chi))/(2r)$, and the two normalized Jacobi sums are inverses on the circle. Sampling $\alpha$ uniformly induces uniform $\ell$. With $G$ the Gauss sum and $(A,B,C,D)$ the normalized Gauss sums for $(\alpha,\alpha\chi,\alpha\rho,\alpha\rho\chi)$, the three circle coordinates, up to unit factors, are $(AB/(CD),A/B,C/D)$. For the first quotient use
\[
 G(\alpha)G(\alpha\chi)=\bar\alpha(4)G(\alpha^2)G(\chi)
\]
and the same identity for $\alpha\rho$. The identity follows from counting roots of $4u(1-u)=v$ in $J(\alpha,\alpha)$ and then using the Gauss formula for Jacobi sums. The four shifts are distinct, so the nonzero fixed Fourier moments vanish by [Katz, *Gauss Sums, Kloosterman Sums, and Monodromy*, §§9.5–9.6](https://web.math.princeton.edu/~nmk/Katz-GKM.pdf). The three exponent rows are independent, so the map of tori is onto. The constant unit factors, including $G(\chi)/r$ and $\rho(4)^{-1}$, preserve that Haar law.

**The quadratic coordinate.** Let
\[
 t(x)=\sum_{u\in\mathbb F_q}\chi(u(u-1)(u-x)).
\]
For $x\in Q\setminus\{1\}$, $(s*s)(x)=(t(x)-2)/2$: expand $1_Q(u)=(1+\chi(u))/2$ for $u\ne0$ in the convolution. The untwisted quadratic sum over $u\ne0$ is $-2$ (the complete sum is $-1$ and its $u=0$ term is $1$), and the twisted term is $t(x)$. Thus
\[
 Y_k=\frac1q\sum_{x\in Q\setminus\{1\}}\chi(1-x)t(x)\eta_k(x)
           -\frac{2}{q}\lambda_k.                                     \tag{4}
\]
The sheaf $N=\mathrm{TwLeg}(1)[1]$ in [Katz, *Convolution and Equidistribution*, Chapter 15](https://web.math.princeton.edu/~nmk/mellin331.pdf) has perverse trace $\chi(1-x)t(x)/q$ off 1: the elliptic-curve trace is $-t(x)$ and the shift changes the sign. The stalk at 1 is zero from the quadratic twist of unipotent inertia. Put $N'=N\otimes\mathcal L_{\chi(x)}$. For a perverse sheaf $M$, write $m_M(\beta)=\sum_{x\ne0}\beta(x)\operatorname{tr}(\mathrm{Frob}_x\mid M)$. The first term of (4) at $2\ell$ is
\[
 \tfrac12\big[m_N(\alpha^2)+m_{N'}(\alpha^2)\big]
 =\tfrac12\big[m_{[2]_*N}(\alpha)+m_{[2]_*N'}(\alpha)\big].              \tag{5}
\]
Here $[2]:x\mapsto x^2$, and the equality is the finite pushforward trace formula. Katz's Theorem 15.2 gives **both** geometric and arithmetic convolution group $SL(2)\times SL(2)$ on $N\oplus N'$. By Theorem 8.1 finite power pushforward changes the geometric group by at most a finite-index restriction. This product is connected, so the two groups remain the full product for $[2]_*(N\oplus N')$. The correction in (4) is uniformly $O(1/r)$ by the Jacobi bound. Also $|Y_0|\le 2+2/q$: each Mellin trace in (5) is bounded by its convolution dimension two, including at bad characters, by Katz's Lemma 2.1 and the weight bound. Here $\lambda_0=-1$, from $J(1,\chi)=J(\chi,\chi)=-1$.

**Why conditioning on the Jacobi coordinates is allowed.** The three circle coordinates (up to constant signs) are Mellin traces of dimension-one objects: $\mathcal L_{\chi(1-x)}(1/2)[1]$, its $\rho(x)$ twist, and its $[2]_*$ image, in the order dictated by $z(\alpha),z(\alpha\rho),z(\alpha^2)$. This follows from the Kummer trace formula and the sign of $[1]$. For the joint direct sum with the two pushed Legendre objects, the geometric group is a subgroup of $\mathbb G_m^3\times SL(2)^2$ surjecting onto $SL(2)^2$. Its identity component still surjects onto this connected product. Taking its derived subgroup yields a subgroup projecting onto the same product, since $SL(2)^2$ is perfect; the derived subgroup projects trivially to the torus. Hence the geometric group contains $\{1\}^3\times SL(2)^2$. This argument does not assume a joint independence theorem for the torus and Legendre traces.

Test against a Laurent monomial on the torus and the two characters of $\operatorname{Sym}^{d_1},\operatorname{Sym}^{d_2}$ of the standard $SL(2)$ representation. When either $d_i>0$, the resulting representation has no geometric invariants by the product inclusion. The corresponding fixed product of Mellin characters has average $O(q^{-1/2})$. To see the required uniformity in $q$, use the proof of Katz's Theorem 7.3 and Remark 7.5, as follows:

- Outside a bounded set of bad characters, tensor products and summands of the Mellin representations are evaluated by middle convolution and its summands. The number of bad characters of the original sum is bounded by boundary ranks; cohomology is in degree zero and trace magnitudes are bounded by convolution dimension. Including the bad set in the average of the convolution trace costs $O(1/q)$ at fixed test degree.
- The original sheaves and their convolution duals have bounded ranks, are tame at $0,\infty$, and are lisse off 1 on $\mathbb G_m$. This survives the power pushforward for these inputs, since the map is finite étale there, tame at the boundaries, and takes 1 to 1. Iterating Katz's Lemma 19.4 with a fresh tame factor first gives lissity off 1 and bounds the generic rank uniformly. Explicitly, for a nonpunctual product step between factors of generic ranks $r_N,r_M$ and convolution dimensions $d_N,d_M$, the convolution rank is at most $r_N d_M+r_M d_N+r_N r_M$. The compactly supported $H^1$ on the generic multiplication fiber supplies the bound: Grothendieck–Ogg–Shafarevich at the two distinct interior singularities and at the two boundaries bounds $-\chi_c$ by the first two terms, and $H_c^2$ has dimension at most $r_Nr_M$. A punctual part of the accumulated factor is supported at 1 and contributes at most its dimension times the new factor's rank. Convolution dimensions multiply, so every fixed product and its summands have bounded rank.
- Orthogonality averages the Mellin trace to the perverse stalk trace at 1. There is no geometric $\delta_1$ constituent by the absence of invariants. The remaining middle extensions have stalk trace bounded by their generic rank times $q^{-1/2}$.

For $d_1=d_2=0$ use the circle law already proved. The tested characters span polynomials in the two standard $SU(2)$ traces, because $\operatorname{tr}(\operatorname{Sym}^d h)$ is a monic polynomial of degree $d$ in $\operatorname{tr}h$. Laurent monomials on the circle and these polynomials suffice for weak convergence on the compact range. Removing the bounded exceptional set and using (4) proves (3). In particular the proof covers varying prime fields, not just increasing extension degree of a fixed field.

## Consequence for the optimum

Let $\delta_q$ be the maximum, over the 16 corners, of the distance in max norm to the nearest tuple from $2\ell\ne0$. Then $\delta_q\to0$. Given $(a,b,c)$, choose $X_{2\ell}$ at the corner opposite to $\sigma a+b$, each of $U,V$ opposite to $\sigma b$, and $Y_{2\ell}$ opposite to $\sigma c$, with arbitrary signs for zero coefficients. At this exact corner the leading part of (2) is $1-L$, where
\[
 L=\frac{|\sigma a+b|}{2}+|b|+2|c|-c
   \ \ge\ \frac{|a|}{2}+\frac{|b|}{2}+|c|.
\]
Use the actual mode within $\delta_q$. Since $|X_{2\ell}|\le1$, the error of $T_2$ from its corner value $1$ is at most $4\delta_q$. The other corner errors together with this one cost at most $5\delta_q L$. The two explicit field-size corrections in (2) cost at most $(1/r+3/q)L$. Feasibility therefore implies
\[
 (1-5\delta_q-1/r-3/q)L\le1.                                           \tag{6}
\]
This bounds the entire feasible parameter set for large $q$; no bounded-coefficient hypothesis is needed.

At mode zero, $|D_\sigma|=(n-1-\sigma)/2$. The unscaled opposite-point column has sum $(\lambda_0+\sigma(\lambda_0+\lambda_{n/2})-s(-1))/2=O(r)$, while the scaled quadratic column $2\,1_{D_\sigma}g_2$ has sum $O(1)$ by (4)–(5). Hence uniformly over feasible rows
\[
 \frac{(Ff)(0)}{\sqrt n}=\frac{a}{2\sqrt2}+O(1/r).
\]
Equation (6) gives $\limsup a\le2$. A feasible constant row has $a=2r/(r+1)$, $b=c=0$, since $|\lambda_k|\le r$ at $k\ne0$. It attains leading constant $1/\sqrt2$. For any asymptotically optimal sequence $a\to2$, and (6) forces $b,c\to0$. This leaves open families of degree at least three, growing degree, or different arithmetic features.

## Three finite effects and the square control

1. The explicit constant row above has value $(r+1)/2-(1+\sigma)/(r+1)$. For primes $p\ge13$ this is strictly bigger than $\sqrt{p-1}/2$ on both sides, but its normalized excess is $1/\sqrt{2p}+O(p^{-1})$. At $p=5$ the plus side has value exactly $\sqrt n/\sqrt2$. Strict inequality at sufficiently large *finite* primes already follows from the constant row.
2. The optimized constant row is slightly better still at prime order with $D_\sigma\ne\varnothing$. Each $\lambda_k$ lies in $\mathbb Q(\zeta_n)$, unramified at $p$, whereas $\mathbb Q(\sqrt p)$ is ramified there. Thus $|\lambda_k|<\sqrt p$. The exact constant optimum is $1+2|D_\sigma|/(1+\max_{k\ne0}(-\sigma\lambda_k))$. The Jacobi endpoint law forces its normalized value to tend to $1/\sqrt2$ as well.
3. At $p=9413$ the triangle column by itself beats the **optimized** constant on both sides. Adding the opposite column makes the gain about $0.000149991$ on the plus side and $0.000141979$ on the minus side in normalized units. The interval replay below proves the strict finite inequalities. The three-parameter theorem excludes a positive limiting excess.

For $q=r^2$ with $r$ an odd prime, the same joint law and restriction apply. The actual values are $\theta_+=r-1$, $\theta_-=(r+1)/2$: $B=\mathbb F_r^\times$ is a clique in $H$, and the minus constant row gives $(r+1)/2$, so the product identity makes both bounds exact. In particular both small-family optima tend to $1/\sqrt2$, while the **actual plus** value tends to $\sqrt2$ after normalization. The square subfield witness $1_B$ lies outside (1) asymptotically. Another difference is exact Jacobi saturation: on nontrivial modes annihilating $B$, $\lambda_k=r$, by the coset identity in [square-order-control.md](square-order-control.md#the-fourier-frequencies-carrying-the-discrepancy). The saturated modes have vanishing density, consistent with the same joint weak law. A fixed small-family obstruction alone cannot distinguish the prime and square full optima.

## Replay

Run from the repository root with the existing NumPy, SciPy and python-flint environment. The table uses floating-point restricted LPs; only the four comparisons at $p=9413$ in the last block are interval-certified. That block keeps each candidate in the small family: it uses the exact integer cyclic convolution, fixes the coefficient numerators, increases the diagonal by an integer that encloses all Fourier errors, and rescales. For the constant optimum an upper bound uses just one nonzero mode, no assumption about which mode is extremal.

| $q$ | $\delta_q$ (FFT) | Constant plus / minus | Combined plus / minus |
|---:|---:|:---|:---|
| $9413$ | $0.696733$ | $0.71414066$ / $0.71443655$ | $0.71429065$ / $0.71457853$ |
| $97^2$ | $0.784231$ | $0.71413695$ / $0.71443451$ | $0.71416075$ / $0.71443451$ |
| $37253$ | $0.558820$ | $0.71070436$ / $0.71077990$ | $0.71071895$ / $0.71077996$ |
| $193^2$ | $0.524637$ | $0.71070455$ / $0.71078009$ | $0.71070459$ / $0.71078009$ |
| $151337$ | $0.362229$ | $0.70890814$ / $0.70892681$ | $0.70890816$ / $0.70892695$ |
| $389^2$ | $0.384669$ | $0.70890824$ / $0.70892688$ | $0.70890830$ / $0.70892688$ |
| $1000033$ | $0.306625$ | $0.70781140$ / $0.70781423$ | $0.70781142$ / $0.70781423$ |
| $997^2$ | $0.313725$ | $0.70781353$ / $0.70781637$ | $0.70781353$ / $0.70781637$ |

~~~sh
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python -B - <<'PY'
from fractions import Fraction
from itertools import product
from math import sqrt

import numpy as np
from flint import acb, ctx
from scipy.optimize import linprog
from square_control import square_field_sign
from theta import paley_sign

for r,p in [(97,9413),(193,37253),(389,151337),(997,1000033)]:
    for q,s in ((p,paley_sign(p)), (r*r,square_field_sign(r))):
        n = len(s)
        X = np.fft.fft(s).real / sqrt(q)
        g2 = np.fft.ifft(2*X**2-1).real
        Y = np.fft.fft(s*g2).real
        even = np.column_stack((X[2::2], X[1:n//2], X[n//2+1:], Y[2::2]))
        radius = max(np.min(np.max(np.abs(even - [a,b,c,2*d]), axis=1))
                     for a,b,c,d in product((-1,1), repeat=4))
        basis = np.column_stack((np.ones(n)/sqrt(q), np.roll(s,n//2)/sqrt(q), 2*g2))
        print(q, f"radius {radius:.6f}")
        for sig in (1,-1):
            vals = []
            for cols in ([0],[0,2],[0,1,2]):
                v = np.fft.rfft((s==sig)[:, None]*basis[:,cols], axis=0).real
                lp = linprog(-v[0], A_ub=-v[1:], b_ub=np.ones(len(v)-1),
                             bounds=(None, None), method="highs",
                             options={"primal_feasibility_tolerance": 1e-9,
                                      "dual_feasibility_tolerance": 1e-9})
                assert lp.success, lp.message
                vals.append(f"{(1-lp.fun)/sqrt(n):.9f}")
            print(sig, *vals)  # constant, triangle, combined

ctx.prec = 96
q, scale = 9413, 10**14
s = paley_sign(q)
n = len(s)
h = np.convolve(s.astype(np.int64), s.astype(np.int64))
h[:n-1] += h[n:]
op = np.roll(s, n//2)
for sig,k,kind,(a,b,c) in (
    ( 1,536,"triangle",(2040540745569,0,4049755)),
    ( 1,536,"combined",(2040828508080,541905685,21058267)),
    (-1,223,"triangle",(2040593731586,0,8881659)),
    (-1,223,"combined",(2040842067563,257783100,12647835)),
):
    mask = [int(x==sig) for x in s]
    row = [m*(a+b*int(op[j])+c*int(h[j])) for j,m in enumerate(mask)]
    row[0] = scale
    assert all(row[j] == row[-j] for j in range(n))
    repair = max(0, -min(int(z.real.lower().floor().unique_fmpz())
                         for z in acb.dft(row)))
    lower = Fraction(sum(row)+repair, scale+repair)
    hi = int((acb.dft(mask)[k].real.upper()*scale).ceil().unique_fmpz())
    assert hi < 0
    constant_upper = 1 + Fraction(sum(mask)*scale, -hi)
    assert lower > constant_upper > 0 and 4*lower**2 > q-1
    print("certified", sig, kind, lower, constant_upper,
          float(lower-constant_upper)/sqrt(n))
PY
~~~
