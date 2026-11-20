# The actual incoming cold secants and their first possible slow projection

Let \(L=2031/128-2^{-17}\), take real \(t\) in the closed interval of half-width \(2^{-17}\) about \(2031/128\), and put \(W=V_{600}\) on the true nine-center orbit. For \(n=(p-1)/2\ge10^{30}\) and **\(p\le4\cdot10^{695}\)**, the projection of every subsequent incoming increment onto the paired right singular space above \(0.8\) is zero. This holds at every consecutive pair, with either starting parity. At sufficiently large primes, a nonzero such projection requires a signed response greater than **9.4** from the nonlinear errors of the actual incoming secants before a single real coordinate first reaches \(4\sqrt t\) in absolute value. Any \(10^{434}\) input sites can be erased independently at each time in that test.

There is also an unforced all-height complex rectangle with lower endpoint \(16640216/2^{20}\), four units below [round 96](astra-paired-96.md). The remaining real gap to the right edge of the cold square is \(2256/2^{20}\). [Arb checker](astra-incoming-97-check.py) · [Frozen integer caps](astra-incoming-97-caps.json) · [Five replay records](astra-incoming-97-checks.jsonl)

## Every pair on the finite real range

Write \(Y_j=V_{600+j}\), \(h_j=Y_j-W\), \(u_j=Y_{j+1}-Y_j\), and \(r=\|u_0\|_{2,n}\) in normalized counting norm. The exact recurrence is \(u_{j+1}=KD_j u_j\), where \(D_j\) uses the secant of \(f_i(x)=\sqrt{4t_i+x^2}\) at the two actual arguments, with \(t_0=n\) and \(t_i=t\) elsewhere. Each factor contracts. The starting bounds are \(r<0.169724(0.51358)^{600}\), \(\|W\|_\infty<4.768\), and \(\|u_0\|_\pi<0.010955\) in the physical packet norm dominating coordinate sup. The first actual secant therefore has norm below \(0.515\). [Physical residual](astra-source-88.md) · [Packet norm of the actual incoming row](astra-adjoint-82.md)

Set \(q=0.8\). Inductively assume all pairs \(KD_{k+1}KD_k\) with \(0\le k<j\) have norm at most \(q\). For each increment needed to form \(h_0,\ldots,h_{j+2}\), the odd subsequence satisfies \(\|u_{2a+1}\|_{2,n}\le0.515q^ar\), and \(\|u_{2a+2}\|_{2,n}\le\|u_{2a+1}\|_{2,n}\). Thus all these actual displacements have norm at most \((1+2(0.515)/(1-q))r=6.15r\), including in the initial case \(j=0\).

Form one high set for each secant,
\[
 H_k=\{i: |(h_{k,i}+h_{k+1,i})/2|>4\},\qquad k=j,j+1 .
\]
Each size is at most \(n(6.15r/4)^2\). At two real arguments \(x,y\) the signed secant is \((x+y)/(f_i(x)+f_i(y))\), also at equality. Convexity bounds its modulus by \(|(x+y)/2|/f_i((x+y)/2)\). Thus off \(H_k\) it is bounded by \(d=8.768/\sqrt{4L+8.768^2}\). Using \(|K_{il}|\le\sqrt p/n\), the high-to-high compression has norm at most
\[
 c=\sqrt p(6.15r/4)^2<\frac{q^2-d^2}{q(1-d^2)}.                     \tag{1}
\]

For a contraction \(K\) with \(\|P_2KP_1\|\le c\) for coordinate projections, and real diagonal \(|D_i|\le B_i=dI+(1-d)P_i\), one has
\[
 \|D_2KD_1\|\le\frac{\sqrt{4d^2+(1-d^2)^2c^2}+(1-d^2)c}{2}.
\]
Factor each signed diagonal as \(B_i\) times a commuting contraction. Dilate \(K\) to an orthogonal matrix \(O\) on two copies of the space and extend \(P_i\) by zero. The original \(B_2KB_1\) is the upper-left compression. Apply the two-projection decomposition to \(P_1,O^*P_2O\), obtained by diagonalizing \(P_1O^*P_2OP_1\) on the range of \(P_1\). On each two-dimensional block the angle cosine \(s\) is at most \(c\). The two singular values of the product of the positive multipliers have product \(d^2\) and squared sum \(2d^2+(1-d^2)^2s^2\), by writing the two diagonal matrices in bases rotated through that angle. Their difference is \((1-d^2)s\). The one-dimensional blocks give \(d\) or \(d^2\) when \(c<1\). Formula (1) consequently closes the induction. In particular \(\|u_{2a}\|_{2,n}\le q^a r\), so the real orbit converges geometrically throughout this finite range to the positive stationary solution.

## A signed history before a slow direction can carry energy

Now allow unbounded eligible primes. If \(\|Y_j\|_\infty<4\sqrt t\) at all times, every actual secant has norm at most \(a=\sqrt{0.8}\), and all the stated projections vanish. Otherwise let \(m\) be the first height with \(|Y_{m,i}|\ge4\sqrt t\) at some \(i\). The test includes the mark conservatively. The starting row satisfies the strict bound, and \(\|u_0\|_\infty<0.010955\) excludes \(m=1\). For \(0\le k\le m-2\), both endpoints of the \(k\)-th secant precede the first exit. Consequently \(\|u_k\|_{2,n}\le a^kr\) through \(k=m-1\).

Freeze \(D=\Phi'_t(V_{100})\), \(T=KD\), and define
\[
 E_k=(D_k-D)u_k,\qquad A_b=\sum_{\ell=0}^{b-1}T^\ell K .
\]
Iterating \(u_{k+1}=Tu_k+KE_k\) and summing the true incoming rows yields
\[
 h_m=\sum_{\ell<m}T^\ell u_0+
       \sum_{k=0}^{m-2} A_{m-1-k} E_k .                               \tag{2}
\]
The first sum has coordinate sup below \(0.010955/(1-0.984138)<0.691\) by the height-100 packet contraction. Also \(|(A_b)_{ix}|<178/\sqrt n\) simultaneously for all \(b,i,x\), eventually through primes uniformly in \(t\). The [translated column estimate](shifted-resolvent-96.md#consequences-for-the-full-linearized-inverse) bounds the sum of positive prices of all Neumann iterates, so truncating at any \(b\) gives the same constant.

For independent sets \(S_k\) of at most \(M\) indices, the erased part of the second term at \(i\) costs at most \(178(1.514)\sqrt M\,r/(1-a)\). This follows by counting Cauchy–Schwarz on each set, \(|D_k-D|\le1.514\), and the geometric bound before the hit. Put \(M=10^{434}\) and use the [field-first physical residual](astra-mixed-81.md) \(\limsup_p\sup_t r\le4(0.428236)^{600}\). Since \(|h_{m,i}|\ge4\sqrt L-4.768\), (2) gives, with \(\sigma=\operatorname{sgn}(Y_{m,i})\),
\[
 \sigma\sum_{k=0}^{m-2}
 [A_{m-1-k}1_{S_k^c}E_k]_i>9.4,\qquad
 \sum_{k=0}^{m-2}\sum_{x\notin S_k}|E_{k,x}|>0.0528\sqrt n .          \tag{3}
\]
Both estimates tolerate erasures chosen after observing the entire trajectory. With the finite-prime residual bound one may instead use \(M=10^{342}\), still with the eventual all-column estimate.

There is an energy form of this necessary observation. Put \(g_{k,x}=\operatorname{arsinh}(Y_{k,x}/(2\sqrt{t_x}))\), \(v_x=\operatorname{arsinh}(V_{100,x}/(2\sqrt{t_x}))\), and \(\bar g_k=(g_{k+1}+g_k)/2\). Then \(D_k=\tanh\bar g_k\), and
\[
 E_{k,x}=z_{k,x}\frac{\sinh(\bar g_{k,x}-v_x)}{\cosh v_x},
 \qquad z_{k,x}=4\sqrt{t_x}\sinh((g_{k+1,x}-g_{k,x})/2).
\]
Indeed \(z_{k,x}^2=u_{k,x}^2-(D_{k,x}u_{k,x})^2\). Contraction of \(K\) telescopes this exact loss to \(\sum_k\|z_k\|_{2,n}^2\le r^2\). Cauchy–Schwarz in space and time in (3) therefore forces
\[
 \sum_{k<m-1}\sum_{x\notin S_k}
 |(A_{m-1-k})_{ix}|^2
 \frac{\sinh^2(\bar g_{k,x}-v_x)}{\cosh^2 v_x}
 >\frac{9.4^2}{nr^2}.                                                 \tag{4}
\]
The square weights in (4) are measured on the actual pre-exit orbit. A field-uniform upper on the signed history or this weighted square sum remains open.

## An overlapping unforced complex rectangle

For all nontrivial rank-three labels \(b\) in inner powers up to four, keep one rank-four factor and the copy of that same standard or dual in the cube. For rank-three labels outside the eight previously selected, also keep the arithmetic unit from the square. With \(C_r\) the [round-95 signed inner coefficient](astra-depth-95.md#eight-further-signed-rank-three-labels) at fixed \(b,u,v,e\), the two new pairings at free arity \(j\) are
\[
 (j+1)\gamma C_{j+1}+
  {j+3\choose3}\frac{3\gamma^3}{8}C_{j+3},\qquad
 C_j+{j+2\choose2}\frac{\gamma^2}{8}C_{j+2}.
\]
For the first pairing \(j\le5\); for the second \(j\le6\). At least 24 copies of each degree-one label occur at its original shift in \((8F)^3\). Using 24 gives \(24/8^2=3/8\) relative to the single \(F\) fiber, entry by entry. The eight quadratic units in \((8F)^2\) give \(1/8\). Both use zero determinant shift relative to the direct charge. Their rank-four children have degrees one/three and zero/two. Round 84 used the trivial inner rank-three label. Rounds 95 and 96's zero-later-child pools on the nontrivial labels used only their zero/two rank-four degrees and only their eight chosen labels. Round 96 also used two later children, absent from the present pairings. The new pools use the nontrivial inner sectors with their existing rank-three root split. For each arithmetic label debit the triangle saving before the reflected-fiber minimum, retaining every omitted charge.

In units \(2^{-20}\), the overlapping closed real intervals are \([16640216,16640218]\), \([16640217,16640220]\), and \([16640219,16640222]\), all with imaginary half-width one and forcing parameter exactly one. The old 58-packet map at \(n\ge10^{30}\) preserves the three new caps, including the physical marked allowance. The coldest cap fails without the new pairings. By the physical secant argument of round 95, all heights on the union have cap below \(4.654\) and residual bounded by \(9.308(0.526)^h\). The genuine stationary row is holomorphic in the interior, with \(|m_p|<3/\sqrt n\), and identifies the physical harmonic action. This overlaps round 96 through the open interval \((16640220,16640222)\).

1. Test (3) or (4) on the actual first exit, choosing the erased sites separately at each time from the largest frozen-column contributions. Ruling out either lower bound excludes any positive incoming projection throughout the unbounded real tail.
2. On the complex square, estimate the corresponding two-step imaginary secants along the physical continuation. The finite real projection theorem and the four-unit complex advance leave an all-prime stationary section there open.
