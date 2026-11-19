# Exact signed extrapolation and the cost of an anchored finish

Two fixed positive widths can cancel the entire forbidden Gram matrix for actual reciprocal rows in a coherent circulant reflection model. The example is the full additive Paley graph. Thus reflection, coherence, complementary KKT identities, and fixed-width scalar balance alone cannot exclude successful signed extrapolation. For the 1-localized Paley target, the additional Gram and positivity constraints remain arithmetic questions.

## A two-width construction with zero projection cost

Let \(N\equiv1\pmod4\) be a prime, index by \(\mathbb F_N\), and set

$$K_{xy}=\chi(x-y)/\sqrt N,\qquad J=\mathbf1\mathbf1^{\mathsf T}/N,
\qquad P_\pm=(I-J\pm K)/2.$$

Then \(K=K^{\mathsf T}\), \(K^2=I-J\), \(K\mathbf1=0\), and every entry has magnitude at most \(N^{-1/2}\). The identity for the square follows by the elementary quadratic character correlation sum. Put \(C_\pm=\{x:\chi(x)=\pm1\}\). For \(0<r<1\), define

$$d_r=\frac{1-r}{1+r},\qquad
t_r=\frac{2d_r}{\sqrt N+d_r},\qquad
y_r=e_0+t_r\mathbf1_{C_-},\quad
x_r=e_0+t_r\mathbf1_{C_+}.$$

These are the actual reciprocal anchored minimizers. Indeed \(x_ry_r=0\) off the mark and \(x_{r,0}=y_{r,0}=1\). Also

$$x_r-y_r=t_r\chi
=d_rK(x_r+y_r),\qquad
x_r+y_r=t_r\mathbf1+(2-t_r)e_0.$$

They have the same mean. Resolving the reflection identity on \(J,P_+,P_-\) gives

$$x_r=(J+rP_-+r^{-1}P_+)y_r.$$

The two sides are nonnegative, and the off-mark complementary products vanish, so the strictly convex quadratic KKT conditions hold. The reciprocal values are both exactly one.

At \(r=0\), put \(t_0=2/(\sqrt N+1)\). The same identities give

$$P_+y_0=0,\qquad y_0\ge0,\qquad (y_0)_0=1,
\qquad \sum y_0=\sqrt N.$$

For any two fixed widths \(0<r<s<1\), set

$$\alpha=\frac{t_0-t_s}{t_r-t_s},\qquad
\beta=1-\alpha.$$

Then \(\alpha>1\), \(\beta<0\), and

$$\alpha y_r+\beta y_s=y_0.$$

The coefficients stay bounded as \(N\to\infty\), since \(\alpha\to(1-d_s)/(d_r-d_s)\). Every forbidden vector \(P_+y_r\) is collinear with \(P_+e_0\), because \(P_+\mathbf1_{C_-}=-P_+e_0/t_0\). Thus scalar cancellation also cancels the full Gram matrix. For any prescribed mark \(a\sqrt N\) and mean \(\mu\ge a\), the padded source

$$Z=a\sqrt N\,y_0+(\mu-a)\left(\mathbf1-
\frac{P_-e_0}{(P_-)_{00}}\right)$$

is nonnegative and already in the exact affine slice. Its projection cost is zero.

The field and the operator here differ from the 1-localized Paley operator. The calculation shows why a fixed-width signed obstruction needs further properties of the localized arithmetic fields. In particular, the positive-mixture lower bound from [the fixed-width seed note](astra-seed-25.md) cannot be extended to signed mixtures using only its scalar identities.

## A quantitative source-cost-to-finish statement

Now use the actual localized geometry from [anchored repair](anchored-repair-20.md). Let \(P\) be the allowed nonconstant projector, \(F=I-J-P\), \(\ell=Pe_0\), \(\kappa=\ell_0\), \(L=P-\ell\ell^{\mathsf T}/\kappa\), and \(M=\mathbf1-\ell/\kappa\). Assume the off-mark padding is positive and use the established nonnegative rows

$$W^{(i)}=M+\eta Le_i,\qquad h_i=W^{(i)}_i>0.$$

Let \(Z\ge0\) have mark \(a\sqrt n\) and mean \(\mu\). Its nearest affine projection is

$$Y=Z-FZ+\frac{(FZ)_0}{\kappa}\ell,\qquad
D^2=\|Y-Z\|_2^2=\|FZ\|_2^2+\frac{(FZ)_0^2}{\kappa}.$$

Write \(E=(-Y)_+\) off the mark. Then \(\|E\|_2\le D\). Choose a minimizing threshold \(t\ge0\) for

$$\delta=t+\sum_{i\ne0}\frac{(E_i-tM_i)_+}{h_i},\qquad
w_i=\frac{(E_i-tM_i)_+}{h_i},\quad w_0=0.$$

The correction \(p=\delta M+\eta Lw\) equals \(tM+\sum_i w_iW^{(i)}\). Therefore \(Y+p\ge0\), its mark is \(a\sqrt n\), and its mean is \(\mu+\delta\). Let \(H=\min_{i\ne0}M_i h_i\), \(h_{\min}=\min_{i\ne0}h_i\). The capped-tail dual gives

$$\delta=\max_{0\le v_i\le M_i/h_i,\ \sum v_i\le1}
\sum_i\frac{v_iE_i}{M_i}
\le\frac{\|E\|_2}{\sqrt H}
\le\frac D{\sqrt H}.$$

Indeed \(\sum_i v_i^2/M_i^2\le H^{-1}\sum_i v_i\le H^{-1}\). Furthermore \(LM=0\), \(\|M\|_2^2=n+1/\kappa\), and \(\|w\|_2\le D/h_{\min}\), so

$$\|p\|_2^2
=\delta^2(n+1/\kappa)+\eta^2\|Lw\|_2^2
\le D^2\left[\frac{n+1/\kappa}{H}
+\frac{\eta^2}{h_{\min}^2}\right].$$

Consequently this particular finish certifies

$$\frac{\theta_{\rm allowed}}{\sqrt n}
\ge\frac{a}{\mu+D/\sqrt H}.$$

In Paley orders, \(H\asymp\sqrt n\), \(h_{\min}\asymp\sqrt n\), and \(\eta\asymp\sqrt n\). Thus a source projection cost \(D=O(n^{1/4})\) gives bounded additional mean and a correction radius \(O(\sqrt n)\). If an allowed final mean is \(\bar\mu>\mu\), the sufficient quantitative condition is \(D\le(\bar\mu-\mu)\sqrt H\). Further positive padding by \(M\) attains that prescribed final mean exactly.

The radius loss can be necessary. On square orders in the bad sector of [the fixed-mark square control](anchored-repair-20.md#the-square-control), every nonnegative row with mark \(a\sqrt n\) has mean at least \(a\sqrt n/h\), \(h=(\sqrt q+1)/2\). Starting from a row of mean \(\mu<a\sqrt2\), any correction making it nonnegative and retaining the mark must have

$$\|p\|_2\ge\sqrt n\,\left(a\sqrt n/h-\mu\right)
=(a\sqrt2-\mu+o(1))\sqrt n.$$

This is compatible with a negative-part norm of order \(n^{1/4}\). A source projection cost and the radius of a subsequent mark-preserving finish control different steps.

## Replay

The [script](parallel-extrapolation-26.py) independently checks the explicit full-Paley KKT pair, two-width signed cancellation, the full forbidden Gram, and positivity at six prime orders. It also checks the source projection and the finish bounds on both localized sectors at three primes and two squares. The [records](parallel-extrapolation-26.jsonl) use floating point. The analytic identities above provide the proofs.

```sh
.venv/bin/python -B research/parallel-extrapolation-26.py > research/parallel-extrapolation-26.jsonl
```
