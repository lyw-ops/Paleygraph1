# A reciprocal quadratic for the fixed-mark defect

Use the Fourier convention for [Problem 26](https://randomstrasse101.math.ethz.ch/posts/PaleyGraph/) from [quadratic theta](quadratic-theta.md). Write $n=(q-1)/2$, $J=\mathbf1\mathbf1^\mathsf T/n$, and $P_++P_-=I-J$. Put $U_\sigma=\operatorname{im}(J+P_\sigma)$ and $\kappa_\sigma=(P_\sigma)_{00}$. Both $\kappa_\sigma\to1/2$ as $q\to\infty$. The following formulas apply whenever both sectors have positive rank.

## Exact reciprocity

For every $r>0$ define

$$
A_\sigma(r)=\min_{\substack{W\ge0,\ W_0=1\\W\in U_\sigma}}
\left(\|JW\|_2^2+r\|P_\sigma W\|_2^2\right),\qquad
B_{-\sigma}(r)=\min_{b\ge0,\ b_0=1}
\left(\|Jb\|_2^2+r^{-1}\|P_\sigma b\|_2^2\right).
\tag{1}
$$

The reciprocal identity is $A_\sigma(r)B_{-\sigma}(r)=1$. To see this, the objective for $B_{-\sigma}$ is coercive on the positive cone because $\|Jb\|_2^2=(\sum_i b_i)^2/n\ge\|b\|_2^2/n$. If $b$ minimizes it, $q_b=(J+r^{-1}P_\sigma)b$ obeys $q_b\ge0$ and $b_i(q_b)_i=0$ for $i\ne0$. Hence $(q_b)_0=B_{-\sigma}(r)>0$, and $q_b/B_{-\sigma}(r)$ is an admissible $A_\sigma$ trial of energy $1/B_{-\sigma}(r)$. For the opposite bound, every feasible pair has $1\le\langle W,b\rangle$ and $\langle W,b\rangle^2\le(\|JW\|^2+r\|P_\sigma W\|^2)(\|Jb\|^2+r^{-1}\|P_\sigma b\|^2)$ by Cauchy–Schwarz on $U_\sigma$.

For the two-penalty regularization $M_\sigma$ in [quadratic theta](quadratic-theta.md), restricting its feasible set gives $A_\sigma(r)\ge M_\sigma(r)$, and dropping the extra sector penalty gives $B_{-\sigma}(r)\le M_{-\sigma}(r)$. More explicitly, let $x=cj+u+sv$, $y=cj+su+v$ be the normalized reciprocal pair at width $s$, with $j=\mathbf1/\sqrt n$, $u\in\operatorname{im}P_\sigma$ and $v\in\operatorname{im}P_{-\sigma}$. Then $y_0^2=M_\sigma(s)$ and

$$
B_{-\sigma}(r)\le \frac{c^2+s^2\|u\|_2^2/r}{M_\sigma(s)}.
\tag{2}
$$

At $r=s$, this is $(1-s\|v\|_2^2)/M_\sigma(s)$ by the energy identity. The stationary row in (2) can be replaced by any nonnegative $b$ with anchor one, even if no stationary residual has been certified.

The [earlier one-sided path](endpoint-tangent.md) fixes mass $\sqrt n$ and maximizes $2u x_0-\|P_\sigma x\|^2$ over $x\ge0$ in $U_\sigma$. Denote that value by $\Psi_\sigma(u)$. The same family of positive exact-sector vectors gives (1) after optimizing an overall scale. Indeed, $z^2/(1+rE)=\max_{c\ge0}(2cz-c^2(1+rE))$ for $z=x_0$ and $E=\|P_\sigma x\|^2$. Thus $B_{-\sigma}(r)=\sup_{c>0}c^2(r\Psi_\sigma(1/(cr))-1)$. Formulation (1) supplies a reciprocal positive trial in physical coordinates and a direct connection to the pinned slice.

## A direct certificate at the prescribed mark

Fix mean $\mu>0$ and mark $a\sqrt n$ with $a>0$. Denote the minimum negative-part norm on this affine slice of $U_{-\sigma}$ by $d_q(a,\mu)$. For any admissible $b$ in (1) define

$$
Z=a\sqrt n\,b,\quad \nu=\overline Z,\quad
\ell=P_{-\sigma}e_0,\quad D=1-\ell/\kappa_{-\sigma},\quad
\delta=(P_\sigma Z)_0.
$$

The projector is circulant with diagonal $\kappa_{-\sigma}$, so $|\ell_i|\le\kappa_{-\sigma}$ by Cauchy–Schwarz and $D\ge0$. If $\nu\le\mu$, the explicit row

$$
Y=(J+P_{-\sigma})Z+\delta\ell/\kappa_{-\sigma}+(\mu-\nu)D
\tag{3}
$$

has the required mark, mean and sector. Its difference from the positive row $Z+(\mu-\nu)D$ is $-P_\sigma Z+\delta\ell/\kappa_{-\sigma}$, whose terms are orthogonal. This gives

$$
d_q(a,\mu)^2\le a^2n\left(\|P_\sigma b\|_2^2+
\frac{((P_\sigma b)_0)^2}{\kappa_{-\sigma}}\right)
\le a^2n\left(1+\frac{\kappa_\sigma}{\kappa_{-\sigma}}\right)
\|P_\sigma b\|_2^2.
\tag{4}
$$

In particular, if the objective of $b$ in (1) is at most $U$ and $a\sqrt U\le\mu$, its mean meets the condition in (3), and $\|P_\sigma b\|_2^2\le rU$. At $r=R/\sqrt n$ this is a uniform $O(\sqrt R\,n^{1/4})$ certificate for fixed $R,U,a,\mu$. For an actual minimizer of $B_{-\sigma}(r)$, the root correction is even smaller. The KKT identity gives $(P_\sigma b)_0=r(B_{-\sigma}(r)-\overline b)$, so $\delta=O(R)$ at bounded $B_{-\sigma}(r)$ and fixed $a$.

Conversely, for any prescribed-mark row $Y$ of defect $d$, take $Z=Y_+$ and $b=Z/(a\sqrt n)$. Its mean is $\overline Z\le\mu+d/\sqrt n$, and $P_\sigma Z=P_\sigma(Y_-)$. Thus

$$
B_{-\sigma}(r)\le\frac{(\mu+d/\sqrt n)^2}{a^2}+\frac{d^2}{a^2rn}.
\tag{5}
$$

For a fixed field family, $d_q(a,\mu)\le C n^{1/4}$ for all sufficiently large $q$ implies $\lim_{R\to\infty}\limsup_q B_{-\sigma}(R/\sqrt n)\le (\mu/a)^2$. A strict inequality in that limit conversely gives the uniform defect bound by choosing a finite $R$ and applying (3)–(4).

[Astra's certificate](astra-transport-22.md) uses the ordinary $M_\sigma(r)$ directly. It gives the sharper constant $d_q(a,1)^2\le nr/(1-r)$ if $M_\sigma(r)\ge r+(1-r)a^2$. Equations (1)–(4) can certify the defect when the ordinary lower estimate is unavailable. Astra also bounds the cost of increasing the mark directly in the actual reciprocal row. Inequality (4) uses a fresh positive trial, with a mean condition that is checked separately from its Fourier error.

## The field-first limit and broad witnesses

For $W\ge0$ in $U_\sigma$ of mass one let $z(W)=\sqrt n W_0$ and $m_{\mathrm{eff}}(W)=(1-W_0)^2/\|W_{\mathrm{off}}\|_2^2$. By (1) and rescaling the $A_\sigma$ trial,

$$
B_{-\sigma}(R/\sqrt n)=
\max_{\substack{W\ge0,\ W\in U_\sigma\\\sum W=1}}
\frac{z(W)^2}{1+R\sqrt n\bigl(\|W\|_2^2-1/n\bigr)}.
\tag{6}
$$

Write $m_0=n/\sqrt q$ and $T_q(K)=\sup\{z(W):m_{\mathrm{eff}}(W)\ge K m_0\}$ over the same mass-one slice, with zero assigned to the empty supremum. The Jacobi cap gives $z(W)=O(1)$ uniformly. For $m_{\mathrm{eff}}\ge K m_0$, the denominator in (6) is at most $1+CR/K+O(R/\sqrt n)$. For $m_{\mathrm{eff}}<K m_0$ it is at least $1+cR/K$ for all sufficiently large fields at fixed $K$. Indeed $\|W\|^2=W_0^2+(1-W_0)^2/m_{\mathrm{eff}}$. It follows that

$$
\lim_{R\to\infty}\limsup_q B_{-\sigma}(R/\sqrt n)=
\left(\lim_{K\to\infty}\limsup_q T_q(K)\right)^2.
\tag{7}
$$

For the lower bound first fix $R$ and send $q$ then $K$ to infinity. For the upper bound first fix $K$ and send $q$ then $R$ to infinity, and finally let $K$ grow. The limits in $R$ and $K$ exist by monotonicity and boundedness. This gives the same broad margin as the [soft-tail formulation](soft-tail-21.md) for fixed prescribed marks. In particular a field-first bound of one in (7) for both prime signs would prove the uniform pinned defect bound at every fixed $a<1$ and $\mu=1$. It would leave the bounded-effective-size prime regime from [Round 20](anchored-repair-20.md) to be handled.

## A sufficient decay rate for the full conjecture

Write $F_q(R)=B_{-\sigma}(R/\sqrt n)$ and let $b$ minimize (1) at $r=R/\sqrt n$. All optimizers have the same $Jb$ and $P_\sigma b$ by strict convexity in these images. The envelope formula therefore gives $F_q'(R)=-\|P_\sigma b\|^2/(rR)$. More explicitly, one may sandwich the difference quotients with minimizers at the two nearby widths. Coercivity on the positive cone makes them bounded, and every subsequential limit minimizes at the original width. The single image gives the same limit for both bounds. Also, $A_\sigma(r)$ is positive concave as an infimum of affine energies, so its reciprocal $F_q$ is convex. It follows that

$$
\sqrt n\|P_\sigma b\|^2
=-R^2F_q'(R)
\le 2R\bigl(F_q(R/2)-F_q(R)\bigr).
\tag{8}
$$

At fixed $R$, whenever $a^2F_q(R)\le1$, the root term in (4) divided by $\sqrt n$ is $O_a(R^2/\sqrt n)$ by the KKT bound. For each fixed $0<a<1$, prescribed mean one, the two conditions

$$
\lim_{R\to\infty}\limsup_p F_p(R)\le1,\qquad
\lim_{R\to\infty} R\limsup_p \bigl(F_p(R/2)-F_p(R)\bigr)=0
\tag{9}
$$

thus give $\limsup_p d_p(a,1)/n^{1/4}=0$. If (9) holds on both signs, it proves Problem 26. In fact, for a positive ordinary theta optimizer $W$ with mark one and sum $S$, translation and rescaling show $W_i\le1$, so $\|W_{\rm off}\|_2\le\sqrt S$. Pairing $W$ with the pinned row on the opposite sector gives $a\sqrt n-S\le d_p(a,1)\sqrt S$. The elementary theta bounds give $S=O(\sqrt n)$, hence $\liminf_p S/\sqrt n\ge a$. Let $a\uparrow1$ on both signs and use endpoint reciprocity. The first part of (9) is the broad bound in (7). The second part strengthens it to a rate that controls the critical-size witnesses as well. Both estimates in (9) remain unproved through all primes.

## Square controls

At $q=t^2$, put $h=(t+1)/2$. The annihilator indicator $\mathbf1_I$ lies in $U_+$ and tests the first problem in (1), giving

$$
B_-(r)\ge \left(h^2/n+r(h-h^2/n)\right)^{-1}.
\tag{10}
$$

At $r=R/\sqrt n$ this lower bound tends to $(1/2+R/\sqrt2)^{-1}$. Thus even the one-sided objective exceeds one on square orders for fixed $R<1/\sqrt2$ in the limit. That narrow witness has bounded $m_{\mathrm{eff}}/m_0$.

One obtains a better lower bound at large $R$ by mixing $\mathbf1_I/h$ with the mass-one row $\pi_C=(\mathbf1+P_+e_0/\omega)/n$, where $\omega=(1+t)/(2n)$ is the Jacobi bound for the negative off-diagonal entries of $P_+$. The second row has $z\to1/\sqrt2$ and squared norm $O(1/n)$. With weight $u$ on the subfield row, $z\to(1+u)/\sqrt2$ and $\sqrt n(\|W\|_2^2-1/n)\to\sqrt2 u^2$ by Cauchy–Schwarz on the cross term. In (6), the resulting lower bound in the square field liminf is

$$
\max_{0\le u\le1}\frac{(1+u)^2}{2(1+\sqrt2 R u^2)}
=
\begin{cases}
(1/2+R/\sqrt2)^{-1},& R\le1/\sqrt2,\\
(1+1/(\sqrt2 R))/2,& R\ge1/\sqrt2.
\end{cases}
$$

This is a lower bound for the plus witness branch. Its broad limit in (7) remains undetermined.

For $0<r<1$, equality in (10) is equivalent to attainment of the [subfield lower bound for the pinned defect](anchored-repair-20.md#the-square-control) in $U_-$ at mean one and mark $h+(h-1)v$, where $v=rn/(h(1-r))$. Indeed, equality in (10) gives a reciprocal minimizer $b$ with $(J+r^{-1}P_+)b=B_-\mathbf1_I$ and $b=0$ on $I\setminus\{0\}$. Then

$$
Y=\frac{b-rB_-\mathbf1_I}{B_-h(1-r)/n}
$$

has mean one and lies in $U_-$. It equals $-v$ on $I\setminus\{0\}$ and is nonnegative outside $I$. Conversely, at the stated mark, attaining the subfield lower bound forces exactly that arrangement by equality in Cauchy–Schwarz. Set $b=(Y+v\mathbf1_I)/(h(1+v))$. This is nonnegative and anchored, and $Jb+r^{-1}P_+ b$ is $B_0\mathbf1_I$, with $B_0$ the right side of (10), since $r^{-1}vh=n+vh$. The KKT conditions hold, proving equality. At $q=389^2$, [two pinned interval certificates](square-pinned-22.md) give exact attainment at $a=0.98$ and at $a=1$. With convex interpolation they prove equality in (10) for the whole interval $0<R\le r_*\sqrt n$, where $r_*$ is the corresponding width at $a=1$ and $r_*\sqrt n>0.29226263069516$.

On the other sign there is an exact value for every $0<r\le1$. With $m_-=(t-1)/\sqrt n$, the [constant minus endpoint](square-endpoint-uniqueness.md#least-norms) gives

$$
B_+(r)=\left[m_-^2+2r(1-m_-/\sqrt n)^2\right]^{-1}.
\tag{11}
$$

Any feasible minus row of mark one has $m=\sum W/\sqrt n\ge m_-$. For fixed $m$, Cauchy–Schwarz at the root bounds its nonconstant energy below by $2(1-m/\sqrt n)^2$, since $\kappa_-=1/2$. The sum of this weighted cost and $m^2$ is increasing at $m\ge m_-$ for $r\le1$. The constant endpoint attains equality with deviation parallel to $P_-e_0$. Therefore the field-first broad mark on square minus is exactly $1/\sqrt2$ by (7).

## Replay

The [script](one-sided-quadratic-22.py) uses projected gradient with momentum for $B_{-\sigma}$. For the upper bound it rounds a nonnegative anchored trial in physical coordinates and evaluates its energy by Arb Fourier transforms. For the lower bound it projects a trial into the required sector, rounds real even Fourier coefficients, adds a rational constant to make the entire inverse transform nonnegative, and evaluates the reciprocal energy. The two certified bounds require only feasibility. It also certifies the mean condition and the projected norm bound in (4), using the exact rational scale $R$ and the positive algebraic width $R/\sqrt n$. Direct measurements of the defect of the iterate and its effective size are floating-point diagnostics.

The [main sweep](one-sided-quadratic-22-certified.jsonl) has 48 intervals over three prime and three square orders. The [million-order sweep](one-sided-quadratic-22-million-certified.jsonl) adds eight. Both signs at each prime order and all four scales meet the mean condition for $a=49/50$, $\mu=1$. The table rounds each enclosure outward. The sign column is the witness sector $\sigma$, so the listed value is $B_{-\sigma}$.

| Field order | $\sigma$ | $R$ | Interval for $B_{-\sigma}$ | Upper bound for $d_q(0.98,1)/n^{1/4}$ |
|---:|:---:|---:|:---|---:|
| $153649$ | $+$ | $1/4$ | $[0.97232716,0.99503070]$ | $0.03477978$ |
| $153649$ | $-$ | $1/4$ | $[0.97830985,0.99997206]$ | $0.03494348$ |
| $1000033$ | $+$ | $1/4$ | $[0.95931544,1.00073718]$ | $0.02197895$ |
| $1000033$ | $-$ | $1/4$ | $[0.95185672,0.99743555]$ | $0.02191729$ |
| $389^2$ | $+$ | $1/4$ | $[1.47199040,1.47199041]$ from (10) | — |
| $389^2$ | $+$ | $1$ | $[1.08652988,1.10923631]$ | $0.50224737$ |

At $389^2$, $R=1$, the rounded dual proves $B_->1/(0.98)^2$, which rules out using the total objective alone to ensure the mean reserve. The separately certified trial mean is below $0.969115$, so (4) still certifies this mark. At $R=1/4$ the same trial has mean above one and the projection certificate does not apply. For comparison, the [actual reciprocal row replay](astra-transport-22.md) finds that moving the square root to mark one can add a substantial defect on its zero set. On the common prime order $9413$, $R=1/4$, the one-sided interval upper bounds are $0.99087813$ and $0.98904766$. The ordinary reciprocal objectives at the same width are approximately $1.00098499$ and $0.99901598$, respectively, in the floating-point replay. These comparisons hold at the tested field orders.

The intervals can also separate the slopes in (8) with a wider secant. At $R=1$, $F_q(1/4)-F_q(1)$ is below $0.04103$ for both signs at $p=1000033$ and exceeds $0.36275$ for the plus witness at $389^2$, using the intervals above and the saved sweeps. The field-first rate in (9) remains unproved. An independent dense quadratic solve on both signs, three widths and four small fields checked the reciprocity identity 24 times. The maximum numerical product error was below $1.1\cdot10^{-12}$.

```sh
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python -B \
  research/one-sided-quadratic-22.py 9413 37633 153649 --square-roots 97 193 389 \
  --steps 384 --certify-max-order 153649
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python -B \
  research/one-sided-quadratic-22.py 1000033 --steps 256 --certify-max-order 1000033
```
