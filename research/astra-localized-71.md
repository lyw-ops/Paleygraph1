# Translated opposite-face budgets for the exact window defects

Use the exact round-70 frequency-of-defect profile $F=F_{s,u}$, extended by zero at the root. Write $q,r$ for optimal probabilities on the tested and opposite sides and $z_i=q_i/q_0$, $w_i=r_i/r_0$. All coordinates lie in $[0,1]$ by the point caps. Reciprocity gives $nq_0r_0=1$. Use the actual full tested-face support $I$, or any certified superset of it. Put $T=I\setminus\{0\}$ and $\gamma=\sqrt n q_0$. The requested collision is $\gamma^2\sum_T F_i z_i^2$.

Every translated opposite row gives the **exact bulk budget**
\[
 \sum_{i\in T} z_i w_{i-h}=1-w_{-h}.
\]
Indeed opposite mean-zero sectors remain orthogonal under every translation, and their constant modes alone give $\sum_i q_i r_{i-h}=1/n$. In particular a unit cap translate costs zero and excludes its positive translated support from the bulk. These statements hold for every choice on either face; the translated witness need not itself be primary at zero.

Square each budget and discard its nonnegative cross terms. A certificate consisting of any prices $c_h\ge0$ such that $\sum_h c_h w_{i-h}^2\ge F_i$ for every $i\in T$ gives
\[
 n\sum_{i\ne0}q_i^2 F_i\le\gamma^2\sum_h c_h(1-w_{-h})^2.
\]
This tests the requested squared pairing on every true optimizer on the tested face, using just *one* opposite optimizer. It holds with $F$ replaced by an individual window indicator. One can combine several opposite optimizers by pricing their translates separately. The standard finite LP dual maximizes $\sum_T F_i t_i$ over $t_i\ge0$ subject to $\sum_T t_i w_{i-h}^2\le(1-w_{-h})^2$ for every translate. In particular the relaxation's failure witnesses are not necessarily feasible probabilities. Free translates may be applied first to certify zeros.

## A quantitative restriction on which translations can pay

Fix $0<\kappa<1$ and put $N_\kappa=\{h:w_{-h}>1-\kappa\}$. Define the uncovered sites
\[
 T_\kappa=\{i\in T:w_{i-h}=0\text{ for all }h\in N_\kappa\}.
\]
Every certificate above costs at least
\[
 \sum_h c_h(1-w_{-h})^2\ \ge \frac{\kappa^2\sum_{i\in T_\kappa} F_i}{\sum_j w_j^2}
 \ \ge\ \kappa^2 r_0\sum_{i\in T_\kappa} F_i.
\]
Sum the covering inequalities over the uncovered sites; the remaining translates cover at most $\sum_jw_j^2$ per unit price and cost at least $\kappa^2$. The last inequality uses $w_j^2\le w_j$ and $\sum_j w_j=1/r_0$. Equivalently a constant dual vector on $T_\kappa$ with value $\kappa^2/\sum_j w_j^2$ is feasible. The Jacobi bracket gives $r_0\asymp1/\sqrt n$. Hence any fixed-$\kappa$ uncovered defect weight $\gtrsim d\sqrt n$ already rules out an $o(d)$ certificate of this type for that witness. Testing only translates a fixed distance below the cap requires $\sum_T F_i=o(d\sqrt n)$ in advance. This requirement concerns exact incidence with the tested support; round 70's counting bound alone is $O_u(n/d)$.

On square fields use the true larger optimum uniform on the subfield annihilator $A$; then $z=1_A$, so the collision equals $\gamma^2\sum_{A\setminus\{0\}}F_i$ for *any* exact profiles. The vector $t=1_{A\setminus\{0\}}$ is feasible in the cover dual with the true support or any superset, for every opposite optimum and even for several at once. On any window satisfying the round-70 marked, mean and RMS hypotheses with the fixed square gap, (5) forces the corresponding cover cost to be of order at least $d$. This last conclusion is conditional on those window hypotheses at square order; the dual witness itself is unconditional.

## Ranked next tests

1. On the exact primary support count the uncovered defect weight for the best available opposite witness across near-cap thresholds. The explicit dual lower bound rejects a witness without fitting any prices. For surviving witnesses, solve the cover on the exact window-frequency profile and seek prime-uniform cost $o(d)$.
2. Positive mixtures and mixed products of positive-cost translated budgets cannot improve the diagonal cover: divide each mask by its own cost $1-w_{-h}$, then $ab\le(a^2+b^2)/2$ pointwise, and Jensen handles squared convex mixtures. Instead test signed combinations $v_i=\sum_h a_h w_{i-h}$ that are nonnegative on $T$ even though some $a_h<0$. Their exact bulk price is $b=\sum_h a_h(1-w_{-h})=\sum_T z_i v_i\ge0$, and $v_i^2$ can be used at cost $b^2$. Cancellation in the price survives this support-specific positivity test. No prime-uniform $o(d)$ upper has been proved; ETH26 remains open.
