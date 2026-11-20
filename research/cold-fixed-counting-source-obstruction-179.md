# A normalized lower bound for the true fixed cold residual

Use the genuine nine-center start, both lifts, the original closed square \(Q\) around \(a=2031/128\) of half-width \(2^{-17}\), and the physical mark \(t_0=n\). Write \(R_j=V_{j+1}-V_j\) and \(\|\cdot\|_{2,n}^2=n^{-1}\sum_i|\cdot_i|^2\). The actual fixed-source shortcut of [Round 177](cold-seed-centered-larger-tube-177.md) fails:
\[
 \liminf_{p\to\infty}\inf_{t\in Q}\|R_{611}(t)\|_{2,n}>0 .
\]
Consequently the unnormalized counting norm grows at least as a fixed positive multiple of \(\sqrt n\), uniformly on this square for sufficiently large eligible primes. This result concerns the fixed height, and leaves the growing signed transmission and stationary common domain open. The proof was found by native Astra agent /root/cold_179.

## Transport against a signed Jacobi-angle test

Use the subsequential compact model and geometric transport \(\mathcal K\) of [Round 79](astra-fixed-79.md). It is an isometry modulo constants on even activation inputs. In it
\[
 U_{j+1}=S+\mathcal K F_t(U_j),\qquad
 F_t(z)=\sqrt{4t+z^2},\quad S=\sqrt8\cos\theta ,
\]
with the principal branch and the affine trace phase of the Jacobi line \(J=e^{i\theta}\) oriented to give this seed. Its angle is Haar. Genuine adjacent differences \(d=U_j-U_{j-1}\) are differences of transported fields, including the first because \(U_0=S+\mathcal KP\) has a finite positive preimage. [Round 80, (4)](astra-dissipation-80.md) gives
\[
 \mathbb E(d\mid J)=0,\qquad \mathbb E(|d|^2\mid J)=\|d\|_2^2 .
\]
The physical fixed caps through \(V_{612}\), from [Rounds 88 and 177](cold-seed-centered-larger-tube-177.md), give \(|U_j-S|\le2.338\). Take \(A=\{|\cos\theta|\ge\cos(\pi/10)\}\), of probability \(1/5\), and \(\sigma=\operatorname{sign}S\) on \(A\). Every point of the segment between adjacent rows, after multiplication by \(\sigma\), is \(z=x+iy\) with \(x>.349\), \(|y|\le 2.338\), \(|z|\le\sqrt8+2.338\). If \(u+iv=\sqrt{4t+z^2}\), then \(u>7.6\) and \(|4t+z^2|<91\). We have
\[
 xu+yv=x(u+y^2/u)+2y\Im(t)/u
 >.349(7.6)-2(2.338)2^{-17}/7.6 .
\]
It follows that \(\Re(z/\sqrt{4t+z^2})>.029\). The derivative is odd, so the real part of \(\sigma\) times the secant on the unreflected adjacent segment is at least \(.029\). On the real diameter this improves to \(.349/8\): the unsigned derivative at absolute value at least \(.349\) is at least \(.349/\sqrt{4(a+2^{-17})+.349^2}>.349/8\).

For \(T=F_t(U_j)-F_t(U_{j-1})\), test \(T-\mathbb ET\) against \(\sigma1_A d\). The centering term vanishes by conditional mean zero. The real part of the inner product is at least \(.029\mathbb E1_A|d|^2=.029\|d\|_2^2/5\), and the test vector has second norm \(\|d\|_2/\sqrt5\). The isometry gives
\[
 \|U_{j+1}-U_j\|_2\ge (.029/\sqrt5)\|U_j-U_{j-1}\|_2 .
\]
The real-diameter factor can be taken as \(.019\). These statements concern every fixed tested step in the genuine prefix.

## Nonvanishing at the finite nine-center start

If \(U_1-U_0=0\) in such a compact model, then \(\mathcal K(F_t(U_0)-P)=0\), hence \(F_t(U_0)=P+c\) for a scalar \(c\). Here \(P,U_0\) are the actual finite Laurent expressions along the first circle of Round 79, so equality holds everywhere by continuity on the Haar coset. The Laurent polynomials \(P+c\pm U_0\) satisfy
\[
 (P+c-U_0)(P+c+U_0)=4t .
\]
They are monomials, since their product is a nonzero constant. They both have positive real part on every circle: \(\Re F_t(U_0)\ge\sqrt{4(a-2^{-17})-1.94^2}>7.7\) and \(|U_0|<4.77\). Thus both have winding number zero, and each is constant along the circle. This would force \(U_0\) constant along that circle, contrary to the opposite strict signs of its real part at the two seed extrema, by \(|U_0-S|\le1.94\). Hence the initial difference is nonzero in every such limit. The real central floor also has the quantitative inherited bound \(\liminf_p\|R_0(a)\|_{2,n}>0.00042\) by the signed source coefficients of [Round 83](astra-direction-83.md). Iteration at that floor gives
\[
 \liminf_p\|R_{611}(a)\|_{2,n}\ge 0.00042(.019)^{611}>10^{-1056}.
\]

## Fixed-height compact transfer with the physical mark

The fixed-word compact comparison of Rounds 79 and 80 allows the coefficients to converge along any chosen \(t_p\to t\in Q\). To apply it up to height 612, the true rows have coordinate cap \(5.2\) on this fixed prefix. Extend the bulk even activation from \(|z|\le5.2\) to an even globally Lipschitz cutoff supported in \(|z|<6\), uniformly in \(Q\), using the principal analytic branch on the larger radius \(6\). For each bounded finite trace approximant, polynomials in \(z,\bar z\) of even total parity approximate the cutoff on its range. The normalized second-norm contraction of \(K\), the Lipschitz bound and the fixed-word moment comparison identify successive rows jointly in second norm, first at fixed approximation and then at accuracy tending to zero. These approximants include duals and both lifts. The actual empirical cap transfers to \(|U_j-S|\le2.338\) by this joint approximation. On the resulting bounded rows the cutoff agrees with the activation.

At the mark, subtracting the real \(2\sqrt n\) activation forcing gives a bounded change of the bulk input coefficient at \(e_0\): \(\sqrt{4n+V_{j,0}^2}-2\sqrt n-F_t(V_{j,0})=O(1)\). Its transported correction is \(o(1)\) in normalized second norm, since \(\|Ke_0\|_{2,n}\le n^{-1/2}\). The seed \(2\sqrt nKe_0\) is retained exactly. Therefore along the compact subsequence the physical fixed increments converge in normalized second norm to the stated compact increments. A violating sequence with \(\|R_{611}(t_p)\|_{2,n}\to0\) would have a compact subsequence, where the nonzero initial increment and the finite chain of lower secants contradict this. This proves a uniform, ineffective positive lower bound for the normalized residual over \(Q\), with no growing-height compact transfer.
