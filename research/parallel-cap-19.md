# Near-unit Jacobi transfer: an obstruction for weights and an inverse test for the repair

For [ETH Problem 26](https://randomstrasse101.math.ethz.ch/posts/PaleyGraph/), the proposed gain bound on arbitrary weighted source sets of size about half the square root is false even on primes. The example can have even source and target of the critical size, maximum individual source weight tending to zero, and negligible mass in every bounded union of critical-size frequency cosets. The [actual clipped recurrence](parallel-tail-18.md) has another constraint: little injection and near preservation of the bulk load leave approximately flat weights for the *next* step. Near-unit runs therefore give signed, approximately flat Jacobi rectangles; their large overlaps force subgroup structure, but the cap count alone does not force overlaps of that size.

## 1. A prime counterexample for arbitrary weights

Write $Q=(\mathbb F_p^\times)^2$, $G=\widehat Q$, $n=(p-1)/2$, $m_0=n/\sqrt p$, $s(x)=\chi(1-x)$, $\lambda=Fs$ with the unnormalized transform, and $k(d)=\lambda_d/\sqrt p$. We use the sign convention and the quantities $Z,z,\alpha,\kappa,\omega,h=h_*$ from [Round 17](parallel-repair-17.md#setup-and-explicit-formula). In particular $K_{ij}=k(i-j)/m_0$, $K^2=I-J$, and off the diagonal
$$
 z_d=\frac{\alpha}{2n}(1+\sigma\lambda_d).
$$
Here and below $p\equiv1\pmod 4$; the proofs using only Fourier identities and phase discrepancy also work at odd square orders. For large $p$, $\alpha=1/(\kappa+\omega)$ and
$$
 z_0=\alpha\omega=1/h,qquad z_d\le 1/h,qquad h\sim m_0.
 \tag{1}
$$
Indeed $\kappa=1/2+O(1/n)$, and $\max_{d\ne0}\sigma k(d)\to1$ by [Xi, Theorem 1.1](https://arxiv.org/pdf/1809.04286) and the [Jacobi lift identity](critical-sets.md#repeated-differences-are-necessary).

For either sign let
$$
 C=\{d\ne0:\sigma k(d)\ge 1-(\log p)^{-2}\},\qquad \delta=|C|/n .
$$
This set is even and $\delta\asymp 1/\log p$: the angle arc has this size, and Xi's $O(p^{-1/4})$ discrepancy is smaller. By (1), for every $d\in C$,
$hz_d\ge 1-(\log p)^{-2}$. There are even sets $S,T\subset G\setminus\{0\}$ with $|S|,|T|\sim h$ and even probability weights $w$, positive exactly on $S$, such that
$$
 \max_j w_j=O(\log\log p/\log p),\qquad
 g(w,T):=\sum_j w_j\sum_{i\in T}(z_{i-j})_+\longrightarrow 1.
 \tag{2}
$$
Both $w$ and the uniform probability on $T$ can have mass $o(1)$, uniformly, in every coset of size at most $p^{3/5}$. By addition the same holds for any fixed number of possibly different such cosets.

Here is the construction, including the evenness and coset assertions. For $t\in G$ let $D_t=\{j:t-j,t+j\in C\}$. The map $(t,j)\mapsto(t-j,t+j)$ has image the pairs of equal parity and fibers of size two, since $n$ is even. Thus
$$
 \frac1n\sum_t |D_t|/n
 =2\big(|C_{\rm even}|^2+|C_{\rm odd}|^2\big)/n^2\ge\delta^2.
$$
A proportion at least $\delta^2/2$ of the $t$'s have $|D_t|\ge n\delta^2/2$. Sample $r=\lfloor\log p/(8\log\log p)\rfloor$ distinct two-element inverse orbits uniformly without replacement, excluding singleton orbits. Let $S_0$ be their union. The common receiving set $Y=\{t:t-S_0\subset C\}$ is even. For each of the indicated $t$'s, $D_t$ is even, and the chance all $r$ orbits land in $D_t$ is at least $(\delta^2/4)^r$ for large $p$. Hence
$$
 \mathbb E|Y|\ge (n\delta^2/2)(\delta^2/4)^r=p^{3/4+o(1)}.
$$
For a coset $V$ of size at most $p^{3/5}$, the probability $S_0$ meets it in at least twenty points is at most
$$
 \binom r{10}\left(\frac{|V|}{(n-2)/2-r}\right)^{10}
 \le p^{-4+o(1)}.
$$
Indeed at least ten sampled orbits would have to meet $V$. There are at most $n^2$ subgroup cosets total, so the contribution to $\mathbb E|Y|$ of samples violating one of the coset bounds is at most $n p^{-2+o(1)}$. Some good $S_0$ therefore has $|Y|\ge p^{2/3}$.

Choose $|T|=2\lfloor h/2\rfloor$ points as two-element inverse orbits from $Y$. They can be chosen so that their fraction in any of those cosets is $o(1)$: sample $M=\lfloor h/2\rfloor$ orbits without replacement and put $a=\lceil M p^{-1/30}\rceil$. The probability at least $a$ sampled orbits meet a specified coset is at most
$$
 \binom M a\left(\frac{p^{3/5}}{(|Y|-2)/2-M}\right)^a
 \le (O(p^{-1/30}))^a.
$$
The union bound over at most $n^2$ cosets tends to zero. Start with uniform weight on $S_0$. Its transfer into $T$ is at least $(|T|/h)(1-(\log p)^{-2})$. Pad $S_0$ by any even set of new points other than zero to $|S|=|T|$, assigning the padding total weight $1/\log p$ uniformly and the original points the rest uniformly. The padding changes the gain by $o(1)$ by (1), and the weight on each original coset is at most $19/(2r)+1/\log p$. This proves (2).

This example has too few appreciably weighted entries to be a flat rectangle. However, neither deleting any fixed number of exceptional coordinates nor just requiring $\|w\|_\infty=o(1)$ rules it out. At fixed positive width, scaling $w$ by $hL$ for bounded $L$ gives squared norm $O(h^2L^2/r)=o(h^2)$ and peak $o(h)$. Thus the **scale** of the energy and spike bounds of [Round 18](parallel-tail-18.md#1-separate-the-exceptional-entries-at-no-field-dependent-cost) is compatible with these weights. This is not a construction of an orbit of the repair.

## 2. Near-preservation flattens the actual next excess

Use the actual variables $e_k,L_k,T,I_k,f_k$ from [Round 18, §2](parallel-tail-18.md#2-the-actual-excess-follows-a-scalar-recurrence). Suppose $L=L_k>0$, $L'=L_{k+1}\ge(1-\epsilon)L$, $I=I_k\le\epsilon L$, and $M=|T|\le(1+\zeta)h$, with $0\le\epsilon<1/2$, $\zeta\ge0$. Equation (1) and the update give $e_{k+1,i}\le L+(f_{k,i})_+$ on $T$, and $e_{k+1}=0$ off $T$. Thus
$$
 \frac Mh\ge1-2\epsilon,qquad
 \|e_{k+1}-L\mathbf1_T\|_1
 \le 2hI+LM-hL'
 \le hL(3\epsilon+\zeta).
 \tag{3}
$$
The first inequality uses $hL'\le ML+hI$; the second counts the excess above $L$ twice and then subtracts the net difference. Consequently,
$$
 \left\|w_{k+1}-\frac{\mathbf1_T}{M}\right\|_1
 \le \frac{2(3\epsilon+\zeta)}{1-\epsilon}.
 \tag{4}
$$
This calculation uses the sign of the actual update and the **positive** injection; no bound on its negative part is required. The column sum into a next receiver $T'$ is at most $|T'|/h$, so replacing $w_{k+1}$ by the uniform weights costs $o(1)$ in gain under $\epsilon+\zeta=o(1)$ and $|T'|=O(h)$. The Round 18 recurrence also gives $g_k\ge1-2\epsilon$ at every such step. Thus two consecutive transitions obeying these hypotheses with errors tending to zero yield a near-unit **uniform** transfer from the first receiving set to the second.

## 3. Flat rectangles and overlap rigidity

Call the source and receiver $A,T$ in this section. Suppose $|A|,|T|\sim m_0$ and the uniform gain tends to one. The off-diagonal estimate $m_0(z_d)_+=(\sigma k(d))_++o(1)$ is uniform in $d\ne0$, and the diagonal has weight at most $1/|T|$ in the difference law. Since $1-x\le2(1-x_+)$ on $[-1,1]$, the signed deficit
$$
 d_{A,T}=\frac1{|A||T|}\sum_{i\in T,j\in A}(1-\sigma k(i-j))
$$
tends to zero. The converse also follows from $x_+\ge x$ and (1). Set $u_A=\mathbf1_A/\sqrt{|A|}$ and $u_T=\mathbf1_T/\sqrt{|T|}$. The signed pairing is $\langle u_T,\sigma Ku_A\rangle=\sqrt{|A||T|}(1-d_{A,T})/m_0\to1$. The contraction and symmetry of $K$ give
$$
 \|\sigma Ku_A-u_T\|_2+\|\sigma Ku_T-u_A\|_2=o(1).
 \tag{5}
$$
For an actual run of at least three consecutive tight transitions, (4) and (5) applied to the two rectangles give $u_{T_3}=K^2u_{T_1}+o_{\ell_2}(1)=u_{T_1}+o_{\ell_2}(1)$, hence $|T_3\triangle T_1|=o(h)$. The repeat is permitted to alternate sets.

The overlap dichotomy of [critical sets](critical-sets.md#translations-that-almost-preserve-a-critical-set) extends to auto- and cross-overlaps here. For each $a\in G$ compare $(A,T)$ with $(B,U)=(A+a,T+a)$ or $(T+a,A+a)$. Put $r=|A\cap B|/m_0$, $v=|T\cap U|/m_0$. From (5), translation invariance, and $K^2=I-J$, we get $r-v=o(1)$ uniformly: the $J$ inner product of two flat vectors of these sizes is $O(m_0/n)=o(1)$. Use rows $T\setminus U$ and columns $B$. The contribution from $A\cap B$ is at least its number of pairs minus the total original signed deficit. The other columns have kernel at least $-1$ in signed $k$ units. On the other hand (5) bounds the total on the chosen rows. Explicitly,
$$
 |T\setminus U|(2|A\cap B|-|B|)-|A||T|d_{A,T}
 \le m_0\sqrt{|B|}\,\sqrt{|T\setminus U|}\,
       \|\sigma Ku_B-u_U\|_2 .
$$
Dividing by $m_0^2$ gives $(1-r)(2r-1)\le o(1)$, uniformly in the shifts. In particular any auto- or cross-overlap above $c m_0$, for fixed $1/2<c<1$, is $(1-o(1))m_0$.

For completeness, in the auto-overlap case the shifts above $c m_0$ form an exact group $H$ for large $p$: symmetry under inversion is exact, and the sum of two $o(m_0)$ symmetric-difference errors is $o(m_0)$, so their sum is again above the cutoff. It is the same group for both sets by the uniform $r-v=o(1)$ and the dichotomy. Averaging the symmetric difference over $H$ and rounding the densities in its cosets changes each set by $o(m_0)$ points, as in the [within-set argument](critical-sets.md#translations-that-almost-preserve-a-critical-set).

Let $E(A,T)=\sum_a |A\cap(T+a)|^2$. By counting quadruples it also equals $\sum_a |A\cap(A+a)|\,|T\cap(T+a)|$. The uniform auto-overlap comparison and $\sum_a|A\cap(A+a)|=|A|^2$ imply $E(A,T)=E(A,A)+o(m_0^3)$, and likewise for $T$. Summing the squares on and off $H$ gives
$$
 E(A,A)/m_0^3\le c+(1-c)|H|/m_0+o(1).
$$
If $E(A,T)/m_0^3>1/2+\eta$ for some fixed $\eta>0$, choose $c<1/2+\eta$; then $|H|\gg_\eta m_0$, so the rounded sets use only boundedly many cosets. The same energy hypothesis forces some cross-overlap above $c m_0$, because the sum of cross-overlaps is $|A||T|$. Thus $A$ is also $o(m_0)$ from a translate $T+a$, and $T$ is $o(m_0)$ from $A+a$ by the paired overlap comparison. It follows that $2a\in H$. The rounded coset unions are exact translates by $a$, since two different $H$-unions differ in at least $|H|\gg_\eta m_0$ places. If the energy ratio tends to one, then $|H|\sim m_0$ and each rounded set is a *single* coset.

The signed cap estimate only supplies the lower bound of [Round 18, §3](parallel-tail-18.md#3-a-weighted-jacobi-criterion-for-transfer) on $E(A,T)/m_0^2$, not one above $m_0/2$. Therefore this argument does not infer a subgroup from a general flat rectangle.

## 4. The signed arithmetic of the single-coset branch

If the energy ratio tends to one, replace $A,T$ by the two cosets from §3. The signed deficit changes by $o(1)$ by the bounded kernel. Write them as $a_0+H,t_0+H$, let $d=t_0-a_0$, and put $B=H^\perp\le Q$, $b=|B|\sim\sqrt p$. The signed rectangle mean becomes exactly
$$
 \frac{1}{|H|}\sum_{u\in H}\sigma k(d+u)
   =\frac{\sigma}{\sqrt p}\sum_{x\in B}s(x)d(x).
 \tag{6}
$$
In particular, $b^{-1}\sum_{x\in B}|s(x)-\sigma\overline{d(x)}|^2\to0$. The restriction of $d$ is real for large $p$ (also a consequence of $2d\in H$): a character whose square is nontrivial has average squared imaginary part $1/2$. Thus there are two cases:

- If $d|_B=1$, then $b$ must be even and the sign must be plus. For odd $b$, $s(x)s(-x)=s(x^2)$ for $x\in B$, and squaring permutes $B$. Away from $x=1$ this gives $s(-x)=+1$ for all but $o(b)$ points. Both distinct cosets $B,-B$ would then have sign sum of magnitude $(1-o(1))b$, contradicting the exact second moment $\sum_{C\in\mathbb F_p^\times/B}(\sum_{x\in C}s(x))^2=p-2b$ from [subgroup modes](subgroup-modes.md#which-scalar-blocks-can-approach-norm-one). For even $b$, $s(x)s(-x)$ is nearly always $+1$ since $-1\in B$; $s(x^2)$ is usually $\sigma$ since squaring has fibers of size at most two. Hence $\sigma=+1$.
- If $d|_B$ is the nontrivial order-two character, then $b$ is even, and the same identity implies $\sigma=d(-1)=(-1)^{b/2}$. Indeed $s(x)s(-x)=d(-1)$ for all but $o(b)$ choices and $s(x^2)=\sigma$ for all but $o(b)$. This is a twisted subgroup sum in (6); untwisted subgroup estimates cannot be substituted for it.

These tests are field-uniform. In the unshifted remaining plus case, the prime bound in [Round 6](parallel-extreme-6.md#a-prime-gap-for-bounded-coset-covers) obstructs $d_{A,T}+\big||H|/m_0-1\big|=o((\log p)^{-2})$ for the **exact coset pair**, but gives no fixed positive gap. This use of Round 6 requires errors at the stated rate if the cosets are only approximations to $A,T$. The exact [prime additive propagation](prime-additive-rigidity.md) proves nonvanishing without a uniform lower bound on the needed projected mass. In particular it cannot exclude $o(1)$ relative signed deficit. The square plus control has $d\in H$ and $B=\mathbb F_{\sqrt q}^\times$ and realizes the unshifted branch.

A usable remaining target is a prime gap for near-flat rectangles (or an actual-orbit estimate excluding long runs of these rectangles), in addition to the startup and injection estimates of Round 18. A flat gap would rule out **consecutive** tight transitions even though a separate one-step bound over all weights is false. The calculation here does not settle the gap for general flat rectangles, the qualitative gap even for both remaining single-coset branches, or the theta asymptotic.

As checks on §1, exact counting verified the parity identity for both signs at $p=401$. An in-memory FFT check at $p=1000033$, with a cap of width $0.06$, gave two-source gains $0.979820$ and $0.980839$ into $500$ even receivers for the two signs. These are floating-point examples of the construction with one inverse orbit and no padding; the asymptotic construction uses the counting proof.
