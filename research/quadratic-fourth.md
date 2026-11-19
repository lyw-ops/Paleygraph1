# One moving width and quantitative fourth-moment certificates

For [Problem 26](https://randomstrasse101.math.ethz.ch/posts/PaleyGraph/), a bounded allowed-sector energy at one moving width on the larger-theta side would suffice by the [fixed positive width limit](parallel-fixed-width-13.md). This criterion uses the actual reciprocal optimizer. At a sampled width the allowed energy, fourth moment, and signed derivative can all be enclosed using two rational positive trial vectors. Approximate complementarity alone leaves room for an arbitrarily large scaled fourth moment.

## A one-sided, single-width criterion

Fix a field, a sign $\sigma$, and $n=|Q|$. Let $b_r$ be the anchored optimum of the [reciprocal quadratic problem](quadratic-theta.md), with $M(r)=b_r^TQ_\sigma(r)b_r$, and write $x_r=b_r/\sqrt{M(r)}$ for the normalized optimizer. Define

$$A_\sigma(r)=\|P_\sigma x_r\|^2,\qquad
  \Gamma_\sigma(r)=\frac1n\sum_{s(t)=\sigma}|\widehat x_r(t)|^4,$$

where the Fourier transform is unnormalized. Parseval and Cauchy–Schwarz give

$$A_\sigma(r)\le\sqrt{\frac{|D_\sigma|}{n}\Gamma_\sigma(r)}.$$

For any $0<r\le s\le1$ and $M(0)$ on the same sign,

$$\boxed{\displaystyle
\sqrt{M(0)}\ge
\frac{\sqrt{M(s)}}{\sqrt{1+(s-r)A_\sigma(r)}}-
r n^{1/4} M(0)^{1/4}\sqrt{A_\sigma(r)}.} \tag{1}$$

Indeed, testing $b_r$ at $s$ gives $M(s)\le M(r)[1+(s-r)A_\sigma(r)]$ because the forbidden-sector coefficient decreases. For the other term, let $b_0$ be an anchored ordinary-theta optimizer, so $Jb_0=\sqrt{M(0)}j$, $P_{-\sigma}b_0=0$ and $0\le b_{0,i}\le1$. The normal equations at $r$ give $Q_\sigma(r)b_r\ge0$ and $(Q_\sigma(r)b_r)_0=M(r)$. Therefore

$$
M(r)\le\langle b_0,Q_\sigma(r)b_r\rangle
\le\sqrt{M(0) M(r)} + r n^{1/4}M(0)^{1/4}\sqrt{M(r)A_\sigma(r)} .
$$

The last inequality uses $\|b_0\|^2\le\sqrt{nM(0)}$. Divide by $\sqrt{M(r)}$ and combine the two comparisons. This is a one-sided use of the [zero-width secant estimate](parallel-quadratic-limit-9.md#exactly-which-theta-witnesses-the-path-selects), followed by a trial in the direction of *increasing* width.

For every prime select the larger ordinary theta sign, so that $M(0)\le1$. Suppose there are widths $r_p=o(n^{-1/4})$ at which $A_\sigma(r_p)$ is uniformly bounded on this chosen side. Applying (1) and the fixed-width limit with the field limit taken before $s\downarrow0$ gives $M(0)\to1$. The same follows from bounded $\Gamma_\sigma(r_p)$ at that single width. In particular one may use a fixed $r_p\sqrt p=\kappa>0$, or a wider $r_p=p^{-1/3}$. The criterion uses neither a terminal support interval nor simultaneous bounds across a range of widths. If $A_\sigma(r_p)$ grows, two widths $r_p\le s_p$ still suffice when $M(s_p)\to1$, $(s_p-r_p)A_\sigma(r_p)\to0$, and $r_p n^{1/4}\sqrt{A_\sigma(r_p)}\to0$. The [slow-width theorem](slow-width.md) gives a concrete choice of $s_p$ for this variant.

## Enclosures from two anchored trials

Take any nonnegative anchored trials $u_+,u_-$ with root one. Write $e_\pm=\|u_\pm\|_{Q_\pm(r)}^2$ and $\Delta=\sqrt{e_+e_--1}$. This is real by reciprocal duality. The actual marker $a_\sigma=(x_r)_0$ is between $1/\sqrt{e_\sigma}$ and $\sqrt{e_{-\sigma}}$. Comparing $a_\sigma u_\sigma$ to the optimum $x_r$ at the same root and expanding the quadratic form gives

$$\|a_\sigma u_\sigma-x_r\|_{Q_\sigma(r)}^2
\le a_\sigma^2e_\sigma-1\le\Delta^2. \tag{2}$$

The cross term in the expansion is nonnegative by the optimum's nonnegative complementary vector. Allowed-sector projection and the triangle inequality give

$$
\left|\sqrt{rA_\sigma(r)} - a_\sigma\sqrt r\|P_\sigma u_\sigma\|\right|\le\Delta,\qquad
\left|\Gamma_\sigma(r)^{1/4}
-a_\sigma\left(\frac1n\sum_{s(t)=\sigma}|\widehat u_\sigma(t)|^4\right)^{1/4}\right|
\le \frac{n^{1/4}}{\sqrt r}\Delta. \tag{3}
$$

The fourth-power estimate uses $\|v\|_4\le\|v\|_2$ in the unitary positional Fourier coordinates. For a two-sided band substitute the lower and upper bounds on $a_\sigma$, truncating a negative lower norm bound at zero. Subtract the two intervals for $rA_\sigma(r)$ to enclose the [signed derivative](astra-convolution-11.md#2-cross-convolution-is-an-exact-energy-measure)

$$g(r)=\frac{d\log M_+(r)}{d\log r}=r(A_+(r)-A_-(r)).$$

These bounds do not rely on the trial iteration reaching its requested tolerance, the residual being certified, or the proposed and actual supports agreeing. To certify an entire compact width interval with one trial pair, note that each $e_\sigma(r)$ and their product are Laurent polynomials with nonnegative coefficients. Each is convex as a function of $\log r$, so its maximum is bounded by the larger endpoint value. Use the smallest width in the interval in the denominator of the fourth error in (3) and use the maximum opposite energy for the root multiplier. This gives an interval upper moment bound, with no assumption about support changes.

For an approximate signed fixed point of residual norm $\varepsilon$, let $E_+,E_-$ be the energies of its pointwise-complementary trials before division by their marks. The [quadratic residual identity](quadratic-theta.md#damped-fixed-point-and-an-exact-residual-bracket) gives $E_++E_-=2+(1+r)^2\varepsilon^2/(4r)$. Also $e_+e_-=E_+E_-$ since the trial marks multiply to one. Thus $\Delta=O(\varepsilon/\sqrt r)$ when $\varepsilon\le\sqrt r$. The trial marks are then bounded above and away from zero by the reciprocal bracket and the uniform bounds on $M(r)$. A bounded allowed trial energy in complementary normalization and residual $O(r)$ suffice for the actual allowed-energy bound. For a bounded scaled fourth moment the corresponding sufficient residual is $O(r n^{-1/4})$.

## A prime obstruction to using approximate complementarity

Let $x,y=Q_+(r)x$ be the true normalized pair at any $0<r\le1$, and suppose $D_+$ contains a nonidentity $t$. In frequency coordinates take the nonnegative spectrum

$$v_i=n^{-1/2}(1+\epsilon\operatorname{Re}\eta_i(t)),\qquad \epsilon\in\{-1,1\}.$$

Its nonconstant part lies in $V_+$ because $s(t)=s(t^{-1})=+1$. Thus $Q_+(r)v=j+r(v-j)$ is also nonnegative. With $0<\delta\le1$, set

$$x'=\lambda(x+\delta v),\quad y'=\lambda(y+\delta Q_+(r)v),\quad
\lambda=\|x+\delta v\|_{Q_+(r)}^{-1}.$$

They have exact reciprocal sector relations, nonnegativity, and $\langle x',y'\rangle=1$. Since $\|v\|_{Q_+(r)}\le\sqrt2$ and $\langle y,v\rangle\ge0$, we have $(1+\sqrt2\delta)^{-1}\le\lambda\le1$. The product of the marks is at least $\lambda^2 x_0y_0=\lambda^2$, so the total off-mark overlap is $O(\delta)$. Choose the sign of the cosine so its Fourier coefficient at $t$ adds with the real part of $\widehat x(t)$. Then $|\widehat{x'}(t)|\ge\lambda\delta\sqrt n/2$, giving $\Gamma_+(x')\ge\lambda^4\delta^4 n/16$.

In particular $\delta=n^{-1/8}$ makes the overlap tend to zero and the scaled fourth moment diverge. This applies over the actual prime Paley signs at all orders with $D_+\ne\varnothing$. The same construction works with the minus sector. The example tests an approach based on positivity, Fourier-sector equations, and a qualitative complementarity error. The perturbed pair need not optimize the rooted problem.

### Unbounded allowed energy with vanishing residual

The Fejér construction gives a stronger version for the energy in (1). For either sign and all sufficiently large primes $p\equiv1\pmod4$ let $m=\lfloor(\log_2 p)/4\rfloor$. There is a square $t$ of order greater than $2m$ with $s(t^j)=\sigma$ for $1\le j\le m$. Indeed, expand the indicator of $\chi(t)=1$ and $\chi(1-t^j)=\sigma$ for all these $j$, excluding zeros. In any nonempty product involving one of the $1-t^j$ factors, a primitive root of unity for the largest selected exponent is a simple root of that factor and absent from the others. The possible factor $t$ does not change its multiplicity. Thus every nontrivial product is nonsquare. The quadratic Weil bound, with degree at most $1+m(m+1)/2$, gives $p/2^{m+1}+O(m^2\sqrt p)$ candidates. At most $O(m^2)$ elements have order at most $2m$. [Weil, On Some Exponential Sums](https://pmc.ncbi.nlm.nih.gov/articles/PMC1079093/)

Take the nonnegative Fejér vector

$$ v_i=\frac{1}{\sqrt n(m+1)}
\left|\sum_{j=0}^m \eta_i(t)^j\right|^2 .$$

It has $Jv=j$, lies in $U_\sigma$, and has allowed energy $2\sum_{j=1}^m(1-j/(m+1))^2\asymp m$. Its translated even averages $v^{(u)}=(T_u v+T_{-u}v)/2$ keep these support and positivity properties and satisfy $\|v^{(u)}\|_{Q_\sigma(r)}^2\le 1+O(rm)$. Averaging over $u$ kills the nonconstant cross term with $P_\sigma x$. It keeps half of the allowed energy of $v$, since each nonzero Fourier coefficient is multiplied by a cosine with mean square $1/2$. The order condition ensures none of the selected modes is self-inverse. Therefore some $u$ satisfies

$$\|P_\sigma(x+\delta v^{(u)})\|^2\ge
  \|P_\sigma x\|^2+\frac{\delta^2}2\|P_\sigma v\|^2.$$

At any width with $rm\le1$, take $\delta=m^{-1/4}$ and normalize the pair with $v^{(u)}$ as above, using the chosen side in place of plus. This gives even, nonnegative reciprocal pairs with inner product one, off-mark overlap $O(m^{-1/4})$, and allowed energy $\gg\sqrt m$. In particular it applies at the moving widths of (1). For the difference $z'=x'-y'$, the residual in the damped fixed-point equation is $O(m^{-1/8})$. To see this, the exact reciprocal relation yields $z'=d\sigma K(x'+y')$. On the bulk, the squared difference between $x'+y'$ and $|z'|$ is $4\min(x_i',y_i')^2\le4x_i'y_i'$. At the mark the same difference with $\sqrt{(z'_0)^2+4}$ has square at most $4(1-x'_0y'_0)$. Thus $\|z'-d\sigma K\Phi(z')\|$ is bounded by a constant times the square root of the off-mark overlap. This constructs a qualitative-residual obstruction for the weaker energy test as well as for the fourth moment. Quantitative control such as (2)–(3) continues to distinguish the actual optimizers.

## Certified field comparisons

The [Arb replay](../quadratic_fourth.py) evaluates (2)–(3) with positive rounded trials and a binary-rational width. The [72 certified rows](../data/quadratic-fourth.csv) cover six primes and six prime squares. Independent dense nonnegative least-squares solves cross-checked the fourth and derivative intervals at $13,49,97,401$ at two widths each. The exact $p=5$, $r=1/4$ case gives $(\Gamma_+,\Gamma_-,g)=(0,32/25,-1/5)$.

The following intervals are rounded outward at $r\sqrt q=1/4$. The final column is a simultaneous upper bound for each of $A_+(r),A_-(r)$.

| Field order | $\Gamma_+(r)+\Gamma_-(r)$ | $\max\{A_+(r),A_-(r)\}$ upper bound |
|---:|---:|---:|
| 401 | [44.23, 44.24] | 2.34 |
| 9413 | [64.23, 64.24] | 2.78 |
| 37253 | [61.63, 61.64] | 2.79 |
| 153649 | [62.47, 64.77] | 2.82 |
| $97^2$ | [285514, 285515] | 75.94 |
| $389^2$ | [$1.550\cdot10^7$, $2.245\cdot10^7$] | 316.03 |

At $q=389^2$ the plus allowed energy also exceeds 204, since $\Gamma_+/n\le A_+$ follows from $|\widehat x(t)|\le\sum_i x_i\le\sqrt n$. Across all 36 certified prime rows the two allowed energies are below 2.82 and their summed scaled fourth moment is below 65. These are finite bounds. The uniform assertion required by (1) is open.
