# One-sided exterior compression and a marked upper bound

Let $J=\mathbf1\mathbf1^{\mathsf T}/n$, $P=I-J$, and $K^2=P$ with $K$ real symmetric and $KJ=0$. For a real diagonal $E$ with $|E_i|<1$, write $X_E=(K-PEP)^{-1}P$, extending the inverse on $P\mathbb R^n$ by zero, and $m_E=(X_E)_{00}$. The actual exterior is $E=D$ off the deleted bulk set $S$ and the mark, with zero diagonal on $S\cup\{0\}$. The [stationary overlap bound](parallel-coupling-2.md#stationary-column-and-same-sign-deletion) supplies a separate sufficient condition for a small deletion effect.

## Transfer with a cap on the retained sign

For $\sigma=\pm1$, suppose $E$ vanishes on $U$ and $\sigma E_i\le\rho<1$ off $U$, with $0\le\rho<1$. Set $\delta=1-\lambda_{\max}(\sigma K_{UU})$. Then

$$
I_U-\sigma(X_E)_{UU}\succeq
\frac{(1-\rho)\delta}{1+\rho-\rho\delta}\,I_U. \tag{1}
$$

The estimate allows $\sigma E_i$ to approach $-1$. Differentiate $X_B$ along a line of diagonals to get $\dot X_B=X_B\dot B X_B$. Thus $\sigma X_E$ increases in Loewner order as $\sigma E$ increases. Compare with $\rho$ off $U$ and zero on $U$, using $\sigma K$ and $\sigma E$ as the operator and diagonal. Before zeroing the constant $\rho$ on $U$, the compressed inverse is

$$A=\frac{\sigma K_{UU}+\rho P_{UU}}{1-\rho^2}.$$

After zeroing it is $A(I+\rho A)^{-1}$ by the resolvent identity. The denominator is positive since $A\succeq-I_U/(1+\rho)$. Apply the increasing scalar function $a\mapsto a/(1+\rho a)$ to the top eigenvalue and use $P_{UU}\preceq I_U$ to get (1).

For same-sign reactivation $F=E+\sigma C^2$ on $S=U$, where $C=\operatorname{diag}(\sqrt{|D_i|}:i\in S)$, the denominator in the marked update is

$$I_S-\sigma C(X_E)_{SS}C=I_S-C^2+C[I_S-\sigma(X_E)_{SS}]C.$$

If $g$ is the gap in (1), this has gap at least $\min(1,g)$. The deletion increment $\sigma(m_F-m_E)$ is at most $\|C(X_E e_0)_S\|_2^2/\min(1,g)$ for $g>0$. For the true stationary $D$, (1) applies whenever $S$ includes every bulk coordinate with $\sigma D_i>\rho$. The prescribed example below exhibits a large exterior column under this cap.

## Exact weighted criterion when some high coordinates are retained

Define $Q=J+(P-\sigma K)/2$, the orthogonal projector onto the constants plus the opposite Fourier sector. Write $Lh=h_U$ for restriction to $U$ on $\operatorname{ran}Q$, $B=LL^*=Q_{UU}$, and

$$r_i=\frac{1+\sigma E_i}{1-\sigma E_i},\qquad
T=Q(\operatorname{diag}r+J)Q\big|_{\operatorname{ran}Q}.$$

There are exact formulas

$$
G:=I_U-\sigma(X_E)_{UU}=2LT^{-1}L^*,\qquad
\langle a,G^{-1}a\rangle=\frac12\min_{h\in\operatorname{ran}Q:\ h_U=a}
\left(\sum_i r_i|h_i|^2+\|Jh\|_2^2\right), \tag{2}
$$

where the inverse formula assumes $B>0$. In particular $B\succeq\delta I_U/2$. To check the first identity, extend $f\in\mathbb R^U$ by zero, put $z=\sigma X_Ef$, and set $h=f-(I-\sigma E)z$. The inverse equation gives $P h=(\sigma K-I)z$. Thus $h\in\operatorname{ran}Q$, $Qz=-(Q-J)h/2$, and applying $Q$ to $z=(I-\sigma E)^{-1}(f-h)$ gives $Th=2Qf$. Restricting $h$ to $U$ gives $Gf$. For the minimum, the feasible vector $T^{-1}L^*(LT^{-1}L^*)^{-1}a$ is $T$-orthogonal to $\ker L$.

The gap is therefore equivalent to a uniform bound on the least weighted energy needed to extend data on $U$ in the opposite support. A sufficient test using only the unweighted minimum-norm extension is as follows. For $r_*\ge1$ let

$$\mathcal C=\|\operatorname{diag}(\sqrt{(r_i-r_*)_+})L^*B^{-1/2}\|^2.$$

Test the minimum using $h=L^*B^{-1}a$. Its squared norm is $\langle a,B^{-1}a\rangle$ and $\sum_i r_i|h_i|^2+\|Jh\|^2\le(r_*+1+\mathcal C)\|h\|^2$. Hence

$$G\succeq \frac{2}{r_*+1+\mathcal C}B. \tag{3}$$

At the true stationary exterior, $A_\sigma=(u+\sigma v)/2$, $A_+A_-=w$ coordinatewise, and $r_i=A_{\sigma,i}^2/w_i$ where the diagonal is retained. If $U$ includes the stripped mark, $H=\{i\notin U:\sigma D_i>\rho\}$, $r_*=(1+\rho)/(1-\rho)$ and $b_U=\lambda_{\min}(B)>0$, the entry bound $|K_{ij}|\le\sqrt q/n$ gives the explicit sufficient estimate

$$
\mathcal C\ \,\le\ \,\frac{(1+\sqrt q)^2 |U|}{4n\tau b_U}\sum_{i\in H} A_{\sigma,i}^2. \tag{4}
$$

Indeed each squared row norm of $L^*B^{-1/2}$ off $U$ is at most $(1+\sqrt q)^2|U|/(4n^2b_U)$, and $r_i=nA_{\sigma,i}^2/\tau$ there. At fixed $\rho$, a bounded right side in (4) suffices to preserve the gap at its original scale even when individual retained entries saturate. The local operator test (3) can be smaller than this squared-mass estimate. A single retained coordinate with $A_{\sigma,i}$ of order one already costs order $n/\tau$ in the weight $r_i$.

## A marked upper bound using only zero-diagonal geometry and a cap

There is a different comparison for the *full stripped mark*. Let $F_0=0$ and suppose $\sigma F_i\le\rho$ off $S\cup\{0\}$, with arbitrary strict values on $S$. Put

$$
L_0=(\sigma K_{S0})^{\mathsf T}(I_S-\sigma K_{SS})^\dagger(\sigma K_{S0}).
$$

The dagger is the inverse on the positive eigenspaces, with zero on the kernel. For $n\ge4$,

$$\sigma m_F\le\rho+4L_0+8/n. \tag{5}$$

To check it, increase the signed diagonal to $\rho$ on the exterior bulk and let the value on $S$ increase to one. Compute this upper comparison starting at the constant $\rho$ on *all* coordinates, adding $1-\rho$ on $S$, then stripping the mark. Define

$$
L_\rho=(\sigma K_{S0}-\rho\mathbf1_S/n)^{\mathsf T}
(I_S-\sigma K_{SS}+\rho J_{SS})^\dagger(\sigma K_{S0}-\rho\mathbf1_S/n),
\quad a=\rho-(\rho+\sigma)/n+L_\rho.
$$

Here $K_{00}=-1/n$ is the Paley marked entry. The resolvent update on $S$ gives the limiting mark before stripping as $a/(1-\rho^2)$, and the rank-one stripping gives $a/(1-\rho^2+\rho a)$. A null vector for $I_S-\sigma K_{SS}$, extended by zero, is an exact $\sigma$ eigenvector of $K$, so it has zero mean and is orthogonal to $K e_0$. This makes the endpoint formulas finite and justifies the inverse on the positive eigenspaces. The inequality $I_S-\sigma K_{SS}+\rho J_{SS}\succeq\rho J_{SS}$ gives a squared inverse-form norm of at most $\rho/n$ for $\rho\mathbf1_S/n$. The other vector has squared inverse-form norm at most $L_0$. Thus $L_\rho\le(\sqrt{L_0}+\sqrt{\rho/n})^2$. Subtract $\rho$ from the stripped fraction, whose denominator is at least $1-2/n$, to obtain (5).

For example $L_0\le q|S|/(n^2\delta)$ when $\delta>0$, while the [positional-block calculation for translated cosets](coset-response.md#a-uniform-bound-from-the-zero-reference) can give $L_0=O(q^{-1/2})$ even without a fixed eigenvalue gap. At the true stationary diagonal $m_F=D_0+O(\tau)$ by the [leverage identity](coset-activation.md#the-exact-interaction). Consequently at decreasing floors a cover of the actual one-sided high set with $\rho=o(1)$ and $L_0=o(1)$ would give the one-sided theta bound directly. One can also use fixed caps followed by $\rho\downarrow0$ where the corresponding covers exist. The comparison uses the zero-diagonal marked column $K_{S0}$ in place of the exterior marked column.

## Prescribed prime-field exteriors can still focus the column

The cap $\rho=0$ and $\|K_{SS}\|=o(1)$ are compatible with an order-one deletion increment for prescribed diagonals. In the [two-frequency construction](exterior-column.md#constructing-a-bounded-centered-exterior), take $f=(e_h+e_{-h})/\sqrt2$ and use the displacement with $\sum_{i\notin\{0,\pm h\}}|(Ke_0)_i(Kf)_i|\ge1/(2\sqrt2)-o(1)$. Let $\eta$ be the sign of $f^{\mathsf T}Ke_0$ (either sign if zero), and take $E_i=-1/16$ on the exterior indices where $\eta(Ke_0)_i(Kf)_i<0$, and zero everywhere else. The sum of the signed products in the exterior is $O(n^{-1})$ by $K^2=P$ and the entry bound. The first Neumann correction to $\eta f^{\mathsf T}X_Ee_0$ is therefore at least $1/(64\sqrt2)-o(1)$ and the remaining terms have total magnitude at most $1/240$. The zeroth term is nonnegative by the choice of $\eta$. For large fields the exterior column has a component of magnitude at least $1/200$ on $f$. Adding $1/4$ on $S=\{h,-h\}$ then increases the mark by at least $(1/5)\|(X_Ee_0)_S\|_2^2$ by the rank update and [contractivity](response-locality.md#contraction-and-response-derivative). This construction chooses a prescribed, even, nonpositive exterior directly from Jacobi fields at prime or square orders.

## A true square stationary counterexample with retained same-sign highs

Take $q=r^2$, $n=(q-1)/2$, and $\tau=n^{-2}$. Let $G_0$ be the subfield annihilator of size $b=(r+1)/2$, including the mark. The [square certificate](square-order-control.md#the-fourier-frequencies-carrying-the-discrepancy) gives $K\mathbf1_{G_0}=\mathbf1_{G_0}-(b/n)\mathbf1$ and the plus theta optimum $r-1$. Choose $S\subset G_0\setminus\{0\}$ of size $1\ll s\ll r$, retain $R=G_0\setminus(S\cup\{0\})$, and take $E$ from the true stationary diagonal by zeroing $S$ and the mark. Use $\sigma=+1$ in (2). Then

$$\|K_{SS}\|\le s\sqrt q/n=o(1),\qquad
\lambda_{\min}\big(I_S-(X_E)_{SS}\big)=O(s^{-1}). \tag{6}$$

To verify saturation on the subfield frequencies, use $A_-\in\operatorname{ran}Q$, so $\sum_{G_0} A_{-,i}=b\sqrt{W/n}$. The optimum gives $A_{+,0}\le (r-1)\sqrt{W/n}$ and $A_{-,0}=1/A_{+,0}\ge b/\sqrt{nW}$. Thus

$$\sum_{G_0\setminus\{0\}}A_{-,i}\le b(W-1)/\sqrt{nW}=O(\tau),\qquad
\sum_{i\in G_0\setminus\{0\}}\frac{1-D_i}{1+D_i}
=\frac n\tau\sum_{i\in G_0\setminus\{0\}}A_{-,i}^2=O(n\tau).$$

In particular both the deleted and the retained coordinates of $G_0\setminus\{0\}$ have $D_i\to1$ uniformly. For $h\in\operatorname{ran}Q$, the same square identity gives $\sum_{G_0}h_i=(b/\sqrt n)\langle h,\mathbf1/\sqrt n\rangle$. With $f=\mathbf1_S/\sqrt s$, this gives by weighted Cauchy–Schwarz

$$
|\langle f,Lh\rangle|^2\le\frac{b^2/n+1+\sum_{i\in R}r_i^{-1}}{s}
\big(\|Jh\|^2+|h_0|^2+\sum_{i\in R}r_i|h_i|^2\big)
\le\frac{O(1)}{s}\langle h,Th\rangle.
$$

Here $r_0=1$ at the stripped mark, and the prefactor uses $b^2/n=O(1)$ and the stationary reciprocal bound on $R$. Taking the supremum over $h$ and using (2) proves (6) for arbitrary strict values of the diagonal off $G_0$. The weighted update denominator $I_S-C(X_E)_{SS}C$ also has gap $O(s^{-1}+n\tau)=O(s^{-1})$, by testing on $C^{-1}f$ with $C^2=D_S$. For this sparse deletion the conclusion concerns the compression gap. The [order-one stationary deletion effect](parallel-coupling-2.md#exact-square-order-control-with-decreasing-floors) uses deletion of the entire positive bulk set.

## Checks and remaining prime input

Direct dense solves at $q=41,101,7^2,11^2$ checked the form identity in (2), the bounds (1) and (3), and the exact marked envelope leading to (5) in 96 prescribed signed cases. The maximum entry discrepancy in the form identity was $2.3\times10^{-15}$. Six singular compression cases at $q=41$ checked convergence to the pseudoinverse endpoint. True square solves with $r=7,11,17,23$ at $\tau=n^{-2}$ verified the witness inequality and the flat-vector bound in (6), with stationary residuals below $1.1\times10^{-12}$. The nonpositive prescribed exteriors at $9413,37253,97^2,193^2$ gave marked increments between $2.7\times10^{-4}$ and $5.9\times10^{-4}$. These floating-point checks supplement the variational and square-witness proofs.

For prime fields (1) settles the transfer from a signed compression gap once the retained same-sign activation is capped. With uncapped retained highs, (2) identifies the weighted extension estimate and (3) gives a test in terms of the exterior on specific opposite-sector extensions. For marked cancellation via (5), the needed arithmetic input is a cover of the true same-sign high set with small zero-diagonal marked capacity. Both the weighted extension estimate for prime stationary tails and the existence of such covers remain open.
