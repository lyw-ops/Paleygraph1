# Exact favorable masks in the true affine chart

Keep the actual selected near-critical short block, eligible primes, endpoints and weights of [Round 174](ordinary-pin-favorable-collision-cut-174.md). In the physical affine chart, the existing \(b\in Q\) mask is equivalent to \(\chi(1-r)=1\) on nonzero contributing \(Y,D\in Q\). Indeed
\[
 b=\frac DY\frac{1-Y}{1-D}=\frac DY(1-r).
\]
Also
\[
 1-A=(1-r)(1-C),\qquad 1-Y=(1-r)(1-D).
\]
The signs for \(A,C\) agree and the signs for \(Y,D\) agree before imposing any favorable restriction. Thus the five favorable masks reduce exactly to the three conditions
\[
 \chi(1-A)=\rho,\qquad \chi(1-Y)=\rho,\qquad
 \chi(A-Y)=\rho\,\chi(r).
\]
For the last equality use \(s=AD/(CY)\), \(CY-AD=r(C-D)\), and \(C-D=(A-Y)/(1-r)\). The denominators have nonzero square sign and \(s\ne1\). All input weights \(g(A),g(C),g(Y),g(D)\) and output weight \(w(s)\) remain. In the two-copy same-slope expansion, the common output condition and two input conditions per copy give five distinct sign factors before any further coincidences are imposed. The existing \(b\)-square constraint already supplies the sign of \(1-r\).

A fixed projective relation between two pairs of cross-copy labels is also removable at the sufficient full diagonal scale. At each slope \(s\) specify two distinct roles per copy and \((x',y')=(T_s(x),U_s(y))\) for projective maps \(T_s,U_s\), allowing the maps to depend on \(s\). Retain finite defined images only. The two-role kernel of [Round 173](ordinary-full-diagonal-two-pin-173.md) has multiplicity at most two and total mass at most \(G^3\). The map of the pair of indices is injective at each \(s\), so the pullback of the second weighted kernel has squared norm at most \(2G^3\), as does the first kernel. Cauchy–Schwarz then bounds this positive two-copy portion by \(O(G^3)=O(p^{3/2})\). Similarly, when the two copies share \(r\) or share \(b\), one projective relation between single cross-copy roles suffices, with maps allowed to depend on the shared slope and common parameter. The fixed-parameter one-role chart is injective and its total tuple mass is at most \(G^3\). The same argument applies.

The true positive common-\(b\) portion already enters the full squared norm directly, with sufficient scale \(O(p^{3/2})\). Square-root bounds for individual Jacobi sums belong to a separate character expansion of that portion and do not multiply the positive physical portion. The previous common-\(b\) bound \(O(p^{2-1/640})\) and whole diagonal bound \(O(p^{37/16})\) still control the unresolved classes.
