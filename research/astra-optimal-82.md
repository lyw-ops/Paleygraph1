# Clipped entropy on the full optimal face and its even part

A true optimal row with small clipped exterior entropy yields an even true optimizer with the same entropy upper up to an additive \(o(1)\) when the cutoff may grow more slowly. This works for arbitrarily small exterior mass and preserves every fixed even terminal height price. At the same cutoff the reduction can fail. At primes 257 and 409 the entire larger optimal face is a line segment, and its unique even row has strictly larger clipped entropy than the full-face minimum at \(B=1\). All the optimizers on the respective segments have exactly the same masked terminal height at times five and six.

## A uniform upper after lowering the cutoff

On \(G=\widehat Q\), let \(q\) be any genuine marked primary optimizer, and let \(Pq_i=(q_i+q_{-i})/2\). Reflection preserves the Fourier sector and fixes the mark. Thus \(Pq\) is a genuine optimizer on the same face. More generally let \(E\) be an inversion-stable exterior, including the case \(E=G\setminus\{0\}\). For \(B>0\) set
\[
 x=(q-B/n)_+\mathbf1_E,\qquad M=\sum x_i>0,\qquad
 T=\{i:x_i>0\},\qquad
 \mathcal D=\sum_i(x_i/M)\log(nx_i/M).
\]
All logarithms are natural and zero terms are omitted. At \(0<c<1/2\) take the actual clipped row \(x'=(Pq-cB/n)_+\mathbf1_E\), with total mass \(M'\) and entropy \(\mathcal D'\) at the same normalization. Uniformly over the prime, cutoff and optimal face,
\[
 M'\ge M+(1-2c)B|T|/n,\qquad
 \boxed{\quad\mathcal D'\le\mathcal D+
                 \log\frac{1-c}{1-2c}.\quad}                          \tag{1}
\]
In fact let \(U=T\cup(-T)\) and \(z=q\mathbf1_E-x\). On \(U\), \(Pz_i\ge B/(2n)\). Hence \(y=x'-Px\) is nonnegative there, with \(y_i=Pz_i-cB/n\). Off \(U\), \(Px=0\) and \(0\le y=x'\le(1-c)B/n\) on \(E\). The same cap holds on \(U\). Also
\[
 \Delta:=\sum y_i\ge\sum_U(Pz_i-cB/n)
          \ge (|T|-c|U|)B/n\ge(1-2c)|T|B/n.
\]
The middle inequality retains the full \(B/n\) on each old clipped site, after averaging within \(U\). It follows that \(ny_i/\Delta\le n(1-c)/[(1-2c)|T|]\). The old relative entropy is at least \(\log(n/|T|)\) by comparison with uniform probability on \(T\), so the relative entropy of \(y/\Delta\) is at most \(\mathcal D+\log((1-c)/(1-2c))\). Convexity gives relative entropy at most \(\mathcal D\) for \(Px/M\), and one more application to the actual mixture \(x'/M'\) proves (1). Bounding the entropy of the added component from its point cap alone would introduce the uncontrolled quantity \(\log(1/M')\).

In particular \(c=1/4\) costs at most \(\log(3/2)\). If \(B\to\infty\), the new cutoff \(\sqrt B\) costs only \(O(B^{-1/2})\). Thus existence of a true row with clipped entropy \(o(D(p))\) at *some* growing \(B=o(D(p))\) is equivalent to existence within the even true face at some such cutoff. The same statement holds for an \(O(D(p))\) bound. The argument applies at each prime and uses no assumption on face dimension.

## The same actual terminal price

Fix any one of the true opposite pin and companion terminal pairs \(R,Z\) of [round 79](terminal-height-79.md), with length \(d\) and deficit \(r=(R)_-\) on the bulk. The fields and their height and deficit masks are even, by symmetry of the initial mark and the Jacobi multiplier at every iteration. For any fixed even nonnegative charge \(h\), including \(Z\mathbf1_{r>u,\,Z>(2d-1)u}\), one has \(\sum h_i(Pq)_i=\sum h_iq_i\). This compares two genuine optimizers at the same time, and can include an arbitrary inversion-stable deletion in the fixed mask.

There is also a density-sensitive bound. For \(0\le l<t\),
\[
 \sum_{l<(Pq)_i\le t/2}h_i(Pq)_i
       \le 2\sum_{l<q_i\le t}h_iq_i.                                  \tag{2}
\]
On each charged inverse pair both entries of \(q\) are at most \(t\), and its larger entry exceeds \(l\) and supplies at least half of the pair mass. Fixed points obey the same inequality. When \(l=0\) the factor two can be dropped because both entries are then accounted for. For an original nonsymmetric deleted set \(F\), the left side can delete \(F\cup(-F)\) and the right side can delete just \(F\). This costs at most a factor two in the number deleted. Taking \(l=k_\delta d/n\) keeps the true lower density floor. If \(t=\alpha M/\sqrt n\), the new upper threshold in the row's own units is \(\alpha' M'/\sqrt n\) with \(\alpha'=\alpha M/(2M')\). Neither (1) nor (2) bounds \(M'/M\) from above. A prescribed cutoff, prescribed relative density threshold, or non-even mask therefore requires its own comparison. Formula (1) also allows the [common high-density deletion](entropy-filter-82.md) to be obtained afresh for the even optimizer using its own \(M'\).

## Sharp obstruction to automatic evenization at the original floor

Along any two-sided feasible odd direction \(h_{-i}=-h_i\) from an even marked optimizer \(e\), every fixed even terminal measurement is constant. Suppose a positive pair at the clipping floor \(B/n\) in the exterior has nonzero \(h_i\), and the even row has positive mass \(M\) strictly above the floor there. Write \(\mathcal D(t)\) for the exterior clipped entropy of \(e+th\) at this same cutoff. At fixed prime, as \(t\to0\),
\[
 \mathcal D(t)=\mathcal D(0)+
   \frac{|t|\log |t|}{M}
   \sum_{\{i,-i\}\subset E:\,e_i=B/n}|h_i|+O(|t|),                  \tag{3}
\]
summing once per inverse pair. The odd direction vanishes at fixed points. A crossing pair creates the clipped amount \(|t h_i|\) on one site and zero on the other. Terms already positive vary smoothly. Use \(\mathcal D=\log(n/M)+M^{-1}\sum x_i\log x_i\), with the new mass differing by \(O(|t|)\), to obtain (3). Such a row cannot minimize the full clipped entropy at that cutoff. Even when the initial row has no site exactly on the floor, a finite step can cross one.

## An entropy projection keeping the original mass and time

A different certificate keeps the original \(B,M\) when the signed Jacobi test needs them. Take \(E=G\setminus\{0\}\) and any positive split on \(E\) satisfying
\[
 (q_i-B/n)_+\le v_i\le q_i,\qquad \sum_E v_i=M>0.
\]
Set \(v_0=0\). Then \(0\le q_i-v_i\le B/n\) on \(E\), and the discarded root is \(O(n^{-1/2})\) on a genuine optimum. Write \(\mathcal D_v=\sum_E(v_i/M)\log(nv_i/M)\). The high-density collision estimate of the [signed Jacobi test](entropy-filter-82.md) holds with this mass and entropy. Explicitly, for \(\alpha\log p\ge C(1+\mathcal D_v)\),
\[
 n\sum_{\substack{i\ne0\\ \sqrt n q_i>\alpha M}}q_i^2
       \le C\{1+B+M^2(1+\mathcal D_v)\}.                              \tag{4}
\]
Indeed, for a nonempty row subset \(S\) above the density floor, let \(L=n\sum_S q_i^2,\ m=(\sum_S q_i)^2/\sum_S q_i^2\), and use the same signed Jacobi field \(W\) with normalized row weights \(q\mathbf1_S/\sum_Sq_i\). In its exact \(q\)-mean, the error on replacing the exterior by \(v\) is bounded by \(\sqrt{B/n}\|W\|_2\), because \(\sum_E(q_i-v_i)^2\le B/n\). The omitted root costs \(O(n^{-1/2})\). Thus the exponential test applies unaltered to \(v/M\) with \(\rho=L/(\sqrt n M\sum_Sq_i)>\alpha\), proving (4). Furthermore the ordinary hard-clipped mass \(M_0\) of this same row at \(B\) is at most \(M\). For a supercritical gap and \(B=o(d)\) the [terminal theorem](terminal-height-79.md) gives \(M_0>0\), permits at least \(H^2/M^2\) deletions, and puts its surviving joint band below \(2C_0M/\sqrt n\). Consequently (4) and this actual terminal height statement use one row at the same time and mass scale. On the specific even optimizer above one can take \(v=Px\), for which \(M\) is unchanged and \(\mathcal D_v\le\mathcal D\). The quadratic cap and surviving height then use the old \(M\), independently of \(M'\) in (1).

This permits a convex search on the genuine even face for a sufficient certificate. Fix \(B,M\) and any upper limit on a *fixed even linear* terminal price for the selected time. Impose that bound along with the exact marked-face equations, positivity, \(0\le v_i\le q_i,\ q_i-v_i\le B/n\) on \(E\), and \(\sum v_i=M\). The least \(\sum_E(v_i/M)\log(nv_i/M)\) is exactly the same with or without requiring both rows even: averaging the two rows with their reflections preserves every constraint and can only decrease the objective. For a fixed feasible \(q\) the inner minimizer is explicit:
\[
 v_i=\min\{q_i,\max((q_i-B/n)_+,\lambda)\},                             \tag{5}
\]
where the common \(\lambda\ge0\) gives total mass \(M\). The sum varies continuously from the sum of the lower bounds to the sum of the upper bounds. The strictly increasing derivative of \(v\log v\) equalizes all unsaturated positive entries. Equivalently, if one endpoint allows a transfer from a larger value to a smaller one, strict convexity improves the pair. This proves (5), including endpoint masses by continuity. When \(M\) is the hard-clipped mass, (5) returns that hard clip. A larger prescribed mass can give a strictly less concentrated probability. The certificate applies (4) directly to this projected probability and does not assert that it is the hard clip at \(B\).

## Global minima at two actual terminal times

The [384-bit checker](astra-optimal-82-check.py) certifies the latter possibility at the actual finite pin and mask conventions of [round 81](astra-cover-81.md), with \(E=G\setminus\{0\}\), \(B=1\), \(u=1/100\), and \(a=1\). The final column is the common linear price \(\sum_{i\ne0:R(i)<-u}q_iZ(i)\) on the entire full face. [Interval records](astra-optimal-82-checks.jsonl)

| Prime | Terminal time | Even entropy | Minimum full-face entropy | Gain from odd displacement | Common masked terminal height |
|---:|---:|---:|---:|---:|---:|
| 257 | 5 | 1.337783072 | 1.337253192 | 0.000529880 | 2.093942673 |
| 409 | 6 | 1.359201444 | 1.356307500 | 0.002893944 | 2.090234387 |

At both primes the genuine complementary positive pair occupies all inverse orbits between them, with only the root shared. The square opposite-cosine equations on the exposed primary support are certified invertible at fixed mark, so the even primary row \(e\) is unique. Any other optimizer has that even part and is supported on the same orbits. In the odd sector the forbidden sine matrix has a certified invertible minor with one column omitted. Thus the full face consists exactly of \(e+th\) for \(|t|\le t_*=\min_{h_i\ne0}e_i/|h_i|\). The checker solves the odd system at unit pivot and certifies the limiting coordinate. Reflection allows \(0\le t\le t_*\). On each interval between crossings of the floor, the unnormalized clipped row is affine. Its normalization traces the entire line segment between the two normalized endpoint laws. On such a segment a positive trial probability \(w\) from its relative interior gives the lower bound \(\sum\mu_i\log(nw_i)\) for \(\mathcal D(\mu)\). This linear lower bound takes its minimum at an endpoint. The same trial's own entropy gives an attainable upper bound. Certifying both endpoints on each of the two and four cells respectively gives the displayed global enclosures. These finite data do not impose the asymptotic terminal-depth conditions.

For the split projection (5) choose \(M\) equal to the clipped mass of the attainable near-minimizing nonsymmetric trial at each prime. These are about \(0.482163934\) and \(0.522810490\), respectively. Because the even primary row is unique, solving its scalar level equation certifies the minimum in the **whole** joint convex problem at this prescribed mass and common terminal price. The resulting relative entropies are in \((1.336136735,1.336136736)\) and \((1.341756993,1.341756994)\). Each is strictly below the corresponding minimum over all scalar-\(B\) hard clips, with the same mass as the associated feasible hard trial. The checker certifies all clamped and free-coordinate inequalities for the solved level.

## Ranked next tests

1. On the actual even marked face, test the fixed-mass projection (5) alongside the hard clip and seek a single growing cutoff with exterior entropy \(o(D(p))\) and one growing admissible time with a sufficiently small retained height price. The cutoff-flexible entropy reduction is lossless at this scale. Check the surviving density threshold using the same clipped mass as the candidate upper.
2. If the cutoff is fixed in advance, include every feasible odd sine direction on the exposed support. For a proposed even minimizer, a floor pair transverse to such a direction gives the strict failure (3). Along one-dimensional fibers the interval minorants above certify whether the nonsymmetric improvement survives a prescribed even terminal height constraint.
