# Unequal activation rates and a weighted time-block bound

The actual bulk secant ratios can be used separately, with the marked secants and the true mean losses retained. For a longer block, a two-state weighted potential captures which favorable times force contraction. A positive density greater than one half suffices. Isolated favorable times can be hidden in the marked component in a linear increment model, even with the actual Paley reflection.

Use the [Round 26 increment notation](parallel-activation-26.md). Write

$$D_{t+1}=K H_t,\qquad H_{t,i}=d_{t,i}D_{t,i},\qquad
E_t=\|D_t\|_2^2,\quad M_t=\frac{(\sum_iH_{t,i})^2}{n}.$$

Let \(a_t=d_{t,0}^2\) and suppose \(\|(H_t)_B\|_2^2\le\rho_t\|(D_t)_B\|_2^2\), where \(B\) omits the mark and \(0\le a_t,\rho_t\le1\). The bulk ratio can be its exact measured value, the harmonic upper bound, or another proved upper bound. The results concern exact inequalities on an actual orbit when those inputs are established.

## A two-step comparison with unequal rates

Put \(a=a_t\), \(b=a_{t+1}\), \(R=\rho_t\), \(S=\rho_{t+1}\), \(k=1/n\), and \(r^2=1-1/n-1/n^2\). Define

$$C=\begin{pmatrix}
a[S+(b-S)k^2]&|b-S|kr\sqrt{aR}\\
|b-S|kr\sqrt{aR}&R[S+(b-S)r^2]
\end{pmatrix},\qquad
Q(a,b,R,S)=\max\{RS,\lambda_{\max}(C)\}.$$

Then

$$E_{t+2}\le Q(a,b,R,S)E_t-SM_t-M_{t+1}.$$

The matrix trace and determinant are

$$\operatorname{Tr}C=S(a+R)+(b-S)(ak^2+Rr^2),$$
$$\det C=aRS\,[S+(b-S)(k^2+r^2)].$$

If \(b\ge S\), the maximum with \(RS\) is redundant. To prove the estimate, first use

$$E_{t+2}\le S E_{t+1}+(b-S)|(KH_t)_0|^2-M_{t+1}.$$

When \(b\ge S\), bound the root by \(k|H_{t,0}|+r\|(H_t)_B\|\). This gives the stated matrix, and \(E_{t+1}=\|H_t\|^2-M_t\) supplies the first mean reserve. When \(b<S\), use instead

$$|(KH_t)_0|\ge(k|H_{t,0}|-r\|(H_t)_B\|)_+.$$

For fixed root input the resulting upper expression increases with the bulk norm, so insert \(\sqrt R\|(D_t)_B\|\). In the region where the positive part is active it is the quadratic with matrix \(C\). In the complementary region it is \(S(a p^2+R q^2)\), for \(p=|D_{t,0}|\), \(q=\|(D_t)_B\|\). If \(a\le R\), this is at most \(RS(p^2+q^2)\). If \(a>R\), its maximum on that region occurs on the common boundary and is bounded by \(\lambda_{\max}(C)\). This proves the general formula.

In the field limit,

$$Q(a,b,R,S)\longrightarrow\max\{aS,Rb,RS\}.$$

For unrestricted root secants \(a=b=1\), the limit is \(\max\{R,S\}\). One favorable bulk step out of a pair therefore gives no field-independent two-step contraction from these data alone.

## A time-block estimate using the exact mean reserve

The following stronger structure is specific to the Paley marked diagonal. If \(K_{00}=-1/n\), let \(O=K+J\). Then \(O\) is an orthogonal reflection and \(O_{00}=0\). For the opposite mask use \(O=K-J\) instead. Thus, for either mask,

$$K=O\mp J,\qquad O^2=I,\qquad O_{00}=0.$$

Choose a fixed lower floor \(0<\rho_*\le1\), put \(\bar\rho_t=\max(\rho_t,\rho_*)\) and \(L=1/\rho_*\). Choose \(0\le\theta<1\) such that \((1-\theta)n+1>L\), and define

$$\Gamma=1+\frac{(L-1)^2}{(1-\theta)n+1-L}.$$

For a block of \(T\) steps define backward weights by

$$u_T=v_T=1,\qquad
u_t=a_t v_{t+1},\qquad
v_t=\bar\rho_t\max(u_{t+1},v_{t+1}).$$

Then

$$\boxed{
E_T\le\Gamma^T\max(u_0,v_0)E_0
-\theta\sum_{t=0}^{T-1}\Gamma^{T-1-t}v_{t+1}M_t.}$$

In particular \(\rho_*=1/2\), \(\theta=1/2\), \(n>2\) gives \(\Gamma=n/(n-2)\). For a polylogarithmic horizon the inflation \(\Gamma^T\) tends to one.

Here is a direct proof. For future weights \(u,v\) with \(v>0\), let \(H=(h_0,h_B)\), \(m=n^{-1}\sum H_i\), and \(z=(OH)_0\). Then \(|z|\le\|h_B\|\), and

$$u|(KH)_0|^2+v\|(KH)_B\|^2
=v\|H\|^2-vnm^2+(u-v)(z\mp m)^2.$$

If \(u\le v\), dropping the last term gives the desired bound with the full mean reserve. If \(u>v\), retain \(\theta vnm^2\) and complete the square in the remaining \(m\). The result is bounded by

$$v h_0^2+
\left[u+\frac{(u-v)^2}{(1-\theta)vn-(u-v)}\right]\|h_B\|^2
-\theta vM.$$

For \(1<u/v\le L\), the bracket is at most \(\Gamma u\). The backward recursion ensures \(u_t/v_t\le L\), since \(a_t\le1\) and \(\bar\rho_t\ge\rho_*\). Therefore

$$u_{t+1}D_{t+1,0}^2+v_{t+1}\|(D_{t+1})_B\|^2
\le\Gamma[u_tD_{t,0}^2+v_t\|(D_t)_B\|^2]
-\theta v_{t+1}M_t.$$

Iteration proves the block estimate. The same proof applies to every time interval, with fresh terminal weights.

## Which favorable time patterns suffice

Set \(a_t=1\) if no marked secant information is used. Let

$$\ell_t=-\log\bar\rho_t.$$

Then \(-\log\max(u_0,v_0)\) is exactly the minimum weighted vertex-cover cost of the time path \(0,\ldots,T-1\), with vertex weight \(\ell_t\). Equivalently, label each time root or bulk, forbid two consecutive root labels, pay zero at a root label and \(\ell_t\) at a bulk label, and minimize the total cost. This follows directly from the two-state recursion. With actual \(a_t\), the root label additionally pays \(-\log a_t\).

If at least \(G_T\) times have \(\rho_t\le\rho_{\rm good}<1\), put \(\ell_{\rm good}=-\log\max(\rho_{\rm good},\rho_*)>0\). Every cover contains at least \(G_T-\lceil T/2\rceil\) of these times. Dropping the nonnegative mean improvement gives

$$\frac{E_T}{E_0}\le
\exp\left(T\log\Gamma-
\ell_{\rm good}[G_T-\lceil T/2\rceil]_+\right).$$

Thus a uniformly favorable fraction greater than one half supplies geometric decay for \(T=o(n)\). For example, if \(G_T\ge(1/2+\epsilon)T\) on the needed prefixes, a horizon of order \(\log q\) can reach the critical residual scale, with a sufficiently large constant. A weighted cover cost growing faster than \(T\log\Gamma\) is the more precise general condition. Positive density alone, with no time-pattern condition, is insufficient.

## Exact alternating counterexample to an aggregate-rate implication

Use the actual Paley \(K\), and let

$$e=e_0-\mathbf1/n,\qquad h=Ke_0,\qquad
\gamma=1-\frac{1-\sqrt\rho}{n},\quad 0<\rho<1.$$

They have equal squared norm \(1-1/n\), and \(Kh=e\). At even times use the diagonal multiplier with root entry one and bulk entries \(\sqrt\rho\). At odd times use the identity multiplier. The resulting linear increment recursion satisfies exactly

$$D_{2j}=\gamma^j e,\qquad
D_{2j+1}=\gamma^{j+1}h,\qquad
\frac{E_{2j}}{E_0}=\gamma^{2j}.$$

The bulk ratio is favorable at one half of all times. Nevertheless, for \(j=O(\log q)\) this energy ratio tends to one. The root secants remain at their worst permitted value, and the favorable times are isolated. The weighted cover cost is zero, in agreement with the block theorem.

This is a linear increment example with prescribed diagonal contractions. It uses the actual coherent Paley reflection, but it is not asserted to be a trajectory of the heterogeneous square-root activation. It proves that an implication using only the frequency of favorable bulk ratios and the general secant bounds cannot supply the missing actual-orbit theorem.

## Replay

The [script](parallel-rate-27.py) checks unequal-rate two-step bounds, the weighted block inequality with its retained mean losses, and the weighted vertex-cover recursion. It also replays the alternating example. The [records](parallel-rate-27.jsonl) are floating-point checks of the displayed formulas.

```sh
.venv/bin/python -B research/parallel-rate-27.py > research/parallel-rate-27.jsonl
```

The [independent actual-orbit audit](parallel-rate-27-orbit-audit.py) constructs
the \(q=61\) operator by direct cosine sums at 192-bit precision and uses dense
matrix multiplication for 16 actual Picard steps. It checks every bulk loss,
root secant, mean-reserve and full-ratio enclosure from the FFT certificate,
then checks all four final residual upper bounds. The [17 Arb records](parallel-rate-27-orbit-audit.jsonl)
reproduce byte for byte on rerun. They certify this finite prefix independently
of the rational trial trajectories used by the FFT calculation.

```sh
.venv/bin/python -B research/parallel-rate-27-orbit-audit.py > research/parallel-rate-27-orbit-audit.jsonl
```
