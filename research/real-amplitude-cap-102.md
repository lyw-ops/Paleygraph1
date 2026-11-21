# Real amplitude clipping as a perturbation of the true weights

Real amplitude clipping gives a strict contraction on the full space for every fixed cap and floor. Its fixed point is a genuine complementary pair for decreased weights whenever its explicit products are positive. The mean activation measures the total decrease. This gives a sufficient real marked test that allows the capped row to exceed the clipping threshold.

## The fixed point and its mark

Let \(p=2n+1\equiv1\bmod 4\) be prime. The real symmetric smoothing operator \(K\) satisfies \(K^2=I-J_0\), \(J_0x=(\mathbb E_n x)\mathbf 1\) and \(K\mathbf 1=0\), with \(\|x\|_{2,n}^2=n^{-1}\sum_i |x_i|^2\). Fix \(t>0\), \(M>0\), \(t_0=n\), \(t_i=t\) elsewhere, and \(n\ge t\). Set
\[
 C_M(x)_i=\max(-M,\min(M,x_i)),\qquad
 F_M(x)=K\Phi_t(C_M(x)),\qquad
 (\Phi_t(x))_i=\sqrt{4t_i+x_i^2}.
\]
The map \(F_M\) contracts in \(\|\cdot\|_{2,n}\) with constant \(a=M/\sqrt{4t+M^2}<1\). Denote its unique fixed point by \(U\). As \(\|F_M(0)\|_{2,n}\le2\), one has \(\|U\|_{2,n}\le2/(1-a)\). Its physical marked coordinate satisfies
\[
                         U_0/\sqrt n \longrightarrow 0.              \tag{1}
\]
To prove this, put \(x=\sqrt n Ke_0\) and \(g(y)=\sqrt{4t+C_M(y)^2}\). At each fixed height the capped iteration from zero has normalized second error \(O(n^{-1/2})\) from that of \(u\mapsto 2x+Kg(u)\). The true exceptional coefficient before \(Ke_0\) differs from \(2\sqrt n\) by at most \(g(M)+M^2/(4\sqrt n)\), and \(g\) is \(a\)-Lipschitz. To apply [fixed-depth parity](iteration-parity.md#uniform-fixed-expression-trace-estimates), approximate the bulk rows at a fixed height in normalized second norm by bounded real combinations of negative Mellin fields. This induction starts at zero. Approximate \(g\) uniformly on the range of each bounded approximant by even polynomials. Its global Lipschitz bound passes the approximation from the bounded row to the original one. The even-product transport rule and addition of \(2x\) give the next approximant. For each fixed height \(j\), the identity
\[
 (2x+Kg(u_j))_0/\sqrt n=-2/n+\mathbb E_n[x_i g(u_{j,i})]
\]
uses \(K_{00}=-1/n\). Boundedness of \(x\) and the same even approximation reduce the second term to fixed odd products, whose means tend to zero. Thus (1) holds first for each fixed-height iterate. Its difference from \(U\) at the scaled mark is at most \(2a^j/(1-a)\). Take \(j\) to infinity after the prime limit. These estimates are uniform for \(t\) and \(M\) in fixed compact subintervals of \((0,\infty)\). On each bounded range used in the proof, the approximation of \(g\) by a polynomial in \(y\) can be made uniform in \((t,M)\) by polynomial approximation on the product of compact intervals followed by symmetrization in \(y\).

## When the capped row represents a positive pair

Write \(C=C_M(U)\), \(L_i=(U_i^2-M^2)_+\) and \(\alpha=\mathbb E_n L_i\). By \(U=K\Phi_t(C)\) and the identity for \(K^2\),
\[
          \alpha=4(1+t-t/n)-(\mathbb E_n\Phi_t(C))^2.                \tag{2}
\]
In particular the cap defect is a one-sided mean-activation deficit. It can be approximated in the field-first order using any fixed height of the contractive clipped iteration. The activation mean differs from that at the fixed point by at most \(2a^{j+1}/(1-a)\) after \(j\) iterations from zero. This applies to the physical mean, including its exceptional entry.

Suppose \(L_i<4t_i\) at each site. Define \(s_i=t_i-L_i/4>0\). The two rows \((\Phi_t(C)+U)/2\) and \((\Phi_t(C)-U)/2\) are positive, lie in the two complementary real Fourier sectors, and have the same mean. Indeed \(K U=(I-J_0)\Phi_t(C)\), so their centered parts are respectively \(+1\) and \(-1\) eigenvectors. Their coordinate products are exactly \(s_i\). Equivalently, \(U=K\Phi_s(U)\) is the true inhomogeneous stationary row. Uniqueness and the marked comparison for real positive weights follow from [weighted complementary projections](marked-response.md#weighted-complementary-projections). In applying that comparison along a line between square roots of weights, allow the marked weight to vary and divide the speed bound by its smallest square root, \(\sqrt{s_0}\).

Let \(\gamma_{p,0}(t)\) be the log mark for the original weights \(t_i\). Since \((\sqrt b-\sqrt c)^2\le b-c\) for \(b\ge c\ge0\), the preceding pair gives
\[
       |\gamma_{p,0}(t)|
       \le \left|\operatorname{arsinh}\frac{U_0}{2\sqrt{s_0}}\right|
             +\frac{\sqrt{\alpha}}{2\sqrt{s_0/n}}.                   \tag{3}
\]
By (1), \(s_0/n\to1\). Thus on any prime sequence with positive relaxed products, \(\limsup|\gamma_{p,0}(t)|\le\tfrac12\sqrt{\limsup\alpha}\). Positivity requires \(|U_i|<\sqrt{M^2+4t_i}\), which allows \(|U_i|>M\). If positivity and \(\alpha\to0\) hold along all sufficiently large eligible primes at each of a sequence of fixed floors \(t\downarrow0\), (3) and the [real theta bracket](smoothing.md) prove the original theta limit. Both hypotheses remain open at those floors. The average in (2) cannot exclude a failure of positivity at a bulk site, where an excess just across the boundary contributes about \(4t/n\).

## Consequence for the physical pre-exit path

On the real diameter of the nominated square use \(W=V_{600}\), \(M=4\sqrt t\), \(r=\|K\Phi_t(W)-W\|_{2,n}\), and \(Y_0=W,\ Y_{j+1}=K\Phi_t(Y_j)\). Its first index \(m\) with \(\|Y_m\|_\infty\ge M\) is allowed to be infinite. By the [physical prefix cap](astra-incoming-97.md#every-pair-on-the-finite-real-range), \(W\) is strictly inside. Through \(m\) inclusive the capped iteration from \(W\) agrees with \(Y\). At any \(j<m\),
\[
  \|U-Y_j\|_{2,n}\le \epsilon_j:=a^j r/(1-a),\qquad
  \alpha\le(2M+\epsilon_j)\epsilon_j.                               \tag{4}
\]
The first inequality is the contraction estimate from the initial residual. For the second, \(L_i\le |U_i-Y_{j,i}|(|U_i|+|Y_{j,i}|)\) because \(|Y_{j,i}|\le M\). Use Cauchy–Schwarz and \(\|U\|_{2,n}\le M+\epsilon_j\). If \(m=\infty\), (4) forces zero defect and \(U\) is the true real row. If \(m\) tends to infinity through some sequence of prime floors and the relaxed products are positive, the actual real mark still tends to zero by (3)–(4), since \(r\) is bounded uniformly there. This implication permits a first \(\|Y\|_\infty=4\sqrt t\) contact. For example, a sufficient positivity check is
\[
 \sqrt n\,\epsilon_{m-1}<\sqrt{M^2+4t}-M.
\]
An eventually uniform relaxed positivity margin on the nominated interval remains open. The result controls real weights.

1. At the original real cold floor, test the signed exterior for the capped fixed equation at the enlarged contact level \(\sqrt{M^2+4t}\). Verify relaxed positivity simultaneously with a vanishing mean defect, either via the actual pre-exit lengths or directly via (2).
2. If enlarged contact persists, use its offending sites and their true relaxed weight defects in a sector-feasibility correction.
