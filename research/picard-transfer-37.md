# When an exact Picard average inherits the stationary mark

Round 37. For the actual zero-start Paley Picard orbit, the raw marked
Cesaro error relative to stationarity is $O_\tau(\sqrt n/T)$ in mean
square. The estimate also controls the proposed mean and the two raw
projected marks. Beyond the square-root scale, a proof of vanishing
averaged marks therefore has to control the actual stationary mark.
A separate stopping rule gives an **unrepaired** positive prefix of
length $O_\tau(n)$ while preserving the round-35 budget. Both arguments
work over eligible squares too.

## 1. Relative energy and the marked coordinate

Use the notation of [round 35](averaged-mark-35.md). Write $q=2n+1$,
$c=\tau/n\in(0,1)$, $w_0=1$, $w_i=c$ otherwise, and
$W=\sum_i w_i$. Let $v_{t+1}=K\Phi(v_t)$ from $v_0=0$, where
$\Phi_i(x)=\sqrt{x_i^2+4w_i}$.
Put $s_t=\sum_i\Phi_i(v_t)/(2\sqrt n)=\sqrt n\mu_t$.
The positive stationary pair $A_+^*,A_-^*$ has common mean
$a=\sqrt{W/n}$, product $w$, and difference $v^*$. In particular,
$v^*=K\Phi(v^*)$ and $\sum_i\Phi_i(v^*)=2\sqrt{nW}$.

For clarity use the counting Euclidean norm. Set
$D_t=\|v_t-v^*\|_2^2$, $E_t=\|v_t\|_2^2$ and
$\gamma_{t,i}=\operatorname{arsinh}(v_{t,i}/(2\sqrt{w_i}))$, with
$\gamma_i^*$ defined at $v^*$. Put

$$
H_t=8\sum_i w_i(\cosh(\gamma_{t,i}-\gamma_i^*)-1),\qquad
N_t=4(s_t-\sqrt W)^2.
$$

The relative dissipation identity

$$
D_t-D_{t+1}=H_t+N_t                                             \tag{1}
$$

is the stationary version of the [hyperbolic secant identity](parallel-activation-26.md)
and was already written in the [earlier external audit](chatgpt-2026-11-17.md).
Indeed, for $x=2\sqrt w\sinh\gamma$, $y=2\sqrt w\sinh\eta$,
subtracting the squared activation difference from $(x-y)^2$ gives
$8w(\cosh(\gamma-\eta)-1)$. Applying $K$ to the activation difference
subtracts exactly the constant Fourier energy $N_t$.

Set $b_q=2\sqrt{q/n}$, $A=b_q\sqrt W$, and
$C=\max(A^2+1,9q/n)$. The entry bound on $K$, with
nonnegative activations, gives
$|v_{t,0}|\le b_q s_{t-1}$ for $t\ge1$ and
$|v_0^*|\le A$, where $v_0^*$ denotes the stationary marked
**coordinate**. For $s_{t-1}\le2\sqrt W$, the derivative of $2\sinh$
between the two marked angles is at most $\sqrt{4A^2+4}$.
Since $2(\cosh x-1)\ge x^2$, this gives
$|v_{t,0}-v_0^*|^2\le(A^2+1)H_t$. The same bound holds at $t=0$.
For $s_{t-1}>2\sqrt W$, use

$$
|v_{t,0}-v_0^*|\le b_q(s_{t-1}+\sqrt W)
\le3 b_q(s_{t-1}-\sqrt W).
$$

Its square is bounded by $9(q/n)N_{t-1}$. The two cases charge
distinct terms in (1): each $H_t$ and $N_t$ is charged at most once.
Consequently for every $L\ge0$

$$
\boxed{\quad
\sum_{t=0}^L |v_{t,0}-v_0^*|^2\le C(D_0-D_{L+1})
\le 4CW\sqrt q.
\quad}                                                           \tag{2}
$$

For the last inequality, $|v^*\|_1\le 2\sqrt{nW}$ and
$|v^*\|_\infty\le A$ imply $D_0\le4W\sqrt q$.
One may keep the actual terminal term
$D_0-D_{L+1}=2\langle v^*,v_{L+1}\rangle-E_{L+1}$.
The large-mean case is needed for a square error in $v$: controlling
only the angle via $H_t$ would not provide it when $|v_{t,0}|$ is
large.

By (1), for the round-35 mean $M_T=T^{-1}\sum_{t=1}^T\mu_t$,

$$
|\sqrt n M_T-\sqrt W|\le\sqrt{W\sqrt q/T}.                    \tag{3}
$$

The marked projection identity of round 35 reads

$$
X_{\sigma,T}(0)=\frac{\mu_T-\mu_0}{2T}
+\frac1{4T}\sum_{t=1}^T[
\Phi_0(v_t)+\Phi_0(v_{t-1})+\sigma(v_{t,0}+v_{t+1,0})].
$$

At stationarity its bracket is constant $4A_\sigma^*(0)$.
The activation at the mark is one-Lipschitz. Apply Cauchy--Schwarz
to each of the four time sums using (2) with $L=T+1$, and use
$s_T^2\le W(T+1)$ from the zero-start norm telescope. This yields

$$
|X_{\sigma,T}(0)-A_\sigma^*(0)|
\le 2\sqrt{CW\sqrt q/T}+\frac{\sqrt{W(T+1)}}{2T\sqrt n}.      \tag{4}
$$

Thus whenever $T/\sqrt n\to\infty$ at fixed positive floor,
the normalized projected marks approach
$A_\sigma^*(0)/\sqrt W$ after division by $\sqrt n M_T$.
Equation (2) also gives

$$
\left|\left(\frac1{T+2}\sum_{t=0}^{T+1}|v_{t,0}|^2\right)^{1/2}
     -|v_0^*|\right|
\le 2\sqrt{CW\sqrt q/(T+2)}.                                  \tag{5}
$$

In particular the marked Cesaro condition on either the round-36
$n^{5/4}$ horizon or the new linear horizon requires vanishing of
the actual stationary mark $m=\operatorname{arsinh}(v_0^*/2)$ at that
floor. On squares with fixed $0<\tau<1$, the exact square theta gives
$m\ge \log((\sqrt q-1)/\sqrt{nW})\to\tfrac12\log(2/(1+\tau))>0$,
so (5) gives a positive square obstruction at every such horizon.
The established short-depth marker theorem does not reach this time scale.

## 2. Finding a positive prefix without reflection

Let $A_{\sigma,t}=(\Phi(v_t)+\sigma v_t)/2\$.
Write $C_{\sigma,L:R}$ for its arithmetic mean over the indicated
inclusive time range. We use both ranges $1:T$ and $0:T-1$.
The norm telescope $E_{t+1}-E_t=4W-4s_t^2$ from zero gives
$T^{-1}\sum_{j=0}^{T-1}s_j^2\le W$. By $A_{\sigma,t}(i)\le
|v_{t,i}|+\sqrt{w_i}$, $|v_{t,i}|\le b_q s_{t-1}$ for $t\ge1$,
and $v_0=0$, on **both** ranges $mathcal I$ we have
$C_{\sigma,\mathcal I}(i)\le A+\sqrt{w_i}$.
Also $C_{+,\mathcal I}(i)C_{-,\mathcal I}(i)\ge w_i$ by time
Cauchy--Schwarz and $A_{+,t}(i)A_{-,t}(i)=w_i$. Therefore

$$
\min_{\sigma,i,\mathcal I} C_{\sigma,\mathcal I}(i)
\ge \frac{c}{A+\sqrt c}.                                      \tag{6}
$$

The function $w/(A+\sqrt w)$ is increasing for $w>0$.
The exact [weighted endpoint identity](astra-averaged-positive-36.md#2-weighted-endpoint-identity-with-the-full-budget)
for uniform weights is

$$
X_{\sigma,T}
=\frac12(C_{\sigma,1:T}+C_{\sigma,0:T-1})
+\frac{\mu_T-\mu_0}{2T}1
+\frac{\sigma}{4T}(v_T+v_{T+1}-v_1) \qquad (T\ge2).           \tag{7}
$$

The scalar term is nonnegative. Let $b=2(1-\sqrt c)\sqrt q/n\$,
so $|v_1\|_\infty\le b$. Fix $\epsilon>0$. Call a terminal
depth $T$ good when $s_{T-1},s_T\le(1+\epsilon)\sqrt W$.
At such $T$ the vector correction in (7) has sup norm at most
$[2(1+\epsilon)A+b]/(4T)$. Therefore both projected averages
are strictly positive if $T$ is good and

$$
T> L_\epsilon:=\frac{(2(1+\epsilon)A+b)(A+\sqrt c)}{4c}.       \tag{8}
$$

There are at most $\lfloor\sqrt q/\epsilon^2\rfloor$ bad indices
$j$ with $s_j>(1+\epsilon)\sqrt W$ in the entire orbit: each
costs more than $4\epsilon^2 W$ from the total reserve
$\sum_j N_j\le D_0\le 4W\sqrt q$. Each bad index obstructs at
most two neighboring terminal depths. From any starting integer
$S\ge\max(2,\lfloor L_\epsilon\rfloor+1)$, at least one good
depth is found in

$$
[S,S+2\lfloor\sqrt q/\epsilon^2\rfloor].
$$

Check only the actual means at consecutive steps to choose it. The
resulting rows are the original $X_{\sigma,T}/M_T$; they retain
the budget, sector and mark by construction. With
$\epsilon=n^{-1/6}$ and $S=\max(2,\lfloor L_\epsilon\rfloor+1)$,
the selected depth is at most $4(1+\tau)n/\tau+O_\tau(n^{5/6})$.
Here $A^2/(2c)=2qW/\tau$ has this linear leading term.
The selection bound is for an unrepaired prefix, while the
[one-reflection argument](astra-completion-37.md) covers each
sufficiently long prefix. Neither provides a positive construction
within the short marked arithmetic window.
