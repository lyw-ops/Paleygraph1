# Exact secondary face dual for the actual terminal statistic

This Round 143 derivation was checked by a separate mathematical auditor. Fix the actual marked orbit and the sign \(s\) of the ordinary optimizer \(F\) used in the terminal test. Let \(V_s\) be the mean-zero \(s\)-eigenspace of \(K\), and \(U_s=\mathbb R\mathbf1\oplus V_s\). Thus \(KF=s(F-\mathbf1)\). The two ordinary faces have root values \(q_s q_{-s}=n\). Use normalized expectation throughout.

For a real bulk cost \(w\), put \(w_0=0\) and
\[
 L(w)=\min\{\mathbb E(Fw): F\ge0,\ \mathbb EF=1,\ F\in U_s,\ F_0=q_s\}.
\]
The two actual costs of interest are \(w_i=G_i\) and \(w_i=(KH^\circ)_i^2\) on the bulk, with \(G=\sqrt n\,g_T\), \(H^\circ=1_{\{j\ne0\}}\sqrt n\,g_{T-1}\), and \(T+1\) inside the simultaneous marked window. Round 142 gives \(L((KH^\circ)^2)=\min_F\mathscr D_{F,T}+O_\tau(T)\) when the cost is set to zero at the root.

Let \(\mathcal R\) be the full ordinary optimal face on sign \(-s\) and define
\[
 I=\{i\ne0:R_i=0\ \text{for every }R\in\mathcal R\}.
\]
Then
\[
 L(w)=\max\left\{\mathbb EZ-\frac{q_s}{n}Z_0:
                    Z\in U_{-s},\ Z_i\le w_i\ \text{for }i\in I\right\}.       \tag{1}
\]
To see this, first use linear programming duality in the full ambient nonnegative cone. Dual variables in \(U_{-s}\) encode the mean and the \(V_{-s}\) projection constraints. The root multiplier \(\beta\) gives the objective \(\mathbb EZ+\beta q_s/n\) under \(Z+\beta e_0\le w\). Since \(q_s>0\) its largest permitted value is \(-Z_0\). Primal compactness and feasibility give finite attained optima. This proves (1) initially with inequalities on the whole bulk.

For every pair of true opposite optima \(\mathbb E(FR)=1=F_0R_0/n\) by orthogonal sectors and root reciprocity, so \(F_i=0\) for every bulk \(i\notin I\). There exists a true \(R^\circ\) positive on that complement: take a finite average of optimizers witnessing positivity at the individual sites. Subtracting a sufficiently large nonnegative multiple of \(R^\circ\) from any \(Z\) leaves the dual objective unchanged and enforces all omitted inequalities. This proves (1) on \(I\), even if some indices of \(I\) are absent from the support of every \(F\).

Consequently only dual minorants on the common zero set of the other true optimal face can obstruct selection of a low-cost terminal row. For the quadratic test, a target is an upper \(o(T^2)\) on the displayed signed mean-minus-mark functional with \(w=(KH^\circ)^2\) on \(I\). The first moment asks for \(o(T)\) with \(w=G\). Equation (1) is exact for both costs and is independent of arithmetic. It supplies no prime-uniform upper on either functional.
