# Two physical cuts at first comparison contact

On the nominated square, the actual signed Jacobi cut behaves differently at two nearby primes. At \(p=173\) the maximum, over **all** pairs of levels, of the minimum after four individual erasures is \(0.1794952084091210\ldots\). At \(p=181\) a single fixed pair has minimum \(0.8733915702384228\ldots\) after four individual erasures. Both statements hold over the *whole* square off its real diameter, including the first comparison contact on every vertical half-ray at the common cutoff \(\delta=2\cdot10^{-14}\). This gives a physical obstruction to using \(0.2910\) independently of the cutoff and prime. Both primes stay below the nominated \(\delta=10^{-8}\) throughout this square.

For sufficiently large eligible primes at the nominated first contact, the [height-100 same-floor predictor](same-floor-97.md) reduces the remaining question to a smaller rectangle of levels or a signed sum of actual outlying coordinates. If every cut on \(0\le u\le0.52, 0\le v\le0.4\) has minimized discrepancy at most **one**, more than \(0.5740\sqrt n\) sign-aligned outlying sites must contribute. The signed excess from this region remains above \(0.0830\) after *any* \(\lfloor\sqrt n/2\rfloor\) additional erasures, in the sense of (4) below. Conversely if \(n^{1/4}r\le10^{-6}\), some single cut in this smaller rectangle has discrepancy greater than **4.0538** after every admissible erasure. Here \(r\) is the normalized second norm of the actual complex predictor residual on this floor. The nominated first contact through unbounded primes remains open.

## Split the actual signed layer integral

Fix a vertical ray at \(t=T+iy\) in the nominated closed square and its first unit-bulk comparison contact at \(t_*=10^{-4}\), with \(n=(p-1)/2\). On the bulk the actual midpoint coordinates obey \(X_j^2=3(1-w_j)\) and \(|X_j|\le t_*\), with equality somewhere. Use the [bare Jacobi identity](astra-signed-97.md#one-fixed-physical-site-for-all-deletions) at an individual site \(k\) maximizing \(|V_k|=P\), where \(V_j=\cosh(\gamma_j)X_j\). Thus \(P\ge t_*\). Put
\[
 d_j=|\tanh\gamma_j|,\qquad e_j=|V_j|/P,\qquad
 c_j=K_{kj}\operatorname{sgn}(X_k\gamma_jX_j),\qquad j\ne0.
\]
All sums below are ordinary individual-site counting sums. At \(n\ge10^{30}\), \(|c_j|\le\mu=1.415/\sqrt n\), and removal of the explicit mark gives
\[
                  \sum_{j\ne0}c_jd_je_j>1-1.480\cdot10^{-7}/t_*
                               =0.99852.                              \tag{1}
\]
For levels \(u,v\) let \(C(u,v)=\sum_j c_j 1_{d_j>u,\ e_j>v}\). Write \(C_m(u,v)\) for its minimum after deleting up to \(m=\lfloor\sqrt n/2\rfloor\) arbitrary individual bulk sites. It is obtained by deducting the \(m\) largest positive contributions, using all if there are fewer. Thus \(C(u,v)\le C_m(u,v)+0.7075\). This comparison permits a fresh deletion after seeing both levels.

Take \(a=0.52, b=0.4\) and introduce the *excess weight*
\[
             L_j=d_je_j-\min(d_j,a)\min(e_j,b).
\]
It vanishes unless \(d_j>a\) or \(e_j>b\) and lies in \([0,1-ab]\), as is seen by monotonicity in both coordinates. Fubini on the low rectangle gives the exact signed decomposition
\[
  \sum c_jd_je_j=\int_0^a\!\int_0^b C(u,v)\,dv\,du+\sum c_j L_j.        \tag{2}
\]
In particular if every such minimized cut is at most \(U\), then
\[
                 \sum c_jL_j>0.99852-ab(U+0.7075).                    \tag{3}
\]
For \(U=1\) the right side is \(0.64336\). Each positive summand costs at most \((1-ab)\mu\), so more than \(0.5740\sqrt n\) actual sites simultaneously have \(c_j>0, L_j>0\). For **every** \(S\subseteq G\setminus\{0\}\), \(|S|\le m\), the same signed, weighted excess satisfies
\[
                       \sum_{j\notin S\cup\{0\}}c_j L_j>0.0830 .       \tag{4}
\]
The deletion in (4) can be chosen after the physical row is known, independently of the deletions used to minimize individual cuts. It is applied to the original excess sum in (3).

## Price the high levels by the genuine complex residual

Use \(W=V_{100}(t)\) for the arithmetic predictor in its original, unnormalized-factor scaling, \(U^{\rm stat}\) for the stationary factor difference in the same scaling, and \(\Delta=U^{\rm stat}-W\). Let \(r=\|K\Phi_t(W)-W\|_{2,n}\), with squared norm \(n^{-1}\sum|\cdot|^2\). The [same-floor comparison](same-floor-97.md#the-actual-first-boundary-lag-is-residual-scale) gives
\[
 \sum h_j^2<4nr^2,\qquad
 \sum\min(|\Delta_j|^2,|\Delta_j|)\le462nr^2,\qquad
 h_j=2\sinh((\gamma_j-\Gamma_j)/2).
\]
On the bulk \(|\tanh\Gamma_j|<0.514\), so \(d_j\le0.514+|h_j|\). For the imaginary row use the unit bulk factorization: up to the common ray sign, \(V_j=(\sqrt3/2)\Im(U^{\rm stat}_j/\sqrt t)\). Define \(V_j^0\) by the same formula with \(W\) and the same sign. Put \(H=2^{-17}\), \(T_-=2031/128-H\). The same-floor analytic calculation bounds \(\|\partial_t W\|_\infty<21\) on the square and \(|W_j|\le4.768\). Since \(W(T)/\sqrt T\) is real, integration along the vertical line yields
\[
 |V_j^0|\le B=\frac{\sqrt3}{2}H
      \left(\frac{21}{\sqrt{T_-}}+\frac{4.768}{2T_-^{3/2}}\right)
 <3.509\cdot10^{-5}.
\]
Consequently \(e_j\le B/t_*+\lambda|\Delta_j|\), where \(\lambda=\sqrt3/(2\sqrt{T_-}\,t_*)\).

For \(x\ge0, s>0\) one has \((x-s)_+\le x^2/(4s)\). The excess therefore admits a useful integrated bound. First,
\[
     L_j\le(d_j-a)_++a(e_j-b)_+ .
\]
The first term is bounded by \(h_j^2/[4(a-0.514)]\). Write \(s=b-B/t_*>0\). When \(|\Delta_j|\le1\) the second positive part \((e_j-b)_+\) is at most \(\lambda^2|\Delta_j|^2/(4s)\). For \(|\Delta_j|\ge1\) use \(e_j\le1\) and \(\lambda^2/(4s)>1\). Thus, *before* multiplying by Jacobi coefficients,
\[
 \sum L_j\le n r^2 D,\qquad
 D=\frac1{a-0.514}+\frac{462a\lambda^2}{4(b-B/t_*)}<5.773\cdot10^9.     \tag{5}
\]
Combining (1), (2), (5) gives the following statement at every such first contact, for all sufficiently large eligible primes:
\[
 \max_{0\le u\le a,\ 0\le v\le b} C_m(u,v)>
    \frac{0.99852-1.415D(n^{1/4}r)^2}{ab}-0.7075.                      \tag{6}
\]
At \(n^{1/4}r\le10^{-6}\) the right side exceeds \(4.0538\). If the maximum is at most one then \(n^{1/4}r>8.874\cdot10^{-6}\). The predictor is at fixed height; its uniform normalized residual bound \(3\cdot10^{-30}\) does not ensure this conditional regime for arbitrarily large \(n\).

## Whole-square finite physical tests

Write \(H=2^{-17}\). At either prime let \(Y\) be the normalized stationary factor difference solving \(Y=K\sqrt{Y^2+4w^c}\), \(w^c_0=n/t, w^c_j=1\) off zero, with the positive square root. The factors \(A,B=(\sqrt{Y^2+4w^c}\pm Y)/2\) have equal means in the two complementary sectors. The [checker](astra-cuts-98-check.py) constructs a real center at \(2031/128\), then proves contraction on one full counting second-norm ball of radius \(10^{-5}\) centered there, uniformly over the square. The center residual splits into its real value and the one changed marked square root; \(K\) contracts in the full counting norm. The ball is invariant, the multiplier norm is below \(0.208\), and positivity of both real parts is checked on an enclosing box. This identifies the actual analytic real-start branch at every floor. The even representation uses multiplicity two except at the two fixed orbits.

The enclosed real-center derivative solves the differentiated equation. To enclose the derivative throughout the square, insert this same vector in the differentiated equation at variable \(t\), bound the residual in the full counting norm, and divide by one minus the uniform contraction bound. By the reality of the branch at real \(T\), \(\Im Y(T+iy)/y\) is the vertical average of \(\Re Y'(T+is)\). The box for this ratio works on both half-rays down to arbitrarily small nonzero \(|y|\). The real-amplitude cut uses \(\tanh\gamma_j=\Re Y_j/\Re\sqrt{Y_j^2+4w^c_j}\). In the imaginary ratio and in the sign \(\operatorname{sgn}(X_k\gamma_jX_j)\) the common imaginary-row scale and ray sign cancel.

* At \(p=173\), \(n=86\), orbit 16 maximizes the imaginary row. Both orders of the 43 positive bulk orbit levels are strict throughout the square. All \(44^2\) pairs of prefixes, including empty masks, are tested on individual sites. The largest untrimmed cut is \(0.7867180002936899\ldots\); the largest optimally trimmed cut is \(0.1794952084091210\ldots\). The budget is four individual sites for each pair of levels.
* At \(p=181\), \(n=90\), orbit 26 maximizes the imaginary row. On the whole punctured square the rational levels \(u=0.16324, v=0.75\) give the same 34 individual sites with the same signs. The untrimmed value is \(1.465288172848840\ldots\); removing the four largest individual positive contributions costs \(0.5918966026104167\ldots\), leaving \(0.8733915702384228\ldots\). All level and orientation decisions and the optimal debit use outward arithmetic.

At both primes the identity \(X_j^2=(3/4)(\Im Y_j)^2(1-\tanh^2\gamma_j)=3(1-w_j)\) checks the cutoff scale. At the edge \(|y|=H\), for every \(T\), the peak site exceeds \(2\cdot10^{-14}\) in \(X^2\); the whole square stays below \(2.5\cdot10^{-14}\). The real row has \(X=0\), so each half-ray has a first contact with \(\max X_j^2=2\cdot10^{-14}\). Up to and including this contact the actual unit-product row is the [unique clamped comparison](astra-tie-95.md#construction-from-real-positive-optimizers): its endpoint products \(1-X_j^2\) satisfy the lower floor and it solves the unit branch of the clamped equations. At the nominated \(10^{-8}\) cutoff both primes thus admit the unit branch throughout. The \(p=181\) obstruction concerns an actual first comparison row for the specified smaller cutoff; the asymptotic implication at \(10^{-8}\) uses the distinct marked-source bound in (1). [Three Arb256 records](astra-cuts-98-checks.jsonl)

1. Bound the signed low-rectangle integrals on the nominated physical row, retaining the factorization into actual real amplitude and relative imaginary level. A uniform minimized upper of one forces the outlying signed mass (3) and (4); in the stated residual regime even a bound of four excludes contact.
2. Estimate the signed excess \(\sum c_jL_j\) directly after erasing its largest paying sites, using its support on the actual departures above the bounded predictor rectangle. A bound at most \(0.0830\) for one permitted deletion, together with the low-cut bound of one, excludes the first activation.
