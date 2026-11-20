# A positive physical form for the actual one-match covariance

Retain the full character group of order \(m=p-1\), both square lifts, the actual \(\omega,\ell\), and the regular set of [Round 167](ordinary-Gauss-covariance-pair-cuts-167.md). Write \(\kappa=\|\omega\|_\infty=O(p^{-1/2})\). The physical Fourier multiplier of \(\ell\) is \(g(t)(1-g(t))\), where \(g(t)=|f(t)|^2\in[0,1]\). It annihilates the physical identity \(t=1\).

## Completed Gauss bound and overlapping selections

For disjoint opposing lists \(A,B\) of size \(r\ge1\), the complete normalized Gauss correlation is \(m/p^r\) times Katz's unnormalized hypergeometric sum of type \((r,r)\) at \(1\). This follows directly by multiplicative orthogonality with \(\prod x_j=\prod y_j\) and additive phase \(e_p(\sum x_j-\sum y_j)\). Katz's middle-extension trace formula at \(1\) and weights at most \(2r-1\) give absolute bound \(r m/\sqrt p\). Repetitions within either list and a trivial label on one side are allowed. See [Katz, From Clausen to Carlitz, Sections 2.1–2.3](https://web.math.princeton.edu/~nmk/clauscar53.pdf).

In the true covariance let \(j\) be the maximal number of disjoint opposite matches. Sum the eight possible matching equations inclusively, counting each individually. For \(j\ge2\), every selected equation is a match and Round 167's estimates still apply after the bounded multiplicity. When \(j=1\), a repeated count is possible if two match equations share a slot. At fixed \(h=\psi'/\psi\), any two distinct match equations are two independent constraints on a forest of draw slots. Their joint mass is \(O(\kappa^2)\): condition on the shared slot in the overlapping case, and on one root per edge otherwise. Restricted regular-frequency sums for \(j=1\) are \(O(\sqrt p+8)\) by the complete \(3+3\) bound and the deletion estimate. Thus the discrepancy between the inclusive sum and the true \(j=1\) contribution costs \(O((p^3/m)\kappa^2\sqrt p)=O(p^{3/2})\). No ratio phase is removed. The same bound pays the \(j=1\) terms with \(h=1\) by \(|\ell(1)|\le2\kappa\) and the single-match cap. The subfamily \(\alpha\beta\gamma\delta=\alpha'\beta'\gamma'\delta'\) also costs \(O(p^{3/2})\) within \(j=1\): any selected match leaves at least one unused free slot in the equality of products, giving a second cap factor.

## Positive physical form

Let \(W=(\alpha,\beta,\gamma,\delta)\) have law \(\omega^{\otimes4}\). Label its two plus slots by \(\alpha,\delta\) and its two minus slots by \(\bar\beta,\bar\gamma\). For a slot \(k\) of one of these signs, denote its label by \(a_k(W)\). Let \(R_i(W,\psi)\) be the actual regular indicator, including all exclusions for lift \(i\) and frequency \(\psi\). Define \(D_{i,k}(W,\psi)\) as the phase \(C_i(W)\) times the other three moving Gauss factors with their original conjugations. For each sign \(\sigma\) put
\[
 U_{\sigma,r}(a)=\frac12\sum_{i=0}^1
 \sum_{k\in\sigma}
 \mathbb E_W\!\left[1_{\{a_k(W)=a\}}\,
 R_i(W,a/r)D_{i,k}(W,a/r)\right].
\]
The half is the genuine lift average. For a match \(a'=ha\), \(r=a/\psi=a'/\psi'\), so the selected normalized factors cancel on the regular frequencies. Summing inclusively over the four slot pairs per sign is exactly
\[
 \sum_{\sigma,r}\sum_{a,h}\ell(h)\,U_{\sigma,r}(a)\overline{U_{\sigma,r}(ha)} .
\]
In the physical transform \(\widetilde U(t)=\sum_a U(a)a(t)\), orthogonality rewrites this as
\[
 \mathcal P_1=\frac1m\sum_{\sigma,r,t} g(t)(1-g(t))\,
                      |\widetilde U_{\sigma,r}(t)|^2\ge0 .
\]
Inversion symmetry of \(\ell\) fixes either choice of Fourier sign. All measures, fixed phases, lift restrictions and marked physical weights are still actual. In particular the true \(j=1\) contribution is \((p^3/m)\mathcal P_1+O(p^{3/2})\) in the original normalization. This identifies a positive spectral criterion \(\mathcal P_1=O(p^{-1/2})\), equivalent to the original one-match target up to the paid error. Slot pairs within each sign are consolidated before squaring, and the two sign contributions are summed after squaring; cancellation of signs of \(\ell\) must manifest as physical spectral localization in this form. Bounding the residual correlations individually supplies only \(\mathcal P_1=O(1)\). The zero-match \(4+4\) bound is separate.
