# The whole three-center step and what it omits

Keep the original closed cold square, the true marked \(t_0=n\), both lifts and the translated \(P_{5000}\) class. At the actual centers define
\[
 B_3=K\operatorname{diag}(d_{t_i}(S_i+\alpha Y_i+\beta W_i)).
\]
The [outward replay](cold-three-center-152-check.py) proves the following uniform eventual bounds:
\[
 \|B_3\|<0.6931,\qquad
 \|B_3-B_2\|<0.0635,\qquad
 \|A_{601}-B_3\|<0.4112,\qquad
 \|A_{602}-B_3\|<0.4122 .
\]
The first two include every power of the two nonseed centers in \(B_3\). The last two concern the actual rows, with the remaining centers and true Picard residual retained.

## Signed finite prefix with the exact W envelope

At good Mellin characters use the [Round 150 Jacobi and Legendre collection](cold-signed-legendre-omission-150.md) in every degree \(j\) of the factors besides \(S,\alpha Y\). For \(j=0\), put the signed seed-only Laurent row into the same coefficient table. Let \(\Gamma_j\) be the symmetric positive comparison obtained by taking moduli only after each of those signed collections. For \(B_3\), at degree \(j\) convolve \(\Gamma_j\) with the \(j\)-fold weight measure \(P_W^{*j}\), where
\[
 P_W=|\beta|\left(\delta_0+
          \tfrac34(\delta_{-1}+\delta_1)+\tfrac14(\delta_{-3}+\delta_3)\right).
\]
This is the exact underlying positive weight measure multiplied by the scalar amplitude cap. The four raw standard or dual lists of [Round 55](astra-rankthree-55.md#exact-feedback-and-arithmetic-weights) give it in either physical lift. In particular the folded weight-three mass is \(|\beta|/2\). The inherited Round 136 generic center upper had charged \(3|\beta|/2\) there with its upper amplitude. Taking only \(j\ge1\) gives the exact selection of the terms of \(B_3-B_2\) before any moduli.

For the actual omission, remove the named \(Y,W\) contributions from the inherited positive center row in full, including that older weight-three charge. Let \(H_h\) be the resulting other-center measure plus the retained actual height-\(h\) residual envelope. At each \(j\) precisely the terms with at least one actual other center or residual survive in \(A_h-B_3\). The comparison uses \(\Gamma_j*J_j\), where
\[
 J_0=0,\qquad J_j=(H_h+P_W)*J_{j-1}+H_h*P_W^{*(j-1)} .
\]
As in [Round 149](cold-two-center-omitted-envelope-149.md), the recurrence selects words with a prior other factor or with their first other factor at the newly added position. This preserves the signed seed and Legendre collections. It leaves the internal labels of all \(H_h\) objects positively enveloped.

## Tails, lifts and the new square budget

Retain Taylor orders \(0,\ldots,13\), and price the weight cutoff and omitted tilted residual as in the Round 150 calculation. The analytic tail of \(A_h-B_3\) is covered by the absolute \(0.0000407\) bound of Round 136 because the selected words form a subset. For \(B_3\) and \(B_3-B_2\), the total normalized dimension is bounded by \(v=0.356+(2\cdot0.244+3\cdot0.083)/7.96<1\). Each word of degree \(m\) has first absolute moment at most \(m\) times its dimension. Its translated rate is then at most \(2(m+1)\) times that dimension. Summing the absolute orders from \(\ell=14\) gives the tail charged in the checker. Both base fibers are kept in each weighted comparison. The exceptional and physical root restoration bounds are the inherited \(O_{5000}(n^{-1/2})\) corrections, covered by the strict finite slack. [Saved records](cold-three-center-152-checks.jsonl)

The step bounds give \(\|B_3^2-B_2^2\|<0.085\) and \(\|B_3^2\|<0.48038761\). With the actual height transfer \(0.017\cdot1.048\), it now suffices to obtain
\[
                  \|A_{601}^2-B_3^2\|<0.50179639.
\]
In particular the direct step route would require an omitted bound below \(0.3069\). The current same-row triangle estimate from \(0.4112(1.048+0.6931)\) still exceeds the square budget. The full signed square, nonlinear invariant ball and half-step remain open.
