# Disjoint rank-three merges in the translated two-height comparison

Use the exact physical heights \(601,602\), common complex square, mark \(t_0=n\), both lifts and the translated \(P_{5000}\) class from [Round 156](cold-rank-three-unit-composition-156.md). In the finite prefix of [Round 153](cold-three-center-composition-153.md), expand about \(S+\alpha Y\), keeping \(W\) and the entire actual other displacement \(H_h\) as separate indeterminates. Here \(A_h\) uses \(S+\alpha Y+\beta W+H_h\). The signed \(\Gamma_d(\lambda)\) tables of the prefix have one coefficient for each full Jacobi Laurent and Legendre label \(\lambda=(k,a,b)\). Their pre-modulus coefficients in \(H_h^j W^l\) at label \(\lambda\) are
\[
 \binom{j+l}{l}\beta^l\Gamma_{j+l}(\lambda).
\]
Degree \(j=0\) gives \(B_3\), and degree \(j>0\) gives \(E_h=A_h-B_3\). This uses the actual unknown \(H_h\) before applying its original positive measure.

## Two disjoint merges at each common label

The [rank-three decomposition](astra-rankthree-55.md#collecting-signed-rank-three-characters) contains an arithmetic unit of weight \(1/4\) in \(W^2\). In \(W^3\) it contains the selected common-standard part \((3/4)W\). For the latter, each of the four normalized standard or dual constituents has coefficient \(1/4\) in \(W\) and a selected coefficient \(3/16\) in \(W^3\). This is the sum of the twelve copies listed there, each weighted \(1/64\), without including the shifted exterior-square sector.

For any \(j\) and common full label at the two respective degrees, merge the following portions before taking absolute values:
\[
\begin{aligned}
 H_h^j:\quad&
 \Gamma_j+\tfrac14\binom{j+2}{2}\beta^2\Gamma_{j+2},\\
 H_h^j W:\quad&
 (j+1)\beta\Gamma_{j+1}
       +\tfrac34\binom{j+3}{3}\beta^3\Gamma_{j+3}.
\end{aligned}
\]
These use disjoint \(W\)-degree pairs \(0,2\) and \(1,3\) at fixed \(H_h\)-degree. For different \(j\), the original polynomial comparison allocated disjoint slots. The remaining nonunit and nonstandard parts keep their old positive charges. Equality is at the multiplier stage for every inner row. The complete label lists are symmetric under exchange of the two Legendre standards and the two Jacobi exponent signs, so the same folded debit is valid for both physical lifts.

## Full outward recomposition and the remaining positive obstruction

The [outward checker](cold-rank-three-common-labels-157-check.py) reconstructs the finite R153 signed tables. At each matching label it uses the lower endpoint of the old separate cap charge minus the new outward merged modulus, whenever this is positive. The saving can include both arithmetic cancellation and tighter amplitude evaluation. Each chosen debit is multiplied by the same inherited positive \(H_h^j\) comparison used originally, and by the exact \(W\) measure for the second merge. If a coefficient falls outside the retained row it receives no debit. The original tail, residual leak, loss rates and both physical repairs are preserved. This verifies the new eventual bound
\[
       \|A_{602}A_{601}-B_3^2\|_{P_{5000}}<0.66365735
\]
on the full original translated class. [Saved result](cold-rank-three-common-labels-157-checks.jsonl)

The fixed twelve-weight trial in Round 153 still gives a componentwise lower factor above \(0.61729\) for the enriched retained positive comparison. A coordinatewise monotone homogeneous price on that comparison alone cannot reach \(0.51961239\). The lower factor concerns the chosen positive map. The full signed derivative estimate and common complex domain remain open.
