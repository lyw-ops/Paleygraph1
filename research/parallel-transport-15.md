# One-sided transport by repairing the attenuated dual

For [Randomstrasse101 Problem 26](https://randomstrasse101.math.ethz.ch/posts/PaleyGraph/), reusing the optimizer at width $s$ in the [single-trial split](quadratic-gap.md#transporting-a-trial-between-two-widths) incurs an energy gap of at least order $s^2/r$ as $q\to\infty$, $s\to0$ and $s/r\to\infty$. The same gap applies to every split of that trial. A second certificate attenuates the expensive component of the dual before repairing its nonnegativity. It uses the chosen-side projection, the bulk positivity defect, and a scalar upper value at $r$. The same repair gives a direct endpoint bound. An annihilator of the square subfield forces an order-one repair cost at $r=q^{-1/3}$.

## Frozen trials at long ratios

Use the [reciprocal normalization](quadratic-theta.md#a-reciprocal-pair-of-nonnegative-quadratic-programs). Fix the sign $\sigma$, let $b_r$ be its nonnegative anchored minimizer, and abbreviate $M_\sigma(r)$ to $M_r$. Write $j=\mathbf1/\sqrt n$ and $x=A_\sigma(s)$, $y=A_{-\sigma}(s)$. With $c=\langle j,y\rangle$, $u=P_\sigma x$, and $v=P_{-\sigma}y$, one has

$$
x=cj+u+sv,\qquad y=cj+su+v,\qquad
c^2+s(\|u\|^2+\|v\|^2)=1,\qquad y_0=\sqrt{M_s}.
\tag{1}
$$

For every anchored nonnegative trial $b$ at $r$, optimality at $b_r$ gives $b^TQ_\sigma(r)b-M_r\ge\|b-b_r\|_{Q_\sigma(r)}^2$. Using $\|P_{-\sigma}b_r\|\le\sqrt{rM_r}$, this gives a norm bound for any $U\ge M_r$,

$$
b^TQ_\sigma(r)b-M_r\ge
\left(\frac{\|P_{-\sigma}b\|}{\sqrt r}-\sqrt U\right)_+^2 .
\tag{2a}
$$

The forbidden **mark** of the target has the stronger scale $r$. Put $\kappa_\epsilon=(P_\epsilon)_{00}=|D_\epsilon|/n$. Since $(Q_\sigma(r)b_r)_0=M_r$, expanding its constant and allowed components gives

$$
(P_{-\sigma}b_r)_0=r\big(M_r-(Jb_r)_0-r(P_\sigma b_r)_0\big)
\le r\big(U+\sqrt{r\kappa_\sigma U}\big).
$$

Here $Jb_r\ge0$ and $|(P_\sigma b_r)_0|\le\sqrt{\kappa_\sigma}\,\|P_\sigma b_r\|$. If $\kappa_{-\sigma}>0$, apply the same mark inequality in the forbidden sector to $b-b_r$ to obtain

$$
\boxed{\displaystyle
b^TQ_\sigma(r)b-M_r\ge
\frac{\big[(P_{-\sigma}b)_0-r(U+\sqrt{r\kappa_\sigma U})\big]_+^2}{r\kappa_{-\sigma}} .}
\tag{2b}
$$

Both $M_s$ and $M_r$ lie in a universal compact subset of $(0,\infty)$, by the anchored Jacobi trial in (4) below and reciprocity. By (1), $v_0=y_0-c/\sqrt n-su_0\ge\sqrt{M_s}-1/\sqrt n-\sqrt s$. Thus $(P_{-\sigma}b_s)_0=s\sqrt{M_s}v_0\gtrsim s$ for large $q$ and small $s$, on both signs and over both primes and squares. Taking a bounded target upper value $U$, (2b) yields a gap $\gtrsim s^2/r$ whenever $s/r\to\infty$. The [exact split identity](quadratic-gap.md#a-capped-gradient-split) identifies twice the minimum split cost with this actual gap. In particular the minimum cost divided by $r$ grows at least as $(s/r)^2$, including when $s^2/r\to0$. This excludes a cost $O(r\log_2^*q)$ from the frozen trial at $r=q^{-1/3}$ and a round-14 reference width $s\to0$ with $s\log_2^*q\to\infty$.

There is also a bound for the convex interpolants $b=\lambda b_s+\mu\mathbf1+\nu e_0$, with $\lambda+\mu+\nu=1$ and all coefficients nonnegative. If $\mu\ge1/2$, the constant energy is at least $n/4$. Otherwise $(P_{-\sigma}b)_0\ge C s(\lambda+\nu)\ge Cs/2$, since $(P_{-\sigma}b_s)_0\gtrsim s$ as above and $(P_{-\sigma}e_0)_0\to1/2$. By (2b), their gaps are $\gtrsim\min(n,s^2/r)$ in the same regime. These mixtures supply no bounded target upper value at $r=q^{-1/3}$ and the slow reference widths above.

## Deflate the expensive part of the dual

For $0\le\rho\le s$ put $H_\rho=y-(s-\rho)u=cj+\rho u+v$. The expensive dual projection is now $P_\sigma H_\rho=\rho u$. For positive $r\le s$ the dual metric satisfies the exact identity

$$
\|H_\rho\|_{Q_{-\sigma}(r)}^2
=c^2+\frac r s(1-c^2)+\left(\frac{\rho^2}{r}-r\right)\|u\|^2.
\tag{3}
$$

The choice $\rho=r$ costs at most one before positivity repair, across arbitrarily long ratios. The choice $\rho=0$ also works for $r=0$ with metric interpreted as $|\langle j,\cdot\rangle|$ on $\mathbb Rj+V_{-\sigma}$. Formula (3) holds for an arbitrary nonnegative reference dual trial $y$ if $u=P_\sigma y/s$ and $1$ is replaced by $\|y\|_{Q_{-\sigma}(s)}^2$.

For an explicit repair, use the [translated Jacobi witness](iterate-majorants.md#repair-with-translated-witnesses) in sector $\epsilon=-\sigma$. Its anchor-one form is

$$
R_\epsilon(i)=\frac{1+\dfrac{2}{\sqrt q+1}\sum_{t\in D_\epsilon}\eta_i(t)}{h_\epsilon},\qquad
h_\epsilon=1+\frac{2|D_\epsilon|}{\sqrt q+1}.
\tag{4}
$$

Here $D_\epsilon$ is the allowed set of nonidentity positions and $\eta_i$ are the frequency characters. Inversion symmetry makes $R_\epsilon$ real and the Jacobi entry bound gives $R_\epsilon\ge0$. Its constant norm is $\sqrt n/h_\epsilon$, and its allowed squared norm is $4n|D_\epsilon|/[(\sqrt q+1)^2h_\epsilon^2]$. Both are $O(1)$, including for the opposite sign. This proves the uniform value bound used in (2).

Measure the **actual** negative part $d_i=(-H_{\rho,i})_+$. For any $t\ge0$ set

$$
p=t\mathbf1+R_{-\sigma}*(d-t)_+,\quad Y=H_\rho+p,\quad
\delta_{r,\rho}(t)=\sqrt n\,t+\|R_{-\sigma}\|_{Q_{-\sigma}(r)}\sum_i(d_i-t)_+ .
\tag{5}
$$

Convolution is the unnormalized sum over frequency translations. Since $R_{-\sigma}\ge0$ and $R_{-\sigma}(0)=1$, the correction satisfies $p_i\ge d_i$. It lies in $\mathbb Rj+V_{-\sigma}$ and $Y\ge0$ with $P_\sigma Y=\rho u$. Translation invariance and the triangle inequality give $\|p\|_{Q_{-\sigma}(r)}\le\delta_{r,\rho}(t)$. The minimum over $t$ is the top-defect sum with fractional cutoff at $\sqrt n/\|R_{-\sigma}\|_{Q_{-\sigma}(r)}$, multiplied by the kernel norm. This follows by differentiating between consecutive defect values. The cap is of order $\sqrt n$ for every $r\le1$. The defect incorporates the slack already present in $y$.

### A chosen-side energy bound at the target

Suppose $Y_0>0$, and put $N=\|Y\|_{Q_{-\sigma}(r)}$, $\ell=Y_0^2/N^2$. For any $U\ge M_r$,

$$
\boxed{\displaystyle
\ell\le M_r,\qquad
\sqrt{E_\sigma(r)}
\le \frac{\rho}{r}\frac{\|u\|}{N}
  +\sqrt{\frac{1-\ell/U}{r}} .}
\tag{6}
$$

Here $E_\sigma(r)=\|P_\sigma b_r\|^2/M_r$ is the [one-sided energy](quadratic-fourth.md#a-one-sided-single-width-criterion). To prove (6), set $\lambda=Y_0/N^2$. Nonnegativity gives $\langle b_r,Y\rangle\ge Y_0$. Completion of the square yields

$$
\|b_r-\lambda Q_{-\sigma}(r)Y\|_{Q_\sigma(r)}^2
\le M_r-\ell .
$$

Project onto $V_\sigma$, using $P_\sigma Q_{-\sigma}(r)Y=(\rho/r)u$, and divide by $\sqrt{M_r}$. The first coefficient $\lambda/\sqrt{M_r}$ is at most $1/N$. The squared relative gap $1-\ell/M_r$ is at most $1-\ell/U$.

The entire certificate can use scalar lower bounds for $\ell$. For example $\ell\ge (H_{\rho,0})_+^2/(\|H_\rho\|_{Q_{-\sigma}(r)}+\delta_{r,\rho}(t))^2$, and $1/N\le\sqrt U/Y_0$. Taking $\rho=r$ removes the width-ratio multiplier on the chosen norm. The opposite reference energy is absent from (3)–(6), with the defect and the upper value $U$ as separate inputs. At $r=q^{-1/3}$, $\|u\|^2=o(\log_2^*q)$ and a relative gap $1-\ell/U=o(r\log_2^*q)$ would give the [round-14 energy condition](parallel-complexity-14.md#4-consequence-at-the-intermediate-width) if $N$ stays bounded below. Equation (2b) prevents using the frozen trial at $s$ for this upper value at the slow reference widths.

### A direct endpoint comparison

Let $b_0$ be the anchored endpoint optimum of sign $\sigma$ and $m_0=\sqrt{M_\sigma(0)}$. Then $0\le b_0\le1$, $\|b_0\|^2\le\sqrt n m_0$, and $\langle b_0,Y\rangle=m_0\langle j,Y\rangle+\rho\langle b_0,u\rangle$. In particular

$$
m_0\langle j,Y\rangle
\ge Y_0-\rho n^{1/4}\sqrt{m_0}\,\|u\| .
\tag{7}
$$

This also works at $\rho=0$. At that endpoint the ratio $Y_0/\langle j,Y\rangle$ is the certified lower bound on $m_0$, and any $t$ gives a bound from (5) with denominator at most $c+\delta_{0,0}(t)$. For the sign chosen by $M_\sigma(0)\le1$, take $r=q^{-1/3}$, $s\to0$ with $s\log_2^*q\to\infty$, and $\rho\le r$. By (1) and the [round-14 marked bound](parallel-complexity-14.md), $H_{\rho,0}=1+o(1)$ and $\rho n^{1/4}\|u\|\le r n^{1/4}/\sqrt s=o(1)$. Consequently a repair with $\langle j,p\rangle=o(1)$ would imply $M_\sigma(0)\to1$ directly. This criterion does not require solving the program at the smaller width.

### A direct certificate from the ordered bulk defect

At $\rho=0$, the raw vector $H_0$ already lies in the opposite Fourier space and has mean coordinate $c$. Write $d_i=(-H_{0,i})_+$ off the mark. For any real $k\in[0,n-1]$ let $T_k(d)$ be the sum of the $\lfloor k\rfloor$ largest bulk defects plus the fractional part of $k$ times the next one. The actual endpoint trial $b_0$ has bulk mass $m_0\sqrt n-1$ and every entry is at most one. Opposite Fourier support gives

$$
H_{0,0}=c m_0-\sum_{i\ne0} H_{0,i}b_{0,i}
\le c m_0+T_{m_0\sqrt n-1}(d).\tag{7a}
$$

The right side is nondecreasing in $m_0$. Independently, for any threshold $t\ge0$, the inequality $T_k(d)\le kt+\sum_{i\ne0}(d_i-t)_+$ yields the explicit bound

$$
m_0\ge\frac{H_{0,0}+t-\sum_{i\ne0}(d_i-t)_+}{c+\sqrt n\,t}.\tag{7b}
$$

This uses only exact Fourier support of the raw vector and the coordinate cap on the endpoint optimizer. No positive correction enters its evaluation. An approximate normalized reciprocal pair can be replaced by an arbitrary reference trial projected into the opposite sector for a rigorous replay.

For the actual pair, $u=[x-sy-(1-s)cj]/(1-s^2)$. Complementarity therefore gives the bulk defect explicitly for all $0\le\rho\le s$:

$$(-H_{\rho,i})_+=\frac{s-\rho}{1-s^2}\left(x_i-\frac{(1-s)c}{\sqrt n}\right)_+,\qquad i\ne0.\tag{7c}$$

Indeed at each bulk coordinate either $x_i=0$, when $H_{\rho,i}\ge0$, or $y_i=0$, when the displayed expression follows by substitution. For the larger-theta sign, $m_0\le1$ and (7a) allows the full deficit in the reference mass. For $s\to0$ with $s\log_2^*q\to\infty$, it suffices to show $T_{\sqrt n-1}(d)\le1-c+o(1)$, because $H_{0,0}=1+o(1)$ and $c$ is bounded below by the [two-row estimate](astra-cuts-15.md#1-a-common-mass-floor-from-the-two-signed-jacobi-rows). The same argument works with the field limit at each fixed $s$, followed by $s\downarrow0$. This targets the largest defects on a set of order $\sqrt n$ in the actual reference spectrum. As floating-point checks at $s=q^{-1/6}$, inversion of (7a) gave $0.78903$ on the larger-theta side of $p=401$ (LP value $0.98476$) and $0.69898$ on the plus side of $389^2$ (exact value $0.70893$).

## A square obstruction to preserving the attenuated projection

For $q=h^2$, let $I=(\mathbb F_h^\times)^\perp$ be the subfield annihilator, with size $k=(h+1)/2$. Its indicator lies in $\mathbb Rj+V_+$ and the exact plus endpoint is $m_0=k/\sqrt n$. [Square-order control](square-order-control.md#the-fourier-frequencies-carrying-the-discrepancy)

For $\sigma=+$, every correction $p\in\mathbb Rj+V_-$ with $Y=H_\rho+p\ge0$ satisfies

$$
\boxed{\displaystyle
\langle j,p\rangle-\frac{p_0}{m_0}
\ge \frac{H_{\rho,0}-\rho\langle\mathbf1_I,u\rangle}{m_0}-c .}
\tag{8}
$$

In fact the sum of $Y$ on $I$ is $m_0(c+\langle j,p\rangle)+\rho\langle\mathbf1_I,u\rangle$ and is at least $Y_0$. At the slow references of (7), and at every $0\le\rho\le r=q^{-1/3}$, the right side in (8) is at least $\sqrt2-1-o(1)$. This uses $|\rho\langle\mathbf1_I,u\rangle|\le\rho\sqrt{k/s}=o(1)$ and $c\le1$. Thus preserving or raising the raw mark requires an order-one constant correction, even if signed corrections are allowed away from the mark. Equivalently the raw bulk defect already obeys

$$
\sum_{i\in I\setminus\{0\}}d_i\ge H_{\rho,0}-m_0 c-\rho\langle\mathbf1_I,u\rangle\ge1-1/\sqrt2-o(1).
\tag{9}
$$

This can happen while $\|d\|_2\le(s-\rho)\|u\|\le\sqrt s\to0$. Any positive repaired dual with the same attenuated projection and with $Y_0$ bounded below has $Y_0/N\le 1/\sqrt2+o(1)$ at $\rho=r$. Indeed $Y_0\le m_0\langle j,Y\rangle+o(1)\le m_0 N+o(1)$ and $N\ge Y_0/\sqrt{M_r}$ is bounded away from zero. This obstruction applies to all repairs preserving that projection. A dual with a different costly projection can give a different target value bound.

## Numerical replay

The replay uses $r=q^{-1/3}$ and the two moving reference paths $s=q^{-1/12}$ and $s=q^{-1/4}$. Their ratios to $r$ grow as powers of the field order. The second lies below the $\sqrt r$ scale, where (2a) can vanish and (2b) still detects the gap. The 64 rows cover both signs over four primes and four prime squares, with $\rho=0$ at the endpoint and $\rho=r$ at positive width. They check the marked gap, repair nonnegativity, the metric triangle bound, and (6) against a separate target solve. The smaller prime case uses a dense theta LP for the endpoint check. The square endpoint checks use the exact subfield formula. The numerical bounds and residuals are floating-point diagnostics. [FFT replay](parallel-transport-15.py) · [CSV](parallel-transport-15.csv)

| Order, plus sign | Reference width | Frozen gap | Norm bound (2a) | Mark bound (2b) | Repaired lower bound on $\sqrt{M_+(0)}$ |
|---|---:|---:|---:|---:|---:|
| $153649$ | $q^{-1/12}$ | 7.34727 | 3.43656 | 6.65149 | 0.69793 |
| $389^2$ | $q^{-1/12}$ | 7.33494 | 3.45685 | 6.64175 | 0.67417 |
| $153649$ | $q^{-1/4}$ | 0.12630 | 0 | 0.08104 | 0.88375 |
| $389^2$ | $q^{-1/4}$ | 0.13376 | 0 | 0.08134 | 0.70893 |

The endpoint repair at $389^2$ and $s=q^{-1/4}$ attains the exact $\sqrt{M_+(0)}$ to floating-point precision. For $\rho=r$ at the same reference path, (6) gives upper energy estimates $17.57$ at $153649$ and $31.02$ at $389^2$, rounded upward, with target solves about $2.60$ and $3.79$. The upper value in (6) comes from an anchored target trial, so these rows isolate the loss on the repaired dual side. All fixed-point residuals were below $2\cdot10^{-10}$. Independent dense nonnegative least-squares solves at $13,49,361,401$ agreed on the target values within $1.6\cdot10^{-15}$ and on the target allowed energies within $1.2\cdot10^{-10}$.

```sh
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python -B research/parallel-transport-15.py
```

The missing prime estimate is small repaired defect at the slow reference, or a sufficiently sharp scalar gap for (6) together with control of the chosen reference norm. The unrestricted split of a frozen reference and the convex interpolants above cannot supply those inputs across the round-14 width ratio.
