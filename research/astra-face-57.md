# Positive complements for short Fourier blocks and across cold thresholds

Write $Q=\mathbb F_p^{\times2}$, $G=\widehat Q$, $n=(p-1)/2$, and $D_s=\{d\in Q:\chi(1-d)=-s\}$. The normalized probability on the true sign-$s$ face has root and point cap $q_s=\gamma_s/\sqrt n$. These caps lie between fixed positive multiples of $n^{-1/2}$, by the Jacobi bound and reciprocity. Let $S_s$ be its full support exposed by an opposite optimum as in [round 53](astra-tail-53.md). We use even exposing rows and even cold scores.

There are two distinct losses in optimizing a high-score submeasure. Even demanding a full positive completion with the **actual optimal root**, separately for every sub-square-root block of frequencies, fails to control prime seed tails when support is unrestricted. On the **true** exposed supports, allowing a different fully optimal positive completion at each score threshold overestimates even the greatest objective attained by one pair at $p=97$, at every tested time. Neither statement supplies an asymptotic counterexample to ETH26.

## An exact block completion on every large prime, with shared tail and optimal root

At the cold seed put $Z(i)=sY_1(i)=2s\sqrt n (Ke_0)_i$, $M_p=2\sqrt{p/n}\to M=2\sqrt2$. Fix $2<r<M$, let $T=\{Z>r\}$, and let $k_p=o(\sqrt p)$ be arbitrary positive integers. **For either sign** there exist even nonnegative weights $w$ on $T$, of mass tending to one, with the following simultaneous property. For every $A\subset D_s$ of size at most $k_p$ there is a probability $b_A$ such that

\[
 b_A|_T=w,\qquad 0\le b_A(i)\le q_s,\qquad b_A(0)=q_s,
 \qquad \widehat b_A(d)=0\quad(d\in A).                         \tag{1}
\]

Here $w$ is independent of $A$ and the complement is supported entirely outside $T$. The support available outside and inside the tail is at this point the whole character group. The stronger [round-56 program](astra-tail-56.md) using all disks and walks of length at most $k_p$ accepts these same tail weights. For each walk use (1) on its set of steps (or inverse representatives). Its translated cycle weights have mean zero under $b_A$ and are bounded below by $-\cos(\pi/g)$ at each site for an odd closed walk of length $g$, by the cycle Rayleigh bound on the list of characters of its visited vertices, allowing repetitions. The disk constraints follow by canceling one coefficient against its positive complement. This includes the growing cutoff $k_p\asymp n^{1/8}$. In contrast the true smaller-sign probability has mean $E Z=2(\gamma_s-1/\sqrt n)\le2$ at this seed, so its upper-tail limsup is at most $(M+2)/(M+r)<1$.

To prove (1), use normalized counting measure on $G$ in the next Gram matrices. For $F=\{1\}\cup A\cup A^{-1}$, $h=|F|\le2k_p+1$, define $L=G\setminus(T\cup\{0\})$. The restricted exponential Gram matrix is
\[
 H_{fd}=n^{-1}\sum_{i\in L}i(f/d),\qquad f,d\in F .
\]
It has a field-uniform positive lower spectral bound. Indeed $P(i)=(M_p+Z(i))/(M_p+r)$ is nonnegative everywhere and majorizes one on $T$. The full matrix weighted by $P$ has diagonal $M_p/(M_p+r)$ since $Z$ has mean zero. Each off-diagonal entry is $O(n^{-1/2})$, since the nontrivial normalized Fourier coefficients of $Z$ are precisely the signed mask values times $2/\sqrt n$. The matrix on $T$ is dominated in PSD order by this weighted matrix. Removing the root costs at most $h/n$ in norm. By the row-sum bound,
\[
 H\succeq\left(\frac{r}{M_p+r}-O(h/\sqrt n)-h/n\right)I.          \tag{2}
\]
This also holds for any specified positive $r<M$.

Fix a tilt degree $j\ge1$ and $0<\epsilon<1$. Let $\pi_j$ be the probability with weights proportional to $(1+Z/M_p)^j$ on the nonroot sites, zero at the root. The [prime polynomial Fourier estimate](astra-tail-53.md) gives point caps $O_j(1/n)$ and nontrivial transform $O_j(p^{-1/2})$, uniformly in the frequency and the choice of sign. Removing the root costs $O_j(1/n)$. Let $U'$ be uniform off the root. Start from
\[
 b=q_s\delta_0+(1-q_s)((1-\epsilon)\pi_j+\epsilon U').
\]
It has the prescribed root and mean, with every nonroot mass between $(1-q_s)\epsilon/(n-1)$ and $O_j(1/n)$. All nontrivial transforms are $O_j(p^{-1/2})$. On $F$, set $a_1=0$, $a_f=-\widehat b(f)$ otherwise, using $\widehat b(f)=\sum_i b(i)i(f)$. Solve $c=H^{-1}a$. The adjustment
\[
 e(i)=n^{-1}\mathbf1_L(i)\sum_{d\in F}c_d\overline{i(d)}
\]
has the required Fourier data on $F$. It is real and even by inversion and conjugation symmetry. Equations (2) and Cauchy–Schwarz give
\[
 \max_i|e(i)|\le \sqrt h\,\|c\|_2/n=O_j(h/(n\sqrt p))=o_j(1/n).
\]
Thus $b_A=b+e$ is positive, within the true cap, of mass one, and agrees with $w=b|_T$. All bounds hold uniformly over the chosen blocks. At fixed $j$, the prime empirical seed law converges to the arcsine law on $[-M,M]$, also after the tilt. Its tilted probability of $Z>r$ tends to one as $j\to\infty$. Taking the prime limit first, then $j\to\infty$ and $\epsilon\downarrow0$, proves the asymptotic capacity statement and gives a diagonal choice of witnesses. This proof uses no arithmetic at growing polynomial degree.

## Uses and limits on the true exposed supports

For an actual tail $T\subset S_s$, the interpolation argument is also a finite test. Start with a capped, normalized even probability $b$ on $S_s$ with the prescribed root. Use $L\subset S_s\setminus(T\cup\{0\})$ of positive repair slack
$\delta=\min_{i\in L}\min(b_i,q_s-b_i)$, taking $L$ inversion-stable. For each block, if the corresponding Gram has least eigenvalue at least $a>0$, then
\[
 \sqrt{|F|}\,\|\widehat b|_{F\setminus\{1\}}\|_2/(na)\le\delta        \tag{3}
\]
suffices for the block completion of this *same* actual tail weight. The extension and its point caps follow directly from the displayed correction. There is no known replacement for (2) on an arbitrary true exposed residual set. In the opposite direction, on a fixed tail with a fixed $w$, take the compact convex polytope of positive complements on $S_s\setminus T$ with the specified mass, root and caps, before imposing forbidden zeros. If it is nonempty of affine dimension $d$, checking joint feasibility for **every $d+1$ frequencies** is already exact by finite Helly inside its affine hull. An even row has one real cosine equation per inverse pair. The same Helly count works with complex equations grouped as affine subsets. This exact cutoff can be used separately at each threshold, including ones with very small residual supports.

For a specified tail perturbation this block cutoff also has a genuine sparse Fourier test. Suppose a true even reference law has strict two-sided point slack on its nonroot exposed orbits, and the perturbation adds $\eta h_j$ to the **orbit masses** on the upper sites, with zero change at the root if present. Let $L$ be all lower nonroot exposed orbits. For every finite field there exists one $\eta>0$ admitting a disjoint positive completion for every block of size $k$ if and only if there is **no** real trigonometric polynomial consisting of a constant and at most $k$ forbidden cosine frequencies which vanishes on $L$ and has nonzero pairing with $h$ on the upper sites. In fact for each block the linear correction on $L$ exists exactly when its target is in the column space of the restricted cosine-and-constant matrix. The condition is the left-kernel criterion. Positive slack permits one sufficiently small common step over the finite collection of blocks. A witnessing polynomial precludes every nonzero step because the root is fixed. This characterization concerns existence of a small perturbation; (3) or explicit solutions quantify its size.

There is an exact nontrivial block threshold on a **true cold tail**. At $p=97$, $t=32$, for every $3.8\le u\le4.1$ the plus tail is empty and the minus tail consists of the orbit $\{16,-16\}$ in $G=\mathbb Z/48$. Its true mass is fixed because the minus face is a singleton after evenization. The least number of forbidden inverse-frequency orbits that can pin this tail mass, keeping the true exposed support, root and caps, is **six**. In particular:

* For every one of the 220 triples, add the same $1/1000$ to this orbit's total mass. Correct on the nine lower nonroot orbits $1,4,9,12,15,17,20,23,24$. With $B_{fj}=\cos(2\pi f j/48)$ on the triple plus frequency zero, the correction is $-10^{-3} B^T(BB^T)^{-1}(\cos(2\pi f16/48))_f$. Arb validates invertibility and all corrected point caps and strict positivity. This delivers an integrated excess of at least $3/10000$ over fully completed thresholdwise capacities at this time, using true optimal completions for every other threshold. The perturbed tail itself has mass below $1/3$ (the true mass is below $.278$), so it simultaneously satisfies every disk and every odd-walk inequality.
* For each of the 792 five-orbit blocks, cyclotomic elimination gives a correction on the same lower sites for unit extra tail mass, retaining the root and mass. Scaling all the respective corrections to the common tail increment $.000066989$ respects every point cap and positivity by the certified minimum slack. Every smaller block extends to a five-block.
* On the six frequency indices $1,7,11,13,18,24$, a cyclotomic linear combination of their cosines and the constant vanishes on all nine lower nonroot orbits and equals one at 16. Since the root value is prescribed, its expectation pins the tail mass to that of the true minus row. Evenization preserves the constraints and the total on the target orbit, so the obstruction also applies to noneven completions.

Even complete Fourier constraints on both true supports at each threshold leave a separate loss. For two actual face laws let $P_s(u)$ denote their oriented survival probabilities, and $a_0$ their common lower endpoint convention from round 53. Define
\[
 V_t=a_0+\int_{a_0}^{a_K}\max_s\max_{\mu_s\in\mathcal F_s}P_s(u)\,du,
 \qquad
 W_t=\max_{\mu_+,\mu_-}\left[a_0+\int_{a_0}^{a_K}\max_s P_s(u)\,du\right].
\]
Here the maximum inside $V_t$ is exactly the full positive-completion capacity with a disjoint complementary mass, including root and all Fourier constraints. $W_t$ uses one fixed pair. At the true $p=97$ faces and zero-floor path, the [384-bit and rational checker](astra-face-57-check.py) gives

| Time | Independently completed $V_t$ | Greatest fixed-pair $W_t$ | Least fixed-pair $M_t^{\rm face}$ |
|---|---:|---:|---:|
| 16 | [2.415566437, 2.415566438] | [2.388219603, 2.388219604] | [2.358888698, 2.358888699] |
| 32 | [2.580976090, 2.580976091] | [2.569630814, 2.569630815] | [2.561786507, 2.561786508] |

The last column comes from [round 54](astra-face-54.md). Through **every integer $16\le t\le32$** one has $V_t-W_t\ge .008607358$ and $(V_t-E_t/4)/t\ge .047667746$. In particular even a full positive complement separately at every threshold need not be realizable by a fixed pair. The previous [round-56 lower packings](astra-tail-56-check.py) pass **all Fourier disks and every odd walk**, since they satisfy $m+2\max_D|\widehat w|\le1$ or are restrictions of true laws. Their recorded lower cost at $t=32$ exceeds 2.601375, strictly above $V_{32}$. This separates the losses from relaxing the complement, switching it at each threshold, and maximizing over pairs in place of minimizing. The interval is a fixed finite-field test and does not instantiate the asymptotic growing window.

For replay, the exact two-dimensional even plus face and unique even minus row come from the cyclotomic elimination in [round 54](astra-face-54-check.py). Rounding each plus coefficient to within $2\cdot10^{-19}$ and expanding the pointwise positivity constraints by $6\cdot10^{-19}$ gives an outer rational polygon covering every feasible point in the parameter box. Its four vertices are moved toward a strictly positive relative-interior point by weight $10^{-10}$ and Arb checks feasibility of all four moved vertices. The rounded per-threshold survival maximum is convex in the parameters, as is the integrated fixed-pair objective; each has its outer maximum at a vertex. The feasible inner vertices give lower bounds. Errors for the rounded masses and scores are included, using monotonicity and common-translation covariance of both upper objectives for score rounding. The [receipt](astra-face-57-checks.jsonl) is reproducible with `.venv/bin/python -B research/astra-face-57-check.py`.

1. On the actual growing late window use one common pair across thresholds in the [full-face LP](astra-tail-53.md). A feasible pair with charged objective per step at most $o(1)$ at one late time on each prime proves the limit. An unbounded prime subsequence with positive normalized dual lower bounds at **every** late time refutes this one-time criterion.
2. To test the strengthened positive-block upper relaxation itself, seek a supported high-tail baseline and certify (3), or exact block completions, before integrating both sides. A positive lower margin above $E_t/4$ of order $t$ throughout the late window on unbounded primes rejects that upper route. Upper certificates with nonpositive limiting charged minimum instead suffice. The all-prime seed obstruction explicitly requires unrestricted support and cannot make this decision.

The prime-uniform late estimate, positivity completion of the short-depth marked averaged proposals, and ETH26 remain open.
