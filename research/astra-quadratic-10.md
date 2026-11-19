# A prime opposite-energy obstruction at moving quadratic width

**Status: partial result, not a proof of Problem 26.** The new estimate below applies to the actual reciprocal QP at $r=\kappa/\sqrt p$, without fixing its support or assuming it has reached its terminal branch. It converts the second and fourth positional moments of **one** nonnegative spectrum into a lower bound for the **opposite** sign energy. Hanson–Petridis is the genuinely prime-field input. In particular, a critical-size spectrum cannot approach an idempotent probability, even with only qualitative convergence and no coset-cover assumption. A certified square-order QP violates this estimate.

This does not cancel the full signed energy integral. The remaining possibility is a boundary layer whose concentrated spectra have sufficiently non-idempotent autocorrelations, or whose effective support is above the threshold identified below. The result is weaker in its constant than the logarithmic-slack result in [the reflected-energy note](parallel-extreme-6.md), but applies to arbitrary weighted spectra of the moving-width QP and needs no logarithmic rate.

## 1. Actual QP spectra, rather than a frozen compression

Use the conventions of [quadratic theta](quadratic-theta.md), [the path limit note](parallel-quadratic-limit-9.md), and [the support note](parallel-quadratic-support-9.md). Thus $n=(p-1)/2$, $G=\widehat Q$, $Q=\mathbb F_p^{\times2}$, $j=\mathbf1/\sqrt n$, and

\[
K^2=I-J,\qquad P_\sigma=(I-J+\sigma K)/2,
\qquad Q_\sigma(r)=J+rP_\sigma+r^{-1}P_{-\sigma}.
\]

Write $x=A_\sigma(r)$, $y=A_{-\sigma}(r)$, $a=x_0=y_0^{-1}$, and $c=j^Tx=j^Ty>0$. These are the unique normalized actual optimizers, so

\[
x,y\ge0,\quad y=Q_\sigma(r)x,\quad
x^Ty=1,\quad x_i y_i=0\ (i\ne0).
\]

Put

\[
S_\sigma=r\|P_\sigma x\|^2,\qquad
S_{-\sigma}=r\|P_{-\sigma}y\|^2,
\qquad S_\sigma+S_{-\sigma}=1-c^2.                 \tag{1}
\]

Normalize the spectrum to a probability and take its positional characteristic function:

\[
\mu_\sigma(h)=\frac{x_h}{c\sqrt n},\qquad
f_\sigma(t)=\sum_{h\in G}\mu_\sigma(h)h(t),\quad t\in Q.
\]

In particular $f_\sigma(1)=1$ and $|f_\sigma|\le1$. Let

\[
D_\sigma^{\rm leak}
 =\sum_{t:\,\chi(1-t)=-\sigma}|f_\sigma(t)|^2,
\qquad C_{2,\sigma}=\sum_{t\in Q}|f_\sigma(t)|^2,
\qquad C_{4,\sigma}=\sum_{t\in Q}|f_\sigma(t)|^4.
\]

The sums here are **unnormalized**. Parseval and $P_{-\sigma}x=rP_{-\sigma}y$ give the exact identities

\[
\boxed{
D_\sigma^{\rm leak}=\frac r{c^2}S_{-\sigma},\qquad
C_{2,\sigma}
 =1+\frac{S_\sigma+r^2S_{-\sigma}}{r c^2}.}       \tag{2}
\]

The first identity is useful because the wrong-sign positional mass of one spectrum charges only the other sign's **positive** energy. No eigenvalue estimate for an arbitrary support compression is being used.

### A uniform bound at the requested moving width

The maximum-at-mark argument also holds at positive $r$: translate a rooted optimizer to any coordinate and divide by its value there. Translation preserves its quadratic energy. Optimality therefore gives

\[
0\le x_i\le a,\qquad 0\le y_i\le a^{-1}.         \tag{3}
\]

Indeed the rooted vector has root one, and a coordinate greater than one would give a strictly cheaper rooted trial. Consequently

\[
\|x\|^2+\|y\|^2\le c\sqrt n(a+a^{-1}).
\]

On the other hand, orthogonality of the three sectors gives

\[
\|x\|^2+\|y\|^2
 =2c^2+(r+r^{-1})(1-c^2).
\]

For $0<r\le1$, the fixed-point relation $x-y=d\sigma K(x+y)$, $d=(1-r)/(1+r)$, and the Jacobi entry bound imply

\[
|a-a^{-1}|\le2dc\sqrt{p/n},\qquad
a+a^{-1}\le\sqrt{14},
\]

where the latter uses $c\le1$ and $p/n\le5/2$ for $p\ge5$. It follows that

\[
1-c^2\le\frac{\sqrt{14}\,r\sqrt n}{1+r^2}.
\]

Thus, for $r=\kappa/\sqrt p$ and $0<\kappa<1/\sqrt7$,

\[
\boxed{
c^2\ge1-\sqrt7\kappa,\qquad
D_\sigma^{\rm leak}\le
\frac{\sqrt7\kappa^2}{1-\sqrt7\kappa}\,p^{-1/2}.} \tag{4}
\]

In particular the uniform wrong-sign pointwise tolerance is $O(\kappa p^{-1/4})$ as \(\kappa\downarrow0\). This estimate is valid through all support changes. Equations (1)–(4) themselves also hold at square field orders; the next step does not.

## 2. A prime phase-packing lemma

The needed arithmetic statement is [Hanson–Petridis, Theorem 1.2](https://arxiv.org/pdf/1905.09134): if all nonzero differences between $U,V\subset\mathbb F_p$ are squares, then

\[
|U||V|\le n+|U\cap V|.                          \tag{5}
\]

For a negative common sign, multiply both sets by a nonsquare before applying the theorem. Since $U,V\subset Q$ and $\chi(-1)=1$, the sign of $u-v\ne0$ is $\chi(1-u/v)$.

Here is a quantitative version for an arbitrary probability \(\mu\) on $G$, with characteristic function $f$, and leakage $D=\sum_{\chi(1-t)=-\sigma}|f(t)|^2$. No optimality assumption is needed in this paragraph. For nonempty $U,V\subset Q$, set

\[
\eta=\min_{u\in U,v\in V,u\ne v}|f(u/v)|,
\qquad
\delta(U,V)=\left(1-\frac{n+|U\cap V|}{|U||V|}\right)_+.
\]

Set \(\eta=0\) if there is no off-diagonal pair. Then

\[
\boxed{D\ge\eta^2\delta(U,V).}                  \tag{6}
\]

To prove this, suppose \(|U|=u\le v=|V|\), and let \(E\) count ordered wrong-sign pairs. Each ratio occurs in at most \(u\) pairs, so \(E\eta^2\le uD\). Delete from \(U\) every vertex occurring in a wrong-sign pair; at most \(E\) vertices are deleted. Applying (5) to the remaining rectangle gives \((u-E)v\le n+|U\cap V|\), with the inequality automatic if \(E>u\). These two inequalities prove (6). Also, if \(\eta>\sqrt D\), there is no wrong-sign pair at all, so (5) holds directly.

For the actual QP, (2) turns (6) into

\[
S_{-\sigma}\ge\frac{c^2}{r}\eta^2\delta(U,V).     \tag{7}
\]

This tests general positional rectangles, including ones that do not arise from a subgroup or a cover of the frequency support.

### Weighted phase vectors and a scalar moment consequence

Define unit vectors

\[
\phi(t)=(\sqrt{\mu(h)}h(t))_{h\in G}.
\]

Their mutual inner products have modulus \(|f(u/v)|\). If unit vectors \(\phi(u),\phi(v)\) each have squared projection greater than \(t_0\ge1/2\) on a common complex line, Cauchy–Schwarz on the perpendicular components gives

\[
|\langle\phi(u),\phi(v)\rangle|>2t_0-1.
\]

Suppose \(D<1\), and put

\[
t_0=\frac{1+\sqrt D}{2},\qquad
T_p=\left\lfloor\frac{1+\sqrt{1+4n}}2\right\rfloor.
\]

Every line therefore has at most \(T_p\) phase vectors with squared projection greater than \(t_0\). Otherwise their field labels would form a sign-\(\sigma\) clique larger than (5) allows. In particular, taking the line through \(\phi(1)\),

\[
|\{t\in Q:|f(t)|^2>t_0\}|\le T_p.
\]

For \(0\le z\le1\),
\(z^2\le t_0z+(1-t_0)\mathbf1_{z>t_0}\). Summing this inequality proves the prime moment bound

\[
\boxed{
C_4\le\frac{1+\sqrt D}{2}C_2
       +\frac{1-\sqrt D}{2}T_p.}                \tag{8}
\]

This is the weighted, quantitative moving-width extension of the exact-feasibility phase-cluster test in [the half-angle note](parallel-half-arithmetic-5.md#a-prime-only-phase-test-without-a-coset-cover). Here neither approximate uniformity on a selected set nor an endpoint solve is required.

## 3. A positive opposite-energy bound using only two moments

For the actual QP, whenever \(C_{2,\sigma}>T_p\), rearranging (8) gives

\[
\boxed{
S_{-\sigma}\ \ge\ \frac{c^2}{r}
\left(
\frac{2C_{4,\sigma}-C_{2,\sigma}-T_p}
     {C_{2,\sigma}-T_p}
\right)_+^2.}                                  \tag{9}
\]

There is no assumption \(D_\sigma^{\rm leak}<1\) in (9): if that inequality fails, the displayed positive ratio is at most one because \(C_4\le C_2\), so (9) follows immediately from (2). Thus (9) is a finite-prime theorem for every positive width. It is a necessary restriction on the particular nonnegative optimizer, not a claimed spectral gap on all vectors in a compression.

To express its content in frequency coordinates, define

\[
R_\mu(h)=\sum_i\mu(i)\mu(i+h).
\]

Parseval gives \(C_2=n\|\mu\|_2^2\) and \(C_4=n\|R_\mu\|_2^2\). At the moving widths in (4), (8) says

\[
\|\mu_\sigma\|_2^2-\|R_{\mu_\sigma}\|_2^2
\ge \frac{1-O_\kappa(p^{-1/4})}{2}
       \left(\|\mu_\sigma\|_2^2-\frac{T_p}{n}\right). \tag{10}
\]

The useful case is when the parentheses are positive. More explicitly, along a prime sequence with fixed \(0<\kappa<1/\sqrt7\), if

\[
\frac{C_{2,\sigma}}{\sqrt n}\longrightarrow\beta>1,
\]

then

\[
\limsup\frac{\|R_{\mu_\sigma}\|_2^2}{\|\mu_\sigma\|_2^2}
\le\frac{1+\beta^{-1}}2<1.                       \tag{11}
\]

At the square-obstruction scale \(m_0=n/\sqrt p\), a spectrum with \(\|\mu_\sigma\|_2^2\sim m_0^{-1}\) has \(\beta=\sqrt2\). Its autocorrelation ratio is consequently at most

\[
\frac{2+\sqrt2}{4}+o(1)=0.853553\ldots+o(1).     \tag{12}
\]

This excludes an approximately idempotent probability at that scale. For a uniform probability on a set \(S\), the ratio in (11) is \(E(S)/|S|^3\); for a subgroup coset it is exactly one. Unlike the earlier logarithmic-slack energy test, (11) permits arbitrary weights and only qualitative convergence of \(C_2/\sqrt n\). Its constant is correspondingly weaker.

In energy variables, a subsequence with \(S_\sigma\to s>0\), \(c^2\to c_0^2>0\), and \(r=\kappa/\sqrt p\) has

\[
\beta=\frac{\sqrt2\,s}{\kappa c_0^2}
\]

by (2). Hence the new restriction is nontrivial for \(s>\kappa c_0^2/\sqrt2\). Below that threshold the moment estimate need not give a saving.

### Optimality makes near-flat height saturation impossible

The moment estimate has a further consequence that uses actual QP optimality, beyond the approximate support equation. Define the height-saturation ratio

\[
\rho_\sigma=\frac{\|x\|^2}{a c\sqrt n}
            =\frac{c C_{2,\sigma}}{a\sqrt n}\le1.
\]

It measures saturation of the bound \(\|x\|^2\le a\sum_i x_i\) from (3). Let \(\widetilde\mu(h)=\mu(-h)\), and use the nonnegative convolution trial \(z=x*\widetilde\mu\). Its root is \(z_0=cC_2/\sqrt n=a\rho_\sigma\). The minimum energy at root \(z_0\) is \((z_0/a)^2\), so

\[
\rho_\sigma^2\le \langle z,Q_\sigma(r)z\rangle.
\]

If \(D_4=\sum_{\chi(1-t)=-\sigma}|f_\sigma(t)|^4\), diagonalizing the circulant quadratic form gives exactly

\[
1-\langle z,Q_\sigma(r)z\rangle
 =c^2\left[r(C_2-C_4)+(r^{-1}-r)(D-D_4)\right].   \tag{13}
\]

Here \(D=D_\sigma^{\rm leak}\). For \(0<r\le1\), both terms on the right are nonnegative. If \(D<1\), then \(D_4\le D^2\). Combining (8), (13), and (2) proves the prime, support-independent inequality

\[
\boxed{
1-\rho_\sigma^2\ge
\frac{r c^2(1-\sqrt D)}2(C_{2,\sigma}-T_p)_+
 +(1-r^2)(1-D)S_{-\sigma}.}                     \tag{14}
\]

Thus a sequence of **actual** QP spectra with fixed
\(0<\kappa<1/\sqrt7\), \(r=\kappa/\sqrt p\),
\(c^2\to c_0^2>0\), and \(C_{2,\sigma}/\sqrt n\to\beta>1\) satisfies

\[
\liminf(1-\rho_\sigma^2)\ge
\frac{\kappa c_0^2}{2\sqrt2}(\beta-1)>0.         \tag{15}
\]

In particular it cannot have \(\rho_\sigma\to1\). This rules out a nearly height-saturated critical mode of **any shape**, with no hypothesis on its additive energy or coset cover. Indeed, (13) would otherwise force its autocorrelation to be asymptotically idempotent; the prime phase-packing bound prevents this. The saving in (15) is proportional to \(\kappa\), so it does not survive taking \(\kappa\downarrow0\) by itself.

### An explicit concentration corollary

Let \(H\le G\), \(B=H^\perp\le Q\), and let \(\rho=\mu_\sigma(h_0+H)\). On \(B\), all characters in \(h_0+H\) have a common phase, so \(|f_\sigma(t)|\ge(2\rho-1)_+\). If

\[
k_\sigma(B)=|\{t\in B:\chi(1-t)=-\sigma\}|,
\]

then

\[
D_\sigma^{\rm leak}\ge k_\sigma(B)(2\rho-1)_+^2. \tag{16}
\]

At a prime, \(|B|(|B|-1)>n\) implies \(k_\sigma(B)\ge1\), by (5). Therefore, at the moving widths of (4), every such frequency coset satisfies

\[
\rho\le\frac12+
\frac12\left(\frac{\sqrt7\kappa^2}{1-\sqrt7\kappa}\right)^{1/2}p^{-1/4}. \tag{17}
\]

The endpoint version has error zero. Formula (17) supplies an explicit polynomial error for the actual positive-width pair, even when its support changes between the measured width and zero.

## 4. Square control, including an actual positive-width certificate

At \(q=s^2\), let \(H\) annihilate \(\mathbb F_s^\times\). The endpoint plus probability \(\mu=\mathbf1_H/|H|\) has positional function \(f=\mathbf1_{\mathbb F_s^\times}\). Thus

\[
D=0,\qquad C_2=C_4=s-1.
\]

Since \(T_q\sim s/\sqrt2\), this violates (8) for large \(s\). The obstruction is exactly the prime step (5), not Parseval or reciprocity.

There is also a strict finite counterexample using an **actual QP**: \(q=49\), \(n=24\), \(r=1/28=(1/4)/\sqrt q\), plus sign. A 192-bit Arb orthant certificate gives

| Quantity | Enclosed value, rounded here |
|---|---:|
| \(C_2\) | 5.9821533101346724 |
| \(C_4\) | 5.9599438252603845 |
| \(D\) | 0.0013386512142382690 |
| \(\mu(H)\), \(H=\{0,6,12,18\}\) | 0.9983246761445214 |
| \(C_4-\frac{1+\sqrt D}{2}C_2-\frac{1-\sqrt D}{2}\cdot5\) | 0.4508998624207226 |

Here the hypothetical prime bound uses \(T=5\). Its moment inequality fails by more than \(0.44\), and its coset-mass bound fails by more than \(0.47\). Thus even at the requested scale, the new assertion cannot follow from identities valid over both primes and squares.

The following replay uses the existing square sign generator and writes no output files. Strict orthant signs and \(|\gamma|<1\) certify the unique damped fixed point, as in the support note. Only positive bulk coordinates \(4,6,12,18,20\) are proposed; the interval solve verifies them.

```python
from flint import arb, acb, arb_mat, ctx
from square_control import square_field_sign

ctx.prec = 192
s = list(map(int, square_field_sign(7)))
n = len(s)
r = arb(1) / 28
d = (1-r)/(1+r)
k = [sum((s[l]*(2*arb.pi()*((i*l) % n)/n).cos()
          for l in range(n)), arb(0))/n for i in range(n)]
positive = {4, 6, 12, 18, 20}
signs = [1 if i in positive else -1 for i in range(1, n)]
H = arb_mat([[int(i == j)-d*k[(i-j) % n]*signs[j-1]
              for j in range(1, n)] for i in range(1, n)])
beta = H.solve(arb_mat([[d*k[i]] for i in range(1, n)]))
assert all(signs[i-1]*beta[i-1, 0] > 0 for i in range(1, n))
gamma = d*(k[0]+sum((k[i]*signs[i-1]*beta[i-1, 0]
                    for i in range(1, n)), arb(0)))
assert abs(gamma) < 1
u0 = 2/(1-gamma**2).sqrt()
x = [u0*(1+gamma)/2] + [
    u0*beta[i-1, 0] if signs[i-1] > 0 else arb(0)
    for i in range(1, n)
]
mu = [v/sum(x, arb(0)) for v in x]
f = acb.dft(mu)
C2 = sum((abs(v)**2 for v in f), arb(0))
C4 = sum((abs(v)**4 for v in f), arb(0))
D = sum((abs(v)**2 for v, a in zip(f, s) if a == -1), arb(0))
t = (1+D.sqrt())/2
assert C4-t*C2-(1-t)*5 > arb(44)/100
assert sum(mu[::6], arb(0))-t > arb(47)/100
```

Independent dense nonnegative least-squares checks used primes \(13,17,29,41,61,97,173,257,401\) and squares \(49,121,169\), at scaled widths \(1/16,1/4,1\). Across 36 solves, the energy/leakage identities and complementarity agreed within \(1.6\cdot10^{-13}\). The prime cases checked 2,160 sampled phase rectangles, 162 subgroup tests, and 54 moment inequalities; the largest floating inequality violation was below \(4\cdot10^{-16}\). A separate 54-case replay checked the convolution trial and (14). These numerical checks are separate from the proofs and the strict square certificate.

## 5. What remains for the full conjecture

The signed derivative is still

\[
\frac{dm(r)}{d\log r}=\frac12(S_-(r)-S_+(r)).
\]

The new estimate rules out a concrete class of prime boundary layers: a side with \(C_2>(1+\delta)\sqrt n\) cannot also have autocorrelation ratio tending to one. For the actual QP, (14) additionally excludes asymptotic saturation of the coordinate-height bound at this scale, regardless of the support's shape. It also rules out majority mass on every frequency coset covered by (17), directly at the moving width. These exclusions use neither a terminal support interval nor a quantitative cyclotomic lower bound for a compressed eigenvalue.

They do **not** show \(S_+-S_-\to0\), and do not bound its integral on the diverging interval from \(\kappa/\sqrt p\) to a fixed width. In (9), the positive part can vanish while \(S_\sigma\) remains substantial. Specifically, a spectrum with \(C_2\le T_p\), or with \(C_4\le(C_2+T_p)/2\), is not excluded. The remaining arithmetic task is to control these more dispersed autocorrelation profiles for the actual complementary pair, or to prove signed cancellation without forcing either energy to vanish. No claim of a proof or refutation of [Problem 26](https://randomstrasse101.math.ethz.ch/posts/PaleyGraph/) is made.
