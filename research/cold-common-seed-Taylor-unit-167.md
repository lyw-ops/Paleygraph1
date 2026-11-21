# A common seed unit across the true first two Taylor orders

Retain the actual \(R=V_{601}-V_{600}\), \(V_s=V_{600}+sR\), both lifts, the original complex square and physical \(t_0=n\) from [Round 165](cold-paired-Taylor-source-saving-165.md). Use its \(M,N,x,\varepsilon\). Let \(r_l^{\rm b}\) be the \(l\)-th bulk Taylor term, computed at all sites with the bulk parameter \(t\) before restoring the marked exception. The true shared Jacobi seed is \(S=2\sqrt n\,Ke_0\), with dimension mass \(s_n=2\sqrt{p/n}\).

## Exact shared scalar after transport by any frozen power

Off the exceptional trivial-character coordinate, the two actual lift values of the unit-normalized Jacobi seed are \(z,z^{-1}\). Indeed they are ratios of the two conjugate-paired Gauss sums, with the quadratic Gauss normalization for \(p\equiv1\pmod4\). Thus in the actual common lift average,
\[
 S=s_n(z+z^{-1})/2,\qquad
 S^2=\frac{s_n^2}{2}+\frac{s_n^2}{4}(z^2+z^{-2}).
\]
The opposite-lift terms give this actual scalar unit, of mass \(U_n=s_n^2/2=2p/n\), as in the pure seed Laurent expansion in [Round 135](cold-remainder-135.md). The remaining same-lift products are retained in the representation. The difference at the exceptional trivial character costs \(O(n^{-1/2}\varepsilon^2)\) after the first \(K\), using the marked-column price.

In \(r_1^{\rm b}=-(3/2)(4t)^{-3/2}R^2\int_0^1(1-s)V_s^2\,ds\), the common \(S^2\) term has coefficient independent of \(s\). Its scalar part is therefore \(-\frac{3U_n}{2(4t)}r_0^{\rm b}\), where \(r_0^{\rm b}=R^2/(2\sqrt{4t})\). The words combine with \(r_0^{\rm b}\) at
\[
 \Xi(t)=1-\frac{3U_n}{8t}.
\]
This is the same actual \(R^2\) at both orders. For any fixed or growing outer exponent \(j\) the term \(B^jK\), with \(B=KD_{602}\), acts on this combined scalar times the single true bulk source. No \(K\) is moved through a multiplier. Physical mark and bad-coordinate corrections are paid separately as before, so the scalar relation is applied to the bulk representation only.

Uniformly on the original square, \(|\Xi(t)|<0.906\) eventually. To check this, take \(t_c=2031/128\), use \(4\le U_n\le5\) eventually and \(|t-t_c|\le2^{-16}\). The bound
\[
 1-\frac{3\cdot4}{8t_c}
    +\frac{3\cdot5}{8}\frac{2^{-16}}{(t_c-2^{-16})t_c}<0.906
\]
is rational, and the real center factor is positive.

## Price on the reassembled source

The paired first-moment comparison for \(r_1\) in Round 165 bounds the generic rank of the full word by \(\varepsilon^2(4M^2-8)\). The scalar-unit branch of \(S^2\) contributes \(2U_n\varepsilon^2\) to that comparison, since the two \(R\) factors retain their separate first moment bounds. This is an explicit branch of the comparison: the opposite-lift half contributes no seed first moment and retains the two \(R\) moment charges. The same-lift half contributes two seed moments and both \(R\) moment charges; the terms with one or two nonseed factors use their unpaired bounds. After removing the unit branch the rank budget thus becomes
\(\varepsilon^2(4M^2-2s_n^2)\le\varepsilon^2(4M^2-16)\), before the scalar Taylor coefficient. Equivalently, for an actual total non-increment mass \(d_s\le M\), the comparison for the nonunit part is \(4\varepsilon^2(d_s^2-s_n^2)+2\varepsilon^2s_n^2\); substitute \(M\) and \(s_n^2\ge8\). This operation does not subtract an unsigned scalar after a norm bound.

The new bound on the first two reassembled Taylor terms after \(K\) is therefore
\[
 \frac{2(0.906)\varepsilon^2}{\sqrt N}
 +\frac{(3/2)\varepsilon^2(4M^2-16)}{N^{3/2}}
 +O(n^{-1/2})<0.0000551
\]
eventually. The genuine first outer multiplication by \(B\) gives price below \(0.0000588\), by the verified \(1.066\) rate. For the full Taylor source, retaining all \(l\ge2\) charges from Round 165 gives eventual price below \(0.0000971\). Specifically its leading bound is
\[
 \frac{\varepsilon^2}{\sqrt N}
 \left[(2+x-12/N)(1-x)^{-5/2}-2(1-0.906)-12/N\right]
\]
plus \(O(n^{-1/2})\) repairs. All comparisons follow by rational squaring. The small signed cancellation persists on the shared component at any outer power; the bound on the full translated inverse and the nonlinear continuation still require a summable transported estimate.
