# Actual cold marked ramification at primes 113 and 173

The physical scalar at prime 173 has an accessible branch point in the closed rectangle

\[
  |\Re\tau-0.0331|\le 0.0001,\qquad
  |\Im\tau-0.03517|\le 0.0001.
\]

A certified loop changes the marked value itself. Complex conjugation gives a second rectangle in the lower half-plane. The physical scalar at prime 113 also has a certified right-half-plane branch point. The square control at order 121 admits a finite obstruction of the same kind. These results rule out full right-half-plane continuation at two actual primes. They allow eventual common cold–hot domains in a thinner neighborhood of the real interval. Problem 26 remains open.

There is also a quantitative relaxation for growing primes. A field-dependent domain can suffice even when its width tends to zero. In the curvature-minus-one hyperbolic metric, hot-to-cold distance at most $\log\log n-\omega(1)$ suffices. Section 4 gives the estimate, an explicit tube-width consequence, and the obstruction it yields through squares.

## 1. A scalar coefficient test on a disk

Use the positive stationary branch, $m=\log A_0$, and the [accepted scalar phase theorem](parallel-cold-complex-36.md). Fix $a>0$, write

\[
 t(h)=a(1+h)/(1-h),\qquad m(t(h))=\sum_{k\ge0}c_k h^k .
\]

The $c_k$ are real. If this scalar germ extends holomorphically to $|h|<R\le1$, then $|\Im m|<\pi/4$ there. At radius $r<R$, the sine coefficient identity gives, for every $k\ge1$,

\[
 |c_k|r^k=\left|\frac1\pi\int_0^{2\pi}
       \Im m(t(r e^{i\theta}))\sin(k\theta)\,d\theta\right|
 \le \frac1\pi\frac\pi4\int_0^{2\pi}|\sin(k\theta)|\,d\theta=1.
\]

Let $r\uparrow R$. Consequently one strict inequality $|c_k|R^k>1$ proves that the **actual Taylor radius** is strictly smaller than $R$. There is a singularity on its first circle, accessible radially from the marked physical germ. Its image in the $t$-plane lies in the open Euclidean disk with real diameter $(a(1-R)/(1+R),a(1+R)/(1-R))$. The normalized physical marked curve is algebraic. The local winding argument in [round 36, Section 4](parallel-cold-complex-36.md) excludes marked zeros and poles anywhere accessible in the right half-plane. A finite nonzero unramified marked value would also have a local analytic logarithm at this first singularity. It follows that this is genuine marked ramification. No singularity of an unrelated sheet is used.

The computed intervals below are rounded outward in the last column.

| Order | $a$ | $R$ | $k$ | Real diameter of obstructed disk | Certified $\lvert c_k\rvert R^k$ |
|---|---:|---:|---:|---|---:|
| Prime 113 | $1/5$ | $7/8$ | 48 | $(1/75,3)$ | $(3.53672,3.53674)$ |
| Prime 173 | $1/20$ | $3/5$ | 47 | $(1/80,1/5)$ | $(14.23434,14.23436)$ |
| Square 121 | $3/4$ | $3/4$ | 48 | $(3/28,21/4)$ | $(2.06583,2.06585)$ |

An entire-half-plane theorem for the small primes 13 and 17, or for square 25, does not extend to all orders of the same type. The square 121 computation proves an obstruction at a particular manageable order, beyond the inherited asymptotic square-family obstruction. These are finite results. No density statement is asserted.

## 2. Rigorous Taylor computation on the physical branch

Write $s=\sqrt{v^2+4w}$ on the real physical branch and $v=Ks$. Products and quotients here are coordinatewise. At a positive real $t=a$, each $w_i>0$. The derivative of the real Picard map $v\mapsto K\sqrt{v^2+4w}$ on a Euclidean ball of radius $b$ about $x$ has operator norm at most

\[
 L=\max_i\frac{|x_i|+b}{\sqrt{(|x_i|+b)^2+4w_i}},
\]

since $\|K\|_{2\to2}=1$. A strict residual bound $\|K\sqrt{x^2+4w}-x\|_2<(1-L)b$ encloses a fixed point in this ball. The real root gives both positive rows $(s\pm v)/2$ and is the unique physical stationary solution. Two real fixed points must in any event agree, since the derivative maximum is strictly less than one on the compact segment between them. The numerical Picard seed and midpoint Newton updates only propose $x$. The contraction test uses Arb bounds and the Euclidean norm on all $n$ coordinates, counting folded even orbits with their multiplicities, including each singleton exactly once. The certificate uses the inverse DFT of the integer Paley multiplier and sums inverse orbit columns to restrict the real circulant matrix to even rows.

Put $s=\sum s_jh^j$, $v=\sum v_jh^j$, and $D=\operatorname{diag}(v_0/s_0)$, where the subscripts here denote Taylor order. Comparing coefficients of $s^2-v^2=4w$ and $v=Ks$ gives

\[
 s_k=(I-DK)^{-1}\operatorname{diag}(2s_0)^{-1}
  \left(4w_k+\sum_{j=1}^{k-1}(v_j v_{k-j}-s_j s_{k-j})\right),
 \qquad v_k=Ks_k.
\]

Here $(4w_k)_0=0$ at the marked coordinate for $k\ge1$, and each other coordinate equals $8a/n$. The inverse exists since $\|D\|<1$ on the real branch, using the full Euclidean norm before restricting to even rows. For the marked derivative use $m'=v'(0)/s(0)$, with the prime denoting differentiation in $h$ and $(0)$ denoting the marked spatial coordinate. This follows from $m=\operatorname{arsinh}(v(0)/2)$ and $s(0)^2=v(0)^2+4$. Coefficient comparison uniquely determines $c_k$. The [640-bit certificate](astra-cold-37-certified.jsonl) records the three resulting enclosures. The proof only requires the corresponding strict test against one. This computation does not assume a transformed Pick criterion or extrapolate from positive finite minors.

## 3. Localized physical monodromy at prime 173

For a direct local test use the polynomial system in the compressed even row $s$,

\[
 F(s,t)=s^2-(Ks)^2-4w(t)=0,\qquad
 J(s)=2\operatorname{diag}(s)-2\operatorname{diag}(Ks)K .
\]

There is no choice of a complex square root in this system. At the positive real base $t=331/10000$ the preceding contraction encloses the physical root. Along any regular continuation from there, $v=Ks$ and $A=(s+v)/2$, $B=(s-v)/2$ continue that pair with $AB=w$ coordinatewise. Their means, sector constraints and physical mean normalization continue by analyticity. In particular, the extracted scalar $A_0$ is the actual marked germ. Each weight is nonzero throughout the path.

Here is the interval proof for one segment. The parameter travels along a straight segment with real parameter $u\in[0,1]$. Let $z(u)=(1-u)z_0+uz_1$ interpolate between two approximate complex roots, treated as exact dyadic points. A floating inverse proposal supplies a fixed complex dyadic matrix $P$. Use the complex coordinate supremum norm and its induced matrix norm. With $e_j=F(z_j,t_j)$, $d=z_1-z_0$, the center defect obeys

\[
 \|P F(z(u),t(u))\|_\infty\le
 E=\max_j\|P e_j\|_\infty+\tfrac14\|P(d^2-(Kd)^2)\|_\infty .
\]

This follows by interpolating the quadratic system exactly and using $u(1-u)\le1/4$. Since $J(z)$ is linear, on $\|x-z(u)\|_\infty\le b$ one also has

\[
 \|I-PJ(x)\|_\infty\le
 \max_j\|I-PJ(z_j)\|_\infty+
 2\|P\|_\infty(1+\|K\|_\infty^2)b=:\eta .
\]

Each accepted segment has $b\ge\max(2E,2^{-40})$ and $\eta<1/2$. Thus $x\mapsto x-PF(x,t(u))$ is a contraction of the stated ball strictly into itself, for each $u$. Both $P$ and $J$ are invertible there by the strict matrix bound. Uniform iteration along the segment gives a continuous root, and the analytic implicit function theorem extends this root locally at every point. At consecutive endpoints the two balls have the same center. The root from the smaller ball belongs to the larger ball and uniqueness identifies their roots. The start certificate puts the physical row strictly inside the first center ball. Failed tube proposals are subdivided, with no conclusion taken from a floating Newton iteration or an unverified path segment.

Starting from $0.0331$ on the real axis, 93 accepted segments reach the bottom midpoint of the stated rectangle. Another 101 traverse its boundary once counterclockwise. At the common entry/return parameter, the [128-bit certificate](astra-cold-37-monodromy.jsonl) gives disjoint real enclosures for $A_0$,

\[
 1.00687\pm0.00000929,\qquad 1.00706\pm0.00000779 .
\]

These bounds allow the entire certified coordinatewise error $b(1+\|K\|_\infty)/2$ in the marked value. In particular the change cannot be an unmarked permutation of two stationary rows. The maximum recorded contraction bound was below $0.496$.

For the branch-location inference, use the finite map to the $t$-sphere from the smooth projective normalization of the physical marked algebraic curve. If no accessible sheet ramified over the closed rectangle, the component reached from the entry germ over a sufficiently small simply connected enlargement would be an unramified covering there. This follows from finiteness of the branch set, or by lifting a contraction of the boundary within the rectangle. Its boundary monodromy on the chosen sheet would be trivial. The distinct returned value contradicts this. Equivalently, a loop permuting the chosen sheet must encircle a ramified sheet in the same orbit of the local monodromy group. The statement permits ramification on the boundary on a different reachable sheet, hence the closed rectangle. It establishes existence within the stated coordinate bounds, without enumerating the enclosed ramification points or determining their orders.

The numerical scouts used cold real Taylor coefficients to select the center. Both the approach and loop start from the positive real germ in the rigorous checker. The interval proof uses only the reported rational rectangle, the actual Paley operator and the original stationary equations.

## 4. A growing-prime sufficient condition with shrinking domains

Fix a cold $a>0$ and $T=2048$. For each sufficiently large $n$ let $D_n$ be any simply connected subdomain of the right half-plane containing $[a,T]$ on which the actual marked germ continues. Let $d_n=d_{D_n}(a,T)$ be hyperbolic distance with curvature $-1$. For $g=\tanh m$ the scalar phase theorem gives $|g|<1$. In a Riemann map $\phi_n:D_n\to\mathbb D$ centered at $T$, write $r=|\phi_n(a)|=\tanh(d_n/2)$.

The inclusion $D_n\hookrightarrow\{\Re t>0\}$ contracts hyperbolic distance. Explicitly, applying ordinary disk Schwarz to $(t-T)/(t+T)$ composed with $\phi_n^{-1}$ puts $\{|\phi_n|\le1/4\}$ inside $|(t-T)/(t+T)|\le1/4$. Throughout that disk $1228<|t|<3414$. For $n>3414$ the hot estimate $|m|\le4/\sqrt n$ therefore gives $|g|\le8/\sqrt n$. For example, $|\sinh m|\le\sinh|m|$ and $|\cosh m|\ge 2-\cosh|m|$ give the factor two for these $n$. Apply three-circles to $g\circ\phi_n^{-1}$ between radii $1/4$ and $1$, taking the outer radius limit. This proves

\[
 |\tanh m(a)|\le (8/\sqrt n)^{\alpha_n},\qquad
 \alpha_n=\min\left(1,\frac{\log(1/r)}{\log4}\right).
\]

For $a\ne T$, $\log(1/r)=2\operatorname{arctanh}(e^{-d_n})\ge2e^{-d_n}$. Hence $(\log n)e^{-d_n}\to\infty$ forces $m(a)\to0$ since the real mark uses the real inverse of $\tanh$. In particular $d_n\le\log\log n-b_n$, $b_n\to\infty$, suffices. For each of a sequence $a_j\downarrow0$ this and the usual real bracket prove the target. The estimate can accommodate shrinking neighborhoods that admit no uniform-width tube. For example, if $D_n$ contains at each $x\in[a,T]$ the Euclidean disk $B(x,x\delta_n)$, then comparison with the centered disk gives $d_n\le 2\log(T/a)/\delta_n$. Thus

\[
 \delta_n\,\log\log n\ \ge\ (2+\epsilon)\log(T/a)
\]

eventually, for any fixed $\epsilon>0$, suffices. This is a sufficient width bound, without a sharpness claim. Formally one may choose the simply connected real tube equal to the union of the centered disks when the germ is compatible on it. The condition has not been proved for primes.

Conversely the actual square lower bound at any fixed $0<a<1$ bounds $|\tanh m(a)|$ below by a positive constant eventually. The same inequality forces $d_n\ge\log\log n-O_a(1)$ on every such square continuation domain. Thus squares force a quantitative loss of hot-to-cold access even when each field is allowed its own domain. The finite prime branch points above give no asymptotic lower bound on $d_n$ through primes.

## Reproduction

Run from the workspace root.

```sh
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python -B research/astra-cold-37.py
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python -B research/astra-cold-37-monodromy.py
```

These are ordinary mathematical proofs with interval-computation certificates. The prime-uniform width or hyperbolic-distance bound, and the all-prime ordinary-theta limit, remain open.
