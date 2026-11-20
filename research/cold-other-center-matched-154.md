# Selected omitted centers with the same signed return

Work on the original closed cold square at the actual heights \(601,602\), with both lifts, physical mark \(t_0=n\), and the inherited \(P_{5000}\) price. In the true fixed center \(S+\alpha Y+\beta W+\gamma F_4+\delta G+\cdots\), the coefficients are shared at both heights. Use the actual retuned coefficients of [Round 62](astra-primitive-62-check.py), with \(\gamma=(499/500)\beta\,\mathrm{groups}[1,1]_{0,0}\) and \(\delta=-2\gamma\,\mathrm{linear\_scalar}(\mathrm{groups},\beta)\). Here \(F_4,G\) have the signs of [Round 151](cold-leading-W-square-151.md).

For \(X\in\{Y,W,F_4,G\}\), write \(T_X=K\operatorname{diag}(X_i d'_{t_i}(S_i))\). This is the linear Taylor term in that center about the genuine seed, with its \(\alpha,\beta,\gamma,\delta\) outside \(T_X\). Select one nonseed center per vertex, with at least one of \(\gamma F_4\) and \(\delta G\), in \(A_{602}A_{601}-B_3^2\) from [Round 153](cold-three-center-composition-153.md). On the canonical input \(C_1\), select the outer constant of \(d'_t(S)=\sum_{k\ {\rm even}}b_k C_k\) and the inner \(C_1\) coefficient in \(d'_t(S)C_1\). These give the exact all-order coefficient \(D=b_0(b_0+b_2/2)\) for the selected harmonics.

The inherited feedbacks \(K(C_1Y)=W\), \(K(C_1W)=F_4\) and \(K(C_1F_4)=-G\), each up to its bounded priced exceptional term, give the following selected expressions. The equality is for the selected harmonics, with \(O_{P_{5000}}(n^{-1/2})\) after restoring the exceptional terms and both physical denominators as in Round 151.
\[
\begin{array}{c|l}
\text{coefficient of the two linear vertices}&\text{selected expression}\\
\hline
\alpha\delta & \alpha\delta D\,K\big(YK(GC_1)+GW\big)\\
\beta\gamma & \beta\gamma D\,K\big(-WG+F_4^2\big)\\
\beta\delta & \beta\delta D\,K\big(WK(GC_1)+GF_4\big)\\
\gamma^2 & -\gamma^2D\,K(F_4G)
\end{array}
\]
The rows for distinct centers contain both orders. There is one order for \(F_4\) at both vertices. Thus the two repeated fields have coefficients \(D(\alpha\delta-\beta\gamma)\) on \(K(WG)\) and \(D(\beta\delta-\gamma^2)\) on \(K(F_4G)\). Other terms could also contribute to these arithmetic rows.

On the real slice each merge is exactly constructive. On the complex square [the outward replay](cold-other-center-matched-154-check.py) shows the four signed summands \(z\) all satisfy \(\Re z<0\) and \(|\Im z|<5\cdot10^{-6}(-\Re z)\). Consequently the merged modulus is at least \((1+(5\cdot10^{-6})^2)^{-1/2}\) times the separate moduli, including their common nonzero factor \(D\). The relative saving from either merge is less than \(1.25\cdot10^{-11}\). The seed binomial series through order \(13\), with the absolute geometric derivative tail as in [Round 152](cold-W-all-order-return-152.md), also gives \(|4tD|<0.86\). This last reduction compares the all-order \(D\) to its leading value \(1/(4t)\).

For these two merged fields the symmetric product measures of \(W,G\) and \(F_4,G\) give the positive canonical price by summing each nonzero weight against \(\pi\), as in Round 151. The outward strict bound is \(0.014\) for the sum of their two priced moduli, with eventual margin for the finite-prime feedback and physical mark corrections. [Saved replay record](cold-other-center-matched-154-checks.jsonl)

This calculation covers two actual omitted-center fields on one input. The other selected expressions, higher nonseed degree, remaining harmonics, true Picard residual and translated input columns are separate terms in the full operator. The merges give no uniform strict debit for the direct \(0.51961239\) budget. The common complex domain still needs a full signed estimate or a different confinement proof.
