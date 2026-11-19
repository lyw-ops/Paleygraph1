# Short bulk jumps suffice for the true charged minima throughout a growing prime window

Let $p\equiv1\pmod4$ be prime, $Q=\mathbb F_p^{\times2}$, $G=\widehat Q$, and $n=|G|=(p-1)/2$. For a primitive generator $b\in Q$, index each site $i\in G$ by the integer $0\le k_b(i)<n$ with $i(b)=e^{2\pi i k_b(i)/n}$. Fix *any* two reference optima, one per sign. The following directed dictionary fixes the root and allows any nonnegative plan on the reference bulk, with target sites on the same exposed face, provided
\[
                    |k_b(i)-k_b(j)|\le R
\]
on each edge. The distance here is along the cut interval. Circular distance also works. Every target must satisfy its full original sector equations. An intermediate site with no net change may both receive and send mass, up to its original budget. The edge itself may cross an opposite exposed site.

**Theorem.** Fix $0<\epsilon<1/4$. At all sufficiently large eligible primes, a proportion $1-o(1)$ of all primitive generators $b$ have the following property. With $R=\lceil n^{3/4+\epsilon}\rceil$, *the same generator for both signs and all times* attains the unrestricted minimum
\[
            M_t^{\rm face}-E_t/4
\]
in this dictionary at every integer in the entire late window $D(p)/2\le t\le D(p)$. Different target pairs can be chosen at different times. At each time the target is a single pair of actual rows for its entire quantile integral. The exceptional proportion is $O(n^{-\epsilon+o(1)})$, uniformly in the reference pair. No factorization condition on $n$ is needed. This is equality of the optimal values, without an estimate yet of their normalized limit.

## A common order from the actual point caps

For every probability $w$ on $G$ write $d_b(w)$ for the supremum of the absolute difference between $w(I)$ and $|I|/n$ over cyclic intervals in the $b$ order. An explicit finite upper estimate is
\[
 \mathbb E_{b\ \rm primitive} d_b(w)
 \ \le\ A_n\|w\|_2,\qquad
 A_n=(1+\log n)\sqrt{n/\varphi(n)}
                    \sum_{d\mid n}d^{-1/2}=n^{o(1)}.             \tag{1}
\]
Indeed the normalized Fourier coefficient of an interval at $h\ne0$ is at most $1/(2\min(h,n-h))$ in modulus, by its geometric sum and the sine bound. This is uniform in both endpoints. The point $b^h$ runs uniformly over all elements of order $n/e$, $e=\gcd(h,n)$, since reduction of units modulo $n/e$ is surjective. Parseval gives
\[
 \mathbb E_b|\widehat w(b^h)|\le
        \sqrt{n/\varphi(n/e)}\,\|w\|_2
 \le\sqrt{ne/\varphi(n)}\,\|w\|_2 .
\]
Summing the geometric coefficients, pairing $h,n-h$ and using
$\sum_{h\le n}\sqrt{\gcd(h,n)}/h\le(1+\log n)\sum_{d\mid n}d^{-1/2}$ gives (1). The divisor count and $n/\varphi(n)$ are $n^{o(1)}$, for instance by their elementary prime products.

For a true row $\mu$ let $q=\mu(0)$ and $w=(\mu-q\delta_0)/(1-q)$. The [point cap and Jacobi bound](astra-critical-44.md) give $\mu_i\le q=O(n^{-1/2})$, so $\|w\|_2\le\sqrt{q/(1-q)}=O(n^{-1/4})$. For any collection of $K$ rows, Markov bounds the proportion of orders in which even one conditional bulk row has discrepancy greater than $a$ by $A_n\sum_w\|w\|_2/a$. Take the two references and one actual minimizing pair at each of the $O(D)$ times (the compact faces attain their minimum). With $a=(R-2)/(2n)$ and $D=O(\log^* p)$ the exceptional proportion has the stated order.

To see exactly what this supplies, take $u$ uniform on $(0,1)$. If the quantile site of the position under $w$ is $k$, then
\[
        k/n-d_b(w)\le u\le(k+1)/n+d_b(w).
\]
This follows by taking the two prefixes ending just before and just after $k$. Coupling the two position quantiles therefore moves the conditional bulks by at most $n(d_b(w)+d_b(w'))+1$ sites. Append a stationary root-to-root atom of mass $q$, which is the same for any two optima on one face. This is a direct coupling supported on the permitted edges, so it preserves the target score law at every threshold. It allows both directions and source-dependent jumps. A flow forced to retain all common bulk mass at each site can require longer jumps.

## Predetermined arithmetic orders for arbitrary changes on the exposed supports

For each sign $s$, there are also orders that work simultaneously for *every pair* of optima on that face, chosen before the reference, target and time. Fix any $0<c<1/2$, $m=\lfloor c\log_2 p\rfloor$. There are
\[
                 (1+o(1))\,\varphi(n)2^{-m}
\]
primitive $b\in Q$ for which $b^j$ belongs to the forbidden mask for $1\le j\le m$. To check primitivity in the [prime run argument](quadratic-fourth.md), sieve the subgroups of index $d\mid n$ with Möbius weights. On each subgroup the count is $(n/d)2^{-m}+O(m^2\sqrt p)$. Indeed, expand its indicator in multiplicative characters of $\mathbb F_p^\times$ with coefficient absolute sum one. For a nonempty set of selected factors $1-X^j$, a primitive root of unity of the largest selected order is simple there and is absent from the others since $j<p$. Its exponent in the character product is $(p-1)/2$ for a primitive multiplicative character, independently of the twist at zero. Thus the distinct-root form of the usual multiplicative Weil bound costs $O(m^2\sqrt p)$, uniformly in $d$. Removing roots costs $O(m^2)$. The total sieve error is $O(2^{\omega(n)}m^2\sqrt p)=p^{1/2+o(1)}$, strictly smaller than the main term. Inversion gives the same zeros for negative $j$. [Weil's character-sum bound](https://pmc.ncbi.nlm.nih.gov/articles/PMC1079093/)

In any such order the phases of every whole row have vanishing first $m$ circular Fourier moments. Their discrepancy from uniform arclength on arcs is $O(1/m)$. Here is an elementary argument. The continuous Fejér kernel of order $L\asymp m/2$, of degree $L-1$ and integral one on the unit circle, has value at least a constant times $L$ on $|u|\le1/(4L)$. All its translates integrate to one against the row. Covering an arc by such intervals bounds its row mass by $O(|I|+1/L)$. The probability density proportional to the square of that kernel has degree at most $m$ and first absolute circular moment $O(1/L)$. Its normalizer is comparable to $L$, and the normalized density is $O(\min(L,L^{-3}|u|^{-4}))$. Adding an independent sample from it sends the row to Haar measure by the Fourier zeros. A shift $u$ changes membership in an arc only within two intervals of length at most $|u|$ at its boundaries. Integrating the preceding arc bound now gives $O(1/m)$ discrepancy, uniformly over all arcs. The discrete uniform arc measure differs from arclength by $O(1/n)$ with boundaries placed between adjacent sites. Deleting the root and renormalizing costs at most $q$ in total variation. The quantile coupling above consequently reaches *every* optimum with radius $O(n/\log p)$ in each such predetermined sign-specific order.

Delete zero sites from the cyclic sign pattern of a nonzero true difference $h$. The remaining sequence has at least $2m+2$ sign changes in *every* corresponding forbidden-run order. Indeed if it had $2r\le2m$ changes, put a point in each intervening gap. The product of $2r$ factors $\sin(\pi(u-u_j))$ is a real trigonometric polynomial of degree $r$ on the circle. Choose its sign so that it agrees strictly with $h$ at every nonzero site. Pairing must give zero by the Fourier zeros and zero mass, whereas every term is positive. The constant case is excluded already by zero mass. Thus arbitrary site-conditioned transfers with at most $m$ runs of net donors after deletion of neutral sites have zero divergence, for every sufficiently large eligible prime and every time. Positive circulations can have zero divergence. These order constraints permit substantial changes that interlace on the actual supports.

## An upper estimate with the terminal energy retained

Let $Z_s(i)=s\sqrt n v_t(i)$, $q_s$ its face's root mass, and $S_s$ the root plus zeros of any fixed opposite optimum. For one true pair having bulk discrepancies $d_s$ in chosen orders, set $r_s=\lceil nd_s+1\rceil$. For the uniform index $j=0,\ldots,n-1$ take $U_s(j)$ and $L_s(j)$ to be the maximum and minimum of $Z_s$ over $i\in S_s\setminus\{0\}$ with $|k_{b_s}(i)-j|\le r_s$. The quantile coupling to the uniform grid guarantees a nonempty set at every $j$. Define the two bounding laws on each sign by appending the **exact** root atom of mass $q_s$ at $Z_s(0)$ to $1-q_s$ times the uniform law of $U_s(j)$ or $L_s(j)$. Denote their increasing quantile functions by $Q_s^U,Q_s^L$. Stochastic order under this coupling yields
\[
 \int_0^1\max_s Q_s^L(u)\,du-E_t/4
 \ \le\ M_t(\mu_+,\mu_-)-E_t/4
 \ \le\ \int_0^1\max_s Q_s^U(u)\,du-E_t/4 .                         \tag{2}
\]
Both inequalities apply to one and the same true pair throughout the integral. A certified or universal discrepancy upper bound may replace $d_s$. In the arithmetic run orders a universal radius encloses the full-face minimum on both sides. For the adaptive orders an upper estimate only requires bounding a single actual pair's discrepancies, directly from its prefix sums if available. The lower bound for a single reference need not hold for the full minimum. Formula (2) is a score test on the actual exposed support. The arithmetical results do not bound the widths of its local score ranges. The charge is subtracted once after integrating the common maximum.

The upper envelope in the common random orders has an arithmetic limitation at every growing-window time. Put $k=\lceil n^{1/2-\epsilon}\rceil$, and let $z_{s,k}(t)$ be the $k$-th largest oriented score on the bulk of the exposed support. There are at least $k$ such sites eventually by the true cap. Choose $k$ distinct sites attaining the top scores, breaking ties arbitrarily. The uniform law on these sites has norm $k^{-1/2}$. Apply (1) to the $O(D)$ such laws at both signs and all late times. For a proportion $1-O(n^{-\epsilon/2+o(1)})$ of the common orders, every one of these laws couples to the uniform index grid with distance at most $R=\lceil n^{3/4+\epsilon}\rceil$. In those orders **every** local upper envelope of radius $R$ is at least $z_{s,k}(t)$ on the entire grid. Its own charged upper endpoint in (2) therefore satisfies, uniformly across the window,
\[
           \int_0^1\max_s Q_s^U(u)\,du-E_t/4
                   \ \ge\ \max_s z_{s,k}(t)-E_t/4-o(1).           \tag{3}
\]
Indeed the mean of either upper law is at least $(1-q_s)z_{s,k}+q_s Z_s(0)$. If $z_{s,k}>0$, the $k$ top sites give $kz_{s,k}^2\le nE_t$, so $q_s(z_{s,k})_+=O(\sqrt{t/k})=o(1)$. The protected root gives $|q_s Z_s(0)|=o(1)$ by the [marked window](vanishing-floor-38.md). Thus locality at this radius suffices for exact transport of the optimizers while coordinatewise maximization within these same neighborhoods replaces even rare upper levels of size $n^{1/2-\epsilon}$ by full bulk mass. A large value in (3) rejects that neighborhood-maximization bound in almost every order. Actual transport keeps the target weights.

## An exact finite check and two ranked tests

The [checker](astra-charged-61-check.py) enumerates the four true even plus vertices at $97$ over the cyclotomic field from the [complete face systems](astra-face-54.md). The even minus face is a singleton. Cutting at the root, the maximum bulk monotone transport radius between any two vertices equals 4 at the two generator powers $23,25\bmod48$, versus 5 in the original coordinate and 10 in the worst order. These vertex bounds hold for every pair in the full even polygon. Mix the vertex-to-vertex coupling for each independent pair of barycentric indices. Conversely one extremal vertex pair needs the stated maximal radius for nonwrapping transport, since increasing quantiles minimize the maximum line distance (the prefix inequalities are necessary for every radius-limited coupling). Thus from any even reference one can attain every optimal score law with jumps at most four at this field. Evenization preserves all cold scores. This finite check does not sample a growing prime window. The [record](astra-charged-61-checks.jsonl) is reproduced by running `.venv/bin/python -B research/astra-charged-61-check.py`.

1. Use the radius-$n^{3/4+\epsilon}$ dictionary in one common primitive order with the exact exposed supports, Fourier equations and root. An actual common-row trial with charged objective $o(t)$ above zero at one late time through all primes proves the desired upper estimate. Conversely, on unbounded primes it suffices that a fixed positive fraction of orders each has a charged lower barrier $\eta t$ throughout the late window. Such orders must intersect the $1-o(1)$ fraction realizing the true minima simultaneously.
2. For the score-envelope test, use the actual support and both exact root atoms in (2). A nonpositive normalized limsup of the upper endpoint at one late time suffices. If its best upper endpoint still exceeds $\eta t$ after charging at every late time on unbounded primes, this rejects that specified envelope. In a rigid arithmetic order a proposal requiring at most $m$ interlaced donor runs already has exactly the reference cost. Neither rigidity nor a large upper endpoint proves a lower barrier for unrestricted faces.

The all-prime $o(t)$ estimate and the ordinary theta limit remain open.
