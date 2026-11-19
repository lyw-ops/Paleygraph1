# The exact Newton corrections at the 30-step and 600-step predictors

Write \(a=2031/128\), \(D=\{|t-a|<1/4\}\) and \(Q=\{|\Re t-a|,|\Im t|<2^{-17}\}\). The actual prime marked iteration from the Jacobi seed has the following obstruction. For any closed interval \(I\subset D\cap\mathbb R\) of positive length and any \(0<\eta<1\), there is a \(c(I,\eta)>0\) such that, for every sufficiently large eligible prime, on a subset of \(I\) of Lebesgue measure at least \((1-\eta)|I|\),
\[
             \|h_{30}(t)\|_{4,\mathrm{count}}\ge c(I,\eta)n^{1/4}.
\]
Here \(h_{30}=(I-KD_{V_{30}})^{-1}(T_t(V_{30})-V_{30})\) is the exact linear correction for the [round-75 predictor](astra-fourth-75.md). The same conclusion applies to any approximate correction with a uniform counting linear defect \(o(\sqrt n)\), in particular the tolerance \(1/32\). This rules out closing the disk by the counting fourth-norm test at this fixed iterate. It leaves the centered signed remainder, the value at the single floor \(a\), and the stationary section itself open.

For the actual nine-center predictor \(V_{600}\) on \(Q\), the counting fourth norm of its exact correction is below \(1/2\) for \(10^{30}\le n\le10^{321}\), for eligible primes and prime squares. The physical stationary section is holomorphic there with \(|m_q|<3/\sqrt n\). On the real interval the corresponding correction is below \(3/5\) through \(n=10^{345}\). With unbounded sizes the real mark has uniform limsup below \(7.1\cdot10^{-174}\). The all-prime 600-step Newton test and ETH Problem 26 remain open. [Earlier 600-step enclosure and Newton criterion](astra-predictor-76.md)

## A holomorphic family that detects the realized 30-step residual

Let \(S=2\sqrt n K e_0\), \(K^*K=I-J\), where \(J\) projects onto constant coordinates. Use \(\|v\|_{2,n}^2=n^{-1}\sum_i|v_i|^2\). Write \(z=1/(2\sqrt t)\) and set
\[
 G_z(x)=\frac{\sqrt{1+z^2x^2}-1}{z},\qquad
 U_0=S,\qquad U_{j+1}=S+K G_z(U_j).
\]
Set \(G_0=0\) by continuity. The proxy \(U_j\) retains the forcing \(S\). Removing the other marked-site correction permits evaluation at \(z=0\). Below we pay this correction explicitly on the target real interval.

There is a connected open neighborhood \(\Omega\) of zero and of the entire image of \(D\) under \(t\mapsto1/(2\sqrt t)\) on which the proxies through height 30 are holomorphic and uniformly bounded by 5 coordinatewise for all sufficiently large primes. To see this on the image of \(D\), reuse the round-75 30-step upper comparisons. Their upper measures explicitly add the cost of the physical marked correction. Omitting that correction retains the same bounds, including the bad-lift allowance for the actual operator \(K\). The constant removed in \(G_z\) is killed by \(K\). The second part of \(\Omega\) is the interior of
\[
  -1/4096\le\Re z\le513/4096,\qquad |\Im z|\le1/65536 .
\]
The two regions overlap at \(z=1/8\), or \(t=16\). The power-series square roots agree there and on their overlap.

The new Arb160 certificate encloses on each of 514 equal slabs the first 14 binomial orders of \(G_z(sX+y)\), where \(s=2\sqrt{q/n}\) and \(X=S/s\). Their scalar coefficients before expanding the powers are \(\binom{1/2}{l}z^{2l-1}\). Collect each \(T_k(X)y^j\) before taking the common upper envelope. From the initial zero feedback, apply the [16-packet mass and second-moment comparison](astra-histogram-53.md). For the absolute tail all powers of \(|z|\) increase with \(|z|\). Taking the maximal modulus \(R\) in the rectangle, its terms agree with the old tail at \(t=1/(4R^2)\). At each return the total raw activation-coefficient price is at most \((1-\sqrt{1-25R^2})/R<2\). Thus the bad-lift repair is below \(4\sqrt q/n<10^{-5}\) for \(n\ge10^{14}\), in the first packet. Adding \(10^{-5}\) at every step yields \(\|U_j\|_\infty<5\) through \(j=30\). On both parts of \(\Omega\), \(|z|5<1\) uniformly. Consequently \(G_z(U_{30})\) is uniformly bounded as well. Contraction of \(K\) then bounds \(U_{31}\) in *normalized second norm*. No coordinate bound for that last output is needed.

Now write the first nonzero possible coefficient of each increment as
\[
 U_j-U_{j-1}=z^j L_j+O_p(z^{j+1}),\qquad
 L_1=K(S^2/2),\qquad L_{j+1}=K(S L_j).
\]
Products are coordinatewise. The recursion follows by expanding \(G_z(x)=zx^2/2+O(z^3)\) and taking the difference of its values on the two preceding iterates, both equal to \(S\) at zero. Cauchy's estimate on a fixed circle in the bridge gives \(\|L_j\|_\infty\le M_j<\infty\) uniformly in the prime for each \(j\le30\).

For every \(1\le j\le31\), \(\liminf_p\|L_j\|_{2,n}>0\). First, \(\|L_1\|_{2,n}^2=\operatorname{Var}_n(S^2)/4\to2\) by the Jacobi arcsine law \(S\Rightarrow2\sqrt2\cos\theta\) for uniform angle. Assume the claim at \(j\le30\). If the next normalized norm tends to zero on a subsequence, \(S L_j\) approaches its mean in normalized second norm by the isometry modulo constants. The means are bounded and a further subsequence converges to a constant \(b\). For each fixed \(\delta>0\), the set \(|S|<\delta\) has positive limiting measure and \(|S L_j|\le M_j\delta\) there. Consequently \(|b|\le M_j\delta\), hence \(b=0\). On \(|S|\ge\delta\) the normalized second norm of \(L_j\) now tends to zero. On the complement its squared norm is at most \(M_j^2\operatorname{Pr}_n(|S|<\delta)\), which tends to zero upon sending \(\delta\downarrow0\). This contradicts the induction hypothesis. [Prime seed law and finite-field moment control](astra-reachable-74.md)

Use the real unit vector \(w_p=L_{31}/\|L_{31}\|_{2,n}\) (in normalized norm). The scalar functions
\[
 f_p(z)=n^{-1}\sum_i (U_{31,i}-U_{30,i})w_{p,i}
\]
are holomorphic and locally uniformly bounded on \(\Omega\). The coefficient at \(z^{31}\) is \(\|L_{31}\|_{2,n}\), bounded away from zero. From every sequence of growing primes one can extract a subsequence converging locally uniformly to a holomorphic \(f\) with nonzero coefficient at that order. In particular \(f(z(t))\) has at most finitely many zeros on the compact interval \(I\). For every \(\eta>0\) it follows that there is a positive uniform threshold \(c\) such that \(|f_p(z(t))|\ge c\) on at least \((1-\eta)|I|\) of \(I\) for every sufficiently large prime. Otherwise take thresholds tending to zero and a violating sequence. On a convergent subsequence, remove open neighborhoods of the finitely many zeros of total length less than \(\eta|I|\). Uniform convergence gives a fixed positive lower bound on the compact remainder, a contradiction.

It remains to restore the physical activation. For real \(t\in I\), put \(F_p(x)=\sqrt{4p+x^2}\). Each actual update satisfies
\[
 V_{j+1}=S+K G_z(V_j)+
 [F_n(V_{j,0})-2\sqrt n-F_t(V_{j,0})]K e_0 .
\]
The bracket is uniformly bounded for \(j\le30\) by the actual round-75 cap and rationalization of the marked root. Since \(\|Ke_0\|_{2,n}\le n^{-1/2}\) and \(G_z\) is globally 1-Lipschitz on the real line, induction gives \(\|V_j-U_j\|_{2,n}=O_I(n^{-1/2})\) through \(j=31\). The actual residual \(r=V_{31}-V_{30}\) therefore obeys \(\|r\|_{2,n}\ge |f_p(z(t))|-O_I(n^{-1/2})\). Finally \(\|I-KD_{V_{30}}\|_{2\to2}\le2\) since both real floor derivatives have modulus below one. Thus a correction with counting linear defect \(e\) satisfies
\[
 \|h\|_{4,\mathrm{count}}
 \ge n^{-1/4}\|h\|_{2,\mathrm{count}}
 \ge \tfrac12 n^{1/4}\bigl(\|r\|_{2,n}-e/\sqrt n\bigr).
\]
This proves the asserted prime-uniform measure bound. Its constant is non-effective in this argument. The same proof works at each fixed seed iterate through 30, using its own leading coefficient.

## Finite counting bounds for the true nine-center correction

On \(Q\) reuse the [600 exact returns](astra-predictor-76.md). Their coordinate cap is \(M=4.768\). Each upper representation contains the real Jacobi seed of mass at least \(2.8284\), so \(\|V_j-S\|_\infty<1.94\), including the initial nine-center row. In particular the initial normalized increment is below 4, and the imaginary cap is \(b=1.94\). With \(L=a-2^{-17}\) the derivative on each consecutive coordinate segment has modulus at most \(M/\sqrt{4L-2b^2+M^2}<0.53755\). On the real segment take \(b=0\) to get \(0.51355\). The marked derivative uses the larger floor \(n\) and satisfies the same bounds. Write \(d\) for the respective upper bound. The residual at height 600 is at most \(4d^{600}\sqrt n\) in counting second norm. Neumann inversion at that height bounds both the counting second and fourth norms of the exact Newton correction by \(4d^{600}\sqrt n/(1-d)\). Rational comparisons give the stated \(1/2\) and \(3/5\) thresholds. The round-76 Taylor bound and radius-\(1/2\) counting contraction close the physical stationary section. Its coordinate cap is at most \(4.768+0.6+0.5<5.9\), giving the stated mark bound by the marked inverse hyperbolic sine.

For arbitrary sizes the normalized real increment at height 600 is below \(4(0.51355)^{599}\). The round-76 positive-factor comparison bounds the real mark limsup by at most \(0.4\) times that number, strictly less than \(7.1\cdot10^{-174}\). These improvements use ordinary rational inequalities on the inherited interval-certified coordinate masses. The new analytic bridge uses outward-rounded Arb160 enclosures. There is no floating inference or finite-prime extrapolation. [Replay script](astra-newton-77-check.py) · [Two records](astra-newton-77-checks.jsonl)

1. For the 30-step exact solve, test the centered remainder through the large-floor expansion. Its first candidate nonconstant coefficient before transport is \(\tfrac12(I-J)L_{31}^2\) at order \(z^{63}\) for the proxy. Establish a positive normalized variance of the square and justify analytic control of the exact remainder up to the target, including the mark. The fourth norm alone can no longer close this fixed-depth branch.
2. For the nine-center 600-step row, look for a common bounded corridor for its finite prefix from \(Q\) to a large floor, and determine the first nonconstant coefficient of its initial residual with the amplitudes kept signed. This would test whether the fixed-depth obstruction also applies to that predictor. A size-dependent depth or a genuinely centered estimate remains available.
