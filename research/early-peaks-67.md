# Growing two-sided peaks of the actual second cold state

Let \(p\equiv1\bmod4\) be prime, \(n=(p-1)/2\), and let the floor \(\tau_p\) tend to zero through \([0,1]\). Use the true Picard orbit and \(V_t=\sqrt n\,v_t/2\). All logarithms below are natural. Write
\[
m=\frac{2\sqrt2}{\pi},\qquad
H_p=\left\lfloor\frac{(\log p)^{1/3}}{\log\log p}\right\rfloor,\qquad
H=\min\big(H_p,\ \lfloor\tau_p^{-1/2}\rfloor\big),
\]
with the second entry omitted at \(\tau_p=0\). There are \(p^{1-o(1)}\) bulk coordinates with \(V_2\ge m\log H-O(1)\), and as many with \(V_2\le-m\log H+O(1)\). At zero floor the lower bound on each signed peak is \((m/3)\log\log p-m\log\log\log p-O(1)\) after the second update. The same lower bound holds for each signed average of the largest \(\lfloor c\sqrt n\rfloor\) values, for any fixed \(c>0\).

For \(\tau_p\ge H_p^{-2}\) with \(\tau_p\to0\), both signed bulk maxima and both of those upper-tail averages equal \((m/2)\log(1/\tau_p)+O(1)\). Thus at floors of order \(1/D(p)\) the first two states cost \(O(\log D(p)/D(p))\) in a normalized prefix bound at \(T\asymp D(p)\) that pays their sup norms individually. At zero floor, paying even the second state in that way cannot be small at depths \(T\le D(p)\). This is an ordinary all-prime estimate for the actual early states. It permits cancellation with later states in the actual average. [Marked depth](vanishing-floor-38.md) · [Two-lift path fields](parallel-graph-shapes-23.md)

## Exact coefficients and a uniform tail estimate

Put \(X_p=\sqrt{n/p}\,x\) with \(x=\sqrt n K e_0\), and \(a=(1-\sqrt{\tau_p/n})\sqrt{p/n}\), so \(V_1=aX_p\). Here \(|X_p|\le1\). For \(a\) in a fixed compact subinterval of \((0,\infty)\), let \(b_h(a,\tau)\) be the coefficient of \(T_{2h}\) in \(u\mapsto\sqrt{\tau+a^2u^2}\). In these variables,
\[
V_2 = O(1) + \sum_{h\ge1} b_h(a,\tau_p) K T_{2h}(X_p)
\tag{1}
\]
where the \(O(1)\) is a uniformly bounded vector. Indeed the true marked activation is separated by one multiple of the bounded column \(x\), and \(K\) kills the constant coefficient. The correct coefficient of \(x\) is \(\sqrt{4+v_1(0)^2}/2-\sqrt{\tau_p+a^2X_p(0)^2}/\sqrt n\).

At zero floor \(b_h(a,0)=2m_a(-1)^{h-1}/(4h^2-1)\), where \(m_a=2a/\pi\). Uniformly for \(0\le\tau\le1\), \(|b_h(a,\tau)|\le C h^{-2}\), and for positive \(\tau\) also \(|b_h(a,\tau)|\le C\tau^{-1/2}h^{-3}\). To see both for positive \(\tau\), set \(f(u)=\sqrt{\tau+a^2\sin^2u}\). On \([0,\pi/2]\),
\[
f''(u)=a^2\tau\cos^2u/f(u)^3-a^2\sin^2u/f(u).
\]
The first term decreases and the positive magnitude of the second term increases. Thus \(f''\) decreases, \(f'\) has variation at most \(2a\), and the variation of \(f''\) is at most \(C\tau^{-1/2}\). Symmetry and integration by parts give the coefficient estimates. The zero-floor bound follows from the exact coefficient formula.

For \(h\le\tau^{-1/2}\) one has
\[
|b_h(a,\tau)-b_h(a,0)|\le C\tau\,\big(1+\log(1/(h\sqrt{\tau}))\big).
\tag{2}
\]
The difference in the defining Fourier integral, shifted to \([0,\pi/2]\), is the decreasing function \(d(u)=f(u)-a\sin u\). Its bound \(\min(\sqrt{\tau},C\tau/u)\) follows by rationalizing and \(\sin u\ge2u/\pi\). The integral up to \(1/h\) is bounded by the right side of (2). In the rest integrate against an antiderivative of \(\cos(2hu)\), using monotonicity to bound the integral by \(C d(1/h)/h\le C\tau\). The sign from shifting the cosine is immaterial. Summing (2) with weights \(2h\) up to any \(H\le\tau^{-1/2}\) costs \(O(1)\), since \(\sum_{h\le J}h(1+\log(J/h))=O(J^2)\) for \(J\ge1\). Therefore
\[
R_H:=\sum_{h\le H} 2h|b_h(a,\tau_p)|=m\log H+O(1).
\tag{3}
\]
If \(H=\lfloor\tau_p^{-1/2}\rfloor\), the cubic coefficient bound gives \(\sum_{h>H}2h|b_h(a,\tau_p)|=O(1)\).

For every even degree \(2h\), the exact two-lift formula of round 23 writes \(K T_{2h}(X_p)=\widetilde Y_h+e_h\). Here \(\widetilde Y_h\) averages the two full Mellin traces of convolution dimension \(2h\), with generic rank \(2h\). The identity stalk after twisting vanishes for even degree. The only correction in the formula is \(\delta_{2h}\lambda_k/n\), with \(|\delta_{2h}|\le2\), so \(\|e_h\|_\infty\le2\sqrt p/n\) for all \(h\). The dimension bound on every Mellin trace gives \(|\widetilde Y_h|\le2h\), including exceptional lifts. Consequently (1)–(3) give the claimed matching upper bounds whenever \(\tau_p\ge H_p^{-2}\). These bounds use absolute summability at positive floor. At zero floor the Chebyshev series of the activation still converges absolutely before \(K\), and its tail beyond \(M\) has normalized \(L^2\) norm at most \(C/M\) after \(K\). [Exact formula and groups](parallel-graph-shapes-23.md#a-fixed-number-of-path-columns-gives-no-leading-gain)

## A growing-degree comparison on an extreme-weight test

For the lower bound choose \(M=\lfloor p^{1/10}\rfloor\), which exceeds \(H\) eventually. Use all the indicated even path factors through \(2M\). Their two full-character groups at each degree are symplectic, and the good-character compact geometric and arithmetic groups are their full product by the round-23 group computation. In the compact model write \(Y_h\) for the average of the two independent standard traces of matrix size \(2h\). The point of using a polynomial test with a dimension-normalized expansion is to make the degree and the arithmetic error explicit when \(H\) and \(M\) vary.

For a polynomial in those traces, define its weighted coefficient sum \(W\) from an expanded expression by assigning to each monomial the product of the convolution dimensions of its factors and summing absolute coefficients times those products. If the maximum number of factors in a monomial is \(k\), the error of comparing its true mean to its product compact expectation is
\[
C W\big(k/\sqrt p+M^2/p\big).
\tag{4}
\]
Indeed the good-character set of the direct sum of the paths is good for its tensor category. There are \(O(M^2)\) bad characters since the sum of their ranks is \(O(M^2)\). At the bad characters both the product and its tensor replacement are bounded by the product dimension, by purity. Averaging the resulting convolution traces over all full characters evaluates their identity stalk. Punctual summands give the compact character integral. For the other part the absolute stalk trace is at most the generic rank divided by \(\sqrt p\). That rank is at most \(k\) times the product dimension by the generic-fiber Euler-characteristic bound \(R(A\star B)\le R(A)D(B)+D(A)R(B)\), as \(R=D\) for the nontrivial generators. The punctual unit has rank zero. Summing proves (4). The bound applies to lift-invariant functions on the square subgroup by averaging over all full characters. Taking a real part, if needed, costs no extra dimension weight, by including the duals. [Good characters and Mellin trace bounds](https://web.math.princeton.edu/~nmk/mellin331.pdf) · [Rank and exceptional-character estimates](parallel-depth-window-30.md#2-quantitative-closure-and-a-separate-geometric-ledger)

Fix one of the two desired signs \(\sigma\in\{\pm1\}\). Set \(\varepsilon_h=\operatorname{sgn}(\sigma b_h)\) for \(h\le H\), choosing either sign for a zero coefficient. Put \(\eta=1/\log(H+2)\), \(B=\lceil H^2\log^3(H+2)\rceil\), and use the polynomial
\[
F=\prod_{h\le H}\left(\frac{1+\varepsilon_h Y_h/(2h)}2\right)^B.
\]
On the actual field evaluate this polynomial at \(\widetilde Y_h\). In both cases \(0\le F\le1\), and the dimension-weighted coefficient sum in its expansion is at most one. Its degree in Mellin traces is at most \(HB\).

The compact expectation of \(F\) is at least \(\exp(-C H^3\log^2(H+2))=p^{-o(1)}\), since \(H\le H_p\). Indeed, for each compact factor of matrix size \(d=2h\), a Frobenius ball of radius \(\sqrt{\eta}\) about \(\varepsilon_h I\) has Haar mass at least \((1+2\sqrt{d/\eta})^{-2d^2}\) by a separated covering in the ambient real dimension \(2d^2\) and translation invariance. On this ball the signed normalized trace is at least \(1-\eta/2\), by the exact Frobenius-distance identity. Apply the ball bound to both members of each pair. This gives the expectation bound by multiplying their masses and \((1-\eta/4)^B\) at each \(h\). Under the probability weighted by \(F\), the variables remain independent. At any \(h\le H\) its signed normalized trace average lies below \(1-\eta\) with probability at most
\[
\exp\big(C h^2\log(h/\eta+2)-B\eta/4\big)\le\eta
\]
for large \(H\). The numerator on this lower set is at most \((1-\eta/2)^B\), and the previous single-pair lower bound gives the denominator. Thus the \(F\)-weighted compact expectation of \(R_H-\sigma\sum_{h\le H} b_hY_h\) is at most \(3\eta R_H=O(1)\).

Apply (4) to \(F\), the product of \(F\) with the preceding deficiency, and
\[
F\left(\sum_{H<h\le M} b_hY_h\right)^2.
\]
Their respective dimension-weighted coefficient sums are at most \(1,2R_H,O(\log^2 p)\), and their degrees are at most \(HB+2\). Each arithmetic error after division by the \(F\)-mean is \(o(1)\), since \(HB=p^{o(1)}\), \(M^2=O(p^{1/5})\), and the denominator is \(p^{-o(1)}\). The compact middle-tail squared moment under the weight is \(\frac12\sum_{H<h\le M} b_h^2=O(H^{-3})\) by independence and centering. It follows that the total actual \(F\)-weighted mass is \(p^{-o(1)}\) and, after normalizing it to a probability, the deficiency has bounded mean and the middle tail has \(o(1)\) second moment. Here the true deficiency is nonnegative because of the exact Mellin dimension bounds.

The error from replacing the true \(KT_{2h}\) by its Mellin average through \(M\) is \(O(p^{-1/2})\) in supremum norm, since \(\sum_h|b_h|=O(1)\). The normalized squared \(L^2\) tail beyond \(M\) is \(O(M^{-2})\). Since \(F\le1\), its \(F\)-weighted second moment after normalizing is \(o(1)\). Markov's inequality now gives a fixed positive fraction of the \(F\)-weight where the deficiency is bounded by a constant and both tails have absolute size at most one. With \(F\le1\) this is a counting fraction \(p^{-o(1)}\), and deleting the mark still leaves \(p^{1-o(1)}\) coordinates. Equation (1) and (3) prove the stated result, separately for both signs.

## What this rules out for early positive repair

At time one the exact projected row satisfies \(\sqrt n X_{\sigma,1}(i)=\sigma V_2(i)/2+O(1)\) off the mark. This follows from the sum and difference formulas, because \(V_1\), the first bulk activation and the first two scaled means are uniformly bounded. The canonical mean injection \(s(1-P_\sigma e_0/(P_\sigma e_0)_0)\) adds \(s(1+O(p^{-1/2}))\) at each off-mark entry and preserves the mark. Therefore time-one completion by this bulk injection alone requires
\[
s\ge (m/2)\log H-O(1)
\]
for either sign. This lower bound is for the specified injection. Signed repairs or a longer genuine average may change these peaks. In particular the proof makes no claim of a lower bound on all late averaged deficits or of an all-prime ordinary-theta limit. [True projected rows](averaged-mark-35.md#3-projected-averages-have-balanced-marks) · [Canonical injection](true-spill-63.md#the-signed-and-absolute-tests)

At zero floor the peaks also identify a necessary avoidance test for the exact larger face. Let \(S_p=\{i\ne0:|V_2(i)|\ge m\log H_p-C\}\) for a constant \(C\) as in the peak bound. For any whole probability \(q_s\) on the larger true face with mark \(\alpha/\sqrt n\) and any \(3\le t\le D(p)\), round 66 gives
\[
\begin{split}
(2m\log H_p-2C)q_s(S_p)
&\le \mathbb E_{q_s}|Y_2|
=m_{s,3}(q_s)-\alpha b_2+2g_2\\
&\le m_{s,t}(q_s)-E_t/4+O(1),
\qquad Y_j=2V_j .
\end{split}
\]
The last bound subtracts the charged reserve at time three from the same row's charge at time \(t\). All differences other than \(-\alpha(B_t-B_3)\) are nonnegative because \(\alpha\ge1\). The early energy and means are bounded and \(B_t=o(1)\) on the marked window. Thus an \(o(L)\) upper certificate on the larger face at \(L+1\) requires a minimizing row that puts \(o(L/\log\log p)\) mass on \(S_p\). A uniform positive lower bound of order \(L/\log\log p\) on this mass for every row of the larger face along a prime subsequence at time \(L\) would reject the late charged estimate throughout that subsequence by round 66. The empirical size of \(S_p\) alone does not give either endpoint weight bound. [Exact signed reserve and fixed-late-time barrier](astra-charged-66.md)

## Ranked next tests

1. On the weighted patches realizing the second-state peaks, test the joint signed sum of subsequent actual iterates in a growing marked window. A pointwise bound on the endpoint difference or its signed projected spill sufficient to repair both whole rows with \(s=o(1)\) passes. A positive inherited peak after the full signed correction at every late time would reject that correction.
2. Estimate the contribution of the same patches under the true optimal Fourier laws at the fixed late times from round 66. The weighted empirical construction supplies many extreme sites, while a useful charged bound must control their actual endpoint probability. It is the latter bound that could pass the single-time criterion.
