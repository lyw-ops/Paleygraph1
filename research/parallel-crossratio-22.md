# Cell third moments as a restricted direction count

For [ETH Problem 26](https://randomstrasse101.math.ethz.ch/posts/PaleyGraph/), this continues the order-two branch of [Round 21](parallel-crossratio-21.md). The exact cell count is a product multiplicity of a shifted coset. Its third moment equals, up to \(O(b^3)\), a count of pairs in a projective image of \(D^2\) whose slopes belong to \(B\). This isolates a restricted direction estimate that would be sufficient. There is also a weaker cap criterion: a uniform \(L^{3/2,q}\) bound for the anchor mean with any finite second index \(q\ge 1\) suffices, and with a weak endpoint bound it is enough to find gaps between occupied scales. The strong moment and the twisted gap remain open here.

## 1. Product cells and their two anchors

Use the notation of Round 21: \(B\le Q\) has even order \(b\asymp\sqrt p\), \(-1\in B\), \(D=\{(x-1)^{-1}:x\in B\setminus\{1\}\}\), and \(r_a(u)\) is the off-identity overlap for the two-anchor image \(X_a\). A four-entry cell has count
$$
N_C(\lambda)=\#\{(X,Y)\in C\times C^{-1}: XY+Y=\lambda X+1\},
\qquad \lambda\notin\{0,1\}.
$$
Put \(Z=-Y^{-1}\in C\) and \(\gamma=1-\lambda\). Then
$$
N_C(\lambda)=\#\{(X,Z)\in C^2:\lambda XZ+X+Z+1=0\}
=\#\{(X,Z)\in C^2:(1+X^{-1})(1+Z^{-1})=\gamma\}.
\tag{1}
$$
Both coordinates are different from \(-1\). The cell is a product representation count on the nonzero part of \(1+C^{-1}\). Swapping the two coordinates accounts for the off-diagonal second-moment degeneracy of Round 21: in its original coordinates the involution is \((X,Y)\mapsto(-1/Y,-1/X)\). Every solution has at most one distinct partner of this form, and fixed points are the at most two roots of \(\lambda X^2+2X+1=0\). Write \(F_C(\lambda)\) for the number of fixed points.

In the parametrization \(h(x)=(\lambda\alpha\beta x+\beta)/(\alpha x+1)\), the map fixing 1 from a solution in (1) has \(\alpha=X,\ \beta=-Z\). Its other fixed point is \(a=Z/X\in B\), so **every** solution with \(X\ne Z\) gives an anchored pair. The solutions \(X=Z\) are precisely the double-fixed-point cases. The multiplier in the \(\phi_a\) coordinate and its inverse parametrization are
$$
u=\frac{1+X}{1+Z},\qquad X=\frac{u-1}{1-ua},\qquad Z=aX.
\tag{2}
$$
For example, the unnormalized matrix for \(h_{a,u}\) has entries \(u-a,a(1-u),u-1,1-ua\), in row order. The two zero-entry possibilities are \(u=a,1/a\), as in Round 21, and are omitted below. Writing \(L(v)=(v-1)^2/v\), another consequence of (1)–(2) is \(\gamma=L(a)/L(u)\). Thus a cell supplies exactly \(N_C-F_C\) pairs \((a,u)\), and each has \(r_a(u)=N_C-2\). In particular for \(s>0\),
$$
\sum_{a,u\ :\ {\rm four\ entries}}r_a(u)^s
=\sum_{\lambda,C:\ N_C\ge2}(N_C-F_C)(N_C-2)^s.
\tag{3}
$$
A one-point cell is fixed under the swap, so it contributes no pair. For each fixed cap, the omitted terms cost \(O_M(p^{-1/2})\) in the normalization of Round 21 because there are at most two per anchor, even if an overlap is full.

One apparent shortcut is to compare the third moment of the product representations of \(1+C^{-1}\) to its quotient representations. In general the uncentered product moment is at most the quotient moment: expand via triples with fixed two relative ratios and use Cauchy–Schwarz after inversion of the relative ratios on one side. But the quotient identity alone contributes \(\gg (p-1)b^2\asymp b^4\) when summed over \(C\). It cannot simply be deleted from that use of Cauchy–Schwarz. This prevents applying the shifted-subgroup quotient estimate of Round 20 by this argument.

## 2. An exact third-moment reduction

Define the point set
$$
\mathcal P=
\left\{
  \left(\frac{r(1-s)}{rs-1},\frac{s(1-r)}{rs-1}\right):
  r,s\in B\setminus\{1\},\ rs\ne1
\right\}.
\tag{4}
$$
This is a projective image of pairs \((t,w)\in D^2\) with \(1+t+w\ne0\): use \(t=(r-1)^{-1},\ w=(s-1)^{-1}\) to obtain
$$
(A,D')=\left(\frac{-(t+1)}{1+t+w},\frac{-(w+1)}{1+t+w}\right).
$$
The map is one-to-one; in particular \(A+D'+1=-1/(1+t+w)\ne0\) and \(t+1=A/(A+D'+1)\), with the second coordinate treated the same way. The omitted pairs are exactly the \(b-1\) with \(s=r^{-1}\). Thus \(|\mathcal P|=(b-1)(b-2)\).

Fix a first solution \((X,Z)\) of (1). Any other solution in its cell is \((rX,sZ)\) with \(r,s\ne1\), since each coordinate determines the other on the curve. Subtract the two curve equations and eliminate \(\lambda\):
$$
r(1-s)X+s(1-r)Z=rs-1.
\tag{5}
$$
If \(rs=1\), this is exactly the distinct swapped solution, and it exists precisely for \(X\ne Z\). Otherwise (5) says that the point in (4) is on the line
$$
\ell_{X,Z}:\quad XA+ZD'=1.
\tag{6}
$$
Conversely every such incidence produces a second solution. In particular \(|\mathcal P\cap\ell_{X,Z}|=N_C-1-\mathbf1_{X\ne Z}\).

Call a line in (6) admissible if \(X,Z\ne0,\ X/Z\in B,\ X,Z\ne-1,\ X+Z+1\ne0\). Each admissible line is the image of exactly one first solution of exactly one cell: the line fixes \(X,Z\) uniquely, hence \(C=XB\) and \(\lambda=-(X+Z+1)/(XZ)\), which is neither 0 nor 1. Write \(J_{\rm adm}\) for the number of ordered distinct pairs of points of \(\mathcal P\) on these lines. Counting the two further solutions after a first one gives the exact equality
$$
\sum_{\lambda,C}(N_C)_3
=J_{\rm adm}+2\sum_{\lambda,C}(N_C-F_C)(N_C-2).
\tag{7}
$$
The correction counts the triples with a swapped solution among the second and third positions. It is \(O(b^3)\) by the second-moment bound (10) of Round 21.

The direction of (6) belongs to \(B\): its slope is \(-X/Z\), and \(-1\in B\). Define
$$
J_B(\mathcal P)=
\#\{(P,P')\in\mathcal P^2:P\ne P',\
     P'-P\ \text{has finite slope in } B\}.
$$
The lines lost when replacing this count by \(J_{\rm adm}\) also cost \(O(b^3)\). There are at most \(b\) lines of each of the following four types, with each line meeting \(\mathcal P\) in at most \(b\) points:

- Through the origin: \(XA+ZD'=0\), which is linear in \(s\) after clearing the denominator in (4), with nonzero constant term \(Xr\) for every \(r\).
- \(X=-1\) in (6): (5) reduces to \((r-1)(1+Zs)=0\). At most one choice of \(s\) survives for each \(r\).
- \(Z=-1\) in (6): exchange the two coordinates in the previous case.
- \(X+Z+1=0\): (5) becomes \(rX+sZ=-1\), again with at most one \(s\) per \(r\).

Consequently the ordinary third moment satisfies
$$
\boxed{\ \sum_{\lambda,C}N_C(\lambda)^3=J_B(\mathcal P)+O(b^3).\ }
\tag{8}
$$
All degeneracies discarded in (8) are accounted for, including the swap. An \(O(b^3)\) bound for \(J_B(\mathcal P)\) would imply \(\sum N_C^{5/2}=O(b^3)\) by Cauchy–Schwarz with \(\sum N_C^2=O(b^3)\). Equation (3) and convexity would then give the strong endpoint moment of the anchor mean after omitting the two zero-entry ratios at each anchor.

For a direct version of the remaining estimate, for \(u\in B\) let \(q_u(v)\) count points \((A,D')\in\mathcal P\) with \(A+uD'=v\). It counts pairs \(r,s\) from (4) satisfying \(r+us-(1+u+v)rs=-v\), and
$$
J_B(\mathcal P)=\sum_{u\in B}\sum_v q_u(v)(q_u(v)-1).
\tag{9}
$$
The average of this directional energy over *all* \(B\)-cosets of slopes is \(O(b^3)\), since at most \(|\mathcal P|^2=O(b^4)\) pairs contribute and there are \(\asymp b\) cosets. That averaging does not bound the specific coset \(B\). Likewise, the pair count is for the projected grid \(\mathcal P\), not the untranslated Cartesian grid \(D^2\). Pointwise torsion estimates bound individual cells but leave a power loss in (8).

## 3. What the twist gives

Suppose \(\chi(1-x)=\sigma d(x)\) for \(x\in B\setminus E\) with \(|E|=o(b)\), as in Round 21. Then
$$
\sigma=d(-1)=(-1)^{b/2}.
\tag{10}
$$
Indeed choose \(x,-x,x^2\notin E\), which is possible since at most \(4|E|\) elements of \(B\) have one of the three values in \(E\). Evaluate the character of \((1-x)(1+x)=1-x^2\) both ways. The right side gives \(\sigma\), and the left side gives \(d(-1)\).

Apart from \(O(b|E|)\) ordered pairs, \(\chi(z-w)=\sigma\) for distinct \(z,w\in D\): substitute \(z=1/(x-1)\), \(w=1/(y-1)\) and use the hypothesis on \(x,y,y/x\). Thus all but \(O(b^2|E|)\) ordered triples of distinct \(t,z,w\in D\) have
$$
\chi(u)=\chi(1-u)=1,\qquad u=(z-t)/(w-t).
$$
For these ratios the square condition on \(\gamma\) in (1) is automatic when \(a\in B\), since \(\chi(\gamma)=\chi(u)\) by (2). The unrestricted ratio count is invariant under \(u\mapsto1-u\) and \(u\mapsto u^{-1}\) by permuting the triple. For fixed cap order the \(o(b^2)\) mass of the anchor mean outside this condition is negligible in the normalized pairing. In the projected grid (4), outside \(O(b|E|)\) parameter pairs one also has \(\chi(A)=d(r)\), \(\chi(D')=d(s)\), and \(\chi(A+D'+1)=\sigma\), by applying the twist to \(r,s,rs\). These are support restrictions; they give no upper bound here on the multiplicity of the surviving directions or ratios. The square-order example in Round 21 satisfies the sign restrictions as well.

## 4. A weaker cap criterion and a test for missing scales

Use the measure \(1/p\) per field element. Put \(r=\bar r\) from Round 21, or restrict the mean to good anchors and ratios and omit the zero-entry terms as above. It also suffices to use a pointwise majorant of the resulting mean. Extend by zero and let \(r^*(s)\), \(0<s\le1\), be its decreasing rearrangement. Define \(F_p(s)=s^{2/3}r^*(s)\). For fixed \(j\) use the cap of order \(M=4^j\), and let \(v_j\) be the absolute off-identity coefficient multiplied by \(\sqrt p\). The estimates of Round 21 give
$$
v_j^*(s)\ll\min(2^j,2^{-j/2}s^{-1/2}).
$$
Their average over \(1\le j\le K\) was bounded there using \(V_K=\sum_{j=1}^K v_j\), with \(V_K^*(s)\ll\min(2^K,s^{-1/3})\). The rearrangement inequality bounds the normalized contribution off the identity for that average by
$$
\frac{O(1)}{K}\int_0^1 F_p(s)\min(2^K s^{1/3},1)\,\frac{ds}{s}.
\tag{11}
$$
For \(1\le q<\infty\), a uniform bound on \(\|F_p\|_{L^q(ds/s)}=\|r\|_{L^{3/2,q}}\) makes (11) \(O_q(K^{-1/q})\) by Hölder: the second factor has \(L^{q'}(ds/s)\) norm \(O_q((K+1)^{1/q'})\), also for \(q'=\infty\). The diagonal is \(O(K^{-1}+p^{-1/4})\). Choose \(K\) large but fixed before \(p\to\infty\) to contradict saturation. Taking \(q>3/2\) relaxes the strong moment condition. For instance a decreasing rearrangement comparable near zero to \(s^{-2/3}(\log(e/s))^{-\alpha}\) with \(1/q<\alpha\le 2/3\) passes the \(q\) test but fails the strong moment.

There is a matching relaxed target in the cells. Give each cell mass \(b^{-3}\), write \(\mu_N(t)=b^{-3}\#\{(\lambda,C):N_C>t\}\), and put \(H_N(t)=t^{5/2}\mu_N(t)\). Give each \((a,u)\) mass \(1/((b-1)p)\), with zero overlap at the omitted ratios. By (3) and \(p\asymp b^2\), its overlap distribution \(\mu_{\rm joint}\) satisfies
$$
t^{3/2}\mu_{\rm joint}(t)
\ll H_N(t)+\int_0^\infty e^{-3v/2}H_N(te^v)\,dv.
$$
Indeed a cell with \(N_C>t\) contributes at most \(N_C\) pairs. For any finite \(h\ge1\), Minkowski bounds the right side in \(L^h(dt/t)\) by \(O(\|H_N\|_{L^h(dt/t)})\). By layer cake, this gives \(L^{3/2,3h/2}\) for the joint overlap from \(L^{5/2,5h/2}\) for the cells. Taking the anchor mean preserves this bound up to a constant: its integrated decreasing rearrangement is bounded by that of the joint overlap, and the Hardy average \(f^{**}(s)=s^{-1}\int_0^s f^*(v)\,dv\) is bounded in these Lorentz norms. Thus a finite-index Lorentz bound at cell exponent \(5/2\) suffices in place of a strong \(5/2\) moment.

One can also detect gaps in a weak endpoint profile. Under a uniform bound \(F_p\le C\), write \(s=2^{-3x}\) in the rearrangement bound for a **single** cap. Its contribution off the identity is bounded by a constant times
$$
\int_0^\infty F_p(2^{-3x})\min(2^{j-x},2^{(x-j)/2})\,dx.
\tag{12}
$$
Outside \(|x-j|\le L\) the contribution is \(O(C 2^{-L/2})\). Accordingly, saturation and a bare weak bound together force positive mass in every fixed-width window of sufficiently large fixed scales: there are \(c>0\) and \(L=L(C)\) so that for every sufficiently large fixed \(j\),
$$
\liminf_{p\to\infty}\int_{j-L}^{j+L} F_p(2^{-3x})\,dx \ge c
$$
along any putative sequence with twisted saturation. This gives a way to bypass a generic strong moment if the arithmetic supplies windows of small mass. Neither the weak bound nor the window estimate needed to exploit (12) is established for these prime-field ratios.

## 5. Exact finite checks

Run [the Python check](parallel-crossratio-22-check.py) with the **--larger** flag to include the last row. It verifies the independent cell count at the smaller primes, the fixed-point and anchored formulas, and the ordered-pair and swap identities in (7)–(9). At \(p=97\) it also checks the original anchored overlaps directly. The last column uses all \(b-1\) anchors and all off-identity ratios. Counts are exact integers; fractional powers and reported normalizations are rounded.

| \(p\) | \(b\) | \(\sum N^2/b^3\) | \(\sum N^{5/2}/b^3\) | \(\sum N^3/b^3\) | \(J_B/b^3\) | \(J_{\rm adm}/b^3\) | \(\sum\bar r^{3/2}/p\) |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 97 | 12 | 1.870 | 3.448 | 6.713 | 2.459 | 1.262 | 1.152 |
| 1,153 | 32 | 3.058 | 5.409 | 10.050 | 3.152 | 1.478 | 0.726 |
| 4,177 | 72 | 2.530 | 4.867 | 9.890 | 3.924 | 2.073 | 1.291 |
| 10,193 | 98 | 3.060 | 5.584 | 10.709 | 3.661 | 1.771 | 0.872 |
| 40,801 | 200 | 3.010 | 5.568 | 10.841 | 3.856 | 1.911 | 0.949 |

These checks do not prove the uniform restricted direction or Lorentz bound.
