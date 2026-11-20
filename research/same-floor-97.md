# A same-floor real reference for the first comparison boundary

At the first activation of the near-flat comparison on the nominated square, freeze the real reflection at the real parts of the complex height-100 predictor on that **same** floor. The scaled bulk entries of its marked column have uniform limsup below 92, and the scaled maximum of its off-diagonal entries has limsup below 182. The actual midpoint tilt from this reference has normalized Hellinger norm at most twice the *complex predictor residual*. At this height the latter is below \(3\cdot10^{-30}\), much below the tilt budget of the reference on the real axis. At sufficiently large eligible primes a first activation still requires a signed singleton exterior sum above \(7.55\cdot10^{-5}\). The new reference puts the unknown exterior contribution entirely on the genuine stationary discrepancy from the complex predictor.

## Transporting the nominal real reflection

Write \(t=T+iy\), \(L=2031/128-2^{-17}\), \(h=2^{-17}\), \(t_0=n\) and \(t_i=t\) otherwise. Let \(W_j=V_j(t)\) be the actual nine-center prefix and \(g_j=\operatorname{arsinh}(W_j/(2\sqrt{t_i}))\). The proposed real trial diagonal in log coordinates is \(\Gamma_i=\Re g_{100,i}\) on the bulk. At the mark put \(\theta=-\arg(t)/2\) and
\[
   \Gamma_0=\Re g_{100,0}+\tfrac12
      \log\frac{\cos(\theta+\Im g_{100,0})}{\cos(\theta-\Im g_{100,0})}.
\]
Thus \(\Gamma\) consists of the half-log ratios of the real parts of the two exact-product *predictor* factors in the normalization of [round 96](astra-count-96.md). The factors need not be complementary here. Their real reflection \(R^\Gamma=M(I-K D_\Gamma)^{-1}KM-D_\Gamma\), \(D_\Gamma=\tanh\Gamma\), \(M=\operatorname{sech}\Gamma\), is well defined by the [arbitrary trial diagonal formula](response-locality.md).

We first check a representation bound for the actual time derivative of the predictor. Work in the base Mellin pair, with the fixed price \(\pi\) of [round 82](astra-adjoint-82.md) on negative fields. The seven nonconstant amplitude groups of \(V_0\) have total dimensional mass below \(1.1\) on the square of half-width \(1/4\) around the nominated center. The Jacobi seed is independent of \(t\). The same rank bounds hold for the finitely corrected actual center fields, whose extra rank cost is \(O(n^{-1/2})\) by [round 76](astra-predictor-76.md). Direct evaluation of the amplitude formulas on the larger square, with their signs left free, gives the initial bound \(\|\partial_t V_0\|_\pi<9\) on the nominated square by Cauchy and \(\pi(k)\le2k\).

For \(j\le99\), the arithmetic operator \(KD_j\), \(D_j=\operatorname{diag}\Phi'_t(W_j)\), has price rate at most \(q=0.984138\). Indeed the round-82 comparison uses increasing envelopes through height 100. The direct time source for the bulk is \(2/\sqrt{4t+W_j^2}\), and is zero at the mark. The leading constant is killed by \(K\) after correcting the marked entry. Set \(\eta=4.8^2/(4L)\). After applying \(K\), the remaining binomial degrees have price at most
\[
   \frac{4}{\sqrt L}\sum_{\ell\ge1}
           \ell\left|{\textstyle-1/2\choose\ell}\right|\eta^\ell+O(n^{-1/2})
      =\frac{2\eta}{\sqrt L(1-\eta)^{3/2}}+O(n^{-1/2})<0.36
\]
for sufficiently large eligible primes. In fact the dimensional mass and first absolute weight before application of a \(2\ell\)-fold product are at most \(4.8^{2\ell}\) and \(2\ell\,4.8^{2\ell}\), by the [negative rank identity and weight convolution](astra-feedback-52.md). The geometric transport keeps nonzero weights, so the price is at most twice the first weight. The bad coordinate and explicit marked change contribute the stated error by the exact marked-column estimate. Differentiating the true recurrence therefore gives
\[
             \|\partial_t V_{100}\|_\pi
                   \le 9q^{100}+0.36(1-q^{100})/(1-q)<21.              \tag{1}
\]

For the next calculation denote by \(m(f)\) and \(b(f)\) upper sums of the absolute coefficients times the dimension and the first absolute weight before transport, respectively. Under sums and products use the corresponding subadditivity and the bounds \(m(fg)\le m(f)m(g)\), \(b(fg)\le m(f)b(g)+b(f)m(g)\), from the fiber tensor rule. For a real-even or real-odd power series \(F\) put \(F_{\mathrm{abs}}(x)=\sum |[z^\ell]F|x^\ell\). For \(m(f),m(g)\le A\), \(b(f),b(g)\le B\), telescoping each power in \(F(f)-F(g)\) bounds its mass by \(F_{\mathrm{abs}}'(A)m(f-g)\) and its first weight by
\[
       F_{\mathrm{abs}}'(A)b(f-g)+B F_{\mathrm{abs}}''(A)m(f-g).
\]
This calculation can first be performed on finite expressions, with the exact finite-field corrections at the single marked coordinate applied after transport. The power tails used here are absolutely summable. Conjugation keeps the two base Mellin fibers, and all the odd powers used below remain odd words in negative factors.

Apply this to \(W_{100}/(2\sqrt t)\) on the unmarked formula and its value at \(T\). Both their mass and first weight are below \(0.61\). Their actual difference is represented with both bounds below \(2.1\cdot10^{-5}\), by integrating (1) and the derivative of \(1/(2\sqrt t)\) along the vertical segment. The geometric series can be evaluated at the mark with the bulk formula before restoring the marked derivative. For \(\operatorname{arsinh}\) the absolute series is \(\arcsin\), and for \(\tanh\) it is \(\tan\). Thus the change from the real-axis multiplier to \(D_\Gamma\) has \(2(m+b)<0.00032\) in the bulk formula. For a negative test factor of price \(P\), the change after \(K\) costs at most \(2(m+b)P+O(n^{-1/2})P\), by the product first-weight bound and the fact that both its mass and its first weight are at most \(P\). The nominal marked entry is a separate bounded correction at zero, again costing \(O(n^{-1/2})P\). Hence the base rate of \(K D_\Gamma\) is eventually below \(0.9845\).

This multiplier has precisely the parity, absolute-mass and first-weight hypotheses of the [translated-source transport](shifted-resolvent-96.md#the-two-estimates-for-one-physical-derivative-step). For \(Z=(I-K D_\Gamma)^{-1}K\), its triangular bound gives scaled limsups below \(92\) on the marked column and \(182\) on all entries, uniformly on the square. These estimates pass to the bulk marked column and the off-diagonal entries of \(R^\Gamma\), respectively. On the bulk \(|D_{\Gamma,i}|\le 4.768/\sqrt{4L+4.768^2}<0.514\) since \(\sinh^2(\Re g_i)\le|\sinh g_i|^2\). The diagonal contribution from \(Z\) is \(O(n^{-1/2})\), so \(|R^\Gamma_{ii}|<0.515\) on the bulk eventually.

## The actual first-boundary lag is residual-scale

At a first threshold the actual pair is exact and has unit bulk products by [round 96](astra-count-96.md#stop-at-the-first-boundary-of-the-selected-real-profile). Let \(z_i\) be its complex relative log in the physical scaling and put \(g=g_{100}\). Let \(U_i=2\sqrt{t_i}\sinh z_i\), \(\Delta=U-W_{100}\), \(R=K\Phi_t(W_{100})-W_{100}\) and \(r=\|R\|_{2,n}\). At the bulk hit \(|X_i|=10^{-4}\), and \(|X_j|\le10^{-4}\) on the entire bulk. The real-factor projection gives \(|\sin\Im z_j|=|X_j|/\sqrt3\) off the mark. Both marked absolute phases of the normalized pair have the same weak sign, since their tangent values are \(v(1\pm c_0)/(2w_0)\). Hence the relative phase at the mark also lies in the strict sector. The initial phase of \(g\) is bounded by \(0.26\) by the genuine predictor coordinate bounds.

Put \(D_i^{\rm sec}=\tanh((z_i+g_i)/2)\). The squared secant equation at the true endpoint gives the [round-84 loss comparison](phase-action-84.md#exact-secant-comparison-in-logarithmic-coordinates), which uses only the equation at the two rows and the phase caps:
\[
 \mathbb E\min(|\Delta|^2,|\Delta|)\le462r^2,\qquad
 \mathbb E(1-|D^{\rm sec}|^2)|\Delta|^2
      \le 2(\sqrt{462}+462\|R\|_\infty)\,r^2<45r^2 .
\]
Here \(\|R\|_\infty<0.001180\), and \(r\le0.169724(0.51358)^{100}<3\cdot10^{-30}\), by the actual height-100 increment estimates. By the hyperbolic sum identity, the loss on the left is exactly
\[
 16\,\mathbb E_i |t_i|\cos(\Im z_i+\Im g_i)
                 \left|\sinh((z_i-g_i)/2)\right|^2 .
\]
This yields a bulk normalized \(L^2\) bound \(<1.2r\) on \(2\sinh((\gamma-\Gamma)/2)\). Indeed \(\gamma_i=\Re z_i\) on the bulk, the cosine factor exceeds \(1/2\), and \(|\sinh \Re w|\le|\sinh w|\). At the mark, the same loss gives \(|z_0-g_0|<8r\), since both log phases there are small and \(|\sinh w|^2=\sinh^2\Re w+\sin^2\Im w\). The map from the complex log to the midpoint real log at that coordinate is uniformly Lipschitz with constant at most \(2\), by the above cosine formula. In particular \(|\gamma_0-\Gamma_0|<16r\) and the full **normalized** real half-log Hellinger norm is \(<2r\).

## Necessary signed exterior cost with the tilted reference

Use the finite real response identity of [round 96](astra-count-96.md#remove-the-entire-observed-block) with \(\Gamma\) in place of the real-axis predictor. Write \(F_j=\sinh(\gamma_j-\Gamma_j)X_j\) on the bulk. At a hit \(i\), removing its diagonal and the explicit marked source now gives
\[
  \operatorname{sgn}(X_i)\sum_{j\notin\{0,i\}} R^\Gamma_{ij} F_j
   \ \ge\ \sqrt{1-|R^\Gamma_{ii}|^2}\,10^{-4}
           -e^{16r}\sqrt{3B/n}\,92
   \ >\ 7.55\cdot10^{-5}.                                             \tag{2}
\]
Here \(\sqrt{3B/n}\le \sqrt3 h/(2L^{3/2})\). Thus the exterior counting first norm is at least \(4.14\cdot10^{-7}\sqrt n\) at each such hit. On the other hand the half-log bound yields \(\|F\|_{1,n}\le 2 r\sqrt{3B/n}+2\cdot10^{-4}r^2\). This uses \(|\sinh x|\le |2\sinh(x/2)|+(2\sinh(x/2))^2/2\). In particular at these first activations one needs \(\sqrt n\,r>1.9\). The two estimates apply eventually through eligible primes. They do not imply a growing-depth bound on \(r\) or rule out the signed cost in (2). [Arb arithmetic checker](same-floor-97-check.py) · [Replay](same-floor-97-checks.jsonl)

### Delete the largest actual lag entries

The [growing erasure identity](astra-signed-97.md#keep-the-specified-first-hit-site) applies also with this reference. To see the resulting scale, write \(E_j=\tanh\gamma_j-D_{\Gamma,j}\) and \(V_j=\cosh\gamma_j X_j\) in that identity, so \(|E_j|<1.514\) on the bulk. Use \(Z=(I-KD_\Gamma)^{-1}K\). For any bulk \(S\) of size at most \(\sqrt n/500\) containing the hit \(i\), the absolute row sum of \(Z_{SS}\operatorname{diag}E_S\) is at most \(q_s=182(1.514)/500<1\) eventually. The Schur-compensated signed row has output at least \(10^{-4}-92e^{16r}\sqrt{3B/n}/(1-q_s)\). Its difference from the singleton row is the product of the inverse row and \(Z_{SS}\operatorname{diag}E_S\), of counting second norm at most
\[
              \frac{182(1.514)}{(1-q_s)\sqrt{500}} n^{-1/4}.
\]
Put \(O=(S\cup\{0\})^c\). The ordinary signed singleton \(\operatorname{sgn}(X_i)(R^\Gamma)_{iO}F_O\) differs from the compensated test after multiplication by the diagonal factors \(\operatorname{sech}\Gamma\). As in round 97's erasure identity, those factors cost at most \(1/\sqrt{1-0.514^2}\) on \(S\), and the full reflection contracts in counting second norm. It follows that if the ordinary signed singleton is at most \(5\cdot10^{-5}\), then \(\|F_O\|_2>6\cdot10^{-7}n^{1/4}\).

Take \(S\) to include \(i\) and the \(\lfloor\sqrt n/500\rfloor-1\) largest absolute entries of \(H=2\sinh((\gamma-\Gamma)/2)\) off the mark and \(i\). The surviving maximum is at most \(2\sqrt{501}\,r n^{1/4}\), by the normalized bound \(2r\) and the count of erased sites. Since \(F_j^2=X_j^2(H_j^2+H_j^4/4)\), the exterior counting norm is at most \(2\cdot10^{-4}r\sqrt n\sqrt{1+501r^2\sqrt n}\). We therefore obtain the additional necessary alternative
\[
  \operatorname{sgn}(X_i)(R^\Gamma)_{iO}F_O>5\cdot10^{-5}
  \quad\text{or}\quad n^{1/4}r>0.0029 .
\]
The second option concerns the actual complex residual at the same floor. A sufficiently precise growing-depth predictor would still need the first-option signed estimate.

1. Estimate the signed sum in (2) under the true complex secant identity, retaining \(\gamma-\Gamma\) rather than the larger geometric tilt relative to the real axis.
2. Repeat the same-floor derivative control at a higher prefix or a corrected Newton reference, measuring both the base packet rate and the required singleton signed margin.
