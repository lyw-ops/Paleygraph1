# The true second mean and cumulative mean deficits

Write \(n=(q-1)/2\), \(g_j=\sqrt n\,\mu_j\), \(P_T=\sum_{j=1}^T(1-g_j)^2\), and \(E_j=\|v_j\|^2\) in counting Euclidean norm. Along the eligible primes with \(\tau_p\to0\), the actual second mean has a common limit in \((0.9436066882988,0.9443204269703)\). In particular,
\[
0.013037 < \lim_{p\to\infty}P_2 < 0.013118 .
\]
The law and polynomial inequalities below supply an ordinary proof with outward interval evaluation of the constants. The certified longer prefixes and the fixed-field infinite-tail bound are separate results. [True first two iterates](vanishing-floor-38.md) · [Whole-prefix budget](true-spill-63.md#a-necessary-whole-prefix-energy-bound-for-order-1t-allowance)

## The compact distribution in the true second iterate

Let \(r=\sqrt2\), \(m=2r/\pi\), and \(x_p=\sqrt n\,Ke_0\). Round 38 proves \(g_1\to m\) and
\[
g_2=\mathbb E_n|x_p+K|x_p||+o(1).
\]
The inner absolute value acts entrywise. The replacement costs \(o(1)\) in normalized Euclidean norm even with a varying floor tending to zero. The constant Chebyshev coefficient of \(|x_p|\) is killed by \(K\), and the others are
\[
 b_h=\frac{2m(-1)^{h-1}}{4h^2-1},\qquad
 |r u|=m+\sum_{h\ge1} b_h T_{2h}(u),\quad |u|\le1 .
\]
Here \(x_p/\sqrt{p/n}\) lies in \([-1,1]\), and \(\sqrt{p/n}\to r\). Using this exact empirical scaling changes the absolute value by \(o(1)\). The omitted Chebyshev tail through degree \(2H\) has uniform normalized Euclidean error \(O(H^{-1})\) after \(K\).

At each fixed \(H\) the full-character joint law from rounds 23 and 38 gives the independent compact variables
\[
 X=r\cos\Theta,\qquad W_h=(A_h+B_h)/2,\qquad
 Z_H=\sum_{h=1}^H b_h W_h .
\]
\(\Theta\) is uniform on the circle, and \(A_h,B_h\) are the standard traces of independent Haar matrices in the compact symplectic group of matrix size \(2h\), independent across all lifts and degrees. The two lifts give the factor \(1/2\). Their product monodromy and the Jacobi torus argument apply to every fixed truncation before taking \(H\) to infinity. The finite-field tail error and the \(L^2\) convergence of \(Z_H\) imply \(g_2\to\mathbb E h(Z)\), where \(Z=\lim_H Z_H\) and \(h(z)=\mathbb E|X+z|\). [Exact two-lift normalization and groups](parallel-graph-shapes-23.md) · [Full-character second-step law](vanishing-floor-38.md#4-the-second-iterate-gives-a-further-strict-loss)

Symplectic invariant pairings give \(\mathbb E A_h^2=1\), \(\mathbb E A_1^4=2\), \(\mathbb E A_h^4=3\) for \(h\ge2\), and \(\mathbb E A_h^6\le15\). For the fourth tensor power the three pairings are independent in dimension at least four, with one relation in dimension two. For the sixth tensor power the fifteen pairings span the invariant space. Central symmetry gives zero odd moments. Consequently \(W_h\) has variance \(1/2\), with fourth cumulant \(-1/8\) for \(h=1\) and zero for every \(h\ge2\). Parseval gives
\[
v:=\mathbb E Z^2=1-m^2,\qquad
\mathbb E Z^4=3v^2-\tfrac18(2m/3)^4,\qquad
\mathbb E Z^6\le15v^3 .
\]
For the last inequality write each \(b_h W_h\) as the sum of its two independent trace terms and expand the sixth power. Every surviving term has even exponents and is bounded above by its Gaussian counterpart with the same variance. The same estimate on the tails gives convergence in \(L^6\), which justifies using all three moments for \(Z\). [Stolz, *On the Diaconis–Shahshahani Method in Random Matrix Theory*](https://www.ruhr-uni-bochum.de/imperia/md/content/stochastik/veroeffentlichungen/stolzdsm.pdf)

## A global sextic sandwich

With \(a=1/(\pi r)\) and \(b=a/24\), for every real \(z\),
\[
m+a z^2+b z^4-z^6/500\ \le h(z)\ \le
m+a z^2+b z^4+z^6/200 .
\]
By symmetry use \(z\ge0\). On \([0,r]\), \(h'(z)=(2/\pi)\arcsin(z/r)\). Integrating its series gives the displayed quadratic and quartic coefficients and a nonnegative remainder. The remainder divided by \(z^6\) increases to its value at \(r\) by positive coefficients and continuity. The upper polynomial exceeds \(h(r)=r\) at this endpoint.

For \(z\ge r\) one has \(h(z)=z\). The upper polynomial \(u\) has increasing \(u''\) there. Its gap from \(z\) is bounded below by \(u(r)-r-(1-u'(r))_+^2/(2u''(r))>1/100\). For the lower polynomial \(\ell\), put \(\epsilon=1/500\). The gap \(r-\ell(r)\) is positive. The derivative of \(z-\ell(z)\) is positive since
\[
\sup_{z\ge0}(2az-3\epsilon z^5)+\sup_{z\ge0}(4bz^3-3\epsilon z^5)
= \frac{8a}{5}\left(\frac{2a}{15\epsilon}\right)^{1/4}
 + \frac{8b}{5}\left(\frac{4b}{5\epsilon}\right)^{3/2}<1 .
\]
The strict comparisons are outward-checked directly. Taking expectations gives the first two means and the \(P_2\) interval stated above. At any eligible depth \(T\ge2\) in the marked window, monotonicity gives \(P_T\ge0.013037-o(1)\). The round-63 gate then requires \(2Ts+T(1-1/n)\tau_p\ge0.013037-o(1)\) for any successful common extra mean \(s\) preserving both marks. A growing lower bound as the fixed prefix length increases is still open. [Outward computation](mean-energy-64-check.py)

## Certified finite prefixes and a fixed-field tail

At zero floor, \(\Phi_0(v)=\sqrt{4+v_0^2}\) and \(\Phi_i(v)=|v_i|\) off the mark. The true trajectory starts from zero and iterates \(K\Phi\). The checker encloses the exact transform of a dyadic center and accumulates each Euclidean defect as a counting norm error \(e_t\). Both \(K\) and \(\Phi\) are nonexpansive, so the mean error is at most \(e_t/2\) by Cauchy–Schwarz. One further exact transform of the center at depth \(T\), with the same error radius, encloses \(E_{T+1}\). Float FFTs only propose the centers.

| Field | Actual \(P_{512}\) | Actual \(E_{513}\) | Additional certified information |
| --- | --- | --- | --- |
| Prime \(9413\) | \((0.01154,0.01155)\) | \(<6\) | \(P_{512}-P_{16}<10^{-4}\) |
| Square \(97^2\) | \((1.165,1.166)\) | \(>96\) | \(P_{16}<0.016438\) |
| Prime \(97\) | \(>0.00972\) | \((5.8168,5.817)\) | \(P_\infty<0.0103\) |

The infinite tail at \(p=97\) uses exact complementary ordinary optimizers \(P,N\) of sum one from round 54. The vector \(w=\sqrt n(P-N)\) is a zero-floor fixed point. Complementarity gives disjoint bulk supports and marked product \(nP(0)N(0)=1\), so \(\Phi(w)=\sqrt n(P+N)\). The exact distance decrement of round 47 gives
\[
\|v_j-w\|^2-\|v_{j+1}-w\|^2\ge4(g_j-1)^2 .
\]
Thus \(P_\infty-P_{512}\le\|v_{513}-w\|^2/4\). The checker bounds the distance using the image of the dyadic center and the inherited radius. The finite square control shows substantial growth beyond time sixteen, while the certified primes in this table permit small cumulative losses. The bounds on the primes apply to those fixed fields. [Exact face](astra-face-54.md) · [Distance decrement](astra-secant-47.md) · [14 replay records](mean-energy-64-checks.jsonl)

## Ranked next tests

1. Use the actual two-step law to approximate the third mean, with a uniform \(L^2\) error at each cutoff and the arithmetic return of \(K\) on the entire retained word family. A strict field-first enclosure of \(g_3\) away from one increases the necessary constant. Unbounded accumulation would require a sequence of certified fixed prefixes whose losses grow without bound.
2. For one actual depth in a growing marked window, seek \(s=o(1)\) with the signed worst-site bound that makes the pinned reflection nonnegative on both rows. Track \(P_T\) and the terminal energy for the same branch and depth. Failure for every \(C/T\) rejects that scale. Larger vanishing allowances still merit a separate test.
