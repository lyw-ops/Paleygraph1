# A global Fourier-feasible descent for the charged score of two true endpoint rows

Let $p\equiv1\pmod4$ be prime, $n=(p-1)/2$, and use the [actual cold scores](astra-tail-53.md) $Z_s(i)=s\sqrt n\,v_t(i)$, $E_t=\|v_t\|_2^2$. Keep the whole probability face for each sign, exposed by a complementary true optimum. Its position-space equations include all forbidden Fourier zeros, the mass and the optimal mark. Evenization preserves every score law. Below a site can mean an inversion orbit, with its **total** probability and with the forbidden Fourier columns averaged on that orbit. Discard an orbit only if every true probability on that face vanishes there. Write $A_s$ for the resulting attainable support, $F_s$ for the true even face, and $d_s=\dim F_s$.

There is a single weighted least-squares descent using both actual supports and every Fourier equation. Its explicit lower bound on the reduction in $M_t-E_t/4$ is strict unless its residual vanishes. The same relative-interior pair can be chosen at every prime so that at **every** late time a zero residual certifies the unrestricted face minimum there. The theorem gives neither an asymptotic lower bound on a nonzero gain nor the all-prime charged upper estimate.

## One positive trial on both faces at once

Fix relative-interior references $b_s\in F_s$. Sort each side's sites in increasing order of $Z_s$, with deterministic tie breaks. Its cumulative masses partition the unit interval. For every positive-length overlap $e$ of a plus cell $i$ and a minus cell $j$, write $w_e$ for the length and $C_e=\max(Z_+(i),Z_-(j))$. The weights form an increasing coupling of the two score laws and $M_t(b)=\sum_e w_e C_e$.

Let $H$ be the span on the edges of the constant and of the site functions imposing the full true equations on either marginal. These include the real and imaginary parts of each forbidden character and the marked-coordinate indicator. Set
\[
 r=C-\Pi_H C,\quad V=\sum_e w_e r_e^2,\quad
 R=\max_e r_e, \qquad \langle f,g\rangle_w=\sum_e w_e f_e g_e.
\]
Redundant equations require only a span projection. If $r\ne0$, then $R>0$ because its mean vanishes. For $0<\lambda\le1/R$ put $w'_e=w_e(1-\lambda r_e)$. Its marginals $b'_s$ are nonnegative, have the original mass and root, are supported on the actual exposed face and satisfy **all** forbidden Fourier equations. The surviving edges are still ordered on each side, so their increasing coupling realizes the true new quantile integral, even for ties or at a vanished edge. In particular
\[
 \boxed{\quad M_t(b')-E_t/4=M_t(b)-E_t/4-\lambda V.\quad}       \tag{1}
\]
Indeed $\langle C,r\rangle_w=V$. The largest allowed step gains $V/R$. This evaluates one pair of whole rows across all thresholds. For the update on either face itself, leave the common pointwise mass on the diagonal and couple the positive and negative parts of $b'_s-b_s$ directly. The edge weights above couple the *two signs' score laws*. That coupling serves a different purpose than the same-sign net transfers. For one preselected trial per time, [round 62](astra-weighted-62.md) gives nonwrapping net transfers in the same typical primitive order throughout the late window, including after splitting orbit masses evenly into sites.

## Vanishing residual decides the global minimum at generic references

Choose the references outside the following finite union of proper hyperplanes of $F_+\times F_-$. For the site orders at every time of interest, exclude every internal plus/minus prefix equality whose two sides do not coincide identically on the entire product. Such a choice is possible arbitrarily close to any relative-interior pair, over any finite collection of times. A surviving shared cut has **fixed cumulative mass on both whole faces**, since the two marginals vary independently. This also covers zero-dimensional faces.

The overlapped cells form a bipartite forest. Between consecutive shared cuts, beginning with 0 and ending with 1, the first edge starts a component. Every subsequent step introduces a new vertex on only one side until a shared cut starts a new component. For the marginals of any other pair $q_s\in F_s$, the total masses of the plus and minus vertices in each component therefore agree. Leaf elimination supplies a signed edge weighting $u$ with marginals $q_s$. It need not be a positive coupling.

For a positive coupling comparison, choose two functions $f_s$ of the scalar score. Start at the smallest score $a$ with $f_+(a)+f_-(a)=a$. Between consecutive distinct scores allocate slope 1 to a face with the larger reference survival probability there, and slope 0 to the other. Either choice at a tie works. Both functions are nondecreasing, $f_+(z)+f_-(z)=z$, and
\[
 f_+(x)+f_-(y)\le\max(x,y),\qquad
 M_t(b)=\sum_s\mathbb E_{b_s} f_s(Z_s).
\]
The latter equality follows by the survival integral for the maximum on the increasing coupling. Equality consequently holds on *every* positive reference edge. If $r=0$, then $C\in H$, so the signed weighting $u$ integrates $C$ to the same value as $w$ by the full marginal moment equations. Hence
\[
 M_t(q)\ \ge\ \sum_s\mathbb E_{q_s} f_s(Z_s)
       = \sum_e u_e C_e = M_t(b).
\]
Together with (1) this proves the exact dichotomy. For non-generic references the step (1) always holds. A coincident prefix movable on one face can prevent the signed lift.

## A ceiling on improvement by arbitrary global net changes

A second estimate controls all target rows, including jumps through any number of the above ordering regions. Let $c_s$ be the volume barycenter of $F_s$ in its affine hull, equal to its unique point at dimension zero. Then every $q_s\in F_s$ obeys $q_s(i)\le(d_s+1)c_s(i)$. In positive dimension, for $0\le u\le1$ the set $u q_s+(1-u)F_s$ occupies a fraction $(1-u)^{d_s}$ of the volume and has its $i$-th coordinate at least $u q_s(i)$. Integrating the superlevel fractions proves the claim. In particular
\[
 \sum_i (q_s(i)-c_s(i))^2/c_s(i)\le d_s.                          \tag{2}
\]
This estimate allows arbitrarily uneven site probabilities. It uses actual face dimensions and entails no factor from the size of the group.

With reference $b=c$, construct the attained scalar minorant $F_{s,t}(i)=f_s(Z_s(i))$ above. Let $B_s$ span the full affine-equation site functions on $A_s$, including the constant. Define $\rho_s=\|F_{s,t}-\Pi_{B_s}F_{s,t}\|_{L^2(c_s)}$. Subtracting a function in $B_s$ cannot change the pairing with $q_s-c_s$. The preceding minorant, (2) and Cauchy–Schwarz give
\[
 0\le M_t(c)-M_t^{\rm face}\le\sum_s\sqrt{d_s}\,\rho_s.            \tag{3}
\]
Equality on shared cuts or within scores needs no genericity in this bound. For the genericity in the preceding section as well, choose $b_s=(1-\epsilon)c_s+\epsilon z_s$ for generic relative-interior $z_s$ and $0<\epsilon<1$. The same proof around $b$ uses its own prices, its own $L^2(b_s)$, and, for $d_s>0$, the factor $\sqrt{(d_s+1)/(1-\epsilon)-1}$. Singleton contributions vanish.

There is a one-sided variant at the actual least Euclidean norm references $m_s$, even if they have additional zeros. Let $l_s(i)=m_s(i)/|i|$, where $|i|$ is the inversion-orbit multiplicity (one per site without orbit aggregation). Minimality along the segment to $q_s$ gives $\langle l_s,q_s-m_s\rangle\ge0$ in unweighted orbit pairing. Likewise $k_s\ge0$ supported on the additional zeros of $m_s$ has nonnegative pairing. Use prices attained at $m$ and let
\[
 \rho_s^*=\inf_{g\in B_s,\, a\ge0,\, k_s}
 \|F_{s,t}-g-a l_s-k_s\|_{L^2(c_s)}.
\]
Any particular choices give a valid upper estimate. By (2), $\|q_s-m_s\|_{L^2(1/c_s)}\le2\sqrt{d_s}$. The sharper alternative $\sqrt{2(d_s+1)}$ follows from $\sum q_s^2/c_s,\sum m_s^2/c_s\le d_s+1$ and $q_s m_s\ge0$. Thus
\[
 M_t(m)-M_t^{\rm face}
 \le\sum_s \min(2\sqrt{d_s},\sqrt{2(d_s+1)})\,\rho_s^*.           \tag{4}
\]
The norm is on the entire attainable support even for the least-norm row. A one-sided price proportional to its density can be removed for free because the exact net direction cannot have negative density pairing. The charge cancels in comparisons (3)–(4) and is subtracted once from the reference when using either as a lower barrier.

The minimum-norm condition has an exact limitation here. Write $K_s$ for the cone of nonnegative price functions supported on the additional zeros. Every feasible tangent from $m_s$ satisfies the homogeneous equations and is nonnegative on those zeros. Conversely every such vector is feasible for a sufficiently small positive step, since the other coordinates of $m_s$ are strictly positive. The nonnegative dual of this tangent cone equals $B_s+K_s$. Its dual is the stated intersection and the finite-dimensional sum is polyhedral and closed. Thus $l_s\in B_s+K_s$. Adding $a l_s$ can simplify an explicit approximation, but leaves the *best* residual in (4) exactly equal to the distance to $B_s+K_s$. The same argument covers the gradient of **any** differentiable convex selector minimized at this reference. At a relative-interior selector all such gradients lie in $B_s$ itself. In particular, for the maximum-entropy true row $h_s$ the logarithm of its positive per-site probability is an exactly conserved net statistic on the entire attainable support (differentiate $\sum_i h_s(i)\log[h_s(i)/|i|]$). It supplies an explicit Fourier-equation price there. Adding families of such selector gradients cannot strengthen the optimized global price certificate. A genuinely smaller residual or an allowed descent (1) requires information about the actual score.

## Check and ranked tests

The [checker](astra-global-63-check.py) uses the [exact cyclotomic face columns](astra-face-54.md) at $p=97$ and the true cold time 32. From strictly positive plus anchors $1/1000,1/100$, the two full face dimensions are 2 and 0. Interval evaluation proves that 15 and 11 positive orbit atoms have distinct internal cumulative cuts and give one 25-edge tree. The two exact marginal tangent columns uniquely lift to its edges by differencing adjacent cuts. Their weighted two-by-two Gram system gives $r$. A safely rounded positive step with all edges retained lowers the actual charged cost by $(424824,424825)\times10^{-9}$. Integrating the target marginals afresh gives the same decrease. The final charged pair also beats the actual least-norm pair by $(1470120,1470121)\times10^{-9}$. One field/depth checks the construction. The proof and pass/fail tests above hold throughout every prime window. Reproduce the [record](astra-global-63-checks.jsonl) with `.venv/bin/python -B research/astra-global-63-check.py`.

1. At one time in $[D(p)/2,D(p)]$ through every sufficiently large prime, compute (or bound) the two-face projection $r$ on the actual increasing coupling. Define $V/R=0$ for $r=0$. A nonpositive limsup of $(M_t(b)-E_t/4-V/R)/t$ proves the desired upper bound with an explicit feasible net-only pair. If this quantity stays bounded below by a positive constant at all late times on unbounded primes, the single prescribed step fails there. For generic references any zero residual computes the exact full minimum.
2. On an unbounded prime sequence with positive reference excess throughout the late window, use the attained scalar prices in (3) or (4). If the reference excess minus the right side stays at least $\eta t$ at every late time for one fixed $\eta>0$, the **full-face** upper estimate fails on that sequence. If this certified lower endpoint fails that margin at even one late time on each sequence member, it gives no such obstruction there. The all-prime charged estimate and ordinary theta limit remain open.
