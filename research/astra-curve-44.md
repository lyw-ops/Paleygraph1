# Actual cold-to-hot strips and signed cubic variation

Fix a real floor interval \([a,T]\) with \(0<a<1\), \(T=2048\), and put \(L=\log(T/a)\). The physical branch at prime 173 has a verified section across this entire interval at \(a=1/32\), even though a wider section is ruled out by actual marked monodromy. The square 121 also has both lower and upper width certificates. Its signed third derivative has more than three times the integrated absolute value of the prime's on the same interval. These are two finite fields. The hot theorem's large-field hypothesis does not hold at \(T\) for them.

| Field | Certified angular half-width | Obstruction to a half-width of | Supremum of the absolute third derivative | Integral of the absolute third derivative |
|---|---:|---:|---:|---:|
| Prime 173 | 0.077 | 0.820 | (0.01973, 0.01993) | (0.06082, 0.06189) |
| Square 121 | 0.125 | 1.288 | (0.10297, 0.10404) | (0.18795, 0.19173) |

Here \(f(s)=m(Te^{-s})\), \(0\le s\le L\), for the actual plus marked logarithm. Angular half-width \(\omega\) means \(a\le|t|\le T,\ |\arg t|<\omega\). For the prime, the entire [certified physical approach and loop](astra-cold-37.md) satisfy this condition at 0.820, since \(\arctan(0.03527/0.0330)<0.820\). Their terminal scalar balls are disjoint. For the square, the round-37 coefficient obstruction at Cayley radius \(3/4\), center \(3/4\), is contained in this strip at 1.288. Indeed the Cayley disk has maximal angle \(2\arctan(3/4)<1.288\) and radial range \((3/28,21/4)\). The square upper certificate uses a genuine marked singularity detected by a Taylor coefficient. Neither upper bound is inferred from numerical continuation failure.

## Relative tubes with the strip metric constant

For all sufficiently small \(\delta>0\), write \(D_\delta=\bigcup_{a\le x\le T} B(x,\delta x)\). If there is a physical marked section on \(D_\delta\), then the curvature-minus-one distance on the [normalized marked surface](marked-surface-37.md) satisfies

\[
 d_Y(y_a,y_T)\le \frac{\pi L}{2\delta}+O(1).
\]

The constant in the error is absolute when \(L>4\delta\). In log coordinates put \(A=\log a,B=\log T\). Every real center \(u\in[A,B]\) has a disk \(|z-u|<\delta/2\) in \(\log D_\delta\), since \(e^{\delta/2}-1<\delta\). The rectangle \(A<\Re z<B-2\delta,\ |\Im z|<\delta\) is also contained there. For \(t=e^{u+iv}\), take \(x=e^u/\cos v\in[a,T]\), which gives \(|t-x|/x=|\sin v|<\delta\).

At the real point \(u\) in the rectangle, let \(h=\min(u-A,B-2\delta-u)\). The infinite horizontal strip has density \(\pi/(2\delta)\) on the axis. The map \(\zeta\mapsto u+(4\delta/\pi)\operatorname{arctanh}\zeta\) takes the disk of radius \(\tanh(\pi h/(4\delta))\) inside the rectangle, since \(|\Re\operatorname{arctanh}\zeta|\le\operatorname{arctanh}|\zeta|\). Thus the density on the rectangle at \(u\) is at most \((\pi/(2\delta))\coth(\pi h/(4\delta))\). Integrate along \([A+\delta,B-3\delta]\). The excess over the infinite-strip density integrates to an absolute constant since \(\int_1^\infty(\coth(\pi v/4)-1)\,dv<\infty\). The omitted axis pieces have total length \(4\delta\) and density at most \(4/\delta\) in the larger log domain, by the centered disks. Inclusion of the section decreases distance, giving the claim.

Consequently for any fixed \(\epsilon>0\), a physical section at \(\delta_n=(\pi/2+\epsilon)L/\log\log n\) through all sufficiently large eligible primes suffices for marked decay at \(a\). Indeed \(\log\log n-d_Y\to\infty\) and round 37 propagates hot smallness. Conversely every sufficiently large square has accessible marked ramification over this thinner relative tube. Otherwise its proper component over the simply connected tube would be an unramified covering, hence admit a section, contradicting the square lower bound \(d_Y\ge\log\log n-O_a(1)\). This improves the earlier sufficient numerator \(2L\) to \(\pi L/2\) without controlling the actual prime section uniformly.

## A posteriori disks with an error bound for the marked logarithm

At a real center \(x\), put \(z=1-x/t\). Use the [stationary Hessian projection](astra-surface-38.md) \(P\) on the relative tangent \(E\), with weights \(w_0=1,w_i=x/n\); all sums count full coordinate multiplicities. The stationary relative displacement solves
\[
 h=\Psi_z(h)=P[h^2/(1+h)]-z Pe_0/(1+h_0).
\]
Let \(H=\sum_{j=1}^N h_jz^j\) be its true Taylor polynomial and \(Q=\sum_{j=0}^N q_jz^j\) the truncated inverse of \(1+H\), coordinatewise. The checker obtains successive jets by expanding \(P[(1-ze_0)/(1+H)]=0\). At radius \(R\), define
\[
 b_i=\sum_j |h_{j,i}|R^j,\quad
 e_i=\frac{1+R\mathbf1_{i=0}}{1-b_i}
       \sum_{j=N+1}^{2N}|[z^j](1+H_i)Q_i|R^j,\quad
 E_R=\|e\|_w+R^{N+1}|q_{N,0}|.
\]
If all \(b_i<1\), then \(\|\Psi_z(H)-H\|_w\le E_R\). Indeed \(\Psi_z(H)-H=P[(1-ze_0)/(1+H)]\), and replacing the reciprocal by \(Q\) leaves only the degree-\(N+1\) marked term after projection. The discarded reciprocal tail has the displayed coordinate bounds and \(P\) contracts the weighted norm.

Take \(d=1/64\), \(b=\max b_i+d\), \(r=d\sqrt{\min(1,x/n)}\). On the weighted ball of radius \(r\) centered at \(H(z)\), all coordinates have modulus at most \(b\). When \(b<1\), a Lipschitz constant for \(\Psi_z\) on that ball is
\[
 \lambda=(1-b)^{-2}-1+R(1-b)^{-2}.
\]
This follows from the power series derivative of \(y^2/(1+y)\), and \(\|Pe_0\|_w\le1\), \(|h_0|\le\|h\|_w\). Whenever \(E_R<(1-\lambda)r\) and \(\lambda<1\), iteration gives the physical germ on the disk, and its marked logarithm differs from the polynomial predictor's logarithm by at most
\[
 \Delta_R=E_R/[(1-\lambda)(1-b)].
\]
The last factor bounds the derivative of the logarithm on the segment between the two marked entries. The real solution is positive at the center, and uniqueness identifies the germ. The images of \(|z|<R\) in the \(t\)-plane are disks with real centers. Every nonempty pairwise intersection is connected and meets the positive axis, where positivity and uniqueness glue the sections.

The checker uses 96 centers from \(1/32\) to 2048 with consecutive ratios at most \(U=9/8\). Each disk passes at degree 12 with \(R=1/10\) at prime 173 and \(R=1/7\) at square 121. With the center nearest in log modulus, \(U^{-1/2}\le x/|t|\le U^{1/2}\). Therefore
\[
 |1-x/t|^2\le (\sqrt U-1)^2+\sqrt U\,(\arg t)^2.
\]
This proves the angular widths in the table.

## Certifying the signed spatial cancellation over the whole interval

The eight fixed-floor records include both \(M_4=\sum w_ic_i^4\) and \(2\|P(c^2)\|_w^2\), where \(c=Pe_0\). At prime 173, floor 1, the numbers lie in \((0.08737298,0.08737300)\) and \((0.08703663,0.08703665)\); their signed difference lies in \((0.00033634,0.00033636)\). It is only one term of the full physical cubic. At floors \(1/20,1/4,1\) that third derivative has signs \(-,+,-\). At every center the first three derivatives from the [signed Hessian formula](astra-complex-39.md) are checked against an independent Taylor recurrence on the complementary quadratic system \(s^2-(Ks)^2=4w\).

For a whole real center cell use \(v=\log(x/t)\). The physical predictor, up to an additive constant, is
\[
 g(v)=\log(1+H_0(1-e^v))+
 \tfrac12\log[(1-(1-e^v)/W)/e^v],\qquad W=\sum w_i.
\]
The disk \(|v|<\log(1+R)\) maps into the verified \(z\)-disk. For real \(v\) in the cell the physical third derivative differs from \(g'''(v)\) by at most \(6\Delta_R/(\log(1+R)-\max_{\rm cell}|v|)^3\) by Cauchy's inequality. The checker combines \(g'''\) into a single rational function of \(z\) before real interval evaluation. Each cell uses 32 closed subintervals. For the integral it sums their lengths times upper and nonnegative lower bounds on the absolute derivative. For the supremum it also evaluates every subinterval midpoint. The projected stationary Hessian, independent complementary recurrence, contraction constants, signed polynomial and quadrature bounds all use Arb at 224 bits.

Replay the [ten records](astra-curve-44-checks.jsonl) with the [checker](astra-curve-44-check.py) from the repository root:

~~~sh
OPENBLAS_NUM_THREADS=1 .venv/bin/python -B research/astra-curve-44-check.py
~~~

## Ranked next tests

1. Bound the true section width \(\delta_p(a)\), or the integral of the local strip density on varying widths, through growing primes. The sufficient target is \(d_Y\le\log\log n-\omega(1)\), achieved in the constant-width case above \((\pi/2+\epsilon)L/\log\log n\). A regularity obstruction needs an accessible marked singularity or disjoint marked return enclosures in the proposed domain. A failed predictor only leaves its width uncertified.
2. Extend the combined rational-numerator certificate to growing fields and the absolute integrals of higher signed real derivatives. A common sequence of bounds \(D_j\) with the divergent quotient sum of round 39 would propagate decay. A validated lower integral above one proposed bound refutes that bound. The finite separation at order three establishes neither an infinite hierarchy nor an asymptotic prime-square gap.
