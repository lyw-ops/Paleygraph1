# Clipped factor geometry and the two signed floor corrections

The clipped real construction of round 89 has a rigid solution set. Differences between two of its genuine clipped factors can occur only on common saturated sites of the same sign. Four genuine Jacobi eigenrows describe these differences, supported separately on the two signs. In particular the total floor correction on each sign is canonical. A two-weight secant gives a quantitative lower bound for the correction whenever a true unforced factor in the positive real-part chart exceeds the clip angle and its summed phases with a clipped factor remain in a common half-plane. This occurs at a certified finite prime and small real floor.

## A coordinate criterion for equality

Use the normalization of [round 89](real-phase-projection-89.md) so the bulk products are one before adding any positive defects, and the marked product is \(n/t\). Fix \(0<a<1\), \(\vartheta=\arctan a\), and take \(\kappa=a^{-2}\) in that construction. At a clipped fixed point write \(U=\mathcal A-\mathcal B\), \(S=\mathcal A+\mathcal B\). On the bulk use the metric \(\|z\|_a^2=a^2(\Re z)^2+(\Im z)^2\), and use the same metric at the mark. In physical \(U\) coordinates write
\[
 g(x)=2\sin\vartheta\sqrt{1+x^2/(4\cos^2\vartheta)}.
\]
Off the mark the activation \(S=\Psi_a(U)\) is \(\sqrt{4+U^2}\), on the positive branch, when \(|\Im U|\le g(\Re U)\). This is the true phase range \(|\phi|\le\vartheta\) for bulk product one. Outside that range it is
\[
       S=\varepsilon(\Im U/a+i a\Re U),\qquad
             \varepsilon=\operatorname{sign}(\Im U).
\]
Indeed each clipped site has \(\tan\phi=\varepsilon a\) and the bulk product \(1+e\ge1\). Then \(\Im U=\varepsilon a\Re S\), \(\Im S=\varepsilon a\Re U\). The bulk defect equals
\[
       e+1=\frac{1+a^2}{4a^2}\big[(\Im U)^2-(a\Re U)^2\big].
\]
This is at least one precisely in the saturated region. The two branches agree on its boundary. Both saturated regions are convex since \(g\) is convex.

For an interior site complex multiplication by \(d=\tanh(\rho+i\phi)\) is the differential. Its two singular values in the metric \(\|\cdot\|_a\) have product \(|d|^2\) and difference \((a^{-1}-a)|\Im d|\). This follows from the trace and determinant of the Gram matrix of \(\begin{psmallmatrix}\Re d&-a\Im d\\a^{-1}\Im d&\Re d\end{psmallmatrix}\). Thus the differential has norm at most one exactly when \((a^{-1}-a)|\Im d|\le1-|d|^2\). The hyperbolic formulas reduce this to \(|\tan\phi|\le a\), with strict contraction in the interior. On each saturated region the displayed real-linear activation is an isometry. Continuity along segments then gives global nonexpansiveness in the bulk metric. For two distinct inputs equality can occur only within one closed saturated region. Any segment with some interior subsegment has strict contraction on that subsegment, and the two saturated regions cannot be joined without an interior subsegment.

At the mark compare two legitimate clipped solutions at fixed \(t\), with relative logs \(z_0,z_0'\) in the physical lift. In their real weight reconstruction the two marked imaginary-to-real ratios are \(P_0(1+c_0)\) and \(P_0(1-c_0)\) with the same sign. Their angles therefore have the same sign and sum to \(\arg(n/t)\), so \(|\Im z_0|\le|\arg t|/2\), and similarly for \(z_0'\). If \(|\arg t|/2<\vartheta\), the marked secant multiplier \(\tanh((z_0+z_0')/2)\) is strictly contractive in \(\|\cdot\|_a\). This part only needs the secant between legitimate fixed points. [A globally extended clipped map and its residual estimates](astra-column-90.md)

## The exact Fourier spaces of differences

For two genuine clipped fixed points let \(\Delta U=U^{(1)}-U^{(2)}\) and \(\Delta S=S^{(1)}-S^{(2)}\). Since \(\Delta U=K\Delta S\), \(K^2=I-J\) gives
\[
 \|\Delta U\|_a^2=\|\Delta S\|_a^2-n\|E\Delta S\|_a^2
                  \le\|\Delta U\|_a^2 .
\]
These are counting norms. Hence the means and marks agree, and every changed bulk site lies in a common closed saturated region of the same sign. The segment between the two solutions is a segment of clipped solutions. Indeed the activation is affine there at every changed coordinate, and both the marked product and positivity chart are retained.

Set \(f=a\Re\Delta U,\ h=\Im\Delta U\), and let \(D_\sigma\) be the changed sites of common sign \(\sigma\). Put \(\varepsilon=\pm1\) on these two sets and zero elsewhere. Then \(f=K(\varepsilon h), h=K(\varepsilon f)\); also \(E(\varepsilon f)=E(\varepsilon h)=0\) by equality of means. It follows that
\[
 K(f+h)=\varepsilon(f+h),\qquad K(f-h)=-\varepsilon(f-h).
\]
Restricting \(f+h\) to \(D_\sigma\) gives a genuine \(\sigma\)-eigenrow, and restricting \(f-h\) gives a genuine \(-\sigma\)-eigenrow. To see this, the original fixed difference also has \(K[\varepsilon(f+h)]=f+h\) and \(K[\varepsilon(f-h)]=-(f-h)\), so take the two signed half-sums. Thus the difference between clipped points is resolved into four real eigenrows with controlled support. This includes the even restriction when both fixed points are even.

In particular a clipped row is the unique legitimate clipped row if neither saturation sign supports a nonzero \(+1\) or \(-1\) Jacobi eigenrow. A sufficient condition is that each saturation sign contains less than \(n/\sqrt p\) sites, by the pointwise bound \(\|g\|_\infty\le(\sqrt p/n)\|g\|_1\) for any such eigenrow. A stronger arithmetic test is available for a large prime divisor \(\ell\) of \(n\). The same nonzero-coset restriction as in [round 89](astra-tails-89.md#prime-divisors-of-the-cyclic-order-at-a-singular-contact) gives \(|D_\sigma|\ge1+(\ell-\sqrt p)/2\) for any sign that actually changes. This test concerns full clipped uniqueness rather than invertibility of the original complex equation.

The separate total defects \(E_\sigma=\sum_{\operatorname{sign}(\Im U_i)=\sigma} e_i\) are equal for all these fixed points. Off \(D_\sigma\), the defect does not change in the corresponding sign. Let \(X=a\Re U^{(2)}\), \(Y=\Im U^{(2)}\). On \(D_\sigma\), the defect difference is a fixed positive multiple of \(2(Yh-Xf)+h^2-f^2\). The quadratic sum vanishes by orthogonality of the two just obtained opposite eigenrows. For the linear term, on the same set \(a\Re S^{(2)}=\sigma Y\), and \(X=K(a\Re S^{(2)})\) globally. Pairing with the restricted \(\sigma\)-eigenrow gives \(\langle X-Y,1_{D_\sigma}(f+h)\rangle=0\). Pairing with the opposite eigenrow gives \(\langle X+Y,1_{D_\sigma}(f-h)\rangle=0\). These two identities cancel the linear sum. Thus the two canonical nonnegative corrections can be studied individually, even if the bulk rows are nonunique.

## A quantitative defect when the genuine row exceeds the cap

Take any true unforced row at the same \(t\) and any clipped row, on the positive mean sheets. Let \(E_*=\sum_{i\ne0}e_i\) for the clipped solution. Suppose the summed relative phases of the two rows admit an orientation \(\beta\) with \(\cos\beta\ge0\) and every rotated cosine at least \(c>0\). Suppose a true bulk phase has magnitude \(\vartheta+g\) or more for some \(g>0\), and all phase differences considered have magnitude at most \(\pi\).

Apply the [Hermitian two-floor expansion](physical-two-floor-88.md#the-signed-secant-with-the-physical-means-retained) coordinatewise with both product changes present. At the mark there is no change of explicit weight. On the bulk write \(s_i=(1+\sqrt{1+e_i})/2\), \(b_i=(\sqrt{1+e_i}-1)/2\). Put \(X_i=|\sinh((z_i-z_i^{\rm clip})/2)|\), \(Q=\sum_i|s_i|^2 X_i^2\), with the unchanged marked square root used at the mark. The normalized factor differences have their true means, so the rotated mean term is nonnegative. If \(r=\max_i|b_i/s_i|\) and \(B=(\sum |b_i|^2)^{1/2}\), the exact expansion and \(|\cosh d|\le1+|\sinh d|\) give
\[
                  (c-r^2-2r)Q\le B^2+2B\sqrt Q .
\]
Here \(\sum c_i |b_i|^2|\cosh d_i|^2\le B^2+r^2Q\), using \(|\cosh d|^2\le1+|\sinh d|^2\); the cross terms give the stated two remaining terms. If \(E_*\le c/2\), then \(r\le E_*/4\le c/8\), \(B\le E_*/4\), and \(Q\le20 B^2/c^2\) by Young's inequality. At an overshooting site \(s_i\ge1\) and \(X_i\ge\sin(g/2)\). In all cases this proves
\[
            E_*\ge \min\{c/2,\ 4c\sin(g/2)/\sqrt{20}\}.                \tag{1}
\]

At \(p=173\), \(t=1/50+0.02161i\), use the actual branch validated in [round 86](astra-phase-86.md). For \(a=1/\sqrt2\), the upper phase exceeds \(\arctan a+0.28\), the true spread is below \(\pi/2+65\cdot0.00003\), and all absolute phases are below \(\arctan(3/2)\). The clipped spread is at most \(2\arctan a\), including the mark since \(|\arg t|/2<\arctan a\). The midpoint of the summed extremes therefore gives \(c>1/7\). It also has \(\cos\beta>0\) because the mark has summed absolute phase smaller than \(0.85\) and all summed phases have magnitude below \(1.6\). Formula (1) yields \(E_*>1/60\) for every legitimate clipped solution at this point. This is a finite obstruction at the stated small floor. [Outward interval check](clipped-signs-90-check.py) · [Replay](clipped-signs-90-checks.jsonl)

1. Estimate the two canonical nonnegative defect masses at the nominated cold center, beginning with the shared support constraints from the two signs of the Jacobi eigenrows.
2. Test whether the actual marked-column and predictor estimates exclude the support of both defects through primes. The finite obstruction does not decide a prime-uniform cold section or the ordinary-theta limit.
