# The first graph shapes on Paley localization

The graph-matrix construction of Potechin and Xu repairs each off-diagonal term by adjoining the boundary edge. Its estimate uses independent random signs to retain backtracking and noncrossing pairings, then identifies concatenated shapes with the second-kind Chebyshev expansion. On actual Paley 1-localization, the fourth moment of the first matrix and the variance of the first correction both differ in their leading terms. The graph-shape matrices also commute, with a positive mixed fourth moment where the free approximation gives zero. This obstructs the random-graph analysis after direct substitution. It does not obstruct an arithmetic construction using other estimates. [Potechin–Xu, §§2.5–2.8](https://arxiv.org/html/2609.30064v1#S2.SS5)

## Fourth moment and the first correction

Let \(Q=(\mathbb F_q^\times)^2\), \(n=|Q|=(q-1)/2\), and \(q\equiv1\pmod4\). With both matrices indexed by \(Q\), set

$$S_{xy}=\chi(x-y),\qquad A=S/\sqrt n,\qquad T=(S\odot S^2)/n,$$

where \(S^2\) is matrix multiplication and \(\odot\) is entrywise multiplication. The diagonal of \(S\) vanishes. Thus \(T\) is exactly the normalized injective two-edge path with its boundary edge adjoined, the first correction appearing in the construction. Write \(\operatorname{tr}_n=n^{-1}\operatorname{Tr}\).

The eigenvalues of \(S\) are \(\lambda_j=\sum_{x\in Q}\chi(1-x)j(x)\). Away from the trivial mode, each \(\lambda_j/\sqrt q\) is the real part of a normalized quadratic Jacobi sum, and both lifts of \(j\) give the same real part. Equidistribution of the full lifts therefore gives the arcsine law on \([-\sqrt2,\sqrt2]\) for \(A\). In particular

$$\operatorname{tr}_n A^2=\frac{n-1}{n},\qquad \operatorname{tr}_n A^4\longrightarrow\frac32.$$

The variance-one semicircle fourth moment is \(2\). The bounded spectrum allows use of the fourth moment under weak convergence, and the trivial mode does not affect the limit. [Xi, Theorem 1.1](https://arxiv.org/pdf/1809.04286) · [Two-lift convention](fourier.md#joint-distribution-on-the-even-modes)

In a length-four closed walk surviving the zero diagonal, a repeated vertex means either the first equals the third or the second equals the fourth. Each such walk has sign product one. Inclusion-exclusion therefore gives the exact sum over ordered distinct labels

$$\sum_{i,j,k,l\ {\rm distinct}}S_{ij}S_{jk}S_{kl}S_{li}
=n^3\operatorname{tr}_n A^4-2n(n-1)^2+n(n-1)
=-\left(\tfrac12+o(1)\right)n^3.$$

All four signs in these distinct-label terms occur to odd edge multiplicity. The normalized unchorded four-cycle correction, with adjacent boundaries and scale \(n^{-3/2}\), has constant eigenvalue \(-(\tfrac12+o(1))\sqrt n\). This is an obstruction to a general norm estimate for the class of backbone corrections. The unchorded four-cycle is not one of the first corrections inserted from the expansion, whose nonlinear coefficients occur at even polynomial degrees.

There is a discrepancy in a term used by the expansion itself. The mean diagonal of the second-kind polynomial \(P_4(A)=A^4-3A^2+I\) tends to \(-1/2\). The injective four-edge path has zero diagonal. Their difference has operator norm at least \(1/2-o(1)\). In addition, \(S_{ij}^2=1\) off the diagonal and \((S^2)_{ii}=n-1\), so

$$\operatorname{tr}_n T^2
=\frac{\operatorname{Tr}S^4-n(n-1)^2}{n^3}
\longrightarrow\frac12.$$

The random-graph variance proxy would assign this correction variance one in the same normalization.

## Classical independence of the first two matrices

For every graph shape with one vertex at each boundary, simultaneous multiplication of both labels by \(u\in Q\) leaves the matrix invariant. The map on all injective labelings preserves \(S_{ux,uy}=S_{xy}\). Thus these matrices are circulant on \(Q\), and they commute even when some individual shapes are not symmetric. In particular,

$$\operatorname{tr}_n(ATAT)=\operatorname{tr}_n(A^2T^2).$$

Both traces tend to \(1/2\). For this calculation put \(X_j=\lambda_j/\sqrt q\), \(T_2(x)=2x^2-1\), and \(Z=K T_2(X)\) with \(K=F\operatorname{diag}(s)F^{-1}\), \(s(x)=\chi(1-x)\). The eigenvalues of \(T\) equal \(qZ_j/(2n)\), since its positional row is \(s(s*s)/n\) and \(K\mathbf1=0\). The [Legendre calculation](parallel-witness-6.md#the-four-coordinates-have-independent-limiting-support) applies on the full character group without the squaring pushforward. For a lift \(\alpha\) of \(j\),

$$Z_j=\tfrac12\bigl(m_N(\alpha)+m_{N\otimes\mathcal L_\chi}(\alpha)\bigr)-2\lambda_j/q,$$

where \(N=\mathrm{TwLeg}(1)[1]\) and \(m_N\) is its full Mellin trace. The two Legendre objects have geometric and arithmetic convolution group \(SL_2^2\). Adding the dimension-one Jacobi object leaves \(\{1\}\times SL_2^2\) in the joint geometric group, since the derived group projects onto \(SL_2^2\) and trivially to the torus. The fixed-word average argument in that note then vanishes for every tensor character nontrivial on an \(SL_2\) factor. Pure Jacobi moments follow from Xi. Thus \((X,Z)\) tends to the product law of \(\operatorname{Re}u\) and \((\operatorname{tr}g_1+\operatorname{tr}g_2)/2\), with \(u\) Haar on the unit circle and independent Haar \(g_i\in SU(2)\). Mellin dimensions bound the Legendre traces by two even at exceptional characters. [Katz, Theorem 15.2 and Lemma 2.1](https://web.math.princeton.edu/~nmk/mellin331.pdf)

For \((A,T)\) the limiting variances are \(1\) and \(1/2\). The product law gives \(\operatorname{tr}_n(A^2T^2)\to1/2\). Both matrices have trace zero, so the alternating word \(ATAT\) for a freely independent centered pair would instead have limit zero. The rectangular limiting support and the uniform Jacobi and Mellin bounds also give

$$\lim_{q\to\infty}\|a A+b T\|_{\mathrm{op}}=\sqrt2\,|a|+2|b|$$

for fixed real \(a,b\). The same fixed-word limits hold on prime-square orders. These tests do not distinguish the prime and square endpoint problems.

## A fixed number of path columns gives no leading gain

For both signs and every fixed degree \(M\ge 2\), consider the Fourier-feasible rows

$$f=\delta_1+1_{D_\sigma}\left(\frac{a+b s(-x)}{\sqrt q}+2\sum_{m=2}^M c_m g_m(x)\right),\qquad g_m=F^{-1}T_m(X),$$

where \(T_m\) is the first-kind Chebyshev polynomial and \(D_\sigma=\{x\in Q:s(x)=\sigma\}\). The best value of \((Ff)_0/\sqrt n\) tends to \(1/\sqrt2\) as \(q\to\infty\) with \(q\equiv1\pmod4\). The coefficients may depend on \(q\). This extends the [constant, opposite-point and quadratic-path restriction](parallel-witness-6.md) to arbitrary fixed-degree polynomial functions of the adjacency spectrum, with these two additional positional columns.

**Exact trace normalization.** Let \(H_m\) be the trace of the hypergeometric sheaf \(\mathcal H_m\) with \(m\) trivial upstairs parameters and \(m\) quadratic downstairs parameters. Choose the additive character over \(\mathbb F_q\) with \(G(\chi)=\sqrt q\). The full multiplicative transform of \(H_m\) at \(\beta\) is \(-[G(\beta)\overline{G(\beta\chi)}]^m\). The bracket is \(\sqrt q J(\beta,\chi)\), including at \(\beta=1,\chi\) where both Jacobi sums equal \(-1\). For the nontrivial modes of \(Q\), the average of \(q^{-m/2}J(\beta,\chi)^m\) over the two lifts is \(T_m(X_k)\). At mode zero it is \((-1/\sqrt q)^m\). Thus for \(x\in Q\),

$$g_m(x)=-q^{-m}H_m(x)+\frac{\delta_m}{n},\qquad \delta_m=T_m(-1/\sqrt q)-(-1/\sqrt q)^m.$$

Let \(N_m\) be the middle extension of \(\mathcal H_m(m)\otimes\mathcal L_{\chi(1-x)}[1]\) from \(\mathbb G_m\setminus\{1\}\), and put \(N'_m=N_m\otimes\mathcal L_{\chi(x)}\). Write \(t_N\) for a perverse trace function and \(m_N(\beta)=\sum_{x\ne0}\beta(x)t_N(x)\). Multiplying the formula for \(g_m\) by \(s\) and averaging the two full character lifts gives, for any lift \(\alpha\) of \(k\),

$$Y_m(k):=(KT_m(X))_k=\tfrac12\bigl(m_{N_m}(\alpha)+m_{N'_m}(\alpha)\bigr)-t_{N_m}(1)+\delta_m\lambda_k/n.$$

The identity-stalk term vanishes for even \(m\). For odd \(m\) it is \(O(q^{-1/2})\) by the stalk weight bound and the rank-one invariant stalk computed below. The last term is uniformly \(O_m(q^{-1/2})\). The same weight bound and the formula for \(g_m\) give \(g_m(1)=O_m(q^{-1/2})\). [Katz, *G₂ and hypergeometric sheaves*, §2](https://web.math.princeton.edu/~nmk/g2hyper62finalcorr.pdf)

**Convolution groups.** The objects \(N_m,N'_m\) are geometrically irreducible, tame at the boundaries, and pure of perverse weight zero, since \(\mathcal H_m\) has weight \(2m-1\). The inertia at \(1\) before the \(\chi(1-x)\) twist is a pseudoreflection of determinant \((-1)^m\). After twisting, the invariant stalk has rank zero for even \(m\) and rank one for odd \(m\). Thus the rank drop and compactly supported Euler characteristic of each perverse object equal \(d_m=2\lfloor m/2\rfloor\). They belong to Katz's category \(\mathcal P\), since geometrically irreducible objects with this singularity are distinct from shifted Kummer sheaves. Their only interior singularity is \(1\), ruling out any nontrivial multiplicative translate of themselves. [Katz, *G₂ and hypergeometric sheaves*, §2](https://web.math.princeton.edu/~nmk/g2hyper62finalcorr.pdf) · [Katz, *Convolution and Equidistribution*, §2](https://web.math.princeton.edu/~nmk/mellin331.pdf)

For arithmetic self-duality, work over any finite extension of the defining field. The hypergeometric trace is real, by negating all additive-sum variables, since \(\chi(-1)=1\). Replacing \(\beta\) by \(\beta^{-1}\) or by \(\beta\chi\) conjugates the Gauss product in its transform. Inverting that transform gives \(H_m(x^{-1})=\chi(x)H_m(x)\). Since \(\chi(1-x^{-1})=\chi(x)\chi(1-x)\), both twisted traces are real and invariant under inversion. On the lisse locus the ordinary sheaf in degree \(-1\) has weight \(-1\), so its linear dual followed by the Tate twist \((1)\) has the conjugate trace. Chebotarev and middle extension identify each perverse object with its Verdier dual pulled back by inversion, the convolution dual. These identities use no choice of the Gauss sign over the extensions. [Katz, *Convolution and Equidistribution*, §§1–2 and Theorem 14.1](https://web.math.princeton.edu/~nmk/mellin331.pdf)

The self-duality is symplectic. To compute its sign, take an extension of size \(u\) of the defining field, and in its quadratic extension let \(B\) be the norm-one group. Put \(\xi(x)=x^{(u+1)/2}\in\{\pm1\}\) on \(B\). For \(x\in B\setminus\{1\}\) the quadratic characters of the larger field satisfy \(\chi(1-x)=-\xi(x)\) and \(\chi(x)=1\). Every character \(\beta\) extending \(\xi\) satisfies \(\beta^u=\beta\chi\), by comparing exponents in the cyclic group of order \(u^2-1\). These two characters are nontrivial. The additive character is pulled back by trace, so Frobenius gives \(G(\beta)=G(\beta\chi)\). The transform of \(H_m\) is therefore \(-u^{2m}\) at all such \(\beta\). Averaging over them gives \(\sum_{x\in B}\xi(x)H_m(x)=-u^{2m}\) by orthogonality. The perverse trace sum of \(N_m\) over \(B\) is consequently \(-1+O_m(u^{-1})\), with the error from the two normalized stalk values used at \(1\). The same holds for \(N'_m\) since \(\chi(x)=1\) on \(B\). These sums tend to the Frobenius–Schur sign by Katz's norm-one formula. [Katz, *Convolution and Equidistribution*, Theorem 9.1 and start of Chapter 10](https://web.math.princeton.edu/~nmk/mellin331.pdf)

The local boundary monodromies of \(\mathcal H_m\) are \(\operatorname{Unip}(m)\) at zero and \(\chi\otimes\operatorname{Unip}(m)\) at infinity. The \(\chi(1-x)\) twist cancels the latter character, so for \(N_m\) both boundaries have the same single unipotent Jordan block. Theorem 18.1 gives arithmetic and geometric group \(Sp(d_m)\). A quadratic Kummer twist is a convolution tensor equivalence, so \(N'_m\) has the same two groups. For any fixed \(d_m\), different values of \(m\) have different generic ranks, and the two twists at fixed \(m\) have different inertia eigenvalues at zero. Translation by \(-1\) moves the interior singularity. Theorem 13.1 gives the full product within each fixed dimension. Across dimensions the simple Lie algebras of the symplectic factors are pairwise nonisomorphic, so the subdirect product has full Lie algebra by Goursat's lemma and is the entire product. The arithmetic group is contained in the same product. The finite pushforward \([2]_*\) used on even modes preserves the product by Theorem 8.1, since its geometric group is connected and the arithmetic group before pushforward is the same group. [Katz, *G₂ and hypergeometric sheaves*, §2](https://web.math.princeton.edu/~nmk/g2hyper62finalcorr.pdf) · [Katz, *Convolution and Equidistribution*, Theorems 8.1, 13.1, 18.1 and 18.2](https://web.math.princeton.edu/~nmk/mellin331.pdf)

**Joint support and the LP.** On even modes \(k=2\ell\), write \(U=X_\ell\), \(V=X_{\ell+n/2}\). The [even-mode joint trace argument](parallel-witness-6.md#the-four-coordinates-have-independent-limiting-support) gives independent limits for \((X_k,U,V,(Y_m(k))_{m=2}^M)\). The first three laws are arcsine on \([-1,1]\). Each \(Y_m\) has the law of an average of two independent Haar compact symplectic traces, with support \([-d_m,d_m]\). The endpoints follow from \(\pm I\), and the compact symplectic group is connected. In the joint group with the three circle objects, the geometric derived subgroup contains the entire symplectic product with trivial circle coordinates. For each test word involving a nontrivial symplectic character, the bounded boundary ranks give only \(O(1)\) bad characters, and the tame convolution rank estimate there bounds the generic rank uniformly in \(q\). The all-character average is then the identity-stalk trace of the corresponding middle convolution, of size \(O(q^{-1/2})\) because it has no geometric unit summand. The three-circle law handles the pure circle words. This proves the joint field-size limit, including varying prime fields.

On nonzero even modes the Fourier constraints read

$$ (Ff)_k=1+\tfrac12(\sigma a+b)X_k+\tfrac12\sigma b(U+V)+\sum_{m=2}^M c_m\bigl(T_m(X_k)+\sigma Y_m(k)\bigr)+O_M(q^{-1/2})\biggl(|a|+|b|+\sum_{m=2}^M |c_m|\biggr). $$

The constant and opposite-point terms follow from the [exact sign-mask formula](parallel-witness-6.md#setup-and-the-exact-three-parameter-row). The error in the path terms is the removed coefficient \(g_m(1)\). At a corner of the limiting rectangle take \(X_k\) opposite to \(\sigma a+b\), both \(U,V\) opposite to \(\sigma b\), and \(Y_m\) equal to \(-d_m\sigma\operatorname{sgn}(c_m)\), with either choice when the coefficient is zero. The expression is at most \(1-L\), where \(L=|\sigma a+b|/2+|b|+\sum_{m=2}^M|c_m|\), since \(|T_m(\pm1)|=1\) and \(d_m\ge2\). The finitely many corners are uniformly approximated by actual nonzero modes. The error costs \(o(1)L\) because \(L\) bounds every coefficient. Feasibility gives \((1-o(1))L\le1\), including \(a\le2+o(1)\).

At mode zero, the constant column contributes \(a/(2\sqrt2)+o(1)\) after normalization, the opposite-point column has unnormalized value \(O(1)\) by the same sign-mask formula, and each path column has unnormalized value \(O_M(1)\) by the displayed trace formula and the convolution-dimension bound on its Mellin traces. The constant row with \(a=2\sqrt q/(1+\sqrt q)\) is feasible on all modes by \(|\lambda_k|\le\sqrt q\) for \(k\ne0\) and attains the limiting bound. In an asymptotically optimal sequence \(a\to2\), \(b\to0\) and every \(c_m\to0\), since \(L\ge |a|/2+|b|/2+\sum_{m=2}^M|c_m|\).

## Relation to the Paley Fourier construction

The SDP target and the conversion in Appendix A do apply. For a PSD circulant matrix \(V\) of diagonal one with \(V_{xy}=-c/\sqrt n\) on nonedges of \(H\), add \(c\mathbf1\mathbf1^{\mathsf T}/\sqrt n\) and rescale to trace one. This is a feasible plus Fourier row and gives \(\theta_+\ge c\sqrt n/(1+c/\sqrt n)\). Conversely an optimal plus circulant row of diagonal one and constant eigenvalue \(\theta_+\) can have that eigenvalue removed, then be rescaled to diagonal one. Its nonedge coefficient is \(-\theta_+/(n-\theta_+)\). The corresponding upper value \(1+\sqrt n/c\) is exactly \(n/\theta_+=\theta_-\). Here the conversion is deterministic by multiplicative transitivity. [Potechin–Xu, Appendix A](https://arxiv.org/html/2609.30064v1#A1) · [Paley Fourier LP](fourier.md)

The useful part of the correction procedure is also exact in the Fourier LP. On circulant matrices, ordinary multiplication becomes pointwise multiplication of eigenvalues. Adjoining the boundary sign is multiplication by \(s\) in the positional row and applies \(K\) to the eigenvalues. The sign mask that keeps the identity is \(J+P_\sigma=(I+J+\sigma K)/2\). Thus spectral positivity followed by a position-support correction is available directly, without neglecting any graph intersections. The existing [fixed-width proof](parallel-fixed-width-13.md) controls bounded iterations of these arithmetic operations with Mellin word estimates. The [fixed-mark repair](anchored-repair-20.md) addresses the negative part created by the position-support projection. Neither gives the missing uniform estimate near the ordinary-theta endpoint.

## Replay

The [script](parallel-graph-shapes-23.py) checks the stated identities by cyclic FFT, with independent dense integer checks at small orders and an explicit injective four-cycle sum at the two smallest orders. Selected normalized traces from the [output](parallel-graph-shapes-23.csv) are floating-point diagnostics.

| Order | \(\operatorname{tr}_n A^4\) | \(\operatorname{tr}_n T^2\) | \(\operatorname{tr}_n ATAT\) | Distinct signed four-cycle sum divided by \(n^3\) |
|---:|---:|---:|---:|---:|
| \(9413\) | 1.494630 | 0.495055 | 0.506449 | \(-0.504307\) |
| \(1000033\) | 1.499845 | 0.499849 | 0.499415 | \(-0.500145\) |

```sh
.venv/bin/python -B research/parallel-graph-shapes-23.py > research/parallel-graph-shapes-23.csv
```
