# A second distinguished feedback for the common complex marked branch

For every sufficiently large eligible prime and prime square the actual marked section extends to
\[
    8135/512<\Re t<1027/64,\qquad |\Im t|<1/2048,
    \qquad |m_q(t)|\le 3/\sqrt n.
\]
This connects to [round 54](astra-signed-54.md) and lowers the common floor from 16.03125 to 15.888671875. The [checker](astra-rankthree-55-check.py) proves strict scalar inequalities on four overlapping closed intervals with imaginary thickness. The all-prime ordinary limit remains open.

## Exact feedback and arithmetic weights

Use \(C_k=T_k(S/s)\), \(S=2x,\ s=2\sqrt{q/n}\), and the round-54 Legendre trace average \(Y\). Let \(U,V\) denote the two positive rank-three traces, with \(\det U=m^{-1},\ \det V=m\) in matrix notation. Here \(m\) is the positive Jacobi trace. The arithmetic group and the central translation between positive and perverse coordinates are those of [round 32](joint-law-32.md). Put
\[
 W=(\operatorname{tr}U+\operatorname{tr}U^*+\operatorname{tr}V+\operatorname{tr}V^*)/4.
\]
At exceptional coordinates define this by the raw full sums and their conjugates. At every coordinate,
\[
  K C_2=Y-2\sqrt q\,C_1/q,\qquad K(C_1 Y)=W+C_1/q.
\]
Indeed \(x=sC_1/2\), \(y=K(x^2)=qY/(2n)-x/\sqrt n\). Substitute this into \(z=K(xy)\) and use the [exact all-lift formula (14)](astra-nested-moment-31.md#4-exact-spectral-normalization-and-uniform-error). In particular the distinguished subtraction costs only a vanishing Jacobi correction after applying \(K\).

At full twist one, the four standard or dual multisets in order \(F=U,U^*,V,V^*\) are
\[
 (-1,-1,3),\quad(1,1,-3),\quad(-1,0,0),\quad(1,0,0).
\]
These follow from the [rank-three inertia table](astra-nested-moment-31.md#2-the-actual-new-rank-and-local-monodromy). The determinant of the first multiset has weight one, so \(m\) has weight \(-1\) here. Twisting by \(\chi\) interchanges the two pairs and replaces \(m\) by its inverse. Thus \(W\) at either twist has measure \(D_W=\delta_0+3(\delta_1+\delta_{-1})/4+(\delta_3+\delta_{-3})/4\). The sign of the positive trace is handled by the common central translation; it respects every character identity used below.

Write the scaled vector as \(S+\alpha Y+\beta W+Z\). Through total polynomial degree 28 let \(c_{rk}\) be the round-54 Laurent coefficients and let \(d_{rk,ab}\) be their signed Legendre-character expansion after translating by \(\alpha Y\), *before* any distinguished subtraction. With \(c=c_{02}\), take
\[
 \alpha=c+c_{22}c^2/2,\qquad \beta=2d_{01,10}=2d_{01,01}.
\]
Both are holomorphic on the strip. In residual arity zero subtract \(\alpha C_2+\beta C_1Y\) before applying \(K\); the second summand cancels both corresponding linear Legendre coefficients exactly. The term \(c_{22}c^2/2\) is a chosen polynomial correction to the dominant first distinguished coefficient.

## Collecting signed rank-three characters

In arity \(j\) and \(W\)-degree \(l\), start with the Legendre coefficients at arity \(j+l\) multiplied by \(\binom{j+l}{j}\beta^l\). In \(W^2\), four ordered dual pairings contribute a total unit coefficient \(1/4\). Move this scalar to the \(l=0\) sector for every Legendre character and every Jacobi mode before taking moduli. The residual quadratic boundary measure is \(D_W^{*2}-\delta_0/4\).

Next, within the sector of trivial Legendre character, collect certain contributions for each Jacobi exponent \(-8\le e\le8\) and each \(F\) above. For an ordinary cosine coefficient \(d_{r,|e|,00}\), write \(b_{r,e}\) for that coefficient divided by two if \(e\ne0\); impossible indices contribute zero. Put \(d_F=(1,-1,-1,1)\) in the displayed ordering. Three coefficients contributing to \(m^e F\) are
\[
 \frac{(j+1)\beta}{4}b_{j+1,e},\quad
 \frac{\binom{j+2}{2}\beta^2}{16} b_{j+2,e-d_F},\quad
 \frac{3\binom{j+3}{3}\beta^3}{16} b_{j+3,e}.
\]
The quadratic contribution is \(\Lambda^2 F^*=F\otimes\det F^*\). In the cubic, the three orderings of \(F^2F^*\) each contain two copies of \(F\), since \(F\otimes F\) is the sum of its irreducible symmetric and exterior squares. The six orderings of \(F G G^*\), with \(G\) the standard of the other rank-three group, each contain one more copy. This yields \(12/64=3/16\). All are arithmetic representation identities, including the Jacobi exponent of the exterior square.

Subtract the difference between the sum of the three absolute values and the absolute value of their sum from the corresponding weight costs. At twist one, \(m^eF\) has the three listed weights shifted by \(-e\). Summing the full set of labels and both exponent signs gives the same measure at twist \(\chi\). The code charges all remaining terms with their positive measures. This selected grouping only requires the quadratic unit and these specified linear, exterior-square, and cubic summands. It leaves further available character coincidences uncollected. Independent copies of the unknown residual are then convolved and projected using the [round-52 weight rule](astra-feedback-52.md#reading-rank-from-two-mellin-characters).

## Interval invariant and lower obstruction

Use the [round-54 frozen-zero invariant](astra-signed-54.md#freezing-the-zero-weight) with a separate rational 46-entry off-zero table per interval, \(\eta=1/5\), and residual cosine-hyperbolic moment \(\epsilon=6/10^5\). For a table \(h_k\) of the combined mass on \(\pm k\), the zero cap is \(\sum(k-1)h_k+\epsilon/\eta+10^{-8}\). For the omitted ordinary Taylor terms beyond degree 28 the input weighted norm sums the seed contributions
\[
 s\cosh\eta+|\alpha|(1+\cosh(2\eta))
  +|\beta|(1+3\cosh(\eta)/2+\cosh(3\eta)/2)
\]
and the residual norm. This bounds the full tail before making any character collections. The strict residual margin accommodates all marked-only product and seed corrections, of order \(O(n^{-1/2})\) in the first packet. For the use of raw conjugates at the exceptional lift, the error before activation is at most twice the product dimension, supported at the mark. The exact seed subtraction above already includes its own exceptional value.

The [interval records](astra-rankthree-55-checks.jsonl) bound the full scaled vector by 4.7. Since \(4.7/\sqrt{4(8135/512)-4.7^2}<3/4\), exact Picard iteration from the two distinguished seeds converges locally uniformly, with the actual marked activation and its smaller derivative for large \(q\). The [positive-factor identification](marked-domain-53.md#from-scalar-slack-to-the-actual-holomorphic-section) gives the stationary real pair and identifies the branch on overlaps. The resulting inverse hyperbolic sine at the mark is bounded by \(3/\sqrt n\).

For comparison take \(\alpha=c\), the same prescription for \(\beta\), and collect only the quadratic unit in the rank-three sector. At \(127/8\) the limiting positive map for this prescription escapes. For arities through eight, take lower endpoints of the degree-28 collected kernels and subtract from each single weight at arity \(j\) a uniform error bounded by the same ordinary Taylor tail at input mass \(s+2|\alpha|+3|\beta|+2\), divided by \(2^j\). Splitting into arithmetic summands preserves the dimension sum. Retain shifts through 14 and 24 output packets. The monotone lower iteration exceeds mass 21 at height 832 and the arity-two, zero-shift kernel atom exceeds \(1/20\). As in [round 54](astra-signed-54.md#lower-escape-with-the-full-irreducible-character-collection), Jensen gives subsequent full mass at least the square of the old mass divided by 20. This rigorous obstruction is restricted to the specified positive map. The strip above does not include \(127/8\).

1. Expand \(W^l\) in both full \(GL_3\) representation rings with the determinant Jacobi exponents, then collect *all* coincident irreducibles before computing packet costs. A strict interval invariant reaching \(127/8\) crosses the former barrier. A certified lower iteration above the quadratic escape threshold refutes that full specified map.
2. Incorporate the next distinguished \(K(C_1W)\) using its four rank-four constituents, retaining arithmetic contractions and the correct twist-dependent weights. Success requires overlapping complex rectangles below the present floor; an escaping positive lower recursion excludes the chosen subtraction and pooling scheme.
