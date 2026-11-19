# Fourier repair at a fixed marked value

A positive correction can repair the off-mark coordinates of a Fourier row while preserving its marked value. This removes the marked completion cost in the [signed repair](threshold-repair-19.md). The same geometry gives a dual interpretation of the minimum squared off-mark violation. A stationary violation at an infeasible target yields a nonnegative witness in the opposite Fourier sector. The square plus obstruction appears directly in this dual, and a tail-scale defect bound on primes is enough to prove [ETH Problem 26](https://randomstrasse101.math.ethz.ch/posts/PaleyGraph/).

## Root-zero Fourier correction

Use the real Fourier sectors $U_{-\sigma}=\mathbb R\mathbf1+\operatorname{im}P$ and $U_\sigma=\ker P$, where $P=P_{-\sigma}$. Put $\ell=Pe_0$, $\kappa=P_{00}>0$, and let $\omega_J=(1+\sqrt q)/(2n)$ be the two-sided bound on $|P_{ij}|$ for $i\ne j$. Let

$$L=P-\ell\ell^\mathsf T/\kappa,\qquad M=\mathbf1-\ell/\kappa.$$

Here $L$ projects orthogonally onto $\operatorname{im}P\cap e_0^\perp$. The row $M$ has mean one, vanishes at the mark, belongs to $U_{-\sigma}$, and lies between $1-r$ and $1+r$ off the mark, where $r=\omega_J/\kappa$. Assume $r<1$. For every $i\ne0$, set

$$\eta=\frac{1-r}{\omega_J+\omega_J^2/\kappa},\qquad W^{(i)}=M+\eta L e_i.$$

These rows have mean one and mark zero. If $j\notin\{0,i\}$, $L_{ji}\ge -\omega_J-\omega_J^2/\kappa$, so $W^{(i)}_j\ge0$. At the receiving site their heights are

$$h_i=W^{(i)}_i=M_i(1+\eta(\kappa+\ell_i))\ge \kappa/\omega_J-1.$$

For the last inequality write $x=\ell_i/\kappa\in[-r,r]$. The height $1+\eta\kappa-x-\eta\kappa x^2$ is concave in $x$ and takes its smaller endpoint value at $x=r$. Thus each off-mark defect admits a nonnegative, marked-zero repair with height within two of the universal translated Jacobi height $1+\kappa/\omega_J$.

For an affine shadow $A$ of the desired mark and any floor $F$ off the mark, add

$$tM+\sum_{i\ne0}\frac{(F_i-A_i-tM_i)_+}{h_i}W^{(i)}.\tag{1}$$

The correction dominates $F-A$ off the mark for any $t\in\mathbb R$. If a constraint is also imposed at the mark, $A_0$ must satisfy it before the correction. Formula (1) uses one application of $L$ after setting the weights. Minimizing its mean gives

$$\min_{t\in\mathbb R}\left[t+\sum_{i\ne0}b_i(g_i-t)_+\right]
=\max_{0\le z_i\le b_i,\ \sum z_i=1}\sum_{i\ne0}z_i g_i,
\qquad g_i=\frac{F_i-A_i}{M_i},\quad b_i=\frac{M_i}{h_i}.\tag{2}$$

The capacities sum to at least one, since $h_i\le n$ by nonnegativity and $\sum_{i\ne0}M_i=n$. Sorting the $g_i$ and filling capacities gives a minimizer. In the Paley ranks, $M_i=1+O(n^{-1/2})$ and $b_i=O(n^{-1/2})$. Cauchy–Schwarz in (2) bounds the additional mean from above by $O(n^{-1/4})\|(F-A)_+\|_{2,\mathrm{off}}$.

## A minimum defect and its opposite witness

Write $a_s>0$ for the mark in scaled coordinates, $\mu>0$ for the mean, and suppose $a_s>\mu$. On the affine space $Y\in U_{-\sigma}$ with $Y_0=a_s$, $\overline Y=\mu$, let $E=(-Y)_+$ off the mark and $E_0=0$. The squared norm of $E$ attains its minimum. Indeed, the possible dominating nonnegative vectors with $E_0=0$ form the projection of a finite polyhedron onto its defect coordinates, a closed polyhedron. Norm minimization there gives the unique minimum defect, with exact negative part at attainment.

For any trial define

$$\gamma=-\ell^\mathsf T E/\kappa,\qquad W=E+\gamma e_0-LE\in U_\sigma.$$

Orthogonality of the nonconstant sectors gives $\langle Y,W\rangle=\mu(\sum_i E_i+\gamma)$. Also $\langle Y,E\rangle=-\|E\|_2^2$. Thus the exact trial identity is

$$\|E\|_2^2=\gamma a_s-\mu\big(\|E\|_1+\gamma\big)-\langle LE,Y\rangle.\tag{3}$$

At a minimum, differentiating the continuously differentiable half-squared violation in the range of $L$ gives $LE=0$. If $E\ne0$, (3) forces $\gamma>0$. Thus $W=E+\gamma e_0$ is nonnegative and gives a strict opposite witness to infeasibility of the target mean and mark. More generally if a trial has $\gamma>0$, (1) in the opposite sector makes its $W$ nonnegative without changing $\gamma$. The repaired $Y$ and $W$ give lower and upper bounds on the same normalized theta, by complementary pairing and exact theta reciprocity. This finite bound does not rely on declaring a small numerical $LE$ to be exactly zero.

In fact, writing $d(\mu)$ for the minimum defect norm,

$$d(\mu)=\sup_{W\in U_\sigma,\ W\ge0,\ W_0=1}\frac{(a_s-\mu\sum_i W_i)_+}{\|W_{\rm off}\|_2}.\tag{4}$$

For any such witness, pairing with $Y$ gives $a_s-\mu\sum W\le\langle E,W_{\rm off}\rangle$. For $d(\mu)>0$, the stationary witness from (3) divided by $\gamma$ attains equality. Every maximizing witness with positive numerator peaks at the mark. Moving a strictly higher entry to the mark would increase the numerator before renormalization and reduce the off-mark denominator. In particular the actual minimizing $E$ satisfies $E_i\le\gamma$.

Let $S_*\!=\min\sum_i W_i$ under the same opposite constraints and let $\mu_*=a_s/S_*$. Formula (4) shows $d(\mu)=0$ exactly at $\mu\ge\mu_*$. The finite-field left slope is

$$\lim_{\epsilon\downarrow0}\frac{d(\mu_*-\epsilon)}{\epsilon}
=\frac{S_*}{\min\{\|W_{\rm off}\|_2: W\ge0,\ W\in U_\sigma,\ W_0=1,\ \sum W=S_*\}}.\tag{5}$$

Testing the least-norm opposite optimum proves one direction. For the other, a positive maximizing witness at $\mu_*-\epsilon$ has sum between $S_*$ and $a_s/(\mu_*-\epsilon)$. Along every convergent subsequence of these bounded nonnegative rows the limit is an opposite optimum, while the numerator is at most $\epsilon\sum W$. This gives (5). The denominator is positive since $Pe_0\ne0$.

## A prime criterion and the square control

Starting from $X=\sqrt n H$ with mark $a_s=\sqrt n a$, use the explicit trial $Y=X+(\mu-c)M$ and update $Y\gets Y+\alpha LE$ with $0<\alpha<2$. Both mean and mark stay fixed. The exact signed descent and switching formulas in [Astra's analysis](astra-signed-20.md) apply with $P$ replaced by $L$. For $\mu=1$ the initial padding $(1-c)M$ is nonnegative, so the [reciprocal energy estimate](parallel-tail-18.md#1-separate-the-exceptional-entries-at-no-field-dependent-cost) bounds $\|E_0\|_2$ by $\sqrt{ns(1-c^2)}$. If any number of steps at fixed width $s$ produces $\|E\|_2\le\eta(s)n^{1/4}$ on both signs for all sufficiently large primes, then (2) and pairing bound both normalized endpoints below by $a/(1+O(\eta(s)))$. Sending $s\downarrow0$ and using $a\to1/(1+s)$ proves the conjecture if $\eta(s)\to0$. A uniform positive descent gap at each fixed width would suffice after $O_s(\log n)$ steps. The criterion also permits field-dependent depths or variable descent.

Conversely, if the conjecture holds then at every fixed $s>0$ the target $\mu=1$ is eventually strictly feasible on both signs, by theta reciprocity and $a\to1/(1+s)<1$. Thus the field-first small-defect criterion for the minimum (4) is equivalent to the conjecture. The numerical descent gives one way to obtain a small defect. Its uniform prime estimate remains open.

## A uniform single-step gap for concentrated prime defects

Let $m_0=n/\sqrt p$, fix $0<\tau<1$ and $\Delta>0$, and for a nonnegative off-mark violation $E\ne0$ put

$$m_{\rm eff}=\frac{\|E\|_1^2}{\|E\|_2^2},\qquad S=\{i:E_i\ge \tau\|E\|_2/\sqrt{m_0}\}.$$

Write $\mathcal E(S)=\sum_d |S\cap(S+d)|^2$. There exist $\xi,\epsilon>0$ such that for all sufficiently large primes, if $m_{\rm eff}\le(1+\xi)m_0$ and $\mathcal E(S)\ge(1/2+\Delta)|S|^3$, then $\|LE\|_2\ge\epsilon\|E\|_2$ on either sign. This uses the [nonalternating coset gap](parallel-rectangle-20.md), together with the earlier [overlap rigidity](parallel-cap-19.md#3-flat-rectangles-and-overlap-rigidity). The assumptions involve effective size and a high layer, so tiny nonzero entries need not be declared zero.

To prove it, let $\xi\to0$ along a contrary sequence, and normalize $e=E/\|E\|_2$. The removed rank-one term has norm $|\ell^\mathsf T e|/\sqrt\kappa\le\omega_J\|e\|_1/\sqrt\kappa=o(1)$ because $e_0=0$ and $m_{\rm eff}=O(m_0)$. Also $\|Je\|_2=\|e\|_1/\sqrt n=o(1)$. Hence $\|Le\|_2\to0$ implies $\sigma Ke=e+o_{\ell_2}(1)$ from $2P=I-J-\sigma K$. The entry cap implies $1-o(1)\le e^\mathsf T\sigma K e\le \|e\|_1^2/m_0$, so $m_{\rm eff}\sim m_0$.

Set $b=m_0^{-1/2}$. The pointwise cap $\sigma Ke\le \|e\|_1/m_0=(1+o(1))b$ gives $\|(e-b)_+\|_2=o(1)$ on the set $e>b$: the uniform $o(b)$ error there has norm $o(1)$ as this set has at most $m_0$ sites. Also $\sum_i e_i(b-e_i)=b\|e\|_1-1=o(1)$. It follows that $\sum_i e_i(b-e_i)_+=o(1)$ by Cauchy–Schwarz on the excess above $b$. On $S^c$ this bounds $b\sum_{S^c}e_i$ by $o(1)/(1-\tau)$, so $\|e_{S^c}\|_2=o(1)$. On $S$ it bounds $\sum_{S}(b-e_i)_+^2$ by $o(1)/\tau$. Thus $e=b\mathbf1_S+o_{\ell_2}(1)$ and $|S|\sim m_0$. The Rayleigh quotient gives the $o(1)$ signed deficit for $S\times S$. The assumed energy makes $S$ close to a union of boundedly many cosets of one subgroup, which the nonalternating prime gap excludes. This proves the uniform assertion by contradiction.

For a fixed $0<\alpha<2$, signed projected descent consequently contracts the defect norm in one step by a uniform factor at most $\sqrt{1-\alpha(2-\alpha)\epsilon^2}$ whenever the two hypotheses hold. The proof concerns slow signed descent, for which convergence of the Rayleigh quotient produces a within-set rectangle directly. For $m_{\rm eff}\le(1-\delta)m_0$ a simpler bound $\|Le\|_2^2\ge\delta/2-O(p^{-1/2})$ follows directly from the same cap and rank-one bound.

At the other extreme, let $\mu=1$ and fix a target $a_s/\sqrt n\le1-\delta$ for some $\delta>0$. Any nonzero minimum defect gives an exact opposite witness $W$ normalized to $W_0=1$ with $\sum W<a_s$. Its regularized quadratic trial bounds $M_\sigma(r)$ above by $(1-\delta)^2+r\|W\|_2^2$. The [slow-width result](parallel-complexity-14.md) therefore forces $\|W_{\rm off}\|_2^2\gtrsim_\delta\log_2^*q$ along such a sequence. If the ratio to $\log_2^*q$ tended to zero on a subsequence, one could choose $r$ with $r\log_2^*q\to\infty$ and $r\|W\|_2^2\to0$, contrary to $M_\sigma(r)\to1$. Thus the stationary defect must have $m_{\rm eff}=(\sum W-1)^2/\|W_{\rm off}\|_2^2=O_\delta(n/\log_2^*q)$. The remaining regimes include critical support without the high-energy hypothesis and effective supports between the critical scale and this coarse upper bound.

## The square control

On square plus, the subfield annihilator $I$ has size $h=(\sqrt q+1)/2$, and every $Y$ in the prescribed sector has sum $h\mu$ on $I$. Consequently

$$d(\mu)\ge\frac{(a_s-h\mu)_+}{\sqrt{h-1}}.\tag{6}$$

This is order $n^{1/4}$ at $\mu=1$ and small fixed $s$. At every square covered by [subfield uniqueness](square-endpoint-uniqueness.md), (6) is exact on a finite interval immediately below $\mu_*=a_s/h$. There exists an optimum $Y^*$ positive off $I$. Otherwise, at an exterior coordinate forced to be zero for all optima, separate the impossible short perturbation in $\operatorname{im}L$ that is nonnegative on the zero set and strictly positive there. The resulting nonnegative vector $v$ in $\ker L$ is supported on the zero set and positive at that exterior coordinate. Pairing with $Y^*$ and completing its anchor as in (3) gives an opposite optimum positive there, contradicting uniqueness of $\mathbf1_I$. Averaging the finitely many optima obtained by making each exterior coordinate positive gives $Y^*$. Now $Y=Y^*+(\mu-\mu_*)M$ remains positive off $I$ for sufficiently small decrement. On $I\setminus\{0\}$ the padding equals $h/(h-1)$, so its defect attains (6) with $E$ proportional to $\mathbf1_{I\setminus\{0\}}$. Here the completed stationary dual is proportional to $\mathbf1_I$.

The [square interval replay](anchored-repair-20-square.py) certifies equality in (6) at $q=389^2$, $\mu=1$, for the actual reference marks at both $s=1/16$ and $s=1/64$. Let $C$ project onto the vectors supported on $I\setminus\{0\}$ with sum zero. The square submatrix of $L$ there acts as $\kappa+\omega$ on these vectors, where $\omega=\kappa/(h-1)$. Thus $Y\mapsto Y-LCY/(\kappa+\omega)$ makes the unmarked subfield entries constant while preserving the mark and mean. To get positive exterior slack, the numerical replay adds a correction in $\operatorname{im}L$ using only exterior violations of a small positive floor. It projects out the subfield shape at every step. The certificate then rounds the accumulated direction, projects it exactly in the Fourier sector, and encloses the exterior of the resulting flattened row with interval arithmetic. If the reference $\ell_2$ error is $e$, the error after scaling, mean padding, and flattening is at most $(1+1/(\kappa+\omega))(\sqrt n+\sqrt{n+1/\kappa})e$. The [two interval records](anchored-repair-20-square-certified.jsonl) bound exterior slack below by $0.00399$. They give minimum defect norms near $4.54520$ and $5.19093$ respectively, with the exact formula (6) in both cases.

## Replay

The [replay](anchored-repair-20.py) runs the fixed-mark gradient iteration starting at the actual reciprocal reference. It tests mean one and a deliberately smaller mean $0.94a$ giving target ratio $1/0.94$. It samples four depths and uses (1) in both sectors. For the selected primal correction, exact integer Fourier coefficients sum to zero by construction. An interval Fourier transform and a rational multiple of $M$ repair the remaining bulk uncertainty, so the final marked value is exactly the actual $H_0$. The dual bounds use the independently rounded interval Fourier spectra from the ordinary theta replay.

The [fixed-width sweep](anchored-repair-20-certified.jsonl) has 144 numerical rows and 35 interval bounds. The [narrower-width sweep](anchored-repair-20-narrow-certified.jsonl) has 112 rows and 28 interval bounds. At width $1/64$ and target mean one, the plus-square $389^2$ defect divided by $n^{1/4}$ stays near $0.3130$, with effective size near $m_0$. The same normalized defect at $p=1000033$ falls from about $0.0729$ to below $0.000062$ by step 16, on both signs, while its effective size exceeds $60m_0$ at that step. These are numerical trajectories. The concentrated-defect gap proved above accounts for the square-shaped obstruction on primes and does not control the broad prime trajectory.

The [near-one scan](anchored-repair-20-near-certified.jsonl) picks the best repair over target ratios $0.996,1,1.005$ after at most 256 steps and has 12 interval bounds among 72 rows. On the conjecture side at $p=1000033$, width $1/64$, the certified lower bound is $0.99742075$ after rounding downward. The complementary sign certifies a lower bound above $0.99577448$, which gives a reciprocal upper bound below $1.004244$ on the conjecture side. Earlier directly rounded witnesses give a tighter bound on this particular prime. This comparison tests the fixed-mark construction and interval correction.

Separately, 42 dense linear programs checked the weighted-tail formula, and 14 infeasible affine examples checked the stationary identity and the maximum-at-the-mark property.

```sh
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python -B \
  research/anchored-repair-20.py --depth 64 --certify-max-order 1000033
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python -B \
  research/anchored-repair-20.py --width .015625 --primes 9413 37253 153649 1000033 \
  --square-roots 97 193 389 --depth 64 --certify-max-order 1000033
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python -B \
  research/anchored-repair-20.py --primes 153649 1000033 --square-roots 389 \
  --width .015625 --target-ratios .996 1.0 1.005 --depth 256 --certify-max-order 1000033
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python -B \
  research/anchored-repair-20-square.py
```
