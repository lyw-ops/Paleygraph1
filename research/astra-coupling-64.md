# How much of the two-face gap can one projected direction recover?

For the actual two optimal faces, one can compare the round-63 gain directly to the unrestricted improvement by a score-independent operator on their attainable supports. Near a collapsing generic coupling there is a sign criterion for loss of the entire fraction. At the true prime face for 97 this loss occurs on a continuum of relative-interior references. A whole-ray line search on the first projected direction cannot improve the fraction. Recomputing the direction on the newly reached support and then taking a whole-ray line search gives the global minimum with a unique minimizing pair of inversion-orbit laws.

## A support and leverage comparison at every prime

Use sign scores $Z_s(i)=s\sqrt n\,v_t(i)$, the true attainable inversion orbits, and their **total** probabilities. Set $J_t(b)=M_t(b)-E_t/4$ and $\Delta=J_t(b)-J_t^{\rm face}$. Choose a relatively interior reference $b$ generic in the sense of [the increasing forest](astra-global-63.md). Every shared internal cut then fixes both cumulative probabilities throughout their independent faces. Let $w_e>0$ be the overlap lengths, $W=\operatorname{diag}(w)$, and $C_e$ the maximum of the two scores. The projected residual, variance, and positive maximum are $r,V,R$ from round 63.

On each sign omit the marked orbit and use only attainable bulk orbits. Denote its original per-site optimal probability at the mark by $b_s(0)$, and set $u_{s,i}=|i|b_s(0)$, where $|i|$ is the orbit cardinality. Translation of any feasible whole row to an individual site proves its site probability is at most its optimal mark, hence every full-face probability satisfies $0\le q_s(i)\le u_{s,i}$. Let $A=\operatorname{diag}(\sqrt{u_{s,i}})$ across the two bulk supports. Write $T$ for the direct sum of the true marginal tangent spaces there, with zero extension on the mark and off support. These are exactly the kernels of the mass and all real and imaginary forbidden Fourier equations with those zeros. Every such tangent is realized locally at $b$ by positivity. Let $P$ be the ordinary orthogonal projector onto $A^{-1}T$.

On $T$, let $Lh$ be the unique signed edge change with those two marginals, extending $h$ by zero at the marks. The generic shared-cut condition and leaf elimination give existence and uniqueness. This is a linear forest operation. Define
\[
 B=W^{-1/2}LAP,\qquad H_B=\operatorname{proj}_{\operatorname{ran}B},\qquad
 K=\|B\|_{2\to2}\max_e\sqrt{(H_B)_{ee}/w_e},\qquad y=W^{1/2}r.
\]
The constrained edge tangent in the $W^{-1/2}$ coordinates equals $\operatorname{ran} B$. Every signed edge change preserving all marginal equations has marginal tangents in $T$ and equals their unique lift. Conversely every lift preserves all equations. Consequently $y\in\operatorname{ran} B$, either from the residual normal equations or by lifting its own marginal changes.

If $V>0$ then
\[
 \boxed{\qquad V/R\ \le\ \Delta\ \le\ D\|B^{\mathsf T}y\|_2
                \ \le\ D K\,V/R,\quad
 D=\sqrt{2\sum_s(1-b_s(0))}<2 .\qquad}                         \tag{1}
\]
The first inequality is the actual step. For the upper bound let $h=q-b$ for an arbitrary pair of true target rows. Coordinate caps and nonnegativity give $\|A^{-1}h\|^2\le\sum_{s,i}(q_s(i)^2+b_s(i)^2)/u_{s,i}\le D^2$. The attained scalar minorant of round 63 agrees with $C$ on the whole reference forest. Its integral changes by $C^{\mathsf T}Lh=r^{\mathsf T}Lh$, because the projected equation prices pair to zero. Therefore $M_t(b)-M_t(q)\le-y^{\mathsf T}B A^{-1}h$. This proves the middle bound. For each edge, $|y_e|\le\sqrt{(H_B)_{ee}}\|y\|_2$ by orthogonal projection. Hence $R\le\|y\|_2\max_e\sqrt{(H_B)_{ee}/w_e}$ and $\|y\|_2^2=V$, proving the last bound. At $V=0$ the same minorant argument gives $\Delta=0$. All costs in (1) refer to whole pairs at the same time with the same terminal charge. The reference tangent bases, cap matrix and signed forest lift determine $K$.

The directional ceiling can also be computed without any inverse overlap lengths. On the true tangent space, the row functional of $B^{\mathsf T}y$ is $k\mapsto C^{\mathsf T}LAPk$. Thus the ceiling is constant across a fixed overlap chamber for these scores even as some overlap weights go to zero. In tangent coordinates with a marginal basis matrix $S$, put $g=(LS)^{\mathsf T}C$ and $Q=S^{\mathsf T}A^{-2}S$. Then $\|B^{\mathsf T}y\|^2=g^{\mathsf T}Q^{-1}g$, by the dual norm identity for the metric $Q$. Singleton faces contribute zero to the cap radius and can be omitted from $D$.

## The sign test at a collapsing coupling

In any fixed generic chamber, parameterize all marginal tangents by $a\in\mathbb R^d$ and call the lifted edge rows $D_e$, so $\delta w_e=D_e a$. Along an affine path of positive references toward its boundary, suppose there are thin edges $I$ with $w_e=x k_e$ ($k_e>0$, $x\downarrow0$) and all remaining weights have positive limits. Assume $\{D_e:e\in I\}$ spans the tangent dual. Write
\[
 H=\sum_{e\in I}D_e^{\mathsf T}D_e/k_e,\qquad
 g=\sum_e C_e D_e^{\mathsf T},\qquad
 \ell_e=D_eH^{-1}g/k_e\quad(e\in I).
\]
Take $g\ne0$. The weighted Gram matrix is $G=H/x+O(1)$, so $G^{-1}g=x H^{-1}g+O(x^2)$. The round-63 edge densities are $r_e=D_eG^{-1}g/w_e$ and $V=g^{\mathsf T}G^{-1}g=xg^{\mathsf T}H^{-1}g+O(x^2)$. The thin densities converge to $\ell_e$ with error $O(x)$, and every regular density is $O(x)$.

* If any $\ell_e>0$, then $V/R=\Theta(x)$. If the limiting objective exceeds the full-face minimum, the captured fraction tends to zero.
* If every $\ell_e\le0$, then $V/R=\Theta(1)$. At least one $\ell_e$ is strictly negative by spanning. The corresponding negative weighted mass has size $\gg x$. Zero total weighted residual forces $R\gg x$. Every positive residual is on a regular or zero-limit edge, so $R=O(x)$.

This classification holds on the actual masks at every prime with the stated chamber geometry. Its asymptotic constants concern the chosen face, time and affine path. In the first case the $x^{-1}$ loss in the factor of (1) is attainable. The fixed marginal tangent and cap maps and the bound $w_e\gg x$ give $\|B\|=O(x^{-1/2})$. The leverage factor is $O(x^{-1/2})$ since diagonal projector entries are at most one. A fixed positive limiting gap and $V/R=\Theta(x)$ force $K\gg x^{-1}$ by (1).

## A continuum on the true prime face and a second projected direction

At $p=97$, $t=32$, the plus coordinates of the cyclotomic parametrization are the unnormalized anchored amplitudes $(u,v)$ of the inversion orbits 10 and 21. The minus face is a singleton. On $b=(x,x)$ for every $0<x\le10^{-8}$ there are 15 plus and 11 minus atoms, with distinct internal cuts and 25 positive overlap edges. Precisely two edges vanish at the limit. Each carries an entire free plus orbit, with rows $(a,0),(0,a)$ and weights $ax$, where $a$ is twice the inverse normalizing mass of the anchored plus solution. Thus $H=a I$. [Cyclotomic two-anchor parametrization](astra-face-54.md)

The cost gradient satisfies
\[
 .307642786<g_u<.307642787,\qquad -.135293843<g_v<-.135293842.
\]
Here and below the [checker](astra-coupling-64-check.py) verifies closed outward enclosures, with strict inequalities at the quoted exterior endpoints. It checks the regular affine weights throughout the interval and removes the two Gram poles before the two-by-two interval solve. If $z=G^{-1}g/x$, the two small-edge residual densities are exactly $z_u,z_v$ and all other densities are smaller than $z_u$. The true step therefore hits orbit 10 at $\lambda=1/z_u$, making its actual probability zero. Every larger positive step along that marginal ray would make it negative. Even exact re-sorting cannot extend this ray. Throughout the interval,
\[
 .367133829\,x < V/R < .367149531\,x,\qquad
 .003883767 < \Delta < .003883770 .                                \tag{2}
\]
This rules out a reference-independent positive capture fraction on an actual prime face. Its dependence on $x$ realizes the order loss in (1).

For the second direction, stay on the true subface $u=0$ reached by the first step. Its remaining coordinate is $v=x(1-z_v/z_u)$, positive and less than $.001$. The same regular forest weights remain positive from $v=0$ through $.001$ on this subface, and the derivative in $v$ remains $g_v<0$. The signed increasing-coupling projection on the remaining one-dimensional tangent therefore points toward **increasing** $v$. Recompute the direction here and allow a full feasible line search along it, re-sorting the two sign laws at crossings.

For the resulting solution, let $d=(d_0,d_u,d_v)$ be the affine coefficients of plus survival minus minus survival on the scalar interval with lower endpoint the score of minus orbit 24. Its width is $l>0$. Exactly
\[
 u_*=0,\qquad v_*=-d_0/d_v\in(.039041321,.039041322).
\]
All other nontrivial scalar intervals have a strict survival order at this point. In the survival objective each interval contributes its width times the larger survival. On every strict interval use that larger side as a global affine minorant. On the unique tied interval mix the two survivals, using a plus proportion $m\in(.186193217,.186193218)$ chosen so the total minorant's $v$ derivative vanishes. The resulting $u$ derivative lies in $(.182895591,.182895592)$. Every full-face row has $u\ge0$. The affine minorant thus proves global optimality on the entire two-dimensional even plus face. On $u=0$ the two one-sided $v$ derivatives are strictly negative and strictly positive, so convexity proves uniqueness there. The strict $u$ derivative excludes every other feasible even point. The attained charged objective is in $(1.506178301,1.506178302)$. These calculations certify a continuum obstruction and its global solution by a renewed direction. The prime-uniform late objective remains open. [Two replay records](astra-coupling-64-checks.jsonl)

Evenization preserves the score laws, so this minimum holds over unrestricted rows as well. In fact, there are several unrestricted minimizing rows. The plus minimizer is positive on thirteen non-self-inverse orbit pairs, including orbit 21. Odd perturbations on these pairs automatically preserve mass, mark and the real Fourier constraints. The forbidden inverse pairs impose twelve independent or redundant real sine equations, so their common kernel has a nonzero odd perturbation. Sufficiently small multiples preserve nonnegativity and the total mass on each orbit, hence the objective.

1. At one growing late time per prime compare the reference charged excess, $V/R$ and the restricted norm in (1) on the **same** generic actual forest. An update with $(J_t(b)-V/R)/t\le o(1)$ passes the desired upper test. A subsequence with $J_t(b)-D\|B^{\mathsf T}y\|\ge\eta t$ at every late time fails the full-face window estimate. A large condition number alone decides neither test.
2. On a projected ray stopped by a true zero, recompute the residual on the surviving support and use a full feasible line search on that new direction. A charged $o(t)$ upper bound at one growing late time per prime passes. A pair whose attaining scalar subgradients mix to a global support price with objective at least $E_t/4+\eta t$ at all late times on a prime subsequence fails the window estimate. The rank-one second step passes the global-optimum test at $p=97,t=32$. For later tests, a certificate of optimality must price the omitted coordinates too.
