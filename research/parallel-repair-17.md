# Four clipped projections for the positive repair

For [ETH Problem 26](https://randomstrasse101.math.ethz.ch/posts/PaleyGraph/), start with the actual reciprocal pair at positive width and project its opposite member to the endpoint Fourier sector. A short formula repairs the negative part of this projection. Four clipped Fourier steps from three quarters of the available mean, followed by one positive Jacobi convolution, fit the reserve on all 20 sampled prime rows, including both signs at $p=1000033$. The same formula reaches the subfield lower bound on the eight sampled square plus rows. The finite tests use no endpoint or repair LP. The residual identity gives a strict contraction through primes up to the universal Jacobi support threshold. That threshold is sharp on the square plus side, and uniform control on the actual prime residuals remains open.

## Setup and explicit formula

Use the notation of [Round 15](parallel-transport-15.md#deflate-the-expensive-part-of-the-dual) and [Round 16](parallel-defect-16.md). Write $P=P_{-\sigma}$, $U_{-\sigma}=\mathbb R\mathbf1+\operatorname{im}P$, and $\overline f=n^{-1}\sum_i f_i$, with $n=(q-1)/2$. For the actual reciprocal pair $x=A_\sigma(s), y=A_{-\sigma}(s)$ at $0<s<1$, let
$$
H=(J+P)y,\qquad c=\langle j,y\rangle,\qquad a=H_0,\qquad B=1-c,\qquad D=\sqrt n\,(-H)_+ .
$$
Here $J$ is the constant projection and $j=\mathbf1/\sqrt n$. All corrections below are in **scaled** coordinates until divided by $\sqrt n$. The input obeys the exact complementarity identity
$$
D_i=\frac{s}{1-s^2}\big(\sqrt n\,x_i-(1-s)c\big)_+\quad(i\ne0),\qquad D_0=0\quad(a>0).
$$
Thus the input to the algorithm already accounts for the slack in the actual reciprocal member $y$.

Let $\kappa=P_{00}=|D_{-\sigma}|/n>0$; the positional sign set $D_{-\sigma}$ here is as in (4) of Round 15. If $\lambda_i=nK_{i0}$ are the Jacobi entries of $K=P_+-P_-$, put
$$
\omega=\max_{i\ne j}(-P_{ij})
       =\frac{1+\max_{i\ne0}\sigma\lambda_i}{2n},
\quad h_*=1+\frac{\kappa}{\omega},
\quad R=\frac{\mathbf1+P e_0/\omega}{h_*}.
\tag{1}
$$
The off-diagonal entries of $-P$ in each row sum to $\kappa$, so $\omega>0$. Translation invariance and (1) give $R\ge0$, $R_0=1$, $R\in U_{-\sigma}$ and $\overline R=1/h_*$. This is the smallest mean among nonnegative, anchored vectors of the form $(\mathbf1+vPe_0)/(1+v\kappa)$, $v\ge0$: nonnegativity requires $v\omega\le1$. The universal Jacobi cap is the same construction with $\omega_J=(1+\sqrt q)/(2n)$ and $h_J=1+\kappa/\omega_J$.

For a proposed mean $b\le B$, use the following projection and finish:
$$
\begin{aligned}
\alpha&=\min\{2,1/(\kappa+\omega)\}, & A_0&=b\mathbf1,\\
E_k&=(D-A_k)_+, & A_{k+1}&=A_k+\alpha P E_k,\\
\sqrt n\,G_k&=A_k+t\mathbf1+R*(D-A_k-t)_+.
\end{aligned}
\tag{2}
$$
Here $*$ is unnormalized cyclic convolution, and $t$ is an upper order statistic of $D-A_k$ at cutoff $h_*$. Formula (2) uses one Fourier projection per step and requires no linear solve or search for a feasible mean. Because $R_0=1$, $R\ge0$, and its translates stay in $U_{-\sigma}$, every $G_k$ belongs to $U_{-\sigma}$ and satisfies $\sqrt n G_k\ge D$, even at infeasible $b$. In particular $G_k\ge0$ and $H+G_k\ge0$.

The mean excess over the **available** reserve is exactly
$$
F_k(b)=\langle j,G_k\rangle-B
      =b-B+\frac{1}{h_*}T_{h_*}(D-A_k),
\tag{3}
$$
where $T_h$ sums the top $h$ entries, with a fractional last entry. This is the minimum over $t\in\mathbb R$ of $b-B+t+h_*^{-1}\sum_i(D_i-A_{k,i}-t)_+$. The residual must be sorted **before** taking its positive part here; negative slack can lower the cost. At $b=B$, the signed tail average in (3) is the entire excess. At $b=3B/4$, it is enough that the average fit in the last $B/4$. If $F_k(b)\le0$, one may add the remaining mass as a constant to reach $B$ exactly. Using the unpadded row preserves the sharper endpoint comparison
$$
m_0=\sqrt{M_\sigma(0)}\ \ge\ \frac{a+(G_k)_0}{c+\langle j,G_k\rangle}.
\tag{4}
$$
This follows by pairing $H+G_k$ with an anchored, nonnegative endpoint row in $U_\sigma$; the pairing equals the product of the two constant coordinates, and is at least the product of the marks.

## What one step does to the violation

Write $r_k=D-A_k$, $S_k=(-r_k)_+$, and $Z=I-\alpha P$. The exact recurrences are
$$
r_{k+1}=Z E_k-S_k,\qquad E_{k+1}=(Z E_k-S_k)_+ .
\tag{5}
$$
For real $z$ and $S\ge0$, $v=(z-S)_+$ satisfies $v^2+(z-v)^2\le z^2$. Sum coordinatewise and use $P^2=P=P^\mathsf T$ to obtain
$$
\|E_{k+1}\|_2^2+\|E_{k+1}-ZE_k\|_2^2
 +\alpha(2-\alpha)\|PE_k\|_2^2\le\|E_k\|_2^2 .
\tag{6}
$$
This bound holds at every proposed mean, including the square plus cases where the reserve is infeasible. It measures squared error; (3) is still the relevant mass certificate.

There is also a pointwise bound at the scale of the Jacobi tail. If $m_k=\|E_k\|_\infty>0$, put $d_k=\|E_k\|_1/m_k$, the effective support size. By (1), off-diagonal entries of $Z$ are at most $\alpha\omega$, its diagonal is $1-\alpha\kappa$, and the latter is at least $\alpha\omega$ by the choice of $\alpha$. From (5),
$$
\boxed{\quad
m_{k+1}\le
\big[1-\alpha\kappa+\alpha\omega(d_k-1)\big]m_k
=\big[1-\alpha\omega(h_*-d_k)\big]m_k .
\quad}
\tag{7}
$$
The coefficient is nonnegative since $d_k\ge1$. Indeed, at row $i$, $(ZE_k)_i\le (1-\alpha(\kappa+\omega))E_{k,i}+\alpha\omega\sum_j E_{k,j}$. The slack $S_k$ can only improve this bound. If $E_k=0$, the iteration stays feasible. If $d_j\le(1-\delta)h_*$ for several successive steps, (7) gives a geometric reduction with multiplier at most $1-\delta\alpha\omega h_*$ on those steps. More generally, the product of the factors in (7) bounds the remaining peak, which in turn bounds the signed tail average in (3).

In prime order, the Jacobi inequality is **strict on both signs**: $\lambda_i\in\mathbb Q(\zeta_n)$, whereas $\sqrt p\in\mathbb Q(\zeta_p)\setminus\mathbb Q$ by the quadratic Gauss sum. The conductors are coprime, so the fields intersect in $\mathbb Q$. Thus $\lambda_i\ne\pm\sqrt p$, and the [Jacobi bound](fable-audit-9.md#a-strict-finite-prime-inequality) gives $h_*>h_J$. In particular a nonzero violation with $d_k\le h_J$ has a strictly smaller next peak at every prime. This is a local, order-by-order theorem. It supplies neither a uniform gap between the two heights nor a bound on $d_k$ in the actual orbit. The largest observed improvement of $h_*/h_J$ in the prime trials was about $0.001$ above one.

For $0<\alpha<2$ there is a necessary obstruction at a persistent nonzero residual. By (6), $PE_k\to0$ at each fixed order. The shadows have fixed mean and a uniform lower bound because $A_{k,i}\ge D_i-\|E_0\|_2$, so they have convergent subsequences. If a limit shadow $A$ has $E=(D-A)_+\ne0$, then $E\in U_\sigma$, $E\ge0$, and $\overline{EA}=b\overline E$. Consequently every positive majorant obeys
$$
\langle j,G\rangle\ge\frac{\overline{ED}}{\overline E}
       = b+\frac{\overline{E^2}}{\overline E}>b.
\tag{8}
$$
Thus no positive majorant has mean $b$ in this case. At such a fixed residual, (7) forces $\|E\|_1/\|E\|_\infty\ge h_*$. One can also extract a finite-step lower bound without identifying a limit: put $W=(I-P)E_k+\|(PE_k-E_k)_+\|_\infty\mathbf1$. This is a nonnegative vector in $U_\sigma$ and, if $E_k\ne0$, has positive mean. Its ratio $\overline{WD}/\overline W$ is a lower bound by the same pairing. This bound and (3) use only the computed orbit.

## Square comparison at every depth

For $q=\ell^2$ and $\sigma=+$, let $I=(\mathbb F_\ell^\times)^\perp$, $k_I=(\ell+1)/2$. Then $\mathbf1_I\in U_+$, $P\mathbf1_I=0$, and $\lambda_i=\ell$ on $I\setminus\{0\}$. Also $\kappa=1/2$ and $h_*=h_J=k_I$. In particular a violation constant on $I$ and zero outside has effective support exactly $h_*$ and $PE=0$. If it is the residual of a shadow, it is a fixed residual of (2).

For **every** shadow at mean $b$, the average of $A_k$ on $I$ is $b$. As $T_{k_I}$ is at least the sum on $I$, there is an exact lower bound independent of depth:
$$
F_k(b)\ge\frac1{k_I}\sum_{i\in I}D_i-B
\ge\frac{a}{m_0^{\rm sq}}-1,
\qquad m_0^{\rm sq}=\frac{k_I}{\sqrt n}.
\tag{9}
$$
The second inequality uses $\sum_I H_i=m_0^{\rm sq}c$ and the negative part off the mark. By the [fixed-width theorem](parallel-fixed-width-13.md), $a\to1/(1+s)$, so the liminf in (9) is at least $\sqrt2/(1+s)-1>0$ for $s<\sqrt2-1$. This applies even when the number of repair steps depends on the order. On the tested square plus rows, the four-step finish attains the first lower bound in (9) to floating-point precision; the independent translated subfield construction from Round 16 certifies the optimum and the square obstruction by interval arithmetic. The square minus rows fit the reserve and serve as a control.

## Reproducible comparison

The [FFT replay](parallel-repair-17.py) uses the exact form of the reciprocal fixed point for its input solve, then Fourier masks, clips and one convolution for the four-step candidate. It records both $b=B$ and $b=3B/4$ at depths $0,1,2,4,8,16$, and checks (5)–(7), (9), and the completed row. It also records the universal cap and ordinary Douglas–Rachford at the **same** mean and depth. The [CSV](parallel-repair-17.csv) has 432 rows: five prime orders, four square orders, both signs, and widths $1/16$ and $q^{-1/4}$.

| Order, plus side | Width | $b/B$ | Excess at depth 0 | Depth 2 | Depth 4 | Depth 16 |
|---|---:|---:|---:|---:|---:|---:|
| $9413$ | $1/16$ | $3/4$ | $0.065604$ | $0.000353$ | $-0.012033$ | $-0.028282$ |
| $153649$ | $1/16$ | $3/4$ | $0.091296$ | $0.006844$ | $-0.008068$ | $-0.027809$ |
| $389^2$ | $1/16$ | $3/4$ | $0.326597$ | $0.324653$ | $0.324653$ | $0.324653$ |
| $1000033$ | $1/16$ | $1$ | $0.112759$ | $0.015332$ | $0.005120$ | $0.000026$ |
| $1000033$ | $q^{-1/4}$ | $3/4$ | $0.068428$ | $0.009048$ | $-0.000761$ | $-0.013390$ |

All 20 prime rows and eight square minus rows fit after four steps at $b=3B/4$. The least prime margin is about $0.0007607$, at the moving width for the largest prime. The four-step Douglas–Rachford shadows also fit on those rows. The clipped update uses one state in the affine space and gives the explicit residual inequalities above. The longer, separately tuned Round 16 runs obtained lower final repair costs in some cases. At $b=B$, the largest positive excess on the 20 prime rows is at most $0.00512$ by depth four and below $0.000051$ by depth sixteen (unrounded values in the CSV). For example, after one step on the fixed-width plus side at $153649$, the excess falls from $0.091296$ to $0.027043$, compared with $0.054687$ for the first Douglas–Rachford shadow.

The [36-row interval replay](parallel-repair-17-certified.jsonl) follows Round 16: it encloses the error to the exact reciprocal pair at each width (treated as an exact binary fraction), rounds the candidate in its allowed Fourier support, and pays a rational constant only if the interval signs require one. It certifies a positive correction to the actual $H$, the spare reserve, and an endpoint lower bound. The spare reserve is at least $0.0007607$ on the prime rows and $0.01013$ on square minus rows. On the square plus rows it separately checks the translated subfield witness and proves that every positive repair has excess at least $0.07312$. The floating trajectories diagnose the formula and its residual, whereas the interval records certify the rounded four-step witnesses.

~~~sh
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 \
  .venv/bin/python -B research/parallel-repair-17.py \
  > research/parallel-repair-17.csv
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 \
  .venv/bin/python -B research/parallel-repair-17.py --certify-max-order 1000033 \
  > research/parallel-repair-17-certified.jsonl
~~~

For a field-first proof it would suffice, at each fixed small $s$, to find a depth $N(s)$ independent of $p$ such that the positive excess in (3) has prime limsup $o_{s\downarrow0}(1)$ on both signs. Then (4) and $a\to1/(1+s)$ give the lower endpoint bound, and reciprocity gives the upper one. Neither the ordinary $\ell_2$ dissipation in (6) nor the strict inequality $h_*>h_J$ proves that statement. For example, actual effective support can exceed $h_*$ even though the signed tail already fits the reserve. The estimates still need to control the actual residual tail or the weighted Jacobi slack in (7) on the prime sequence.
