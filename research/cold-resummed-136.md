# Resumming the pure seed powers of the actual remainder

Keep the original fully marked square and \(h=601,602\). Put \(C_h=V_h-S\) and \(E_h=D_h-D^{\mathrm J}\) as in [Round 135](cold-remainder-135.md). The geometric calculation below groups powers of the same rank-one seed before applying the positive envelope to the nonseed factors. It gives a translated physical bound for the actual remainder through sufficiently large eligible primes.

## Exact signed coefficient collection

At good full Mellin characters the seed is \(s_n(L+L^{-1})/2\), with \(s_n=2\sqrt{p/n}\). Retain binomial orders \(\ell=0,\ldots,13\) in the bulk derivative. The exact coefficient of \(C_h^jL^k\), for \(j\ge1\), is the sum of the terms
\[
 \frac{(-1)^\ell\binom{2\ell}{\ell}}
      {4^\ell(2\sqrt t)^{2\ell+1}}
 \binom{2\ell+1}{j}\left(\frac{s_n}2\right)^{2\ell+1-j}
 \binom{2\ell+1-j}{(2\ell+1-j-k)/2}.
\]
Only admissible integral binomial indices contribute. The common coefficient can be summed before modulus even if the signed decomposition of \(C_h\) is unavailable. Indeed, for each fixed word of \(j\) actual nonseed objects and specified independent lifts, the repeated seed exponent gives the same tensor factor \(L^k\) acting on that word. The calculation does not identify different nonseed words on the basis of their numerical weights.

Let \(\beta\) be the symmetric weight envelope of \(C_h\), from the eight nonseed center pieces and the actual-height residual envelope of [Round 130](cold-combined-height-130.md). Its retained piece includes the excess-zero charge. The remaining off-zero tilted mass is at most \(\varepsilon=5\cdot10^{-7}\), with tilt \(w\mapsto\cosh(w/5)\). For fixed \(j\), let \(\gamma_j\) be the symmetric positive measure obtained by taking the modulus of each collected Laurent coefficient. The resulting retained comparison is \(\gamma_j*\beta^{*j}\). The omitted residual and its descendants add at most
\[
 j\varepsilon \|\gamma_j\|_{\rm tilt}
       (\|\beta\|_{\rm tilt}+\varepsilon)^{j-1}
\]
in tilted mass. The signed collections ahead of this step are in actual Mellin objects. The subsequent treatment of the nonseed words by \(\beta\) is a positive upper.

The replay uses the original square for all coefficient enclosures. It keeps all \(|w|\le150\) weights of the retained polynomials and prices the outlying weights in tilted mass. The translated price is checked at each non-affine base column, its affine limit, and the single off-base first-moment charge, using the rational prices of [Round 96](shifted-resolvent-96.md). Tilted errors cost at most ten times their tilted mass. The analytic orders starting at \(\ell=14\) cost at most \(0.0000407\) by [Round 135](cold-remainder-135.md#a-quantitative-tail-and-counting-comparison-for-the-actual-remainder). The exceptional-lift and marked corrections are still \(O_{5000}(n^{-1/2})\) relative price, uniformly on the original square. They restore the actual marks at \(t_0=n\) and retain both boundary pairs.

The [outward check](cold-resummed-136-check.py) verifies that the eventual actual step prices at both heights satisfy
\[
 \|KE_h^{(1)}\|_{P_{5000}}<0.527,\qquad
 \|K(E_h-E_h^{(1)})\|_{P_{5000}}<0.142,\qquad
 \|KE_h\|_{P_{5000}}<0.666,
\]
where \(E_h^{(1)}\) has physical diagonal \(d_{t_i}'(S_i)C_{h,i}\). The last comparison prices the combined upper, and is slightly sharper than adding the two separate decimal bounds. All three include the infinite analytic tail and eventual exceptional repair.

## Obstruction to repricing this comparison

In the geometric positive comparison for height 601, restrict the positive transport matrix after the Laurent resummation to weights \(1,\ldots,12\). The replay supplies a fixed positive integer vector whose image is componentwise strictly larger than \(0.570\) times the vector. The vector was selected in a floating exploration and then checked outward in Arb. Positivity gives that every monotone homogeneous norm of this comparison has rate above \(0.570\), since one can iterate the componentwise inequality. The same conclusion holds for a positive linear reprice by pairing with the witness directly.

Thus changing the packet price alone cannot make this resummed comparison reach \(0.472\). The finite witness does not refute the actual signed \(KE_h\), since the comparison already discards cancellation between nonseed objects. To improve this route, an actual repeated-field identification across nonseed terms or a new signed transport estimate is needed. The physical half-step and invariant-ball margins are separate obligations.

Replay with python-flint 0.9.0. The [saved records](cold-resummed-136-checks.jsonl) contain the two actual translated uppers and the positive-comparison lower witness. The replay imports the accepted Round 130 coefficient and activation envelopes and independently advances the verified height-602 step.
