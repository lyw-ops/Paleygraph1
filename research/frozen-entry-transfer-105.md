# Frozen signed entry transfer at the quadratic residual scale

The translated-bound propagation needs a signed leading term only at the starting inverse. A two-sided resolvent identity puts that same inverse at both ends of the quadratic error. If the starting \(\beta\)-entry bound and the Newton residual scale hold together, the quadratic error spends no additional power of \(n\).

For two physical predictors \(V_a,V_b\) on common sheets put \(D_j=\Phi'_t(V_j)\), \(Z_j=(I-KD_j)^{-1}K\), \(E=D_b-D_a\). Write \(\delta_a=\|Z_a\|_{\max}\), where the max is over all matrix entries. Suppose \(\|Z_b\|_{2\to2}\le z\), and use \(E\) as a diagonal matrix. The usual first resolvent identity in both orientations gives, exactly,
\[
 Z_b-Z_a=Z_b E Z_a=Z_a E Z_b,
 \qquad Z_b=Z_a+Z_a E Z_a+Z_a E Z_b E Z_a.                         \tag{1}
\]
For a fixed row \(i\) and column \(k\), the two outer vectors of the last term have unnormalized second norms at most \(\delta_a\|E\|_2\), using the diagonal vector norm on \(E\). Complex entries cause no difficulty because the absolute bilinear pairing is bounded by the product of the Hermitian norms. Hence
\[
 \|Z_b\|_{\max}
 \le \delta_a+\|Z_a(D_b-D_a)Z_a\|_{\max}
        +z\,\delta_a^2 n\|D_b-D_a\|_{2,n}^2.                         \tag{2}
\]
The only linear term uses the known starting inverse at both ends. The quadratic remainder allows the endpoint inverse to be controlled solely in operator norm. This replaces the dependence on the unknown endpoint entries in the [first resolved-difference estimate](api-astra-review-104.md).

Suppose the actual successive Picard increments from \(a\) through \(b\) obey \(\|V_{a+j+1}-V_{a+j}\|_{2,n}\le r_a q^j\), with a uniform \(q<1\), and the scalar curvature on the segments is at most \(C\). Then \(\|D_b-D_a\|_{2,n}\le Cr_a/(1-q)\), by integrating each actual derivative difference and summing. If \(\delta_a\le Bn^{-\beta}\), (2) yields
\[
 \|Z_b\|_{\max}
 \le Bn^{-\beta}+\|Z_a(D_b-D_a)Z_a\|_{\max}
 +\frac{zB^2 C^2}{(1-q)^2}n^{1-2\beta}r_a^2.                        \tag{3}
\]
For uniform \(0<\beta\le1/2\) and \(n^{(1-\beta)/2}r_a\to0\), the last term is \(o(n^{-\beta})\). This is exactly the [translated Newton residual scale](translated-newton-103.md). A bound \(O(n^{-\beta})\) on the middle term then propagates the translated exponent to all later admissible endpoints. The middle term can be split into the actual adjacent derivative differences with the **fixed** \(Z_a\) on both sides. A signed bound with a summable depth weight for those frozen tests would suffice.

This gives a conditional transfer from one compatible genuine starting height. It does not establish that height, the physical contraction along any later segment, or the signed middle bound. At fixed height a constant normalized residual fails the required prime-uniform scale. In particular the finite translated exponents already verified on the physical prefixes cannot alone initialize (3) through primes.

## A signed bound for two frozen negative Mellin columns

There is a useful case in which the middle term in (3) has the needed extra power by parity. Use the [negative Mellin fields and lift average](iteration-parity.md#uniform-fixed-expression-trace-estimates). Suppose each column of \(Z_a\) admits approximations by sums of these fields with total absolute coefficient times convolution dimension at most \(B/\sqrt n\), uniformly in the translated column. For each field assume generic rank equal to its convolution dimension. Assume the same bounded-boundary condition as in the [translated column calculation](shifted-resolvent-96.md#the-two-estimates-for-one-physical-derivative-step): the bad Mellin characters of the factors in a product and its convolution are contained in the union of their boundedly many specified boundary fibers. This must hold for the approximations with a uniform bound on the number of fibers. Suppose \(E=D_b-D_a\) is likewise approximable by such sums of dimension mass at most \(W\), apart from a diagonal row \(e_{\mathrm{exc}}\) of counting first norm at most \(M_{\mathrm{exc}}\). Then
\[
  \|Z_a E Z_a\|_{\max}
  \ll B^2 W\,p^{-1/2} + B^2 M_{\mathrm{exc}}/n.                    \tag{4}
\]
The constant is uniform in the depths under these representation bounds.

Indeed, three negative fields with convolution dimensions \(d_1,d_2,d_3\) have mean product \(O(d_1d_2d_3/\sqrt p)\). Expand each lift average into its two full characters. The resulting parity-odd middle convolution has no geometric punctual summand at \(1\). The generic rank bound for two factors in the cited parity argument, and multiplicativity of dimension, give generic rank \(O(d_1d_2d_3)\) after three factors. Its nonpunctual trace at \(1\) is therefore \(O(d_1d_2d_3/\sqrt p)\) by the middle-extension weight bound. Each omitted bad Mellin coefficient costs \(O(d_1d_2d_3)\), and the bounded union of boundary fibers makes their total cost in the average \(O(d_1d_2d_3/p)\). All these estimates are per word, so summing uses only the stated dimension masses. Approximation limits at a fixed field preserve the resulting finite-vector inequality.

The formula \(Z_a=K(I-D_aK)^{-1}\) makes \(Z_a\) symmetric under transpose. Its \((i,k)\) frozen linear entry in (3) is \(n\) times the empirical average of two negative columns multiplied by \(E\). The three-field estimate gives the first term in (4). Each column also has sup norm no greater than its dimension mass, so the exceptional row costs the second term. The established packet argument gives the required column representation at the earlier depths with a strict packet contraction. Extending a compatible representation and the scaled residual jointly to a growing starting depth remains open.

## Exponentially growing partial column representations

The independent reviewer observed that bounded dimension mass for the full inverse is unnecessary. Suppose \(Z_a=L_h+T_h\), where \(L_h=\sum_{j<h}(KD_a)^j K\). Suppose its columns have the same negative representations with dimension mass \(O(n^{-1/2}\rho^h)\) and uniform boundary allowance, for some fixed \(\rho>1\), and \(\|T_h\|_{2\to2}=O(q^h)\) with \(0<q<1\). The partial sum is transpose symmetric since \((KD_a)^j K=K(D_aK)^j\). Under the same assumption on \(E\) as in (4), expand the middle term of (3) into four terms and apply parity only to \(L_h E L_h\). For a crossed term each \(T_h\) row or column costs \(O(q^h)\) in counting second norm, and each \(E\) times an \(L_h\) column costs \(O(\rho^h\|E\|_{2,n})\) in that norm. The two-tail term uses the diagonal operator norm. Thus
\[
 \|Z_a E Z_a\|_{\max}\ll
 Wn^{-1/2}\rho^{2h}+M_{\mathrm{exc}}n^{-1}\rho^{2h}
 +\|E\|_{2,n}(\rho q)^h+\|E\|_\infty q^{2h}.
\]
Choose \(h\) within a bounded distance of \((\log n)/(4\log(\rho/q))\) and put \(\beta=-\log q/(2\log(\rho/q))\). The first and last terms are \(O(n^{-\beta})\) at bounded \(W,\|E\|_\infty\). At bounded \(M_{\mathrm{exc}}\) the exceptional term is smaller. The crossed term is \(o(n^{-1/4-\beta/2})\) if \(\|E\|_{2,n}=o(n^{-(1-\beta)/2})\), which is \(o(n^{-\beta})\) as \(\beta\le1/2\). The same exponent for the starting \(Z_a\) follows by balancing the single partial-sum entry bound with its counting tail at twice this cutoff, assuming the representations and tail bound up to that length. The quadratic remainder still has the scale in (3). This is a conditional extension to a noncontracting packet price. It requires finite-depth bounds with \(\rho,q\) uniform at the actual growing starting row, and a bounded signed field representation of the actual derivative difference.

1. Try to verify the truncated representation hypotheses at the same genuine growing depth as the quadratic residual scale. Track the actual boundary union through the Neumann truncation and the derivative difference.
2. Seek a genuine growing starting height satisfying both translated entry decay and \(n^{(1-\beta)/2}r_a\to0\). Bounds (3)–(4) transfer up to the actual chosen endpoint without paying a second counting-residual threshold.
