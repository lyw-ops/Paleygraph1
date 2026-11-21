# An opposing Legendre unit return on the genuine cold column

Use the same actual fixed centers, both heights, physical mark and lifts as [Round 154](cold-other-center-matched-154.md). The selected inner vertex of \(A_{602}A_{601}\) now takes the pure seed \(d_t(S)\) on the canonical input \(C_1\). Write \(d_t(S)=\sum_{k\ {\rm odd}}a_k C_k\). Select the \(C_2\) coefficient of \(d_t(S)C_1\), namely \(v_2=(a_1+a_3)/2\). The inner output is thus \(v_2K(C_2)=v_2Y+O_{P_{5000}}(n^{-1/2})\).

At the outer vertex take the three distinct true nonseed factors \(\alpha Y,\beta W,\delta G\), or \(\alpha Y,\gamma F_4,\delta G\), in the Taylor expansion about \(S\). This gives \(d_t'''(S)\) in each case since the six orderings of the three factors give a total multiplicity \(3!\), canceling the Taylor factorial. Select the constant coefficient \(q_0\) of \(d_t'''(S)\). The responses are consequently \(\alpha\beta\delta q_0v_2K(Y^2WG)\) and \(\alpha\gamma\delta q_0v_2K(Y^2F_4G)\), with the inherited marked and exact feedback errors. These outer Taylor selections contain true omitted centers, so they occur in \(A_{602}A_{601}-B_3^2\).

As in the [Legendre square decomposition](cold-mixed-seed-column-141.md), the actual two independent Legendre standards give
\[
 Y^2=\tfrac14(S_A+S_B)+\tfrac12AB+\tfrac12 .
\]
The two independent derived factors are also independent of the derived constituents of \(W,F_4,G\), including the rank-five, six and seven constituents of \(G\). The last term in the displayed decomposition returns the exact same two arithmetic rows as Round 154 in both lifts. Collect the following two pairs before taking absolute values:
\[
\begin{array}{c|cc}
 &\text{Round 154 sum}&\text{new selected term}\\
 \hline
 K(WG)&D(\alpha\delta-\beta\gamma)&\tfrac12\alpha\beta\delta q_0v_2\\
 K(F_4G)&D(\beta\delta-\gamma^2)&\tfrac12\alpha\gamma\delta q_0v_2
\end{array}
\]
The other summands of \(Y^2\) have their original coefficients and are outside this comparison. Finite exceptional corrections use \(K(C_2)=Y-2C_1/\sqrt p\) and the same two physical denominator restorations as the [marked mixed calculation](cold-mixed-seed-column-141.md).

For \(d_t(s)=s(4t+s^2)^{-1/2}\) and \(z=s/(2\sqrt t)\), one has \(d_t'''(s)=(-3+12z^2)/((2\sqrt t)^3(1+z^2)^{7/2})\). The [outward replay](cold-legendre-unit-return-155-check.py) encloses \(q_0\) by termwise differentiation of the same seed series as Round 152. In its omitted tail, the consecutive ratio for the positive cubic majorant is at most \((31/29)^3(0.356)^2<0.16\). The other two retained harmonics use the inherited absolute geometric derivative or seed tail. On the complex square the replay shows, for each row in the table, that the merged modulus is strictly between \(0.998\) and \(0.999\) times the Round 154 modulus. Thus the two specific opposing terms give between \(0.001\) and \(0.002\) relative reduction on this column. The same positive weight for the shared field applies to both contributors. [Outward record](cold-legendre-unit-return-155-checks.jsonl)

The selected one-column gains require charging the other outer terms, the other ordering, other harmonics, the genuine Picard residual and all translated input columns before using them against the full \(0.51961239\) budget. The calculation supplies no upper on that full difference.

## The fixed-return choice on other canonical inputs

On \(C_j\) for odd \(j\ge3\), select the same inner \(C_1\) in the two-linear-vertex paths and the same inner \(C_2\) in the new cubic-outer paths. Their common factors use
\[
 D_j=b_0(b_{j-1}+b_{j+1})/2,\qquad v_{j,2}=(a_{j-2}+a_{j+2})/2.
\]
For even \(j\) both selections vanish by parity. They are geometrically small for large \(j\), by the same uniformly convergent seed series. In fact the corresponding merges are constructive on the real slice for every odd \(j\ge3\).

To check this, write \(u=s_n/(2\sqrt t)>0\) on the real slice and set \(C_1=\cos\theta\). The factor \(1+u^2\cos^2\theta\) is \(A(1+r e^{2i\theta})(1+r e^{-2i\theta})\) with \(A>0\) and \(r=(\sqrt{1+u^2}-1)/(\sqrt{1+u^2}+1)<0.032\). The \(2m\)-th Fourier coefficient of its \(-\nu\) power is \((-1)^m h_m^{(\nu)}\) with \(h_m^{(\nu)}>0\). Expanding both binomials, the consecutive terms in \(m\) of each positive summand have ratio at most \(r\max(1,\nu)\). Thus \(h_{m+1}^{(\nu)}<h_m^{(\nu)}\) for \(\nu=1/2,3/2\). The derivative coefficients \(b_{2m}\) have sign \((-1)^m\) and satisfy \(|b_{2m+2}|<|b_{2m}|\) for \(m\ge1\). The seed coefficients are \(a_{2m+1}=u(-1)^m(h_m^{(1/2)}-h_{m+1}^{(1/2)})\).

For \(j=2k+1\), \(k\ge1\), the signs are \((-1)^k\) for \(D_j\) and \((-1)^{k-1}\) for \(v_{j,2}\). The old center sums before multiplication by \(D_j\) are negative on the real slice. The new factors before \(v_{j,2}\) are positive there. Therefore each pair has common sign \((-1)^{k-1}\) on this slice. The fixed-return selection opposes only at \(j=1\) on the nonzero canonical cosine inputs. This calculation leaves families with output shifts depending on the input, as well as noncanonical inputs, open.
