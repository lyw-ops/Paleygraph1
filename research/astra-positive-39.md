# The second pinned reflection and a positive completion with extra mean

At the actual depth-one Picard proposal with floor $\tau=7/50$, both pinned reflections at threshold zero, applied consecutively, still leave a positive fraction of the bulk negative in each sign. The normalized marked product is strictly below its necessary bound. The computation uses a compact path law only for the initial row and the transformed test. It controls the unknown transform of the first clipping deficit by an orthogonal-reflection identity.

There is also an unconditional constructive bound in the positive direction. Whenever $T/\sqrt n\to\infty$, both true projected rows can be made nonnegative while retaining their individual marks exactly and increasing their common **scaled** mean by $O(\sqrt n/T)=o(1)$, uniformly in $0\le\tau\le1$. This horizon lies outside the proved window for vanishing marked values. ETH Problem 26 for ordinary theta remains open.

## 1. A positive completion with an explicit price at each time

Use the [actual Picard recurrence](averaged-mark-35.md), the [endpoint formula](astra-completion-37.md), and the [pinned projection](astra-conic-primal-34.md). Norms without a spatial subscript are counting Euclidean norms; $E$ means $n^{-1}\sum_i$ and $\|f\|_{2,n}^2=E f^2$. Let $Z_\sigma=\sqrt n X_{\sigma,T}$, of scaled mean $G=\sqrt n M_T$. Write
\[
 Z_\sigma=U_\sigma+e_\sigma,\qquad
 U_\sigma=\frac{\sqrt n}{T}\sum_{t=1}^T A_{\sigma,t}\ge0,\qquad
 h_\sigma=\|e_\sigma\|_{2,n}
 =\frac{\|P_{-\sigma}(v_{T+1}-v_1)\|}{2T}.
\]
For $a=(P_\sigma e_0)_0$, $\ell=P_\sigma e_0$, the row $b_\sigma=1-\ell/a$ has mean one, belongs to $\mathbb R1+V_\sigma$, vanishes at the mark and is at least $1/2$ everywhere else for $n\ge16$. Indeed $|\ell_i|/a\le(1+\sqrt{2n+1})/(n-2)$ off the mark.

Choose $s\ge4n^{1/4}h_\sigma$ and $s>0$. Start at $Y=Z_\sigma+s b_\sigma$, put $d_i=(s/4-Y_i)_+$ off the mark and $d_0=0$. Set $L=P_\sigma-\ell\ell^T/a$ and $R=2L-I$. Then
\[
 E d\le E(-s/4-e_\sigma)_+\le h_\sigma^2/s.
\]
The off-mark signed spill bound of rounds 34–37 is $\|Rd\|_{\infty,\mathrm{bulk}}\le3\sqrt n E d$. Hence the single explicit reflection $Y+2Ld=(Y+d)+Rd$ has bulk minimum at least $s/4-3\sqrt n h_\sigma^2/s\ge s/16$. Its mark is $Z_\sigma(0)$ and its mean is $G+s$. If $h_\sigma=s=0$, $Z_\sigma=U_\sigma$ is already nonnegative. A common $s$ can be chosen by taking the maximum for the two signs. This proof uses the actual endpoint without solving for the stationary pair.

The mark is positive for all sufficiently large $T$, uniformly in $n\ge16$ and $0\le\tau\le1$. Indeed the coherence estimate and the energy telescope from time zero give
\[
 T^{-1}\sum_{t=1}^T |v_t(0)|\le2\sqrt q\,T^{-1}\sum_{t=0}^{T-1}\mu_t
 \le2\sqrt{qW/n}.
\]
The marked raw factors have product one, and either is bounded above by $1+|v_t(0)|$. Cauchy–Schwarz on their time averages gives $U_\sigma(0)\ge\sqrt n/(1+2\sqrt{qW/n})$. Meanwhile $|e_\sigma(0)|\le\sqrt n h_\sigma$ and the same telescope gives $h_\sigma\le[2\sqrt{W(T+1)}+2]/(2T)$. Thus the original mark is positive as claimed.

At positive floor, the stationary comparison bound $\|v_t-v^*\|\le\|v^*\|\le2\sqrt W\,q^{1/4}$ from [round 36](astra-averaged-positive-36.md) gives the common price
\[
 s\le \frac{8\sqrt W\,(nq)^{1/4}}{T}
\]
when choosing the displayed sufficient price for both signs. At $\tau=0$ the same finite-time endpoint estimate follows by continuity. This proves the uniform $o(1)$ allowance at every $T/\sqrt n\to\infty$. At fixed positive floor round 37 shows that the proposed marks already inherit the stationary marked values on this horizon. Their required prime cancellation remains unproved.

There is a signed sector consequence on squares. Along any growing square sequence and any growing depth inside the [round-38 marked window](vanishing-floor-38.md), take $\tau_q\to\tau\in[0,1)$. Then $Z_-(0)/\sqrt n\to1$ and $G\le\sqrt{1+\tau}+o(1)$. Since a nonnegative minus row of unit mean has mark at most $(\sqrt q+1)/2$, applying the construction just to that row gives
\[
 \liminf_q \frac{n^{1/4}}{T}\|P_+(v_{T+1}-v_1)\|
 \ \ge\ \frac{\sqrt2-\sqrt{1+\tau}}2 .
\]
This charges the *actual terminal difference in the opposite sector*. A corresponding prime upper bound is unavailable in the marked window.

## 2. Testing two real reflections with an unknown transformed hinge

For the rest of the note $T=1$, $\tau=7/50$, and rows are normalized to mean one. Write $z=X_{\sigma,1}/M_1$, and for a row in its affine space of prescribed mean and mark use $F(z)=z+2L(-z)_+$, with zero clipping at the mark. The canonical representative is $c=1+(z(0)-1)\ell/a$. Thus $Lz=z-c$ and
\[
 F(z)=c+L|z| .
\]
The mark is positive for large fields. Zeroing the input of $L$ at that coordinate never affects the output. The formula makes $F$ nonexpansive on this affine space.

Let $x_q=\widehat s/\sqrt q$ be the Jacobi coordinate of [round 38](astra-prime-repair-38.md). Orient the bulk coordinate by $x=\sigma x_q$, set $t=T_2(x)=2x^2-1$, and use $y=\sigma KT_2(x_q)$. In the limiting probability space $x$ is arcsine, and $y$ is the sum of two independent semicircle variables, each supported on $[-1,1]$, independently of $x$. Let $f(x)=2\sqrt{\tau+2x^2}$, $g=E f/2$, and $c_j=2E[fT_j]$ for $j\ge1$ under this arcsine law. Define $b=c_2/(4g)$ and the actual affine comparison row $z'=c+2bL T_2(x_q)$. Its limiting bulk expression and distance from the actual input are
\[
 z'=1+\frac{\sqrt2}{g}x+b(t+y),\qquad
 \lim\|z-z'\|_{2,n}
 =d_*:=\left[\frac{1+\tau-g^2}{2g^2}-b^2\right]^{1/2}.                 \tag{1}
\]
Indeed, in the expansion of the round-38 bulk row every omitted even degree contributes $c_j(T_j+\sigma KT_j)/(4g)$. The scalar and transformed families are mutually orthogonal in the limiting $L^2$, each term having second moment $1/2$. Completeness and contraction give the limit after finite truncation. The two actual marks agree exactly, so their scaled masses do not contribute to the difference. Here $g=1.00112350\ldots$, and hence both actual normalized marks divided by $\sqrt n$ tend to $1/g<1$.

Use the nonnegative test
\[
 h(x)=(-9/20-x)_+/E(-9/20-x)_+ .
\]
Put $h_q=h(\sigma x_q)$ and $H_q=2Lh_q$. Its norm limit is $N=[2(Eh^2-1)-h_1^2]^{1/2}$ for $h_j=2E[hT_j]$, and its conditional mean given $(x,y)$ is
\[
 H=h-1-h_1x+h_2 y.                                                      \tag{2}
\]
Here and below a conditional-mean statement means convergence of pairings with bounded continuous functions of $(x,y)$ in the empirical limit. For finite scalar polynomials these formulas follow from the [joint path law and root pinning](scalar-seed-25.md): all remaining path variables are centered and independent of $(x,y)$, and $L$ kills the constant and Jacobi-linear terms. Polynomial approximation in $L^2$ and contraction extend this to $h$. The sign on the odd transformed terms has no effect on their conditional mean or norm. Removing the marked coordinate before interpreting these bulk formulas is justified by $H_q(0)=0$.

For the comparison row take its true deficit $d=(-z')_+$, zero at the mark. Put
\[
 B=.040-.070x+.047t-.055y,\qquad
 B^R=-.040+.070x+.047y-.055t.
\]
Use these same expressions in the actual coordinates and set $B(0)=0$. On the bulk $RB$ has limiting expression $B^R$, with vanishing $L^2$ error. Indeed $R1=-1$, $Rx=-x$ and $Rt=y+o(1)$ on the bulk, using the fixed-path estimate also at the mark. Furthermore $R L=L$ and the exact relation $L K=\sigma L$ yield $Ry=t+o(1)$ in bulk $L^2$ from the same formulas (equivalently use $K^2=I-J$). All fixed-degree inputs are bounded at the mark; resetting them there changes normalized $L^2$ by $o(1)$.

Write $u=z'+d+RB$ and $r=R(d-B)$. The first *actual* reflection on the comparison row is exactly $u+r$. The second hinge satisfies
\[
 (-u-r)_+ =(-u)_+-r/2+(|u+r|-|u|)/2 .
\]
Since $RH_q=H_q$, its linear error pairs exactly as $E[rH_q]=E[(d-B)H_q]$. Cauchy–Schwarz on the final absolute-value error costs at most $\|d-B\|_{2,n}\|H_q\|_{2,n}/2$. Using the limiting bulk symbols on the right, and reverting to the actual starting row by nonexpansiveness twice, gives
\[
 \limsup_q E[h_q F^2(z)]\le
 E\left[h z'+\left(\frac{d+B}{2}+(-u)_+\right)H\right]
 +\frac N2\left(\|d-B\|_2+d_*\right),                              \tag{3}
\]
where $u=(z')_++B^R$ on that right-hand side. In particular, the expression does not replace $K d$ by a compact variable. The comparison cost is $Nd_*/2$ because the difference of the two final rows belongs to $\mathrm{im}\,L$. The possible $O(\sqrt n)$ positive common mark in $E h_q z'$ contributes $o(1)$.

## 3. The compact integral and stability of the conclusion

The [Arb checker](astra-positive-39-check.py) gives the following [128-bit record](astra-positive-39-certified.jsonl). Its two-dimensional quadrature uses $65536$ angular midpoints for $x$ and $16384$ bins for each semicircle variable. Their exact bin masses are convolved to get the midpoint law for $y$. At fixed $x$, both $z'$ and $B^R$ are affine in $y$ and the two pieces of $u$ have positive slope. Splitting at their roots, the conditional integral and squared residual require only the first three prefix moments of that midpoint law. Every floating guess for a bin index is certified by interval inequalities.

| Quantity | Certified outward bound |
| --- | ---: |
| Signed midpoint integral in (3) | $<-.08530964$ |
| Error of that integral | $<.00409247$ |
| $\|d-B\|_2$ | $<.06547204$ |
| Initial path truncation $d_*$ | $<.03824283$ |
| Test norm $N$ | $<1.332276$ |
| Full upper bound in (3) | $<-.01212878$ |

For the discretization estimates the changes in $x,y$ are at most $\pi/(2\cdot65536)$ and $2/16384$. On the support, $b<.26$, $\sqrt2/g<1.42$, $|z'|\le3.2$, $0\le d\le1.2$, $|B|\le.267$ and $|B^R|\le.259$. Also $h<5$, its Lipschitz constant is below 8, $|h_1|<2$, $|h_2|<1.2$, and $|H|<10.4$. The coefficient $(d+B)/2+(-u)_+$ has absolute value below one. In $x$ its Lipschitz constant is at most $(2.46+.258)/2+2.46+.29$, and in $y$ it is at most $(.26+.055)/2+.26+.047$. The product rule yields Lipschitz constants below $130,8$ for the signed integrand. For $d-B$ the constants are below $3,.32$. Applying the latter to the RMS directly by Minkowski supplies the residual-error entry. These estimates hold across all hinges.

Thus $E[h_q F^2(z)]<-.012$ eventually for **each sign** on every prime or eligible square sequence. In particular a positive fraction of coordinates fall below $-.005$. To see this, the actual normalized $\|z\|_{2,n}$ is uniformly bounded from the depth-one projection and energy bounds, and $\|F(z)\|_{2,n}\le3\|z\|_{2,n}$. The bounded test and Cauchy–Schwarz on $\{F^2(z)<-.005\}$ give the assertion, since $E h_q\to1$. The positive pinned mark is outside this set.

The same strict failure tolerates small nonzero thresholds and mean or mark allowances **within these two reflections**. With bulk threshold $\delta$ the exact formula is $F_\delta(z)=c+L|z-\delta|$, also for field-dependent thresholds. Thus changing the two thresholds costs at most $\delta_1+\delta_2$ in normalized $L^2$, for nonnegative thresholds. Differences stay in $\mathrm{im}\,L$, so the induced change in the signed test is at most $(N/2+o(1))(\delta_1+\delta_2)$. In particular any $\delta_1+\delta_2\le .01$ leaves a strict negative margin. Changing the normalized mean by $o(1)$ and the mark by $o(\sqrt n)$ through the canonical representative costs $o(1)$ in normalized $L^2$: the norm of $\ell$ is $\sqrt a$ in counting norm. Changing the initial row by this amount and the affine representative by this amount changes the two-step output by $o(1)$, from the same exact formula. This covers an $o(1)$ scaled mean allowance and $o(1)$ unnormalized marked loss at this floor, including the anchored injection in Section 1 at such a scale. Arbitrary feasible completions of those marks are outside the conclusion, as are larger numbers of reflections, other thresholds, and growing Picard depths.

## 4. One sign does have a strictly positive completion at this very input

At $T=1$ and $\tau=7/50$, the two prescribed marks individually approach $\sqrt n/g$, with $g>1$. The exact identity $\theta_+\theta_-=n$ gives some sign $\sigma$ at each field with $\theta_\sigma\ge\sqrt n$. Let $w$ be an optimal nonnegative even row of unit mean in that sector, attaining $w(0)=\theta_\sigma$. Its mixture with the constant row
\[
 y=(1-\lambda)1+\lambda w,\qquad
 \lambda=\frac{z(0)-1}{\theta_\sigma-1}
\]
has exactly the proposed mean and mark. For every sufficiently large field it has all coordinates at least $.001$: indeed $\limsup\lambda\le1/g$ and $1-1/g>.001$. The selected sign may vary with the field. Thus at least one of the two individually obstructed two-step trajectories has an interior feasible completion with a uniform reserve.

There is a construction without using either the optimum or its sign as input. Starting at the two actual proposals, apply $F_\delta$ independently with fixed $\delta=1/2000$, checking for nonnegativity after each update. At least one sign succeeds in $O(n)$ reflections. In the feasible sign above, write $b_0=.001-\delta$, and let $w_j$ now denote the successive affine iterates. The update is the affine orthogonal projection of $w_j+2d_j$, where $d_{j,i}=(\delta-w_{j,i})_+$ in the bulk. At the mark $d_{j,0}=0$. Consequently the **counting** squared norm obeys
\[
 \|w_j-y\|^2-\|w_{j+1}-y\|^2
 \ge 4\sum_{d_{j,i}>0} d_{j,i}(y_i-\delta)
 \ge 4 b_0\|d_j\|_1 .
\]
If $w_{j+1}$ still has a negative coordinate, the off-mark bound on $Rd_j$ from Section 1 forces $\|d_j\|_1\ge\delta\sqrt n/3$. The mark is pinned and positive. Every unsuccessful output therefore spends at least $4b_0\delta\sqrt n/3$ of the initial squared distance. This distance is $O(n^{3/2})$: the true initial row has $\|z\|^2=O(n)$, while a nonnegative unit-mean optimum has $\|w\|^2\le n\max_i w_i\le n\theta_\sigma$. For the latter inequality, translate any entry to the mark and symmetrize by inversion to preserve evenness and its value there. The elementary unit-mean witness in the opposite sector has root of order $\sqrt n$ from the [Jacobi bound](iterate-majorants.md), so complementary theta gives $\theta_\sigma=O(\sqrt n)$. The same squared-norm estimate holds for the mixture $y$. This proves the stated iteration bound. In particular the negative results and this constructive positive result apply to the very same thresholds on the first two steps. The argument leaves simultaneous positivity of both signs at this input unresolved.

Replay from the repository root with

    .venv/bin/python -B research/astra-positive-39-check.py

The prime-specific estimate at a depth compatible with the proved marked window remains missing.
