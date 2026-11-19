# One-time oriented transport and the opposite endpoint's signed tail

There is a one-time alternative to the [adjacent Wasserstein test](astra-late-51.md) at unrestricted collision. A supercritical larger mark forces a linear cost in elapsed time, payable jointly by one-sided scalar transport and the root-orthogonal part of the **actual smaller optimum**. At prime squares the latter vanishes identically, so the transport itself grows at least linearly at every late time. At genuine primes even the first Jacobi sample requires a fixed positive correction to the larger signed affine endpoint model. This precludes controlling the two affine replacement errors independently by vanishing whole-history costs.

## Exact identities at any collision

Keep the cold path and notation of [round 44](astra-critical-44.md). Write $X,\bar X$ for the two actual least-norm endpoints, of signs $\sigma,\tau=-\sigma$, masses $\sqrt n$, and marks $\alpha\ge1$, $\beta=1/\alpha$. Let $P=P_\tau$, $k=(P e_0)_0$, $c=(\beta-1/\sqrt n)/k$, and decompose
\[
 \bar X=J_\beta+R,\qquad J_\beta=j+cPe_0 .
\]
The vector $R\in V_\tau$ has zero mean and zero mark. This is the orthogonal decomposition at the prescribed mean and mark. The affine row can be signed. All endpoint laws below use the true positive rows. For $t\ge1$ put
\[
 h_t=\tau(Pv_t)_0
 =\tfrac12[\tau v_t(0)+\phi_{t-1}(0)-2g_{t-1}/\sqrt n],
 \qquad w_t=\tau Pv_t-h_t Pe_0/k .
\]
Indeed $Kv_t=(I-jj^*)\phi_{t-1}$. At zero set $w_0=0,h_0=0$. The affine oriented mean is exactly $c h_t$; uniformly on the [arithmetic window](vanishing-floor-38.md), $h_t=1+o(1)$ for $1\le t\le D$ since $g_{t-1}\le\sqrt D$. Also $k=1/2+O(1/n)$ from the sector counts, so $c=2\beta+o(1)$ is bounded. Define the signed accumulated tail
\[
 N_t=\sum_{u<t}\langle R,(-\tau v_u)_+\rangle .
\]
The identity $\tau K R=R$ with $R_0=0$ gives $\langle R,\tau v_{u+1}\rangle=\langle R,|v_u|\rangle$. Hence $\langle R,w_t\rangle=2N_t$ and the smaller oriented mean is $\bar m_t=c h_t+2N_t$. In particular the residual charges can have either sign. For the affine row of either sign $s$ and mark $\gamma$, the same sector calculation, now keeping its mean and mark, gives its negative-hinge integral
\[
 \langle J_\gamma,(-s v_t)_+\rangle
 =g_t-\tfrac12\gamma b_t+
     \tfrac12 c_\gamma(h_{s,t+1}-h_{s,t})=g_t-\gamma+o(1)
\]
uniformly for $1\le t<D$. In fact for $\alpha\ge1+\delta$ let $a=1-(1+\delta/2)^{-2}>0$. Since $\sum_{t<D}g_t^2\le D$, at least $aD$ times have $g_t\le1+\delta/2$. Discarding the first $aD/2$ sites in time leaves at least $aD/2-O(1)$ times proportional to $D$ where the larger affine hinge is at most $-\delta/2+o(1)$. Positivity of the actual larger law forces at least $\delta/2-o(1)$ of signed residual correction to that scalar hinge at each such time. This count need not lie inside the last half alone.

Let $U_t$ be the minimum of $E[(x-y)_+]$ between the law of $x=\sigma\sqrt n v_t(i)$ under $X_i/\sqrt n$ and that of $y=\tau\sqrt n v_t(i)$ under $\bar X_i/\sqrt n$. If $W_t$ is their ordinary Wasserstein distance and $m_t,\bar m_t$ their means, then $2U_t=W_t+m_t-\bar m_t$. This follows from $2(x-y)_+=|x-y|+x-y$ under every coupling. Consequently $U_t\ge m_t-\bar m_t$. With $E_t=\|v_t\|^2$, the larger side's exact reserves give
\[
 U_t+2N_t\ \ge\ 2t(\alpha-1)-\alpha B_t+E_t/4+A_t+H_t-c h_t.       \tag{1}
\]
For every fixed $\delta>0$ and every $D/2\le t\le D$ on a subsequence of marks $\alpha\ge1+\delta$, this costs at least $(2\delta-o(1))t$. One late time with $(U_t+2N_t-E_t/4)/t\le o(1)$ through primes suffices. In particular, sublinear one-sided transport and an upper $o(t)$ bound for the smaller residual's signed accumulated tail suffice. This can tolerate growing absolute transport costs.

There is a direction-specific alternative to measuring the signed tail. Put $C_t=\langle v_t,Kv_t\rangle$ and $L_t=\langle R,w_t\rangle_+^2/\|w_t\|^2$, zero if $w_t=0$. Then
\[
\begin{split}
 L_t+2U_t\ \ge\ &4t(\alpha-1)-2\alpha B_t+2(A_t+H_t)
 -2c h_t+h_t^2/k+\sigma C_t/2\\
 &+(\sqrt{L_t}-\|w_t\|)^2 .                                      \tag{2}
\end{split}
\]
Use $\|w_t\|^2=(E_t-\sigma C_t)/2-h_t^2/k$ in (1) and bound $2N_t\le\sqrt{L_t}\|w_t\|$. With the full squared norm $\|R\|^2$ on the left, the square on the right becomes $\|R-w_t\|^2$; using the signed gap $m_t-\bar m_t$ instead of $U_t$ then gives equality. Round 44 gives $C_t=o(1)$ uniformly in the window. Thus sublinear upward transport at a supercritical late time forces at least $(4\delta-o(1))t$ in this specific direction of the smaller optimum. Large collision orthogonal to $w_t$ gives no credit.

At $q=h^2$ the [least-norm square formula](square-endpoint-uniqueness.md) gives $R=0$ exactly. Thus $W_t\ge U_t\ge 2(\alpha-1)t+E_t/4+A_t+H_t-O(1)$ uniformly in the marked window, and $\alpha\to\sqrt2$. For an adjacent late pair this gives $W_t+W_{t+1}\ge[4(\sqrt2-1)-o(1)]t$. The proof uses the actual square optima and needs no polynomial collision hypothesis.

## A nonvanishing affine replacement error through genuine primes

At $t=1$ take either sign $s$, normalized mark $\gamma$, $Z=sY_1=2s\sqrt n Ke_0$ and the 1-Lipschitz hinge $f(z)=(-2-z)_+$. Away from the root the affine density is
\[
 \sqrt n J_\gamma(i)=1-c_\gamma/(2\sqrt n)+c_\gamma Z_i/4
                     =1+\gamma Z_i/2+o(1)
\]
uniformly, by the Jacobi bound and $k_s=1/2+O(1/n)$. At the root $Z_0=-2s/\sqrt n$, so the hinge is zero for large $n$. The oriented bulk Jacobi sample converges to $2\sqrt2\cos\Theta$ for uniform $\Theta$, for either varying sign by symmetry of the [prime arcsine law](fourier.md#joint-distribution-on-the-even-modes). For the larger sign $\gamma\ge1$, and on the support of $f$ the limiting density is bounded above by $1+Z/2$. The true endpoint is positive. Thus its signed residual $R_s=X_s-J_\gamma$ obeys the prime-only restriction
\[
 \liminf_{p}\sum_i \frac{R_s(i)}{\sqrt n} f(Z_i)
 \ \ge\ 2\mathbb E[(-1-\sqrt2\cos\Theta)_+^2]
 =1-3/\pi>0 .                                                       \tag{3}
\]
The last integral is $2\pi^{-1}\int_0^{\pi/4}(\sqrt2\cos u-1)^2du$. If $\alpha\to1$, the smaller sign satisfies the same inequality by $\beta\to1$. Projecting a whole-history Lipschitz test onto its first coordinate preserves its Lipschitz constant. Therefore the actual larger residual against whole-history Lipschitz tests cannot vanish even through primes. This leaves open cancellation **between** the two signed residual laws and scalar tests restricted to late times.

## Reproduction and next tests

The [384-bit checker](astra-transport-52-check.py) uses the two certified active systems or the exact square endpoints, and propagates the actual undamped states through depth 16. It checks the identities at every step, including the full squared mismatch, and integrates the rounded atomic CDFs with outward rounding. Selected enclosures from the [five records](astra-transport-52-checks.jsonl), given to five decimals, are:

| Field | $W_{16}$ | $U_{16}$ | Smaller $N_{16}$ | Larger seed hinge correction |
|---:|---:|---:|---:|---:|
| 101 | 1.05049 | 1.05049 | .04705 | .03336 |
| 173 | .53915 | .10959 | .48259 | .03970 |
| 401 | .20411 | .13000 | .32083 | .04214 |
| 121 (square) | 7.90692 | 7.90692 | 0 | .08196 |
| 961 (square) | 11.78354 | 11.78354 | 0 | .11127 |

These fixed-field values do not establish late-window prime asymptotics. The full ETH26 limit is open.

1. Estimate the minimum over the late window of $(U_t+2N_t-E_t/4)/t$ on actual prime optima. A nonpositive limsup through all primes proves the limit by (1). A subsequence with a positive lower bound for the late minimum rejects that estimate. The upper signed tail may be used directly, including cancellations.
2. For a fixed proposed excess $\delta>0$, test whether some late $t$ has $(L_t+2U_t)/t\le4\delta-\eta$ for a fixed $\eta>0$ through primes. Equation (2) excludes a subsequence there with excess at least $\delta$. Doing this at every fixed $\delta$ suffices. An unbounded prime subsequence with late minimum tending to $4\delta$ or above defeats the strict margin at that tolerance. In estimating $U_t$, independent whole-history $o(1)$ replacement bounds have already been refuted by (3).
