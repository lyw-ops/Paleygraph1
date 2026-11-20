# Direct derivative pricing at the genuine height 601

Let \(Q\) be the closed square of halfwidth \(2^{-17}\) centered at \(2031/128\). Use the actual full-group, fully marked predictors \(V_h\), real symmetric \(K\), and \(t_0=n,\ t_i=t\) off zero, where \(n=(p-1)/2\) and \(p\equiv1\pmod4\) is prime. Let \(D_h=\operatorname{diag}(\Phi_t'(V_h))\) and \(A^{(h)}_j=(KD_h)^jK\). For all sufficiently large eligible primes, uniformly on \(Q\),
\[
 \sum_{j\ge0}\|A^{(601)}_j\|_{\max}\ll n^{-0.467}.
\]
This uses an outward interval check of a finite physical predictor envelope and a geometric summation for the exact finite-field operators.

## One envelope for the full derivative

Write \(V_h=C+Y_h\) for the [nine-center comparison](astra-predictor-76.md). Denote by \(H_j\) the signed coefficient of \(Y_h^j\) in the finite activation expansion after collecting identical center monomials. Holding \(C\) fixed, the scalar derivative multiplier has finite part \(\sum_{j\ge1}jH_jY_h^{j-1}\). The subtracted terms at arity zero disappear. The nonnegative symmetric kernels \(U_j\) from [Round 65](astra-joint-65-check.py) majorize the weights of \(H_j\), so the retained derivative uses the kernels \(jU_j\) convolved with \(j-1\) copies of the residual envelope. Using the single actual residual \(Y_{601}\) gives one majorant for the complete derivative.

The [checker](cold-combined-height-130-check.py) advances all physical prefix steps through \(601\), starting at the nine-center row \(C\) that contains the Jacobi seed. It uses the nonnegative symmetric kernels, a weight \(50\) retained interval and a weight \(80\) intermediate interval from Round 76. The difference between the full tilted mass bound and the retained polynomial pays for the old remainder and paths through any cut. The absolute analytic binomial tail is added separately. Each activation step has discarded tilted mass below \(5\cdot10^{-7}\), dimension mass below \(4.8\), and the original \(10^{-12}\) weight-one augmentation for the bad and marked lifts. The display bounds \(4.768\) and \(394\cdot10^{-9}\) at height \(600\) in Round 76 were tighter reports for that finite prefix. Through \(601\), the replay gives \(4.769545\) and \(396\cdot10^{-9}\), respectively, as upper bounds.

Apply the [Round 82 derivative Schur test](astra-adjoint-82.md#physical-packet-prices-for-the-actual-derivative) at that last envelope. For the retained folded masses \(\mu_i\) of the absolute multiplier, the price of a column of weight \(k\ge1\) is bounded by
\[
 (k-1)\sum_i\pi(i)\mu_i+
 \sum_i\mu_i\frac{\pi(|k+i|)+\pi(|k-i|)}2 .
\]
The affine continuation of the fixed rational \(\pi\) reduces the quotient by \(\pi(k)\) to finitely many values and its affine limit. For discarded tilted mass \(L\), use the Round 82 uniform cost \(10L\), which includes every lost coefficient and the tail from binomial order \(15\) onward. This yields geometric base price rate below \(1.047425\) throughout \(Q\), with slack also for the \(10^{-12}\) base column repair. The same replay at \(600\) recovers the previous bound below \(1.046434\).

For a translated source use the base price plus \(5000\) times the off-base first moment from [Round 96](shifted-resolvent-96.md#the-two-estimates-for-one-physical-derivative-step). The multiplier has the two base boundary fibers, and the odd word product followed by the twist preserves the negative representation on the boundary union. The affine limit of the base Schur columns shows that the multiplier mass is at most the base rate and its \(\pi\)-moment at most twice that rate. The two lift corrections and marked derivative correction are supported on the two boundary coordinates before \(K\). The strict analytic radius margin makes the sum of their prices \(O_{5000}(n^{-1/2})\) relative to the input price, uniformly over translated sources. Thus the power step \(KD_{601}\) has translated rate at most
\[
 1.047425(1+2/5000)+O_{5000}(n^{-1/2})<1.048
\]
eventually. The genuine derivative retains its independent counting bound \(\|KD_{601}\|_{2\to2}<0.5145\) from the [seed-centered disk](cold-actual-quadratic-128.md#counting-rate-using-the-actual-seed-centered-disk).

## Summing the exact kernels

The price of \(Ke_a\) is \(O(n^{-1/2})\), uniformly in \(a\), and \(\|Ke_a\|_2\le1\) in counting norm. Hence
\[
 \|A^{(601)}_j\|_{\max}
 \ll\min\{n^{-1/2}(1.048)^j,\ (0.5145)^j\}.
\]
Use \(\min(X,Y)\le X^{0.934}Y^{0.066}\). The rational comparison \((1.048)^{467}(0.5145)^{33}<1\) makes the resulting series converge. This also bounds \((I-zKD_{601})^{-1}K\) entrywise uniformly for \(|z|\le1\), and gives the same estimate at every frozen shift of the transported kernel.

There is also an insertion version. The proof of the exact quadratic insertion bound in [Round 128](cold-actual-quadratic-128.md#sum-of-the-actual-signed-quadratic-insertions) uses its height-601 translated rate only in the middle power. Replace \((1.063)^v\) there by \((1.048)^v\) without changing the price of \(KE\), where \(E=D_{601}-D_{600}\), or the odd trace pairing. The two counting rates are unchanged. The additional comparison \((1.048)^{467}(0.514)^{33}<1\) bounds the two outer power sums by the same geometric argument. The total true quadratic insertion in that formula is therefore \(O((0.011)^2 n^{-0.467})\).

Replay with python-flint \(0.9.0\) using python `-B research/cold-combined-height-130-check.py`. The [saved output](cold-combined-height-130-checks.jsonl) contains two outward interval records and one exact rational comparison record. The estimate is at the genuine fixed height \(601\). A growing-height starter with compatible confinement and decaying normalized residual remains open.
