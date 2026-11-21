# Exact spectrum of the conditional reciprocal triple

Use the actual projected source and normalized stationary laws of [Round 120](reflected-offmark-cubic-120.md). The proof here applies to the true reflected pair or complete slab in its stated critical cap-rate branch. Let \(a,b,c\) have respective signed/product laws \(\pi_*,\omega,\omega^-\), where \(\pi_*\) can be signed, has mass one and bounded total variation. Write \(e=a-b\), \(d=c-b\), and let \(B(e,d)=n^{-1}\sum_b\xi_d(b)\pi_*(b+e)\), \(\xi_d(b)=n\omega_b\omega^-_{b+d}\). Thus \(B\) is the signed pair law of \((e,d)\). The pair laws of both \(d\) and \(d-e\) are exactly uniform: the two relevant sources are in the favored sector plus constants and the other factor is in the opposite sector plus constants. This applies to the signed \(\pi_*\) by linearity.

## Exact conditional Fourier constraint

For positional \(v,w\in Q\), use the unnormalized Fourier coefficients of laws given by multiplication against \(e(v)d(w)\). Then
\[
 \widehat B(v,w)=\widehat{\pi_*}(v)\widehat\omega((vw)^{-1})\widehat{\omega^-}(w).
\]
This follows by substituting \(e=a-b,d=c-b\), so the three factors really are those of the genuine three inputs. Let \(B_e\) denote the first marginal and put \(B^\circ(e,d)=B(e,d)-B_e(e)/n\). Then all three pair marginals in \(e,d,d-e\) vanish, and the nonzero positional coefficients of \(B^\circ\) lie in
\[
           s(v)=s(vw)=\epsilon,\qquad s(w)=-\epsilon,\quad
           v,w,vw\ne1.
\]
The constant cases have been accounted for by the exact pair laws. The two-dimensional Fourier expansion of the complete translated kernel is
\[
 T_3(e,0,d)=p^{-3/2}\sum_{v,w\in Q}s(v)s(w)s((vw)^{-1})
                        \overline{e(v)d(w)}.
\]
It follows either by orthogonality in the full output coordinate or from the three separate Jacobi expansions. Since \(s(1)=0\), the contraction against \(B_e(e)/n\) is zero, even when the first marginal is concentrated. On the displayed support of \(B^\circ\) the multiplier is exactly \(-\epsilon\). In particular the complete, unmasked unrestricted contraction has no hidden as-yet-unknown sign estimate: with the usual scalar prefactor it agrees exactly with
\[
              -\mathbb E_n[(q_*-m)(g-\mu)(g_--\mu)].
\]
The arithmetic difficulty arises when one retains the correct collision removal and joint masking, or when using the actual repair geometry to estimate a residual. The two uniform marginals do not make the remaining signed pair law a product.

## Deleted output is a factorized main term, not a pointwise conditional loss

With \(D(e,d)=\sum_b\xi_d(b)\pi_*(b+e)k(-b-e)k(-b)k(-b-d)\), the deleted-output contribution to the normalized triple-law contraction is \(n^{-2}\sum_{d\ne0,\ e\notin\{0,d\}}D(e,d)\). The two powers of \(n\) arise from the uniform difference and the single-output average. Define \(J_0(\sigma)=\sum_y\sigma_y k(-y)\) for a law \(\sigma\). Then
\[
 \frac1n\sum_{d\ne0,\ e\notin\{0,d\}} D(e,d)
    =J_0(\pi_*)J_0(\omega)J_0(\omega^-)+O(n^{-1/2}).                \tag{1}
\]
Without distinct deletion this is exactly the factorization of three independent draws. The removed collision mass in total variation is \(O(n^{-1/2})\) by the bounded absolute total mass and maximum atom bounds. This controls the error in (1) without a pointwise sign assumption. In particular \(|D(e,d)|\le\max|\pi_*|=O(n^{-1/2})\) individually since \(\xi_d\) is nonnegative with total mass one. This pointwise bound does not suffice to treat the entire two-index sum as a little-oh correction.

In actual coordinates, multiplying (1) by the cubic prefactor \(\epsilon(\sqrt p)^3m\mu^2\) gives \((\epsilon K q_*)(0)(Kg)(0)(Kg_-)(0)+O(n^{-1/2})\), with the extra \(1/n\) still required to obtain the deleted-output term in the observable. Thus the aggregate can be critical and is independently explicit. No estimate forcing this factorized term alone to vanish is required: it cancels the exceptional output term in the joint observable of Round 120.

The true conditional coefficient before multiplying by the three kernels is \(\xi_d(b)\pi_*(b+e)=q_*(b+e)g(b)g_-(b+d)/(n^2m\mu^2)\). No additional favored factor at \(b+e\) occurs. The bounds for the separate law \(w_*=q_*g/(n\mathbb E_n(qg))\) from Round 117 must not be transferred to the variation of \(\pi_*\); the available bound on that variation is \(O(1)\). A prime-uniform gain for the full masked distinct cubic still needs a genuinely joint estimate using the actual repair source or another exclusion of the underlying branch.
