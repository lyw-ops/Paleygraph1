# A prime restriction on concentrated repair spectra

Let \(p\equiv1\bmod4\) be prime, \(Q=(\mathbb F_p^\times)^2\), \(G=\widehat Q\), \(n=(p-1)/2\), and \(m_0=n/\sqrt p\). Write \(k(j)=m_0K_{j0}\), so \(|k(j)|\le1\), and let \(\mathcal T\) be additive Paley convolution on \(\mathbb F_p\). The compression to \(Q\) is diagonal in the multiplicative Fourier basis with multiplier \(k(j)\). Use counting \(\ell^2\) norms on \(Q\) and \(\mathbb F_p\).

Fix a bound on the number of cosets and constants \(0<c_1<c_2\). Take \(B\subset Q\) to be a union of at most that many multiplicative cosets \(a_iH_i\) of possibly different subgroups, with \(c_1\sqrt p\le |H_i|\le c_2\sqrt p\). The choices can depend on \(p\). Put \(Y=(1-B)\setminus\{0\}\).

## A rich-ratio bound for mixed cosets

For \(u\ne0,1\), the number of representations of a ratio \(u\) of two points of \(Y\) is \(|Y\cap uY|\). For choices \(x\in aH,\ y\in bJ\) from two of the original cosets, the equation \(1-x=u(1-y)\) leads to \(\alpha=a/(1-u)\), \(\beta=-bu/(1-u)\), and \(v+w=1\) with \(v\in D=\alpha H,\ w\in E=\beta J\). Let \(N(D,E)\) count the last solutions. It bounds the contribution from this pair at \(u\), allowing the possibly removed zero of \(Y\).

The number of \(u\) assigned to \((D,E)\) is exactly \(N(D/a,E/b)\). In fact \((\alpha/a,\beta/b)\) ranges bijectively over all nonzero pairs summing to one. For the rich cells \(\Theta_t=\{(D,E):N(D,E)\ge t\}\), the identity \(\sum_{D,E}N(D,E)=p-2\) gives \(|\Theta_t|\le(p-2)/t\). For \(t\) above a fixed constant this is within both cutoffs of Mit'kin's estimate, since \(|H||J|\asymp p\). The estimate gives \(t|\Theta_t|\ll (|H||J|\,|\Theta_t|^2)^{1/3}\) and hence \(|\Theta_t|\ll p/t^3\). Apply it again to the distinct pairs \((D/a,E/b)\) of scaled cells. The number of relevant \(u\) is then \(\ll p/t^2\). Summing over the fixed number of cross pairs and increasing the constant for small \(t\) proves
\[
 |\{u\ne0,1:|Y\cap uY|\ge t\}|\ll p/t^2,\qquad t\ge1.
\]
The same bound holds for any nonzero scalar multiple of \(Y\). This extends the shifted-subgroup estimate of [Round 20](parallel-rectangle-20.md#2-shifted-subgroup-correlations-and-an-additive-gap). [Mit'kin estimate in Macourt, Shkredov and Shparlinski, Lemma 2.1](https://arxiv.org/pdf/1701.06192)

By summing this tail, the small correlations have squared sum \(O(p\log(2R))\) up to threshold \(R\), and the large ones have sum \(O(p/R)\). Therefore the smooth cap inequality (5) of Round 20 applies to any complex \(g\) supported in \(Q\cap vY\), \(v\ne0\), with \(|g|\le1\). Its proof uses these two sums and the same cap coefficients. If \(\|g\|_2^2\gg\sqrt p/L\), put \(R=M=\lceil M_* L^4\log^2(2L)\rceil\). The cap mass for sign \(+1\), divided by \(\|g\|_2^2\), is at most a constant times
\[
 M^{-1/2}+p^{-1/4}
   +L(M^{-1/4}+p^{-1/8})\sqrt{\log(2M)}+L/\sqrt M .
\]
For \(1\le L\le p^{1/12}\), first choose a sufficiently large fixed \(M_*\) and then take \(p\) large. The displayed bound is at most \(1/2\) uniformly. Indeed the term involving \(M^{-1/4}\) is \(O(M_*^{-1/4}\sqrt{1+\log M_*})\), and \(L p^{-1/8}\sqrt{\log(2M)}=o(1)\). The cap-to-Rayleigh comparison from Round 20 yields \(\langle g,(I-\mathcal T)g\rangle\ge M^{-1}\|g\|_2^2\).

## Application to the actual retargeted deficits

Let \(b\ge0\), \(b_0=0\), \(r=\mathbb E b>0\), and \(\|L_\sigma b\|_{2,n}\le C r\) with fixed \(C\). In particular this includes the same actual repair deficits throughout the [Round 151 block](ordinary-retargeted-motion-151.md#a-block-with-the-same-masked-endpoint-lower-bound). Let \(\rho=-\sigma\), \(m_{\rm eff}=nr^2/\mathbb E b^2\) and \(L=\max(1,m_{\rm eff}/m_0)\), assumed at most \(p^{1/12}\). Write \(f(x)=(\sum_j b_j j(x))/(\sum_j b_j)\) on \(Q\), zero elsewhere. Then \(|f|\le1\) and \(\|f\|_2^2=n/m_{\rm eff}\ge\sqrt p/L\).

For every anchor \(a\in G\), write
\[
 t_B=\frac{\|1_{Q\setminus B}f\|_2^2}{\|f\|_2^2},
 \qquad
 d_a=\frac{\sum_j b_j^2(1-\rho k(j-a))}{\sum_j b_j^2}.
\]
Uniformly for all such \(p,B,a\) and \(b\),
\[
 \boxed{\displaystyle t_B+d_a\ \gg\
             \frac{1}{L^4\log^2(2L)}} .
\]
The implicit constant depends on \(C\) and the fixed coset bounds.

To prove this, use \(\ell=P_\sigma e_0\) and \(P_\sigma b=L_\sigma b+(\ell^{\mathsf T}b)\ell/\ell_0\). Since \(b_0=0\), the bulk entry bound gives \(|\ell^{\mathsf T}b|=O(\sqrt n\,r)\), and \(\|P_\sigma b\|_{2,n}=O(r)\). With \(J\) the projection onto constants, \(I-\rho K=2P_\sigma+J\). The ratio of the corresponding quadratic form to \(\|b\|_{2,n}^2\) is \(O(L/\sqrt p)\). Under multiplicative Fourier transform this is the relative integral of \((1-\rho\chi(1-x))|f(x)|^2\) on \(Q\), by diagonalization of \(K\).

Modulate \(f\) by the character \(\bar a\), so its additive Rayleigh defect for \(I-\rho\mathcal T\) is \(d_a\). Truncate to \(B\). Since the positive semidefinite form has operator norm at most two, its new defect with original norm denominator is \(O(d_a+t_B)\). Modulation preserves the sign concentration just proved. Affinely reflect the truncated function by \(x\mapsto1-vx\) with \(\chi(v)=\rho\), as in Round 20. This changes the additive form to \(I-\mathcal T\). Restrict the reflected function to \(Q\). The discarded squared mass is \(O(L/\sqrt p)\) relative to \(\|f\|_2^2\), including the possible image at zero of the value at one, whose square is at most one. Thus the resulting \(g\), supported in \(Q\cap v^{-1}Y\), has Rayleigh numerator \(O((d_a+t_B+L/\sqrt p)\|f\|_2^2)\).

For \(d_a+t_B\) below a sufficiently small fixed constant this construction keeps \(\|g\|_2^2\ge\|f\|_2^2/2\) for large \(p\). The cap bound then forces \(d_a+t_B+O(L/\sqrt p)\gg1/M\). Since \(ML/\sqrt p=o(1)\) uniformly in the indicated range, the last error is absorbable. The case of a larger constant \(d_a+t_B\) gives the stated bound directly.

In the nearly critical case \(m_{\rm eff}/m_0\to1\) and \(\|L_\sigma b\|_{2,n}/r\to0\), the flattening part of the [Round 20 anchored estimate](anchored-repair-20.md#a-uniform-single-step-gap-for-concentrated-prime-defects) gives a nearly uniform high set \(S\) of size \((1+o(1))m_0\) and a vanishing signed within-set pair deficit. Some anchor in \(S\) has row deficit \(o(1)\). The normalized weights \(b_j^2/\sum_i b_i^2\) approach the uniform weights on \(S\) in \(\ell^1\), so this anchor has \(d_a=o(1)\). Therefore the relative Fourier mass outside every such \(B\) has a uniformly positive lower bound in this critical case. No additional high-layer additive-energy assumption is used. Away from criticality the inequality retains both alternatives. The actual flow still needs a reason its endpoint charge implies concentration or small anchor deficit.
