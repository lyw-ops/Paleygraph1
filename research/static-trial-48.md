# Exact harmonic dual for the cold static trial

The [static trial](astra-stencil-48.md#a-static-trial-criterion-for-the-square-separating-node) for the 128-hot-node stencil has an exact dual involving only an opposite-sector row and a bulk harmonic constraint. This gives finite upper certificates for the trial optimum. At prime 173 the actual cold mark at \(a=1/2\) passes the limiting stencil's cold-node tolerance, while the minus static trial has a certified deficit larger than \(0.028\). This separates the sufficient trial from its scalar target already at a prime. The statement uses the cold value alone and makes no finite claim about adding the ill-conditioned hot coefficients.

## Duality

Use \(E=n^{-1}\sum_i\), \(E_b=n^{-1}\sum_{i\ne0}\), \(W_a=1+(1-1/n)a\), and \(R=e^{-B}\sqrt{n/W_a}\), where \(B\) is a fixed measure budget. In the sign-\(\sigma\) cone let

\[
 Z_\sigma(B)=\max_{\ell\in U_\sigma,\ \ell\ge0,\ E\ell=1}
 \left[\frac{\ell_0}{R}+a(E_b\sqrt{\ell})^2\right].
\]

Then

\[
 Z_\sigma(B)=
 \inf\{ E g:\ g\in U_{-\sigma},\ g_0\ge n/R,\quad
             g_i>0\ (i\ne0),\quad aE_b(1/g)\le1\}.
 \tag{1}
\]

For any such \(g\) and any primal \(\ell\), Cauchy–Schwarz gives
\((E_b\sqrt\ell)^2\le E_b(g\ell)E_b(1/g)\). Therefore
\(\ell_0/R+a(E_b\sqrt\ell)^2\le E(g\ell)=Eg\) by complementary-sector orthogonality. This direction alone certifies a deficit.

For equality, represent \((E_b\sqrt{\ell})^2\) as
\(\inf_{h_i>0,\ E_b h=1} E_b(\ell/h)\). The equality in Cauchy–Schwarz is achieved by \(h\) proportional to \(\sqrt\ell\) when all entries are positive and by approximation otherwise. The compact convex primal set and the positive convex \(h\)-set satisfy the continuous concave-convex minimax hypotheses, so the maximum and infimum interchange. For each \(h\), the remaining linear maximum over \(\ell\) has the dual constraint \(g_0\ge n/R,\ g_i\ge a/h_i\) off the mark, with objective \(Eg\). Such an \(h\) exists for a given \(g\) precisely when \(a E_b(1/g)\le1\), by padding \(a/g\) with a nonnegative constant. This proves (1). Both variational values are unchanged by even symmetrization, using concavity of the primal objective or convexity of the reciprocal constraint.

## The actual budget of the fixed stencil

Use the [round-47 stencil](seed-majorant-47.md#a-shorter-square-control-for-the-real-measure-budget) with \(J=128,T=32,a=1/2\), and \(x_i=1-i/[5(J+1)]\). Write \(d=(a/T)^2\), \(z_*=(1-d)^{-1}\), \(D(z)=\prod_i(1-(1-x_i)z)\), and \(r=(T-a)/(T+a)=63/65\). Its exact limiting budget has the integral

\[
 B=\frac{1-d}{\pi T_J(2z_*-1)}
 \int_0^{\pi/2}
 \frac{\sin\theta\cos\theta}{\sin^2\theta+d\cos^2\theta}
 \,|\cos(2J\theta)|\,\frac{D(z_*)}{D(\cos^2\theta)}
 \arctan(T\tan\theta)\,d\theta .
\]

This follows by putting \(s=\tan^2\theta\), \(z=(1+s)^{-1}\) in the absolute residual kernel from the Chebyshev interpolation proof. The endpoint value of the arctangent is taken by continuity. The denominator \(T_J(2z_*-1)=(r^{-J}+r^J)/2\). Direct Arb interval integration across 16,384 subintervals gives \(0.017<B<0.0195\). The finite-field measure densities are pointwise no larger than the limiting density, so the same upper bound works there.

## Certified separation at finite primes

The [checker](static-trial-48-check.py) uses \(B=0.0195\) for the harmonic dual, so its costs bound \(Z_\sigma(B_{\rm actual})\) from above by monotonicity in \(B\). A numerical optimizer suggests cosine coefficients. The certificate uses only a rounded rational vector in the opposite Fourier sector, a rational scale, and interval inequalities verifying positive coordinates, the mark, and the harmonic constraint in (1). It verifies the saved duals without calling the optimizer in replay mode.

The certified lower deficits \(W_{1/2}-Z_\sigma(B_{\rm actual})\) include \(0.115\) at prime 101 plus, \(0.028\) at prime 173 minus, \(0.078\) at prime 281 plus, \(0.024\) at prime 401 plus, and \(0.168\) at square 121 minus. An independent actual positive-factor chart via the [round-45 checker](astra-strip-45-check.py) encloses \(m_{173}(1/2)\) around \(0.0152217148250\), strictly below \(0.017\). Thus the cold physical estimate already holds in this example, and the minus trial criterion loses genuine slack. These finite deficits establish neither eventual prime failure of the trial nor any asymptotic claim about the scalar marks.

The [seven records](static-trial-48-checks.jsonl) replay with the repository Python interpreter and the saved input.

~~~sh
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 \
  .venv/bin/python -B research/static-trial-48-check.py \
  --replay research/static-trial-48-checks.jsonl
~~~
