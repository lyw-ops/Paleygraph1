# Two-argument coincidences and some same-pole terms on the full diagonal

Use the actual \(g,w\), eligible primes, mark \(v\ne0\), and physical \(u\)-square condition of [Round 172](ordinary-full-diagonal-affine-172.md). Put \(G=\sum g=O(\sqrt p)\). In the physical two-copy expansion of \(\sum_s w(s)P_s^2\), remove the already priced \(x=0,y=0\) boundary at target scale in norm. In the resulting tuples \(A,C,Y,D\) are all nonzero and different from \(1\), \(u\ne0,1\), and \(s\ne0,1\). Each tuple has weight \(g(A)g(C)g(Y)g(D)\). The first and second copies have the same physical slope.

## Two physical labels can be fixed at target cost

At fixed \(s\), any two different argument roles and their specified values determine at most two retained physical tuples. The multiplicity is bounded as follows.

- Giving \(A,Y\) determines at most one \(u\) by \(sY(1-u+uA)=A(1-u+uY)\). If its linear coefficient and constant both vanished, \(sY=A\) would make the coefficient \(A(A-Y)\) nonzero since \(A\ne Y\). Giving \(C,D\) uses the inverse affine map and \(s^{-1}\) and has the same bound.
- Giving \(A,C\) determines \(u=(1-C)/(1-A)\); the required ratio \(D/Y=sC/A\) then determines \(Y\) from \(D=1-u+uY\) because \(1-u\ne0\). Giving \(Y,D\) determines \(u\) and \(C/A=D/(sY)\) similarly.
- Use \(E=A/s\), \(CY=DE\), \(C+Y=D+sE+(1-s)DE\). Giving \(A,D\) fixes \(E\) and hence the sum and product of \(C,Y\), up to two roots. Giving \(C,Y\) instead makes \(D\) satisfy \(D^2+((1-s)CY-C-Y)D+sCY=0\), with \(E\) then determined.

The physical variables \(x,y\) are recovered uniquely whenever \(u,A,Y\) are known. The total tuple mass over all \(s\ne0,1\) is at most \(G^3\). Giving \(A,C,Y\) determines \(u,D,s\), and the remaining weight \(g(D)\) is at most one.

For fixed ordered distinct roles \(i,j\), denote the weighted restricted kernel by \(T_{ij}(s;a,b')\). For every \(s,a,b'\) the multiplicity just proved gives \(T_{ij}\le2\), and \(\sum_{s,a,b'} T_{ij}\le G^3\). As \(w\le1\),
\[
 \sum_{s,a,b'} w(s)T_{ij}(s;a,b')^2\le 2G^3.
\]
Cauchy in this weighted norm gives the same bound with any other ordered pair of distinct roles in the second copy. Thus the union of all such two-label coincidences, including distinct roles permuted between copies, costs \(O(G^3)=O(p^{3/2})\). This is a positive physical cut in the full one-slope criterion. It does not require passing to the twisted two-dimensional energy.

There is also a cut for a common affine intercept \(b\) or slope \(r\) together with one literal physical argument between the two copies. At fixed \(s,b\), each of \(A,C,Y,D\) is injective as a function of the remaining parameter \(r\): use
\[
 A=\frac{rs}{s-b},\quad
 C=\frac{rb}{(1-r)(s-b)},\quad
 Y=\frac r{1-b},\quad D=\frac{br}{(1-r)(1-b)}.
\]
All denominators are nonzero on the retained domain. At fixed \(s,r\), each is likewise injective as a function of \(b\), using \(s\ne0\) for \(C\). Applying the same restricted-mass argument proves a target-scale cost for these intersections. Equality of \(b\) alone or \(r\) alone is not covered.

## Degenerate two-root Jacobi terms at a common affine intercept

This is a separate character expansion using the prior positive completion of the \(A=1\) boundary. Retain the actual \(\omega\), its cap \(\kappa=O(p^{-1/2})\), the square condition and \(\ell=\omega-\omega*\omega\), the Fourier coefficients of \(w\). Open the two-character formula of Round 171 for the first copy, with characters \(\alpha,\beta\), and its conjugate for the second, with \(\alpha',\beta'\). Put \(\gamma=\alpha\beta,\ \gamma'=\alpha'\beta'\). After opening \(w\) with character \(\delta\), the \(s\)-dependent character product for pairs sharing an intercept \(b\) is
\[
 L(s)M(s-b),\qquad L=\delta\alpha/\alpha',\quad M=\gamma'/\gamma .
\]
All other character phases have modulus one. The convention that even the trivial character vanishes at zero keeps the two physical exclusions exactly before any completion. Temporarily completing from \(s\ne0,1\) to the full field adds at most 1 in absolute value at each fixed tuple. Since \(b\ne0\), the completed sum is a unit scalar times \(J(L,M)\) by \(s=b x\).

The mass of line pairs sharing \(b\) is at most \(G^3\): fixing \(b=(1-Y)D/(Y(1-D))\) and one of \(Y,D\) determines the other, so the single \(b\)-row weight is at most \(G\), and the total line weight is at most \(G^2\). This also bounds the completion error after \(\|\ell\|_1\le2\). Terms with exactly one trivial character or with both characters nontrivial and \(LM=1\) have \(|J|\le1\); hence they cost \(O(G^3)\). If \(L=M=1\), the Jacobi bound is \(p-2\), but at fixed \(\alpha,\alpha',\beta\) the equation \(\gamma'=\gamma\) determines \(\beta'\) at \(\omega\)-cost at most \(\kappa\), and \(L=1\) determines \(\delta\) at absolute \(\ell\)-cost at most \(2\kappa\). Even with the \(p\) bound the terms cost \(O(p\kappa^2G^3)=O(p^{3/2})\). This uses the signed actual outer law and full line masks. These are cuts in a character expansion distinct from the physical two-label cuts, so the same terms must not be debited twice.

The regular same-intercept terms still have a square-root Jacobi cost per tuple and the distinct-intercept terms are not supplied by this argument. The full diagonal target remains open.

## Removing the logarithm in the full diagonal bound

The gateway's output-first incidence orientation can remove the logarithm from the full diagonal estimate once the secondary term is retained. Use the already checked \(j_{Y,D}(X)=1/r-(b/r)X\) chart of Round 172, with \(X=1/s\). Keep the original \(b\)-square mask. For the heavy \(Y,D\) with \(g(Y),g(D)>p^{-1/8}\), omit \(g(C)\) positively and call the resulting nonnegative upper \(F(X)\). Thus \(F\le G^2\) pointwise. It contains the three actual factors \(g(Y)g(D)h(j_{Y,D}(X))\), where \(h(e)=g(e^{-1})\) off zero and \(h(0)=0\). Extending \(X\) by the same chart is an upper on the true \(s\ne0,1\) domain.

For an arbitrary output set \(S\) of \(X\)'s, use the graphs \(e=j_{Y,D}(X)\) for incidence on \(S\times T\), where \(T\) is a level of the input \(h(e)\). The project's projective line chart gives \(m_{\mathcal L},M_{\mathcal L}\le2V\) and \(N_{\mathcal L}\le UV\), with the same heavy size condition as Round 172. The finite-field point-line estimate gives
\[
 I(S\times T,\mathcal L)
 \ll |T|^{1/2}
  \left(|S|^{5/8}E(\mathcal L)^{1/8}N_{\mathcal L}^{1/2}
                 +N_{\mathcal L}\max(1,|S|/\sqrt p)\right).
\]
Use [Petridis–Roche-Newton–Rudnev–Warren, Theorems 1.1 and 2.1](https://arxiv.org/abs/1911.03401). After layer cake in the three true weights this gives
\[
 \sum_{X\in S}F(X)
 \ll |S|^{5/8}G^{35/16}
      +G^{5/2}\bigl(1+|S|/\sqrt p\bigr).
\]
In the first term, \(E^{1/8}N_{\mathcal L}^{1/2}\) is bounded as in Round 172 by \(U^{13/16}V^{7/8}+U^{3/4}V^{7/8}\), and the remaining level exponent is \(1/2\). In the secondary term, integrate \(N_{\mathcal L}\) exactly to at most \(G^2\) and the square root of the input level size to \(O(\sqrt G)\). The plateau on the \(Y,D\) thresholds below \(p^{-1/8}\) is retained in the layer-cake integral.

Consequently the decreasing rearrangement obeys
\[
 F^*(k)\ll
    G^{35/16}k^{-3/8}
    +\min\{G^2,G^{5/2}/k\}+G^{5/2}/\sqrt p .
\]
Here the pointwise \(G^2\) bound is used to clip the potentially large secondary term. Since \(w\le1\) and its counting mass is at most \(G\), integrate the squares of the displayed upper only to \(\lceil G\rceil\). The first term gives \(O(G^{35/8}G^{1/4})=O(G^{37/8})\). Split the clipped term at \(k=\sqrt G\); either part is at most \(O(G^{9/2})\). The last term costs \(O(G^6/p)=O(G^4)\). The true light-pair diagonal costs at most \(O(p^{9/4})\) at this cutoff and the endpoint error is \(O(p^{3/2})\), as in Round 172. Thus the entire original weighted diagonal satisfies
\[
 \sum_{s\ne0,1}w(s)P_s^2 = O(p^{37/16})
\]
without a logarithm. This uses the true output mass and a positive upper retaining three of the four physical factors. It leaves the power gap to \(p^{3/2}\) and the need for a genuinely coupled estimate.

The heavy affine-fiber bound of [the weighted-energy note](ordinary-weighted-affine-vertical-saving-173.md) also improves the physical line mass in a fixed \(b\)-row. At fixed \(b\ne0,1\), the equation \(b=D(1-Y)/(Y(1-D))\) becomes
\[
 \frac1Y=b\,\frac1D+(1-b).
\]
The true \(g\) is inversion symmetric because it is the squared modulus of a characteristic function of a real probability. Thus, with both weights at least \(\tau=p^{-1/1280}\), this row has at most \(O(p^{1/2-1/640})\) pairs by the proved two-level affine estimate. The parts with either weight below \(\tau\) each cost at most \(\tau G\), since both row directions are injective. Consequently the true \(b\)-row mass is \(O(p^{1/2-1/1280})\) uniformly, and the weight of same-\(b\) line pairs is \(O(p^{3/2-1/1280})\). The regular same-\(b\) two-root Jacobi terms therefore have absolute weighted bound \(O(p^{2-1/1280})\) from their \(\sqrt p\) individual estimates. This remains above the target.

The same affine-fiber estimate also gives a power improvement for the entire positive same-\(b\) and same-\(r\) physical classes. In the original line formulas fix \((r,b)\) and vary the admissible \(s\). The map \(s\mapsto A=rs/(s-b)\) is injective off its pole since \(rb\ne0\), and
\[
 C=\frac{A-r}{1-r}.
\]
This is an affine map with nonzero slope and translation for \(r\ne0,1\). The \(A\)-values with \(g(A),g(C)\ge\tau\) number \(O(p^{1/2-1/640})\). The two complementary light pieces each contribute at most \(\tau G\) because both argument maps are injective. Thus
\[
 \sum_s g(A_{r,b}(s))g(C_{r,b}(s))=O(p^{1/2-1/1280})
\]
uniformly with the true exclusions. The actual \(r\)-row mass \(\sum_b\mu_0(r,b)\) has the same bound, using \(Y=r+(1-r)D\) and the light-pair estimate with the two injective directions. The \(b\)-row mass was bounded above in the same way.

For either kind of row let \(m\) be its mass and \(F_{\rm row}(s)\) its nonnegative physical kernel. Then \(F_{\rm row}\le m\) pointwise and \(\sum_s F_{\rm row}(s)\ll p^{1/2-1/1280}m\), by the per-line estimate. Since \(\sum_{\rm rows}m\le G^2\) and \(\sup_{\rm rows}m\ll p^{1/2-1/1280}\), the corresponding full same-parameter collision contribution is at most
\[
 \sum_{\rm rows}\sum_s w(s) F_{\rm row}(s)^2
 \ll p^{1/2-1/1280}\sum_{\rm rows}m^2
 \ll p^{2-1/640}.
\]
The two classes overlap. Each bound is valid separately and neither reaches the \(O(p^{3/2})\) target for the unpinned entire class.
