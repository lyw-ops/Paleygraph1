# A signed prefix of the true exterior forcing at a recurrent mask

A recurrent physical mask forces a single **signed** prefix average of the genuine Jacobi forcing, unless the unaveraged exterior forcing somewhere before the last good time grows exponentially in the marked depth. The signed test uses a positive-density subset of the critical coset as its contracted set. There is also a version keeping both saturated cosets out of the exterior. Its additional expense is the smaller of the two sign occupations of the true orbit, summed only on the other sites. The three alternatives below concern the zero-start prime orbit.

Use the [round-94 bounded family](astra-quotient-94.md) and its [round-95 size filter](astra-recur-95.md). Write $J=\lfloor D(p)/8\rfloor$, $\mathcal T$ for the good terminals, and let $\sigma$ be the companion sign, so $P_T$ is the negative mask of the opposite primary pin with start one, allowance and cutoff $u=\delta/8$. Let $S=C$ or $S=L$, $m=|S|$, $\mu=\sqrt p/n$ and $M=\mathsf K_{S,S}$. We have $|C|\le m\le2|C|$, $\mu m=O(1)$ and $\|M\|_{1\to1},\|M\|_{\infty\to\infty}\le\kappa\le\kappa_*<1$ for all large fields. All unmarked coordinates below use the true cold states $Y_j$.

Suppose a fraction $\alpha>0$ of $C$ belongs to $P_T$ at least $bJ$ times, for fixed $b>0$. This is exactly the positive-density obstruction reached by the bounded-list selector, since $|\mathcal T|\ge J/4$. There are constants $c,c'>0$ depending only on the fixed parameters for which at least one of the following occurs.

* At least $c|C|$ sites satisfy $\max_{t\le J}|Y_t(i)|\ge\exp(c'J)$. Then at some $j<J$ the mean absolute transformed exterior forcing on $S$ exceeds $\exp(c'J/2)$ for sufficiently large $J$.
* There are one good $T$ and an inversion-symmetric $E\subseteq C\cap P_T$, $|E|\ge c|C|$, with $k=T-2$, for which
  \[
   \frac{\sigma}{k|E|}\left\langle \mathsf K1_E,
          \sum_{j<k}1_{E^c}|Y_j|\right\rangle\ge cJ.                 \tag{1}
  \]
  In particular this is a lower bound for a signed correlation with the single nonnegative prefix-averaged input. Cancellation between times and between output sites is retained. Sites of $C\setminus E$ are included in this version of the input.

In the second case define the genuine prefix minority occupation by
\[
 m_i^-(k)=\min\left\{\sum_{t=1}^{k}(Y_t(i))_+,
                           \sum_{t=1}^{k}(-Y_t(i))_+\right\}.
\]
On the same $T,E$ and for either choice of $S$, there is a real test $\psi$ supported on $S$, given explicitly below, with $\|\psi\|_1\le |E|/(1-\kappa)$ and $\|\psi\|_\infty\le1/(1-\kappa)$, such that
\[
 \frac{1}{k|E|}\left\langle\mathsf K\psi,\sum_{j<k}1_{S^c}|Y_j|\right\rangle
       +\frac{2\mu}{(1-\kappa)k}\sum_{i\in S\setminus E} m_i^-(k)
       \ \ge cJ.                                                      \tag{2}
\]
The first term has the whole fixed contracted set removed. Its absolute upper is a constant times the restricted first absolute moment of the transform of the one averaged input, using $|S|/|E|=O(1)$. Alternatively apply [round 95, (3)](astra-recur-95.md) once to that input before taking the square root. Both (1) and (2), and the exponential conclusion for the absolute forcing, tolerate the independently chosen $H_p^2$ erasures at each time from round 95. Indeed they change any transformed output coordinate by $o(1)$ per step, and the normalized tests have bounded first norm. The true marked forcing is treated separately throughout.

## Earlier wrong-sign occupation at a mask visit

Write $W=2T-1$ and $V=Y_{T+1}+Y_T-2Y_1$. The [exact projected difference](timed-pinning-69.md) gives the unnormalized primary projection as its nonnegative raw prefix minus $\sigma P_\sigma V/2$. The pin addition is nonnegative off the mark at these terminals. On $P_T$, keeping the full early raw contribution and using $P_\sigma=(I-J_0+\sigma\mathsf K)/2$, where $J_0$ projects onto constants, gives
\[
 8\sum_{j=1}^{T-1}(-\sigma Y_j(i))_++4Wu\le
 2H_T(i)+2|Y_1(i)|+2g_T+2g_{T-1}+4g_0,\qquad
 H_T(i)=\sum_{v=-1}^1 |Y_{T+v}(i)| .                                 \tag{3}
\]
Indeed $V$ has mean zero and off the mark $\mathsf K Y_{j+1}=|Y_j|-2g_j$. The last four terms on the right are uniformly bounded by the Jacobi seed and good-time bounds. Thus every visit has $H_T\gg_u J$ and its earlier wrong-sign sum is at most $H_T$ for sufficiently large $J$.

Fix a small $\eta>0$ depending on the contraction gap. For $B_i(k)=\sum_{t=1}^k |Y_t(i)|$, call a visit large if $H_T(i)\ge\eta B_i(T-2)$. After the first half of the $bJ$ visits at a recurrent site, every remaining visit has $B_i(T-2)\gg_{u,b}J^2$. Indeed all but at most three previous three-time blocks lie within the prefix, and each coordinate time is counted at most three times. Every large visit multiplies $B_i$ by at least $1+\eta$ from $T-2$ to $T+1$. From $bJ/4$ such visits at least $bJ/12-O(1)$ have the same residue modulo three and hence concatenate. This forces the exponential peak. If a fixed positive fraction of sites has these peaks, sum their maxima over space and bound by the sum over all times. Summing the [contracted first-norm recurrence](astra-recur-95.md) then gives the stated exponential lower for some single exterior forcing even after erasure. In fact, on at least one of the two prefixes ending immediately before or after that forcing, the restricted first absolute moment of the transform of the *prefix-averaged* exterior exceeds $\exp(c'J/3)$. Subtract the two unnormalized prefix sums and use the triangle inequality. The empty prefix contributes zero. This particular prefix need not end at a good time.

Otherwise at least $\alpha|C|/2$ sites have $\gg_b J$ later visits with $H_T<\eta B_i(T-2)$. Double counting selects one common $T$ and $|E|\gg_{\alpha,b}|C|$ such sites. All selection predicates are invariant under inversion. At every $i\in E$,
\[
       B_i(k)\gg J^2,\qquad
       \sum_{t=1}^k(-\sigma Y_t(i))_+\le \eta B_i(k).                 \tag{4}
\]
The cutoff at $T-2$ leaves the entire three-time block available in the multiplicative growth argument.

## Contracting after summing in time

Sum the true recurrence from $j=0$ through $k-1$. On $E$ its signed output totals contribute at least $(1-2\eta)\sum_E B_i$ by (4). Its internal input costs at most $\kappa\sum_E B_i$: every absolute column sum on the subset $E$ is at most $\kappa$, and the input prefix ends one step earlier than $B_i$. The true scalar source $\sum_{j<k}\beta_j x$ costs $O(k|E|)$. Taking $2\eta<1-\kappa_*$ proves (1).

For the full set $S$, put $Q_i=\sum_{t=1}^kY_t(i)$, $s_i=\operatorname{sgn}Q_i$ (choose $+1$ at zero), and $l_i=(B_i-|Y_k(i)|)/B_i$, with zero at $B_i=0$. Write $D_s,D_l$ for the diagonal matrices on $S$ with these entries. For $d=\sum_{j<k}(\mathsf K1_{S^c}|Y_j|)|_S$ and $f=\sum_{j<k}\beta_j x|_S$, the summed restricted equation and its exact unsigned counterpart are
\[
         Q= M D_l B+d+f,\qquad
         B=D_sM D_l B+D_s(d+f)+2m^-(k).                                \tag{5}
\]
In particular all internal nonlinear feedback in this identity still contracts in first and supremum norms. Let $v=(I-D_sM D_l)^{-*}1_E$ and $\psi=D_s v$, extending $\psi$ by zero. The Neumann series gives the asserted norm bounds for $v$ and $\psi$. Off $E$ the adjoint equation gives $|v_i|\le\mu\|v\|_1\le\mu |E|/(1-\kappa)$. Taking the pairing with $1_E$ in (5) now gives exactly
\[
          \sum_E B_i=\langle\psi,d+f\rangle+2\langle v,m^-(k)\rangle .
\]
The on-$E$ minority costs at most $2\eta\sum_E B_i/(1-\kappa)$ by (4). Take $\eta\le(1-\kappa_*)/8$ and absorb it. The mark costs $O(k|E|)$ as above. Bounding only the remaining minority charge by its absolute value proves (2).

## Both positional signs must pay on the same prefix

Use $U=k^{-1}\sum_{j<k}1_{(S\cup A_j)^c}|Y_j|$ and the counting Fourier convention $\widehat U(w)=\sum_iU_i\overline{i(w)}$. The first term of (2) is $[n|E|]^{-1}\sum_w s(w)\overline{\widehat\psi(w)}\widehat U(w)$ up to $o(1)$ for the allowed erasures. Write $S=cH$, $B=H^\perp$, and choose one representative $z$ for each $B$-coset in the square group. Since $U$ vanishes identically on $S$, orthogonality gives $\sum_{b\in B}c(b)\widehat U(zb)=0$ on **each** fiber. Since $\psi$ is supported on $S$, its conjugate Fourier transform at $zb$ is $c(b)\overline{\widehat\psi(z)}$. Thus for any independently chosen $e_z\in\{1,-1\}$, the signed term equals
\[
 -\frac{2}{n|E|}\sum_{zB} e_z\overline{\widehat\psi(z)}
       \sum_{b:\,s(zb)=-e_z}c(b)\widehat U(zb)+O(1).                  \tag{6}
\]
Subtract $e_z$ from the multiplier throughout each fiber. Only $zb=1$ has multiplier zero before this subtraction. Its cost is $O(1)$ since $\|\psi\|_1\ll|E|$ and $0\le\widehat U(1)\le2n k^{-1}\sum_{j<k}g_j\le2n$, by the true energy telescope from start zero. In particular one may keep just the sign with the smaller absolute *complex sum* in each fiber, after observing the whole prefix. Outside the identity fiber those two absolute values coincide exactly.

If the complementary minority term in (2) is $o(J)$, Cauchy–Schwarz in (6) forces
\[
 \sum_{zB}\min_{a=\pm1}
 \left|\sum_{b:\,s(zb)=a}c(b)\widehat U(zb)\right|^2\gg n^2J^2.       \tag{7}
\]
Indeed $\sum_{zB}|\widehat\psi(z)|^2=|S|\|\psi\|_2^2\ll|S||E|$, and $|E|/|S|$ is bounded below. These are Fourier coefficients of one actual prefix average. A separate second moment for every time is unnecessary. The exponential alternative, the complement minority cost, and the prime upper on (7) remain open. Prescribing an exterior sequence independently of the recurrence does not supply the mask comparison (3).

## Finite physical replay

At $p=769$, take the order-four coset $C=48+96\mathbb Z$ in $\mathbb Z/384$ and its order-eight union $S$ with the subgroup. The actual minus pin with plus companion at $T=10$, start one, allowance $1/20$, cutoff $1/100$, has $E=C\cap P_T=\{48,336\}$. All three mean tests pass, and the contraction on $S$ is below $0.331240$. At $k=8$, the exact normalized history in (5) is $4.228786045\ldots$. Its signed exterior, true mark, and signed minority contributions are respectively $1.525942091\ldots$, $2.691457996\ldots$, and $0.011385957\ldots$. The 384-bit replay solves the adjoint system and checks the true prefix and the mask inequality. This tests the identities at finite size without assuming recurrence at positive asymptotic density or optimizer contact. [Arb checker](astra-fiber-96-check.py) · [Replay](astra-fiber-96-checks.jsonl)

1. For the selected good prefixes estimate the signed positional sum of the time-averaged, eroded exterior in (2), retaining the actual minority correction on the complement. The adaptive-set version (1) gives a test with the plain mask indicator if the other critical sites can be included in the exterior estimate.
2. Bound the maximum restricted first absolute moment of the true prefix-averaged exterior transforms by $\exp(o(J))$ over all prefix lengths through $J$. This relatively weak upper excludes the exponential alternative, even when the individual absolute inputs are too large for the $o(J)$-averaged test in round 95. Neither alternative has yet been excluded on the bounded prime family.
