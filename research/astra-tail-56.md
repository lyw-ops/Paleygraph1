# Shortening the actual exposed-tail cycle cover on the growing prime window

Let $n=(p-1)/2$, $Q=\mathbb F_p^{\times2}$, $G=\widehat Q$, for primes $p\equiv1\bmod4$. Use the two exact exposed supports, oriented scores $Z_s(i)=s\sqrt n\,v_t(i)$, point caps $q_s$, and terminal energy $E_t=\sum_i v_t(i)^2\le4t$ of the [one-time face program](astra-tail-53.md). For a dictionary of translated odd-cycle tests, let $I_t$ be the integrated maximum of its two tail capacities, including the lower endpoint as in [(3) of round 55](astra-translated-55.md). Cycles below are vertex-simple unless identified as walks.

On **every** sufficiently large eligible prime, using just cycles of length at most the nearest odd integer to $n^{1/4}$ changes this integrated upper bound by at most $O(\sqrt t)$, uniformly in the two actual exposed supports and in time. In particular it changes the charged minimum per step over $D(p)/2\le t\le D(p)$ by $o(1)$ in the [proved growing window](vanishing-floor-38.md). Thus longer simple cycles cannot repair a positive asymptotic failure margin of this shortened program. Adding valid single-edge Fourier constraints gives a stronger upper program for which length $n^{1/8}$ already suffices to the same accuracy. Neither cutoff alone proves that the charged minimum is small.

## Fourier coefficients from translates of a triangle

For side $s$ let $D=\{d\in Q:\chi(1-d)=-s\}$. The primal of the round-55 covering LP at $T=S_s\cap\{Z_s>u\}$ maximizes the mass $m=\sum_iw_i\le1$ over $0\le w_i\le q_s\mathbf1_T(i)$ with
\[
 \sum_i w_i V_C(i-a)\le c_g(1-m)\quad(a\in G),\qquad
 V_C(i)=\frac1g\sum_{j=1}^g\operatorname{Re}i(d_j),\quad c_g=\cos(\pi/g).
\]
Here the forbidden oriented steps $d_j$ run around the cycle. Finite LP duality gives this program. Imposing the mass cap gives exactly the outer truncation at one, since all packing constraints are homogeneous upper bounds under downscaling.

Write $\varepsilon=-s$. For any $x\in Q\setminus\{1\}$ the number of simultaneous neighbors of $1,x$ in the forbidden graph is
\[
 N(x)=\#\{e\in Q:\chi(1-e)=\chi(x-e)=\varepsilon\}
 \ \ge\ (p-15-2\sqrt p)/8.                                             \tag{1}
\]
Expand $(1+\chi(e))(1+\varepsilon\chi(1-e))(1+\varepsilon\chi(x-e))$ and remove $e=0,1,x$. The pair sums are $-1$ before their coefficients, as $\chi(-1)=1$. The cubic sum $A=\sum_e\chi(e(1-e)(x-e))$ has $|A|\le2\sqrt p$ by Hasse for the nonsingular Legendre curve, and removing the three exceptional terms costs at most 12. If $x\in D$ the exact count is $8N(x)=p-11-4\varepsilon+A$. Multiplication by any vertex in $Q$ gives the same lower bound for common neighbors of arbitrary distinct vertices. This is the triple-intersection count with the two specified signs. [Brouwer and Martin](https://par.nsf.gov/servlets/purl/10389096)

For $p\ge29$, each $d\in D$ therefore occurs in a forbidden triangle. With $\widehat w(d)=\sum_i w_i i(d)$, the triangle constraint says that the function of $a$ given by $F(a)=(1-m)/2-\sum_iw_i V_3(i-a)$ is nonnegative. Its mean is $(1-m)/2$. Its Fourier coefficient at $d$, in absolute value, is $k|\widehat w(d)|/6$, where $k\ge1$ counts occurrences among the three steps and their inverses with multiplicity. All these contributions have the same coefficient. Bounding the coefficient by the mean yields
\[
              |\widehat w(d)|\le3(1-m)\quad (d\in D).                    \tag{2}
\]
Conversely $\max_D|\widehat w|\le(1-m)/2$ suffices for **all** translated odd-cycle constraints, since $c_g\ge1/2$. At mass one the triangle translates alone recover all forbidden zeros. At general mass the two inequalities sandwich the cycle packing between capped Fourier discrepancy programs. In particular asymptotic unit capacity holds exactly when there exist supported subprobabilities with the prescribed point caps, mass tending to one and forbidden Fourier discrepancy tending to zero. For sufficiency rescale by $1/\max(1,m+2\max_D|\widehat w|)$. This statement allows nonuniform witnesses on the actual tails.

## Uniform shortening and its integrated error

Let $G_0\ge5$ be odd, $L=G_0-2$, and suppose the right side of (1) exceeds $L+1$. Keep every translated simple cycle of length at most $G_0$. Given a longer cycle of length $g$, take any consecutive $L$ steps. The endpoints are distinct. Choose a common neighbor outside its $L+1$ vertices by (1). The segment and the two connectors give a simple forbidden $G_0$-cycle. For fixed $a$, put $u_d=\sum_i w_i\operatorname{Re}(i-a)(d)$. By (2) the two connector terms are at least $-6(1-m)$ in total. Hence the segment has total at most $[G_0c_{G_0}+6](1-m)$. Sum over all $g$ starting points. Each original edge is counted $L$ times. The longer cycle inequality follows with its right hand side multiplied by
\[
 H=\frac{G_0c_{G_0}+6}{L c_{G_0}}=1+\frac{2+6/c_{G_0}}L ,
\]
since $c_g\ge c_{G_0}$. Thus scaling $w$ by $1/[m+H(1-m)]$ makes it feasible for the full dictionary, retaining the point cap. If $F_{G_0}(u)$ and $F_\infty(u)$ are the respective maxima of the two side capacities, monotonicity of $m/[m+H(1-m)]$ gives
\[
 0\le F_{G_0}-F_\infty\le(H-1)F_{G_0}(1-F_{G_0}).                         \tag{3}
\]
The result also controls individual coefficients with near-sharp constants at high order. For $d\in D$ of even order $r$, use an odd $L<r$ of size comparable to $r$ with $L+1<N(d^L)$. The largest odd integer below $\min(r,p/32)$ works for large $p,r$. Apply the segment estimate to $1,d,\ldots,d^L$, then maximize over $a$. The maximum is at least $|\widehat w(d)|\cos(\pi/r)$. This yields $|\widehat w(d)|\le(1+O(1/r))(1-m)$ in the full packing. For odd order $r\ge3$ the simple $d$-cycle has coefficient $c_r$ already, giving $|\widehat w(d)|\le1-m$ exactly.

Put $q=\max_s q_s=O(n^{-1/2})$ by the Jacobi point bound. For $u>0$ the point caps imply $F_{G_0}(u)\le\min(1,qnE_t/u^2)$. For $u<0$, any true row restricted to its tail is feasible, so $1-F_{G_0}(u)\le\min(1,qnE_t/u^2)$ by the same bound on its lower tail. Both estimates use $\sum_i Z_s(i)^2=nE_t$. Integration on the line, taking identical affine terms for both dictionaries, gives
\[
 0\le I_{G_0,t}-I_{\infty,t}\le4(H-1)\sqrt{qn E_t}.                      \tag{4}
\]
Taking $G_0\asymp n^{1/4}$ proves the claimed $O(\sqrt t)$ bound. In (3) the integrated profile $\int F_{G_0}(1-F_{G_0})$ can be much smaller than the field-uniform estimate.

For the strengthened program impose also $|\widehat w(d)|\le1-m$ for all $d\in D$. Each actual restricted row satisfies this by cancellation with its discarded complement. Inversion preserves every score and support when using even exposed rows, so inversion averaging permits real Fourier coefficients and two linear inequalities per frequency. Now any longer cycle has left side at most $1-m$, permitting $H=1/c_{G_0}=1+O(G_0^{-2})$ in (3)–(4), without (1). This proves the $n^{1/8}$ cutoff. For this strengthened program one can exactly separate all truncated cycle constraints using **closed walks**. For each translate and length, maximize the sum of the step weights $u_d$ on walks returning to identity, by dynamic programming on the current group element and length. The frequencies $d,d^{-1}$ have the same $u_d$. Any odd closed walk of length $g\le G_0$ decomposes into simple cycles and two-step retracings, including at least one odd simple cycle of length $j\le g$. That cycle costs at most $jc_j(1-m)$, and the other steps individually cost at most $1-m$. Since $j(1-c_j)\ge g(1-c_g)$ by differentiation of $x(1-\cos(\pi/x))$ for $x\ge3$, their total is at most $gc_g(1-m)$. Thus this separation procedure enforces exactly the stipulated strengthened constraints.

## A missing parity constraint and an actual finite tail gap

At every eligible $p\ge29$, one sign forbids the involution $d=-1\in Q$. All its true laws put exactly $1/2$ on either parity coset in $G$. Without the exposed-support restriction, the all-simple-cycle capacity of such a coset equals **$3/5$** whenever $q_s\ge 6/(5n)$, as holds eventually. Translation averaging within the coset makes any packing uniform there, with its only nonidentity Fourier coefficient $\pm m$ at the involution. A forbidden triangle through $d$ gives $m/3\le(1-m)/2$, with the translate aligned to the coset. Conversely the $d$-edges are a matching. In every triangle at most one edge contributes, and in longer odd cycles at most half the edges contribute. Since $c_g\ge c_5>3/4$ for $g\ge5$, mass $3/5$ passes all tests. This gap matters if the last program is used as a replacement for the original one.

At $p=97$ the gap also occurs **inside** the exposed minus support. On its even sites $0,\pm4,\pm12,\pm16,\pm20,24$ put per-site numerator 2, except 3 at 24, over denominator 39. The total is $m=7/13$ and every point respects the actual cap. The forbidden involution coefficient is $m$, while every other forbidden coefficient is at most $1/13$ in modulus by the cyclotomic calculation. Triangles through the involution have average at most $(m+2/13)/3=(1-m)/2$. Every other triangle has average at most $1/13$. Longer cycles have average at most $(m+1/13)/2<c_5(1-m)$. The simple-cycle packing on these exact exposed parity sites thus exceeds the true mass by at least $1/26$. Parity itself is not a cold threshold.

For actual cold thresholds on both true $p=97$ supports, the integrated lower bound for the whole simple-cycle covering program exceeds an upper bound on the full-face minimum by at least $0.001115t$ **at every integer $16\le t\le32$**. Its own terminal-energy-corrected value is at least $0.048305t$ throughout. At $t=32$ the cover is at least 2.601376 and the chosen feasible pair gives at most 2.565689. The [exactly optimized face enclosure](astra-face-54.md) is smaller still. This fixed-prime window does not establish a positive limiting gap.

The [checker](astra-tail-56-check.py) uses the certified relative-interior pair with both $p=97$ supports and the true zero-floor orbit. It rounds scores with verified error $10^{-6}$. Shifting all scores by that amount bounds the integral error by monotonicity and common translation covariance. HiGHS only proposes nonnegative orbit masses on each rounded tail. The checker rounds those masses to rationals and scales by a certified upper bound on $1,m+2\max_D|\widehat w|,\max_i w_i/q_s$, then takes the better of that packing and the restricted true row at each threshold. This is a feasible lower bound for the all-cycle packing without claiming to optimize it. The comparison full-face upper bound evaluates one true pair. No floating-point optimization tolerance enters the three [receipts](astra-tail-56-checks.jsonl). Replay with `.venv/bin/python -B research/astra-tail-56-check.py`.

1. On the true growing window, test the strengthened disk-and-odd-walk program with odd cutoff $G_0\asymp n^{1/8}$, retaining $E_t/4$. A feasible upper certificate with charged late minimum per step at most $o(1)$ on every prime proves the target. An unbounded prime subsequence with a positive lower bound for its charged minimum rejects this strengthened cover route even with arbitrarily long walks. The larger raw simple-cycle program admits the analogous two-sided test at cutoff $n^{1/4}$.
2. If the cover fails, seek a primal pair in the original full-face quantile LP, independently at each time. A nonpositive limsup for the charged late minimum through all primes suffices. A strictly positive lower bound throughout the late window on an unbounded prime subsequence falsifies this one-time criterion. The fixed-field gap makes this distinction necessary. The all-prime ordinary theta limit remains open.
