# The optimal-face quantile LP and a prime obstruction to packing its tails

The combined cost in [round 52](astra-transport-52.md) is a single integrated maximum of two scalar quantiles, up to the known affine term. Its best value over both entire optimal faces is a linear program with one extra variable per distinct score threshold. Optimizing the faces separately at each time is permitted. On the first actual prime Jacobi sample, a plausible relaxation of this LP loses a fixed amount of the smaller endpoint's tail probability on **every** eligible prime sequence. The obstruction persists with simultaneous Fourier frame packings of dimension growing almost to square-root scale. No prime-uniform bound for the late minimum is established.

## One-time optimal-face program

Use the round-52 notation. Put $z_i=\sigma\sqrt n v_t(i)$ for the larger sign, and let $x=z_i$ under $X_i/\sqrt n$, $y=-z_i$ under $\bar X_i/\sqrt n$. Write $Q_x,Q_y$ for the increasing quantiles. Since increasing quantiles minimize the absolute difference, they also minimize the upward cost. Using $2N_t=E y-c h_t$ gives the equality
\[
 U_t+2N_t=M_t-c h_t,\qquad
 M_t=\int_0^1\max(Q_x(u),Q_y(u))\,du.                           \tag{1}
\]
Indeed $(x-y)_++y=\max(x,y)$. In particular $M_t\ge E x$. The round-44 identity tested on the larger row now reads
\[
 M_t-E_t/4=(2t-B_t)(\alpha-1)-B_t+A_t+H_t
                +\int_0^1(Q_y-Q_x)_+\,du.                         \tag{2}
\]
Every actual optimal pair satisfies these formulas. At a nearly equal pair a positive linear contribution from either reserve or the reverse quantile cost can defeat this window. Equation (2) identifies the three nonnegative costs separately; it does not establish such a late obstruction.

Take any certified complementary optimal pair and, for each sign $s$, let $S_s$ be the root and all bulk zeros of the opposite row. The full optimal face consists exactly of probability laws supported on $S_s$ with Fourier coefficients zero on its forbidden positional mask. This follows by pairing with the fixed opposite optimum at mean one, as in the [optimal-face identity](endpoint-norm.md). This also proves the forward inclusion for asymmetric optimizers. Write $a_0<\cdots<a_K$ for the union of the possible scalar sites $z_i,-z_i$. Compute
\[
 M_t^{\rm face}=a_0+\min\sum_{k=0}^{K-1}(a_{k+1}-a_k)u_k ,
 \qquad
 u_k\ge\mu_+\{z>a_k\},\quad u_k\ge\mu_-\{-z>a_k\}.              \tag{3}
\]
Here $\mu_+,\mu_-$ indicate the larger and smaller faces in that order and are variables in their respective faces. The survival probability of the maximum under the increasing coupling is the larger of the two survival probabilities at every threshold, proving (3), including atoms. This uses only $O(n)$ scalar variables and thresholds. In particular one cannot generally interchange the minimum over rows with a separate minimum at each threshold. Even rows suffice since the site scores are even.

At each time (3) can use different optimizers, because (2) holds for the selected larger row on its whole prefix and $A_t,H_t\ge0$. Hence a single late time on each prime with $(M_t^{\rm face}-E_t/4)/t\le o(1)$ proves ETH26. The bounded affine term in (1) is immaterial at these times. A feasible primal upper bound suffices. A certified dual lower bound of $\eta t+E_t/4$ for some $\eta>0$ at every late time on an unbounded prime subsequence refutes the proposed face-window upper estimate, even if a different proof still establishes the ordinary limit.

## What a local upper-tail packing can and cannot see

For sign $s$, let $A\subset Q$ consist of $d$ positions whose pairwise nonidentity ratios all belong to the forbidden mask. Set $b_i=(i(a))_{a\in A}$ for the character indexed by $i$. Every endpoint probability $\mu$ satisfies
\[
 \sum_i\mu_i b_i b_i^*=I_d,\qquad \mu_i\le\gamma/\sqrt n,
                                                                    \tag{4}
\]
where $\gamma$ is the normalized optimal mark. The diagonal uses total probability and the off-diagonals are forbidden Fourier coefficients. The point cap follows by translating the row. The [prime run lemma](quadratic-fourth.md#unbounded-allowed-energy-with-vanishing-residual) supplies such an $A$ of size $1+\lfloor(\log_2 p)/4\rfloor$ for each sign via consecutive powers.

For a set $S$, relax its mass upper bound by maximizing $\sum_{i\in S}w_i$ on nonnegative weights supported on $S$, imposing the point cap, mass at most one and $\sum_i w_i b_i b_i^*\preceq I_d$ for every selected frame. Call this packing value $C_s(S)$. Restricting any true law to $S$ proves it is an upper bound for its tail mass. One may intersect $S$ with the certified allowed face when known. Thus integrating the larger of the two upper capacities over thresholds bounds (1) from above. A simple lower certificate for the relaxation itself uses the uniform law on nonempty $S$. If its largest forbidden Fourier coefficient in absolute value is $\eta$, Gershgorin gives simultaneously for every frame of size at most $d$,
\[
 C_s(S)\ge \min\{\gamma |S|/\sqrt n,\,[1+(d-1)\eta]^{-1}\}.        \tag{5}
\]
The input is an actual subset of scores. Equation (5) also applies on a known face after changing $S$ accordingly.

**Prime seed obstruction.** Take the support-unrestricted version of this tail relaxation. For any fixed $-M<r<M$, $M=2\sqrt2$, let $S=\{i\ne0:sY_1(i)>r\}$. Through eligible primes,
\[
 C_s(S)\longrightarrow1
 \quad\text{even for all forbidden frames of size } d_p=o(\sqrt p)
 \text{ simultaneously}.                                        \tag{6}
\]
The sign can vary with $p$. Choose $M_p=2\sqrt{p/n}$, so $|sY_1|\le M_p$. Tilt uniform probability by the nonnegative weight $(1+sY_1/M_p)^k$ and normalize to a probability $\pi_k$. At any fixed integer $k$ its normalizer tends to a positive constant by the [prime arcsine law](fourier.md#joint-distribution-on-the-even-modes), and $\|\pi_k\|_\infty=O_k(1/n)$. Every nontrivial positional Fourier coefficient of $\pi_k$ is $O_k(p^{-1/2})$, uniformly in the position. Indeed the [fixed-expression Fourier inversion](iteration-parity.md) applied to each seed monomial gives a bounded-rank normalized convolution trace lisse away from 1, with normalized inverse coefficient $O_k(p^{-1/2})$ there. The bounded exceptional characters cost $O_k(p^{-1})$ and the constant monomial has zero coefficient. This is the polynomial version of the [opposite pairing estimate](negative-pairing.md#the-true-iteration-against-bounded-degree-fej%C3%A9r-tests).

Consequently the frame Gram matrices for $\pi_k$ are all bounded by $(1+O_k(d_p/\sqrt p))I$. Divide by this upper factor and restrict to $S$, which preserves each PSD bound. The point cap holds eventually since $\gamma$ is bounded below by the reciprocal of the uniform Jacobi mark bound. For each fixed $k$, the limiting surviving mass is the proportion above $r$ under the arcsine law tilted by $(1+z/M)^k$. It tends to one as $k\to\infty$ because any interval strictly between $r$ and $M$ has positive arcsine mass and larger exponential weight than the entire lower interval. Removing the root costs $O_k(1/n)$. Taking the field limit first proves (6).

In contrast, for the true smaller sign $E(sY_1)=2(\beta-1/\sqrt n)\le2$ exactly by $v_1=2Ke_0$ and sector orthogonality. Since $sY_1\ge-M_p$, for every fixed $2<r<M$ its true probability above $r$ has limsup at most $(M+2)/(M+r)<1$. This is an unconditional gap, without any hypothesis on endpoint collision or mark convergence. On a subsequence with $\alpha\to1$ both means tend to 2 and the actual common-quantile envelope itself has
\[
 \limsup M_1\le M-(M-2)^2/(2M)<M .
\]
Indeed the two deficits $M_p-Q_x,M_p-Q_y$ are comonotone in $[0,2M_p]$. Their expected minimum is at least their expected product divided by $2M_p$, and the expected product is at least the product of the expectations. Integrating the relaxed capacities instead tends to $M$ by (6) and bounded convergence. This seed obstruction concerns local packings with discarded complementary mass. It leaves the late face LP open.

For a **common full probability** the trace in (4) is already $d$, so the matrix inequality forces equality. All two-point forbidden frames together then recover every Fourier zero. Thus a feasible local packing of mass $1-o(1)$ need not have a positive completion with the prescribed optimal mark. One inexpensive way to keep part of this missing information is to impose the exact moment equations for the complementary mass too. For every true sign $s$,
\[
 E_{\mu_s}\{sY_{u+1}-|Y_u|\}=\gamma b_u-2g_u.
\]
This follows from the sector equation and the root injection. Any **nonnegative** shift of a linear combination of these increment tests has known total expectation, hence bounds its integral on each restricted submeasure. The first such constraint using $M_p+sY_1$ recovers the strict smaller-side tail gap above. Later increments are simultaneously available, without a bound on the density.

## Replay and ranked tests

The [320-bit replay](astra-tail-53-check.py) independently integrates the two survival functions at rounded sites with their errors, verifies the Fourier zeros of the certified prime endpoints, the comonotone deficit bound at the seed, and records (5) from actual threshold sets for every frame of dimension at most four. At depth 16 the quantile envelopes are 2.33751, 2.66625, 2.47224 at primes 101, 173, 401, respectively. These [three finite checks](astra-tail-53-checks.jsonl) do not certify a late prime limit or numerical optima of (3) on a degenerate face.

1. Bound the optimal-face LP (3) at one growing late time through primes, retaining $E_t/4$. A primal feasible objective satisfying the stated upper estimate suffices. Uniformly positive normalized dual lower bounds at all late times on an unbounded prime subsequence falsify this estimate.
2. For upper-tail capacity bounds retain support and the known cold increment moments of a full completion. Test the actual positive-score tails against (5) first. If its integrated lower certificate already exceeds the energy allowance by $\eta t$ throughout the late window along unbounded primes, the proposed local packing bound fails at that window. The seed already rules out expecting support-free subprobability packings to resolve the entire history. ETH26 remains open.
