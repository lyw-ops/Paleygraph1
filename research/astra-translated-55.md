# Short forbidden odd cycles on prime subgroups and translated tail bounds

Let $n=(p-1)/2$, $Q=\mathbb F_p^{\times 2}$, $G=\widehat Q$ for $p\equiv1\pmod4$ prime. Write $s(x)=\chi(1-x)$, $D=\{s=-\sigma\}$. Every probability on the sign-$\sigma$ optimal face has transform zero on $D$. For any $B\le Q$ write $b=|B|$, $H=B^\perp$, and $d=\lceil b/2\rceil+\mathbf1_{\sigma=+1}$.

* If $p\ge757$, $b\ge2\sqrt n$ and $d(d-1)>n$, **every coset** of $H$ has mass at most $\cos(\pi/13)/(1+\cos(\pi/13))<0.4927$. Both parities and both signs are included. The arithmetic conditions hold, for either sign, whenever $b\ge(2+\eta)\sqrt n$ through sufficiently large primes and $\eta>0$ is fixed.
* For the plus sign and even $b$, the stronger cap $1/3$ holds whenever $(b/2)(b/2+1)>n$, without the lower cutoff on $p$. Thus two such cosets together carry at most $2/3$.
* On the canonical larger-theta face let $C$ be the exact cap sites. If its sign is plus and $b=|C^\perp|$ is even, then $\mu(C)\le1/3$ through all sufficiently large primes. At either sign and either parity, on any supercritical sequence $\alpha\ge1+\delta$, one has $\mu(C)<0.4927$ eventually.

These estimates also supply nonnegative trigonometric tests for dispersed tails on the full optimal faces. The remaining time-dependent term is specified below. No estimate on that term through all primes is proved here.

## The odd cycle and its sharp bipartite alternative

On $B$ join $u,v$ if $v/u\in D$. Inversion preserves $s$, so this is an undirected Cayley graph of degree $k=|D\cap B|$. If it is bipartite then it has an independent set of size at least $\lceil b/2\rceil$. Distinct elements of that set have differences of sign $\sigma$ since they are squares and $\chi(-1)=1$. For the plus sign adjoin 0. For the minus sign dilate by a nonsquare. Either gives a prime Paley clique of size at least $d$. Hence $d(d-1)\le n$. [Hanson–Petridis, Corollary 1.5](https://arxiv.org/pdf/1905.09134)

On a nonbipartite graph let $g$ be the shortest odd cycle length. If $g\ge5$, the cycle has no chord, and an exterior vertex has at most two neighbors on it. Indeed, three neighbors cut the cycle into three arcs, all of length at least two by triangle-freeness. An odd arc then has length at most $g-4$, and closing it through the exterior vertex gives a shorter odd cycle. Counting incidences yields $gk\le2b$. The compression of the convolution with $s$ on $Q$ to the unit indicator of $B$ has Rayleigh quotient $\sum_B s=\sigma(b-1-2k)$. Its operator norm is at most $\sqrt p$ by the Jacobi bound. Thus $k\ge(b-1-\sqrt p)/2$. For $p\ge757$, $b\ge2\sqrt n$, one has $11b>15(1+\sqrt p)$. Indeed at $b=\sqrt{2(p-1)}$ the squared inequality is equivalent to $(\sqrt p+1)(17\sqrt p-467)>0$. It follows that $2b/k<15$, hence $g\le13$. A triangle already has this property. [Jacobi normalization](fourier.md)

For a forbidden cycle $u_0,\ldots,u_{g-1},u_g=u_0$, put $c_g=\cos(\pi/g)$ and
\[
 V(i)=g^{-1}\sum_{j=0}^{g-1}\operatorname{Re}i(u_{j+1}/u_j).
\]
Every $V(i)\in[-c_g,1]$: apply the smallest eigenvalue $-2c_g$ of the cycle adjacency matrix to the vector $(i(u_j))_j$. Every feasible law has $\mathbb E V(i-a)=0$ for each $a\in G$, by the forbidden transforms. Since $V(i-a)=1$ on $a+H$, positivity gives
\[
              \mu(a+H)\le c_g/(1+c_g).                                      \tag{1}
\]
This proves the first cap. Its uniform constant at the threshold comes from prime clique exclusion and the cycle length.

Bipartiteness is the precise obstruction to improving the single-zero $1/2$ bound for unrestricted feasible laws of this sector when $k>0$. In the identity component $L=\langle D\cap B\rangle$, parity of word length in the steps defines a character into $\{\pm1\}$, equal to $-1$ at every step. It extends to a character of $B$ since $B$ is cyclic (take a root of its value on a generator of $L$). Mix the trivial character and the extension equally in $\widehat B$, and distribute each mass uniformly over its lifts to $G$. The transform vanishes outside $B$ by lift orthogonality, and inside $D\cap B$ by cancellation. This law gives exactly $1/2$ to $H$, and one forbidden zero bounds all cosets by $1/2$. For $k=0$ the uniform law on $H$ realizes mass one. Such lifted laws need not have the prescribed optimal mark or support. For a nonbipartite finite graph (1) gives strict inequality. The $p=41$, $b=5$ quotient in the replay actually realizes (1) at $g=5$ for an unrestricted feasible plus law.

## A triangle on an even plus subgroup

For the plus sign and even $b$, there is a forbidden triangle if and only if $D\cap B^2\ne\varnothing$. In fact if $y^2\in D\cap B^2$, then $s(y)s(-y)=s(y^2)=-1$; both roots belong to $B$. Choose the forbidden root $z\in\{y,-y\}$. Then $1,z,z^2$ are distinct and their three edges are forbidden. Conversely if $D\cap B^2=\varnothing$, all forbidden steps lie in the other parity class, so the graph is bipartite. In this case $B^2\cup\{0\}$ is a prime Paley clique and $(b/2)(b/2+1)\le n$. Taking $g=3$ proves the stronger prime bound.

The [canonical cap-period theorem](astra-face-54.md) gives $C$ a subgroup, and $m=\mu(C)=\alpha\sqrt n/b\le1/2$ for all sufficiently large eligible primes. Consequently $b\ge2\alpha\sqrt n$. If $b$ is even and the sign is plus, the triangle condition applies already at $\alpha=1$, hence $m\le1/3$ and $b\ge3\alpha\sqrt n$. For either sign on $\alpha\ge1+\delta$ the first cap applies since $d(d-1)>n$ eventually. This last conclusion concerns exact cap sites of the canonical row. The inequalities (1) themselves hold for every feasible row.

## A translated, score-dependent upper certificate

Use the oriented scalar scores $Z_+(i),Z_-(i)$ for the larger and smaller sides at time $t$, with their designated signs as in the [full-face quantile LP](astra-tail-53.md). Let $S_s$ be each side's exposed support and $q_s=\gamma_s/\sqrt n$ its point cap. For each forbidden cycle and translate build the nonnegative function $W(i)=(c_g+V(i-a))/(1+c_g)$, with known expectation $h_W=c_g/(1+c_g)$. For any threshold $u$ put $T_s(u)=S_s\cap\{Z_s>u\}$. For any selected collection of such tests define
\[
 L_s(u)=\min\!\left\{1,\ \inf_{\lambda_W\ge0}
 \left[\sum_W\lambda_W h_W+
 q_s\sum_{i\in T_s(u)}\left(1-\sum_W\lambda_W W(i)\right)_+\right]\right\}.       \tag{2}
\]
On $T_s(u)$ the test majorant plus its displayed residual dominates one. Outside it the majorant is nonnegative. Taking expectation under any feasible law and applying its point cap on the residual proves $\mu_s(T_s(u))\le L_s(u)$. Ordinary coset covers are included because $W=1$ on the translated coset. One can use a different majorant at each threshold since every certificate holds for every full feasible row simultaneously.

With $a_0=\min_{s,i\in S_s} Z_s(i)$, $a_K=\max_{s,i\in S_s}Z_s(i)$, integrate the larger of the two bounds. The resulting explicit sufficient test at one time is
\[
  a_0+\int_{a_0}^{a_K}\max_s L_s(u)\,du - E_t/4\ \le\ o(t).                  \tag{3}
\]
This is a finite staircase integral of independent covering LPs on the exposed supports; no positive completion of a projected vector is needed. The affine term $a_0$ must be included. The prime caps alone leave (3) open when the score tails have little overlap with the translated tests.

There is a lower test for this entire covering relaxation, even with **all** translates and cycles of unbounded length. For nonempty $T=T_s(u)$ let $\varepsilon_T$ be the maximum absolute nontrivial forbidden Fourier coefficient of its uniform probability (zero for an empty forbidden mask). Then
\[
 L_s(u)\ \ge\ \min\{q_s|T|,\ (1+2\varepsilon_T)^{-1}\}.                    \tag{4}
\]
Indeed the uniform law on $T$ has $\mathbb E W\le(c_g+\varepsilon_T)/(1+c_g)$ for every translated cycle separately, since the edge weights in $V$ have total absolute value one. Scale its mass to the right side of (4). Its point caps hold, and every $\int W$ is at most $h_W$ because $c_g\ge1/2$. Integrating the pointwise majorant in the proof of (2) against this subprobability proves (4), including the outer truncation at one. In particular $L_s(u)\ge\min(q_s|T|,1/3)$ with no coherence computation. This gives a threshold-by-threshold lower falsifier on **actual exposed supports**, independent of the size of the test dictionary.

There is already a prime obstruction at the seed for the support-unrestricted version of (2). For any fixed interior threshold $-2\sqrt2<r<2\sqrt2$, the tilted prime seed probabilities in [round 53](astra-tail-53.md) have point weights $O_j(1/n)$ and all nonidentity Fourier coefficients $O_j(p^{-1/2})$ for each fixed tilt degree $j$. Scale by $(1+2O_j(p^{-1/2}))^{-1}$, using a nonnegative uniform error bound in this expression, then restrict to the oriented tail. Every cycle test remains valid by the preceding estimate and $W\ge0$. Letting $p\to\infty$ and then $j\to\infty$ gives packing mass tending to one. Thus even all translated prime-cycle constraints in (2) together give asymptotic seed capacity one on these unrestricted tails. On the true smaller side for $r>2$ its exact mean is at most two, giving a strictly smaller limiting upper bound as recorded in round 53. The seed does not prove a late obstruction on the true supports.

1. Test the actual supports at late times using (2), including cycles that spread their weight across multiple cosets, and take the minimum of the normalized left side of (3) over the permitted late window. A positive liminf on an unbounded prime subsequence after substituting the lower certificate (4) disproves this upper-certificate route even with all translated cycles. Minimization over true rows can still improve it.
2. For the exact full-face program allow an independently optimized pair at each eligible late time. A subsequence of primes with dual bounds $M_t^{\mathrm{face}}-E_t/4\ge\varepsilon t$ at every such time falsifies the proposed one-time estimate. The cap-period and odd-cycle restrictions do not yield this lower bound or the opposite required upper bound.

The [checker](astra-translated-55-check.py) performs an exact signed subgroup graph sweep through 5000, including the odd-girth count, the even-plus equivalence, and the finite prime cutoffs. Its [three records](astra-translated-55-checks.jsonl) also enclose the uniform cycle constant and check the sharp five-cycle example. The ordinary all-prime theta limit remains open.
