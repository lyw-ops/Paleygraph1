# Multiplicative autocorrelations forced by a slow prime repair

Use the definitions of \(Q,K,k,m_0,\mathcal T\) from [Round 151](ordinary-prime-coset-spread-151.md). Norms on \(Q\) and \(\mathbb F_p\) in the cap argument are counting norms. For complex \(g\) supported on \(Q\) with \(|g|\le1\), put \(N=\|g\|_2^2\) and
\[
 A_g(u)=\left|\sum_{x\in Q}g(ux)\overline{g(x)}\right|,\qquad
 D_g=\sup_{s\ge1}\frac{s^2}{p}\left|\{u\in Q\setminus\{1\}:A_g(u)\ge s\}\right|.
\]
This uses the absolute value of the signed correlation, after summation. Define \(\eta_g=\langle g,(I-\mathcal T)g\rangle/N\) when \(N>0\). Suppose \(L\ge1\) and \(N\ge c_0\sqrt p/L\) with fixed \(c_0>0\). Then for all sufficiently large ordinary primes
\[
 L^2(1+D_g)\log(2L(1+D_g))
       \gg_{c_0}\min(\eta_g^{-1/2},p^{1/4}),
\]
interpreting the first argument as infinite at zero.

## The signed cap calculation

For the smooth Jacobi cap \(P_M(z)=((1+z)/2)^M\), use the identity and coefficient bounds of [Round 20](parallel-rectangle-20.md#1-a-smooth-jacobi-cap). In the Fourier expansion of its pairing with \(|\widehat g|^2\), the identity correlation is \(N\). For nonidentity \(u\), sum the stated tail defining \(D_g\). The squared correlations at most \(R\ge1\) have sum \(O(p(1+D_g\log(2R)))\), and the correlations above \(R\) have sum \(O(pD_g/R)\). The first part follows by integrating the tail against \(2s\), including the trivial \(p\) bound below one. The second part includes the threshold contribution \(R|\{u:A_g(u)>R\}|\).

Apply Cauchy–Schwarz to the small correlations with the \(\ell^2\) norm of the cap coefficients. Use the pointwise off-identity coefficient bound on the large correlations. After division by \(N\), with \(R=M\), the relative cap mass is at most a constant times
\[
 M^{-1/2}+p^{-1/4}
  +L(M^{-1/4}+p^{-1/8})\sqrt{(1+D_g)\log(2M)}
  +\frac{L D_g}{\sqrt M}.
\]
Here the term \(4/(p-1)\) in the off-identity bound is absorbed by the \(\sqrt{M/p}\) term. Put \(A=1+D_g\), \(X=L^2 A\log(2LA)\), and \(M=\lceil M_*X^2\rceil\). Then \(\log(2M)\ll(1+\log M_*)\log(2LA)\). The terms involving \(M^{-1/4}\) and \(M^{-1/2}\) can first be made small with fixed \(M_*\). The \(p^{-1/8}\) term is \(O_{M_*}(p^{-1/8}\sqrt X)\). Unless \(X\gg p^{1/4}\), we can choose its threshold small enough that the whole relative cap mass is below \(1/2\). In that case \(1-P_M(z)\le M(1-z)/2\) and the compression identity give \(\eta_g\ge1/M\). This gives the claimed minimum bound.

## Actual deficits and unrestricted anchors

Let \(b\ge0\), \(b_0=0\), \(r=\mathbb E b>0\), \(\|L_\sigma b\|_{2,n}\le C r\) with fixed \(C\), and \(L=\max(1,m_{\rm eff}/m_0)\), as for the [actual retargeted block](ordinary-retargeted-motion-151.md). Write \(f(x)=(\sum_j b_jj(x))/(\sum_j b_j)\), zero off \(Q\), and \(\rho=-\sigma\). Fix an anchor \(a\in G\) with the squared-weight phase defect \(d_a\) of Round 151. Modulate by \(\overline{a(x)}\), affinely reflect by \(x\mapsto1-vx\) with \(\chi(v)=\rho\), and restrict the result to \(Q\). Call this actual reflected function \(g_a\).

The exact identity \(I-\rho K=2P_\sigma+J\) and the pin entry bound give
\[
 \frac{\langle b,(I-\rho K)b\rangle_{2,n}}{\|b\|_{2,n}^2}
  =\frac{2\|P_\sigma b\|_{2,n}^2+r^2}{\|b\|_{2,n}^2}
  =O_C(L/\sqrt p).
\]
Under multiplicative Fourier transform this is the squared-mass defect for the sign \(\chi(1-x)=\rho\). Consequently reflection discards a fraction \(O_C(L/\sqrt p)\) when restricting back to \(Q\), as in Round 151. Modulation makes the additive Rayleigh defect of \(f\) equal to \(d_a\), and reflection converts the sign-\(\rho\) form to the positive sign. The triangle inequality for the square root of this form proves \(\eta_{g_a}=O_C(d_a+L/\sqrt p)\) and \(N\gg\sqrt p/L\) when \(L=o(\sqrt p)\).

In particular the same actual near-critical branch, \(m_{\rm eff}/m_0\to1\) and \(\|L_\sigma b\|_{2,n}/r\to0\), admits anchors with \(d_a=o(1)\) by the Round 20 flattening argument. The new estimate forces \(D_{g_a}\to\infty\). This restriction concerns the actual affine-reflected, weighted inverse Fourier function and needs no assumption about its support or additive energy. An ordinary-prime upper on these signed correlations tied to the actual orbit is still missing.

## Uniform and deficit-weighted anchor averages

Fix the same \(b,v\), and let \(F_0(x)=f(1-vx)\) for \(x\in Q\). Thus \(g_a(x)=F_0(x)\overline{a(1-vx)}\) when \(1-vx\in Q\), with value zero otherwise. Write \(N=\|F_0\|_2^2\) and
\[
 C_a(u)=\sum_{x\in Q}g_a(ux)\overline{g_a(x)}
       =\sum_x F_0(ux)\overline{F_0(x)}\,\overline{a(r_u(x))},
 \qquad
 r_u(x)=\frac{1-vux}{1-vx}.
\]
Use only contributing terms, so \(r_u(x)\in Q\). For each \(u\in Q\setminus\{1\}\) the map \(x\mapsto r_u(x)\) is injective since its determinant is nonzero. Character orthogonality in the anchor \(a\) gives the exact identity
\[
 \mathbb E_{a\in G}\sum_{u\in Q\setminus\{1\}}|C_a(u)|^2
   =\sum_{u\ne1,x}|F_0(ux)F_0(x)|^2
   =N^2-\sum_x|F_0(x)|^4.
\]
Thus \(\mathbb E_{a\in G}D_{g_a}\le N^2/p=O(1)\) in the critical branch. This is a uniform-anchor estimate.

Put \(\nu_a=b_a/\sum_j b_j\) on the anchors. In the same expansion, averaging \(|C_a(u)|^2\) with these weights replaces the orthogonality indicator on \(x,y\) by \(f(r_u(y)/r_u(x))\). Explicitly the off-diagonal term is the sum over \(u\ne1,x\ne y\) of
\[
 F_0(ux)\overline{F_0(x)F_0(uy)}\,F_0(y)\,
                         f(r_u(y)/r_u(x)).
\]
The diagonal term still sums to \(N^2-\sum_x|F_0(x)|^4\). This formula gives the signed arithmetic quantity in the true anchor distribution.

For critical actual \(b\), the Round 20 flattening makes \(\nu\) and the squared weights \(b_j^2/\sum_i b_i^2\) close in \(\ell^1\) to the uniform distribution on the same near-flat set \(S\). For \(\nu\), use the near equality of the total mass to the mass on \(S\), which follows from the critical effective size and Cauchy–Schwarz on \(S\). The within-\(S\) phase deficit tends to zero, so \(\mathbb E_\nu d_a=o(1)\). The cap bound then gives \(D_{g_a}\to\infty\) in \(\nu\)-probability. Since \(pD_{g_a}\le\sum_{u\ne1}|C_a(u)|^2\), it follows that
\[
 \frac1p\mathbb E_{\nu}\sum_{u\ne1}|C_a(u)|^2\longrightarrow\infty.
\]
An \(O(p)\) upper bound on this deficit-weighted fourth moment, along ordinary primes for the actual critical repair, would exclude the critical branch. The uniform-anchor identity shows why it is the off-diagonal contribution in the true weight, rather than the unweighted diagonal, that must be controlled.

## Allowing a growing number of cosets

Let \(B\) be a union of at most \(h=h(p)\ge1\) cosets of multiplicative subgroups of sizes comparable to \(\sqrt p\), with fixed comparison constants. Let \(t_B\) be the relative squared mass of \(f\) outside \(B\). The mixed-coset proof of Round 151 gives weak \(\ell^2\) bound \(O(\sqrt p)\) for the ratio count from each ordered coset pair, with the identity ratio omitted. For a nonnegative array \(u\), the functional \(\sup_{E\ne\varnothing}|E|^{-1/2}\sum_{i\in E}u_i\) is subadditive and lies between its weak \(\ell^2\) bound and twice that bound. The upper comparison follows by summing the ordered majorant \(u_i^\downarrow\le \|u\|_{2,\infty}/\sqrt i\). Hence the weak bound for the union is \(O(h^2\sqrt p)\).

Truncate the modulated \(f\) to \(B\) before reflection. The resulting \(g\) has \(D_g=O(h^4)\), since its absolute correlation is at most the ratio count on its shifted support. Its normalized defect is \(O_C(t_B+d_a+L/\sqrt p)\). If \(t_B+d_a\) is at most a sufficiently small fixed constant, its norm still satisfies \(N\gg\sqrt p/L\). The cap estimate then gives
\[
 t_B+d_a\gg \frac1{h^8 L^4\log^2(2hL)}
 \qquad\text{provided}\qquad h^8 L^5\log^2(2hL)=o(\sqrt p).
\]
Indeed \(X=O(h^4L^2\log(2hL))=o(p^{1/4})\), forcing the \(\eta_g^{-1/2}\) branch in the bound on \(X\). The small-error condition absorbs \(L/\sqrt p\). Larger values of \(t_B+d_a\) give the conclusion directly. This includes \(L\le p^\gamma\) for every fixed \(\gamma<1/10\) when \(h\) is bounded.
