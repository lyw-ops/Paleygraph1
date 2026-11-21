# The paired J invariant as a cross-ratio, and the two degenerate classes

Use the actual \(g\), \(w=g(1-g)\) and \(G=\sum g=O(\sqrt p)\), the physical masks and nonzero interior of [Round 178](ordinary-parabolic-row-mean-square-178.md), and the two-copy chart of [Round 179](ordinary-affine-triple-diagonal-179.md). Counting norms are used throughout.

Write \(\mathcal D=\sum_s w(s)P_s^2=\sum_c\mathcal D_c\), where \(\mathcal D_c\) collects the pairs of lines at common output with \(J=c\). This note proves:
- \(J\) is a cross-ratio of the two lines.
- The classes \(J\in\{0,1\}\) cost \(O(p^{2399/1280})\).
- Each single class \(J\notin\{0,1\}\) costs \(O(p^{15/8})\).

The sum over the generic classes remains at the Round 179 bound \(O(p^{9/4})\), and the sufficient \(O(p^{3/2})\) diagonal remains open.

The argument was found by a native Claude research agent (archived draft: [native-claude-ordinary-prime-paired-J-fibers-180.md](native-claude-ordinary-prime-paired-J-fibers-180.md)). An independent agent audit checked it: [native-claude-audit-180.md](native-claude-audit-180.md).

## Lines as cross-ratios

Put \(X=1/s\), \(\pi=1/b\) and \(\rho=(1-r)/b\), and call \(e=(\pi,\rho)\) the line. Write \([z;a,b,c]\) for the Möbius map sending \(a,b,c\) to \(0,1,\infty\). From the Round 178 labels,
\[
 \tfrac1A=[X;\pi,\rho,\infty],\quad \tfrac1Y=[1;\pi,\rho,\infty],\quad
 \tfrac1C=[X;\pi,\rho,0],\quad \tfrac1D=[1;\pi,\rho,0].
\]
The nonzero interior is exactly the condition that \(0,1,\infty,X,\pi,\rho\) are pairwise distinct.

Let \(j_e(z)=(z-\pi)/(\rho-\pi)\). For two lines at the same output, the Round 179 paired map is \(h_k=j_{e'}\circ j_e^{-1}\). In particular it does not depend on \(s\). Its coefficients are
\[
 k=\frac{\rho-\pi}{\rho'-\pi'},\qquad d=j_{e'}(\pi),\qquad k+d=j_{e'}(\rho),
\]
and therefore
\[
 J=\frac{d(k+d-1)}{k}=[\pi';\pi,\rho,\rho']=\frac{(\pi-\pi')(\rho-\rho')}{(\rho-\pi)(\rho'-\pi')},\qquad
 J-1=\frac{(\pi-\rho')(\rho-\pi')}{(\rho-\pi)(\rho'-\pi')}.
\]
Consequently:
- \(J=0\) exactly when \(\pi'=\pi\) (common \(b\)) or \(\rho'=\rho\) (common \(Y/D\)).
- \(J=1\) exactly when \(\pi'=\rho\) or \(\rho'=\pi\).

Neither condition is a common \(r\) or a common \(k\).

## The classes J ∈ {0,1}

**Affine row bound.** From [Round 173](ordinary-weighted-affine-vertical-saving-173.md), uniformly in \(cd\ne0\),
\[
 R_*=\sup_{cd\ne0}\sum_z g(z)g(cz+d)=O(p^{1/2-1/1280}).
\]
- Pairs with both weights at least \(p^{-1/1280}\) form an affine heavy set of size \(O(p^{1/2-1/640})\).
- The other pairs cost at most \(2p^{-1/1280}G\).

**Rows at a fixed parameter.** At fixed \(s\), the lines with fixed \(\pi\) form an affine row \(1/D'=\pi(1/Y')+1-\pi\). The lines with fixed \(\rho\) form \(1/A'=c(1/Y')+1-c\), where \(c=(X-\rho)/(1-\rho)\notin\{0,1\}\). By inversion symmetry of \(g\), each row sum is at most \(R_*\). This step bounds two second-copy factors and the second-copy mask by one, only after the \(J\) sorting.

Inserting \(1[J=0]\le1[\pi'=\pi]+1[\rho'=\rho]\), and the analogous bound for \(J=1\), gives
\[
 \mathcal D_0+\mathcal D_1\le 4R_*\mathcal M_w,\qquad \mathcal M_w=\sum_s w(s)P_s .
\]

**The first mass.** Since \(w\le g\), \(\sum_s w(s)\le G\). Cauchy–Schwarz against the accepted Round 179 whole diagonal gives
\[
 \mathcal M_w\le G^{1/2}\,O(p^{9/8})=O(p^{11/8}),
\]
and so
\[
 \mathcal D_0+\mathcal D_1=O(p^{15/8-1/1280})=O(p^{2399/1280}).
\]

**Scope of retained weights.** The step \(\mathcal D_0+\mathcal D_1\le4R_*\mathcal M_w\) keeps \(w\), the whole first copy and two second-copy factors. The factor \(\mathcal M_w\) passes through Round 179, whose decisive bound majorizes \(D\), \(D'\), the masks and \(w\) by one. The final exponent therefore does not retain \(D\) and \(w\) in the sense of the mission (audit correction).

**Conditional criterion.** If \(\mathcal M_w=O(p^{1+1/1280})\), then \(\mathcal D_0+\mathcal D_1=O(p^{3/2})\). Through Cauchy–Schwarz this would need essentially the target diagonal itself, so a direct first-mass estimate is required.

## Generic classes

Fix \(e\) and \(J\notin\{0,1\}\). The fibre in \((\pi',\rho')\) is the curve
\[
 (\pi'+\beta)(\rho'+\alpha)=J(1-J)(\rho-\pi)^2,\qquad
 \alpha=(J-1)\rho-J\pi,\quad \beta=(J-1)\pi-J\rho .
\]
Its right side is nonzero, so the curve is absolutely irreducible. A line \(1/Y'=y\) therefore meets the fibre in at most two points. Bounding the remaining second-copy factors by one gives
\[
 \mathcal D_J\le 2G\,\mathcal M_w=O(p^{15/8}).
\]
This improves the Round 179 per-class price \(O(p^{2-1/640})\). There are up to \(p-2\) generic classes and every \(\mathcal D_J\) is nonnegative, so sorting by \(J\) gives no cancellation. The generic range stays at \(\mathcal D_{\rm gen}\le\mathcal D=O(p^{9/4})\).

## The remaining quantity in normal form

For \(J\notin\{0,1\}\), use \(\gamma=[\,\cdot\,;\pi,\rho,\rho']\) and put \(z_0=\gamma(0)\), \(z_1=\gamma(1)\), \(z_X=\gamma(X)\), \(z_\infty=\gamma(\infty)\). Then \((e,e',X)\) corresponds bijectively to \((J;z_0,z_1,z_X,z_\infty)\), with the four \(z\)'s pairwise distinct in \(\mathbb F_p\setminus\{0,1,J\}\). The eight labels are explicit Möbius images:
- first copy: \([z;0,1,z_\infty]\) and \([z;0,1,z_0]\);
- second copy: \((z-J)/(z-z_\infty)\) and \((z-J)/(z-z_0)\);

each at \(z=z_X\) and \(z=z_1\). At fixed \((J,z_0,z_\infty)\), \(\mathcal D_J\) is exactly a bilinear form in \(z_X\) and \(z_1\) with kernel \(w([z_X;z_0,z_1,z_\infty])\), and all eight amplitudes and \(w\) are kept. The open problem is a saving summed over \(J\) in this form.

## Checks

These finite diagnostics use exact arithmetic modulo \(p\):
- [paley-180-J-exact-check.py](paley-180-J-exact-check.py), at \(p=13,17,29,37,41\) over all chart pairs: the cross-ratio labels, the interior criterion, and the exact \(J=0\) and \(J=1\) conditions.
- [paley-180-J-normal-form-check.py](paley-180-J-normal-form-check.py): the normal-form table, on 3000 random configurations at each of \(p=101,409,1009\).
- [paley-180-J-row-fibre-check.py](paley-180-J-row-fibre-check.py), run with arguments `13 17 29 37`: the row identities, and multiplicity at most two in generic fibres.
- [paley-180-audit-J-check.py](paley-180-audit-J-check.py), the independent audit: Round 179's own \(k,d\) against the cross-ratio on all pairs at \(p\le29\).

## Next tests

1. A direct first-mass bound \(\mathcal M_w=O(p^{1+1/1280})\) that avoids the second moment.
2. A bilinear estimate for the Möbius kernel at fixed \((z_0,z_\infty)\), summed over \(J\), keeping the eight amplitudes.
