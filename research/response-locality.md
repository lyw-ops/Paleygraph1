# Marked response under changes on a frequency set

Use the Paley operator $K$, the projection $P=I-J$ onto mean-zero vectors, and $H(D)=K-PDP$ on that subspace. For any real diagonal $D$ with $|D_i|<1$, let $X(D)$ be the inverse extended by zero on the constants. Write $D_i=\tanh\gamma_i$ and $M_i=\sqrt{1-D_i^2}$. The matrix

$$R(D)=M X(D) M-D$$

agrees with the difference of the complementary projectors at the true stationary diagonal, so $R(D)_{00}$ there is the [marked leverage difference](marked-response.md). The identities below hold for every strict real diagonal.

## Contraction and response derivative

For a vector $z$, set $v=X(D)Mz$. Then $Kv=P(Dv+Mz)$ and $\|Kv\|=\|v\|$. The block map taking $(v,z)$ to $(Dv+Mz,Mv-Dz)$ is orthogonal because $D^2+M^2=I$. Subtracting $\|v\|^2$ from the corresponding norm identity gives

$$\|R(D)z\|^2+\|J(Dv+Mz)\|^2=\|z\|^2.$$

In particular the symmetric $R(D)$ is a contraction. Along any smooth path of $\gamma$, put $E=\operatorname{diag}(\dot\gamma_i)$. We have $\dot D=M^2 E$, $\dot M=-DME$, and $\dot X=X\dot D X$ on the mean-zero subspace with the zero extension. Therefore

$$\dot R=R E R-E.$$

At the marked coordinate this reads $\dot R_{00}=\sum_i R_{0i}^2\dot\gamma_i-\dot\gamma_0$. Holding the mark fixed, $R_{00}$ is nondecreasing in each bulk $\gamma_i$.

## Changing an entire set

Let $S$ exclude the mark. At a reference diagonal write $A=R_{SS}$ and $c=R_{S0}$. Increase every $\gamma_i$ in $S$ by the same $t$, with the other coordinates fixed. The differential equation gives $\dot A_t=A_t^2-I$, $\dot c_t=A_t c_t$, and $\dot R_{00}(t)=\|c_t\|^2$. With $u=\tanh t$, the solutions are

$$A_t=(A-uI)(I-uA)^{-1},\qquad c_t=\sqrt{1-u^2}(I-uA)^{-1}c,$$

$$R_{00}(t)-R_{00}(0)=c^{\mathsf T}u(I-uA)^{-1}c.$$

These formulas follow by diagonalizing $A$ and integrating the scalar equations. For an arbitrary change supported on $S$, bound it above and below by the shifts $t$ and $-t$ with $t$ the maximum absolute change. Bulk monotonicity then implies that whenever $\|A\|\le1-\delta$, the change in $R_{00}$ is bounded by $\|c\|^2/\delta$, uniformly in the size and signs of the changes to $\gamma$.

### A one-sided envelope with a reference and an exceptional set

Take strict diagonals $E,F$ whose marked entries are zero, and write $m_E=R(E)_{00}$. Fix a sign $\sigma$ and a bulk set $S$ with

$$\sigma\big(\operatorname{arctanh}F_i-\operatorname{arctanh}E_i\big)\le\theta
\quad(i\notin S\cup\{0\}),\qquad \theta\ge0.$$

On $S$ allow arbitrary changes. Define the inverse quadratic form of the reference by

$$L_\sigma(E,S)=c^{\mathsf T}(I_S-\sigma A)^\dagger c,\qquad
A=R(E)_{SS},\quad c=R(E)_{S0}.$$

The inverse is zero on the kernel. In fact any vector on $S$ with $Af=\sigma f$, extended by zero, satisfies $R(E)f=\sigma f$ by contractivity and therefore $c^{\mathsf T}f=0$. Set $b=\sigma m_E+L_\sigma(E,S)$. Then $-1\le b\le1$ and

$$
\boxed{\displaystyle
\sigma m_F\le\frac{b+\tanh\theta}{1+b\tanh\theta}.} \tag{1}
$$

First increase the hyperbolic coordinates in $S$ by $\sigma s$, where $s$ is a positive constant larger than all the required signed increases. The exact set-shift formula gives the signed marked increment $\tanh s\,c^{\mathsf T}(I_S-\sigma\tanh s\,A)^{-1}c$. It tends to $L_\sigma(E,S)$ as $s\to\infty$, including when the compression has an endpoint eigenvalue. Contractivity gives $b\le1$. Next increase the hyperbolic coordinates in the other bulk set $T$ by $\sigma\theta$. At any intermediate increase $\sigma h$ there, with $z(h)=\sigma R_{00}(h)$, the differential equation gives

$$z'(h)=\sum_{i\in T}R_{0i}(h)^2\le1-z(h)^2.$$

For finite strict diagonals with marked entry zero, $|z|<1$ by the [stripped norm identity](stationary-attenuation.md#two-source-identities). Integrating the derivative of $\operatorname{arctanh}z$ gives $z(\theta)\le(z(0)+\tanh\theta)/(1+z(0)\tanh\theta)$. The two shifts dominate $F$ in the signed coordinate order. Monotonicity followed by $s\to\infty$ proves (1).

With $E=0$ one has $m_E=-1/n$ in the Paley problem, and $L_\sigma(0,S)=K_{S0}^{\mathsf T}(I_S-\sigma K_{SS})^\dagger K_{S0}$. For a signed cap $\sigma F_i\le\rho<1$ outside $S$, use $\theta=\operatorname{arctanh}\rho$. Equation (1) gives $\sigma m_F\le\rho+L_\sigma(0,S)+1/n$. This sharpens the [constant-background comparison](parallel-exterior-3.md#a-marked-upper-bound-using-only-zero-diagonal-geometry-and-a-cap) and also applies to nonconstant reference diagonals.

For the stationary problem a reference with $\sigma m_E=o(1)$, $\theta=o(1)$ and $L_\sigma(E,S)=o(1)$ gives the corresponding one-sided marked bound. The cap only restricts the signed relative hyperbolic coordinates outside $S$. The inverse quadratic form allows compression eigenvalues approaching the endpoint if their contribution to the marked column is sufficiently small.

A dense check at two small prime and two small square orders verified this envelope in 256 reference, target and exceptional-set comparisons. It also tested orthogonality of the marked column to the endpoint eigenspace of the reference compression.

### A pointwise one-sided bound

For strict diagonals $E,F$ with zero mark, let $s_i=(\sigma[\operatorname{arctanh}F_i-\operatorname{arctanh}E_i])_+$ and let $S=\{i:s_i>0\}$. Write $T=\operatorname{diag}(\tanh s_i:i\in S)$, $A=R(E)_{SS}$ and $c=R(E)_{S0}$. Then

$$
\sigma(m_F-m_E)\le c^{\mathsf T}(T^{-1}-\sigma A)^{-1}c
\le \frac12\sum_{i\ne0}R(E)_{i0}^2(e^{2s_i}-1). \tag{2}
$$

The value is zero when $S$ is empty. The first bound is equality if all changes are ordered in direction $\sigma$. In general increase the reference hyperbolic coordinates by $\sigma s_i$ to dominate $F$ in that order. To prove the exact ordered formula, reduce to $\sigma=1$ by changing $K,E,F$ to $\sigma K,\sigma E,\sigma F$, so the response also changes by $\sigma$. With $V=(F-E)_{SS}>0$ and $M_i=\sqrt{1-E_i^2}$, the resolvent formula on $S$ gives

$$m_F-m_E=x_S^{\mathsf T}(V^{-1}-(X_E)_{SS})^{-1}x_S,\qquad x=X_Ee.$$

Conjugate the middle denominator by $M_S$ and use $M X_E M=R(E)+E$. The diagonal term is $(1-E_i^2)/V_i-E_i=(1-E_i F_i)/V_i=1/T_i$, and $M_S x_S=c$. Since $\sigma A\preceq I$, the inverse in (2) is bounded above by $(T^{-1}-I)^{-1}$. Its entries are $\tanh s_i/(1-\tanh s_i)=(e^{2s_i}-1)/2$. This gives a bound in terms of a single known reference column without requiring a gap for the compression.

On 320 mixed changes at small prime and square orders, the exact ordered formula agreed with direct inversion to within $2.8\cdot10^{-15}$ and both comparisons held.

At $D=0$, $R=K$ and $|c_i|\le1/m_0$ with $m_0=n/\sqrt q$. The [progression compression gap](progression-gap.md) therefore gives a marked change of $O_B(1/m_0)$ for any diagonal supported on a bulk subset of one of those progressions. The entries on the set may be arbitrarily close to either endpoint of $(-1,1)$.

## A uniformly bounded background

Suppose that at a reference diagonal $D$ we have $D_i=0$ on $S$ and $\|D\|\le\rho<1$. Put $m_*^2=1-\rho^2$. If $\|K_{SS}\|\le1-\delta$ and $|S|/n\le\delta/2$, then

$$\|R(D)_{SS}\|\le1-\frac{\delta^2 m_*^2}{8(1+\rho)^2}.$$

For the bound, let $f$ be a unit eigenvector of $R(D)_{SS}$ extended by zero, with eigenvalue $\sigma(1-\epsilon)$ of largest magnitude and $\sigma=\pm1$. Since $R(D)$ is a contraction, $\|R(D)f-\sigma f\|\le\sqrt{2\epsilon}$. With $x=X(D)f$, $R(D)f=Mx$ and $M_i=1$ on $S$, so $\|x-\sigma f\|\le\sqrt{2\epsilon}/m_*$. Project $Kx=P(Dx+f)$ onto $S$. Because $Df=0$ and $\|P_S Jf\|\le |S|/n$, this yields

$$\delta\le\|K_{SS}f-\sigma f\|\le (1+\rho)\sqrt{2\epsilon}/m_*+|S|/n,$$

which gives the claimed gap. Hence an arbitrary change on $S$ is negligible at the marked point if the reference column satisfies $\|P_S R(D)e_0\|=o(1)$ and the two gaps $1-\rho$ and $\delta$ are fixed.

The column condition holds for a clipped fixed-depth diagonal, using the [fixed-expression closure rules](iteration-parity.md). Use the diagonal at a fixed Picard depth $t$, clipped to $[-\rho,\rho]$ and with its marked entry set to zero. Then $X(D)e_0$ has the norm-convergent series $\sum_{j\ge0}(K D)^j K e_0$. After scaling by $\sqrt n$, each fixed term is approximable in normalized $\ell_2$ by bounded expressions of negative type. The initial term is the Jacobi field. The clipped activation is a bounded Lipschitz odd function of the scaled iterate in the bulk, and can be approximated in normalized $\ell_2$ by negative expressions. Multiplication by it takes the product of two negative expressions, and applying $K$ returns a negative expression. At each step, first choose a bounded approximation to the current term and then approximate the clipped activation so the product error is small. This proves the approximation by induction. The tail of the series is bounded by $\rho^{j+1}/(1-\rho)$ in unscaled $\ell_2$, uniformly in $q$.

It follows that $X(D)e_0$ has vanishing mass on any $o(n)$ set, including the mark alone. Zeroing $D$ on such an $S$ preserves this property and the marked limit. Indeed the change in the column is at most $(1-\rho)^{-1}\rho\|P_S X(D)e_0\|$ by the resolvent identity. The progression gap and the preceding argument now allow arbitrary bulk activations on $S$ while preserving a vanishing marked inverse entry. This transfer uses the fixed-depth approximation only for the bounded background. The stationary diagonal still needs to be related to such a background away from the exceptional set.

For use with the [marked-inverse criterion](marked-response.md#a-symmetric-operator-for-the-response), strip the actual marked entry from the diagonal first. If $m$ and $m^\circ$ are the marked inverse entries before and after stripping, the rank-one resolvent identity gives $m=m^\circ/(1-D_0m^\circ)$. So $m^\circ\to0$ suffices regardless of the actual marked activation. For the stripped diagonal $m^\circ=R_{00}$.

## Square-order test of the formula

At $q=r^2$, let $S$ be the subfield annihilator with the mark deleted and put $b=|S|=(r-1)/2$. From the exact Jacobi values on this subgroup, $c$ at the zero reference is constant $r/n$, and $K_{SS}$ has eigenvalue $\alpha=(r(b-1)-1)/n$ on the constants. If $D_i=d$ on $S$ and zero elsewhere, the shift formula is exactly

$$R_{00}(D)=-\frac1n+\frac{d b r^2/n^2}{1-d\alpha}.$$

For $d=1-1/q$, this tends to $2/3$ as $r\to\infty$. The progression result gives a vanishing response for an equally sized interval with a generating step. Here the diagonals are prescribed to compare the two compression mechanisms. At $q=389^2$ and $p=151337$, both supports have size $194$ and the respective responses are about $0.6638064$ and $0.0024353$. The [prescribed-shift probe](../response_shift.py) uses the formula with the numerically computed compression and marked column. The [output](../data/response-shift.csv) agrees with the closed form at all three square orders. Direct inversion on small prime and square orders also checks the shift formula at nonzero reference diagonals.
