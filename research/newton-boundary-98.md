# One physical Newton correction at the first comparison boundary

At a first activation of the selected near-flat comparison, a single exact Newton correction to the complex height-100 predictor leaves a pointwise error at most \(124600\sqrt n\,r^2\), with \(r\) the actual normalized second norm of the predictor residual at that floor. A Cauchy contour estimate on that correction forces \(\sqrt n\,r^2>1.4\cdot10^{-9}\) on the **full** nominated square, for all sufficiently large eligible primes. On a fixed interior strip the bound is \(2.3\cdot10^{-9}\).

## The nonlinear remainder after the Newton step

Set \(a=2031/128\), \(h=2^{-17}\), \(L=a-h\), \(Q=\{|\Re t-a|\le h,\ |\Im t|\le h\}\), and \(t_0=n,\ t_i=t\) in the bulk. Use the physical operator \(K\) and activation \(\Phi_t(u)_i=\sqrt{4t_i+u_i^2}\), with the phase of each root as specified by the positive real branch. At a first activation of the [selected real profile](astra-count-96.md#stop-at-the-first-boundary-of-the-selected-real-profile) its complex reconstruction \(U\) solves \(U=K\Phi_t(U)\) with these bulk and marked parameters. The first activation has unit bulk products in the reconstruction. Write \(U_i=2\sqrt{t_i}\sinh z_i\), with the relative logs \(z_i\) from the [same-floor comparison](same-floor-97.md#the-actual-first-boundary-lag-is-residual-scale).

Use the actual nine-center row \(W=V_{100}(t)\), \(R=K\Phi_t(W)-W\), \(r=\|R\|_{2,n}\), and set \(D=\operatorname{diag}\Phi'_t(W)\). Let
\[
  H=\sum_{k\ge0}(KD)^k R,\qquad Z=(I-KD)^{-1}K,\qquad
  \Delta=U-W,\qquad B=\Phi_t(W+\Delta)-\Phi_t(W)-D\Delta.
\]
The [round-82 physical price](astra-adjoint-82.md#physical-packet-prices-for-the-actual-derivative) gives \(q=0.984138\) as a strict upper rate on represented rows and \(\|R\|_\pi<0.001180\), so \(\|H\|_\infty<0.075\) on \(Q\). The [seed-centered coordinate disks](astra-source-88.md#the-seed-centered-disks-on-the-complex-square) also give \(\|D\|_{2\to2}<0.51358\) on the whole square. Thus \(H\) is holomorphic in the interior of \(Q\) and \(H=(I-KD)^{-1}R\) on \(Q\). It is real on the real part of \(Q\).

Subtracting the two equations gives \(\Delta=R+KD\Delta+KB\) and hence \(U=W+H+ZB\). For \(|\Delta_i|\le1\), the straight segment \(v=W_i+s\Delta_i\) has \(|\Im v|<3\), since \(|\Im W_i|<2\). On this segment the real part of \(4t_i+v^2\) exceeds \(4\Re t_i-9\). The root along the segment gives the prescribed endpoint activation: for the predictor and the exact pair the logarithmic phases lie strictly inside \(\pi/4\) in absolute value, and \(|\arg(\sqrt{t_i})|<10^{-6}\), so both corresponding activations have positive real part. Since
\[
  |\Phi''_{t,i}(v)|\le \frac{4|t_i|}{(4\Re t_i-9)^{3/2}}<0.2
\]
in both the bulk and the mark, the Taylor integral gives \(|B_i|\le0.1|\Delta_i|^2\). On the remaining coordinates the exact secant is \(\tanh((z_i+g_i)/2)\), where \(g_i=\operatorname{arsinh}(W_i/(2\sqrt{t_i}))\). This secant has modulus less than one by the phase bounds. Thus \(|B_i|\le1.514|\Delta_i|\) there. The actual secant loss comparison at the first activation gives \(\|\min(|\Delta|^2,|\Delta|)\|_{1,n}\le462r^2\). In particular \(\|B\|_{1,n}<700 r^2\) if \(r>0\); when \(r=0\), \(B=0\). The [translated-source entry estimate](shifted-resolvent-96.md#consequences-for-the-full-linearized-inverse) gives \(\max_{i,j}|Z_{ij}|\le178/\sqrt n\) eventually, uniformly in \(t\), for this particular complex multiplier \(D\). Therefore
\[
   \|U-W-H\|_\infty
     \le \frac{178}{\sqrt n}\sum_j |B_j|
     \le 124600\sqrt n\,r^2.                                           \tag{1}
\]
The factor \(\sqrt n\) in (1) converts from the normalized first norm; the estimate uses the translated bound for **every** physical source.

## A common interior strip and a finite test on the full square

At a hitting bulk site the exact first-boundary identity gives \(|\sin\Im z_i|=10^{-4}/\sqrt3\). Since \(\Im(U_i/\sqrt t)=2\cosh(\Re z_i)\sin(\Im z_i)\), the magnitude of this imaginary part is at least \(2\cdot10^{-4}/\sqrt3\). In the strip
\[
   Q_{\rm in}=\{|\Re t-a|\le h/2,\ |\Im t|\le h/1000\},
\]
write \(t=T+iy\). Cauchy's estimate along \([T,t]\) bounds \(|H_i'(s)|\) by \(0.075/(h/2-|y|)\) because the disk of radius \(h/2-|y|\) about every such \(s\) lies in \(Q\). The [same-floor time estimate](same-floor-97.md#transporting-the-nominal-real-reflection) gives \(\|W'(s)\|_\infty<21\) eventually. Using real values at \(T\), \(\|W+H\|_\infty<4.843\), and the derivative of \(1/\sqrt t\) then gives
\[
 \left|\Im\frac{W_i(t)+H_i(t)}{\sqrt t}\right|
 \le \frac{21|y|+0.075|y|/(h/2-|y|)}{\sqrt L}
     +\frac{4.843|y|}{2L^{3/2}}
 < 4\cdot10^{-5}.
\]
After rotating and rescaling (1), the first-hit angle lower bound forces
\[
   \sqrt n\,r^2 >
   \frac{\sqrt L}{124600}
        \left(\frac{2\cdot10^{-4}}{\sqrt3}-4\cdot10^{-5}\right)
   > 2.3\cdot10^{-9}.
\]
This holds at every first activation lying in \(Q_{\rm in}\) for sufficiently large eligible primes. It also applies to a first activation anywhere on a vertical ray segment from \(Q_{\rm in}\cap\mathbb R\) staying in \(Q_{\rm in}\).

On **all** of \(Q\), define the finite nominal correction \(H_{750}=\sum_{k=0}^{749}(KD)^kR\), in the actual group. The packet estimate gives \(\|H-H_{750}\|_\infty\le0.075 q^{750}<5\cdot10^{-7}\). From (1) a first activation implies either
\[
 \sqrt n\,r^2>10^{-9}
 \qquad\text{or}\qquad
 \max_{i\ne0}\left|\Im\frac{W_i+(H_{750})_i}{\sqrt t}\right|>8\cdot10^{-5}.
\]
Indeed if the first inequality fails then the two errors after division by \(\sqrt L\) sum to at most \((124600\cdot10^{-9}+5\cdot10^{-7})/\sqrt L\). The second term in the alternative involves only the fixed-depth physical prefix and its linearization, with no unknown midpoint weights. The interval replay checks the scalar margins. At this fixed height the established \(r<3\cdot10^{-30}\) has no decay with the prime, so (1) does not exclude first activation at unbounded order. [Arithmetic checker](newton-boundary-98-check.py) · [Replay](newton-boundary-98-checks.jsonl)

## Control the Newton correction on the full square

Use the larger square \(Q^+\) with the same center \(a\) and half-width \(1/125\). The center amplitude formulas are analytic there, as in the [initial time-source estimate](same-floor-97.md#transporting-the-nominal-real-reflection). The [contour replay](newton-contour-98-check.py) reapplies the [actual forward packet comparison](astra-predictor-76.md#a-finite-comparison-for-the-complete-nine-center-predictor) on \(Q^+\) with the same degree, weight cuts and exceptional budget. The cap through height 100 is \(4.8\). All physical square-root arguments through \(\Phi_t(V_{100})\) have positive real part, and \(\|KD\|_{2\to2}\le 4.8/\sqrt{4(a-1/125)-4.8^2}<1\), including at the mark where \(t_0=n\). Thus the exact \(H=(I-KD)^{-1}R\) is analytic on a neighborhood of \(Q^+\). This analyticity uses only the physical coordinate cap on \(Q^+\).

Split each edge of \(Q^+\) into eight segments of equal length and use reflection across the real axis on the bottom edge. On each remaining edge segment \(S\), re-enclose the forward packets on \(S\) and charge each derivative step in the [round-82 price](astra-adjoint-82.md#physical-packet-prices-for-the-actual-derivative). The retained coefficient for arity \(j\) in the derivative comes from \(jU_j\) convolved with the \((j-1)\)-fold power of the residual packet envelope. The difference of full and retained tilted masses, with the derivative of the unexpanded binomial tail, is charged at \(10\) times its tilted norm. The derivative exceptional budget stays below \(10^{-12}\), since the uncollected dimensional derivative series remains below one and the [marked and lift repairs](astra-adjoint-82.md#physical-packet-prices-for-the-actual-derivative) apply on the same bounded coordinates. Let \(q_S<1\) denote the resulting height-100 rate and \(r_S\) the product bound on \(\|R\|_\pi\) using the 100 successive rates. Write \(M_S=r_S/(1-q_S)\); it bounds each coordinate of \(H\) on \(S\) by the physical Neumann series there.

Cauchy's formula for every \(t\in Q\) gives
\[
 |\partial_t H_i(t)|\le
       \frac{1}{2\pi}\sum_{S\subset\partial Q^+}
       \frac{|S| M_S}{\operatorname{dist}(Q,S)^2}.
\]
For each segment the squared distance is bounded below by \((1/125-h)^2\) plus the squared distance of its tangential interval from \([-h,h]\), in coordinates centered at \(a\). Retaining the edge segments separately gives a bound below \(15.811\). Along the vertical segment from \(T\), the previous bound \(21\) for \(\|W'\|_\infty\), reality at \(T\), and \(\|W+H\|_\infty<4.843\) on \(Q\) now give
\[
 \max_{i\ne0}\left|\Im\frac{W_i(t)+H_i(t)}{\sqrt t}\right|
 <7.1\cdot10^{-5}\qquad(t\in Q).
\]
The physical angle lower bound and (1) therefore force
\[
 \sqrt n\,r^2>\frac{\sqrt L}{124600}
     \left(\frac{2\cdot10^{-4}}{\sqrt3}-7.1\cdot10^{-5}\right)>1.4\cdot10^{-9}.
\]
The first-boundary conclusion is eventual, using the translated-source estimates and the derivative bound for \(W\). The fixed-height normalized residual bound \(r<3\cdot10^{-30}\) stays constant through primes. The unresolved estimate is an upper on \(\sqrt n\,r^2\) for a calibrated growing-height predictor, or direct signed cancellation of \(ZB\) on the actual first row. [Arb192 contour checker](newton-contour-98-check.py) · [Replay](newton-contour-98-checks.jsonl)

1. Seek the same comparison for a growing-height family with \(\sqrt n\,r^2\to0\), retaining a quantitative imaginary margin and bounded translated inverse estimates.
2. At fixed height estimate \(\left|\Im((ZB)_i/\sqrt t)\right|\) on the actual first row. A uniform upper below \(2\cdot10^{-4}/\sqrt3-7.1\cdot10^{-5}\) excludes a first activation.
