# Uniform support separation and cancellation in the true forced barrier

Through eligible primes the two actual barrier rows at time \(t=L+1\) identify the same primary exposed support by a coordinatewise threshold. If \(I\) is the union of supports on that primary face, including the root, both rows lose the same primary mark \(h(1-|I|/n)\) up to an error smaller than \(h n^{-A}\) for every fixed \(A\). The common loss therefore cancels in the two-tilt comparison. The remaining charge at either tilt equals, to superpolynomial accuracy, that of a strictly positive logarithmic optimizer on the *exact* primary face. The conclusions apply separately to both signs and in particular to the true larger one. The actual fixed-point derivative for these rows has almost isometric directions through every marked depth, including after enforcing the common mean. These results leave the required signed upper estimate on the larger face open.

## The common primary error

Write \(\mathbb E\) for the counting average on \(n=(p-1)/2\) sites. In this note rows are mean one, so \(c(y)=\mathbb E[y\sigma Y_t]-E_t/4\), \(\gamma(y)=y_0/\sqrt n\). Write \(\alpha=\max\gamma\) on the indicated sign, \(F\) for its full primary face, \(c_*=\min_F c\), \(J=I^c\), and \(s_I=|I|/n\). Let \(e=[\mathbb Q(\zeta_n+\zeta_n^{-1}):\mathbb Q]\), \(R=4\sqrt{nt}\), \(h=(2n^{2n})^{-e}/[4(1+R)]\), exactly the previous two-tilt scale. For \(k=1,2\) let \(y=n z_{kh}\) maximize \(\gamma-kh c+h\mathbb E\log y\). All estimates below also hold uniformly on \(0\le k\le n^C\) for each fixed \(C\) and \(1\le t\le D(p)\) (hence also at \(L+1\) eventually). The error notation \(\varepsilon_n\) means \(O_{C,A}(n^{-A})\) for every fixed \(A>0\), and may change at each occurrence. [True tilts and cyclotomic bounds](astra-charged-67.md) · [Window](vanishing-floor-38.md)

Use \(a=n/2+1\). Every vertex on either sign has at most \(a\) positive coordinates. Indeed the rank of \(n(I-P_\sigma)\) is \(n-(n-1-\sigma)/2\), and the support columns of a vertex are independent. The Cramer proof with this rank supplies two bounds. Every positive probability coordinate of a vertex is at least \(m=n^{-ae}\), and every positive difference of normalized vertex marks on the same sign is at least \(G=(2n^{2a})^{-e}\). For the first, the numerator and denominator of each coordinate are real cyclotomic integers of absolute value at most \(n^a\) in every embedding. The norm of a nonzero numerator is an integer of absolute value at least one. For the second, apply the same argument to a cross numerator and the product of two denominators, before multiplying by \(\sqrt n\). This proof uses the actual sign projectors. [Sign ranks](fourier.md) · [Projection-minor details](astra-charged-67.md#recovering-the-signed-marginal-without-knowing-the-exposed-support-or-primary-mark)

For any feasible \(w\), stationarity along the affine difference gives
\[
  (\gamma(w)-\gamma(y))/h-k(c(w)-c(y))=1-\mathbb E[w/y].                 \tag{1}
\]
The gap between the linear score at \(y\) and its full maximum is at most \(h\). A vertex off \(F\) has linear gap at least its primary deficit times \(1-khR/G\); on \(F\) the gap is nonnegative. Here \(khR/G=\varepsilon_n\), so the full linear maximum is \(\alpha-kh c_*\), also when \(k=0\). In any vertex decomposition of \(y\) the off-face fraction \(\rho\) and the primary mark loss obey
\[
 \alpha-\gamma(y)\le h/(1-khR/G),\qquad \rho\le 2h/G.                 \tag{2}
\]
Each \(i\in I\) is positive at some primary vertex \(w^{(i)}\). Testing (1) there gives \(\mathbb E[w^{(i)}/y]\le1+kR\), so \(y_i\ge m/(1+kR)\). At each \(i\in J\) some opposite primary vertex \(v^{(i)}\) has \(v^{(i)}_i\ge nm\) in mean-one units. This follows from strict complementarity for the single-mark LP and decomposition in opposite vertices. Opposite-sector orthogonality gives \(\mathbb E[yv^{(i)}]=1\); the root accounts for \(\gamma(y)/\alpha\) by complementary mark reciprocity. Positivity and (2) then give \(y_i\le 2h/(\alpha m)\). Both signs' \(\alpha\) are bounded above and away from zero by the Jacobi bracket. [Exterior partition](rank-partitions.md#complementarity-gives-the-partition) · [Endpoint normalization](astra-charged-68.md)

Let \(w\) be the normalized conditioning of this decomposition on \(F\). The coordinate range is bounded by \(n\), so \(\|w-y\|_\infty\le n\rho\) and \(|c(w)-c(y)|\le R\rho\). In particular
\[
  \sup_{i\in I}|w_i/y_i-1|\le 2nh(1+kR)/(Gm)=\varepsilon_n.
\]
Indeed \(h/(Gm)=n^{-(2n-3a)e}/[4(1+R)]\), with \(2n-3a=n/2-3\). Thus \(w\) is in the relative interior of \(F\) for large \(p\). Inserting it in (1) gives the promised common term and a one-sided true charge sandwich for \(k\ge1\):
\[
 \frac{\alpha-\gamma(y)}h=1-s_I+\varepsilon_n,\qquad
 c_*-\varepsilon_n\le c(y)\le c_*+s_I/k+\varepsilon_n.                \tag{3}
\]
For the lower bound use the conditioned feasible row. The upper bound uses the linear gap at \(y\) of at most \(h\) together with the displayed primary loss. In particular \((V(h)-V(2h))/h=c_*\) differs from \(c(nz_h)\) by at most \(s_I+\varepsilon_n\). A third tilt \(k=n^C\), at the *same* barrier floor, gives error \(s_I n^{-C}+\varepsilon_n\) without resolving gaps between secondary scores. This still requires knowing the actual signed charge in the arithmetic window.

More precisely let \(x_k\) maximize \(\mathbb E[\mathbf1_I\log x]-k c(x)\) on \(F\) with positive entries on \(I\); the logarithm here and below is summed only on its indicated domain. Existence and uniqueness follow from compactness and strict concavity on the active coordinates. For all \(k\) above,
\[
   \sup_{i\in I}|x_{k,i}/y_i-1|=\varepsilon_n,\qquad c(x_k)-c(y)=\varepsilon_n.       \tag{4}
\]
To see this, apply full and facial stationarity in the common affine direction \(x_k-w\). Subtract them to get \(\mathbb E_I[(x_k-w)(1/y-1/x_k)]=0\), where \(\mathbb E_I\) uses divisor \(n\). Write \(r=x_k/w\) on \(I\), \(H=\mathbb E_I[(r-1)^2/r]\), and \(b=\sup_I|1-w/y|\). Then \(H=\mathbb E_I[(r-1)(1-w/y)]\le b\sqrt{H\mathbb E_I r}\le b\sqrt{H(H+2)}\). Thus \(H\le2b^2/(1-b^2)\). Each \((r_i-1)^2/r_i\le nH\), proving uniform relative agreement. Equation (4) follows by the conditioning cost bound and the resulting superpolynomial total variation agreement between \(w/n\) and \(x_k/n\). In particular two truly different facial rows can account for the two linear evaluations even after the primary terms cancel. If the primary face is a singleton, both barrier charges equal its exact charge to superpolynomial accuracy, with no secondary optimization needed.

## Obstruction on the actual primal fixed point

Put \(B=\sqrt n e_0-kh\sigma Y_t\), \(r_0=h/y\) coordinatewise, \(\lambda=\mathbb E r_0\), \(b=h/\lambda\), and \(d=y-r_0/\lambda\). Here \(r_0\) denotes a vector. Affine stationarity gives \(P_\sigma r_0=-P_\sigma B\); testing against \(y-1\) gives \(\lambda=h+\mathbb E[yB]-\mathbb E B\). Since \(\mathbb E Y_t=0\), the bound on \(R\), (2) and the Jacobi brackets imply \(\lambda=\alpha-1/\sqrt n+O(h+khR)\asymp1\). The common mean is \(\mathbb E y=\mathbb E[r_0/\lambda]=1\). Consequently
\[
  d=\sigma K\sqrt{d^2+4b}+2P_\sigma B/\lambda,\qquad
  D_y=\operatorname{diag}\frac{d}{\sqrt{d^2+4b}}
      =\operatorname{diag}\frac{y^2-b}{y^2+b}.                        \tag{5}
\]
Indeed the activation is \(y+r_0/\lambda\), and the difference of the two sides before the forcing is \(-2P_\sigma r_0/\lambda\). Let \(S\) be the diagonal sign equal to \(+1\) on \(I\) and \(-1\) on \(J\). The pointwise active and inactive bounds above give
\[
  \|D_y-S\|_{2\to2}\ll h(1+kR)^2/m^2=\varepsilon_n.                  \tag{6}
\]
Thus the sign of \(d\) exactly identifies \(I\) for all sufficiently large eligible primes, uniformly in these tilts. Formula (6) includes every coordinate and both signs. In particular the two tilts share the same limiting sign *at each large field*, including any tied primary optimizers.

The fixed-\(\lambda\) Jacobian in (5) is \(A=\sigma K D_y\). Set \(Q=\sigma KS\), and write \(\epsilon=\|D_y-S\|\). Both maps are contractions in normalized Euclidean norm, and \(\|A^j-Q^j\|\le j\epsilon\). For \(j\) steps, each of the conditions \(\mathbb E[S Q^i v]=0\) for \(0\le i<j\) removes at most one dimension. On their intersection \(\|Q^j v\|=\|v\|\), because \(K^2=I-\mathbf1\mathbf1^{\mathsf T}/n\). One may in addition impose \(\mathbb Ev=0\). It follows that the \(j\)-step derivative has stretch at least \(1-j\epsilon\) on a subspace of dimension at least \(n-1-j\).

The same obstruction survives enforcing the mean at each update. Near this fixed point determine \(\lambda(d)>0\) from \(\mathbb E\sqrt{d^2+4h/\lambda(d)}=2\) for mean-zero \(d\). Its scalar derivative in \(\lambda\) is strictly negative, so the local implicit function is smooth. The derivative of the right-hand side of (5) then has the form \(M=A+v_0 f^{\mathsf T}\) on the mean-zero space. On the additional subspace \(f^{\mathsf T}A^i v=0\) for every \(0\le i<j\) one has \(M^jv=A^jv\) exactly, regardless of the size of the rank-one correction. Thus for every \(2j<n-1\) there is a subspace of dimension at least \(n-1-2j\) with
\[
                \|M^jv\|\ge(1-j\epsilon)\|v\| .                       \tag{7}
\]
In particular full-space contraction by any fixed factor less than one at or before the marked depth fails on the actual primes for this Picard map in both conventions. The test permits finitely many further oblique or orthogonal linear constraints by intersecting subspaces. It makes no assertion about convergence along the particular cold orbit, a scalar score, or damped or Newton updates.

## The two support restrictions of the limiting derivative

Let \(D_I,D_J\) be the coordinate projectors on the primary sets \(I,J\), and retain \(Q=\sigma K(D_I-D_J)\) from (6). On the mean-zero space there is the exact identity
\[
 (I-Q)v=2P_{-\sigma}D_Iv+2P_\sigma D_Jv,\qquad
 \|(I-Q)v\|^2=4\bigl(\|P_{-\sigma}D_Iv\|^2+\|P_\sigma D_Jv\|^2\bigr).      \tag{8}
\]
Indeed \(I\mp\sigma K=J_{\mathrm{const}}+2P_{\mp\sigma}\), where \(J_{\mathrm{const}}\) is the constant projector. Apply these two operators to \(D_Iv,D_Jv\) respectively. Their constant terms add to zero and the two sector terms are orthogonal.

The kernel of \(I-Q\) there is the orthogonal sum \(T_\sigma\oplus T_{-\sigma}\) of the two actual primary-face tangents. If \(Qv=v\), equality of the norms of \(K(D_I-D_J)v\) and \(v\) forces \(\mathbb E[(D_I-D_J)v]=0\). Thus both coordinate pieces have zero mean. Equation (8) puts them in \(V_\sigma,V_{-\sigma}\), respectively. A mean-zero sign-\(\sigma\) direction supported on \(I\) has zero root, by pairing with an opposite optimizer positive at the mark and supported on \(J\cup\{0\}\). It is then a tangent direction because a relative interior optimizer is positive at every site of \(I\). A sign-\(-\sigma\) mean-zero direction supported on \(J\) is an opposite tangent by the same relative interior argument using the support \(J\cup\{0\}\). Conversely both tangents satisfy (8) with value zero.

On \(U=\mathbf1^\perp\) let \(C\) be the compression to \(U\) of \(D_IP_{-\sigma}D_I+D_JP_\sigma D_J\). Equation (8) gives \((I-Q)^*(I-Q)|_U=4C\), with the adjoint taken on \(U\). For any observable \(g\in U\) perpendicular to the two tangents, the optimal constant in
\[
 |\langle g,v\rangle|\le \mathcal R(g)\|(I-Q)v\| \quad (v\in U)
\]
is \(\mathcal R(g)=\tfrac12\sqrt{\langle g,C^\dagger g\rangle}\), where \(C^\dagger\) inverts \(C\) on the orthogonal complement of its kernel. This follows by Cauchy--Schwarz in the diagonalization of the positive operator \(C\), with equality at \(v=C^\dagger g\) when \(g\ne0\). In particular the late observable restricted to \(I\), after subtracting its mean and its component in \(T_\sigma\), is already perpendicular to \(T_{-\sigma}\). A directional bound can therefore test its inverse spectral moment on these two actual Fourier restrictions while keeping the \(T_\sigma\) response in the facial problem. This identity gives no field-uniform estimate of that inverse moment.

## Finite replay

At the eligible prime 13 the larger minus face is the singleton \(y=(3,0,0,3,0,0)\). It pairs optimally with the plus row \(1+\cos(\pi i/3)\), whose only zero is at 3. The two barrier optimizers are even by uniqueness and reflection. At the illustrative cold time 3, eliminating the even Fourier and mass constraints leaves their sites 1 and 2 as two variables. The checker encloses their rescalings by \(h\) using a self-mapping rectangle for the exact two stationary equations. Brouwer gives a fixed point there and strict concavity identifies it as the true barrier optimum. For tilts 1 and 2, the scaled primary losses lie within \(1.5\cdot10^{-11}\) of \(4/6\), and their signed charges differ from the exact primary-face charge by less than \(7.51\cdot10^{-12}\). This is a finite outward-rounded check of the normalizations. [Arb checker](astra-forced-69-check.py) · [Two interval records](astra-forced-69-checks.jsonl)

## What can still be tested on the larger sign

1. On the common exposed support use the *facial* center \(x_0\) and its response to the late score \(g=\sigma Y_t\). In normalized Euclidean norm on \(I\), let \(T\) be the tangent of \(F\), and \(P_k\) the orthogonal projection onto \(\{v/x_k:v\in T\}\). Differentiating facial stationarity gives \(x_k'/x_k=-P_k(x_k g)\), hence
\[
 c(x_1)=c(x_0)-\int_0^1\|P_k(x_k g)\|_{2,n}^2\,dk.
\]
Smoothness follows by the negative-definite facial Hessian, also in the zero-dimensional case. This is an exact signed gain on the primary face without the primary term or cyclotomic scale. A prime-uniform upper \(o(L)\) for the right side passes for the larger sign by (3)–(4) and the [charged reserve](astra-charged-66.md). A positive normalized lower margin along unbounded primes rejects this one-time charge test. Neither inequality is established here.
2. For a direct forced iteration try a marked or score-direction estimate after imposing the common support. A contraction factor bounded away from one in the full Euclidean norm through \(L+1\) steps fails by (7) on every sufficiently large eligible prime; this failure applies even with the actual normalization. A bound on the signed terminal pairing alone that is \(o(L)\) on an actual larger-face row would suffice. The ordinary theta limit remains open.
