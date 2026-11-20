# Prime power saving in the actual shifted high-layer energy

Keep the actual probability law \(\nu\) on \(\widehat Q\), its Fourier row \(f\), the physical mark \(v\ne0\), and the original cross-ratio sum from [Round 162](ordinary-physical-slope-fiber-count-162.md). Use counting measures. The actual cap gives \(\sum_{z\in Q}|f(z)|^2\ll\sqrt p\). Fix a squared threshold \(a>1/2\) and let
\[
 X=\{x\in Q:1-vx\in Q,\ |f(1-vx)|^2\ge a\}.
\]
Then, uniformly in the physical \(v\) on the selected prime family,
\[
 E^\times(X)\ll_a p^{3/2-1/209}.
\]

## Small quotient set after the actual affine shift

For any \(u,w\in 1-vX\), apply Cauchy–Schwarz to the centered random variables \(c(u),c(w)\) for \(c\sim\nu\). This gives
\[
 |f(u/w)|\ge |f(u)||f(w)|-\sqrt{(1-|f(u)|^2)(1-|f(w)|^2)}
             \ge 2a-1.
\]
This is valid for complex coefficients and the original nonnegative probability law. Thus \(|(1-vX)/(1-vX)|\ll_a\sqrt p\), including the constant quotient. Also \(N=|X|\ll_a\sqrt p\) by the same Parseval bound.

For nonempty \(X\) write \(K=N^3/E^\times(X)\ge1\). Apply Theorem 1.2 of [Reiher and Schoen, *Note on the theorem of Balog, Szemerédi, and Gowers*](https://link.springer.com/article/10.1007/s00493-024-00092-5) in the multiplicative abelian group, with the loss parameter fixed at \(1/4\). There is \(X_0\subseteq X\) of size \(\gg N K^{-1/2}\) with \(|X_0/X_0|\ll K^4|X_0|\). If needed trim \(X_0\) to \(X_1\) of size \(m\le\lfloor\sqrt p\rfloor\); since \(N=O(\sqrt p)\), this loses at most a constant factor, preserving \(m\gg_a NK^{-1/2}\) and \(|X_1/X_1|\ll_a K^4m\).

Set \(A=-vX_1\), \(B=A^{-1}\), and \(C=(A+1)^{-1}\). All three sets have size \(m\), with no zero before inversion. In Theorem 1 of [Zhelezov, *On additive shifts of multiplicative almost-subgroups in finite fields*](https://arxiv.org/pdf/1507.05548#page=2), use shift one. Its prime-field hypothesis applies and yields
\[
 m^{1+1/26}\ll\max\{|AB|,|(A+1)C|\}
                    \ll_a \max\{K^4m,\sqrt p\}.
\]
If the first term is the maximum, then \(K^{4+1/52}\gg_a N^{1/26}\), hence \(E^\times(X)\ll_a N^{3-2/209}\). If the second term is the maximum, \(m\ll_a p^{13/27}\) and therefore \(K\gg_a N^2p^{-26/27}\), giving \(E^\times(X)\ll_a Np^{26/27}\). With \(N\ll_a\sqrt p\) both imply the claimed bound. The empty set costs zero.

## A bound at every fixed positive squared threshold

For a fixed \(a>0\), the centered-variable argument need not give a pointwise quotient lower. Instead every subset \(W\) of the unreflected level \(1-vX\) satisfies
\[
 E^\times(W)\gg_a |W|^4/\sqrt p.
\]
To see this, choose unit phases \(e_w\) so that \(e_w f(w)=|f(w)|\). Jensen gives \((\sqrt a|W|)^4\le\mathbb E_{\nu}|\sum_{w\in W}e_w c(w)|^4\). Bound the last expectation by \(n\max\nu\) times the uniform anchor average. Character orthogonality leaves only multiplicative quadruples, each of modulus at most one. The actual cap is \(n\max\nu=O(\sqrt p)\). This is the hereditary physical Fourier bound of [Round 86](astra-fibers-86.md) applied to the true law here.

Put \(N_0=\sqrt p\), \(D=\max(1,N_0^3/E^\times(X))\), and \(K=N^3/E^\times(X)\) for nonempty \(X\). Since \(N=O_a(N_0)\), \(K\ll_a D\) and
\[
 NK^{-1/2}=\sqrt{E^\times(X)/N}\gg_a N_0D^{-1/2}.
\]
The first BSG step with the same trimming gives an \(X_1\) of size \(m\gg_a N_0D^{-1/2}\) and quotient set at most \(O_a(K^4m)\). In \(W_1=1-vX_1\), the hereditary energy estimate gives \(L=m^3/E^\times(W_1)\ll_a N_0/m\ll_a D^{1/2}\). A second application of Reiher–Schoen gives \(W_2\subseteq W_1\) of size \(l\gg m L^{-1/2}\gg_a N_0D^{-3/4}\) and \(|W_2/W_2|\ll L^4 l\). Its inverse affine preimage \(X_2\subseteq X_1\) has \(|X_2/X_2|\ll_a K^4m\ll_a K^4L^{1/2}l\). Apply the same Zhelezov theorem to \(-vX_2\), its reciprocal and the reciprocal of its translate by one. Its size is at most \(\sqrt p\). The two quotient bounds give
\[
 l^{1/26}\ll_a \max(K^4L^{1/2},L^4)\ll_a D^{17/4}.
\]
Thus \(N_0^{1/26}\ll_a D^{17/4+3/104}=D^{445/104}\), and \(D\gg_a p^{2/445}\). In particular for sufficiently large primes, \(D>1\) and
\[
 E^\times(X)\ll_a p^{3/2-2/445}.
\]

## Transfer to the true weighted slope band

Let \(Y\) be the other actual reflected physical level at a fixed squared threshold \(b>0\), and let \(h(u)=|X\cap u^{-1}Y|\) for \(u\in Q\). By counting multiplicative quadruples or Parseval,
\[
 \sum_u h(u)(h(u)-1)\le\sum_u h(u)^2
    \le \sqrt{E^\times(X)E^\times(Y)}.
\]
Consequently a true slope cut with \(|f(t)|^2\le p^{-\sigma}\) costs \(O_{a,b}(p)\) in the original four-vertex block whenever
\[
 \begin{array}{ll}
 \sigma\ge 1-4/445,&a,b>0,\\
 \sigma\ge 1-1/209-2/445,&\max(a,b)>1/2,\\
 \sigma\ge 1-2/209,&\min(a,b)>1/2.
 \end{array}
\]
The middle case includes the original \(a+b>1\) slice. All other physical conditions can be retained since the bound dominates the absolute sum, with the four true vertex amplitudes at most one. The result improves the \(\sigma\ge1\) slice and is an ordinary proof on the selected prime branch. It leaves fixed moderate slopes and the uncut ordinary target open.

## A stronger pointwise overlap bound when both thresholds exceed one half

For \(u\in Q\setminus\{1\}\) restrict to \(x\in X\cap u^{-1}Y\), and write \(A_x=1-vx\). The two unreflected sets of vertex values are \(Z=\{A_x:x\in X\cap u^{-1}Y\}\) and \(uZ+1-u\). When both squared thresholds exceed one half, the pointwise Fourier argument bounds both of these sets' quotient cardinalities by \(O_{a,b}(\sqrt p)\). Trim to at most \(\lfloor\sqrt p\rfloor\) points at a constant-factor loss if needed. Apply the same Zhelezov theorem with first set \(Z\), second set \(Z^{-1}\), shift \(d=u^{-1}-1\ne0\), and third set \((Z+d)^{-1}\). Multiplication by \(u\) identifies the shifted quotient set with that of \(uZ+1-u\). All inversions are of nonzero elements. This gives
\[
 h(u)^{27/26}\ll_{a,b}\sqrt p,qquad h(u)\ll_{a,b}p^{13/27}
 \qquad(u\ne1).
\]
The theorem's constant is uniform in nonzero \(d\), by rescaling the three sets to shift one. Thus
\[
 \sum_{u\ne1}h(u)(h(u)-1)\ll p^{13/27}|X||Y|
 \ll_{a,b}p^{1+13/27}.
\]
This replaces the last sufficient endpoint above by \(\sigma\ge26/27\) when both squared thresholds exceed one half. The identity dilate has been excluded as in the actual physical arc. No exponent below \(26/27\) follows for this block from the pointwise argument alone.
