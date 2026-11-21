# A quantitative near-unit slope bound using weighted cosets

Use the genuine selected ordinary-prime critical branch, true \(f,\nu\), phase defect \(e\) and sign \(\rho\) of [Rounds 157 and 158](ordinary-prime-near-unit-slope-spread-158.md). All norms on the physical field are counting norms. For \(0<\epsilon<1\) write
\[
 W_\epsilon=\{x\in Q:|f(x)|\ge1-\epsilon\},\qquad
 \lambda=\min(1,|W_\epsilon|/\sqrt p).
\]
Uniformly along the branch,
\[
                 \frac{\lambda^6}{\log^2(2/\lambda)}
                  \ll e+\epsilon+p^{-1/2}.
\]
In particular the estimate is automatic if \(\lambda\le p^{-1/4}\) or if \(\epsilon\) exceeds a sufficiently small fixed multiple of \(\lambda^2\), so assume the other cases below.

## Weighted concentration on fewer good cosets

The geodesic argument of Round 158 gives \(H=\langle W_\epsilon\rangle=W_\epsilon^{O(1/\lambda)}\), since Parseval bounds all needed products by \(2\sqrt p\) when \(\epsilon\ll\lambda^2\). In particular \(h=|H|\in[\lambda\sqrt p,2\sqrt p]\) and \(1-|f|=O(\lambda^{-2}\epsilon)\) there. Orthogonality gives a dual annihilator coset with true mass \(1-O(\lambda^{-2}\epsilon)\). Project to that coset, obtaining \(f_C\), with
\[
 \|f-f_C\|_2^2\ll\lambda^{-2}\epsilon\sqrt p,\qquad
 |f_C(xh')|=|f_C(x)|\quad(h'\in H),\qquad |f_C|\le1.
\]
The first bound uses the actual pointwise cap on \(\nu\). Call a coset good when the wrong sign on that coset has density at most \(1/4\). By constancy of the modulus and the pin, the mass of \(f_C\) outside the good cosets is \(O(1+\lambda^{-2}\epsilon\sqrt p)\).

For \(S_\Omega=\sum_{x\in\Omega}\chi(1-x)\), expand the fourth moment by using the first variable as a base:
\[
 \sum_\Omega S_\Omega^4
   =\sum_{u,v,w\in H}\ \sum_{x\in Q}
      \chi\bigl((1-x)(1-u x)(1-v x)(1-w x)\bigr).
\]
Only \(O(h)\) tuples give a square polynomial, since the root from \(1-x\) must pair with another root and the two remaining roots must pair. These contribute \(O(ph)\). All others contribute \(O(h^3\sqrt p)\) after opening the square restriction and using Weil; the additional factor \(x\) in the second complete character sum makes that polynomial nonsquare because its other roots are nonzero. On a good coset \(|S_\Omega|\ge h/2-1\). The number \(K\) of good cosets is therefore \(O(p/h^3+\sqrt p/h)\), which is \(O(\sqrt p/h)\) since \(h\ge p^{1/4}\).

## Uniform Mit'kin cutoffs and a weighted weak second norm

For two of the \(H\)-cosets, the number \(R_{ij}(u)\) of pairs giving a ratio \(u\ne0,1\) after the physical affine reflection obeys
\[
               |\{u:R_{ij}(u)\ge t\}|\ll h^2/t^2.
\]
To see the uniformity, use the \(N(D,E)\) cells and their exact \(u\)-multiplicity from [Round 151](ordinary-prime-coset-spread-151.md). Mit'kin permits sets of at most \(\min(h^2,p^3/h^4)\) cells. This is comparable to \(h^2\) for \(h\le2\sqrt p\). If at least \(M=\lfloor\tfrac12\min(h^2,p^3/h^4)\rfloor\) cells were \(t\)-rich, use any \(M\) of them in the lemma to obtain \(t=O(1)\). For \(t\) above a sufficiently large absolute constant, therefore, both the rich set and its rescaled copy are eligible. The first use gives at most \(O(h^2/t^3)\) rich cells. The second use on their rescaled copies gives \(O(h^2/t^2)\) for the number of relevant \(u\)'s. For bounded \(t\), use total pair count at most \(h^2\). The range under consideration has \(h\) growing, so rounding \(M\) changes no estimates. [Macourt–Shkredov–Shparlinski, Lemma 2.1](https://arxiv.org/pdf/1701.06192)

Let \(\omega_i\) be the modulus of \(f_C\) on good coset \(i\), so \(\sum_i\omega_i^2\le\|f_C\|_2^2/h\ll\sqrt p/h\). Take a true supported anchor with \(d_a=O(e)\) by the error averaging of [Round 157](ordinary-marked-frequency-localization-157.md). Modulate by \(\bar a\), restrict \(f_C\) to the good cosets, then affinely reflect and restrict to \(Q\) as in Round 152, obtaining \(g\). Its absolute correlations are majorized by \(\sum_{i,j}\omega_i\omega_j R_{ij}(u)\). The Lorentz form \(\sup_{E\ne\emptyset}|E|^{-1/2}\sum_{u\in E}R(u)\) is subadditive and equivalent within factor two to the weak counting second norm. It follows that the absolute correlations of \(g\) have weak norm at most
\[
       O\bigl(h(\sum_i\omega_i)^2\bigr)
                 \ll h K\sum_i\omega_i^2
                 \ll p/h .
\]
Thus \(D_g\ll(\sqrt p/h)^2\ll\lambda^{-2}\). Keeping these weights, rather than bounding every \(\omega_i\) by one, is needed for this exponent.

## Cap comparison and the stated exponent

The approximation to the true \(g_a\) from Round 152 costs \(O(1+\lambda^{-2}\epsilon\sqrt p)\) in counting squared norm. This bounds the reflected additive Rayleigh defect by \(O(e+\lambda^{-2}\epsilon+p^{-1/2})\) by the square-root triangle inequality. Unless this error parameter is bounded below, \(\|g\|_2^2\asymp\sqrt p\), and in all cases \(|g|\le1\). Larger error already implies the claim after multiplication by \(\lambda^2\).

The cap inequality of Round 152 now yields
\[
 \lambda^{-2}\log(2/\lambda)
           \gg \min\!\left(\eta_g^{-1/2},p^{1/4}\right).
\]
If the first term is the minimum, square and invert to get \(\lambda^4/\log^2(2/\lambda)\ll\eta_g\) and multiply by \(\lambda^2\). If the second is the minimum, the same inequality gives \(\lambda^4/\log^2(2/\lambda)\ll p^{-1/2}\) already. This proves the stated bound with the actual pin and weights and an explicit use of prime order.

For \(E=e+p^{-1/2}\) and \(E+\epsilon\) small, inversion gives
\[
 |W_\epsilon|/\sqrt p\ll (E+\epsilon)^{1/6}
                       \log^{1/3}(2/(E+\epsilon)).
\]
For instance splitting the summation at \(\epsilon=2\log(k)/k\) for large \(k\) gives a quantitative bound on \(n\|\nu^{*k}\|_2^2/\sqrt p\) by this expression plus \(O(k^{-2})\). Here the low amplitudes cost at most \((1-\epsilon)^{2k-2}\|f\|_2^2\). This is an estimate for the true convolution powers. The original regular average still has its unsmoothed joint weights.

The logarithm in the illustrative cutoff choice can be avoided. For \(k\ge3\), weighted layer integration gives
\[
 \sum_x|f(x)|^{2k}
 =(2k-2)\int_0^1 t^{2k-3}
                   \sum_{|f(x)|\ge t}|f(x)|^2\,dt .
\]
For \(s=1-t\) small use the bound above with \(\epsilon=s\); the remaining part is exponentially small in \(k\). On \(s\le1/k\) the amplitude factor is bounded by its value at \(E+1/k\), up to an absolute constant. On \(2^j/k\le s\le2^{j+1}/k\) the amplitude factor increases by at most \(O(2^{j/6})\), while the layer integration weight is \(O(2^j\exp(-2^j))\). It follows that the normalized squared norm and the modulus of the \(k\)-fold ratio-law Jacobi expectation are both
\[
 \ll (E+1/k)^{1/6}\log^{1/3}(2/(E+1/k))
\]
when \(E+1/k\) is small. Use their trivial constant bound for larger values.

## A two-threshold restriction at fixed moderate amplitudes

For fixed \(a,b\in(0,1]\) with \(a+b>1\), define \(B_s=\{x\in Q:|f(x)|^2\ge s\}\). Center the two random variables \(c(x),c(y)\) for \(c\sim\nu\). Cauchy–Schwarz gives
\[
 |f(x/y)|\ge |f(x)|\,|f(y)|
           -\sqrt{(1-|f(x)|^2)(1-|f(y)|^2)}
 \ge \sqrt{ab}-\sqrt{(1-a)(1-b)}
\]
on \(B_a\times B_b\). The last number is positive. The quantitative pin gives \(f=o(1)\) pointwise uniformly on the wrong sign, since its residual's counting second norm tends to zero. Therefore every nonzero difference \(x-y\) between the two levels has sign \(\rho\). If necessary, dilate both sets by a nonsquare. In the resulting square case the prime roots-of-unity bound gives \(|B_a||B_b|\le n+|B_a\cap B_b|\). This constrains the two actual layers while retaining all distinct pairs. [Hanson–Petridis, Theorem 1.2](https://arxiv.org/abs/1905.09134)

## A filtered part of the original favorable sum

Insert the factor \(\psi_k(t)=|f(t)|^{2k}\) at the slope of the actual favorable off-diagonal, keeping all four original physical \(F_0\) factors. This is a smooth filter on the original sum. Its normalized Mellin coefficients form the nonnegative probability \(\eta_k=(\nu*\check\nu)^{*k}\), so its Fourier coefficient sum is one. If \(\mu=\nu*\eta_k\), then
\[
 \|\mu\|_\infty\le\|\eta_k\|_\infty
                  =\|\nu^{*k}\|_2^2
\]
by Cauchy–Schwarz for the correlation of \(\nu^{*k}\) with its translates. The actual filtered bound of Round 156 consequently gives
\[
 |S_{\rho,\psi_k}|\ll p+
       p^{3/2}(E+1/k)^{1/6}\log^{1/3}(2/(E+1/k))
\]
in the small-parameter range. In particular the smooth high-power-filtered part of the original favorable geometry is \(o(p^{3/2})\) for growing \(k\) on the true critical branch. This does not control \(S_{\rho,1}\) at the required \(O(p)\) scale.
