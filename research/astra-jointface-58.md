# A common positive sector map freezes the actual marked score laws

Let $n=(p-1)/2$, $K^2=I-J$, $J=\mathbf1\mathbf1^*/n$, and let $v_t$ be the actual cold orbit,
$\phi_t=|v_t|+b_t e_0$, $b_t=\sqrt{4+v_t(0)^2}-|v_t(0)|$, $v_{t+1}=K\phi_t$. The two optimal endpoint probabilities $\mu_s$ have caps $q_s=\mu_s(0)$, $q_+q_-=1/n$, and disjoint positive supports off the root. Write $Y_t=\sqrt n v_t$, $E_t=\|v_t\|^2$, and use the [round-53 integrated maximum](astra-tail-53.md) $M_t$ of the two oriented increasing quantiles.

On every eligible prime, any common positive affine averaging of the simplex preserving both sector classes and both optimal marks leaves **each entire score law exactly unchanged at every depth**. Even allowing unrestricted root motion, any such averaging has antipodal empirical RMS error at least $\sqrt8-o(1)$ at *every individual time* of the growing arithmetic window. This rules out a sector-preserving realization of the [cheap empirical coupling](astra-drift-49.md). A support-conditioned move can escape the obstruction. At $p=97$ a single such move strictly improves the true joint objective while necessarily worsening it on a whole interval of thresholds. The all-prime estimate on the full optimal faces remains open.

## Exact rigidity and the price of moving the root

Let an affine map of the full probability simplex into itself carry each set of nonnegative probabilities in $\mathbb R\mathbf1+V_s$ into that same set. It has a column-stochastic nonnegative matrix $B$. The uniform probability is the unique common feasible law, hence is fixed and $B$ is doubly stochastic. Small mean-zero sector perturbations about uniform span $V_s$, and their images stay in the same sector. Thus $BK=KB$. Symmetry of $B$ is unnecessary. Set $l=1-B_{00}$. For any optimal input pair, with normalized losses $d_s=1-(B\mu_s)_0/q_s$,

$$
 d_++d_-\ge l .
$$

Indeed $\mu_+(j)/q_++\mu_-(j)/q_-\le1$ off the root, while at the root the sum equals two. Average against $B_{0j}$. Exact simultaneous marks imply $B_{00}=1$.

For a real vector $f$ write $D_B(f)=\tfrac12\sum_{ij} B_{ij}(f_i-f_j)^2=\langle f,(I-B)f\rangle$. Then $D_B(Kf)=D_B(f)$ by commutation, $K^2=I-J$ and bistochasticity. There is an exact finite identity for the true time evolution:

$$
 D_B(v_{t+1})-D_B(v_t)=4l
 -\sum_{ij} B_{ij}(|v_t(i)v_t(j)|-v_t(i)v_t(j))
 -b_t\sum_{j\ne0}(B_{0j}+B_{j0})|v_t(j)|.
$$

Folding to $|v_t|$ gives the first subtraction. At a root-bulk edge, replacing $a=|v_t(0)|$ by $\sqrt{4+a^2}$ increases the squared difference to $c=|v_t(j)|$ by $4-2b_t c$. The total root-bulk weight is $2l$. It follows that $D_B(v_t)\le4tl$, with equality at $t=1$. With exact simultaneous marks all transitions of positive weight have $Y_t(i)=Y_t(j)$ at every time. The induced coupling from each input law to its image preserves the whole history, so both marginal laws and the charged $M_t-E_t/4$ are identical. This permits a new operator and a new actual input pair at each candidate time.

For approximate marks put $r_s^2=n\sum_i\mu_s(i)^2$. The $W_1$ change of each individual score law is at most $r_s\sqrt{2D_B(v_t)}$, by coupling an input column $j$ to $i$ via $B_{ij}$ and Cauchy–Schwarz under $B_{ij}/n$. The integrated maximum changes by at most the sum of these two $W_1$ costs, by its quantile formula. Consequently its absolute change is at most $(r_++r_-)\sqrt{8t(d_++d_-)}$. The image laws are still probabilities in their sectors, with the stated possible mark losses. This bound excludes an order-$t$ improvement from vanishing common mark loss whenever both collisions are $O(\sqrt t)$ in the $r_s$ convention. Exact rigidity has no collision premise.

## A cheap antipodal plan must mix Fourier sectors even at a single late time

For an arbitrary doubly stochastic $B$, the uniform-marginal plan has probabilities $B_{ij}/n$. Its antipodal RMS cost at time $t$ is $e_t=(\sum_{ij}B_{ij}(v_t(i)+v_t(j))^2)^{1/2}$. Let $m=n^{-1}\sum_j\phi_{t-1}(j)$, $w=Kv_t=\phi_{t-1}-m\mathbf1$ for $t\ge1$. We have $w_j\ge-m$, $w_0\ge2-m$, and $m=2g_{t-1}/\sqrt n\le2\sqrt{D/n}$ for $t\le D$ by the [cold norm telescope](astra-critical-44.md). If $BK=KB$, the sum defining $e_t^2$ is unchanged on replacing $v_t$ by $w$, since $K$ is isometric on mean-zero vectors and commutes with $B$. Counting only root-bulk and root-root edges gives, for $m\le1$,

$$
 e_t^2\ge 2(1-B_{00})(2-2m)^2+B_{00}(4-2m)^2
 \ge 2(2-2m)^2.
$$

This gives $e_t^2\ge8-o(1)$ uniformly for every $1\le t\le D$. At the seed $e_1^2=8(1+B_{00}-2/n)$, since $v_1=2Ke_0$ and $K^2=I-J$. A nonzero cyclic shift has $B_{00}=0$ and attains the limiting constant. The proof applies to prime squares as well.

More generally, testing the same cost against $(Ke_0)_j$ gives

$$
 e_t\sqrt{1-1/n}\ \ge\ \langle v_t,(I+B)Ke_0\rangle
 =w_0+\langle w,Be_0\rangle+\langle v_t,(BK-KB)e_0\rangle.
$$

The test has squared norm $1-1/n$ under the unnormalized edge weights and $Be_0$ is a probability. Hence every cheap empirical coupling satisfies $\sqrt{E_t}\,\|(BK-KB)e_0\|\ge 2-2m-e_t\sqrt{1-1/n}$. The transpose obeys the same bound. In particular $e_t=o(1)$ on a growing late time requires a commutator norm at least $(1-o(1))/\sqrt t$ on the marked column since $E_t\le4t$. The endpoint-marginal quantile coupling is outside this empirical constraint.

## What a positive move on the actual supports can do

The restriction to maps on the *full* sector classes matters. The unions of positive off-root supports of the two optimal faces are disjoint by complementarity for every cross-pair of optima. Given any two target rows on these faces, one common column-stochastic map can send every pair of input optima to those targets. Fix the root and send every nonroot source of sign $s$ to the target's conditional bulk law. On unused columns take the identity. More economically, for one input pair one can retain the minimum of old and target mass at each site, and send only surplus bulk mass to the same sign's deficits in proportion to their sizes. These constructions impose the Fourier equations at the selected outputs. They need not preserve the two entire sector classes.

Exact support-conditioned flows are necessarily dispersed. A nonzero change $h$ on one face has zero root and mass, $h=sKh$, and, writing $V=\sum h_+=\sum h_-$, the Jacobi entry bound gives $\|h\|_\infty\le (2\sqrt p/n)V$. Both the positive and negative changes thus require at least $n/(2\sqrt p)$ sites, and no $k=o(\sqrt p)$ of their sites can carry a fixed fraction of their variation. This applies to a single common pair across all thresholds at any depth. Individual tail gains on smaller sets can still occur with sufficient compensating movement elsewhere.

The [three replay records](astra-jointface-58-checks.jsonl) use the [exact parameterization of the two full even faces at 97](astra-face-54.md). At $t=32$, move the anchored plus coordinates $(x,y)$ from $(0,0)$ to $(0,1/32)$, leaving the singleton even minus face fixed. This is one true pair across all thresholds. The positive flow moves total probability between $.029845098$ and $.029845099$, with 10 donor and 10 recipient sites. It improves the common quantile objective by between $.003649205$ and $.003649206$. The terminal energy charge is identical. Thus exact sector-class-preserving common averaging cannot obtain even this improvement from that input.

The obstruction to optimizing **separately at each threshold** also holds for the minimum. Put $F_{x,y}(u)=\max_s\mu_s(Z_s>u)$ and $F_0=F_{0,0}$. For each $u\in[3.45,3.60]$, the plus survival already exceeds the minus survival at the origin and its slopes in $(x,y)$ are greater than $.5057,.3078$. Every feasible pair has $x,y\ge0$, so $F_{x,y}-\min F\ge .30(x+y)$ throughout this band. In particular any pair with different even laws worsens the joint envelope there. On $[.60,.65]$, the base plus survival exceeds minus by more than $.03$, and the plus slopes satisfy $a>0$, $-.281<b<-.28$. The trial $(0,1/32)$ retains plus dominance there, so $\min F\le F_0-.28/32$. For $x+y<1/64$, we also have $F_{x,y}\ge F_0-.281/64$, giving an integrated gap at least $.05(.28/32-.281/64)>.000217$. For $x+y\ge1/64$, the first band gives a gap of at least $.15\cdot .30/64>.000217$. Therefore
$$
 \min_{x,y}\int F_{x,y}(u)\,du-\int\min_{x,y}F_{x,y}(u)\,du>.000217
$$
over the common finite score range. The shared additive lower endpoint cancels. Evenization preserves all score laws, so this covers asymmetric competitors too. The lower bound concerns the minimum, whereas the [round-57 switching gap](astra-face-57.md) concerned the maximum.

Run `.venv/bin/python -B research/astra-jointface-58-check.py`. The 384-bit checks use true Arb DFT states, exact cyclotomic face elimination, and rational score rounding with enclosure. The directed shift mixture independently checks both terms of the Dirichlet identity at all 32 steps. The two threshold bands and both slopes are tested directly against the unrounded scores. The prime-uniform results above are written proofs; the strict cost improvement and incompatible minimizing bands are certified at one finite prime.

1. Seek a common support-conditioned flow on each side, allowing both increases and decreases of the maximum survival across thresholds. For a directed edge dictionary on each actual exposed support, enforce nonnegative flows with total outflow at most the current mass per site, fixed root, and zero forbidden transform of the flow divergence. Evaluate the joint LP on the resulting rows, charging $E_t/4$. One upper certificate of $o(t)$ after charging at some $D/2\le t\le D$ on each prime suffices. Positive normalized lower certificates throughout a late window on an unbounded prime sequence reject that edge dictionary; with all within-sign bulk edges they reject the full one-time bound.
2. For an endpoint-conditioned adaptation of an empirical antipodal plan, test the marked commutator before imposing global sector control. A proposal with $e_t=o(1)$ and $\sqrt{E_t}\|(BK-KB)e_0\|<2-\eta$ for any fixed $\eta>0$ is already excluded at every sufficiently large prime in this window. A surviving proposal must handle the sector change on the actual endpoint marginals and then certify their objective. No such prime-uniform transfer or proof of ETH26 follows here.
