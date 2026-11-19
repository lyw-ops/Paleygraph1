# Warm tangent trials for both cold marks

At a fixed field a reference from the warmer floor $b$, paired with an explicit same-side tangent step, encloses each marked logarithm at $a=b e^{-h}$ with error $O_b(h^3)$ as $h\downarrow0$. A shared warmer stationary pair can achieve exact equality in both cold scores only if the flat Fourier column $K e_0$ takes at most two distinct bulk values. The prime arcsine law excludes this exceptional geometry at all sufficiently large primes, for *every* pair of distinct floors. These are a constructive local estimate and an exact obstruction. The estimates below do not give a field-uniform positive deficit or an all-prime cold bound.

## Exact loss of a fixed opposite reference

Use the [paired score](paired-trial-49.md) at the true same-side mark $x=P_0/\sqrt n$. Let $P,R$ be the two cold mean-one stationary rows, $W=1+(1-1/n)a$, $w_0=1$, $w_i=a/n$ on the bulk, $E_bF=n^{-1}\sum_{i\ne0}F_i$. Write $v=\ell/P$ and $r=Q/R$ for a nonnegative feasible same-side trial and an opposite mean-one reference, respectively. For $f=\ell_0/\sqrt n$, $g=Q_0/\sqrt n$, and $H=E_b\sqrt{\ell Q}$, the score at any $0<y<1/g$ is $S(y)=f/y+aH^2/(1-gy)$. Since $PR=nw/W$ and opposite rows pair to one in normalized counting measure,

\[
 W-S(x)
 =a\left(E_b v-\frac{(E_b\sqrt{vr})^2}{E_b r}\right)
 =a\min_{k\ge0}E_b(\sqrt v-k\sqrt r)^2.                         \tag{1}
\]

Here $1-xg=(a/W) E_b r>0$ and $v_0+aE_bv=W$. For positive $Q$, every feasible trial has positive bulk mass if both Paley frequency sectors are nonempty, since a multiple of the marked point mass uses both sectors.

Equip the coordinates with the inner product having weights $w_i/W$. Let $T_+=V_\sigma/P$, $T_-=V_{-\sigma}/R$ be the two relative tangent spaces. They and the constants form an orthogonal decomposition. Put $p=\mathrm{proj}_{T_+}e_0$, $q=\mathrm{proj}_{T_-}e_0$, so $p+q=e_0-\mathbf1/W$, $v-1\in T_+$, $r-1\in T_-$. At equality in (1) there are scalars $d$ and $\kappa>0$ with $v-\kappa r=d e_0$. Projection onto the three summands gives precisely

\[
 \kappa=1-d/W,\qquad v=1+d p,\qquad r=1-(d/\kappa)q.              \tag{2}
\]

Conversely every such nonnegative pair gives equality. Positive marked leverage $p_0,q_0>0$ follows from a nonzero cosine mode of each sector taking value one at the mark. The branch condition $f\ge Wgx^2$ consequently amounts to $d\ge0$ on the equality locus, since $v_0-r_0=d(p_0+q_0/\kappa)$. Thus the attainable references for a sharp lower score follow an explicit one-dimensional ray, restricted by positivity. This describes the optimum over all same-side trials.

There is a quantitative one-sided witness. Take any $u\in T_-$ with $u_0=0$ and $\|u\|_\infty\le1$. For the scalar $k=E_b\sqrt{vr}/E_b r$, orthogonality gives $E_b(vu)=0$, hence

\[
 k^2 |E_b(ru)|\le
 \sqrt{(W-S(x))/a}\,(\sqrt{E_bv}+k\sqrt{E_b r}).
                                                                    \tag{3}
\]

This follows by factoring $v-k^2r$ and applying Cauchy–Schwarz. In particular $k\sqrt{E_br}\le\sqrt{E_bv}$. A bounded zero-mark test correlated with the reference proves a deficit whenever the bulk overlap stays positive quantitatively.

## Constructing a local enclosure at a colder floor

Use subscripts $b$ for the warm data and their relative tangents. Multiplying the marked weight by $e^h$ is equivalent, by scaling all weights, to moving the floor to $a=b e^{-h}$. Differentiating the mean-one rows at $h=0$ gives $P'_b/P_b=p_b$, $R'_b/R_b=q_b$. Indeed the two log derivatives lie in their respective tangents and their sum is $e_0-\mathbf1/W_b$ by the product identity. From a single warm computation use

\[
 Q=R_b,\qquad \ell=P_b(1+2h p_b).                                \tag{4}
\]

The extrapolant is in the correct affine space, has mean one, and is positive for all sufficiently small $h>0$ at fixed field. No cold coordinate enters (4). The physical cold rows are analytic locally, so the cold relative ratios satisfy $v=1+h p_b+O(h^2)$ and $r=1-h q_b+O(h^2)$. On the bulk $p_b+q_b=-1/W_b$. Taking $k=1-h/(2W_b)$ in (1) proves $0\le G=W-S(x)=O(h^4)$.

The function $S(y)$ is convex. At $x$, with $t=xg=r_0/W$, its exact derivative is

\[
 x S'(x)=\frac{r_0-v_0-G t}{1-t}=-h+O(h^2).
\]

The last equality uses $p_{b,0}+q_{b,0}=1-1/W_b>0$. The smaller solution $x_-$ of $S(y)=W$ lies below $x$. Convexity gives $0\le x-x_-\le G/|S'(x)|=O(xh^3)$, including $G=0$. This root uses only (4) via the quadratic in round 49. Swapping sectors, the two lower estimates for $\log(\sqrt W x)$ give a two-sided enclosure of the plus mark. No uniform radius or uniform Taylor constant has been established as the prime varies.

## Simultaneous exact scores force a two-valued flat bulk column

Suppose that for *both* sectors the reference is the opposite physical row at the same $b\ne a$, and that each true cold score attains $W$ for some feasible same-side trial. The trials can be chosen independently and no branch assumption is needed. Applying (2) in both directions gives
\[
 P_b/P=1+s p,\qquad R_b/R=1+t q
\]
for some nonzero $s,t$. Neither row can stay fixed between two distinct floors, since its mark varies strictly with log marked weight at derivative $P_0 p_0>0$ or $R_0 q_0>0$. The bulk product of these ratios equals $b W/(a W_b)$. Using $q_i=-1/W-p_i$ there gives a quadratic polynomial in $p_i$ with nonzero quadratic coefficient $-st$. Thus $p$ takes at most two bulk values.

Here is why this restriction reaches the *flat* Fourier column even if the chosen floors are cold. Let $A$ be the algebra of real vectors constant on each of the resulting bulk cells, with the mark its own cell. It equals $\mathrm{span}\{\mathbf1,e_0,p\}$. The cold relative tangent projections preserve $A$, since they kill constants, send $e_0$ to $p,q$, and send $p$ to $p,0$, respectively. For $t$ close to $a$ one can solve the relative product equation in $A$:
\[
 (1+u)(1+v)=\frac{w(t)/W_t}{w(a)/W},\qquad
 u\in A\cap T_+,\quad v\in A\cap T_- .
\]
For precision, project this equation to the mean-zero subspace of $A$ in the cold weighted inner product. Its linearization $(u,v)\mapsto u+v$ is an isomorphism onto that subspace. Its constant equation is automatic by orthogonality of $u,v,\mathbf1$ and the unit weighted mean of the right side. The finite-dimensional implicit function theorem gives positive factors, and stationarity identifies them as $P_t/P,R_t/R$. By real analyticity and the identity theorem for each within-cell difference, these ratios belong to $A$ for every $t>0$. At $t=n$, both flat rows equal one. Closure under reciprocals of positive elements then puts $P,R$ themselves in $A$, hence every physical row and its derivative is in $A$.

At $t=n$ the relative plus tangent is just the usual sector $V_\sigma$, so its projection of $e_0$ is $((I-J)+\sigma K)e_0/2$. Its bulk takes at most two values. This proves the promised necessary condition on $Ke_0$ without a stationary solve at either floor. The [prime Jacobi arcsine law](fourier.md) gives positive limiting mass in three disjoint bulk intervals for the scaled column, which excludes this possibility at every sufficiently large eligible prime. Compactness of the trial polytopes gives a strictly positive optimum deficit in at least one sign at each such field and pair of floors. The size of this deficit may tend to zero. The fixed positive tolerance in the continuation stencil is compatible with this theorem.

The two-value condition is sharp for local simultaneous equality. Suppose instead that the flat column takes at most two bulk values and both sectors are nontrivial. At the flat floor its projected marked vectors span, with the constants, the same cell algebra $A$ of dimension three. (A single bulk value would put two nonzero orthogonal tangents and the constant in dimension two.) The preceding implicit-function argument starting at the flat floor puts every stationary row in $A$. At any other floor its relative projection of $e_0$ in each sector is the corresponding relative log derivative, which is in $A$. The two projections and the constant are nonzero and mutually orthogonal. Consequently the intersection of each relative tangent with $A$ is one-dimensional. In particular $R_b/R=1+s q$ for all $b$. For $b>a$ close enough, $s<0$ by strict marked monotonicity, and $s\to0$ as $b\downarrow a$. Set $d=-s/(1-s/W)$ in (2). The resulting same-side trial is positive and satisfies the branch condition. The construction in the other sign works on a common neighborhood. Thus simultaneous exact certificates for *some* distinct floors imply the two-value condition, and that condition guarantees simultaneous exact certificates on a right neighborhood of *each* floor.

## Finite checks and next tests

The [checker](astra-ref-50-check.py) proposes (4) from the warm rows and their first derivatives at $b=11/20$, rounds both Fourier trials to dyadic coefficients, and checks the smaller roots for $a=1/2$ using Arb at 192 bits. It uses neither a cold solve nor optimization over the same-side trial. The four [records](astra-ref-50-checks.jsonl) give
\[
 0.0056794<m_{97}(1/2)<0.0057495,\qquad
 0.0151781<m_{173}(1/2)<0.0152525 .
\]
They also prove that entries 1, 2 and 3 of the flat column are distinct in both fields. Replay with `.venv/bin/python -B research/astra-ref-50-check.py --replay research/astra-ref-50-checks.jsonl`. The enclosed marks concern these two primes only.

1. At a fixed prime-uniform warm-to-cold step, test positivity of (4) and bound its computed lower-root losses in both signs, starting with the fixed $a=1/2$ stencil budget. A subsequence with a nonpositive trial entry, or a lower log root bounded strictly below the negative budget in one sign, refutes that particular step and predictor. A uniformly useful chain from the proven hot interval would additionally need certified input rows/tangents at each step or a method for passing their enclosures forward.
2. At a proposed fixed warm floor, quantify the fixed-reference gap using bounded zero-mark opposite tangent witnesses in (3), or rigorous fixed-reference duals evaluated at the desired target. An unbounded prime sequence with score optimum below $W$ by a fixed positive amount at the prescribed lower target rules out that common floor even with arbitrary same-side optimization. The exact two-value obstruction at the physical mark alone does not furnish such a margin.
