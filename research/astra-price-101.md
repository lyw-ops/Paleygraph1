# A uniform background on the signed head

On the original filtered trapped list, the flat trial may leave as much as
$o(J)/b$ probability **per measured high block**, where $b=|G/L|$. A centered
head projection can therefore use one uniform background on the whole quotient.
There is also a sparse set, determined by the authentic sector alone, on
which such a cap necessarily fails. Whether the genuine signed data put
their high prices on this set matters.

Use the prime, companion sign, zero start, original candidate list and
$J=\lfloor D(p)/8\rfloor$ of [round 98](astra-quotient-98.md).
The original positive root filter and $|\lambda|\le\kappa_*<1$ remain in force.
Only the trial uses the shrinking root $\eta=A/J$, $A=8/c_0$, from
[round 99](quotient-floor-99.md). Write $v_0=0$ and let $v_R$ be the
original-denominator signed means of the true flat prefix, with its permitted
per-time exterior erasures. Put $s=AJ/\log J$, $S=\{R:v_R>s\}$.
The separately erased triangular row retains the original weights
$2(J-1-j)/(J(J-1))$.

## Capped head trial

For any allowed probability $u$ with $w=u_0\ge\eta$ and
$u_R\le d/b$ on $S$, the [positive first-mass bound](astra-quotient-99.md)
$\sum_R(v_R)_+\le b$ gives
\[
       \frac{\langle v,u\rangle}{w}
       \le \frac{s(1-w)+d}{w}
       \le \frac{J^2}{\log J}+\frac{dJ}{A}.                       \tag{1}
\]
Thus any $1\le d=o(J)$ suffices through primes if the trial is available.
In particular the head can carry its full uniform background.

Let $P_c$ project onto the allowed nonidentity Fourier modes, and let
$Q_c=P_c-(P_c)_{:S}[(P_c)_{SS}]^\dagger(P_c)_{S:}$.
Its range consists of the mean-zero allowed rows vanishing on $S$, by the
Gram projection in [round 100](astra-root-100.md). If $k=Q_ce_0$ has
$k_0>0$, put $t=\|k_-\|_\infty>0$. Then
\[
 u=(k+t\mathbf1)/(bt),\qquad
 u_R=1/b\ (R\in S),\qquad u_0=1/b+k_0/(bt).                       \tag{2}
\]
The single inequality $(b\eta-1)t\le k_0$ suffices. One may use any
$t\ge\|k_-\|_\infty$ with this property, or any direction in the same
subspace. Conversely, given an allowed probability of root $w>1/b$ and
exactly uniform entries on $S$, subtract its uniform background to obtain a
mean-zero head-zero direction of root $w-1/b$ and negative part at most
$1/b$. This proves exactness when all directions are tested. The projected
root column itself requires only one head solve and one scan.

More generally, the maximum root subject to the head cap $d/b$ has the dual
\[
 \min_{c,g}\left(c+\frac d b\sum_{R\in S}[-c-g_R]_+\right),
 \qquad c+g_R\ge1_{R=0}\quad(R\notin S),\quad g\in V_{-\sigma}(B). \tag{3}
\]
Here $c$ is real. Add a nonnegative multiplier at every capped coordinate in
the probability LP and minimize each multiplier at fixed $c,g$. This gives
(3) by finite LP duality, with the uniform law feasible for $d\ge1$.
An opposite-sector majorant must now pay for the sizes of its actual defects.

## A forced exterior set and a comparison on the same prime matrix

Let $P=P_c+\mathbf1\mathbf1^*/b$, $h=Pe_0$, and $\rho=h_0$.
The compressed Jacobi operator $K_B$ gives
$P=(I+\sigma K_B+\mathbf1\mathbf1^*/b)/2$, hence
$1-\rho=(1-\sigma\lambda-1/b)/2$ is bounded below eventually.
For $0<\eta<1$ form
\[
 H=\{R\ne0:h_R>(1-\rho)\eta/2\},\qquad
 |H|\le\frac{4\rho}{(1-\rho)\eta^2}.
\]
Indeed $\sum_{R\ne0}h_R^2=\rho(1-\rho)$. For every allowed probability
of root $w\ge\eta$, projection gives
$\sum_{R\ne0}u_Rh_R=(1-\rho)w$. Off $H$ the contribution is at most
$(1-\rho)\eta/2$. Consequently
\[
 \sum_{R\in H}u_Rh_R\ge(1-\rho)w/2.
\]
If $u_R\le d/b$ on $H$, Cauchy–Schwarz and the size bound give an upper
$2\rho d/(b\eta)$ on this sum. Necessarily
$d\ge b(1-\rho)\eta^2/(4\rho)$. At $\eta=A/J$, even a cap $d=o(J)$
fails on this $O(J^2)$-point set whenever it is contained in the true head,
since $b\asymp\sqrt n$ dominates every fixed power of $J$.
This is a conditional obstruction on the genuine prices, with $H$ specified
before they are inspected.

The scalar moment and transform constraints alone permit this obstruction at
the full horizon on **each** filtered prime quotient. For comparison keep the
zero start and the true bounded scalars $\beta_j$. Prescribe the nonnegative
activation entering update $j$ to be zero for $j=0$ and
$[J^3/(J-2)]1_L$ for $1\le j\le J-2$ ($J\ge3$), adding
$\beta_j\sqrt n e_0$ separately in every update. These inputs replace the
actual absolute states. The quotient means of the resulting signed states,
averaged at $0\le j<J$, equal $T\sigma K_Be_0$, where
$T=J^2+\sqrt n\sum_{j<J-1}\beta_j/(mJ)=J^2+O(1)$.
Indeed averaging on quotient blocks commutes with the Jacobi multiplier,
and the quotient mean of $1_L$ is $e_0$.
After deleting the original block the normalized price is exactly
\[
               T\left(1-\sigma\lambda-\frac1{bw}\right)
\]
before exterior erasures. This uses $\sigma K_Bu=u-\mathbf1/b$.
Every permitted per-time erasure changes a block mean by at most
$O((J^2+1)H_p^2/m)=o(1)$: the block input is transformed by $K_B$ with
entries at most one, and the marked physical column is bounded by the
complete Jacobi estimate. Thus the lower is $\gg J^2$ for **every** eligible
trial even after erasure. Before erasure the quotient average of the squared
signed block means is $O(J^4/b)$ by $\|K_Be_0\|_2\le1$, and the quotient
average of their positive parts is $O(J^2/\sqrt b)$. Both averages vanish
even after the uniform $o(1)$ perturbation.
For $R\in H$, the exterior signed mean exceeds
$T[(1-\rho)\eta-1/b]-o(1)>s$ eventually. This comparison tests the
genuine prime multiplier and locations. It supplies no trajectory satisfying
the nonlinear recurrence after the first update.

## Finite actual signed-price separation

At $p=769$, $m=8$, $b=48$, $J=16$, use the plus signed data with erasure
$2+2j$ from the [previous replay](astra-quotient-99.md).
The actual head above $6/5$ is $\{10,12,36,38\}$, and every exact avoiding
law has root below $0.076456$. Formula (2) with $t=137/1000$ produces root
in $[0.081732399,0.081732400]$ and normalized signed price in
$[2.979944464,2.979944465]$, leaving $1/48$ at every head site.

The full signed optimum gives a stronger separation. Among all allowed laws
with normalized price at most $-1/100$, the maximum root lies in
$[0.076460565,0.076460566]$, strictly above the all-law exact-avoidance
upper. At price cap zero the interval is $[0.076601033,0.076601034]$.
For each cap $\xi$, maximize $u_0$ under
$\langle v-\xi e_0,u\rangle\le0$ and the original probability constraints.
The [384-bit checker](astra-price-101-check.py) solves the fixed
24-column primal and transposed dual systems. All basic masses and the price
multiplier are strictly positive and every nonbasic dual slack is positive.
Basic equalities are exact by construction and both sine and cosine
constraints are included. The [replay record](astra-price-101-checks.jsonl)
uses the finite cutoff $6/5$; neither its floor nor this prime establishes
the asymptotic trial.

1. On the true $AJ/\log J$ head measure the centered column ratio in (2)
   and the cap dual (3) with $d=1$ or growing $d=o(J)$. The forced set $H$
   diagnoses one possible failure on each candidate.
2. When this cap fails, price the genuine signed values directly, retaining
   the separate physical triangular test. The prime-uniform flat upper,
   triangular estimate, escaped branch and ordinary theta limit remain open.
