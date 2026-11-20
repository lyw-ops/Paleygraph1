# Exterior forcing of recurrent heights on a critical coset

The two nearly saturated cosets in a trapped prime sequence can be removed from the input of the Jacobi transform together. Their entire internal nonlinear feedback is a strict contraction. The resulting sufficient estimate involves only the signed transform of the **true exterior activation**. There is a sharp obstacle to bounding this transform by an unweighted approximation error. On the very same prime matrix, a nonnegative exterior error of order $D(p)n^{-1/4}$ in supremum norm can sustain opposite order-depth heights on two fixed positive fractions of a critical-size coset. The obstacle concerns prescribed exterior data. The true zero-start orbit has only its one marked source.

## A restricted estimate for the actual good terminal times

Write $G=\widehat Q$, $n=(p-1)/2$, $\mathsf K=F\operatorname{diag}(s)F^{-1}$, $s(z)=\chi(1-z)$, and $x=\sqrt n\,\mathsf K e_0$. The complete Jacobi bound is $|\mathsf K_{ik}|\le\mu=\sqrt p/n$. Let $C$ be a self-inverse coset of a subgroup $H$, and $L=H\cup C$. Fix one real primary optimizer of mark $a$, $\gamma=\sqrt n a\ge1+\delta$, and use the bounded list at a fixed shortfall mass from [round 94](astra-quotient-94.md). One may filter the list by $a|L|\le 1/2$ *before* selecting a pin. Indeed every trapped selected sequence has $(1-o(1))a|L|\le\Theta_\sigma(L^\perp)/|L^\perp|\le1/\sqrt5$ by [round 93](astra-coset-93.md) and round 94, so its actual candidate passes eventually. The contact and occupancy comparison of round 94 applies to the filtered maximum by the same selected-sequence argument. On this list $|L|\asymp_\zeta\sqrt n$ since the optimizer puts fixed mass on $C$ under its point cap. We may take $S=L$ in everything below, or $S=C$ if its single-coset version is preferable. Put $m=|S|$.

With $P_S$ the coordinate restriction/zero extension, let $M=(\mathsf K_{ik})_{i,k\in S}$ and $\kappa=\sum_{k\in S}|\mathsf K_{ik}|$ for any $i\in S$. This sum is constant on $S$, since $S$ is a coset and the kernel is translation invariant. All three operator norms on $\ell^1(S),\ell^2(S),\ell^\infty(S)$ are bounded by $\kappa$, and
\[
 \kappa\le\mu m\le(1+o(1))/(\sqrt2\gamma).
\]
Thus the gap from one is absolute. On an individual trapped sequence one has the sharper $\limsup\kappa\le\sqrt{2/5}/(1+\delta)$ also for $S=L$.

Set $J=\lfloor D(p)/8\rfloor$. Let $\mathcal T\subset[\lceil J/2\rceil,J-2]$ consist of the actual terminals with all three adjacent $g$ at most four. It has size at least $J/4$ eventually. The genuine cold recurrence, including its field-dependent marked scalar, reads
\[
 y_{j+1}=M|y_j|+d_j+\beta_j x|_S,\quad y_j=Y_j|_S,\quad
 d_j=(\mathsf K 1_{S^c}|Y_j|)|_S,\quad y_0=0,\quad 0\le\beta_j\le2.
 \tag{1}
\]
Here and below $\mathsf K 1_{S^c}|Y_j|$ means the transform of $1_{S^c}|Y_j|$. One may discard a different set $A_j\subset S^c$ of at most $H_p^2$ sites in each $d_j$, where $H_p\ge2$ and $\log_2^*H_p\le(7/8-\xi)\log_2^*p$ for fixed $0<\xi<7/8$. Denote the resulting field by $d'_j$. The actual finite Mellin approximants through $J+1$ have supremum $U\le p^{1/8}$ and normalized second error $e=o(1/H_p)$, with $H_p\le\log_2\log_2p$ eventually. Hence $\|d_j-d'_j\|_\infty\le\mu(H_p^2 U+H_p\sqrt n\,e)=o(1)$ simultaneously, even for adaptive erasures. [Arithmetic window](terminal-height-79.md) · [Approximation with the actual scalar](trimmed-mellin-77.md)

Use $F_j=m^{-1}\sum_{i\in S}|d'_j(i)|$ and $V_k=\sum_{0\le j<k}\kappa^{k-1-j}F_j$. From (1) and $\|x\|_\infty\le\sqrt{p/n}$ one gets $\mathbb E_S|Y_k|\le O(1)+V_k$. At a good terminal $T$, the exact three-time formula on the exterior gives
\[
 |Z_{\sigma,T}(i)|\le2+\tfrac14|Y_{T-1}(i)|+\tfrac12|Y_T(i)|+
 \tfrac14|Y_{T+1}(i)| \quad(i\ne0).
\]
Indeed the scalar is $(g_T-g_{T-1})/2$ and at each neighbor the two unsigned coefficients have magnitude $1/4$ on disjoint sign parts. At the center the coefficient is $1/2$. Set $w_{-1}=w_1=1/4$, $w_0=1/2$. At any fixed $u,\rho>0$ and on either sign,
\[
 \Pr_C\!\left\{i\ne0:\ \frac{\#\{T\in\mathcal T:Z_{\sigma,T}(i)>uJ\}}{|\mathcal T|}\ge\rho\right\}
 \le \frac{|S|}{|C|}\frac{O(1)+|\mathcal T|^{-1}\sum_{T\in\mathcal T}
                               \sum_{v=-1}^{1}w_v V_{T+v}}{\rho uJ}.       \tag{2}
\]
This is Markov's inequality in time and space, with the exterior indicator retained so that no projected marked height enters. Thus an $o(J)$ bound for the displayed weighted forcing average suffices. A simpler sufficient condition is $\sum_{j<J}F_j=o(J^2)$, since each $F_j$ has total time weight at most $1/(1-\kappa)$ before the division by $|\mathcal T|$. Either bound, uniform on the filtered bounded list, removes the trapped alternative at one admitted pin for the specified positive mass by [round 94, (2)](astra-quotient-94.md). Neither bound is established for the true exterior fields.

One can also move an arbitrary square-root-sized set of sites into the contracted part at **each** time. Choose any fixed $\kappa_0$ strictly between $1/\sqrt2$ and one, and arbitrary $S_j\supseteq L$ of size at most $\kappa_0/\mu$, possibly chosen from the entire true history. In (1) the internal matrix becomes $\mathsf K_{S_{j+1},S_j}$. Its norm between the two *normalized* first-norm spaces is at most $\mu|S_j|\le\kappa_0$, since each input site contributes at most $\mu$ times its amplitude to the output mean. Replace $F_j$ by the mean absolute exterior transform on $S_{j+1}$ with source outside $S_j\cup A_j$, and replace $\kappa$ by $\kappa_0$. The same proof gives (2) with prefactor $\max_j|S_j|/|C|=O_\zeta(1)$. This permits tracking $c\sqrt n$ additional sites through changing locations, for a fixed positive $c$. The larger target mean must be tested on those sites too. The remaining tower-sized $A_j$ need no such tracking.

For the original fixed coset $S$ there is a test directly in positional variables. Write $S=cH'$ and $B'=(H')^\perp$, take $v_j=1_{(S\cup A_j)^c}|Y_j|$ and $\widehat v_j(z)=\sum_i v_j(i)\overline{i(z)}$. Then
\[
 \mathbb E_S|d'_j|^2=n^{-2}\sum_{zB'\in Q/B'}
   \left|\sum_{w\in zB'}s(w)c(w)\widehat v_j(w)\right|^2 .                \tag{3}
\]
This follows by orthogonality on $H'$. A bound $o(n^2J^3)$ for the double sum on the right before normalization and summed over $j<J$ suffices by Cauchy–Schwarz. Both whole saturated cosets and the independently chosen erasures are already absent from $v_j$.

## Sharp error scale for nonnegative exterior activation

The following statement uses the actual prime Jacobi matrix, its identity $\mathsf K^2=I-\mathbf1\mathbf1^*/n$, and even data. It prescribes the input on $S^c$ independently of the full Picard recurrence. Suppose $m\asymp\sqrt n$, $S=-S$ is a coset, $\kappa\le\kappa_*<1$, and let $C=S$ or its distinguished self-inverse half as above. There is one even $e\ge0$ supported outside $S$, with $\|e\|_\infty\ll_{\kappa_*}\sqrt{m/n}$, for which the exact restricted update
\[
 z_0=0,\qquad z_{j+1}=M|z_j|+j(\mathsf K e)|_S+\beta_j x|_S                \tag{4}
\]
has two fixed sets of positive relative size in $C$. On the respective sets $\pm z_T(i)\gg_{\kappa_*} J$ simultaneously for every $J/2\le T\le J$, for sufficiently large $J,n$. The sets can be chosen after the bounded scalars $\beta_j$ are specified. This includes the true scalar sequence as a choice in (4). The exterior amplitudes $je$ are $O(J\sqrt{m/n})=o(1)$ throughout the arithmetic window.

Here is the construction with the sharp scale. Choose independent fair signs on the inversion orbits of $S$, and let $\eta$ be the resulting array, zero outside $S$. For $h=\mathsf K\eta$, each $h(i)$ is a Rademacher sum. Its sum of squared coefficients is at most $2m\mu^2\ll m/n$, including the fixed inversion points. The product bound $\prod\cosh(t a_k)\le\exp(t^2\sum a_k^2/2)$ gives subgaussian tails by the exponential Markov inequality. Consequently for $A=B\sqrt{m/n}$,
\[
 \mathbb E\|h-\operatorname{clip}_{[-A,A]}h\|_2^2\ll m e^{-cB^2},
 \qquad \mathbb E\,\mathbb E_S|h|^2\ll m/n .
\]
The first norm is full counting norm. Chebyshev's inequality gives at least $|C|/3$ of each sign on $C$ with probability tending to one, using inversion orbits of size at most two. For any fixed small $\varepsilon>0$, first choose $B$ large, then $n$ large. Markov's inequality gives one simultaneous choice with the clipped error norm at most $\varepsilon\sqrt m$, the local RMS of $h$ at most $\varepsilon$, and both sign counts as stated.

Put $e=1_{S^c}(A+\operatorname{clip} h)$ with clipping at $\pm A$, $d=(\mathsf K e)|_S$ and $\lambda=\sum_{k\in S}\mathsf K_{ik}$, independent of $i\in S$ with $|\lambda|\le\kappa$. In local RMS norm $\|\cdot\|_S$, one has $\|d-\eta|_S\|_S\le\varepsilon+m/n+2\kappa A$. In fact $\mathsf K h=\eta-\bar\eta$, $|\bar\eta|\le m/n$, $\mathsf K$ kills the constant $A$, the full clipping error is contractively transported before restricting, and removing its local input costs at most $2\kappa A$. Also $M\eta|_S=h|_S$. The vector $z_*=\eta|_S+\lambda$ satisfies $|z_*|=1+\lambda\eta|_S$. It solves the frozen equation $z=d+M|z|$ up to RMS error at most $(1+\kappa)\varepsilon+m/n+2\kappa A$. This equation has a unique solution $z$ by strict contraction, with RMS distance to $z_*$ bounded by that residual divided by $1-\kappa$. Taking $\varepsilon$ sufficiently small ensures $\pm z>(1-\kappa_*)/2$ on respectively a fixed fraction of $C$ (the loss in a fraction of $S$ costs at most two times that fraction on $C$).

Since $\|z\|_S=O(1)$, (4) gives $\|z_{j+1}-(j+1)z\|_S\le\kappa\|z_j-jz\|_S+O(1)$, hence uniform $O(1)$ error. By summing Chebyshev bounds over $T\in[J/2,J]$, an $O(1/J)$ fraction of $C$ suffices to remove all errors exceeding $(1-\kappa_*)T/4$ at any of those times. The remaining two sets prove the claim. Conversely, any prescribed exterior sequence with supremum $o(J\sqrt{m/n})$ through the entire window has restricted transformed RMS $o(J)$ by full $\ell^2$ contraction. Equation (1) and the geometric sum give $o(J)$ restricted RMS throughout. The same bound controls discrepancies between two restricted recurrences at a common marked scalar. Thus the exterior supremum scale for fixed-density order-depth *local states* is sharp up to constants. For the direct companion projector, the same construction gives $(J_0+P_\sigma)e|_S=(\bar e+\sigma d)/2$, where $J_0$ projects onto constants. It too takes order-one values of both signs on positive fractions of $C$ from this small exterior input.

## Finite replay and next tests

At $p=97$, $C=\{0,16,32\}$ passes the round-94 primary mass test $7/50$. All fifteen times $16,\ldots,30$ pass the three-neighbor mean test in a finite horizon $32$. With start one, allowance $1/20$ and cutoff $1/100$, neither exterior site belongs to a physical mask at any of those times. The maximum of their true plus companion heights is between $0.057059438$ and $0.057059439$. The checker rebuilds the actual local and exterior terms at every update. At $p=12289$, on the separate order-32 coset of offset 96, the certified contraction is below $0.313012$. The prescribed exterior ramp in (4) with zero marked forcing gives all 16 sites of each sign beyond $\pm40$ at time 80. This second replay checks only the error construction. [Arb384 checker](astra-recur-95-check.py) · [Two replay records](astra-recur-95-checks.jsonl)

1. Estimate (3) for the true exterior input using cancellation within the positional fibers. An average saving on the exact good-time weights of (2) suffices and can be tested with arbitrary time-dependent erasures of the stated size.
2. If the second moment is dominated by exceptional heights, test the restricted first absolute moment $F_j$ directly on the same true transforms. The sharp construction shows why supremum control of the *untransformed* exterior activation at an inverse power of the marked depth alone cannot supply this estimate. The recurrent prime bound and the ordinary theta limit remain open.
