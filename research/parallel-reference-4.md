# Exceptional sets at a fixed-depth reference

For [Randomstrasse101 Problem 26](https://randomstrasse101.math.ethz.ch/posts/PaleyGraph/), the [one-sided comparison](response-locality.md#a-one-sided-envelope-with-a-reference-and-an-exceptional-set) requires the marked form $L_\sigma(E,S)$ of the reference, rather than a gap on all of $S$. There is an exact weighted extension on the opposite Fourier sector **including the constants**. At a uniformly bounded reference, it is equivalent, up to explicit factors, to a zero-background form on modified data. At fixed depth the modified data have a separate constant contribution. A translated subfield coset at square order shows that this contribution cannot be dropped even for a clipped first Picard iterate.

## Exact extension for a strict diagonal

Use the frequency coordinates, the mark $0$, $J=jj^{\mathsf T}$ with $j=\mathbf1/\sqrt n$, $P=I-J$, and $K=K^{\mathsf T}$ with $K^2=P$ and $KJ=0$. The inverse $X_E=(K-PEP)^{-1}$ on $P\mathbb R^n$ is extended by zero. For real diagonal $E$ with $|E_i|<1$ and $E_0=0$, let $M=(I-E^2)^{1/2}$ and $R=M X_E M-E$. Fix $\sigma=\pm1$ and $S$ not containing $0$, and write $c=R_{S0}$. Define

$$
V=\operatorname{ran} Q,\quad Q=J+(P-\sigma K)/2,\quad
w_i=\sqrt{\frac{1+\sigma E_i}{1-\sigma E_i}},\quad W=\operatorname{diag}(w_i),
\quad T=Q(W^2+J)Q\big|_V .
$$

Here $T>0$ on $V$. Let $D_S:V\to\mathbb R^S$ be coordinate restriction. The full identity and the marked extension are

$$
I-\sigma R=2W Q T^{-1}Q W,\qquad
\boxed{\displaystyle L_\sigma(E,S)=\frac12
\min_{\substack{h\in V\\h_S=W_S^{-1}c}}
\left(\sum_i w_i^2|h_i|^2+\|Jh\|_2^2\right).} \tag{1}
$$

Here and below inverse operators on $V$ act by zero on its orthogonal complement. Formula (1) includes singular compressions and nonzero $E_S$; when $E_S=0$ the compressed operator is the one in the [exterior extension formula](parallel-exterior-3.md#exact-weighted-criterion-when-some-high-coordinates-are-retained).

To prove it, put $D=\sigma E$. For any input $f$ set $z=\sigma X_E M f$ and $h=M f-(I-D)z$. The inverse equation gives $Ph=(\sigma K-I)z$, so $h\in V$ and $2Qz=-h+Jh$. Also $z=W f-(I-D)^{-1}h$ and $2(I-D)^{-1}=I+W^2$. Projecting gives $Th=2Q W f$. Since $(I-\sigma R)f=Wh$, this proves the first identity.

On $S$ the signed defect is $G_E=I_S-\sigma R_{SS}=2 W_S D_S T^{-1}D_S^* W_S$. Its range contains $c$, since $c=-\sigma(I-\sigma R)_{S0}$ and $\operatorname{ran}(D_S T^{-1}D_S^*)=\operatorname{ran}D_S$. In particular, $W_S^{-1}c$ is feasible. For any $a$ in $\operatorname{ran}D_S$, the least $T$-energy lift of $a$ is $T^{-1}D_S^*(D_S T^{-1}D_S^*)^\dagger a$: it is feasible and $T$-orthogonal to $\ker D_S$. Its energy is $a^{\mathsf T}(D_S T^{-1}D_S^*)^\dagger a$. Equivalently, for $G\succeq0$ and $u\in\operatorname{ran}G$, $u^{\mathsf T}G^\dagger u=\sup_f(2u^{\mathsf T}f-f^{\mathsf T}Gf)$, so an invertible congruence changes the data by the inverse factor even if $G$ is singular. This proves the extension formula. Any feasible $h$ gives an upper certificate; a test vector $f$ with $f^{\mathsf T}G_E f>0$ gives the lower certificate $|f^{\mathsf T}c|^2/(f^{\mathsf T}G_E f)$.

Another exact form is

$$
L_\sigma(E,S)=2\left\|\Pi_{\operatorname{ran}(T^{-1/2}D_S^*)}
                 T^{-1/2}Qe_0\right\|_2^2 .
$$

Indeed $W_0=1$, so $W_S^{-1}c=-2\sigma D_ST^{-1}Qe_0$. The factors $W_S$ disappear from this projection, but the weights on the whole of $V$ remain.

## Reduction to a form on the zero-background projection

Suppose $\|E\|_\infty\le\rho<1$, and define

$$
\kappa=\frac{1+\rho}{1-\rho},\qquad A=I-\sigma K,\qquad G=A_{SS},
\qquad x=X_E e_0,\qquad \ell=Ex.
$$

The zero-background extension operator on $V$ is $T_0=I_V+J|_V$, and $\kappa^{-1}T_0\preceq T\preceq\kappa T_0$. From (1) at $E=0$, and then at $E$, it follows that

$$\kappa^{-1}G\preceq W_S^{-1}G_E W_S^{-1}\preceq\kappa G.$$

All three matrices in this comparison have the same kernel. The column identity is

$$
a:=W_S^{-1}c=[(I-\sigma E)x]_S
=[K e_0+(K-\sigma I)\ell]_S=-\sigma[A(e_0+\ell)]_S . \tag{2}
$$

The first equality uses $E_0=0$ and $W^{-1}M=I-\sigma E$; the second uses $x=K(e_0+\ell)$; the last uses $0\notin S$. Thus the correct zero-background data include the feedback $\ell$. Let $f_j$ be an orthonormal eigenbasis of $G$ with eigenvalues $\lambda_j$, extended by zero off $S$, and set

$$
\psi_j=\frac{A^{1/2}f_j}{\sqrt{\lambda_j}}\quad(\lambda_j>0),\qquad
C_E=\sum_{\lambda_j>0}|\langle\psi_j,A^{1/2}(e_0+\ell)\rangle|^2.
$$

The $\psi_j$ are orthonormal because their Gram matrix before dividing by $\sqrt{\lambda_j}$ is diagonal with entries $\lambda_j$. If $\lambda_j=0$ then $A^{1/2}f_j=0$, so the data in (2) pair to zero on that mode. The variational inverse or inversion on the common range gives

$$
\boxed{\qquad \kappa^{-1} C_E\le L_\sigma(E,S)\le\kappa C_E,\qquad C_0=L_\sigma(0,S).\qquad} \tag{3}
$$

This tests the reference with a compression of $K$ and a single reference inverse column. An error $\epsilon$ in $\ell$ in full $\ell_2$ changes $\sqrt{C_E}$ by at most $\sqrt2\,\epsilon$, regardless of the positive eigenvalues of $G$. For example $x^{[N]}=\sum_{k=0}^N(KE)^kKe_0$ has error at most $\rho^{N+1}/(1-\rho)$; use $\ell^{[N]}=Ex^{[N]}$ in (2) and (3). A computed approximate $\widehat x$ can instead use $\|x-\widehat x\|_2\le\|Ke_0+KE\widehat x-\widehat x\|_2/(1-\rho)$. These errors are controlled before restriction to $S$, where an error bound in ordinary $\ell_2(S)$ would need division by the square root of a gap.

## Fixed depth: ordinary column mass and the normalized small-gap modes

Let $q$ be an eligible field order, $n=(q-1)/2$, and $\mathcal F$ the unitary Fourier transform from positions in the square subgroup to frequencies. Then $\mathcal F^{-1}A\mathcal F$ multiplies by $1-\sigma s$, $s(a)=\chi(1-a)$, with $s(1)=0$. In particular $\mathcal F^{-1}j=\delta_1$. For $0<\eta<1$ define the following quantities using only the zero-background compression:

$$
\begin{aligned}
C_{0,<\eta}&=\sum_{0<\lambda_j<\eta}|\langle\psi_j,A^{1/2}e_0\rangle|^2,\\
I_\eta&=\sum_{0<\lambda_j<\eta}|\langle j,\psi_j\rangle|^2
       =\sum_{0<\lambda_j<\eta}\frac{|\langle j,f_j\rangle|^2}{\lambda_j},\\
\Lambda_\eta&=\left(\sum_{0<\lambda_j<\eta}
     \|\mathbf1_{\{a\ne1\}}\,\mathcal F^{-1}\psi_j\|_1^2\right)^{1/2}.
\end{aligned} \tag{4}
$$

The second equality uses $A^{1/2}j=j$. The last test can use any orthonormal eigenbasis; the estimate holds in the chosen basis. It can also be replaced by the operator norm from positional $\ell_\infty$ off $1$ to the $\ell_2$ norm of the vector of low-mode pairings, which is basis-independent.

Take the bulk activation $E_i=Y_i/\sqrt{Y_i^2+4\tau}$ with $Y=\sqrt n\,v^{(t)}$ or $\sqrt n\,z_t$, at fixed $\tau>0$ and depth $t$. Clip by the odd map to $[-\rho,\rho]$, and strip the mark. One can also zero it on any $o(n)$ set (which need not be $S$). For the unclipped fixed-depth activation the [uniform fixed-depth draft](uniform-fixed-depth.md) supplies a $\rho<1$ depending on $t,\tau$. For each $\epsilon>0$ there are constants $B_\epsilon,H_\epsilon$ independent of $q$ such that for all large $q$:

* $x$ has an $\ell_2$ approximant within $\epsilon$ with pointwise bound $B_\epsilon/\sqrt n$.
* Writing $\alpha=\langle j,\ell\rangle$, the positional field $\mathcal F^{-1}(\ell-\alpha j)$ has an $\ell_2$ approximant within $\epsilon$, zero at $1$ and bounded by $H_\epsilon/\sqrt q$ elsewhere.

Here is the arithmetic input and the approximation argument. Use the [fixed-expression trace rules](iteration-parity.md#uniform-fixed-expression-trace-estimates): a fixed even product of bounded negative Mellin fields is a positive expression up to bounded errors on boundedly many characters; application of $K$ gives a bounded negative expression up to a vanishing error in normalized $\ell_2$. For the positional statement, Fourier inversion of the even product is the bounded-complexity trace on the square subgroup plus the Fourier transform of the exceptional error. Away from $1$ its trace is $O(q^{-1/2})$ by the weight bound, and the exceptional term is $O(1/n)$ there. These estimates apply to the unitary inverse Fourier transform of the product divided by $\sqrt n$. The possible punctual part is at $1$.

Approximate the scaled iterate by bounded negative fields in normalized $\ell_2$, using the fixed-depth argument. The clipped activation is an odd Lipschitz function; approximate it on the bounded approximant's range by an odd polynomial. Masking $o(n)$ bounded entries contributes $o(1)$ in normalized $\ell_2$. In the Neumann series, start from the negative field $\sqrt n\,Ke_0$. If the current scaled term is approximated by a bounded sum of negative fields, its product with the activation is approximated by an *even* polynomial in negative fields. In the product error first use the boundedness of the actual activation for the column error, then boundedness of the column approximant for the activation error. The result after applying $K$ is again approximable by bounded negative fields. This argument uses even products; it does not require an odd polynomial of negative fields to itself be a sum of negative-type traces. Truncate with the Neumann bound above to get the first assertion. Multiplying the scaled column by the activation once more gives even expressions, so the positional estimate off $1$ follows by Parseval, the trace estimate and restriction off $1$. This proves both assertions with one accuracy chosen before the field limit. The constants may grow with depth and the demanded accuracy.

With these constants, a quantitative bound is

$$
\frac{\sqrt{L_\sigma(E,S)}}{\sqrt\kappa}
\ \le\
\frac{1+\rho}{\sqrt\eta}\big(B_\epsilon\sqrt{|S|/n}+\epsilon\big)
+\sqrt{C_{0,<\eta}}+|\alpha|\sqrt{I_\eta}
+\sqrt2\left(\epsilon+\frac{H_\epsilon}{\sqrt q}\Lambda_\eta\right).
\tag{5}
$$

On the modes $\lambda_j\ge\eta$, (2) and Parseval on $S$ bound the contribution to $\sqrt{C_E}$ by $\|[(I-\sigma E)x]_S\|_2/\sqrt\eta$. On the modes $0<\lambda_j<\eta$, decompose $A^{1/2}(e_0+\ell)$ into $A^{1/2}e_0$, $\alpha j$, and $A^{1/2}(\ell-\alpha j)$. Pair the last term against the orthonormal $\psi_j$. The positional approximation error costs at most $\sqrt2\,\epsilon$ in their joint $\ell_2$ norm by Bessel, and its bounded approximation costs at most $\sqrt2\,H_\epsilon\Lambda_\eta/\sqrt q$ by spatial $\ell_1$-$\ell_\infty$ duality. This proves (5). The same calculation and the reverse triangle inequality give

$$
\sqrt{\kappa L_\sigma(E,S)}\ \ge\
\left[|\alpha|\sqrt{I_\eta}-\sqrt{C_{0,<\eta}}
-\sqrt2\left(\epsilon+\frac{H_\epsilon}{\sqrt q}\Lambda_\eta\right)\right]_+ . \tag{6}
$$

Thus a sufficient field-first test, at some fixed $\eta$, is $|S|=o(n)$, $C_{0,<\eta}=o(1)$, $\alpha^2 I_\eta=o(1)$ and $\Lambda_\eta=o(\sqrt q)$. Here $|\alpha|\le\rho/(1-\rho)$; $I_\eta=o(1)$ suffices for the constant term. No lower bound on any of the positive $\lambda_j<\eta$ is required. The last test is automatic if there are boundedly many low modes and their positional lifts off $1$ are supported, up to $o(1)$ in $\ell_2$, on sets of size $o(q)$. At $|S|=O(\sqrt q)$ the number bound is automatic:

$$
\#\{j:0<\lambda_j<\eta\}
\le \frac{\|K_{SS}\|_{\rm F}^2}{(1-\eta)^2}
\le \frac{q|S|^2}{n^2(1-\eta)^2}.
$$

The spatial condition concerns the **normalized defect** $\mathcal F^{-1}A^{1/2}f_j/\sqrt{\lambda_j}$, so a support approximation for $\mathcal F^{-1}f_j$ alone without a rate at scale $\sqrt{\lambda_j}$ does not imply it. If $|S|=o(\sqrt q)$ there are no low modes at fixed $\eta<1$ for large $q$, by the entry bound. In all these tests the marked value of the reference itself is $o(1)$: it equals $x_0$, of absolute value at most $B_\epsilon/\sqrt n+\epsilon$.

## Square order: the zero-reference test can miss a constant

Let $q=r^2$, $r$ an odd prime, $B=\mathbb F_r^\times$ of order $b=r-1$ in the positional square subgroup, and $B^\perp$ its frequency annihilator of size $m=n/b$. Set $S=h+B^\perp$ with $h\notin B^\perp$, for instance the nontrivial coset of order two in the quotient so that $S=-S$. Take $\sigma=+1$.

The inverse Fourier images of vectors on $S$ are one-dimensional on each positional coset of $B$, spanned by the restriction of the phase of $h$ to that coset. This follows by character orthogonality for $B^\perp$ on the quotient. Thus the compression of $K$ has one scalar per position coset, namely the average of $s$ there. On $B$ the average is $1-1/b$ since $s=1$ on $B\setminus\{1\}$. Off $B$ the average is $-2/b$: for $c\notin B$, $c$ a square, sum $\chi_r(N(1-ct))$ over $t\in\mathbb F_r^\times$. The norm polynomial has nonzero discriminant and square leading coefficient, so the complete quadratic character sum is $-1$; removing $t=0$ subtracts one. These are also the scalar blocks in the [subfield computation](square-order-control.md#the-fourier-frequencies-carrying-the-discrepancy).

For $\eta=1/2$ the only low eigenvalue of $G$ is $1/b$, with $f=\mathbf1_S/\sqrt m$. In position, $f$ has modulus $1/\sqrt b$ on $B$, and its value at $1$ is $1/\sqrt b$. Application of $A^{1/2}$ there kills every point but $1$. Therefore $\psi=j$ exactly, $I_\eta=1$, $\Lambda_\eta=0$, and $C_{0,<\eta}=1/n$. All other gaps are $1+2/b$, so $L_+(0,S)\le 1/n+qm/n^2=O(1/r)$. In contrast, at any strict bounded $E$ the same low contribution to $C_E$ is exactly

$$|\langle j,A^{1/2}(e_0+\ell)\rangle|^2=(1/\sqrt n+\alpha)^2.$$

For a concrete reference use the first Picard iterate at $\tau=1$, clipped at $\rho=1/16$ and zeroed on $S\cup\{0\}$. Put $y=\sqrt n\,Ke_0$ and $u=1-1/\sqrt n$. Off the zeroed entries, $E_i$ is the clipping of $u y_i/\sqrt{u^2y_i^2+1}$. We have $|y_i|\le2$, $u\ge1/2$ for large $r$, and consequently $E_i y_i\ge(\rho/2)y_i^2$: the unclipped ratio to $y_i$ is at least $1/(2\sqrt5)$ and the ratio after reaching the cap is at least $\rho/2$. Since $n^{-1}\|y\|_2^2=1-1/n$ and $m=O(\sqrt n)$,

$$
\alpha
=\frac1n\sum_i E_i y_i+\langle j,E(x-Ke_0)\rangle
\ \ge\ \frac\rho2(1-o(1))-\frac{\rho^2}{1-\rho}
\ \ge\ \frac\rho3
$$

for large $r$. The error bound uses the Neumann series. Thus $L_+(E,S)\ge\kappa^{-1}\rho^2/9$ for all sufficiently large $r$, although $L_+(0,S)\to0$. In fact $C_E=(1/\sqrt n+\alpha)^2+o(1)$ by the ordinary restricted-column bound for the rest of the modes. This example uses an actual first-depth reference and a prescribed exceptional set; it makes no stationary assumption on that set. The obstruction is in the constant direction of the opposite-sector extension. The comparison already fails for bounded references even after zeroing them on the tested set.

### A punctured coset with a small marked form and no uniform gap

Use the same reference and write $S_0=h+B^\perp$ for the full coset just tested. Remove an arbitrary set $U\subset S_0$ of size $1\ll k\ll m$, and test $S'=S_0\setminus U$, of size $m'=m-k$. The full-coset compression of $A$ equals $(1+2/b)I-(r/n)\mathbf1\mathbf1^{\mathsf T}$ by the two eigenvalues just computed. The restriction to $S'$ still has a single small gap, now $\delta=1/b+rk/n\to0$, and $m'\delta\asymp k$. Since $E_{S'}=0$, (3)'s underlying Loewner comparison implies $\lambda_{\min}(I_{S'}-R_{S'S'})\le\kappa\delta\to0$ as well.

Nevertheless the low-mode contribution to $\sqrt{C_E}$ for $S'$ tends to zero. In fact, using $a$ from (2) on the full coset, the exact full-coset low mode gives $|\sum_{S_0}a_i|=\sqrt{m/b}|1/\sqrt n+\alpha|=O_\rho(1)$. Therefore the new low-mode contribution is bounded by

$$
\frac{|\sum_{S'}a_i|}{\sqrt{m'\delta}}
\le \frac{O_\rho(1)+\sqrt k\,\|a_U\|_2}{\sqrt{m'\delta}}=o(1).
$$

The last step uses the ordinary restricted-column bound, since $|U|=o(n)$. The contribution of the remaining modes also tends to zero by that bound on $S'$. Thus $L_+(E,S')=o(1)$, even though the actual reference compression has an eigenvalue tending to the endpoint. If an even exceptional set is desired, remove $U$ in inversion pairs.

## Checks and what remains

Dense floating-point checks at $q=41,73,7^2,11^2$ used both signs and 96 prescribed reference/set pairs, including 48 with singular compression. They used a direct solve for $X_E$, diagonalization for the opposite-sector basis, and independent minimum-energy and compression evaluations of (1). The maximum discrepancies in the full identity, (2), the energy value, and the extension constraint were respectively $2.7,1.1,3.2,2.5$ times $10^{-15}$; all comparisons (3) held within $10^{-11}$. For the square example, a 16-term FFT Neumann sum at $r=389$ gave $L_+(0,S)\simeq0.0027203$, $\alpha\simeq0.0560670$ and $C_E\simeq0.0062801$, with inverse residual below $6\cdot10^{-17}$. These are checks; the limit separation follows from the bounds above.

For the stationary application one still needs a reference and sets $S$ for which the signed relative hyperbolic excess is small outside $S$, as well as the extension or overlap estimate on $S$. Formula (5) gives one sufficient prime-field target beyond control of ordinary column mass: bound the constant and off-identity positional overlaps of the normalized low-gap modes, or directly produce a low-energy extension in (1). Fixed-depth parity alone does not give this on the true exceptional sets.
