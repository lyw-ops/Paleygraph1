# The mark localizes the critical obstruction to one additive class

Use the genuine retargeted short block of [Round 151](ordinary-retargeted-motion-151.md) under the fixed hypothetical ordinary gap. Write \(\nu=b/(nr)\), \(r=\mathbb E b\), \(\rho=-\sigma\), \(m_0=n/\sqrt p\), and \(M_a=\sum_{u\in Q\setminus\{1\}}|C_a(u)|^2\) as in [Round 156](ordinary-sign-selective-completion-156.md). Work on the hypothetical critical-size branch \(m_{\rm eff}/m_0\to1\) and keep the actual \(b_0=0\) and relative pin bound.

## Marked phase and a narrower positive moment

The phase \(c_\sigma(a)\) of [Round 149](ordinary-averaged-repair-dual-149.md#constraints-on-the-same-selected-prime-deficit) is \(\rho k(a)\). [Round 150](ordinary-prime-repair-source-150.md#retargeting-the-mark-before-relaxed-repair) gives its current weighted mean \(q/\sqrt p+O(\delta)\) at the selected step. The same holds uniformly for the following short block: the normalized change in \(b\) in Round 151 gives total variation \(O(\delta)\) in \(\nu\), and \(|k|\le1\). In particular \(\mathbb E_\nu(\rho k)\ge (1+\eta)/\sqrt 2-o(1)\) by the fixed gap. Thus
\[
 I_{\rm arc}=\{a:\rho k(a)\ge 1/2\}
\]
has \(\nu\)-mass bounded below, by comparing that mean to \(1/2+\nu(I_{\rm arc})/2\).

The additive frequency identity of Round 156 on the class \(\chi(\xi)=\rho\) reads
\[
 S_{\rho}^{\rm add}=\tfrac12\sum_a\nu_a(1+\rho k(a))M_a+O(p).
\]
All the weights of this positive moment are nonnegative. In particular the part supported on \(I_{\rm arc}\) is no greater than twice this moment up to \(O(p)\). An independent \(O(p)\) upper on \(\sum_{a\in I_{\rm arc}}\nu_a M_a\) suffices to exclude the hypothetical critical branch, as does such an upper on \(S_{\rho}^{\rm add}\). The two statements are sufficient by the quantitative lower below. If \(q/\sqrt p\le1-\varepsilon\) along a sequence for some fixed \(\varepsilon>0\), the other additive sign also has \(\omega(p)\) contribution on that hypothetical sequence: \(\mathbb E_\nu(1-\rho k)\ge\varepsilon-o(1)\), \(0\le1-\rho k\le2\), and \(M_a/p\to\infty\) in \(\nu\)-probability by [Round 152](ordinary-affine-correlations-152.md).

## Quantifying the obstruction without a flattening rate

Let
\[
 e=1-\mathbb E_{a,j\sim\nu}\rho k(j-a),\qquad E=e+p^{-1/2}.
\]
With the normalized counting norm on index space, \(I-\rho K=2P_\sigma+J\) and \(K_{ij}=(\sqrt p/n)k(i-j)\) give
\[
 e=1-\frac{m_0}{m_{\rm eff}}
     +\frac{2\|P_\sigma b\|_{2,n}^2+r^2}{\sqrt p\,r^2}
 =O\bigl(|1-m_0/m_{\rm eff}|+p^{-1/2}\bigr).
\]
The last estimate uses the pin formula from Round 153, whose rank-one correction has normalized norm \(O(r)\). The phase bound gives \(e\ge0\). The [entry cap](ordinary-affine-jacobi-factorization-153.md) and critical size imply that the squared weight law \(\mu_j=\nu_j^2/\sum_i\nu_i^2\) satisfies \(\mu_j\le C\nu_j\). The squared-weight defect \(d_a=\sum_j\mu_j(1-\rho k(j-a))\) therefore satisfies \(\mathbb E_\nu d_a\le Ce\). By Markov, increasing the fixed cutoff multiple if needed, \(d_a=O(e)\) on a subset of \(I_{\rm arc}\) with \(\nu\)-mass bounded below. If \(e=0\), use \(d_a=0\) on the supported anchors.

On this subset the reflected additive defect in Round 152 is \(O(E)\). Since \(L=\max(1,m_{\rm eff}/m_0)\) is bounded and \(E\ge p^{-1/2}\), the cap lower in that round implies
\[
 D_{g_a}\gg \frac{E^{-1/2}}{\log(2/E)}.
\]
Indeed the right side in its bound on \((1+D_{g_a})\log(2(1+D_{g_a}))\) is at least a fixed multiple of \(E^{-1/2}\). Inverting this increasing function gives the displayed inequality as \(E\to0\). Since \(M_a\ge pD_{g_a}\), it follows that
\[
 \sum_{a\in I_{\rm arc}}\nu_a M_a\gg
     \frac{pE^{-1/2}}{\log(2/E)},\qquad
 S_{\rho}^{\rm add}\gg \frac{pE^{-1/2}}{\log(2/E)} .
\]
The additive \(O(p)\) error is absorbed since \(E\to0\). This is a lower estimate on a hypothetical branch. It neither provides an upper on it nor establishes that such a sequence of primes exists.

## Exact square-field control with the pin and phase retained

Let the field order be \(P=s^2\) for odd \(s\), \(Q\) the nonzero squares, \(H=\mathbb F_s^\times\subset Q\) and \(A=H^\perp\subset\widehat Q\). Then \(|A|=(s+1)/2\). Use \(\rho=+1\), \(v=1\) and \(\nu\) uniform on \(A\setminus\{1\}\). The inverse transform \(f\) is \(1\) on \(H\), the constant \(-2/(s-1)\) on \(Q\setminus H\), and zero elsewhere. Thus \(b=n\nu\) has \(r=1,b_0=0\) and \(m_{\rm eff}=(s-1)/2\sim n/\sqrt P\). Since \(\chi(1-x)=1\) on \(H\setminus\{1\}\), the wrong-sector part of \(f\) is exactly constant. The Fourier description of the pin yields \(L_-b=0\). Also \(\sum_{x\in Q}\chi(1-x)=-1\) by the two degenerate Jacobi sums. Hence
\[
 \mathbb E_\nu k=\tfrac1s\sum_{x\in Q}\chi(1-x)f(x)
        =\tfrac1s\bigl(s-2+2\bigr)=1 .
\]
Each supported anchor consequently has \(k(a)=1\). With \(\ell_0=1/2\), the phase identity of Round 149 gives \(B=s+1\). The completed mean-one row has marked value \(B/(1+B/n)=s-1\), so its root has the same asymptotic scaling as the marked phase.

For each supported anchor \(a\), \(g_a\) is identically one on \(H\setminus\{1\}\) and has modulus at most \(2/(s-1)\) on \(Q\setminus H\). When \(u\in H\setminus\{1\}\), its correlation is \(s+O(1)\) since the product of the two indicators gives \(s-3\) and the outside-outside sum is \(O(1)\). When \(u\notin H\) there is no inner-inner term, there are at most \(2(s-1)\) one-inner terms, and the rest costs \(O(1)\). Thus \(M_a=s^3+O(s^2)\) uniformly. Choose a full-field additive character with positive quadratic Gauss sum \(s\). The additive sign identity and its \(O(P)\) error use finite-field Jacobi and Gauss bounds and apply here with the exact wrong-sector pin. Its matching additive class therefore has \(s^3+O(s^2)\), and the other class \(O(s^2)\). This control has no asserted negative-part history. It shows the quantitative pin, phase and size conditions alone cannot yield a field-general \(O(P)\) upper on the matching class.
