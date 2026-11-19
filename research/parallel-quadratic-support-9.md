# The actual supports of the zero-floor quadratic path

For [Randomstrasse101 Problem 26](https://randomstrasse101.math.ethz.ch/posts/PaleyGraph/), the support of the damped quadratic optimizer is **not nested**, already at the prime $61$. There is nevertheless a last interval of constant support at each field. On that interval a rank-one Schur formula identifies the two terms that move the mark away from its endpoint. There is also a bound from a single positive $r$ that permits arbitrary support changes below it.

## Notation and normalization

Work in the real multiplicative frequency space of dimension $n=(p-1)/2$. Write $j=\mathbf1/\sqrt n$, $J=jj^{\mathsf T}$, $e=e_0$, $K^2=I-J$, and $P_\sigma=(I-J+\sigma K)/2$. For $0<r<1$, set $Q=J+rP_\sigma+r^{-1}P_{-\sigma}$. If $b$ is the unique minimizer with $b\ge0,b_0=1$ and $M=b^{\mathsf T}Qb$, use

\[
 x=b/\sqrt M,\qquad y=Qx,\qquad a=x_0=1/\sqrt M,\qquad y_0=a^{-1}.
\]

The quadratic optimality conditions give $x,y\ge0$ and $x_i y_i=0$ for $i\ne0$. In particular $x^{\mathsf T}y=1$; $y$ is the corresponding normalized optimizer for the inverse form. Put $c=j^{\mathsf T}x=j^{\mathsf T}y\le1$; the inequality follows from $x^{\mathsf T}Qx=1$. The mean at positive $r$ need not equal one. It satisfies

\[
 1-c^2=r(\|P_\sigma x\|^2+\|P_{-\sigma} y\|^2)
       =\frac{r}{(1-r)^2}\|x-y\|^2.                 \tag{1}
\]

This is the normalization in which the endpoint has $j^{\mathsf T}x^*=j^{\mathsf T}y^*=1$ and $x^*_0=\theta_\sigma/\sqrt n$, using the signs from [the Fourier convention](fourier.md). The character space for $K$ is cyclic of order $n$, generally composite even at prime field order. The [prime cyclic Fourier uncertainty theorem](https://arxiv.org/abs/math/0308286) does not give full spark for these support compressions.

## Which endpoint does damping select?

Take $u=x+y$, $z=x-y$, and $d=(1-r)/(1+r)$. Then $z=dT(z)$, where $T(z)=\sigma K\Phi(z)$, $\Phi_0(z)=\sqrt{4+z_0^2}$, and $\Phi_i(z)=|z_i|$ off the mark. The map $T$ is nonexpansive in Euclidean norm. Its fixed points are the differences of the endpoint pairs: $w=T(w)$ gives $A=(\Phi(w)+w)/2\in\mathbb Rj\oplus\operatorname{ran}P_\sigma$, $B=(\Phi(w)-w)/2\in\mathbb Rj\oplus\operatorname{ran}P_{-\sigma}$, with the prescribed products. They have common mean $j^{\mathsf T}A=j^{\mathsf T}B=1$ by orthogonality. Conversely an optimal pair gives a fixed point. Existence also follows by compactness from the positive-$r$ pairs: $c\le1$ and nonnegativity bound their norms for fixed $n$, and $P_{-\sigma}x=rP_{-\sigma}y$, $P_\sigma y=rP_\sigma x$.

For every fixed point $w$, nonexpansiveness gives $\|z/d-w\|^2\le\|z-w\|^2$. Cancelling terms yields

\[
 \|z\|^2\le(1-r)\langle z,w\rangle,
 \qquad \|z\|\le(1-r)\|w\|.                      \tag{2}
\]

Every subsequential limit of $z$ as $r\downarrow0$ is a fixed point of least norm. The least norm pair is unique: every choice of endpoint optimizers $A,B$ is complementary, and $\|A-B\|^2=\|A\|^2+\|B\|^2-2$, so the two strictly convex minimum-norm selections decouple on their respective convex optimal faces. Thus $x^*,y^*$ are individually the least norm endpoint optimizers in this normalization. This identifies the pair used in the Schur formula below even when a Fourier LP has many maximizers.

There is a useful exact derivative, including through support changes. Differentiating the optimal value by the envelope formula and using $y=Qx$ gives

\[
 \frac{d}{dr}\log M(r)
 =\|P_\sigma x\|^2-\|P_{-\sigma}y\|^2
 =\frac{\|x\|^2-\|y\|^2}{1-r^2}.                \tag{3}
\]

Uniqueness and continuity of the minimizer suffice for this differentiation. Equations (2) and (3) give the support-independent bound, valid for any $0<r\le1/2$,

\[
  |\log M(r)-\log M(0)|
 \le r\|x^*-y^*\|^2+2\operatorname{artanh} r .    \tag{4}
\]

Indeed $\|x\|^2+\|y\|^2=2+\|z\|^2$ and $(1-r)^2/(1-r^2)\le1$. In particular it is the **signed** norm difference in (3) that matters for a long cold interval, even when the bound (4) is large.

## The terminal support and its marked Schur formula

For a candidate support $S\ni0$, the formula $b_S=Q_{SS}^{-1}e_S/(Q_{SS}^{-1})_{00}$, $b_{S^c}=0$ gives the optimizer exactly when $b_S>0$ and $(Qb)_{S^c}\ge0$. For each $S$ these are rational sign tests in $r$; the denominators used in the inverse and in the normalization are nonzero for $r>0$. There are finitely many supports, and a numerator is either identically zero or has finitely many roots. Thus the true support is constant on an interval $0<r<r_*(p,\sigma)$. There is no lower bound here for $r_*$ as $p$ grows. The terminal $S$ is defined by positivity at $r>0$, so an entry tending to zero still belongs to $S$.

Use the terminal $S$, and from now on within this calculation restrict $e,j$ to $S$. Write $E_S$ for extension by zero, $T_S=P_{-\sigma}E_S$, $C=T_S^{\mathsf T}T_S=(P_{-\sigma})_{SS}$, $N=\ker C$, and $e_N,j_N$ for orthogonal projections onto $N$. Put $\alpha=x_0^*$. Since $x^*_S\in N$ and has mean one, $j_N\ne0$. On $S$, the relation $y_0e=Q_{SS}x_S$ gives, after projection onto $N$,

\[
  a^{-1}e_N = (1-r)c\,j_N+r\Pi_N x_S .           \tag{5}
\]

At $r=0$ this shows $e_N=\alpha j_N$. For every positive $r$ in the interval, (5) then forces $\Pi_N x_S$ to be parallel to $j_N$. In particular

\[
 x^*_S=\frac{j_N}{\|j_N\|^2},\qquad
 \|x^*\|^2=\frac1{\|j_N\|^2}.                    \tag{6}
\]

Let $v=e-\alpha j\in N^\perp$, $g=(1-r)^{-1}$, and let $G_r$ be zero on $N$ and have eigenvalue $r/[r^2+(1-r^2)\lambda]$ on each positive $C$-eigenspace of eigenvalue $\lambda$. The actual value obeys

\[
\boxed{
 a(r)^2=\alpha^2g+v^{\mathsf T}G_r v
 -\frac{(\alpha g-j^{\mathsf T}G_r v)^2}
 {\|j_N\|^2/r+j^{\mathsf T}G_r j+g}.}            \tag{7}
\]

In fact $Q_{SS}=D_r+(1-r)jj^{\mathsf T}$, $D_r=rI+(r^{-1}-r)C$. The inverse mark is the minimum over $\eta\in\mathbb R$ of $(e-\eta j)^{\mathsf T}D_r^{-1}(e-\eta j)+g\eta^2$. Expanding around $\eta=\alpha$ gives (7). Keeping only the kernel and the $g\eta^2$ term gives a lower bound, and taking $\eta=\alpha$ gives an upper bound:

\[
 \frac{\alpha^2}{1-r+r\|x^*\|^2}\le a(r)^2
 \le\frac{\alpha^2}{1-r}+v^{\mathsf T}G_r v.      \tag{8}
\]

The positive-eigenvalue term also has an interpretation in the **opposite** active spectrum. Since $y_S^*=\alpha^{-1}e$ and $y^*\in\mathbb Rj\oplus\operatorname{ran}P_{-\sigma}$, $T_S^{\mathsf T}P_{-\sigma}y^*=v/\alpha$. Moreover $P_{-\sigma}y=r^{-1}T_S x_S\in\operatorname{ran}T_S$ all along the interval, so its limit is the minimum-norm extension. Hence $P_{-\sigma}y^*=\alpha^{-1}T_SC^\dagger v$. For the positive spectral projections $L_\lambda$ of $T_ST_S^{\mathsf T}$ this gives

\[
 \frac{v^{\mathsf T}G_r v}{\alpha^2}
 =\sum_{\lambda>0}\frac{r\lambda}{r^2+(1-r^2)\lambda}
     \|L_\lambda P_{-\sigma}y^*\|^2.             \tag{9}
\]

Thus a small unweighted minimum eigenvalue is not a test for a large marked Schur contribution. The term charges only the marked direction, with reduced weight on $\lambda\ll r^2$ in the opposite extension. For $r\le1/2$ its vanishing is equivalent, up to absolute factors, to vanishing of

\[
 r\!\sum_{\lambda\ge r^2}\!\|L_\lambda P_{-\sigma}y^*\|^2
 +r^{-1}\!\sum_{0<\lambda<r^2}\!\lambda\|L_\lambda P_{-\sigma}y^*\|^2 .
\]

Along primes and $r=r(p)\to0$ in the certified terminal intervals, this and $r\|x^*\|^2=o(1)$ suffice for $a(r)/\alpha\to1$ by (8). For a signed test (7) retains the subtraction and does not require the positive and negative corrections to vanish separately. At fixed $p$, $v^{\mathsf T}C^\dagger v=\alpha^2(\|y^*\|^2-1)$ and (7) gives $(a^2)'(0)=\alpha^2(\|y^*\|^2-\|x^*\|^2)$, in agreement with (3). The terminal-support computation is conditional on knowing the true branch or certifying it by the signs. Sampling a single support and freezing it down to zero is not justified.

## A one-parameter test that does not freeze the support

For a fixed $r>0$, use $x,y$ from the true problem. Write $X=x^*$, $Y=y^*$, $B=\{1,\ldots,n-1\}$, and keep $e,j$ on the full space. The following identities charge only the observed **same-sign** supports in the upper bounds:

\[
\begin{aligned}
 \alpha/a &=(1-r)c+r\alpha a+r\langle X_B,x_B\rangle-\langle X_B,y_B\rangle,\\
 a/\alpha &=(1-r)c+r/(\alpha a)+r\langle Y_B,y_B\rangle-\langle Y_B,x_B\rangle.
\end{aligned}                                                     \tag{10}
\]

For the first identity, $\langle X,y\rangle=c+r(\langle X,x\rangle-c)$ by the exact sector of $X$ and $P_\sigma y=rP_\sigma x$. The second interchanges the signs. In particular the cross terms have the favorable sign even if the supports of the endpoint optimizers differ arbitrarily from those at $r$.

Use the [Jacobi entry bound](fourier.md#joint-distribution-on-the-even-modes) $\max_{ij}|K_{ij}|\le\sqrt p/n$. Because $X=j+\sigma KX$ and $\sum_i X_i=\sqrt n$, $0\le X_i\le(1+\sqrt p)/\sqrt n$; the same holds for $Y$. The positive-$r$ marks and their reciprocals are bounded as well, since $|z_0|\le(\sqrt p/n)\sum_i u_i\le2\sqrt{p/n}$. Take a common absolute constant $C_0=4$. For an observed nonnegative bulk vector $h$ define

\[
 \mathcal C_p(h)=\inf_{t\ge0}\left[t+C_0\sum_{i\in B}(h_i-t/\sqrt n)_+\right].
\]

Only positive coordinates enter the sum. The mean and point cap of $X,Y$ show, for example, $\langle X_B,x_B\rangle\le\mathcal C_p(x_B)$. With $c\le1$, (10) consequently gives the finite error certificate

\[
 \big|\log(a/\alpha)\big|
 \le \log\!\left(1+r[C_0^2+\max\{\mathcal C_p(x_B),\mathcal C_p(y_B)\}]\right).  \tag{11}
\]

Unlike (8), (11) uses only the observed pair at $r$, with no hypothesis on the subsequent support. For example, one sufficient prime-field condition is

\[
 \liminf_{r\downarrow0}\limsup_{p\to\infty}
 r\max\{\mathcal C_p(x_B(r)),\mathcal C_p(y_B(r))\}=0,
\]

combined with $a(r)\to1$ at each fixed $r>0$ through primes. That fixed-$r$ premise follows from the existing [fixed-depth parity draft](iteration-parity.md#application-to-the-picard-iterates): replace its even activation by absolute value and multiply each feedback step by $\sigma d$, which leaves the polynomial approximation and parity argument unchanged. At a fixed $d<1$, the error from truncating to $t$ iterations from zero is at most $d^t\,2d/(1-d)$ in Euclidean norm, uniformly in the field, by contraction. Send the field size to infinity at fixed depth, then send the depth to infinity.

A simpler sufficient moving-scale assumption is $a(r(p))\to1$ and $r(p)\sqrt n\max\{\|x_B(r(p))\|_\infty,\|y_B(r(p))\|_\infty\}\to0$. The capped form counts excess on the true supports instead of charging every bulk coordinate for the largest height. Neither the capped-height estimate nor a bound on the terminal intervals follows from (1); a term $r\|z\|^2=O(1)$ alone does not control those excesses.

The test also locates an obstruction at square field orders. For $q=h^2$ and $\sigma=+1$, use the [subfield optimizer](square-order-control.md#the-fourier-frequencies-carrying-the-discrepancy) $X=\alpha\mathbf1_L$, where $L$ annihilates the multiplicative subfield subgroup and $\alpha=(h-1)/\sqrt n\to\sqrt2$. The first identity in (10) works with this endpoint choice whether or not it is the minimum-norm optimizer. Since $c\le1$, it gives

\[
 r\sum_{i\in L\setminus\{0\}}x_i
 \ge a^{-1}-\frac{1-r}{\alpha}-ra.
\]

The fixed-depth draft also applies to square orders. With the square field limit first and $r\downarrow0$ second, the lower limit of the left side is at least $1-1/\sqrt2$. The sum is entirely on the intersection of the actual positive support and the subfield annihilator. This is a set of size at most $(h+1)/2=O(\sqrt n)$. In particular the fixed-$r$ mark can be balanced even while a vanishing fraction of the sites carries a nonvanishing boundary certificate.

## Certified support reversal at $p=61$

Here $n=30$, $2$ is a primitive root, and $K_{ij}=k_{i-j}$ with $k_h=n^{-1}\sum_{l=0}^{n-1}\chi(1-2^{2l})\cos(2\pi lh/n)$. Take $\sigma=+1$. The table lists the positive bulk support on $1,\ldots,15$; reflect it to all nonzero coordinates.

| $r$ | Positive bulk representatives | $z_1/u_0$ | Certified lower bound on $\min_{i\ne0}\lvert z_i\rvert/u_0$ |
|---:|---|---:|---:|
| $1/4$ | $2,3,5,6,11,12,13,15$ | −0.002493394619 | 0.002 |
| $1/8$ | $1,2,3,5,6,11,12,13,15$ | 0.006051721369 | 0.006 |
| $1/32$ | $2,3,5,6,11,12,13,15$ | −0.008179255288 | 0.008 |

To certify a row, put $D=\operatorname{diag}(\operatorname{sign}z_B)$ from the proposed support. On the active orthants $u_B=D z_B$, so the normalized bulk $\beta=z_B/u_0$ and mark $\gamma=z_0/u_0$ solve

\[
 (I-dK_{BB}D)\beta=dK_{B0},\qquad
 \gamma=d(K_{00}+K_{0B}D\beta).                  \tag{12}
\]

The bulk solve is nonsingular by $d<1$. Check $D\beta>0$ componentwise and $|\gamma|<1$; then $u_0=2/\sqrt{1-\gamma^2}$ exactly recovers the unique contraction fixed point. This certifies a **true** support. Here is the Arb replay for the strict bounds (the displayed values of $\beta_1$ are rounded):

```python
from flint import arb, arb_mat, ctx

ctx.prec = 128
p, n = 61, 30
assert all(pow(2, 60 // q, p) != 1 for q in (2, 3, 5))
qr = {a*a % p for a in range(1, p)}
s = [0] + [1 if (1-pow(2, 2*l, p)) % p in qr else -1 for l in range(1,n)]
k = [sum(s[l]*(2*arb.pi()*((i*l) % n)/n).cos()
         for l in range(n))/n for i in range(n)]
for den, entry, margin in [(4, False, 2), (8, True, 6), (32, False, 8)]:
    d = arb(den-1)/(den+1)
    S = {2,3,5,6,11,12,13,15} | ({1} if entry else set())
    D = [1 if min(i,n-i) in S else -1 for i in range(1,n)]
    H = arb_mat([[int(i == l)-d*k[(i-l) % n]*D[l-1]
                  for l in range(1,n)] for i in range(1,n)])
    beta = H.solve(arb_mat([[d*k[i]] for i in range(1,n)]))
    assert all(D[i-1]*beta[i-1,0] > arb(margin)/1000 for i in range(1,n))
    gamma = d*(k[0]+sum(k[i]*D[i-1]*beta[i-1,0] for i in range(1,n)))
    assert abs(gamma) < 1
    print(den, beta[0,0], gamma)
```

In particular, the actual positive support gains and loses frequency $1$ as $r$ decreases. This refutes a nested-support argument even at prime order. It neither implies an asymptotic obstruction nor supplies the prime-field control of (9) or (11).
