# Cross-convolution, loss of the mark, and the signed energy integral

**Status: partial progress; no proof or refutation of Problem 26.** This note works with the actual complementary quadratic optimizers, including across support changes. It gives an exact positive measure whose signed character average is the energy difference, an explicit moving-cutoff error, and two obstructions to closing the argument by convolution. In particular, cross-convolution tends to the uniform distribution even on the bad square sequence. Positive convolution trials of degree at least two lose their useful marked value when both positional second moments are $o(\sqrt n)$. Iterating the previous scalar moment bound does not repair that loss.

The only files written for this investigation are this note and [astra-convolution-11.py](astra-convolution-11.py). The script prints its results and writes no data files. The starting sources were [quadratic theta](quadratic-theta.md), [the quadratic path limit](parallel-quadratic-limit-9.md), [the prime moving-width obstruction](astra-quadratic-10.md), and [square endpoint uniqueness](square-endpoint-uniqueness.md). The statement of [Randomstrasse101 Problem 26](https://randomstrasse101.math.ethz.ch/posts/PaleyGraph/) and [Hanson–Petridis, Theorem 1.2](https://arxiv.org/pdf/1905.09134) were checked against their primary sources on 2026-11-17.

## 1. Normalization and a uniform bound for every fixed scaled width

Let $q\equiv1\pmod4$ be a prime or an odd prime square, $n=(q-1)/2$, $Q=\mathbb F_q^{\times2}$, and $G=\widehat Q$. Use unnormalized cyclic convolution on $G$. Put $s(t)=\chi(1-t)$, $J=\mathbf1\mathbf1^\mathsf T/n$, and

$$
 P_\pm=(I-J\pm K)/2,\qquad
 Q_\pm(r)=J+rP_\pm+r^{-1}P_\mp.
$$

For $0<r\le1$, let $x=A_+(r)$, $y=A_-(r)$, $a=x_0=y_0^{-1}$, and $c=\mathbf1^\mathsf T x/\sqrt n=\mathbf1^\mathsf T y/\sqrt n$. Thus

$$
 x,y\ge0,\quad y=Q_+(r)x,\quad
 x_i y_i=\mathbf1_{i=0},\quad x^\mathsf T y=1.
$$

Write $m(r)=\log a$,

$$
 S_+=r\|P_+x\|^2,\quad S_-=r\|P_-y\|^2,
 \quad b=1-c^2=S_++S_-,\quad g=S_+-S_-.
 \tag{1}
$$

Then $d m/d\log r=-g/2$. All these are actual optimizers, not arbitrary vectors in a chosen compression.

The translation argument gives $x_i\le a$, $y_i\le a^{-1}$. The fixed-point equation and the Jacobi entry bound give

$$
 |a-a^{-1}|\le2d c\sqrt{q/n},\qquad
 a+a^{-1}\le2\sqrt{1+d^2c^2q/n},\qquad d=(1-r)/(1+r).
$$

Using the exact norm identity from the preceding notes, with $u=c^2$,

$$
 2u+(r+r^{-1})(1-u)
 =\|x\|^2+\|y\|^2
 \le2\sqrt{nu+d^2qu^2}.
$$

Set $r=\kappa/\sqrt q\le1$. Multiplication by $r/(1+r^2)$, followed by dropping the positive $2ru/(1+r^2)$ term, gives

$$
 1-u\le\kappa\sqrt{2u+4u^2}.
$$

Squaring is legitimate because both sides are nonnegative. Solving the resulting inequality on $0<u\le1$ proves

$$
 \boxed{
 c^2\ge L(\kappa):=
 \frac1{1+\kappa^2+\kappa\sqrt{\kappa^2+6}},\qquad
 1-c^2\le\sqrt6\,\kappa.}
 \tag{2}
$$

Unlike the earlier $1-\sqrt7\kappa$ estimate, the lower bound $L(\kappa)>0$ applies to **every fixed** $\kappa>0$. It is independent of primality, and therefore cannot itself remove the square obstruction.

## 2. Cross-convolution is an exact energy measure

Define probabilities and their positional characteristic functions by

$$
 \mu_+=x/(c\sqrt n),\quad \mu_-=y/(c\sqrt n),\qquad
 f_\sigma(t)=\sum_{h\in G}\mu_\sigma(h)h(t).
$$

Both $f_\sigma(1)=1$, and $|f_\sigma(t)|\le1$. The reciprocal relation says

$$
 f_-(t)=r f_+(t)\ (s(t)=+1),\qquad
 f_+(t)=r f_-(t)\ (s(t)=-1).
 \tag{3}
$$

Consequently

$$
 h(t):=f_+(t)\overline{f_-(t)}\ge0,
 \qquad
 \pi_r(t):=c^2h(t)
 \tag{4}
$$

is a probability measure on $Q$. Indeed, Parseval and $x^\mathsf T y=1$ give $c^2\sum_t h(t)=1$. More precisely,

$$
 \boxed{
 \pi_r(1)=c^2,\quad
 \sum_{s(t)=+1}\pi_r(t)=S_+,\quad
 \sum_{s(t)=-1}\pi_r(t)=S_-,\quad
 g(r)=\sum_t s(t)\pi_r(t).}
 \tag{5}
$$

This is a positive-measure representation of the signed derivative. It does not replace the difference by the sum of the two energies.

In frequency coordinates, put $\nu=\mu_+*\widetilde\mu_-$, where $\widetilde\mu(h)=\mu(-h)$. Its transform is $h$, and

$$
 \nu(0)=\frac1{nc^2},\qquad
 0\le\nu(h)\le\nu(0).
 \tag{6}
$$

For the upper bound, the nonnegative Fourier transform $h(t)$ has its largest inverse-transform modulus at zero. Nonnegativity of $\nu$ follows separately from convolution of probabilities. Equivalently, for unnormalized correlations $R_{xy}(\eta)=\sum_i x_i y_{i+\eta}$, $\eta\in G$,

$$
 R_{xy}(\eta)=c^2+\sum_{t\ne1}\pi_r(t)\eta(t),
 \qquad 2c^2-1\le R_{xy}(\eta)\le1.
$$

These quantities are real by inversion symmetry. There is also the following real correlation identity:

$$
 \boxed{R_{xy}
 =\frac r{1+r^2}(R_{xx}+R_{yy})
  +\frac{(1-r)^2}{1+r^2}c^2\mathbf1.}
 \tag{7}
$$

To verify (7), compare its constant Fourier coordinate and its two nonconstant sectors using (3). No support or differentiability assumption is involved.

### Why even strong mixing of this convolution is insufficient

Let

$$
 F(r)=\sum_{t\ne1}|f_+(t)f_-(t)|^2,
 \qquad B_{\sigma,4}=\sum_{s(t)=\sigma}|f_\sigma(t)|^4.
$$

Since $0\le h(t)\le r$ for $t\ne1$,

$$
 \boxed{F=r^2(B_{+,4}+B_{-,4})
       \le r\frac{1-c^2}{c^2}.}
 \tag{8}
$$

Parseval yields the exact distance to the uniform probability $u_G$:

$$
 n\|\nu-u_G\|_2^2=F,\qquad
 \|\nu-u_G\|_{\rm TV}\le\tfrac12\sqrt F.
$$

At every fixed scaled width, (2) implies the explicit bound

$$
 F(\kappa/\sqrt q)
 \le\frac{\kappa^2(\kappa+\sqrt{\kappa^2+6})}{\sqrt q}.
 \tag{9}
$$

Thus the actual cross-convolution converges to uniform in relative squared $\ell_2$ distance and in total variation **through both primes and squares**. This is a proved failure of the proposed implication “cross-convolution mixes, therefore the marked value tends to zero.”

For a square $q=s^2$, the subfield trial gives

$$
 M_+(\kappa/s)\le\frac{d^2}{n}
  +\frac\kappa s\left(d-\frac{d^2}{n}\right),
 \qquad d=(s+1)/2.
$$

Therefore for $0<\kappa<1$,

$$
 \liminf_{s\to\infty}m(\kappa/s)
 \ge\tfrac12\log\frac2{1+\kappa}>0,
 \tag{10}
$$

while (9) still tends to zero. This square comparison is analytic and does not rely on extrapolating the experiments. It also does not require uniform entry into a terminal support interval.

## 3. Positive convolution trials lose the mark

Reflection of frequency coordinates commutes with the real symmetric circulant quadratic form and fixes the anchor. Uniqueness therefore makes $x,y$, and hence $\mu_\pm$, inversion-even. We may consequently identify convolution and reflected convolution in the following discussion.

Call a convolution word **mixed** if it contains at least one factor of each of $\mu_+,\mu_-$. Every mixed word is $\nu*\rho$ for a probability $\rho$. By (6), its maximum coordinate is at most $1/(nc^2)$. The same bound holds for any convex mixture of mixed words, even if degrees and coefficients depend on $q,r$.

For any probability $v\ge0$, any test width $t>0$, and either sign,

$$
 \langle v,Q_\sigma(t)v\rangle\ge\|Jv\|^2=1/n.
$$

Its normalized marked trial value is $v_0/\sqrt{\langle v,Q_\sigma(t)v\rangle}$. Hence every mixed-word trial satisfies

$$
 \boxed{\frac{v_0}{\sqrt{\langle v,Q_\sigma(t)v\rangle}}
       \le\frac1{c^2\sqrt n}.}
 \tag{11}
$$

At fixed scaled width this tends to zero by (2), at **any** test width. The actual normalized optimum is of order one. Cross-convolution does not supply a useful marked trial despite its good positivity and mixing properties.

There is a version that also covers pure powers. Put $C_{2,\sigma}=\sum_t|f_\sigma(t)|^2$. An autocorrelation $\mu_\sigma*\mu_\sigma$ has maximum $C_{2,\sigma}/n$; subsequent probability convolutions cannot increase that maximum. Thus every convex mixture $v$ of words of total degree at least two satisfies

$$
 \boxed{\frac{v_0}{\sqrt{\langle v,Q_\sigma(t)v\rangle}}
 \le\frac{\max\{C_{2,+},C_{2,-},c^{-2}\}}{\sqrt n}.}
 \tag{12}
$$

In particular, when both $C_{2,\sigma}=o(\sqrt n)$ and $c$ stays bounded below, **all** such positive mixtures give a vanishing normalized mark. This includes unbounded convolution degrees. The restriction to nonnegative coefficients matters: subtraction or clipping can evade this argument, but requires a new proof of positivity and of its marked energy.

This bound does not cover the entire remaining case from the preceding note: $C_2\asymp\sqrt n$ with $C_4\ll C_2$ is still possible at the level of the estimates. Section 4 addresses why scalar moment iteration alone leaves that case open.

### Squaring the width is exact, but has a complementarity cost

Set $u=\mu_+*\mu_+$, $v=\mu_-*\mu_-$. Equations (3) give

$$
 v=Q_+(r^2)u,\quad
 u_0=C_{2,+}/n,\quad v_0=C_{2,-}/n,\quad
 \langle u,v\rangle=(1+F)/n.
$$

Testing both reciprocal problems proves

$$
 \boxed{
 \log\frac{C_{2,+}}{\sqrt{n(1+F)}}
 \le m(r^2)\le
 \log\frac{\sqrt{n(1+F)}}{C_{2,-}}.}
 \tag{13}
$$

The interval width is exactly

$$
 \log\frac{n(1+F)}{C_{2,+}C_{2,-}}
 =\log\frac{\langle u,v\rangle}{u_0v_0}\ge0.
 \tag{14}
$$

Thus $r\mapsto r^2$ is genuine, but it does not preserve complementarity. When both $C_2$'s are bounded and $F=o(1)$, the interval width is $\log n-O(1)$, and grows rather than shrinks. Formula (12) explains this without selecting a particular degree.

For completeness, mixing a self-convolution with the original optimizer has a stronger first-order necessary condition than the earlier quadratic trial inequality. Set $z=c\sqrt n(\mu_\sigma*\mu_\sigma)$, $a_\sigma=A_{\sigma,0}$, and

$$
 \rho_\sigma=z_0/a_\sigma
 =cC_{2,\sigma}/(a_\sigma\sqrt n).
$$

The feasible direction $z-\rho_\sigma A_\sigma$ fixes the mark. Its right derivative gives

$$
 \rho_\sigma\le
 \langle A_{-\sigma},z\rangle
 =c^2\left[1+r B_{\sigma,3}+r^2B_{-\sigma,3}\right],
 \qquad
 B_{\sigma,3}=\sum_{s(t)=\sigma} f_\sigma(t)^3.
 \tag{15}
$$

The cubic moments here are **signed**, since the inversion-even characteristic functions are real but need not be nonnegative. No replacement by absolute cubic moments is an identity. Inequality (15) is also an immediate consequence of $A_{-\sigma}\ge0$ and complementarity at the root. In the dispersed prime experiments it has large positive slack; it does not balance the two energies.

## 4. What iteration of the prime moment bound actually gives

For one side write $D=\sum_{s(t)=-\sigma}|f_\sigma(t)|^2<1$,

$$
 \alpha=(1+\sqrt D)/2,\qquad
 T_p=\left\lfloor\frac{1+\sqrt{1+4n}}2\right\rfloor.
$$

The previous phase-packing argument, using Hanson–Petridis, bounds the number of positions with $|f_\sigma(t)|^2>\alpha$ by $T_p$. The elementary scalar inequality

$$
 z^k\le\alpha^{k-1}z+(1-\alpha^{k-1})\mathbf1_{z>\alpha}
 \qquad(0\le z\le1)
$$

gives, for every integer $k\ge1$,

$$
 C_{2k,\sigma}\le\alpha^{k-1}C_{2,\sigma}
 +(1-\alpha^{k-1})T_p.
 \tag{16}
$$

Applying the original bound to the probability $\mu_\sigma^{*k}$ also gives

$$
 C_{4k,\sigma}\le\alpha_k C_{2k,\sigma}+(1-\alpha_k)T_p,
 \quad \alpha_k=(1+\sqrt{D_k})/2,
 \quad D_k\le D^k.
 \tag{17}
$$

These statements need no rate of approach to a subgroup. They remain upper bounds on higher moments. They supply no lower bound that would recover $C_2$ from them. For instance, scalar profiles with $\Theta(n)$ nonidentity squared amplitudes of order $n^{-1/2}$ have $C_2=\Theta(\sqrt n)$, $C_4=O(1)$, and vanishing higher nonidentity moments. At $r=\kappa/\sqrt p$, their possible energy scale $rc^2(C_2-1)$ is order one. This observation is only about scalar moment constraints: it does **not** construct a positive characteristic function or an actual QP pair.

A stronger check uses an actual square pair. At $q=49$, $r=1/7$, the interval certificate below proves

$$
 C_{2,+}<5,\quad C_{2,-}<5,\quad D_\pm<1,
 \quad S_+-S_->0.11,\quad m(r)>0.03.
 \tag{18}
$$

Here the hypothetical prime threshold is $T=5$. Since $C_{4k}\le C_{2k}\le C_2<5$, **every** inequality (16) and (17), on both sides and at every degree, holds for this square pair. This includes iterating the scalar inequality on convolution powers. Thus that entire scalar hierarchy at one width does not imply pointwise energy balance or distinguish all square controls. This does not assert that the square path passes prime tests at every width, nor that the stronger phase-packing statement itself holds over squares.

The least-norm endpoint square pair makes the asymmetry particularly explicit. From the endpoint uniqueness note,

$$
 C_{2,+}=C_{4,+}=s-1,\qquad
 C_{2,-}=\frac{2s}{s+1},\qquad
 C_{4,-}=1+\frac{4(s-1)}{(s+1)^3}.
$$

The minus formula follows from $f_-=2/(s+1)$ on its $n/2$ allowed nonidentity positions. Its pure convolution trials have a vanishing normalized mark; the plus side retains the subfield concentration. At $r=0$ the cross-convolution is exactly uniform on every field, so its uniformity has already discarded the endpoint mark entirely.

## 5. A controlled signed integral and the exact missing estimate

Integrating (1) and using (2) gives an explicit cutoff certificate. For $0<\kappa<\sqrt q$,

$$
 \left|\int_0^{\kappa/\sqrt q}g(r)\frac{dr}{r}\right|
 \le\int_0^\kappa (1-L(t))\frac{dt}{t}
 \le\sqrt6\,\kappa.
$$

Since $m(1)=0$ and $m(0)=\log(\theta_+/\sqrt n)$,

$$
 \boxed{
 \left|2\log\frac{\theta_+}{\sqrt n}
  -\int_{\kappa/\sqrt q}^{1}\sum_t s(t)\pi_r(t)\frac{dr}{r}\right|
 \le\sqrt6\,\kappa.}
 \tag{19}
$$

This uses the actual path, with no frozen support and no uniform fixed-depth assumption. It is an exact reduction, not a proof that the integral is small.

To expose the arithmetic needed beyond mixing, use $\sum_{t\ne1}s(t)=-1$. Put

$$
 V(r)=\sum_{t\ne1}\left(\pi_r(t)-\frac b{n-1}\right)^2
      =c^4F-\frac{b^2}{n-1}\ge0,
$$

and define the signed covariance

$$
 \mathcal C(r)=\sum_{t\ne1}
 \left(s(t)+\frac1{n-1}\right)
 \left(\pi_r(t)-\frac b{n-1}\right).
$$

Then

$$
 g(r)=-\frac b{n-1}+\mathcal C(r),\qquad
 |\mathcal C(r)|\le\sqrt{\left(n-1-\frac1{n-1}\right)V(r)}.
 \tag{20}
$$

The integrated first term is at most $\log(\sqrt q/\kappa)/(n-1)$. Therefore a precise prime-specific target, equivalent to the conjecture, is

$$
 \boxed{
 \lim_{\kappa\downarrow0}\limsup_{p\to\infty}
 \left|\int_{\kappa/\sqrt p}^{1}\mathcal C_p(r)\frac{dr}{r}\right|=0.}
 \tag{21}
$$

Here $p\equiv1\pmod4$ runs over primes. The baseline and cutoff errors in this equivalence have been bounded explicitly above. Covariance cancellation, rather than decay of both energies, is permitted by (21).

The scale loss in using only mixing is now visible. Formula (9) gives $F=O_\kappa(p^{-1/2})$, while the Cauchy–Schwarz bound sees $n c^4F$, potentially of order $\sqrt p$. Even at a single width, $F=o(1)$ is far from the uncentered sufficient scale $F=o(1/n)$. Across an interval of logarithmic length $O(\log p)$, a uniform pointwise $o(1)$ bound on the signed density also needs a rate or an integrable envelope.

For example, a stronger sufficient variance estimate would control the integral of $\sqrt{nV(r)}$ by $o(1)$; this still allows nonzero total energy if its positional distribution is nearly uniform. Another stronger sufficient small-width condition is

$$
 n c^4(B_{+,4}+B_{-,4})\le H(r)^2,
 \qquad \int_0^\epsilon H(r)\,dr\longrightarrow0
 \quad(\epsilon\downarrow0),
 \tag{22}
$$

uniformly over the relevant primes and widths. Indeed (8) gives $|g(r)|\le c^2\sqrt{(n-1)F(r)}\le rH(r)$, so its small-width integral is bounded by $\int_0^\epsilon H(r)dr$. For the remaining fixed-width interval one could use the fixed-width convergence input from the earlier notes. Neither (22), the variance integral, nor the signed target (21) is proved here. The Hanson–Petridis scalar hierarchy (16)–(17) does not supply these estimates for dispersed amplitudes.

Thus the outstanding task is a prime estimate on the **signed positional bias of the actual cross energy measure, integrated over widths**, or a sufficient quantitative substitute. Proving only cross-convolution mixing, or repeating positive convolution and scalar moment tests, leaves the demonstrated losses unresolved.

## 6. Computations and strict square certificates

The following commands are self-contained replays from the repository root:

```sh
.venv/bin/python -B research/astra-convolution-11.py
.venv/bin/python -B research/astra-convolution-11.py --certificate
.venv/bin/python -B research/astra-convolution-11.py --integral
.venv/bin/python -B research/astra-convolution-11.py --primes 9413 37253 --squares 97 193 --kappas .25 1 4
.venv/bin/python -B research/astra-convolution-11.py --primes --squares 7 13 97 193 --kappas .5
```

The default run uses nine primes $13,17,29,41,61,97,173,257,401$, squares $49,121,169$, and scaled widths $1/16,1/4,1,4$, omitting the one width above one. These are 47 independent dense NNLS solves. The largest identity discrepancy was $6.92\cdot10^{-13}$; the largest KKT residual was $6.07\cdot10^{-14}$. It checks the cross measure, (7), the mixed-word cap, the squared-width relation, (2), (8), and the first-order inequality (15). The prime moment checks at scaled widths at most $1/4$ passed. These are floating-point normalization checks, separate from the mathematical proofs.

Mixing a self-convolution with one cross-convolution was sampled at 101 weights. It did not improve the self-convolution trial in the default moving-width cases $\kappa\le1$. There was a tiny improvement on the minus side at $p=17,\kappa=4$, so no blanket claim that mixing never improves a trial is made. The rigorous obstruction is the marked-value bound (12).

Selected larger numerical values at $r\sqrt q=1/4$:

| $q$ | $m(r)$ | $S_+-S_-$ | $F(r)$ | $C_{2,+},C_{2,-}$ | Squared-width interval width |
|---:|---:|---:|---:|---:|---:|
| $9413$ | $0.0004771355$ | $-0.0000713024$ | $9.3273\cdot10^{-8}$ | $3.78896,3.81703$ | $5.78503$ |
| $97^2$ | $0.2283794926$ | $0.1924707780$ | $0.0006283075$ | $95.79318,2.56846$ | $2.95130$ |
| $37253$ | $-0.0004033780$ | $-0.0000096580$ | $5.6326\cdot10^{-9}$ | $3.79273,3.80024$ | $7.16417$ |
| $193^2$ | $0.2316804956$ | $0.1962157215$ | $0.0003198629$ | $191.81635,2.58586$ | $3.62593$ |

The large run uses the existing safeguarded FFT iteration and rejects residuals above $2\cdot10^{-8}$. An additional attempted $193^2,\kappa=1/16$ solve stopped at residual $1.51\cdot10^{-5}$; that row was rejected and is not used. At $9413,\kappa=1/16$, a separate completed row had residual $9.90\cdot10^{-10}$. Large rows are numerical, not interval certificates.

At $q=49$, the script additionally solves the signed orthant equations with 192-bit Arb balls. For denominator 28 the proposed positive bulk coordinates are $\{4,6,12,18,20\}$; for denominator 7 they are $\{1,3,4,6,7,12,17,18,20,21,23\}$. It verifies every strict bulk sign and $|\gamma|<1$, reconstructing the unique damped fixed point. The resulting rigorous enclosures imply:

| Quantity | $r=1/28$ | $r=1/7$ |
|:---|---:|---:|
| $m(r)$ | $0.13625780340207286\ldots$ | $0.03330912595965212\ldots$ |
| $S_+-S_-$ | $0.11552381609009387\ldots$ | $0.11659683362485409\ldots$ |
| $F(r)$ | $0.00644791758267119\ldots$ | $0.04171826169083277\ldots$ |
| $C_{2,+}$ | $5.9821533101346724\ldots$ | $4.1875938488330681\ldots$ |
| $C_{2,-}$ | $2.0558556318848953\ldots$ | $2.8267970829787443\ldots$ |

In the $r=1/7$ column both leakages are below $0.065$, so (18) and its all-degree scalar-moment consequence are certified. The $r=1/28$ column reproduces the earlier prime-moment failure at a narrower width while checking the new cross quantities.

Finally, midpoint integration of the signed density on $[1/(4\sqrt q),1/4]$, with 16, 32, and 64 logarithmic cells, was compared with the exact numerical endpoint expression $2[m(r_{\rm lo})-m(r_{\rm hi})]$. At 64 cells:

| $q$ | Signed endpoint expression | Unsigned numerical integral | Signed quadrature error |
|---:|---:|---:|---:|
| $49$ | $0.2557869210$ | $0.6834552219$ | $2.47\cdot10^{-6}$ |
| $97$ | $0.0204876086$ | $0.6644021641$ | $9.04\cdot10^{-7}$ |
| $401$ | $-0.0101468590$ | $0.7912971228$ | $1.02\cdot10^{-6}$ |

All quadrature errors were inside the deterministic Lipschitz mesh bound from the path-limit note. In particular the signed integral has either sign at prime order, while the unsigned integral is much larger. These finite calculations support the normalizations and identify the obstruction; they establish no all-prime decay estimate in (21).
