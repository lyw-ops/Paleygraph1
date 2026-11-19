# A genuine sector down to zero and a signed Schur test beyond a right angle

Let \(n=(p-1)/2\), \(p\equiv1\pmod4\) prime, \(c=(n-1)/n\), and \(W=1+ct\). Use the actual real symmetric Jacobi operator \(K\), with \(K^2=I-J\) for the mean projector \(J\). The weights in scaled physical coordinates are \(t_0=n\) and \(t_i=t\) on the bulk. The original stationary equation has a single-valued physical section on the following open set, for every eligible field:
\[
 \Re t>0,\qquad \mathcal B_n(t):=\frac n2(1+c|t|-|1+ct|)<|t|.                 \tag{1}
\]
At every eligible size, (1) has the explicit polar form \((n-1)\sin^2(\arg t/2)<1+(1-2/n)|t|\) in the right half-plane. This includes the entire relative sector \((n-1)\sin^2(\arg t/2)<1\) from zero to infinity in the right half-plane. At every \(n\ge10^{30}\) it includes \(|\Re t-2031/128|\le2^{-17}\), \(|\Im t|\le130/\sqrt n\). The [earlier isotropic chart](parallel-complex-structure-35.md#2-a-quantitative-local-theorem-for-any-positive-weighted-barrier) has radius \(x^{3/2}/(32\sqrt n)\) at a real floor \(0<x<n\). Near the candidate floor its coefficient is below two. Toward zero its relative disk width decays as \(\sqrt{x/n}\), while (1) retains a relative width of order \(1/\sqrt n\). The field-dependent sector does not give a common positive width through unbounded primes.

## The weighted angular budget at the genuine endpoint

Write \(A_i=(\Phi_i+U_i)/2=\sqrt{t_i}e^{z_i}\), \(B_i=(\Phi_i-U_i)/2=\sqrt{t_i}e^{-z_i}\), \(\phi_i=\Im z_i\), and start each log at its real positive stationary factors. At \(\lambda=1\), \(EU=0\) and \((E\Phi)^2=E(\Phi^2-U^2)=4W\) by the bilinear isometry. Thus both factor means equal \(\sqrt W\). The nonconstant parts of the factors belong to opposite real Fourier sectors, so the Hermitian pairing gives the full angular identity
\[
             \sum_i |t_i| e^{-2i\phi_i}=n|W|,
   \qquad   \sum_i |t_i|\sin^2\phi_i=\mathcal B_n(t).                 \tag{2}
\]
This is the full-row version of the [conjugate stationary pairing](parallel-cold-complex-36.md#1-the-exceptional-coordinate-forces-a-complex-sector). Along the physical branch the mark satisfies \(|\phi_0|\le|\arg W|/2\), by that pairing. Also \(\mathcal B_n/n\le\sin^2(\arg t/2)<1/2\) since \(|1+ct|\ge c|t|+\cos(\arg t)\). In (1) the total angular budget is therefore less than every individual weight. All phases stay strictly in \((-\pi/2,\pi/2)\) from the real start. If two phases in that interval differ by \(\pi/2\), their squared sines sum to one. Their two charges already consume at least the smaller weight. A first encounter with that diameter is impossible in (1).

The phase diameter below \(\pi/2\) gives an invertible Jacobian by the signed test below. To establish continuation, take the circular arc at fixed \(|t|\) from the positive axis to the point in question. The budget increases monotonically in the absolute polar angle. At fixed field the strict margin on this compact arc puts all bulk phases in \([-\pi/2+\epsilon,\pi/2-\epsilon]\) for some \(\epsilon>0\). Rotate both sets of factors by \(e^{-i\arg(t)/2}\). Their bulk arguments become \(\pm\phi_i\). Their marked arguments are \(\pm\phi_0-\arg(t)/2\), of magnitude strictly below \(\pi/2\), uniformly on this arc, by the marked sector. Both rotated sums equal \(n e^{-i\arg(t)/2}\sqrt W\), so positivity of the individual real parts bounds each modulus. The reciprocal products give lower bounds on all moduli. Consequently every limiting physical pair is compact, its \(\Phi_i=2\sqrt{t_i}\cosh z_i\) is nonzero, and (2) still excludes diameter \(\pi/2\). The implicit function theorem continues each arc. The arcs at nearby moduli give compatible local solutions by continuation from the same real stationary branch, using finitely many implicit-function neighborhoods along each compact arc. They give a single holomorphic section on (1).

For the explicit strips, writing \(t=x+iy\), rationalization gives
\[
 \frac{\mathcal B_n}{|t|}=
 \frac{(n-1)(1-\cos(\arg t))}{1+c|t|+|1+ct|},\qquad
 \mathcal B_n=\frac{nc\,y^2}{(|t|+x)(1+c|t|+|1+ct|)}
        \le \frac{nc\,y^2}{4x(1+cx)} .                             \tag{3}
\]
For \(n\ge4\), (1) is equivalent to \(|n+(n-1)t|>n+(n-3)|t|\). Squaring the two positive sides gives the polar form in the opening paragraph. At \(n=2\) both descriptions include the full right half-plane. The first denominator in (3) is at least two in this half-plane. The second estimate gives \(\mathcal B_n<x\) if \(\sqrt n\,|y|<2x\sqrt{x+1/c}\). The last coefficient is greater than \(130.3319\) on the stated real strip. In particular (1) holds across the closed height \(130/\sqrt n\) without a size ceiling. The entire relative sector is useful also at moving real floors much smaller than the candidate floor.

## A Schur test that keeps the large real amplitudes and both phase signs

At any physical point of a forced or unforced continuation with \(|\phi_i|<\pi/2\), put \(\rho_i=\Re z_i\), \(E=\operatorname{diag}\tanh\rho\), \(M=\operatorname{diag}\operatorname{sech}\rho\), \(T=\operatorname{diag}\tan\phi\), and \(D=\operatorname{diag}\tanh z\). All real amplitudes enter the self-adjoint real response
\[
   R=M X M-E,\qquad X=(I-KE)^{-1}K=K(I-EK)^{-1}.
\]
At a fixed field \(\|E\|<1\) and \(\|R\|\le1\). Indeed set \(v=XM f\), so \(v=K(Ev+Mf)\). The real orthogonal block with rows \((E,M),(M,-E)\) sends \((v,f)\) to \((Ev+Mf,Rf)\). This gives \(\|Rf\|^2+\|J(Ev+Mf)\|^2=\|f\|^2\). [Real response identity](response-locality.md#contraction-and-response-derivative)

The full complex Jacobian \(I-KD\) is invertible exactly when \(I-iRT\) is invertible. In fact \(D=(E+iT)(I+iET)^{-1}\). Right multiplication of \(I-KD\) by \(I+iET\) gives \(I-KE-i(K-E)T\), and \((I-KE)^{-1}(K-E)=XM^2-E=M^{-1}RM\). The diagonal matrices used here are invertible, or commute where reordered.

Split the nonzero-phase coordinates into \(P=\{T_i>0\}\), \(N=\{T_i<0\}\). Put \(L=|T|^{1/2}R|T|^{1/2}\) and write \(A=L_{PP}\), \(C=L_{PN}\), \(B=L_{NN}\). Removing zero phases and conjugating by \(|T|^{1/2}\) gives the block system
\[
 \begin{pmatrix}I-iA&i C\\-iC^*&I+iB\end{pmatrix}.
\]
Each diagonal block is invertible. The exact remaining Schur matrix is \(I+iB-C^*(I-iA)^{-1}C\). Its real Hermitian part gives the sufficient condition
\[
           \lambda_{\max}\big(C^*(I+A^2)^{-1}C\big)<1.                 \tag{4}
\]
The version with the signs interchanged holds as well. Keeping both same-sign blocks also permits the sufficient test \(\|(I+A^2)^{-1/4}C(I+B^2)^{-1/4}\|<1\). Indeed two-sided scaling makes each diagonal block unitary and the two off-diagonal operator norms equal this norm. All tests include large positive or negative real logarithms, which enter through \(R\). The simpler sufficient condition \(\|C\|<1\) follows immediately. This holds if \(\max_{P}\tan\phi\;\max_{N}|\tan\phi|<1\), in particular for diameter below \(\pi/2\). If either sign is absent the remaining diagonal block is invertible.

There is a sufficient test using just the return between **opposite high phases**. Suppose \(|\tan\phi|\le b\). For \(0\le d\le b\) let \(H_\pm=\{\pm\tan\phi>d\}\) and \(k=\|R_{H_+,H_-}\|\), interpreted as zero for an empty block. Then
\[
       \|C\|\le \tfrac12\left[\sqrt{4bd+(b-d)^2k^2}+(b-d)k\right].
                                                                      \tag{5}
\]
To verify this bound first enlarge the diagonal weights to \(\sqrt b\) on the high sets and \(\sqrt d\) on the rest by factoring out coordinate contractions. Dilate the contraction \(R_{PN}\) to an orthogonal map between enlarged spaces, with the high projections \(P_0,Q_0\) zero on the added spaces. Give the new low sites weight \(\sqrt d\). The original product is a compression. Moving the orthogonal map left gives a product of two operators with eigenvalues \(\sqrt b,\sqrt d\) on the ranges and kernels of two orthogonal projections satisfying \(\|P_0'Q_0\|=k\). Diagonalizing \(Q_0P_0'Q_0\) decomposes the generic part into two-dimensional planes, with squared principal cosine \(s^2\le k^2\). On such a plane the product's squared singular values have sum \(2bd+(b-d)^2s^2\) and product \((bd)^2\). The one-dimensional pieces have gains \(b,\sqrt{bd},d\), with \(b\) possible only at \(k=1\). This gives (5), including degenerate weights by continuity. In particular the full Jacobian is invertible under
\[
                  bd+(b-d)k<1.                                      \tag{6}
\]
For the [height-600 physical forcing path](phase-action-84.md) in \(|\phi|\le\arctan(3/2)\), take \(b=3/2,d=1/3\). Only \(k<3/7\) is needed. At every high site the initial log \(w_i\) satisfies \(|\Im w_i|<0.26\), so the exact difference of two hyperbolic sines gives
\[
 |U_i-X_i|\ge4\sqrt{\inf\Re t}\cos\big((\arctan(3/2)+0.26)/2\big)
                           \sin\big((\arctan(1/3)-0.26)/2\big)>0.38.
\]
Here \(\inf\Re t=2031/128-2^{-17}\) on the candidate square. By the [enlarged-sector secant bound](astra-imaginary-84.md#large-derivatives-at-height-600-beyond-unit-phase), the fraction of the union \(H_+\cup H_-\) is at most \(870\lambda^2\|R_X\|_2^2/(0.38)^2\), with uniform field-first limsup below \(5.65\cdot10^{-412}\). This is an instantaneous estimate along the true forced path in the enlarged sector. It neither bounds \(k\) on those actual sets nor prevents sector exit. A uniform test through the remaining forcing parameters would need both continuation controls.

## A genuine mixed-phase example at prime 173

At \(t=1/50+7i/200\), the physical unforced row from the positive axis has phase minimum in \((-0.848,-0.847)\) and maximum in \((1.501,1.502)\). There are 40 positive and 46 negative phases. Both signs exceed the unit-derivative threshold, and their diameter exceeds \(2.348\) radians. A rational vector proves \(\|C\|>1.408\), whereas \(\operatorname{tr} C^*(I+A^2)^{-1}C<0.7497\). Thus (4) certifies the full 86-coordinate Jacobian beyond both the angular-diameter and raw cross-norm tests. This finite example works at its stated floor; the uniform candidate-square result is (1) at the size-dependent width.

The checker starts from an interval-certified real stationary solution, reuses the [round-37 validated continuation](astra-cold-37-monodromy.py), then encloses the two reciprocal factors of each physical Fourier coordinate. On all 65 verified segments, including the endpoint refinement, the enclosed normalized plus factors have positive real part. Thus the principal endpoint phases are the continuous lifts from the real start. It computes \(R,A,C\) on the full cyclic matrix with Arb at 128 bits and evaluates the trace on the true signed partition. Floating point is used to propose continuation centers and a rational witness for the lower bound. [Checker](astra-compression-85-check.py) · [Outward records](astra-compression-85-checks.jsonl)

1. On the actual height-600 path bound the damped return (4) on the two phase signs, starting with \(H_+,H_-\) in (6). The observed set density permits both high sets to have unbounded size. Their interaction through the real amplitude response is the remaining spectral quantity.
2. On the genuine endpoint use (2) together with the spatial locations of both phase extrema to improve (1) beyond the \(n^{-1/2}\) scale. The exact total charge alone allows an almost vertical phase on one site with very small opposing phases. A fixed positive width at the cold square and the ordinary-theta asymptotic remain open.
