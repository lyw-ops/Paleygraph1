# All Legendre orders in the actual two-center cold derivative

Use the original closed marked square, \(t_0=n\), and the actual fixed predictor coefficient \(\alpha(t)\) of the Legendre field \(Y\), with \(|\alpha|<0.244\) from [Round 146](cold-actual-legendre-amplitude-146.md). As there \(S=s_nC_1\), \(d_t(v)=v/\sqrt{4t+v^2}\), and
\[
 B=K\operatorname{diag}\bigl(d_{t_i}(S_i)+\alpha Y_i d'_{t_i}(S_i)\bigr).
\]
Let \(B_2=K\operatorname{diag}(d_{t_i}(S_i+\alpha Y_i))\), with the same physical mark. On the inherited two-boundary-pair \(P_{5000}\) class on the whole square, uniformly for all sufficiently large eligible primes,
\[
 \|B_2-B\|_{P_{5000}}<0.0092,\qquad
 \|B_2\|_{P_{5000}}<0.644,\qquad
 \|B_2^2\|_{P_{5000}}<0.415 .
\]
Thus all quadratic and higher Legendre terms within this genuine two-center subrow are included. The full height-\(601,602\) derivatives also have other centers and a Picard residual. These bounds leave their joint signed comparison and the nonlinear invariant open.

## The positive comparison for the higher terms

Off the mark expand the exact derivative at \(u_t C_1+v_tY\), where \(u_t=s_n/(2\sqrt t)\) and \(v_t=\alpha/(2\sqrt t)\):
\[
 d_t(S+\alpha Y)=
 \sum_{\ell\ge0}(-1)^\ell b_\ell(u_t C_1+v_tY)^{2\ell+1},
 \qquad b_\ell=4^{-\ell}\binom{2\ell}{\ell}.
\]
The terms with no \(Y\) and with exactly one \(Y\) are precisely the two terms used in \(B\), before \(K\). For the rest use the rational caps \(U=0.356\), \(V=0.244/7.96\) on the moduli; the two scalar inequalities are inherited from [Round 145](cold-jacobi-linear-legendre-145.md) and the actual amplitude. Thus \(w=U+2V<1\).

Within either fixed base fiber the average over both full lifts gives the symmetric atomic measures
\[
 \mu_C=(\delta_{-1}+\delta_1)/2,\qquad
 \mu_Y=\delta_0+(\delta_{-2}+\delta_2)/2,
\]
of dimension masses one and two. For the degree \(m=2\ell+1\) term with \(b\ge2\) \(Y\)-factors, use the positive convolution \(\mu_C^{*(m-b)}*\mu_Y^{*b}\) with scalar majorant \(b_\ell\binom{m}{b}U^{m-b}V^b\). The full lifts in each factor of a product of averaged physical traces can be taken independently. The mass and absolute first moment of each of \(\mu_C,\mu_Y\) are equal, and the first moment of the convolved word is at most \(m\) times its mass. Outside the base fibers the multiplier has weight zero. The odd product with a negative input packet is of the even transport type, as in the [two-pair calculation](shifted-resolvent-96.md).

For \(\ell=1,\ldots,7\) sum the exact rational folded masses of those convolutions and apply the base/off-base column formula of Round 145, including the affine limit. This checks the common column supremum, not a sum of separate suprema. In the analytic tail \(\ell\ge8\), use \(\pi(k)\le2k\) and the raw moments to bound the rate of a word by \(2(m+1)\) times its dimension. This also bounds the off-base column. With \(b_\ell\le1\) and allowing all \(b\) in this tail, the omitted price is at most
\[
 \sum_{\ell\ge8}4(\ell+1)w^{2\ell+1}
 =4w^{17}\left(\frac9{1-w^2}+\frac{w^2}{(1-w^2)^2}\right).
\]
The exact retained comparison plus this tail is below \(0.00905\). The marked value with \(t_0=n\) is restored by one bounded physical point correction. The lift discrepancy is bounded termwise by the absolute coefficient times the dimension bound and the input price, since the series at \(w<1\) is summable. Thus the actual differences have uniform \(O_{5000}(n^{-1/2})\) repair costs and the strict margin yields the \(0.0092\) bound eventually. Add the established \(0.634\) selected estimate and then square in the same class to obtain the two other bounds.

Replay the [exact rational checker](cold-higher-legendre-step-148-check.py) with Python 3. It imports the recorded Round 145 price calculation and reproduces [one record](cold-higher-legendre-step-148-checks.jsonl). Together with the actual amplitude, this is a uniform comparison for the two-center selected block. For the full \(A_h\), a corresponding omitted rate \(<0.356\) at either height or a two-height difference from \(B_2^2\) below \(0.585\) would suffice for contraction of the relevant step or product. No such omitted estimate is asserted here.
