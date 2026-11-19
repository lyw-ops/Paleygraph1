# Net transport of the charged optimizers and a restriction on localized updates

Let $p\equiv1\pmod4$ be prime, $Q=\mathbb F_p^{\times2}$, $G=\widehat Q$, $n=(p-1)/2$. Take any fixed reference on each of the two true faces. At every late time in the [marked window](vanishing-floor-38.md), select a pair attaining the minimum $M_t^{\rm face}$ of the [single-pair quantile program](astra-tail-53.md). The score on face $s$ is $Z_s(i)=s\sqrt n v_t(i)$ and the energy charge is $E_t/4=\sum_i v_t(i)^2/4$.

Fix $0<\epsilon<1/4$, $R=\lceil n^{3/4+\epsilon}\rceil$. A common proportion $1-O(n^{-\epsilon+o(1)})$ of primitive orders realizes all these selected minima using only direct transfers from **net donors to net recipients**, with nonwrapping jumps at most $R$. All common mass stays at its original site. In the same orders, carrying a fixed proportion of any one of the nonzero net movements takes $\gg n/R$ intervals of length $O(R)$ on the donor side, and also on the recipient side. This is relative to the net mass, even for target pairs arbitrarily close to their references.

There is a separate assertion uniform in **every** primitive order and **all** possible target rows. Any coordinated change whose net support lies in $k$ cyclic intervals of length $O(R)$ is identically zero if
\[
 k<(1/4-\epsilon)\log_2 n-\log_2\log_2 n-O(1).
\]
The implicit constant depends only on the interval length constant and $\epsilon$. The intervals may be selected from the actual exposed sites, with arbitrary holes and arbitrary weights. Consequently a method that iterates individually face-feasible updates using $o(\log p)$ local patches per update returns exactly the reference value at every late time, regardless of the number of updates. This decides that dictionary without a lower bound on the unrestricted charged objective.

## Routing only the required mass

For a difference $h=\mu'_s-\mu_s\ne0$ of actual probabilities on one face put $m=\sum h_+=\sum h_->0$, with $h_-=(-h)_+$. The whole Fourier sector gives $Kh=sh$. The Jacobi entry bound is $\max_{ij}|K_{ij}|\le\sqrt p/n$. Thus the two probabilities $w_+=h_+/m,w_-=h_-/m$ satisfy
\[
 \max_i w_\pm(i)\le 2\sqrt p/n,\qquad \|w_\pm\|_2=O(n^{-1/4}).
\]
They are root-free, since the optimal mark is fixed. Each lies on the true exposed bulk. Their individual forbidden transforms may be nonzero. Removing the common mass first and applying the original cap on the reference, without using the eigenvector relation for the *difference*, would lose a factor $1/m$.

Use the [primitive-order discrepancy bound (1)](astra-charged-61.md) for these probabilities. In expectation the discrepancy $d_b(w)=\sup_I|w(I)-|I|/n|$ over cyclic intervals in a primitive order $b$ is at most $n^{o(1)}\|w\|_2$. Markov and a union bound over the $O(D(p))$ nonzero differences at both signs give $d_b(w)\le (R-2)/(2n)$ simultaneously with the stated exceptional fraction. The increasing position quantiles then differ by at most $n(d_b(w_+)+d_b(w_-))+1\le R$, by the two prefix inequalities. Give this coupling weight $m$ and leave $\min(\mu_s,\mu'_s)$ on its diagonal. Both marginals are the true chosen rows. In particular a common target is used across the score integral and the same $E_t/4$ is subtracted. No maximization over neighborhood scores enters the result.

For a union of $k$ intervals of length at most $C R$, subadditivity gives $w_\pm(\bigcup I)\le k(C+1)R/n$ in these same orders. Even a routing that uses longer edges has these prescribed net weights. This bound controls the preselected collection of optimizers and references, without claiming simultaneous discrepancy over the entire face.

There is also a uniform charge-scale bound on the effect of small net mass at specified score sites. For any given pair of true references and targets let $m_s$ be the net mass by sign. Couple each side by keeping common mass fixed and directly moving the excess. Couple the two reference score laws by increasing quantiles, then sample targets conditionally on the two chosen source sites (splitting ties with their true masses). The target integrated maximum is at most the resulting expected maximum, since increasing quantiles minimize the expected maximum. Reversing the roles gives
\[
 |M_t(\mu')-M_t(\mu)|\le\sum_s\sum_i |h_s(i)|\,|Z_s(i)|.
\]
This also follows from the scalar $W_1$ triangle bound. On a set of $k$ sites the contribution of sign $s$ on the right is at most $2m_s\sqrt{(p/n) k E_t}$, by the entry cap for $|h_s|$ and Cauchy–Schwarz. On the full group the sharper bound from $\sum |h_s|^2\le4m_s^2\sqrt p/n$ is $2m_s p^{1/4}\sqrt{E_t}$. Since $E_t\le4t$, order-$t$ improvements require total net mass $\gg\sqrt t/p^{1/4}$. On any $o(t)$ designated extreme sites their possible contribution is $o(t)\sum m_s$. The common energy charge cancels in this comparison of true objectives. These estimates allow order-$t$ improvements involving many sites at larger net mass.

## Intervals supporting an exact Fourier update

Choose **any** primitive $b\in Q$ and assign exponent $k$ to the character with value $\omega^k$ at $b$, where $\omega=e^{2\pi i/n}$. Let
\[
 F_s=\{j:\chi(1-b^j)=-s\}\cup\{0\},\qquad
 N_{s,r}(b)=\#\{j:j,j+1,\ldots,j+r-1\in F_s\}.
\]
Cyclic indices are understood. Let a nonzero mean-zero vector with the forbidden Fourier zeros of sign $s$ be supported in $r$ disjoint cyclic intervals, each containing an occupied site. If the sum of their diameters (number of sites minus one per interval) is $W$, then
\[
 \boxed{\quad W\ge N_{s,r}(b)\ge n2^{-r}-r\sqrt p/2-r/2 .\quad}       \tag{1}
\]
In the lower estimate $1\le r\le n$. It uses the actual Paley mask and is independent of all choices of intervals. In the first inequality an ordinary feasible probability can instead use the forbidden set alone, without adding the mass-zero frequency. The same second bound holds in that version.

To see the first assertion, rotate the site indices to cut between intervals. The resulting Fourier modulation preserves all zeros. Write the polynomial of the vector on the lifted interval as $H(z)=\sum_{a=1}^r z^{u_a}P_a(z)$, where $u_a$ is the start of band $a$ and $\deg P_a$ is at most its diameter. Each $P_a$ is nonzero. At a run start $z=\omega^j$ the $r$ equations $H(\omega^l z)=0$, $0\le l<r$, force the polynomial determinant
\[
 \Delta(z)=\det[\omega^{lu_a}P_a(\omega^l z)]_{0\le l<r,\ 1\le a\le r}
\]
to vanish because the vector with entries $z^{u_a}$ is in the matrix kernel. Its degree is at most $W$. Let $v_a$ be the least exponent of $P_a$ with nonzero coefficient $c_a$. The coefficient of $z^{\sum v_a}$ is $\prod_a c_a$ times the Vandermonde determinant of $\omega^{u_a+v_a}$, all distinct since the occupied bands are disjoint. The polynomial is therefore nonzero, proving the root count.

For the second assertion sum $2^{-r}\prod_{l<r}(1-s\chi(1-b^l x))$ over $x\in Q$. The empty subset contributes $n2^{-r}$. For a nonempty subset of $j$ distinct shifts, the [complete translated character bound](parallel-torus-8.md#a-uniform-bound-for-twisted-translate-correlations) gives error at most $j\sqrt p$ before the $2^{-r}$ averaging. Summation gives $r\sqrt p/2$. At the $r$ sites where a character argument vanishes the nonnegative test contributes at most $1/2$ per site, while elsewhere it is the exact indicator. The number of pure forbidden run starts is consequently at least the second bound, and adjoining exponent zero can only increase it. [Weil's character-sum bound](https://pmc.ncbi.nlm.nih.gov/articles/PMC1079093/)

For $k$ intervals of at most $CR$ sites, merge overlaps and drop unoccupied bands. If the union is the circle its cardinality already forces $k\ge n/(CR)$. Otherwise there remain $r\le k$ bands with total diameter at most $kCR$. Formula (1) gives
\[
 n2^{-k}\le k(CR+(\sqrt p+1)/2).
\]
If $k\le \log_2 n$, taking logarithms gives the claimed lower bound. For larger $k$ it is immediate. A net-only radius-$R$ proposal with donor sites in $k$ intervals of length $CR$ has its entire changed support in the same intervals expanded by $R$ on each side, hence satisfies the same restriction with $C+2$. This conclusion permits arbitrary coordination across all $k$ patches within an update. It applies anew if the generator is changed at each individually feasible update.

## Finite checks and next tests

The [exact checker](astra-weighted-62-check.py) finds the smallest nonwrapping radius that realizes **every pair** of true even optima at $p=97$ when only net mass is moved. Its optimum over primitive orders is five, attained at powers $23,25\bmod48$. Allowing common mass to be rerouted gave four. In the reference order net-only transport needs sixteen, against five with such rerouting. For the calculation use the two independent plus directions of the [full cyclotomic face](astra-face-54.md). The minus face is a singleton after evenization. Six distinct lines where a coordinate of the difference vanishes decompose the two-dimensional space into cones. On each cone the positive and negative parts are linear. Adding plans for its bounding rays yields the same radius bound throughout the cone with the right donor and recipient marginals. Conversely every ray occurs at small scale from a relative interior point of the full polygon. The line quantile bottleneck is exact by the prefix inequalities. The [four records](astra-weighted-62-checks.jsonl) also give exact run counts at three primes. In particular at $p=9413$ in order $b=9$, the six-band diameter lower bound is 70 for plus and 78 for minus. Reproduce with `.venv/bin/python -B research/astra-weighted-62-check.py`.

1. Seek a single globally coordinated net-only target on each face in a common typical order, with full Fourier equations and the retained diagonal. Evaluate its actual score quantiles. A late value $M_t-E_t/4\le o(t)$ on every sufficiently large prime closes the charged estimate. A local patch solver below the bound (1) has the reference cost exactly. A positive reference excess at every late time on unbounded primes rules out that solver.
2. On prime sequences with reference excess at least $\eta t$ throughout the late window, test all true target differences against their cap-weighted score sums on the complement of $o(t)$ designated extreme sites. A uniform bound there below $(\eta-\delta)t$ for some $\delta>0$ proves a genuine lower obstruction for the **full** minimum. A true improving pair by $\eta t$ must pay at least that much up to $o(t)$ outside those sites, and must meet the net-mass lower bound above. The prime-uniform late upper estimate and ETH26 remain open.
