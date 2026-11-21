# The exact bulk support of the ordinary optimal face

Fix one eligible finite prime, one sign \(s\), and its ordinary true optimum \(q_s>0\). Use the normalized inner product and \(U_s,U_{-s}\) of [Round 143](ordinary-terminal-face-dual-143.md). Let \(\mathcal F\) be the primal ordinary optimal face in \(U_s\), and \(\mathcal R\) the complementary ordinary optimal face in \(U_{-s}\). Thus \(F_0=q_s\), \(R_0=n/q_s\), and both have mean one. Put \(I=\{i\ne0:R_i=0\text{ for all }R\in\mathcal R\}\).

Then
\[
 I=\bigcup_{F\in\mathcal F}\{i\ne0:F_i>0\}.
\]
The inclusion from right to left is the ordinary exact complementarity. For the other inclusion, take a bulk coordinate \(j\) vanishing on all of \(\mathcal F\). The polytope of \(F\ge0\), \(F\in U_s\) and \(\mathbb EF=1\) is compact. The primary objective \(\mathbb E(Fe_0)=F_0/n\) has a positive gap to every nonoptimal vertex. Since there are finitely many vertices and all optimal vertices have \(F_j=0\), for some \(\epsilon>0\) the perturbed objective \(\mathbb E(F(e_0+\epsilon e_j))\) has the same maximum \(q_s/n\).

The primal affine equalities on \(F\) have multiplier row in \(U_{-s}\). The perturbed dual therefore attains a row \(Z\in U_{-s}\) with \(Z\ge e_0+\epsilon e_j\) and \(\mathbb EZ=q_s/n\). For every true \(F\) one has \(\mathbb E(FZ)=\mathbb EZ\) by orthogonal sectors, so \(\mathbb E(F(Z-e_0-\epsilon e_j))=0\). Since \(F_0=q_s>0\), this forces \(Z_0=1\). Hence \(R=(n/q_s)Z\) is a true complementary optimizer, with \(R_j\ge (n/q_s)\epsilon>0\). This excludes \(j\) from \(I\).

A finite average gives a single true \(F^\circ\) positive on every point of \(I\). The secondary-dual recession directions \(H\in U_{-s}\) obey \(H\le0\) on \(I\), and their objective is exactly
\[
 \mathbb EH-q_s H_0/n=\tfrac1n\sum_{i\in I}F_i^\circ H_i.
\]
It is nonpositive, with equality exactly when \(H\) vanishes on \(I\). For the original first spill \(s=-\sigma\), so the dual recession row is in \(U_\sigma\). This finite-dimensional argument gives no uniform lower bound on the masses of \(F^\circ\) or an upper on the adaptive signed cost.
