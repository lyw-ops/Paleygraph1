# A marked inverse-square spectral window forced by any fixed gap

This test uses the actual optimum for the first-spill sign with the same physical mark and admissible growing time \(T\) as in [Round 150](ordinary-prime-repair-source-150.md). It applies without any assumption that the retargeted deficit has critical effective size.

Under the fixed hypothetical gap and fixed floor of that round, the original marked first reflection has actual bulk negative part \(b^{(0)}\), with
\(\mathbb E(F b^{(0)})\ge g\) for every true opposite optimum \(F\), where \(g\) is bounded below by a positive constant. The bound \(\mathbb E[(b^{(0)})^2]=O(T^{-1})\) and the deleted marked site give
\[
                      \mathbb E(1_{\rm bulk}F^2)\ge cT .
\]
In particular this holds on the true least-bulk-energy optimum. In the notation of [Round 137](ordinary-bulk-spectrum-137.md), let \(x=F|_S\) on its actual positive bulk support, and let \(A,g_S,\mu_p\) be the corresponding compressed operator, marked forcing, and its spectral measure divided by \(n\). Use \(g_S\) to distinguish that forcing from the scalar gap \(g\). One has
\[
 D_p=\|x\|_2^2/n=\int\lambda^{-2}\,d\mu_p\ge cT,\qquad
 \int\lambda^{-1}\,d\mu_p\le C
\]
on the fixed gap, with zero mass at \(\lambda=0\).

The probability \(d\zeta_p=\lambda^{-2}d\mu_p/D_p\) consequently satisfies
\[
 \zeta_p([\Lambda,2])\le C/(D_p\Lambda)\le C/(cT\Lambda).
\]
For a sufficiently large fixed \(A_0\), the region \(0<\lambda\le A_0/T\) must contribute at least \(cT/2\) to the actual inverse-square moment. Thus a prime-uniform \(o(T)\) upper in every fixed window \(0<\lambda\le A_0/T\), at one selectable growing \(T\) in the original simultaneous marked window, would exclude the gap using only the low-spectrum part. It does not require bounding the inverse-square moment uniformly at all scales.

For example the spectral projection \(x_{\rm low}\) of the true bulk optimizer onto \(0<\lambda\le T^{-1/2}\) has \(\|x-x_{\rm low}\|_2/\|x\|_2=O(T^{-1/4})\). This follows from the same Markov bound and the exact spectral representation of \(x\). The low projection is close to the actual nonnegative row in relative second norm. No positivity or approximate moment claim for arbitrary adaptive supports is needed. The missing estimate is an upper on the source-weighted low spectrum on the actual supports \(S\), with the true forcing \(g_S\).
