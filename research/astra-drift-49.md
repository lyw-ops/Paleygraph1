# Matching the full cold history across the exact endpoint support

In the proved marked window there is one symmetric coupling of cyclic indices which sends the **whole true Picard history** to its negative with arbitrarily small empirical RMS error. A different coupling for each time or scalar threshold is unnecessary. For a positive endpoint whose collision is polynomial in the window length, this transfers to its signed secants if the RMS difference of the endpoint densities on the paired indices is small enough. It allows a large common density on each pair. The transfer premise has not been proved through primes.

At prime 173, one coupling of the first six actual states costs less than 1.150, while *every* coupling preserving the exact larger-side endpoint support costs more than 3.404. More than 28 percent of all pairs must cross that support boundary in every coupling as cheap as the displayed one. This is a finite obstruction to imposing that constraint on an empirical matching.

## One arithmetic coupling, uniform over all time pairs

Take the [round-38](vanishing-floor-38.md) window at zero floor. For any fixed exponent $B>0$, increase the absolute subtraction in $D=\lfloor\log_2^*q-\log_2^*\log_2^*q-C_B\rfloor$ as needed. At a cyclic index $i$ put $h_i=(Y_0(i),\ldots,Y_D(i))$, $Y_t=\sqrt n\,v_t$ for the actual zero-start orbit. There is a symmetric probability $P$ on pairs $(i,j)$ with uniform marginals satisfying
\[
 \epsilon(P):=\big(E_P\|h_i+h_j\|_\infty^2\big)^{1/2}
       = O_B(D^{-B}).                                                \tag{1}
\]
It can be supported on a permutation and its inverse. It applies to both eligible primes and square controls. A permutation realizing the cost need not be an involution.

Here are the resource details for (1). Use the negative Mellin approximants $N_t$ from [the signed history proof](astra-completion-40.md), with its requested precision strengthened by four inverse powers of $D$. Their bounded coordinate vectors $N(i)$ satisfy $\|N(i)\|_\infty\le U$ and $(E_i\|N(i)-h_i\|_\infty^2)^{1/2}=O_B(D^{-B-1})$, the latter by summing the squared marginal errors. Enlarge $U$ to dominate $D^{2B+10}$ as well as all input resources. The geometric estimate used below is precisely the earlier mixed **odd-word** estimate at the identity.

For any real one-Lipschitz $f$ in sup norm on the $k=D+1$ dimensional cube, replace it by its odd part $f_o$. Then $f_o(0)=0$ and $|f_o|\le U$. Odd-symmetrized tensor Bernstein approximation to $f_o$ with per-coordinate degree $m=\lceil k U^2/\eta^2\rceil$ has uniform error at most $\eta$: take independent binomial samples and sum the coordinate variances. Choose $\eta=D^{-2B-4}/U$. The weighted coefficient sum at radii $U$ is at most $U2^{km}$, exactly as for the even polynomials in round 40. Here $m$ is polynomial in $U$ and $k\le U$. Expansion in the negative expressions uses only odd words. Including all per-word geometric and coefficient costs, its mean is $O(2^{C U^c}/\sqrt q)$ for absolute fixed $C,c$, by the product estimate of round 30. Division by $U$ in $\eta$ only changes the fixed outer exponent $c$. The same one-extra-level tower accounting as round 40, with its fixed slack exponent reduced if needed, ensures $2^{C U^c}\le q^{1/8}$. It also ensures $U D^{2B+4}q^{-3/8}=o(1)$. Consequently $|E_i[f(N(i))-f(-N(i))]|=O(\eta)$ simultaneously for all such $f$.

Finite Kantorovich duality for distance $\|\cdot\|_\infty$ gives a coupling of $N$ and $-N$ of mean distance $O(\eta)$. Equivalently this is the finite transport LP on the union of their supports, whose dual Lipschitz potentials can be extended to the cube by $f(x)=\min_y(f(y)+\|x-y\|_\infty)$. The squared distance is at most $2U$ times the distance. Lift the coupling to the original index labels by splitting equal atoms uniformly. Minkowski and the two marginal RMS approximations give (1) on the **true** histories. The minimum of squared true cost over the doubly stochastic matrices is attained at a permutation. Symmetrizing such a plan preserves its cost.

## What the matching can transfer to an unrestricted exact face

Let $\rho_i=n\mu_i$ for the actual larger-side endpoint probability of sign $\sigma$, and $r^2=E_i\rho_i^2=1+L$, with $L$ its collision excess. For any coupling with uniform marginals let $b(P)^2=E_P(\rho_i-\rho_j)^2$. For $z_i=\sigma(Y_t(i)-Y_s(i))$ write the exact decomposition
\[
 E_i\rho_i z_i = \tfrac14 E_P[(\rho_i-\rho_j)(z_i-z_j)]
                +\tfrac14 E_P[(\rho_i+\rho_j)(z_i+z_j)].              \tag{2}
\]
By nonexpansiveness $\|z\|_{2,n}\le2\sqrt{t-s}$. Thus the absolute values of the two terms are at most $b(P)\sqrt{t-s}$ and $r\epsilon(P)$, respectively. The second bound improves to $r\epsilon(P)/2$ on a prefix. Neither support cardinality nor a subgroup enters. In particular, if there are plans with
\[
      b(P)=o(\sqrt D),\qquad r\epsilon(P)=o(D),                       \tag{3}
\]
the larger-side mark tends to one. Indeed (2) at $s=0,t=D$ gives $o(D)$; the exact [round-45](endpoint-direction-45.md) identity has $2D(\alpha-1)\le E_i\rho_i\sigma Y_D(i)-E_D/4+\alpha B_D$, with $B_D=o(1)$ and $E_D\ge0$. The other mark follows by complementarity. In particular $r=O(D^c)$ for any fixed $c$ makes the second condition automatic for the arithmetic plans with $B>c$. Small *relative* imbalance alone would not imply the first condition. The finite examples below also show why mere existence of an unweighted low-cost plan supplies no bound on its imbalance.

There is a sharper quantitative inverse inequality for **every** matching. Put $e_T=(E_P|Y_T(i)+Y_T(j)|^2)^{1/2}\le\epsilon(P)$. At $s=0$ the first term of (2) is at most $b(P)\sqrt{E_T}/2$ and the second is at most $r e_T/2$. Completing the square in the exact time identity gives
\[
 b(P)^2+2r e_T \ \ge\ 8T(\alpha-1)+\big(b(P)-\sqrt{E_T}\big)^2
                 +4(A_T+H_T)-4\alpha B_T .                            \tag{3a}
\]
Here $A_T$ is the squared-mean reserve and $H_T$ the actual wrong-sign occupation of the row as in round 44. Thus if $\alpha\ge1+\delta$ and $r e_D=o(D)$, **every** such plan has $\liminf b(P)^2/D\ge8\delta$, even if chosen after observing the exact endpoint. Since $\rho\ge0$, $b(P)^2\le2r^2$; for small matching error (3a) recovers the coefficient four in the full collision bound and also charges the missing energy to differences across paired sites. It makes no assumption on a subgroup or on which density levels carry those differences.

The same bounds apply to the actual raw secant on **every** late interval, and the energy correction always remains $-(E_t-E_s)/4$. To keep an interval with controlled negative correction, fix $0<\delta<1$. Take $s_j=\lfloor D/2^j\rfloor$ down to a fixed index $J$ chosen so $2^{-J}<\delta/8$. At least one interval $[s_j,s_{j-1}]$ has $E_{s_{j-1}}-E_{s_j}\ge-\delta(s_{j-1}-s_j)$ for large $D$. Otherwise telescoping would give $E_D<E_{s_J}-\delta(D-s_J)<0$, since $E_{s_J}\le4s_J$. Every one of these lengths is comparable to $D$ for this fixed tolerance. Under (3), the upper corrected secant per step on the selected interval is at most $\delta/4+o_\delta(1)$. Taking the field limit first and then $\delta\downarrow0$ suffices. This argument provides no nonnegative energy increment on a prescribed half-window.

There is also a conclusion for rows of unrestricted collision. Keep the second term in (2) signed. If $b(P)=o(\sqrt D)$ for a plan of cost $O_B(D^{-B})$ but $\alpha\ge1+\delta$ along a subsequence, then the **weighted matching-error term** at $s=0,t=D$ is at least $(2\delta-o(1))D$. Hence $r\gg_\delta D^{B+1}$ there. The square subfield row with limiting mark $\sqrt2$ must pay in imbalance or in concentrated matching error. The endpoint row is the only part of these implications for which a prime-only estimate is missing.

## A certified incompatibility already at finite primes

Write $S=\{\rho>0\}$, $w=\mathbf1_S-|S|/n$, $s_w=\|w\|_{2,n}$, and take $z=\sigma Y_T$ on a prefix. Apply (2) with $w$ in place of $\rho$. Every plan of cost $e$ obeys
\[
 2|E_i w_i z_i|\le
       \sqrt{P(\mathbf1_S(i)\ne\mathbf1_S(j))}\,\|z\|_{2,n}+s_w e.     \tag{4}
\]
In particular a support-preserving plan costs at least $2|E w z|/s_w$. This is the same as twice the empirical RMS of the conditional mean $E[z\mid\mathbf1_S]$ since $E z=0$. For an interval use $2e$ in place of $e$ in (4). The result allows fractional, randomized, or endpoint-dependent plans.

The [checker](astra-drift-49-check.py) constructs each actual six-step history with 224-bit Arb DFTs. It certifies the prime complementary active systems following round 45, and uses the exact subfield endpoint in square orders. A floating assignment on rounded costs only proposes a permutation. All its indices, cost upper bounds and bounds for arbitrary couplings are then checked with Arb. In the final column the cutoff is the exact rigorous cost upper recorded for each specific proposed permutation, not its rounded display below.

| Field order | Proposed cost upper | Every support-preserving cost exceeds | Crossing probability at proposed budget exceeds |
|---:|---:|---:|---:|
| 101 | 1.457 | 3.301 | .2216 |
| 173 | 1.150 | 3.404 | .2838 |
| 121 (square) | 1.823 | 3.303 | .0389 |
| 961 (square) | 1.213 | 2.410 | .0083 |

The eight [records](astra-drift-49-checks.jsonl) include both prefix and late-half identities. At 173 the actual depth-three to depth-six signed mean is between .08107 and .08108 even though the prefix signed mean exceeds 2.0985. These fixed depths give no prime asymptotic estimate. Replay with `.venv/bin/python -B research/astra-drift-49-check.py`.

1. For the exact larger-side endpoint, minimize $b(P)$ subject to a prescribed history RMS budget. Both squared objectives are linear in the plan. At polynomial collision, a bound $b=o(\sqrt D)$ at the round-49 budget suffices. A positive liminf of the constrained minimum divided by $\sqrt D$ on unbounded primes refutes that budget. Level-set versions of (4) give certified lower bounds for the constrained LP.
2. For higher collision, test the signed second term of (2) on the actual positive row and retain the energy difference on a late interval. Controlling the sum of the two signed terms minus $(E_t-E_s)/4$ to $o(t-s)$ suffices with the round-38 mark. If the imbalance term is already $o(D)$ but every admissible plan has positive order-$D$ weighted error at the prefix on a prime subsequence, the advocated signed-error transfer at that prefix fails even when the empirical costs vanish.
