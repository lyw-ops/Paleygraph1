# Height-weighted collision on the true terminal face

An order-\(d\) bound for the inverse positive leverage at an early good time has a counting-measure consequence. There must be order \(n/d\) actual sites with both primary density and companion height of order \(d\), carrying positive primary mass. A single subset survives erasure and keeps comparable companion height at every time in a growing nearby interval. A height-weighted hinge also gives a different high-density alternative with a polynomial loss of leverage on the whole face.

## A simultaneous upper cutoff in both variables

Use any good terminal time \(b\) of [round 79](terminal-height-79.md), including the earlier time \(b\le D/13+O(1)\) from [round 86](astra-leverage-86.md). Fix a normalized larger mark \(\sqrt n a\ge1+\delta\), take the clipping floor \(B=0\), and use that time's \(d\asymp D(p)\), exterior deficit \(r\), mask \(P=\{r>u\}\) with \(u=\delta/8\), and companion \(h=Z_{\sigma,b}1_P\). The mark is excluded from \(P\). Write \(q(f)=\sum_iq_i f_i\) and \(\mathbb E f=n^{-1}\sum_i f_i\). On \(P\), \(h\ge(2d-1)r\). At any genuine optimizer set
\[
             V(q)=\frac nd\sum_P(1+h_i)q_i^2.
\]
Use the pure terminal metric with \(w_i=d/[n(1+h_i)]\) on the exposed part of \(P\), \(w_i=da\) on the remaining exposed exterior and \(w_0=a^2\). If \(V_*=\min_{\mathcal Q_a}V\), then
\[
           1+V_*\ \le\ \ell_+^{-1}\ \le\ 1+V_*+1/d.                 \tag{1}
\]
Indeed the uncharged contribution to the squared marked norm is at most \(a\sum_iq_i/(da)=1/d\), by the true point cap. Additional capacity restrictions on the charged sites can only raise the inverse leverage.

Uniformly over primes sufficiently large for the fixed gap, there exist \(c_\delta,k_\delta,C_\delta>0\) such that, for **each** optimizer, putting \(V=V(q)\), after every deletion \(|L|\le c_\delta nd/V^2\) its true joint band contains a set \(J\subset I(q)\setminus L\) with
\[
 \begin{split}
 k_\delta d<nq_i\le C_\delta V,\qquad &(2d-1)u<h_i\le C_\delta V \quad(i\in J),\\
 q(r1_J)\gg_\delta1,\qquad q(h1_J)&\gg_\delta d,\qquad
 q(J)\gg_\delta d/V,\quad |J|\gg_\delta nd/V^2,\\
 \mathbb E(h1_J)&\gg_\delta d/V.                                  \tag{2}
 \end{split}
\]
No precision tower restricts \(V\) here. The integer erasure budget can be zero at large \(V\). For a known upper \(V\le W\), every occurrence of \(V\) on the right of an upper cutoff and in the denominators of the lower bounds and erasure budget can be replaced by \(W\).

For the proof, the good-time first-moment bound \(\mathbb E h\ll 1\) follows from the bulk three-time expansion with adjacent \(g_j\le4\). Also \(\mathbb E h^2\ll d\) because projection contracts normalized second norm, and the raw signed activation has norm \(O(\sqrt{b+1})\), including the root. Hence
\[
 \frac{q(h1_L)}{d}
 \le \sqrt{\frac Vd}\left(\mathbb E\frac{h^2}{1+h}1_L\right)^{1/2}
 \ll\left(\frac{V^2|L|}{dn}\right)^{1/4}.
\]
For \(A\ge1\),
\[
 \frac{q(h1_{\{nq>AV\}})}d\le A^{-1},
 \qquad
 \frac{q(h1_{\{h>AV\}})}d
 \le\sqrt{\frac Vd}\left(\frac{\mathbb E h^2}{AV}\right)^{1/2}
 \ll A^{-1/2}.                                                     \tag{3}
\]
The density estimate uses \(n\sum q_i^2h_i\le dV\). On the joint band all three removed deficit prices are bounded by their height prices divided by \(2d-1\). Apply (3) and the deletion estimate to the round-79 lower \(q(r1_{I(q)})\gg_\delta1\), first fixing \(A=C_\delta\) large and then taking \(c_\delta\) small. The upper cutoffs turn the remaining height lower into the mass, cardinality and counting-height assertions of (2). In particular \(V\gg_\delta d\) by \(q(J)\le1\).

If \(\ell_+^{-1}=O_\delta(d)\), take its actual norm minimizer. Both \(h_i,nq_i\) on \(J\) are comparable to \(d\); its counting fraction is comparable to \(1/d\) since \(|P|/n\ll_\delta1/d\). Its unweighted counting height and primary mass both have fixed positive lower bounds. Thus at this leverage scale an \(o(1)\) **counting** first moment on the physical mask \(P\cap\{h\le C_\delta W\}\), for a known \(W=O_\delta(d)\) bounding the inverse leverage, would exclude a gap. More generally the sufficient counting upper is \(o(d/W)\). This test has no endpoint density in its mask. The separate [round-86 result](astra-leverage-86.md) can use an unweighted local collision bound alone. Formula (2) uses the actual height weight.

## Persistent sites of the unpinned companion

The same sites can be constrained at other times without changing the optimizer. For \(0\le t\le b\), the exact raw activation is 1-Lipschitz in normalized \(Y\) (including its marked square root), and the primary projection is contractive. Nonexpansiveness of the full cold step gives
\[
 \|Z_{\sigma,b}-Z_{\sigma,t}\|_{2,n}
   \le \|Y_b-Y_t\|_{2,n}\le 2\sqrt{b-t}.
\]
For integers \(1\le m\le b\), the normalized second norm of
\(H_m(i)=\max_{b-m\le t\le b}|Z_{\sigma,t}(i)-Z_{\sigma,b}(i)|\)
is at most \(C\sqrt m\log(2+m)\). To see this, pad the path after its last backward step by a constant to the next power of two. Every prefix is a concatenation of at most one dyadic interval of each length. At any one length the sum of squared second norms over the disjoint intervals is at most \(8m\), by the preceding increment estimate. Bound the pointwise maximum at that length by the square sum and add the norms over lengths.

For \(J\) from (2), \(n\sum_Jq_i^2\ll_\delta V\) since \(1+h_i\gg_\delta d\). Drop the sites in \(J\) for which \(H_m>h/2\); their original height costs at most \(2q(H_m1_J)\ll_\delta\sqrt{Vm}\log(2+m)\). Consequently, with a sufficiently small \(c'_\delta>0\), (2) still holds on the resulting common subset with adjusted constants for
\[
 m=\min\left(b,\left\lfloor\frac{c'_\delta d^2}{V\log^2(2+d)}\right\rfloor\right).
\]
Here \(V\gg_\delta d\) and the case \(m=0\) needs no removal. On every retained site at every one of these times,
\[
                 h_i/2\le Z_{\sigma,t}(i)\le 3h_i/2.                  \tag{4}
\]
The pin mask and deficit in (2) are measured only at \(b\); (4) concerns the genuine companion throughout the interval. For \(V=O_\delta(d)\) this yields order \(n/d\) common sites throughout order \(d/\log^2 d\) neighboring times. A counting upper \(o(d/W)\) for the height on \(P\cap\{h\le C_\delta W\}\) after also requiring (4), with the window length computed using \(W\), suffices in (2).

## A polynomial loss for a height-weighted hinge

Keep the actual mask, let \(0<t<a\), and minimize the convex objective
\[
 {\cal H}=\min_{q\in{\cal Q}_a}\sum_{i\in P}c_i(q_i-t)_+^2,
 \qquad c_i=n(1+h_i)/d .
\]
Choose an even minimizer \(q^*\) by convexity and reflection. Its hinge \(z_i=(q_i^*-t)_+1_P\) is common to all minimizers by strict convexity in the nonnegative hinge vector. For \(f_i=c_i z_i\) on \(P\), zero elsewhere, the supporting inequality gives the exact all-face price
\[
 \min_q q(f)=\beta=q^*(f)={\cal H}+t\sum_i f_i,\qquad
 V_*\ge\beta^2/{\cal H}\quad({\cal H}>0).                            \tag{5}
\]
Indeed \(\sum_{P} f_i^2/c_i={\cal H}\). More locally, for any freed set \(A\subset P\), every genuine \(q\) pays on the original source outside \(A\)
\[
 \sum_{\{f_i>0\}\setminus A}c_iq_i^2\ \ge\
   \frac{(\beta-a\sum_A f_i)_+^2}{\sum_{P\setminus A} f_i^2/c_i}
\]
when the denominator is positive. This uses the actual point cap and permits arbitrary exterior weights off the retained source for the corresponding leverage bound.

Split the fixed positive deficit on \(I(q^*)\) according to \(q_i^*\le2t\) or \(q_i^*>2t\). If the high sites pay a fixed positive amount, then **all** genuine optimizers have inverse marked norm at least of order \(nt\). In fact, writing \(G\) for those high sites, their measured height gives
\[
      {\cal H}\ \ge\ \frac{nt}{2d}\sum_{G}q_i^*h_i\gg_\delta nt,       \tag{6}
\]
since \(z_i^2\ge(q_i^*)^2/4\ge tq_i^*/2\) there. Equations (1) and (5) then apply. At \(t=H^{-1/4}(1-a)/\sqrt n\) with the round-83 half-height tower \(H\), this lower is \(p^{1/2-o(1)}\). This is a polynomial branch-selection threshold for the new weighted objective. It does not give a polynomial bound for the previously selected *unweighted* hinge minimizer.

In the other alternative the actual low sites pay a fixed deficit and order-\(d\) companion height. At this same \(t\) the old low-site deletion estimate still applies. On any \(F\) of at most \(H^2/(4nt^2)\) such low sites one has \(n\sum_F(q_i^*)^2\le H^2\) and \(q^*(F)\le H^2/(2nt)\). The three finite cold approximants have bulk supremum \(O(\log\log p)\) and second error \(o(1/H)\); the [round-86 deficit envelope](astra-leverage-86.md) gives removed deficit \(o(1)\). Thus a bound \(\ell_+^{-1}=o(nt)\) at this time forces surviving low payment for this weighted minimizer. It does not imply a moderate \(V(q^*)\) on that same minimizer. Statement (2) separately uses a row with controlled \(V\).

## The same weighted source still forces a common Jacobi head

In (6) with \(t=\alpha M/\sqrt n\), \(M=1-a\), \(\alpha=H^{-1/4}\), use **the weighted gradient itself**: \(v=f/\sum f\), \(m=1/\sum v_i^2\), and \(\rho=\sqrt n\,q^*(v)/M\). Put \(F=\{f>0\}\), so \(|F|\le1/t\) and \(\rho>\alpha\). At every precision \(K\) admitted in [round 86](astra-leverage-86.md), including the \(12/13-\xi\) range at the earlier good time,
\[
                        \rho^2m/(d^2K^2)\longrightarrow\infty.           \tag{8}
\]
Indeed run the three physical cold approximants there at \(K'=K/\alpha\). Its iterated-log height is at most \(\max(\log_2^*K,\Lambda/2)+O(1)\) for \(\Lambda=\log_2^*p\), leaving a fixed relative tower margin at the indicated horizons. The bulk expansion for \(Z_{\sigma,b}\) has bounded coefficients and a bounded constant. Replacing its three positive parts by those of the corresponding approximants therefore costs \(o(1/K')\) in normalized bulk second norm, and the bulk supremum of the replacement is \(O(1+\log\log p)\). Since \(K',H\le\log\log p\) eventually and \(|F|/n=O(H^{1/4}/\sqrt n)\), this proves \(\mathbb E[(1+h)^21_F]=o(1/(K')^2)\). No approximation of the mask indicator is necessary. By the true point cap and (6),
\[
 \sum f_i^2\le (na/d)^2 n\,o(1/(K')^2),\qquad \beta\gg_\delta nt,\qquad
 \rho^2m=\frac{n\beta^2}{M^2\sum f_i^2}.
\]
Now \(t/(aM)=\alpha/(\sqrt n a)\) with \(\sqrt n a=O(1)\), giving (8).

In particular the polynomial weighted collision lower (6) and the tower unweighted collision lower persist **simultaneously on the weighted hinge source** after every erasure
\[
         |A|\le\frac{\beta^2}{4a^2\sum f_i^2}
             =\frac{M^2\rho^2m}{4na^2}.
\]
Indeed \(a\sum_A f_i\le\beta/2\). The restricted inequality after (5) gives at least \(\beta^2/(4{\cal H})\ge{\cal H}/4\) in weighted collision on \(F\setminus A\). Unweighted Cauchy–Schwarz gives \(n\sum_{F\setminus A}(q_i')^2\ge M^2\rho^2m/4\) for every genuine \(q'\). In particular all \(|A|\le d^2K^2\) are eventually permitted; caps away from the retained source may be freed for the polynomial inverse-leverage bound.

Finally set \(W(j)=\sigma\sum_i v_i k(j-i)\), \(T=\{j\ne0:W(j)>\rho/8\}\). The [round-83 sector identity](astra-split-83.md) gives \(q'(W)=(nq'(v)-1)/\sqrt p\) and (5) gives \(q'(v)\ge q^*(v)\). The same pointwise estimate \(W\le1\) proves \(q'(T)\gg\rho M\) simultaneously on the whole maximizing face, including the root correction as in round 83 (1). The size, \(\rho>\alpha\) and (8) meet the hypotheses used to bound its cold counting energy in round 83 (2). Thus the weighted construction preserves the common-head conclusion while strengthening its terminal-metric obstruction. The choice of source and head can differ from their unweighted counterparts.

## An exact leverage and erasure comparison on three real faces

Use the previous finite pin and height conventions, with no frozen head or energy cap on the terminal weights. At \(p=97,b=4,t=(1-a)/(5\sqrt{48})\), both the weighted hinge and the full inverse norm are minimized at the origin of the two genuine nonnegative even anchor parameters. Their gradients have strictly positive entries there, and averaging a row with its reflection preserves the face and lowers the convex objectives. The weighted hinge is \(0.570829617\ldots\), the all-face source floor is \(0.900114076\ldots\), and (5) gives \(V_*\ge1.419347079\ldots\). The full positive inverse leverage is \(2.492042059\ldots\). The high part in (6) has measured height \(0.968958167\ldots\) at this finite threshold.

At primes \(257,409\), the even optimizer \(e\) is unique and the whole face is \(e+s v\), \(|s|\le s_*\), with \(v\) real odd. The complementary supports, even solve and odd kernel dimension are certified as in [round 82](astra-optimal-82.md). Write the full squared marked norm as \(B_0+B_1(s/s_*)^2\), where \(B_1>0\), and let \(T=\sum e_i h_i\). Then, at inverse-norm budget \(B_0+x B_1\) with \(0\le x\le1\), the **minimum surviving height after one optimally chosen site deletion over the whole genuine face** is exactly
\[
                T-\max_{\{i,-i\}} h_i(e_i+s_*|v_i|\sqrt x).           \tag{7}
\]
Oddness kills the total-height derivative and the quadratic metric cross term. In each pair the larger individual charge is increasing in \(|s|\), so the best deletion uses the maximum feasible displacement. At both primes orbit 33 strictly wins at both endpoints; comparison of affine functions of \(\sqrt x\) gives the same orbit over the whole interval. The residual therefore decreases strictly as soon as any extra norm is allowed.

| Prime and time | Least inverse norm \(B_0\) | Extra inverse norm \(B_1\) at the endpoint | Best one-site residual at \(x=0\) | At \(x=1\) |
|---|---:|---:|---:|---:|
| \(257,5\) | 2.848427362 | 0.000176035 | 1.923956307 | 1.923074535 |
| \(409,6\) | 2.602143230 | 0.002192492 | 1.937563134 | 1.937095245 |

These finite checks show how evenization can miss the best post-deletion price at a specified energy budget despite preserving the entire untrimmed height. The finite cutoffs do not assert a supercritical asymptotic branch. [Arb384 checker](astra-terminal-87-check.py) · [Outward intervals](astra-terminal-87-checks.jsonl)

1. At one early good time bound the pure terminal inverse leverage against the polynomial threshold (6), and measure the actual low-site price of the weighted minimizer if the high alternative is thereby excluded. A moderate inverse bound \(W\) gives the stronger test (2) on the norm-minimizing row.
2. At \(W=O_\delta(d)\), bound the **unweighted counting** mass of sites in the actual deficit mask that have order-\(d\) height throughout (4). An \(o(1/d)\) counting fraction excludes the fixed gap with that inverse bound. Neither the required all-prime inverse upper nor this counting upper is established here.
