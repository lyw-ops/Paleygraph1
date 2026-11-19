# Sparse even masks can saturate the Jacobi cross compression

At every sufficiently large eligible prime there are two disjoint inversion-symmetric bulk masks of size \(O(n/\sqrt{\log p})\) whose Jacobi cross compression has a growing family of singular values tending to one. At floors \(t_p\to2031/128\), comparison factors on these masks satisfy the exact products, both physical factor means, and the full unforced angular identity, with zero marked phase and bounded normalized second norms. These identities leave enough freedom for the comparison Jacobian to have small singular values. The genuine complementary sector equations are a separate constraint.

## An alternating positional interval

Let \(n=(p-1)/2\), \(Q=\langle g\rangle\subset\mathbb F_p^\times\) be the group of squares and label characters of \(Q\) by \(i\in\mathbb Z/n\). The actual Jacobi operator \(K\) is the Fourier multiplier \(d(g^k)=\chi(1-g^k)\) at positional frequency \(k\). Here \(d(1)=0\), \(d(g^{-k})=d(g^k)\), and \(n\) is even. Let \(T\) translate physical rows by \(n/2\); its multiplier is \((-1)^k\).

Put \(L=\lfloor(\log_2 p)/3\rfloor\). For any prescribed signs \(\sigma_0,\dots,\sigma_{L-1}\), the number of \(x\in Q\) with \(\chi(1-g^\ell x)=\sigma_\ell\) for all \(\ell\) is
\[
                 n2^{-L}+O(L\sqrt p).
\]
Expand the product of \((1+\sigma_\ell\chi(1-g^\ell x))/2\), and permit an \(O(L)\) error at zeros of the individual factors. For each nonempty subset of factors, write the sum over \(Q\) as the average of the untwisted sum over \(\mathbb F_p^\times\) and the sum twisted by \(\chi(x)\). The polynomials have distinct simple roots, since \(L<n\) and the extra root at zero is distinct. The quadratic Weil bound gives \(O(L\sqrt p)\) for each complete sum and hence for their average with coefficients bounded by \(2^{-L}\). The main term has order \(p^{2/3}\) and dominates. [Weil's multiplicative character bound](https://pmc.ncbi.nlm.nih.gov/articles/PMC1079093/)

Choose \(\sigma_\ell=(-1)^\ell\), and write \(x=g^a\). There are only \(O(L)\) positions \(a\) for which the block \(B=[a,a+L-1]\) in \(\mathbb Z/n\) meets \(-B\), since such an intersection requires \(2a=-(\ell+\ell')\) modulo \(n\). Exclude them. On \(B\cup(-B)\) the actual multiplier \(K\) equals \(\varepsilon T\) with \(\varepsilon=(-1)^a\). This uses inversion invariance of \(d\), and the even order \(n\) makes \((-1)^k\) well defined.

## Disjoint bulk masks and many nearly isometric directions

Let \(m=\lceil n/\sqrt L\rceil\), and let \(S_+\) consist of the indices at cyclic distance between one and \(m\) from \(0\). Put \(S_-=S_++n/2\). Eventually these sets are disjoint, each has size \(2m\), and both are invariant under inversion. Both miss the mark. Use counting Euclidean norms in this section.

Split \(B\) into \(J=\lfloor L^{1/8}\rfloor\) disjoint successive blocks \(B_j\) of length \(b=\lfloor L/J\rfloor\), discarding unused positions. For each block take the normalized even packet
\[
 U_j(i)=(2nb)^{-1/2}\sum_{k\in B_j\cup(-B_j)}e^{2\pi i k i/n}.
\]
These real rows are orthonormal by their disjoint supports in positional Fourier coordinates. For \(1\le |i|\le n/2\), the geometric sum over either block has modulus at most \(n/(2|i|)\), using \(\sin(\pi |i|/n)\ge2|i|/n\). Summing the squared tail outside radius \(m\) and allowing for the mark gives
\[
             \|1_{S_+^c}U_j\|_2^2\le n/(bm)+2b/n .
\]
On their \(J\)-dimensional span \(\mathcal E\), Cauchy–Schwarz therefore gives
\[
 \|1_{S_+^c}U\|_2^2\le \eta_p\|U\|_2^2,\qquad
 \eta_p=J(n/(bm)+2b/n)=O(L^{-1/4}+L/n).
\]
Let \(u=1_{S_+}U\) and \(v=Tu\), so \(v\) is supported on \(S_-\) and the truncation is injective. Because \(KU=\varepsilon TU\), \(\|K\|\le1\) and \(T\) commutes with \(K\),
\[
    \|Ku-\varepsilon v\|_2=\|Kv-\varepsilon u\|_2
                    \le 2\sqrt{\eta_p}\|U\|_2.                         \tag{1}
\]
For a sharper Rayleigh estimate, expand \(\varepsilon\langle Tu,Ku\rangle\) using \(u=U-h\). Its first term is \(\|U\|_2^2\), each linear term is \(-\|h\|_2^2\) by \(KU=\varepsilon TU\), and the quadratic term has modulus at most \(\|h\|_2^2\). Since \(\|u\|_2^2=\|U\|_2^2-\|h\|_2^2\), this yields
\[
  \|1_{S_-}K u\|_2\ \ge\
       \left(1-\frac{2\eta_p}{1-\eta_p}\right)\|u\|_2 .
\]
Thus the even cross compression has at least \(J\) singular values above this bound by the singular-value min–max principle. Requiring \(\sum_i u_i=0\) costs at most one dimension and also gives \(\sum_i v_i=0\).

## Exact angular budget with an almost singular comparison Jacobian

Fix \(a_*=2031/128\), let \(t=a_*+iy\), and put \(c_n=(n-1)/n\). Assign phases \(\pi/4,-\pi/4\) on \(S_+,S_-\). Select two further disjoint even bulk masks \(C_+,C_-\), disjoint from both \(S\)'s, with equal cardinality and combined counting fraction \(M_n\to M=1/2\). Give them phases \(s y,-s y\), respectively, for a constant \(s>0\) specified below. All other phases are zero. The masks can be unions of two-element inversion orbits since \(m=o(n)\). Set \(t_0=n\), \(t_i=t\) on the bulk and \(A_i=\sqrt{t_i}e^{z_i}, B_i=\sqrt{t_i}e^{-z_i}\), with \(z_i=\rho_i+i\phi_i\) and real amplitudes \(\rho_i\) to be chosen. The products \(A_iB_i=t_i\) are exact. The equal-sized phase pairs cancel all imaginary terms in \(\sum_i|t_i|e^{-2i\phi_i}\).

To obtain exactly the [unforced angular identity](astra-compression-85.md#the-weighted-angular-budget-at-the-genuine-endpoint), choose \(y=y_p>0\) so that
\[
 \frac{1+c_n|t|-|1+c_nt|}{2|t|}-M_n\sin^2(sy)=\frac{2m}{n}.
\]
The first term is, by the difference of squares,
\[
 \frac{c_ny^2}
 {|t|(|t|+a_*)(1+c_n|t|+|1+c_nt|)} .
\]
In the limit its quadratic coefficient at zero is \(C=1/[4a_*^2(1+a_*)]\). Set \(s^2=(99/100)C/M\). The full left side is therefore between fixed positive multiples of \(y^2\) on a sufficiently small interval, uniformly for large \(p\). By continuity \(y_p\asymp\sqrt{m/n}\) exists and tends to zero. In particular \(t_p=a_*+iy_p\) eventually lies in the fixed cold square. At that point \(\sum_i|t_i|e^{-2i\phi_i}=n|1+c_nt_p|\), with phase diameter \(\pi/2\) and \(\phi_0=0\).

It is possible to match both physical means without changing either extreme mask or its amplitudes, which we keep zero. Set \(W=1+c_nt_p\), and require the bulk contribution, after removing the common marked contribution \(n^{-1/2}\), to equal \(Z=(\sqrt W-n^{-1/2})/\sqrt{t_p}\). To do so retain \(\rho_0=0\), and use pairs of sets with opposite \(z\), so that \(\sum\sinh z_i\sqrt{t_i}=0\) identically and the \(A\) and \(B\) means are the same. At zero amplitudes the common real bulk coefficient is
\[
      Z_0=c_n+\frac{4m}{n}(\cos(\pi/4)-1)+M_n(\cos(sy_p)-1).
\]
Choose the amplitudes on \(C_+,C_-\) to be \(x,-x\), respectively. Their change to the common bulk coefficient is \(M_n[\cosh(x+isy_p)-\cos(sy_p)]\), so choose
\[
          \sinh x=\frac{\Im Z}{M_n\sin(sy_p)} .
\]
It matches the imaginary part exactly. Since \(Z=\sqrt{c_n+1/t_p}-1/\sqrt{nt_p}\), its imaginary part divided by \(y_p\) tends to \(-1/[2a_*^2\sqrt{1+1/a_*}]\). It follows that \(|\sinh x|^2\to 1/[(99/100)a_*M]\). The real increment tends to \(M(\sqrt{1+1/[(99/100)a_*M]}-1)\), while \(\Re Z-Z_0\to u_*=\sqrt{1+1/a_*}-1\). The increment is strictly smaller than \(u_*\), since \(M=1/2\) and \(99/100>(2+u_*)/(2+2u_*)\), using \(a_*<16\) and \(u_*>1/40\). Thus two equal-cardinality even sets of fixed positive density among the remaining zero-phase sites can be assigned amplitudes \(b_0,-b_0\), increasing the real part by the designated multiple of \(\cosh b_0-1\). Leave all other amplitudes at zero. Both \(x,b_0\) stay bounded. Consequently \(EA=EB=\sqrt W\) as in the physical mean sheet, with \(E|A|^2,E|B|^2=O(1)\) from the bounded bulk factors and the known mark. Both the ordinary and Hermitian scalar pairings of the centered factors therefore vanish.

On \(S_\pm\) the formal Jacobian \(I-KD\) at this comparison profile has \(D=\operatorname{diag}(\tanh z_i)\) equal to \(\pm i\), regardless of its other entries. For \(u,v\) from the preceding section, set \(h=u+i\varepsilon v\). Its norm is \(\sqrt{2}\|u\|_2\), since its supports are disjoint. By (1),
\[
 \|(I-KD)h\|_2=\|u+i\varepsilon v-iKu-\varepsilon Kv\|_2
       \le4\sqrt{\eta_p}\|U\|_2 .
\]
This produces at least \(J-1\) even mean-zero directions with small singular value while retaining the products, means, pairings and all contact phases. Imposing any fixed number of additional linear moment equations on \(h\) still leaves a growing space of such directions. The construction does not impose that the actual two factors lie in their complementary sectors. It does not provide a singularity or phase contact of a physical branch.

1. Estimate the signed compression on the phase masks selected by a genuine row. In addition to the phase budget, use the actual sector equations to exclude resonance with the nearly translated modes above.
2. For phase profiles beyond first contact, use the fully weighted Schur return or the genuine factor constraints on the active negative-cosine set. A uniform estimate based only on mask density, evenness and finitely many moments cannot use the same near-contact singular-value argument.
