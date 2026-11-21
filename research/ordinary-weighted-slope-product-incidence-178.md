# Actual slope-product energy and the one-match incidence bound

Use the actual \(\mu(r,b)=g(Y)g(D)\) with the square mask and all interior exclusions of [Round 171](ordinary-affine-line-energy-171.md). Extend \(\mu\) by zero on the affine group, let \(M_1=\sum\mu\le G^2=O(p)\), and write \(m(r)=\sum_b\mu(r,b)\). The weighted row estimate of [Round 177](ordinary-shifted-energy-four-factor-diagonal-177.md) is
\[
 \sum_r m(r)^2=O(p^{3/2-\kappa}),\qquad \kappa=3/418 .
\]
Every straight line in the parameter plane has weighted mass at most \(2G\). For a vertical line use the injection from \(D\) at fixed \(r\); for any other line use the nonzero degree-two equation for \(Y\) at fixed \(D\) from Round 171. These assertions remain true on arbitrary positive subfamilies of the actual lines.

## Point-plane incidence with the genuine pair weights

Let \(\mathcal E(\mu)=\sum_h(\sum_j\mu(j)\mu(jh))^2\), in counting normalization. Its quadruples satisfy \(j_1^{-1}j_2=j_3^{-1}j_4\). Distinguish the common slope product \(\xi=r_1r_4=r_2r_3\), using the exact point-plane chart of [Petridis–Roche-Newton–Rudnev–Warren, Lemmas 3.1–3.2 and (9)](https://arxiv.org/pdf/1911.03401):
\[
 P_{1,4}=(r_1,b_1,r_1 b_4),\qquad
 \Pi_{3,2}:\ b_3 X-r_3 Y-Z+r_3 b_2=0 .
\]
At fixed \(\xi\), each chart on the corresponding line pairs is injective. For the plane chart use the coefficient of \(Z\) equal to \(-1\). The projection \((X,Y,Z)\mapsto(X,Y)\) and \(r_4=\xi/r_1\) recover points and their weights. The plane charts in affine point dual coordinates are the same pair coordinates up to an invertible linear change.

Give \(P_{1,4}\) weight \(\mu(j_1)\mu(j_4)\) and \(\Pi_{3,2}\) weight \(\mu(j_3)\mu(j_2)\). Their total masses at this \(\xi\) both equal
\[
 W_\xi=\sum_r m(r)m(\xi/r)\le\sum_r m(r)^2=O(p^{3/2-\kappa}),\qquad
 \sum_\xi W_\xi=M_1^2 .
\]
Every line in the point chart and in the dual chart has weighted mass at most \(2G\). Indeed, off the direction of the third axis, projection is injective on that line and the pair weight is at most the first line's weight. Parallel to that axis, fix \((r_1,b_1)\), and sum the remaining weight at fixed slope \(r_4=\xi/r_1\). The argument in the dual chart is the same with \((3,2)\).

For the weighted use of (9), first remove all elements of group weight \(\mu(j)<p^{-2}\). They cost at most \(4p^{-2}M_1^3=O(p)\) in the original energy, because any three group elements determine the fourth in a relative quadruple. Every remaining point or plane has weight in \([p^{-4},1]\). All bounds on \(W_\xi\) and weighted collinearity hold for this reduced weight, with its own \(M_1\le G^2\).

Apply unweighted point-plane incidence to the sets with point weight \(>t\) and plane weight \(>s\), then integrate \((t,s)\in(0,1)^2\). The inequality (9) can be applied with the smaller set as points, using duality when needed. The leading asymmetric term and the collinearity term are each bounded by the sum of their two orientations. In particular, if \(L(t)\) is a level cardinality, \(\int L(t)\,dt=W_\xi\) and \(\int L(t)^{1/2}\,dt\le W_\xi^{1/2}\). For collinearity the level maximum is at most \(2G/\max(t,p^{-4})\), with the same bound in the dual chart. Thus the integrated incidence is
\[
 O\!\left(W_\xi^2/p+W_\xi^{3/2}+G(1+\log p)W_\xi\right).
\]
Use the supremum and first mass of \(W_\xi\) in the first two terms. They sum to \(O(p^{5/2-\kappa})\) and \(O(p^{11/4-\kappa/2})\), respectively. The term with \(\log p\) has size \(O(p^{5/2}(1+\log p))\), which is smaller than the dominant power. Restoring the small-weight cuts, this proves
\[
 \mathcal E(\mu)=O(p^{11/4-3/836}).
\]
It bounds the genuine entire right energy and every positive generic restriction. No high-level truncation remains in the statement.

## Weighted affine incidence and the actual one-match criterion

For a nonnegative affine weight \(\mu\), let \(F_\mu 1_U(y)=\sum_j\mu(j)1_U(j^{-1}y)\). In counting norms the finite-field proof of [Rudnev–Shkredov, Theorem 8](https://arxiv.org/pdf/1812.01671) gives
\[
 \|F_\mu1_U\|_2
 \ll |U|^{5/8}\mathcal E(\mu)^{1/8}M_1^{1/2}
       +M_1(1+|U|/\sqrt p).
\]
To see it directly, suppose \(M_1,|U|>0\), put \(m_U(h)=|U\cap hU|\), and expand the square. It is exactly \(\sum_h\Delta(h)m_U(h)\), with \(\Delta(h)=\sum_j\mu(j)\mu(jh)\). The relative first mass is \(M_1^2\) and its squared mass is \(\mathcal E(\mu)\). Estimate (22) in the same source implies
\[
 |\{h:m_U(h)\ge t\}|\ll |U|^5/t^4
 \quad(t\ge C\max\{1,|U|^2/p\})
\]
with absolute \(C\). To get this from (22), absorb the field mean and singleton terms, and use \(t\le |U|\) when needed to absorb the alternative \(|U|^2/t\) bound. If \(t>|U|\) the set is empty. For \(H=\max\{C(1+|U|^2/p),\ \mathcal E(\mu)^{1/4}|U|^{5/4}/M_1\}\), the portion \(m_U\le H\) costs \(M_1^2 H\). The remaining part is bounded by Cauchy–Schwarz and the rich squared mass \(O(|U|^5/H^2)\), giving \(O(\mathcal E(\mu)^{1/2}|U|^{5/2}/H)\). This proves the displayed second-norm upper. The empty cases are zero. Testing against \(1_T\) gives the weighted affine incidence inequality
\[
 I_\mu(U\times T)\ll |T|^{1/2}
 \bigl(|U|^{5/8}\mathcal E(\mu)^{1/8}M_1^{1/2}
       +M_1(1+|U|/\sqrt p)\bigr).
\]

In the actual twisted physical chart \(s=b+r e\), \(h_t(e)=g(t/e)\) is extended by zero at \(e=0\), and \(\sum_e h_t(e)\le G\) for \(t\ne0\). Completing the \(g(C)\) factor by one gives the valid positive upper of [Round 173](ordinary-weighted-affine-vertical-saving-173.md). Expand only \(h_t\) by layer cake and integrate the second-norm bound directly. Its levels \(U\) satisfy \(\int_0^1 |U|^{5/8}\,du=O(G^{5/8})\) and \(\int_0^1 |U|\,du\le G\). The actual interior \(H_\alpha(s,t)\) therefore has counting second norm \(O(p^{37/32-3/6688})\) over \(s\), uniformly in \(t\). Summing the real \(w(t)\) after squaring and restoring the earlier endpoint contributions in weighted norm gives
\[
 \sum_{s\ne0,1,t}w(t)|H_\alpha(s,t)|^2
   =O(p^{45/16-3/3344}).
\]
Thus the matching-number-one covariance is \(O(p^{29/16-3/3344})\) in the normalization of Round 173. The sufficient \(O(p^{3/2})\) covariance, zero match, and coupled full physical diagonal remain open.

## Transverse first mass

Put \(n_q=\sum_r\mu(r,q)\) and \(n_{c,q}=\sum_{b+c r=q}\mu(r,b)\). For any fixed \(c\), the actual first mass \(\sum_{a\ne0}\Delta(a,c)\) equals \(\sum_q n_{c,q}n_q\), since each second line at intercept \(q=b+cr\) determines a unique \(a=r'/r\). For \(x=1/Y\), \(y=1/D\) the row equation is
\[
 (qx-c)y=x(x+q-1-c).
\]
For the mixed sum only \(q\ne0,1\) matters since \(n_0=n_1=0\). A zero of \(qx-c\) can also zero the numerator only at \(q=c\) or \(q=1\) when \(x\ne0\). At \(q=c\ne0,1\) this would be \(x=1\), which is excluded. Thus each of the relevant rows is single-valued in \(x\), and \(n_{c,q}\le G\). The possibly unneeded \(q=0,1\) can be omitted throughout. Now use \(\sum_q n_{c,q}^2\le GM_1\), \(\sum_q n_q^2=O(p^{3/2-\kappa})\) from Round 177, and Cauchy–Schwarz. This gives first mass \(O(p^{3/2-\kappa/2})\) at every fixed \(c\). Combining it with the actual generic maximum of Round 176 gives squared generic mass \(O(p^{5/2-\kappa/2-1/1280-1/840})\) there. A further improvement at fixed \(c\) would need a stronger bound on the transverse row masses or their mixed product.
