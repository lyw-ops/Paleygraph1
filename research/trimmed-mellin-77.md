# A stronger trimmed-mass obstruction from the true cold orbit

The near-minimal clipped-tail regime can be ruled out even when the trimmed mass is larger than the round-76 necessary lower bound by any fixed power of the marked depth. The estimate combines forbidden-projector coherence with the finite-depth approximation of the *actual* nonlinear orbit. It applies to a true feasible row with a fixed supercritical mark and allows arbitrary square-root-sized deletions.

## Statement

Put \(\Lambda=\log_2^*p\), and fix \(0<\varepsilon<1\) and \(\delta>0\). Allow any threshold \(B\ge0\).
Let \(q\) be feasible on either true sector, \(n=(p-1)/2\), \(x_i=(q_i-B/n)_+\), and \(A\subset G\) arbitrary with
\[
                       |A|\le (1-\varepsilon)^2 n/(1+\sqrt p).
\]
Set \(H=\max(2,n^{1/4}\sum_{i\notin A}x_i)\). For all sufficiently large eligible primes, uniformly over \(q,A,B\),
\[
  \sqrt n\,q_0\ge1+\delta
            \quad\Longrightarrow\quad
  \log_2^*p-\log_2^* H\le C_{\delta,\varepsilon}(1+B).          \tag{1}
\]
In particular, at \(B=o(D(p))\) the trimmed mass multiplied by \(n^{1/4}\) must grow faster than every fixed power of \(D(p)\) for a fixed supercritical gap. It also exceeds every \(H_p\ge2\) with \(\log_2^* H_p\le(1-\kappa)\Lambda\) for a fixed \(0<\kappa<1\) in that regime. At a fixed \(B\), it is at least a fixed iterated logarithm of \(p\) with a finite number of iterations depending on \(\delta,\varepsilon,B\). These statements follow from (1) and \(D(p)\asymp\Lambda\). The conclusion covers a singleton root, all high sites in \(A\), and choices of \(A\) made after observing the window.

## The cold approximation at the shorter horizon

Use the geometric closure estimate (7) of [round 30](parallel-depth-window-30.md#2-quantitative-closure-and-a-separate-geometric-ledger) and the vanishing-floor polynomial budget of [round 38](vanishing-floor-38.md#1-uniformity-of-the-marked-arithmetic-as-the-floor-vanishes). Suppose (1) fails uniformly. Then there is a sequence of eligible primes with fixed supercritical gap and \(g=\Lambda-\log_2^*H\) satisfying \(g/(1+B)\to\infty\). In particular \(g\to\infty\) and \(B=o(g)\). Set \(J=\lfloor g/8\rfloor\), and use a polynomial approximation error \(e=(H+\Lambda)^{-4}\) at each step. The exact cold recurrence is
\[
 Y_{t+1}=\beta_t\sqrt n K e_0+K|Y_t|,
 \qquad \beta_t=\sqrt{4+v_t(0)^2}-|v_t(0)|\in[0,2].
\]
The coefficient \(\beta_t\) is the actual field-dependent scalar and is retained unchanged. If the current negative-field expression has resource budget \(U_t\) and hence sup norm at most \(U_t\), take \(U_t\ge e^{-2}\) and the even Bernstein polynomial on \([-U_t,U_t]\) with error at most \(e\). Its weighted coefficient sum \(S_{U_t}\) and the next expression budget, including the controlled source and the exceptional lift corrections, are bounded by \(U_{t+1}=2^{C U_t^4}\) with an absolute \(C\), by the cited estimates. The transported replacement costs at most \(C S_{U_t}/\sqrt p\) in normalized \(L^2\). Since absolute value is 1-Lipschitz and \(K\) contracts \(L^2\), induction gives approximation error at most \(\sum_{u<t}(e+C U_{u+1}/\sqrt p)\). This uses the polynomial bound on the range of the approximant; no pointwise bound on the exact \(Y_t\) is assumed.

Start with \(U_0\) a fixed constant multiple of \(e^{-2}+1\), and \(V_0=(U_0+C+2)^8\). The tower \(V_{t+1}=2^{V_t}\) dominates the resources by \(U_t\le V_t^{1/8}\), after increasing the absolute base constant if necessary, since \(C V_t^{1/2}\le V_t/8\). Its initial iterated logarithm is at most \(\max(\log_2^* H,\log_2^*\Lambda)+O(1)\). The gap from \(\Lambda\) to this maximum is \(\min(g,\Lambda-\log_2^*\Lambda)\ge g/2\) eventually. Iterating through \(J+2\) therefore gives \(\log^* V_t\le\Lambda-3\) eventually. Thus \(V_t\le\log_2\log_2 p\): if \(T_j\) is the tower sequence starting at 1, these inequalities give \(V_t\le T_{\Lambda-3}\) and \(p>T_{\Lambda-1}\). In particular the budgets are at most \(p^{1/8}\), and \(H\le\log_2\log_2 p\) eventually since \(g\to\infty\).

It follows that there exist uniform approximants \(\widetilde Y_t\) to every actual iterate through \(J+1\) with
\[
 \|\widetilde Y_t\|_\infty\le p^{1/8},\qquad
 \|Y_t-\widetilde Y_t\|_{2,n}\le C(J+2)(e+p^{-3/8})
                      =o\big((H+\sqrt\Lambda)^{-1}\big).         \tag{2}
\]
For each \(p\) and scalar \(H\), the construction uses only \(H\) and the actual cold orbit; it needs no information about the coordinates of \(q\) or \(A\). No bounded-depth estimate has been interchanged with the field limit.

## Apply the actual signed comparison

If \(n^{1/4}M_E\le H\) with \(M_E=\sum_{i\notin A}x_i\), (2) of [round 76's trimmed projection estimate](astra-masked-76.md#removing-arbitrary-exceptional-coordinates) gives
\[
 \sqrt n\|x\|_2\le C_\varepsilon(\sqrt B+H),
 \qquad \sum_i x_i\le C_\varepsilon n^{-1/4}(\sqrt B+H).         \tag{3}
\]
The second inequality uses \(\sum_A x_i\le\sqrt{|A|}\,\|x\|_2\) and the bound on \(M_E\). Counting norms are used in (3). The \(L^2\) control extends to the discarded coordinates, including the root.

Take \(d=\lfloor\sqrt{J\max(1,B)}\rfloor\), so \(d\to\infty\), \(d=o(J)\) and \(B=o(d)\). Apply the [selected smooth-window construction](relative-window-77.md#paired-rows-with-a-nonnegative-bulk-constant) in the shorter horizon \(J\) at fixed taper exponent \(m=4\). The exact mark bounds through the full \(D(p)\) apply on this shorter horizon. Its allowance tends to zero, and \(\|(R_s)_-\|_{1,n}\le C/d\). In (1) of the relative-window note replace the raw positive parts \(u_{s,t}=(sY_t)_+\) by those of \(\widetilde Y_t\). Keep the exact constant and pin coefficients, and evaluate only on the bulk. This gives a bulk approximant \(\widetilde R_s\) with sup norm \(O(p^{1/8}+1)\) and normalized \(L^2\) error \(o((H+\sqrt\Lambda)^{-1})\). The absolute coefficient sums in that formula are at most two, so the error is the maximum in (2) times an absolute constant. The pin coefficients are bounded on the selected windows by the true mean and mark bounds.

Pair the exact negative part with \(q\) in the opposite sector. The low part \(z=q-x\le B/n\) contributes \(O(B/d)=o(1)\). The \(x\) part is at most
\[
 O(p^{1/8}+1)\sum_i x_i+
       \sqrt n\|x\|_2\,\|R_s-\widetilde R_s\|_{2,n,\mathrm{bulk}}
       = o(1),                                                   \tag{4}
\]
by (2)–(3) and \(H\le\log_2\log_2 p\). This follows from the Lipschitz property of the negative-part function and Cauchy–Schwarz, with the root omitted. But exact complementary orthogonality requires
\[
 \sum_{i\ne0}q_i (R_s(i))_-\ge m_s(\sqrt n q_0-1-\epsilon).
\]
For a fixed supercritical gap the right side is bounded below by a positive constant, contradicting (4). This proves (1), without any assumption on the locations of the deleted sites or the actual mask. The argument bounds a restricted tail regime through primes. It does not establish that a true primary optimizer is in that regime or resolve the conjecture.

## Ranked next tests

1. On an actual larger primary face test whether the trimmed mass admits a bound below the new tower-scale threshold for at least one growing \(B=o(D)\). Use the arbitrary-deletion bound to remove the root and high points before measuring the remainder.
2. If the remaining mass is outside this range, estimate the density and height band of the signed Schur interaction at an actual selected window. The proof above identifies the required role of an approximation stronger than a bounded-error normalized \(L^2\) proxy for larger tail masses.
