# A single signed original-block test at a predetermined triangular prefix

For the recurrent bounded trapped alternative of [round 97](astra-prefix-97.md), it suffices to bound **one signed original-block mean** and the original-eroded quotient charge. Both use the predetermined horizon. The first mean uses the identity positional fiber alone. The second test can also use the signed cold states themselves. The estimate includes recurrent trajectories with exponential peaks.

Use the original prime zero-start cold path, the [bounded family](astra-quotient-94.md), its [size and erasure filters](astra-recur-95.md) and the [physical visit inequality](astra-fiber-96.md). Thus $p\equiv1\bmod4$, $G=\widehat Q$, $n=(p-1)/2$, $J=\lfloor D(p)/8\rfloor$, $L=K\cup C$ is the subgroup containing the recurrent candidate $C$, $m=|L|\asymp\sqrt n$, $m/|C|\le2$, $B=L^\perp$, and $\sigma$ is the companion sign. Write $\lambda=\sum_{i\in L}\mathsf K_{0i}$, so $|\lambda|\le\kappa_*<1$ throughout the qualified list. Let $q$ be any genuine real nonnegative probability constant on every $L$-coset with $\mathsf Kq=\sigma(q-\mathbf1/n)$ and $w=q(L)\ge w_*>0$, using the same prescribed root floor as in round 97. Lifting a restricted optimizer supplies such a row on the filtered family.

Put $W_j=|Y_j|$, where $Y_0=0$, $Y_{j+1}=\mathsf K W_j+\beta_j\sqrt n\,\mathsf K e_0$, and $2g_j=(\sum W_j+\beta_j\sqrt n)/n$. For $J\ge2$ set
\[
 \omega_j=\frac{2(J-1-j)}{J(J-1)}\quad(0\le j<J),\qquad
 U_\omega=\sum_{j<J}\omega_j1_{(L\cup A_j)^c} W_j,\qquad
 U_J=J^{-1}\sum_{j<J}1_{(L\cup A_j)^c}W_j .
\]
The two inputs may even use different permitted sets $A_j\subset L^c$ of size at most $H_p^2$ at each time, under the original round-95 growth condition.

If a fraction $\alpha>0$ of $C$ belongs to the genuine negative masks at at least $b_0J$ of the admitted good terminal times per site, then for all sufficiently large eligible primes on this branch
\[
 \boxed{\quad
  \sigma\mathbb E_L\mathsf K U_\omega+
  \frac{2}{J-1}\inf_q\frac{\langle q,U_J\rangle}{q(L)}
                        \ \ge\ cJ.\quad}                                      \tag{1}
\]
Here $c>0$ depends on the fixed pin and recurrence parameters. Thus a one-sided $o(J)$ upper for this one signed triangular transform, together with one qualified trial row of original-exterior charge $o(J^2)$, excludes this recurrent obstruction. The time weights are fixed in advance. Each candidate on the prefiltered list specifies its own output block and positional fiber; the recurrent member can depend on the observed masks. The transform needs no spatial absolute values. Upper bounds for the two terms uniform on the filtered bounded list exclude positive trapped mass at one admitted pin by the inherited selector. The finite-power escaped branch remains open.

## Exact signed transfer

For each time write
\[
 a_j=\mathbb E_L W_j,\quad z_j=\sigma\mathbb E_LY_j,\quad
 e_j=\langle q,1_{L^c}W_j\rangle,\quad
 d_j=\sigma\langle q,1_{L^c}Y_j\rangle,\quad
 f_j=\sigma\mathbb E_L\mathsf K(1_{L^c}W_j).
\]
The actual marked source is kept explicitly. The quotient eigenrelation gives
\[
 wz_{j+1}+d_{j+1}=w a_j+e_j+\beta_j\sqrt n\, w/m-2g_j.
\]
The constant internal column sum on $L$ gives
$z_{j+1}=\sigma\lambda a_j+f_j+\sigma\beta_j\sqrt n\lambda/m$.
Subtracting yields the exact identity
\[
 w f_j=w(1-\sigma\lambda)(a_j+\beta_j\sqrt n/m)
                      +e_j-d_{j+1}-2g_j .                                    \tag{2}
\]
Since $d_j\le e_j$ and $e_0=0$, summation by parts gives
\[
 \sum_{j<J}\omega_j(e_j-d_{j+1})\ge
 \sum_{j<J}\omega_j(e_j-e_{j+1})
 =-\frac{2}{J(J-1)}\sum_{j<J} e_j .
\]
In particular the last nonzero time weight is on $j=J-2$. Positivity of the marked term follows from $1-\sigma\lambda\ge1-\kappa_*$. The zero-start energy estimate $\sum_{j<J}g_j\le J$ gives $2\sum\omega_jg_j\le4$. This proves the finite un-erased bound
\[
 \sum_{j<J}\omega_j f_j +\frac{2}{w(J-1)}\frac1J\sum_{j<J}e_j
 \ge (1-\sigma\lambda)\sum_{j<J}\omega_j a_j-4/w .                           \tag{3}
\]
For every allowed erasure the round-95 estimate bounds the removed first norm by $H_p^2 U+H_p\sqrt n\,e=o(\sqrt n)$. Each transformed coordinate changes by $o(1)$ using $\|\mathsf K\|_{\max}\le\sqrt p/n$. The charge against any qualified quotient law changes by $o(1)$ using $\|q\|_\infty\le1/m$. Hence (3) transfers uniformly to both independently eroded inputs.

To lower-bound its right side, discard terminal times $T>(1-b_0/4)J$. At most $b_0J/4+1$ visits per recurrent site are discarded. Every retained visit has $H_T(i)=W_{T-1}(i)+W_T(i)+W_{T+1}(i)\gg J$ by [round 96, (3)](astra-fiber-96.md), off the physical mark. For sufficiently large $J$ each of the three time weights is at least $c_{b_0}/J$. A site-time amplitude enters at most three such visits. Therefore $\sum_j\omega_j W_j(i)\gg J$ at each recurrent site. Their density on $L$ is at least $\alpha/2$ up to omission of the single marked point, proving $\sum_j\omega_j a_j\gg J$. This elementary step needs neither a common terminal time nor a sign assumption on those large amplitudes. Taking the infimum in (3) proves (1).

In counting Fourier convention $\mathbb E_L\mathsf K U_\omega=n^{-1}\sum_{z\in B}s(z)\widehat U_\omega(z)$, whereas $\sum_{z\in B}\widehat U_\omega(z)=0$ by eroding $L$. Subtracting $\sigma$ gives the exact one-sign formula
\[
 \sigma\mathbb E_L\mathsf K U_\omega
 =-\frac2n\sum_{z\in B:\,s(z)=-\sigma}\widehat U_\omega(z)
   -\frac1n\widehat U_\omega(1).
\]
The last mean lies in $[0,4]$ by the same energy estimate. The opposite positional sign sum is real because the input is real and the sign class is inversion symmetric, even for asymmetric erasures. A sufficiently negative signed sum on this single identity fiber is the obstruction in the first term of (1).

## The quadratic test can also retain exterior sign cancellation

Define $V_J=J^{-1}\sum_{j<J}1_{(L\cup A_j)^c}Y_j$, using the actual signed states. For the un-erased exterior, summing (2) gives a second exact expression,
\[
 \sum_{j<J}\omega_j(e_j-d_{j+1})
    =\sum_{j<J}\omega_j(e_j-d_j)
       -\frac{2}{J-1}\frac1J\sum_{j<J}d_j .
\]
This follows by differencing the same linear weights, using $d_0=0$. The first sum is nonnegative; it equals twice the triangular average of the exterior occupation of $(-\sigma Y_j)_+$ against $q$. Consequently the stronger recurrent estimate is
\[
  \sigma\mathbb E_L\mathsf K U_\omega+
  \frac{2}{J-1}\inf_q\frac{\sigma\langle q,V_J\rangle}{q(L)}
                   \ \ge\ cJ .                                               \tag{4}
\]
The absolute value of the change under erasure of signed states is bounded by the removed unsigned first norm already estimated. The signed charge is linear in $q$ and can be computed using only $\widehat V_J$ on the identity and the $\sigma$ part of $B$, since $\widehat q$ has that support. Thus a one-sided $o(J^2)$ trial bound on this signed charge suffices alongside the one-sided triangular upper, even if the unsigned exterior charge of the trial row is large. Inequality (1) follows from (4) by positivity.

## Finite physical replay and next estimates

The [checker](astra-quotient-98-check.py) uses the genuine $p=769$ path, $|L|=8$, $J=16$, and the six-point allowed clique of round 97 supplying a positive quotient law of exact block root $1/8$. It checks (2) at each update, (3), the signed refinement (4) through its exact Abel identity, both signed Fourier formulas, and the exact changes on two independently chosen one-site exterior erasures at each time. The [saved record](astra-quotient-98-checks.jsonl) tests the finite identities without assuming asymptotic recurrence at this field.

For that exact clique row the eroded signed triangular mean lies in $[0.259599450,0.259599451]$. The eroded flat quotient charge lies in $[1.496416831,1.496416832]$ with unsigned states and $[0.345602443,0.345602444]$ with signed states. Over every qualified quotient probability with root at least $1/8$, the minimum of the **unnormalized-by-root signed charge** lies in $[0.277985927,0.277985932]$. The single-site erasures break inversion symmetry, so the program retains the permitted sine and cosine coefficients. A tightened rounded primal candidate certifies positivity and the actual root constraint. Rounded nonnegative dual multipliers certify the lower bound after charging all coefficient residuals against the unit Fourier cap. These bounds concern the fixed prime and horizon.

1. Estimate the one-sided opposite-sign sum for the triangular original exterior on the filtered list. A lower bound $-o(nJ)$ suffices. Only one signed sum per original subgroup is needed.
2. Try the one-sided signed original-eroded flat-prefix charge (4) with the actual prescribed root floor. No through-primes $o(J^2)$ trial upper or $o(J)$ signed triangular upper has been obtained here.
