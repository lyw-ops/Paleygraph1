# Round 180 candidate: paired J fibres of the actual diagonal

Call: `ordinary-prime-paired-J-fibers` (mission export `coordination/missions/round-180/ordinary-prime-paired-J-fibers.md`, coordinator record `coordination/round-179.json`).
Author: research subagent (Claude Code). This is an agent candidate, not an acceptance or a mathematical certification. No repository file was modified.

## Outcome

**Inconclusive.** Labels: (a) proved here from inherited accepted bounds, (b) conditional criterion, (c) finite or model evidence only.

- (a) The Round 179 invariant is a cross-ratio of the two lines: \(J=[\pi';\pi,\rho,\rho']\). The paired map \(h_k\) does not depend on \(s\).
- (a) \(J=0\) means \(\pi'=\pi\) or \(\rho'=\rho\). \(J=1\) means \(\pi'=\rho\) or \(\rho'=\pi\).
- (a) The two special classes together cost \(\mathcal D_0+\mathcal D_1\le 4R_*\mathcal M_w=O(p^{15/8-1/1280})=O(p^{2399/1280})\). Here \(w\), \(D\) and the whole first copy are kept.
- (a) Each single generic class \(J\notin\{0,1\}\) costs \(\mathcal D_J\le 2G\mathcal M_w=O(p^{15/8})\). These bounds cannot be summed over the up to \(p-2\) generic classes, so the generic range stays at the inherited \(O(p^{9/4})\).
- (b) If \(\mathcal M_w=\sum_s w(s)P_s=O(p^{1+1/1280})\), then \(\mathcal D_0+\mathcal D_1=O(p^{3/2})\).
- (c) Exact modular checks of every identity used, and the earlier floating-point model runs.

**Correction to the earlier handback summary.** That summary priced \(\mathcal D_0+\mathcal D_1\) at \(O(p^{2429/1280})\) and the generic classes at \(O(p^{243/128})\), because it used \(\mathcal M_w=O(p^{179/128})\) from the Round 178 output-first estimate. Cauchy–Schwarz against the accepted Round 179 diagonal bound gives the smaller \(\mathcal M_w=O(p^{11/8})\) (Section 3.3). This report uses that value. The earlier alternative exponent \(2439/1280\) came from the same Cauchy–Schwarz step applied to the weaker Round 173 diagonal \(O(p^{37/16})\). All three routes are listed in Section 3.3.

## 0. Hypotheses and scope

We use the actual \(g=|f|^2\) on \(Q\) (zero off \(Q\)), \(w=g(1-g)\), \(G=\sum g=O(\sqrt p)\), and the physical masks and nonzero interior of Round 178, as fixed in Round 179. The prime \(p\equiv1\bmod4\) is eligible, and all norms are counting norms. The facts used are:

- \(0\le g,w\le1\), \(w\le g\), so \(\sum_s w(s)\le G\).
- \(g(z)=g(1/z)\) on \(\mathbb F_p^\times\), as noted in Round 173. Hence also \(w(z)=w(1/z)\).
- The accepted bounds quoted in Section 3.

The physical masks (including \(b\in Q\)) are written \(1_{\mathcal M}\). Only the second copy's mask is dropped, and only where stated. Distinct \(b\) is never identified with distinct \(r\) or distinct \(k\), and no single-label coincidence cut is used.

## 1. Chart and cross-ratio identification

### 1.1 Labels as cross-ratios

The Round 178 line labels are
\[
A=\frac{rs}{s-b},\quad C=\frac{rb}{(1-r)(s-b)},\quad Y=\frac{r}{1-b},\quad D=\frac{rb}{(1-r)(1-b)} .
\]
Put \(X=1/s\), \(\pi=1/b\), \(\rho=(1-r)/b\). We call \(e=(\pi,\rho)\) the line. Write \([z;a,b,c]=\frac{(z-a)(b-c)}{(z-c)(b-a)}\) for the Möbius map with \(a\mapsto0\), \(b\mapsto1\), \(c\mapsto\infty\), so that \([z;a,b,\infty]=\frac{z-a}{b-a}\).

**Lemma 1.** On the chart domain \(r\notin\{0,1\}\), \(b\notin\{0,1\}\), \(s\notin\{0,1,b\}\),
\[
\frac1A=[X;\pi,\rho,\infty],\quad \frac1Y=[1;\pi,\rho,\infty],\quad
\frac1C=[X;\pi,\rho,0],\quad \frac1D=[1;\pi,\rho,0],\quad \rho=\frac YD .
\]

*Proof.* \(\rho-\pi=-r/b\) and \(X-\pi=(b-s)/(sb)\). So \([X;\pi,\rho,\infty]=(X-\pi)/(\rho-\pi)=(s-b)/(rs)=1/A\). Likewise \((1-\pi)/(\rho-\pi)=(1-b)/r=1/Y\). Next,
\[
[X;\pi,\rho,0]=\frac{\rho(X-\pi)}{X(\rho-\pi)}=\frac{(1-r)s}{b}\cdot\frac{s-b}{rs}=\frac{(1-r)(s-b)}{rb}=\frac1C .
\]
Setting \(X=1\) gives \(1/D\). Finally \(Y/D=(1-r)/b=\rho\). \(\square\)

**Lemma 2 (interior).** On the chart domain, the four labels avoid \(\{0,1\}\) iff \(0,1,X,\pi,\rho\) are pairwise distinct. Together with \(\infty\), these are six distinct points of \(\mathbb P^1\). The map \((r,b,s)\mapsto(\pi,\rho,X)\) is a bijection onto such triples, with inverse \(b=1/\pi\), \(r=1-\rho/\pi\), \(s=1/X\).

*Proof.* The chart domain already gives:

- \(\rho\ne\pi\) (from \(r\ne0\)) and \(\rho\ne0\) (from \(r\ne1\)),
- \(\pi\ne0,1\) (from \(b\ne\infty,1\)),
- \(X\ne0,1,\pi\) (from \(s\ne\infty,1,b\)).

By Lemma 1, \(A=1\iff C=1\iff X=\rho\), and \(Y=1\iff D=1\iff\rho=1\). No label is \(0\) or \(\infty\) on the chart domain. \(\square\)

The output \(s\equiv X\) is common to both copies, and the line \(e\) carries the parameters. In the chart of Round 179, \(v=1/A\), \(x=1/Y\), \(u=1/C\). With \(j_e(z)=[z;\pi,\rho,\infty]=(z-\pi)/(\rho-\pi)\), an affine map,
\[
v=j_e(X),\qquad x=j_e(1).
\]

### 1.2 The paired map and J

For a second line \(e'=(\pi',\rho')\) at the same \(s\), Round 179 defines the unique \(k\ne0\) with \(x'=h_k(x)\), where \(h_k(z)=v'+k(z-v)=kz+d\) and \(d=v'-kv\). It sets \(J=d(k+d-1)/k\).

**Proposition 3.** \(h_k=j_{e'}\circ j_e^{-1}\). In particular \(h_k\) does not depend on \(s\). Moreover
\[
k=\frac{\rho-\pi}{\rho'-\pi'},\qquad d=j_{e'}(\pi),\qquad k+d=j_{e'}(\rho),
\]
\[
J=[\pi';\pi,\rho,\rho']=\frac{(\pi-\pi')(\rho-\rho')}{(\rho-\pi)(\rho'-\pi')},\qquad
J-1=\frac{(\pi-\rho')(\rho-\pi')}{(\rho-\pi)(\rho'-\pi')} .
\]

*Proof.* \(H=j_{e'}\circ j_e^{-1}\) is affine. It sends \(v=j_e(X)\mapsto j_{e'}(X)=v'\) and \(x=j_e(1)\mapsto x'\). Since \(x\ne v\) (because \(X\ne1\)), an affine map is fixed by two distinct points, so \(H=h_k\). Its slope is the ratio of the slopes, \((\rho-\pi)/(\rho'-\pi')\). Further \(d=H(0)=j_{e'}(\pi)\) and \(k+d=H(1)=j_{e'}(\rho)\). Hence
\[
d=\frac{\pi-\pi'}{\rho'-\pi'},\qquad k+d-1=\frac{\rho-\rho'}{\rho'-\pi'},
\]
and \(J=d(k+d-1)/k\) is the displayed product. Expanding the numerator of \(J-1\) gives \(\pi\rho+\pi'\rho'-\rho\rho'-\pi\pi'=(\pi-\rho')(\rho-\pi')\). The cross-ratio form follows from the definition of \([\cdot;\cdot,\cdot,\cdot]\). \(\square\)

**Corollary 4.** The denominators are nonzero, so \(J\in\mathbb F_p\) and the classes \(J=c\), \(c\in\mathbb F_p\), partition all pairs. Also:

- \(J=0\iff d=0\) or \(k+d=1\iff \pi'=\pi\) (common \(b\)) or \(\rho'=\rho\) (common \(Y/D\)).
- \(J=1\iff d=1\) or \(k+d=0\iff \rho'=\pi\) or \(\pi'=\rho\). Here \(J-1=(d-1)(d+k)/k\).

Neither condition is a common \(r\) or a common \(k\).

Round 179 also proved that the companion \(h_{\lambda/k}\) acting on \(u\) has the same \(J\). It is not needed below.

## 2. The J-sorted diagonal

For the line \(e\) at output \(s\) put
\[
a_e(s)=1_{\mathcal M}(e)\,1[e\text{ interior at }s]\;g(A)g(C)g(Y)g(D),\qquad P_s=\sum_e a_e(s).
\]
\(P_s\) is the interior part of the Round 178 positive diagonal. Then
\[
\mathcal D:=\sum_s w(s)P_s^2=\sum_{c\in\mathbb F_p}\mathcal D_c,\qquad
\mathcal D_c=\sum_s w(s)\sum_{e,e':\,J(e,e')=c}a_e(s)a_{e'}(s).
\]
By Proposition 3, \(J\) depends only on the pair of lines.

Given \(e\) and an affine \(h=(k,d)\), the second line \(e'\) is determined by \(j_{e'}=h\circ j_e\), namely
\[
\pi'=j_e^{-1}(-d/k),\qquad \rho'=j_e^{-1}((1-d)/k).
\]
So in Round 179 variables,
\[
\mathcal D_{\rm gen}:=\sum_{c\ne0,1}\mathcal D_c=\sum_s w(s)\sum_e a_e(s)\sum_{h:\ d\notin\{0,1\},\ k+d\notin\{0,1\}} a_{h\circ e}(s),
\]
where \(a_{h\circ e}(s)\) carries the weight \(g(1/h(v))\,g(1/h(x))\,g(1/h_{\lambda/k}(u))\,g(D')\) together with its mask and interior indicator.

## 3. Pricing J ∈ {0,1}

### 3.1 Inherited bounds used, with exact statements

1. **Round 173, heavy affine fibre** (`research/ordinary-weighted-affine-vertical-saving-173.md`). Put \(\varepsilon_*=1/1280\), \(\delta_*=1/640\), \(\tau=p^{-\varepsilon_*}\). For any affine \(T(x)=cx+d\) with \(cd\ne0\), a set \(X\) with \(g(x),g(Tx)\ge\tau\) on \(X\) has \(|X|=O(p^{1/2-\delta_*})\), uniformly in \(c,d\).
   Its consequence, stated in `research/ordinary-full-diagonal-two-pin-173.md` for the \(b\)-row \(1/Y=b/D+(1-b)\) and for \(C=(A-r)/(1-r)\), is the two-level affine row bound. We use it in the uniform form
   \[
   R_*:=\sup_{cd\ne0}\sum_{z\in\mathbb F_p}g(z)g(cz+d)=O(p^{1/2-1/1280}).
   \]
   Proof of this form: the pairs with both weights at least \(\tau\) contribute at most \(|X|=O(p^{1/2-1/640})\), since \(g\le1\). The pairs with \(g(z)<\tau\) contribute at most \(\tau\sum g(cz+d)\le\tau G\), and those with \(g(cz+d)<\tau\) at most \(\tau G\). The total is \(O(p^{1/2-1/640}+p^{1/2-1/1280})\).
2. **Round 179, whole diagonal** (`research/ordinary-affine-triple-diagonal-179.md`, accepted in `research/round-179-acceptance.json`): \(\sum_s w(s)P_s^2=O(p^{9/4})\) for the actual whole positive diagonal, endpoints included. The interior \(P_s\) above is at most the full one, so the bound applies to it.
3. **Round 178** (`research/ordinary-parabolic-row-mean-square-178.md`): \(\sum_s w(s)\le G\) and \(w\le1\). This is used in Section 3.3.
   For comparison only, Section 3.3 also uses the Round 178 output-first first-mass estimate on an output set \(T\):
   \[
   \sum_{s\in T}P_s\ll p^{139/128}|T|^{5/8}+G^{5/2}(1+|T|/\sqrt p).
   \]
   It comes from the weighted affine incidence of `research/ordinary-weighted-slope-product-incidence-178.md` with \(\mathcal E(\mu_*)=O(p^{43/16})\), and completes \(g(C)\le1\).

### 3.2 The four fixed-parameter rows

Fix \(s\) (so \(X\)) and one parameter of the second line. In each case keep two of the second copy's four factors, and bound the other two factors and the second copy's mask by one.

- **Fixed \(\pi\), varying \(\rho'\)** (used for \(\pi'=\pi\), and for \(\pi'=\rho_e\) in the \(J=1\) class). With \(z=1/Y'=(1-\pi)/(\rho'-\pi)\), which is injective in \(\rho'\) because \(\pi\ne1\), Lemma 1 gives \(1/D'=\rho'(1-\pi)/(\rho'-\pi)=\pi z+(1-\pi)\). Slope \(\pi\ne0\), shift \(1-\pi\ne0\). By inversion symmetry,
  \[
  \sum_{\rho'}a_{(\pi,\rho')}(s)\le\sum_z g(z)g(\pi z+1-\pi)\le R_* .
  \]
  This is the Round 173 \(b\)-row \(1/Y=b/D+1-b\). Dropped: \(g(A'),g(C')\), mask.
- **Fixed \(\rho\), varying \(\pi'\)** (used for \(\rho'=\rho\), and for \(\rho'=\pi_e\) in the \(J=1\) class). With \(z=1/Y'=(1-\pi')/(\rho-\pi')\), which is injective in \(\pi'\) because \(\rho\ne1\), put \(t=1/(\rho-\pi')\). Then \(z=1+(1-\rho)t\) and \(1/A'=1+(X-\rho)t\), so
  \[
  1/A'=cz+(1-c),\qquad c=\frac{X-\rho}{1-\rho}\notin\{0,1\}
  \]
  because \(X\ne\rho\) and \(X\ne1\). Hence \(\sum_{\pi'}a_{(\pi',\rho)}(s)\le R_*\). Dropped: \(g(C'),g(D')\), mask.

In each row the fixed parameter (\(\pi\), \(\rho\), \(\rho_e\) or \(\pi_e\)) lies outside \(\{0,1\}\) and differs from \(X\) on the interior, which is all the slope and shift conditions need.

**Proposition 5.**
\[
\mathcal D_0\le 2R_*\mathcal M_w,\qquad \mathcal D_1\le 2R_*\mathcal M_w,\qquad \mathcal M_w:=\sum_s w(s)P_s .
\]

*Proof.* By Corollary 4, \(1[J=0]\le1[\pi'=\pi]+1[\rho'=\rho]\) and \(1[J=1]\le1[\pi'=\rho]+1[\rho'=\pi]\). Inserting these and positivity,
\[
\mathcal D_0\le\sum_s w(s)\sum_e a_e(s)\Bigl(\sum_{\rho'}a_{(\pi_e,\rho')}(s)+\sum_{\pi'}a_{(\pi',\rho_e)}(s)\Bigr)\le 2R_*\sum_s w(s)\sum_e a_e(s).
\]
For \(\mathcal D_1\), use the rows \((\rho_e,\cdot)\) and \((\cdot,\pi_e)\) instead. \(\square\)

In this step \(w(s)\), the whole first copy (\(A,C,Y,D\), mask) and two second-copy factors (\(Y',D'\) or \(Y',A'\)) are kept. Only the other two second-copy factors and the second-copy mask are bounded by one, and only after the J sorting.

### 3.3 The first mass M_w

**Route B (used).** By Cauchy–Schwarz with weight \(w\), then inherited bounds 2 and 3,
\[
\mathcal M_w\le\Bigl(\sum_s w(s)\Bigr)^{1/2}\Bigl(\sum_s w(s)P_s^2\Bigr)^{1/2}\le G^{1/2}\,O(p^{9/8})=O(p^{11/8}).
\]
The losses are those internal to Round 179's proof: \(D,D'\), the masks and \(w\) are bounded by one inside its Cauchy–Schwarz bound by \(\sum_h m(h)^3\).

**Route A (earlier summary; superseded).** Since \(w\le1\) and \(\sum w\le G\), rearrangement gives \(\mathcal M_w\le\sum_{n\le\lceil G\rceil}P_{(n)}\), the first mass of the \(\lceil G\rceil\) largest \(P_s\). The output-first estimate gives \(O(p^{139/128}G^{5/8}+G^{5/2})=O(p^{179/128})\). This loses \(g(C)\) and is weaker than Route B, since \(179/128>176/128\).

**Route 173 (earlier alternative; superseded).** Route B with the Round 173 diagonal \(O(p^{37/16})\) instead of Round 179 gives \(\mathcal M_w=O(p^{45/32})\), and \(\mathcal D_0+\mathcal D_1=O(p^{2439/1280})\).

**Theorem 6 (a).**
\[
\mathcal D_0+\mathcal D_1\le 4R_*\mathcal M_w=O\bigl(p^{1/2-1/1280}\cdot p^{11/8}\bigr)=O\bigl(p^{15/8-1/1280}\bigr)=O\bigl(p^{2399/1280}\bigr).
\]
This exponent sits \(3/8-1/1280\) above target and \(3/8+1/1280\) below the inherited \(9/4\). It improves the per-class prices of Round 179 (\(O(p^2)\) for \(J=0\), \(O(p^{2-1/640})\) for \(J=1\)). It also improves the Round 177 common-\(b\) bound \(O(p^{2-3/418-1/1280})\) on the common-\(b\) subclass.

**Criterion 7 (b).** If \(\mathcal M_w=O(p^{1+1/1280})\), then \(\mathcal D_0+\mathcal D_1=O(p^{3/2})\). Under Route B this would need \(\sum_s w(s)P_s^2=O(p^{3/2+1/640})\), which is essentially the target itself. A direct first-mass estimate that does not go through the diagonal is needed. Note also that \(\mathcal M_w\le\mathcal D^{1/2}(\sum w)^{1/2}\), so reaching the target \(\mathcal D=O(p^{3/2})\) would already give \(\mathcal M_w=O(p^{1})\).

## 4. Generic classes J ∉ {0,1}

### 4.1 The fibre over a fixed line is an irreducible hyperbola

Fix \(e=(\pi,\rho)\) and \(J\). With \(u=\pi'\), \(t=\rho'\), the class condition is \(F(u,t)=0\), where
\[
F(u,t)=(\pi-u)(\rho-t)-J(\rho-\pi)(t-u)=(u+\beta)(t+\alpha)-J(1-J)(\rho-\pi)^2,
\]
\[
\alpha=(J-1)\rho-J\pi,\qquad\beta=(J-1)\pi-J\rho .
\]
The identity is \(\alpha\beta-\pi\rho=J(1-J)(\rho-\pi)^2\). For \(J\notin\{0,1\}\) the constant is nonzero (since \(\rho\ne\pi\)), so \(F\) is absolutely irreducible: a product of two independent linear forms minus a nonzero constant. For \(J=0\) the curve splits into the lines \(u=\pi\) and \(t=\rho\). For \(J=1\) it splits into \(u=\rho\) and \(t=\pi\). This agrees with Corollary 4.

**Lemma 8.** For \(J\notin\{0,1\}\), each value \(y=1/Y'\) occurs for at most two \(e'\) in the fibre.

*Proof.* \(1/Y'=y\) is the line \(1-u=y(t-u)\). Restricted to a line, \(F\) is a polynomial of degree at most 2 in the line's parameter. It is not identically zero, since an irreducible conic contains no line. \(\square\)

**Proposition 9 (a).** For every \(J\notin\{0,1\}\),
\[
\mathcal D_J\le 2G\,\mathcal M_w=O(p^{1/2+11/8})=O(p^{15/8}).
\]

*Proof.* At fixed \(s,e\), bound the second copy by \(g(Y')\) alone, keeping \(w\) and the first copy. Lemma 8 and inversion symmetry give \(\sum_{e':J}a_{e'}(s)\le2\sum_y g(y)\le 2G\). Then sum against \(w(s)a_e(s)\). \(\square\)

This improves Round 179's per-class \(O(p^{2-1/640})\). There are up to \(p-2\) nonempty generic classes, and every \(\mathcal D_J\ge0\), so sorting by \(J\) gives no cancellation. Summing these bounds is useless. The generic range is bounded only by \(\mathcal D_{\rm gen}\le\mathcal D=O(p^{9/4})\).

### 4.2 Exact four-point normal form (the remaining quantity)

For \(J\notin\{0,1\}\) the points \(\pi,\rho,\rho'\) are distinct. Let
\[
\gamma(z)=[z;\pi,\rho,\rho'],
\]
so that \(\gamma(\pi)=0\), \(\gamma(\rho)=1\), \(\gamma(\rho')=\infty\) and \(\gamma(\pi')=J\). Put \(z_0=\gamma(0)\), \(z_1=\gamma(1)\), \(z_X=\gamma(X)\) and \(z_\infty=\gamma(\infty)=(\rho-\rho')/(\rho-\pi)\).

Cross-ratios are invariant under Möbius maps, and \([z;a,\infty,c]=(z-a)/(z-c)\). So Lemma 1 gives:

| Copy | \(1/A\) | \(1/Y\) | \(1/C\) | \(1/D\) |
|---|---|---|---|---|
| first | \([z_X;0,1,z_\infty]\) | \([z_1;0,1,z_\infty]\) | \([z_X;0,1,z_0]\) | \([z_1;0,1,z_0]\) |
| second | \(\dfrac{z_X-J}{z_X-z_\infty}\) | \(\dfrac{z_1-J}{z_1-z_\infty}\) | \(\dfrac{z_X-J}{z_X-z_0}\) | \(\dfrac{z_1-J}{z_1-z_0}\) |

The parameters are recovered as
\[
X=[z_X;z_0,z_1,z_\infty],\quad \pi=[0;z_0,z_1,z_\infty],\quad \rho=[1;z_0,z_1,z_\infty],\quad \pi'=[J;z_0,z_1,z_\infty],\quad \rho'=[\infty;z_0,z_1,z_\infty].
\]

The two interior conditions (Lemma 2 for both copies) together with \(J\notin\{0,1\}\) make
\[
(e,e',X)\longleftrightarrow(J;z_0,z_1,z_X,z_\infty)
\]
a bijection onto the quadruples of pairwise distinct elements of \(\mathbb F_p\setminus\{0,1,J\}\). All \(z\)'s are finite because \(0,1,X,\infty\ne\rho'\).

Define
\[
\varphi_0(z)=g([z;0,1,z_\infty])\,g([z;0,1,z_0]),\qquad
\varphi_J(z)=g\Bigl(\frac{z-J}{z-z_\infty}\Bigr)g\Bigl(\frac{z-J}{z-z_0}\Bigr),\qquad \psi=\varphi_0\varphi_J .
\]
By inversion symmetry of \(g\) and \(w\), and since \(w(s)=w(1/s)=w(X)\),
\[
\mathcal D_J=\sum_{z_0\ne z_\infty}\ \sum_{z_1\ne z_X}w\bigl([z_X;z_0,z_1,z_\infty]\bigr)\,\psi(z_X)\,\widetilde\psi(z_1),
\qquad \widetilde\psi=\psi\cdot1_{\mathcal M}(e)1_{\mathcal M}(e').
\]
All dependence on \(z_0,z_\infty,J\) is through \(\psi\) and the kernel. A mask that depends only on the line parameters (as \(b\in Q\), that is \(\pi\in Q\), does) is a function of \(z_1\) alone at fixed \((J,z_0,z_\infty)\), because \(\pi,\pi'\) are. Such a mask is absorbed into \(\widetilde\psi\). A mask depending on \(s\) as well would have to be kept in the kernel. The distinctness conditions are part of the summation range.

So, at fixed \((J,z_0,z_\infty)\), \(\mathcal D_J\) is exactly a bilinear form with kernel \(W(z_X,z_1)=w([z_X;z_0,z_1,z_\infty])\) between \(\psi\) and \(\widetilde\psi\). All eight amplitude factors and \(w\) are kept (verified exactly; see Section 6).

## 5. What was majorized by one, and where

| Step | Kept | Bounded by one |
|---|---|---|
| Proposition 5, rows with \(\pi\) fixed | \(w\); first copy; \(g(Y'),g(D')\) | \(g(A'),g(C')\); second mask |
| Proposition 5, rows with \(\rho\) fixed | \(w\); first copy; \(g(Y'),g(A')\) | \(g(C'),g(D')\); second mask |
| Proposition 9 | \(w\); first copy; \(g(Y')\) | \(g(A'),g(C'),g(D')\); second mask |
| \(\mathcal M_w\) (Route B) | — | internal to Round 179: \(D,D'\), masks, \(w\) |
| \(\mathcal M_w\) (Route A) | — | \(g(C)\) |
| Normal form (Section 4.2) | everything | nothing |

All bounding by one happens after the J sorting. In particular \(D\) and \(w\) are never bounded by one before the sort.

## 6. Evidence (c)

All scripts are in `/private/tmp/claude-501/-Users-lyuyuwei--claude-spares-spare-6UwrMo/5c2fbe9f-e42f-418e-9bd9-cc365745ecfe/scratchpad/r180/`.

- `exact_check.py` (pure Python, exact arithmetic mod p; re-run for this report). For \(p=13,17,29,37,41\) and all chart triples, it checks:
  - the equivalence in Lemma 2;
  - the four cross-ratio formulas of Lemma 1 and \(\rho=Y/D\);
  - for all ordered pairs of interior lines with all labels in \(Q\setminus\{1\}\) at every \(s\in Q\setminus\{1\}\): \(J_{\rm R179}=[\pi';\pi,\rho,\rho']\), \(J=0\iff\{\pi'=\pi\text{ or }\rho'=\rho\}\), and \(J=1\iff\{\pi'=\rho\text{ or }\rho'=\pi\}\).

  Pair counts (J=0 / J=1 / generic):

  | p | J=0 | J=1 | generic |
  |---|---|---|---|
  | 13 | 6 | 0 | 4 |
  | 17 | 54 | 44 | 40 |
  | 29 | 2034 | 1228 | 5492 |
  | 37 | 7728 | 5044 | 30552 |
  | 41 | 13080 | 8338 | 60536 |

- `normal_form_check.py` (re-run). Checks every entry of the Section 4.2 table, the recovery formulas for \(X,\pi,\pi'\), and \(\gamma(\pi')=J\). It used 3000 random generic configurations at each of \(p=101,409,1009\), with no failures.
- `row_fibre_check.py` (new, re-run). For \(p=13,17,29,37\) it checks:
  - the row identities \(1/D=\pi(1/Y)+1-\pi\) and \(1/A=c(1/Y)+1-c\) with \(c\notin\{0,1\}\), on all interior triples;
  - \(k,d\) and \(J=d(k+d-1)/k\) via \(h=j_{e'}\circ j_e^{-1}\), and the factorization of \(J-1\);
  - that each value of \(1/Y'\) occurs at most twice in a generic fibre over a fixed line, on a deterministic subsample of first lines (maximum observed: 2).
- Model runs (`model_sub.py`, `linked_check.py`, `model_J.py`; floating point, NumPy). These were run earlier in this round. They were not re-run for this report, because the NumPy environment has been deleted. Their logs were not saved, so only the earlier summary's figures can be quoted: on two-subgroup mixture models \(g=(1_{H_1}+1_{H_2})^2/4\) with \(p\) up to 601, \(\mathcal D/p^{3/2}\le2\cdot10^{-4}\), and \(J=0\) carries 11–32% of \(\mathcal D\). `linked_check.py` compared \(\mathcal D_0,\mathcal D_1\) with \((\sup F_\pi+\sup F^\rho)\mathcal M_w\). These are models, not the actual \(g\), and say nothing about the asymptotic target.
- The symbolic checks `sym1.py` and `sym2.py` (SymPy) were run earlier and agree with Proposition 3 and the companion invariance. They cannot be re-run now because SymPy is gone. Proposition 3 is proved by hand above and checked exactly modulo p.

## 7. Remaining gap

- **Proved:** \(\mathcal D_0+\mathcal D_1=O(p^{2399/1280})\), and each \(\mathcal D_J=O(p^{15/8})\) for \(J\notin\{0,1\}\).
- **Open:** \(\mathcal D_{\rm gen}=\sum_{J\ne0,1}\mathcal D_J\), still only \(O(p^{9/4})\). The exact remaining quantity has two equivalent forms:
  - In the Round 179 variables:
    \[
    \sum_s w(s)\sum_e a_e(s)\sum_{(k,d):\ d\notin\{0,1\},\ k+d\notin\{0,1\}}a_{h_{k,d}\circ e}(s),
    \]
    with \(J=d(k+d-1)/k\), \(v'=kv+d\), \(x'=kx+d\), \(u'=h_{\lambda/k}(u)\).
  - In normal form:
    \[
    \sum_{J\ne0,1}\ \sum_{z_0\ne z_\infty}\ \langle \psi_{J,z_0,z_\infty},\,W_{z_0,z_\infty}\,\widetilde\psi_{J,z_0,z_\infty}\rangle,
    \]
    where \(W_{z_0,z_\infty}(z_X,z_1)=w([z_X;z_0,z_1,z_\infty])\).
- **Also open:** the first mass \(\mathcal M_w\) at \(O(p^{1+1/1280})\), which would close \(J\in\{0,1\}\) by Criterion 7.

Nothing here refutes the sufficient diagonal. No lower bound beyond the trivial one was found for \(\mathcal D_{\rm gen}\).

## 8. Next tests, ranked

1. A first-mass bound \(\mathcal M_w=\sum_s w(s)P_s=O(p^{1+1/1280})\) that does not pass through the second moment. Currently \(\mathcal M_w=O(p^{11/8})\). This closes \(J\in\{0,1\}\) at once, and with Proposition 9 it lowers each generic class to \(O(p^{3/2+1/1280})\).
2. A bilinear estimate at fixed \((z_0,z_\infty)\) for the kernel \(w([z_X;z_0,z_1,z_\infty])\), summed over \(J\). At fixed \(z_0,z_\infty,z_1\) the kernel is a Möbius image of \(w\) in \(z_X\). A saving must come from the \(J\)-dependence of \(\varphi_J\), shared between \(z_X\) and \(z_1\). Positivity forbids any cancellation in \(J\).
