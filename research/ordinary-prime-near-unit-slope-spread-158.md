# Near-unit physical slopes cannot occupy the critical scale

Let \(p\equiv1\pmod4\) run through ordinary primes in the hypothetical genuine selected near-critical branch of [Round 157](ordinary-marked-frequency-localization-157.md). Use the true probability \(\nu\) on \(\widehat Q\), its inverse Fourier function \(f\) on \(Q\), and the actual favorable sign \(\rho=-\sigma\). Then for every choice of \(\epsilon_p\downarrow0\),
\[
 \bigl|\{x\in Q:|f(x)|\ge1-\epsilon_p\}\bigr|=o(\sqrt p).
\]
This uses the actual cap \(\max\nu\ll p^{-1/2}\), \(\|f\|_2^2\sim\sqrt p\) in counting norm, the pin, and [the prime coset spread](ordinary-affine-correlations-152.md#allowing-a-growing-number-of-cosets).

## From the near-unit set to a large genuine subgroup

Write \(W=\{x\in Q:|f(x)|\ge1-\epsilon_p\}\). It contains the identity and is inversion-symmetric. On \(Q\) define
\[
 d(x)=\inf_{|z|=1}\|a(x)-z\|_{L^2(\nu(a))}
      =\sqrt{2(1-|f(x)|)}.
\]
The triangle inequality and pointwise unit modulus give \(d(xy)\le d(x)+d(y)\). Consequently \(|f|\ge1-L^2\epsilon_p\) on \(W^L\). For each fixed \(L\), Parseval bounds \(|W^L|\le2\sqrt p\) eventually.

Suppose \(|W|\ge c\sqrt p\) on a subsequence for a fixed \(c>0\), and put \(H=\langle W\rangle\). The word graph for the generating set \(W\) is undirected. If it had a geodesic of length \(3m\), its vertices at positions \(0,3,\ldots,3m\) would have pairwise disjoint one-step neighborhoods of size \(|W|\), all in \(W^{3m+1}\) after translating the start to the identity. Choosing fixed \(m\) with \((m+1)c>2\) contradicts the Parseval bound. Thus the diameter is bounded by a fixed \(L=L(c)\). In particular \(c\sqrt p\le h=|H|\le2\sqrt p\), and \(|f|\to1\) uniformly on \(H\).

By orthogonality on \(H\),
\[
 \tfrac1h\sum_{x\in H}|f(x)|^2=\sum_C\nu(C)^2,
\]
where \(C\) runs over cosets of the annihilator of \(H\) in \(\widehat Q\). The left side tends to one, so a coset \(C_0\) has \(\nu(C_0)=1-o(1)\). Let \(f_{C_0}(x)=\sum_{a\in C_0}\nu_a a(x)\). Its modulus is constant on every \(H\)-coset in \(Q\). The true cap gives
\[
 \|f-f_{C_0}\|_2^2=n\sum_{a\notin C_0}\nu_a^2
                 \ll \sqrt p\,\nu(\widehat Q\setminus C_0)=o(\sqrt p).
\]

## Wrong-sign mass and the prime coset estimate

The [exact pin comparison](ordinary-affine-jacobi-factorization-153.md#the-scalar-correction-for-a-true-critical-anchor) gives \(\sum_{\chi(1-x)=-\rho}|f(x)|^2=O(1)\). Thus \(f_{C_0}\) has \(o(\sqrt p)\) squared mass on this wrong sign. Call an \(H\)-coset good if at most \(h/4\) points have the wrong sign. On each other coset its whole squared mass is at most four times its wrong-sign mass, by constancy of the modulus.

Put \(S_\Omega=\sum_{x\in\Omega}\chi(1-x)\) for each coset \(\Omega\). Then
\[
 \sum_{\Omega}S_\Omega^2
 =\sum_{u\in H}\sum_{x\in Q}\chi((1-x)(1-u x)).
\]
The identity \(u=1\) costs at most \(n\), and the complete sum for every \(u\ne1\) is \(O(\sqrt p)\) uniformly, by opening the square restriction and applying the ordinary quadratic and squarefree cubic Weil bounds. Hence the sum is \(O(n+h\sqrt p)=O(p)\). On a good coset one has \(|S_\Omega|\ge h/2-1\), with the possible \(x=1\) treated separately. There are therefore \(O_c(1)\) good cosets. Their union captures all but \(o(\sqrt p)\) of the squared mass of \(f_{C_0}\) and of \(f\).

The cited Round 152 bound with a bounded number of cosets of order comparable to \(\sqrt p\) forbids this. Indeed its relative outside mass would be \(o(1)\), while the genuine critical branch has \(d_a=o(1)\) in true-anchor probability and bounded \(L=\max(1,m_{\rm eff}/m_0)\). The coset incidence argument in that bound is where prime order is essential. This contradiction proves the stated near-unit estimate.

In particular for every \(c>0\) there is a fixed \(\lambda(c)<1\) such that \(\#\{|f|>\lambda(c)\}<c\sqrt p\) eventually. Otherwise a diagonal subsequence with thresholds tending to one contradicts the theorem. The conclusion controls the top amplitude levels. It gives no \(O(p)\) upper on the matched anchor moment and permits an order-\(\sqrt p\) family of slopes at an amplitude bounded strictly below one.

## Smoothing under convolution and loss of within-set phase

For every integer sequence \(k_p\to\infty\),
\[
 n\|\nu^{*k_p}\|_2^2=\sum_{x\in Q}|f(x)|^{2k_p}=o(\sqrt p).
\]
To prove it, split at the fixed \(\lambda(c)\). The part above the threshold is at most \(c\sqrt p\). The rest is bounded by \(\lambda(c)^{2k_p-2}\|f\|_2^2\). Sending \(c\) to zero proves the result. More generally any fixed desired small multiple of \(\sqrt p\) is achieved uniformly eventually at a sufficiently large fixed convolution depth depending on that multiple.

If \(\check\nu(a)=\nu(a^{-1})\), the \(k_p\)-fold convolution of \(\nu*\check\nu\) has inverse transform \(|f|^{2k_p}\). Its mean Jacobi phase \(\mathbb E\,\rho k(a)\) is at most \(p^{-1/2}\sum|f|^{2k_p}=o(1)\) in modulus, by the defining Fourier formula for \(k\). By contrast, before these repeated convolutions the genuine pair law \(\nu*\check\nu\) has mean tending to one, as in Round 157. Thus the actual critical law loses its Jacobi alignment under convolution. The unresolved favorable moment uses its original coupled weights.
