# Signed terminal-source cancellation and an obstruction to RMS completion

For every sufficiently large prime in the round-38 log-star window, each sector carries half the squared norm of the true Picard endpoint difference, up to a vanishing additive error. The endpoint norm itself stays uniformly away from zero at **every** positive depth. In the cold limit the lower bound on the norm of each projection is $0.01084468$. Thus the explicit sufficient mean allowance in [round 39, Section 1](astra-positive-39.md) diverges in *each* sign throughout the short window. This rules out proving completion by making that particular allowance small. It gives no lower bound of this size on the optimal price of completion.

The arithmetic result also tests the signed endpoint against arbitrary moving upper hinges of the actual terminal source, including thresholds selected from its history. All results below apply through primes and through the eligible square fields with the inherited arithmetic laws. They do not prove simultaneous positive completion or the ordinary theta limit.

## A signed estimate uniform over the observed history

Write $Y_t=\sqrt n\,v_t$, $v_0=0$, $v_{t+1}=K\phi_t$, $\phi_t=(v_t^2+4w)^{1/2}$, $w_0=1, w_i=\tau/n$ otherwise, and $E=n^{-1}\sum_i$. Unsubscripted Euclidean norms are counting norms. For any fixed $B>0$ put
\[
 D=\lfloor \log_2^* q-\log_2^*\log_2^*q-C_B\rfloor .
\]
We may enlarge the constant in [round 38](vanishing-floor-38.md). Uniformly in $0\le\tau\le1$, $0\le r,s\le D+1$, and all real functions $F$ on $\mathbb R^{D+2}$ satisfying $F(0)=0$, $F(-u)=F(u)$, and Lipschitz constant at most one for the sup norm, one has
\[
 \left|E\big[(Y_r-Y_s)F(Y_0,\ldots,Y_{D+1})\big]\right|
     =O_B(D^{-B}).                                                   \tag{1}
\]
The arguments of $F$ are the successive values at the same spatial coordinate. The function may be chosen after the field, floor, and whole orbit are known. It must satisfy the displayed bounds and use the same function at every coordinate. In particular (1) does not allow an arbitrary coordinate-dependent Fourier test.

Here are the approximation and conductor details. Use the quantitative [round-30 closure, (5)–(9) and (15)](parallel-depth-window-30.md), with the [uniform-floor Bernstein step](vanishing-floor-38.md). Set $\epsilon=D^{-(B+5)}$. We have real negative Mellin expressions $N_t$ of weighted size and individual geometric resources at most $U$ through time $D+1$, with
\[
 \max_{t\le D+1}\|Y_t-N_t\|_{2,n}
      \le C D(\epsilon+q^{-1/4})=:\delta .
\]
One can take $U\ge \max(D+2,\epsilon^{-2},2)$ and allow one further resource of size $2^{C U^6}\le q^{1/8}$, uniformly. Indeed the incoming bound is an iterated exponential with one level per step and polynomial initial size in $D$. Changing a fixed outer power, allowing one more exponential and reserving a fixed power of $q$ costs a constant in $C_B$. More explicitly, dominate every enlarged resource step $2^{C u^6}$ with a tower $V_{j+1}=2^{V_j}$, $u_j\le V_j^{1/16}$, starting with $V_0=(U_0+C+2)^{16}$. Then $C V_j^{6/16}\le V_j/16$; choose $C_B$ so the last $V_j<q$. Its base has iterated logarithm at most $\log_2^*D+O_B(1)$.

For $k=D+2$, approximate $F$ on $[-U,U]^k$ by the tensor Bernstein polynomial with degree $m=\lceil k U^2/\epsilon^2\rceil$ in each variable. Its uniform error is at most $\epsilon$: the expected maximum coordinate error in independent binomial sampling is bounded by the square root of the sum of the variances, at most $U\sqrt{k/m}$. Symmetrize under simultaneous negation. The resulting polynomial $P$ has only even total degrees, and its weighted monomial coefficient norm at radii $U$ is at most $U 2^{mk}$. To see the latter, each affine binomial factor has coefficient norm one, each grid value of $F$ has modulus at most $U$, and the binomial coefficient sums multiply. In particular this last operation and the additional factor $N_r-N_s$ cost at most $2^{C U^6}$ in weighted size. The only geometric estimate on this final polynomial is the odd-word mean estimate; expansion weights sum absolutely. The resource ledger for the preceding iterates is unchanged.

Every term of $(N_r-N_s)P(N_0,\ldots,N_{D+1})$ is an odd word in negative expressions. Its mean is bounded by $C 2^{C U^6}/\sqrt q$. This is [round 30, proof of (7)–(8)](parallel-depth-window-30.md), applied to mixed words: an odd word has no punctual part at one, the generic-rank stalk bounds its mean there, and the bad-character errors are charged by the product of the weighted sizes. This use of parity only requires invariance under a *simultaneous* sign change.

Finally $\|Y_t\|_{2,n}=\|v_t\|\le2\sqrt{(1+\tau)t}$. The empirical RMS of $F(Y_0,\ldots,Y_{D+1})$ is at most $(\sum_t\|Y_t\|_{2,n}^2)^{1/2}=O(D)$. The RMS change on replacing all inputs by $N_t$ is at most $\sqrt k\,\delta$. Cauchy–Schwarz bounds the difference between the true pairing and its polynomial evaluation by $O(D\delta+\sqrt D(\sqrt k\,\delta+\epsilon))$. These bounds imply (1), without a sup estimate on any true iterate.

In particular define the nonnegative true source $S_t=\sqrt n(\phi_t-\phi_0)$. For any 1-Lipschitz $h$ on $\mathbb R_+^k$ in sup norm with $h(0)=0$,
\[
 \sup_{r,s,h}\left|E[(Y_r-Y_s)h(S_0,\ldots,S_{D+1})]\right|
 =O_B(D^{-B}).                                                       \tag{2}
\]
Off the mark $S_t=\sqrt{Y_t^2+4\tau}-2\sqrt\tau$, an even 1-Lipschitz function. At the mark the actual source divided by $\sqrt n$ equals $\sqrt{4+v_t(0)^2}-2\le v_t(0)^2/4$, and the bulk substitute divided by $\sqrt n$ is at most $|v_t(0)|$. Round 38 bounds their maximum over time by $O_B(D^{-B})$ after increasing the exponent there if necessary. The correction to the pairing from the single mark is bounded directly by this maximum times $|v_r(0)-v_s(0)|$. Thus (2) covers $h=(S_T-a)_+$ for *all* $a\ge0$, and, up to a factor two, positive excess over the maximum of earlier sources. Its measure is empirical counting measure. It supplies no estimate after reweighting by an arbitrary concentrated opposite-sector probability.

Writing $u=v_{T+1}-v_1$, $1\le T\le D$, we have $\sqrt n\, K u=S_T-E S_T$, since $K^2=I-J$. Also $E(Y_{T+1}-Y_1)=0$. Taking the terminal source itself in (2) gives the signed quadratic estimate and exact projection consequence
\[
 |\langle u,Ku\rangle|=O_B(D^{-B}),\qquad
 \|P_\sigma u\|^2=\tfrac12\|u\|^2+O_B(D^{-B})
 \quad(\sigma=\pm1).                                                \tag{3}
\]

## Why the actual endpoint cannot return to its starting value

Let $d_j=\|v_{j+1}-v_j\|$ and $g_t=(2\sqrt n)^{-1}\sum_i\phi_t(i)$. Picard is nonexpansive. For all finite fields and every $T\ge1$ the triangle inequality applied to $v_1,v_{T+1},v_{T+2},v_2$ gives
\[
 \|v_{T+1}-v_1\|\ge(d_1-d_{T+1})/2\ge(d_1-d_2)/2.                 \tag{4}
\]
The first two actual steps therefore suffice to exclude a return at *any* depth, provided they dissipate by a definite amount. In the [actual-increment identity](parallel-activation-26.md), discarding only nonnegative terms yields
\[
 d_1^2-d_2^2\ge4(g_2-g_1)^2
    +4\sum_{i\ne0}(-v_1(i)v_2(i))_+-8\tau.                         \tag{5}
\]
Indeed the coordinate loss is $2(\phi_1\phi_2-v_1v_2-4w)$; use $\phi_1\phi_2\ge|v_1v_2|$ off the mark and its nonnegative loss at the mark. Independently, omitting the *entire* coordinate loss always leaves $d_1^2-d_2^2\ge4(g_2-g_1)^2$.

For the cold limiting constants take any sequence $\tau_q\to0$. Define $A=\sqrt2\cos\Theta$ with $\Theta$ uniform on $[0,\pi]$, $m=2\sqrt2/\pi$, $b=2m/3$, and $Y$ the sum of two independent centered semicircle variables on $[-1,1]$, so $EY^2=1/2$. By the [actual second-state joint expansion](astra-prime-repair-38.md), the scaled pair $(Y_1/2,Y_2/2)$ has limiting bulk law $(A,A+bY+Z)$, where $A,Y,Z$ are independent and $Z$ is centered. In this sentence $Y$ without a subscript is the compact path variable. The coefficient $b=c_2(0)/2$ follows from $c_2(0)=4m/3$. These assertions about the infinite remainder follow by $L^2$ closure of the fixed finite joint laws. The second component has the uniform second moment needed to pass Lipschitz tests in it, and the first component is uniformly bounded. Finite-depth comparisons of floors are uniform here: per step changing $\tau$ to zero perturbs the activation by at most $2\sqrt\tau$ in counting norm. The marked activation is unchanged at a common input.

The first difference has $d_1\to d=2\sqrt{1-m^2}$, since $d_1=\|(I-J)(\phi_1-\phi_0)\|$ and its scaled bulk input tends to $2|A|$ in the cold limit. The marked excess has vanishing counting norm. Also $g_1\to m$ and $\liminf g_2\ge E|A+bY|$, by conditional Jensen. For $|z|\le\sqrt2$ the arcsine density gives
\[
 E|A+z|-m\ge z^2/(\pi\sqrt2),\qquad
 E\big[(-A(A+z))_+\big]\ge |z|^3/(6\pi\sqrt2).
\]
For the first inequality integrate $2\arcsin(z/\sqrt2)/\pi$ from zero, using symmetry. For the second integrate $t(|z|-t)/(\pi\sqrt{2-t^2})$ from zero to $|z|$. Now $|bY|\le2b<\sqrt2$. The crossing test is convex in the remainder $Z$, conditional on $A,Y$, and $E|Y|^3\ge(1/2)^{3/2}$. Thus
\[
 \begin{split}
 \liminf(g_2-g_1)&\ge a:=b^2/(2\pi\sqrt2),\\
 \liminf(d_1^2-d_2^2)&\ge L:=4a^2+2b^3/(3\pi).
 \end{split}                                                       \tag{6}
\]
The second term of $L$ has a factor 16 before the compact crossing expectation: the coefficient 4 in (5) and the two scale factors 2 in the limiting states.

The [Arb256 check](astra-completion-40-checks.jsonl) encloses $a>0.04054271$, $L>0.05245981$, and
\[
 \liminf_{q\to\infty}\inf_{T\ge1}\|v_{T+1}-v_1\|
  \ \ge\ c=(d-\sqrt{d^2-L})/2>0.01533669.
\]
Combining with (3) gives the cold lower bound $c/\sqrt2>0.01084468$ for the liminf of the norm of **either** projection, uniformly in the marked window.

There is also a positive lower bound uniform in the floor. At each fixed $0<\tau\le1$ the same second-state expansion gives $g_1\to E\sqrt{\tau+A^2}$ and $\liminf g_2\ge E\sqrt{\tau+(A+b_\tau Y)^2}$, $b_\tau=c_2(\tau)/2>0$. Positivity of $c_2$ follows from strict positive covariance of $T_2(\cos\Theta)$ with the strictly increasing function of it defining the activation. Strict convexity yields a strict mean gain for every positive floor. The displayed lower bound on the gain is continuous in $\tau$ on $[0,1]$, by bounded convergence; at zero (6) is positive. It consequently has a positive minimum. This is uniform for varying floors as well: on each fixed finite prefix the norm change between floors $\tau,\tau'$ costs at most $2t\sqrt{|\tau-\tau'|}$ by nonexpansiveness. The $d_1$ are uniformly bounded by $d_0\le2$. Equations (3)–(4) and $d_1^2-d_2^2\ge4(g_2-g_1)^2$ give the asserted positive lower bounds.

## Consequence for simultaneous completion

The [round-39 construction](astra-positive-39.md) sets a sufficient scaled mean increment in sign $\sigma$ equal to
\[
 s^{\rm RMS}_\sigma={2 n^{1/4}\over T}\,
       \|P_{-\sigma}(v_{T+1}-v_1)\|.
\]
At fixed or varying floors in $[0,1]$, each of these prescribed sufficient increments is $\gg n^{1/4}/T$ throughout the arithmetic window, and hence diverges there. Outside the window (4) still gives the same lower order for the *maximum* of the two prescribed increments at every $T$, since the projections are complementary on mean-zero vectors. This argument concerns the price supplied by that RMS inequality. The same anchored reflection might succeed at a much smaller increment when its signed spill is controlled.

In particular (2) proves cancellation with the entire Lipschitz source history while (3) and (6) force positive energy in both actual projected endpoints. A completion proof using a signed pairing would still need to handle the opposite positive feasible test, or its concentration on spatial sites. No uniform Lipschitz representation of those tests by the source history has been established. The square obstruction to genuine simultaneous completion from [round 38](vanishing-floor-38.md) is compatible with all the signed tests above.

Run `.venv/bin/python -B research/astra-completion-40-check.py` to reproduce [seven records](astra-completion-40-checks.jsonl). The first checks the cold analytic constants. The other six enclose the actual unrounded $p=101$ Picard prefix at two floors and three times and verify the centered-source, sector-energy and no-return formulas. The uniform theorems use the proofs above.
