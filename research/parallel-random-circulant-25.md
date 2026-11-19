# Random circulant Gaussian trees and the Paley arithmetic fields

The deterministic smoothing and residual certificate of Chen et al. applies to our Paley operator. The Gaussian tree comparison has different low-degree limits. A transfer also needs control of positive Fourier-kernel vectors. [Chen et al., §§4, 7–10 and Proposition 11.1](https://arxiv.org/html/2610.22971v1)

Write \(n=(q-1)/2\), \(K=F\operatorname{diag}(s)F^{-1}\), \(s(x)=\chi(1-x)\), and \(U=\sqrt n Ke_0=\lambda/\sqrt n\). All statements below use the actual Paley signs.

## The first two Gaussian tree normalizations fail

The leaf has limiting arcsine law on \([-\sqrt2,\sqrt2]\). The [Legendre joint law](parallel-graph-shapes-23.md#classical-independence-of-the-first-two-matrices) also identifies the first even feedback. Put \(X=\lambda/\sqrt q\) and \(Z=K(2X^2-1)\). Then

$$\mathbb E_n U^2\to1,\qquad \mathbb E_n U^4\to\frac32,\qquad K(U^2-1)=\frac{q}{2n}Z.$$

Here \(\mathbb E_n\) means the coordinate average. The limit of \(Z\) is \((t_1+t_2)/2\), where \(t_1,t_2\) are independent Haar \(SU(2)\) traces. They have second moment one and fourth moment two. Consequently

$$\mathbb E_n[K(U^2-1)]^2\to\frac12,\qquad
\mathbb E_n[K(U^2-1)]^4\to\frac58.$$

The Gaussian leaf has fourth moment three. Its Hermite square has variance two, whereas the Paley first graft has variance one half. Even after adjusting the graft variance, its standardized fourth moment is \(5/2\). The Paley leaf and first graft have limiting fourth cumulants \(-3/2\) and \(-1/8\), respectively. These discrepancies persist at prime-square orders.

Thus changing the leaf marginal alone leaves a further obstruction to Gaussian graft coordinates. The Mellin convolution objects provide the arithmetic replacement. The [fixed-width proof](parallel-fixed-width-13.md) already handles fixed expressions and their even nonlinear feedback in normalized \(\ell_2\). Uniform estimates for growing expressions remain necessary for the endpoint.

## The residual certificate and its exact stationary cost

The deterministic proof uses symmetry of \(K\) and \(K^2=I-J\), and therefore also covers the even values of \(n\) occurring here. For \(w_0=1\), \(w_i=\tau/n\) off the mark, \(W=\sum w\), and \(\Phi(v)=\sqrt{v^2+4w}\), let \(f^*=K\Phi(f^*)\). With \(r=v-K\Phi(v)\) and mean-zero even \(v\), it gives

$$\left|\log\frac{\theta_+}{\sqrt n}-\operatorname{arsinh}(v_0/2)\right|
\le\frac12\log W+
\sqrt{(\|v\|_2+\tfrac12\|f^*\|_2)\|r\|_2}.$$

This certificate and the elementary bound \(\|f^*\|_2=O_\tau(q^{1/4})\) already appear in [the iteration note](iteration-parity.md#the-remaining-analytic-limit). Their combination makes \(\|r\|_2=o(q^{-1/4})\) sufficient at bounded trial norm and vanishing marked trial value, with fixed \(\tau\) before the field limit.

For the random graph, the proof uses a simultaneous kernel bound to make the stationary norm polylogarithmic. [Chen et al., Proposition 5.4 and §11](https://arxiv.org/html/2610.22971v1#S11) On square orders \(q=t^2\), the probability row \(\mathbf1_I/h\), \(h=(t+1)/2\), satisfies

$$\frac{\|\mathbf1_I/h\|_2}{\|\mathbf1_I/h\|_1}=h^{-1/2}\asymp n^{-1/4}.$$

A kernel bound of order \(\operatorname{polylog}(n)/\sqrt n\) for this ratio fails on that row. This is a separate arithmetic requirement from a comparison of finite polynomial fields.

There is a corresponding quantitative obstruction directly in the residual. On square plus \(\theta_+=t-1\), so \(\theta_+/\sqrt n\to\sqrt2\). Fix \(0<\tau<1\). For any mean-zero even trials with \(\|v\|_2\le C\) and \(v_0\to0\), the left side of the residual bound tends to \(\frac12\log2\), while its smoothing term is at most \(\frac12\log(1+\tau)\). Therefore

$$\liminf_{t\to\infty}q^{1/4}\|v-K\Phi(v)\|_2>0.$$

For an explicit constant, the point cap \(p_i\le (\sqrt q+O(1))\sum p/n\) in either positive sector gives \(\|f^*\|_2\le C_\tau q^{1/4}\). Insert this estimate and half the positive gap \(\frac12\log[2/(1+\tau)]\) into the displayed certificate. Bounded-energy approximants with a small marked coordinate therefore cannot attain a residual smaller than the critical power on this square sequence.

## A contraction criterion that also applies to arithmetic fields

The Gaussian contraction can be replaced by a mixed-moment hypothesis. Let \(D=Y-X\), \(X_s=(1-s)X+sY\), and suppose

$$\mathbb E[D^2X_s^2]\le A\,\mathbb E D^2\qquad(0\le s\le1).$$

For \(\phi_\tau(x)=\sqrt{x^2+4\tau}\), weighted Cauchy–Schwarz gives

$$\mathbb E\frac{D^2}{X_s^2+4\tau}\ge
\frac{(\mathbb E D^2)^2}{\mathbb E[D^2(X_s^2+4\tau)]}
\ge\frac{\mathbb E D^2}{A+4\tau}.$$

Use \(\phi'_\tau(x)^2=1-4\tau/(x^2+4\tau)\), integrate its derivative along the segment, and apply Cauchy–Schwarz once more. This proves

$$\mathbb E|\phi_\tau(Y)-\phi_\tau(X)|^2
\le\frac{A}{A+4\tau}\mathbb E|Y-X|^2.$$

The result holds on a finite coordinate probability space as well. A uniform bound of this form for the arithmetic nonlinear fields would replace the Gaussian step in a contraction argument. Fixed-expression Mellin estimates currently give no bound on \(A\) uniform in depth. The stationary norm or residual-pairing requirement above would still have to be met.

## Replay

The [script](parallel-random-circulant-25.py) records the two fields' second and fourth moments, checks the exact Fourier energy identities, and compares the deterministic residual formula with numerical stationary references at eight small-order/sign inputs. The [records](parallel-random-circulant-25.jsonl) are floating-point checks.

```sh
.venv/bin/python -B research/parallel-random-circulant-25.py > research/parallel-random-circulant-25.jsonl
```
