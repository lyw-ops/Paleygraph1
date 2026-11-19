# Transferring finite-time parity to the true half-angle

For [Randomstrasse101 Problem 26](https://randomstrasse101.math.ethz.ch/posts/PaleyGraph/), there is a capped test for transferring the signed moments from averaged smoothing iterates to the actual half-angle. The test is a single upper bound on a commutator across the **true** bulk cap. In particular it does not require an $\ell_2$ bound on the true stationary vector, and the bulk test can subtract the discrepancy at the mark. A second sufficient test uses the real low spectral projection of the symmetric half-angle inverse. Both are conditional through primes. The square family fails the first-moment transfer even at sufficiently small **fixed** floors.

## Capping the discrepancy before taking the time average

Use $K^2=P=I-J$, $K=K^{\mathsf T}$, $n=(q-1)/2$, $e=Pe_0$, and $g=Ke$. Fix $0<\tau\le1$, put $w_0=1,\ w_i=\tau/n$ off the mark, $\nu_i=\sqrt{w_i}$ and $W=\sum_i w_i$. Write $u=\Phi(v)$, $v=Ku$ for the stationary pair, with $\Phi_i(s)=\sqrt{s^2+4w_i}$. Thus $u=Kv+c\mathbf1$, $c=2\sqrt{W/n}$. The averaged iteration is

$$z_0=0,\qquad u_t=\Phi(z_t),\qquad z_{t+1}=(z_t+Ku_t)/2.$$

Set $\gamma_i=\operatorname{arsinh}(v_i/(2\nu_i))$, $\eta_{t,i}=\operatorname{arsinh}((z_t)_i/(2\nu_i))$. The stripped diagonals $B$ and $B_t$ have entries $\tanh(\gamma_i/2)$ and $\tanh(\eta_{t,i}/2)$ in the bulk, and zero at the mark. Write $\bar u_T=T^{-1}\sum_{t<T}u_t$, $G_T=T^{-1}\sum_{t<T}B_t$, and

$$\bar\Delta_i=\frac4T\sum_{t<T}w_i(\cosh(\gamma_i-\eta_{t,i})-1),\qquad S_t=\frac{\sum_i u_{t,i}}{\sqrt n}.$$

The [averaged norm identity](iteration-parity.md#a-criterion-involving-only-the-iterates) gives $\|z_T\|^2\le2WT$ and $T^{-1}\sum_{t<T}S_t\le2\sqrt W$. Consequently the slack $s_T=4W-c\sum_i\bar u_{T,i}$ is nonnegative. Use the projection $\Pi=\Pi_M$ onto the mark and bulk sites with $\sqrt n\,u_i\le M$, and put $R=I-\Pi$, $r_M=\operatorname{rank}R/n$. The cap is fixed during the time average and can be chosen using the exact spectrum. The following is an exact localized telescope:

$$
\sum_{i\ {\rm kept}}\bar\Delta_i
=\frac{2\langle z_T,\Pi v\rangle}{T}
+4\tau r_M-s_T-c\sum_{i\ {\rm omitted}}\bar u_{T,i}
+\langle\bar u_T,[\Pi,K]v\rangle. \tag{1}
$$

In fact $4w_i\cosh(\gamma_i-\eta_{t,i})=u_i u_{t,i}-v_i(z_t)_i$. Substitute $u=Kv+c\mathbf1$ in the kept sum. Commuting $\Pi$ past $K$ leaves $-\langle z_t-Ku_t,\Pi v\rangle$, which telescopes. The discarded bulk weights sum to $\tau r_M$. The commutator is the difference of two cross-boundary pairings, $\langle\Pi\bar u_T,KRv\rangle-\langle R\bar u_T,K\Pi v\rangle$. The two nonnegative slack terms in (1) can be retained in a finite test.

For the moments only the bulk matters. Set

$$\mathcal F_{M,T}=\langle\bar u_T,[\Pi,K]v\rangle-\bar\Delta_0.$$

Since $\tanh(x/2)$ is $1/2$-Lipschitz and $\cosh d-1\ge d^2/2$, Jensen gives the first bound below, with $\|x\|_{2,n}^2=n^{-1}\sum_i |x_i|^2$:

$$
\begin{aligned}
\|B-G_T\|_{2,n}^2
&\le \frac{\sum_{i\ {\rm kept}}\bar\Delta_i-\bar\Delta_0}{8\tau}
       +4r_M\\
&\le C_\tau\sqrt{(1+M)/T}+C/M+(\mathcal F_{M,T})_+/(8\tau).
\end{aligned} \tag{2}
$$

Here $r_M\le 2\sqrt W/M$, $\|\Pi v\|^2\le v_0^2+2M\sqrt W$, and $v_0=O(1)$ by the Jacobi entry bound. Thus one sufficient capped condition is

$$
\lim_{M\to\infty}\liminf_{T\to\infty}\limsup_{q\to\infty}
  (\mathcal F_{M,T})_+=0 . \tag{3}
$$

It also suffices to provide a sequence of depths and caps with $M\to\infty,\ M/T\to0$ and vanishing field limsup of the positive excess. For each such pair the field limit is taken at fixed $M,T,\tau$. One may sharpen either test by replacing $\mathcal F_{M,T}$ with $\mathcal F_{M,T}-s_T-c\sum_{i\ {\rm omitted}}\bar u_{T,i}$, retaining the two slack terms from (1). A direct scalar alternative is to bound the capped **bulk** sum in the first line of (2). The true tail can hold large absolute mass: the cost for discarding sites in the diagonal comparison is their *density*. Subtracting $\bar\Delta_0$ lets the test allow a nonvanishing discrepancy at the mark. Bounding the full uncapped discrepancy, as below, also controls the mark.

## From capped comparison to all fixed signed moments

For a stripped $E$ in the closed unit ball of real diagonals, write $x_j(E)=(KE)^j g$ and

$$a_k(E)=g^{\mathsf T}E(KE)^k g.$$

These are the moments $b^{\mathsf T}SC^k b$ of the [signed time expansion](parallel-sign-4.md#finite-time-versus-the-arithmetic-limit), with $C=S|E|^{1/2}K|E|^{1/2}$, $b=S|E|^{1/2}g$. The exact finite-word comparison, by replacing each diagonal factor once, is

$$a_k(B)-a_k(E)=\sum_{j=0}^k
\langle x_{k-j}(B),(B-E)x_j(E)\rangle,\qquad
|a_k(B)-a_k(E)|\le\sum_{j=0}^k\|(B-E)x_j(E)\|. \tag{4}$$

Take the [fixed-depth inertia proof draft](iteration-parity.md) as the arithmetic input. At fixed $T,\tau,j$, the scaled $\sqrt n\,x_j(G_T)$ is approximable in $\|\cdot\|_{2,n}$ by bounded negative fields (linear combinations at any prescribed accuracy). Initially it is the scaled Jacobi column. Each $B_t$ is a bounded odd Lipschitz function of $\sqrt n z_t$ on the bulk at fixed $\tau$; stripping the mark costs $O(n^{-1/2})$ in normalized $\ell_2$. The time average $G_T$ is also approximable by negative fields, using odd polynomial approximations to the $B_t$ on the ranges of the bounded approximants to the iterates. In $KE x_j(E)$, the product of the negative approximants has even parity and applying $K$ restores negative parity. For the product error, first approximate the word by a bounded field, then choose the diagonal approximation accuracy using that bound and $\|G_T\|_\infty\le1$. The normalized mean of the final product of three negative fields in $a_k$ vanishes by the odd-mean estimate. For that last step one can first replace the right word, with error at most the word error times $\|g\|$, and then the diagonal, using boundedness of both scaled test fields. In particular $a_k(G_T)\to0$ for every fixed $k,T,\tau$.

One cannot multiply the convergence in (2) by a word bound that grows with $T$. The two-limit argument that avoids this is as follows. Along the chosen depths let $\limsup_q\|B-G_T\|_{2,n}\to0$. Induct on $j$ that the true $x_j(B)$ has bounded scaled approximants at any fixed accuracy and that

$$\lim_{T}\limsup_q\|x_j(B)-x_j(G_T)\|=0$$

along those depths. The initial word $g$ is flat by the Jacobi entry bound. In the induction step bound the next difference by the current difference plus $\|(B-G_T)x_j(B)\|$. Choose a single approximant $f$ to the **true** word, with $\sqrt n\|f\|_\infty\le C_f$; the latter term is at most $2\|x_j(B)-f\|+C_f\|B-G_T\|_{2,n}$. Send $T$ to infinity and then the approximation error to zero. Choosing one sufficiently large fixed $T$ now provides a bounded scaled approximation to $x_{j+1}(B)$ from the trial word. The same argument applied to $g^{\mathsf T}B x_k(B)$ gives $a_k(B)\to0$. This is the real-diagonal transfer of [diagonal-damping.md](diagonal-damping.md#an-iterated-limit-transfer) applied to the averaged half-angle and with (1)–(3) supplying the new input. The uniformly bounded coefficients $|a_k|\le1$ then give cancellation uniformly on each bounded time interval, and at every fixed linear damping $0<d<1$.

For a single finite test one can avoid the all-orders claim. For example, use the [Krylov residual identity](parallel-half-krylov-5.md#the-signed-residual-identity) at time zero: if a polynomial $p$ is used on the true source $b$, the center for $m_B-K_{00}$ is the single polynomial $f(s)=2p(s)-(1-s)p(s)^2$ evaluated in the signed source form. With $D=I-|B|$, this gives the finite bound

$$
|m_B-K_{00}|\le
\left|\sum_k f_k a_k(E)\right|
+\sum_k |f_k|\sum_{j=0}^k \|(B-E)x_j(E)\|
+\big\|D^{-1/2}[1-(1-C)p(C)]b\big\|^2. \tag{5}
$$

Thus only the weighted finite comparison for the chosen trial resolution and its true source residual has to be small, not every true signed moment. If using the time-tail version of the certificate, the prefix and center are again scalar functions of $C$ with absolutely convergent power series at every fixed time and bounded, fixed polynomial degree. Truncation plus (4) then gives the corresponding finite comparison, independently of the saturation gap. None of these steps bounds the true weighted residual itself.

## Two sufficient tightness estimates on the true spectrum

The **full** discrepancy obeys $\sum_i\bar\Delta_i=2\langle z_T,v\rangle/T-s_T$ by (1) with $\Pi=I$. Hence a field-first vanishing upper bound on $\langle z_T,v\rangle/T$ implies (2) even without capping, and also implies the stationary marked cancellation via $|\gamma_0-T^{-1}\sum_{t<T}\eta_{t,0}|^2\le \sum_i\bar\Delta_i/2$. Here are two ways to formulate the extra tightness sufficient for this stronger route.

First put $U_i=\sqrt n\,u_i$ on the bulk, and write $Z(T)=\limsup_q\max_{i\ne0}\sqrt n\,|(z_T)_i|$, finite for each fixed $T$ under the [uniform fixed-depth draft](uniform-fixed-depth.md). In the original Euclidean pairing, split the true spectrum at $U_i=M$. The low part uses $\|\Pi v\|^2\le v_0^2+2M\sqrt W$. It follows that

$$
\limsup_q\frac{\langle z_T,v\rangle}{T}
\le C\sqrt{(1+M)/T}
+\frac{Z(T)}{T}\limsup_q \frac1n\sum_{U_i>M}U_i. \tag{6}
$$

In particular, uniform integrability of the actual bulk total spectrum, together with $Z(T)=O_\tau(T)$, suffices. A linear **upper** bound on $Z(T)$ is enough here; the bound $o(T)$ in the sup-only drift criterion was needed because that criterion used no tail information. More generally one can use the measured capped second moment instead of $O(M)$ in (6), and restrict the tail pairing to the actual signed iterate cost on $U_i>M$. For instance a uniform weak $L^2$ bound $n^{-1}\#\{U_i>x\}\le C_\tau x^{-2}$ in both $q$ and $x\ge1$, with $\log(2+Z(T))=o(T)$, suffices. Indeed the capped second moment is $O_\tau(1+\log M)$, and the first moment restricted to $U_i>M$ is $O_\tau(M^{-1})$. Take $M=\max(2,Z(T))$ in this estimate. Fixed-depth bounds alone do not give either stated growth rate for $Z(T)$. Also a bound just on the mean of $U_i$, or a bound on its tail *density* without a matching cost estimate, does not justify discarding the tail pairing.

There is a distinct version in the **real spectrum of the true symmetric operator** $H=K-PBP$ on $P\mathbb R^n$. Let $Q_\epsilon=\mathbf1_{|H|\le\epsilon}$, let $\mu$ be its source spectral measure at $e$, and put $a=u_0-2\sqrt{\tau/n}$. Use the [exact half-angle column](stationary-secant.md#the-exact-inverse-column), $v=aH^{-1}e$. The [marked spectral bound](parallel-half-modes-5.md#a-hard-signed-window) gives $\mu([-\epsilon,\epsilon])\le2\epsilon$; summing geometric shells above $\epsilon$ gives $\|(I-Q_\epsilon)v\|\le C/\sqrt\epsilon$. In particular

$$
\frac{\langle z_T,v\rangle}{T}
\le \frac{C}{\sqrt{T\epsilon}}+\frac{\langle z_T,Q_\epsilon v\rangle}{T}. \tag{7}
$$

One can choose $\epsilon=\epsilon_T\downarrow0$ with $T\epsilon_T\to\infty$ and test only the positive part of the last pairing in the field-first limit. This is a *mixed* spectral test of the true column against the actual iterate, not a count of low modes. There is also an unsigned bound in terms of the mass of the inverse column on the real window. Put $M_B=(I-B^2)^{1/2}$. On the bulk $M_{B,i}^{-2}=\tfrac12+u_i/(4\nu_i)$ so $n^{-1}\sum_i M_{B,i}^{-2}\le C_\tau$. For the shell $I_j=\{\epsilon 2^{-j-1}<|\lambda|\le\epsilon 2^{-j}\}$ let $v_j=\mathbf1_{I_j}(H)v$. The defect bound on the entire window above that shell gives $\|M_B v_j\|^2\le 2\epsilon 2^{-j}\|v_j\|^2$. Cauchy–Schwarz and the exact inverse column now give

$$
\frac{\|Q_\epsilon v\|_1}{\sqrt n}
\le \sum_{j\ge0}\frac{\|M_B^{-1}\|_{\mathrm F}}{\sqrt n}\,\|M_B v_j\|
\le C_\tau \sum_{j\ge0}\left(\int_{I_j}|\lambda|^{-1}\,d\mu\right)^{1/2}. \tag{8}
$$

For example, a bound $\int_{|\lambda|\le s}|\lambda|^{-1}d\mu\le C_\tau s^\kappa$ uniform in $q$ and $0<s\le1$, for $\kappa>0$, gives $O_\tau(\epsilon^{\kappa/2})$ in (8). When estimating the last pairing of (7) by the bulk sup, the marked term is separately $O((1+\log(1/\epsilon))/\sqrt T)$. In fact $|(Q_\epsilon v)_0|\le |v_0|+a\int_{|\lambda|>\epsilon}|\lambda|^{-1}d\mu$ and the marked linear mass bound makes each geometric shell outside the window cost $O(1)$; use $|(z_T)_0|\le\sqrt{2WT}$. Thus $Z(T)=O_\tau(T)$ and the displayed power bound suffice by taking $\epsilon_T=T^{-1/2}$. This need not require a second inverse moment; (8) uses square roots of shell energies. Bare $\mu([-\epsilon,\epsilon])=O(\epsilon)$ is insufficient, and a little-$o(1)$ bound on absolute inverse mass is not by itself a bound on the square-root sum in (8). Alternatively, estimate the mixed pairing of (7) without taking absolute inverse moments.

The capped test (3) separates the finite-time step from the signed inverse-tail estimate in [stationary-defect-tail.md](stationary-defect-tail.md#the-defect-bounds-the-marked-orbit). The stronger drift tests (6) and (7) would already control the undamped mark at that floor. This distinction matters when choosing what to prove: the capped test only needs control relative to the marked discrepancy, and does not give the late-time tail.

## Square-order test of the order of limits

Let $q=r^2$, $r$ odd prime. The [exact square value](square-order-control.md#a-square-order-comparison) gives $\vartheta(\overline H_q)=r-1$, hence at each fixed $0<\tau<1$, $\liminf_q\gamma_0\ge \tfrac12\log(2/(1+\tau))$. The fixed-depth parity input applies also to squares; their trial moments and trial marks vanish at each fixed depth in the field-first limit. In particular the full signed drift in (6)–(7) cannot vanish, by the full discrepancy and its marked term.

The actual first moment also fails at small **fixed** $\tau$; decreasing floors are unnecessary for this part. In the [square witness bound](parallel-coupling-2.md#exact-square-order-control-with-decreasing-floors) write $\ell_i=(r-\lambda_i)/(r+1)$ on the bulk and $D_i^{\rm full}=v_i/u_i$. That bound holds before the floor limit:

$$
\frac1n\sum_{i\ne0}(1+D_i^{\rm full})
\le\frac{\sqrt\tau}{s}+\frac2n\#\{i\ne0:\ell_i<s\}.
$$

The arcsine limit of $\lambda_i/r$ bounds the field limsup of the last density by $O(\sqrt s)$ for fixed small $s>0$. Take $s=\tau^{1/3}$. Since $(1+B_i)^2=(1+B_i^2)(1+D_i^{\rm full})$ on the bulk, it follows that $\limsup_q\|1+B\|_{2,n}^2\ll \tau^{1/6}$. By $\|g\|_\infty\le\sqrt q/n$ and $\|g\|^2=1-1/n$,

$$\limsup_q|a_0(B)+1|\ll\tau^{1/12}.$$

So for all sufficiently small fixed floors there is a gap in $a_0(B)-a_0(G_T)$ at every fixed $T$. In fact $|a_0(B)-a_0(G_T)|\le(q/n)\|B-G_T\|_{2,n}$. Inserting the resulting lower bound in (2) rules out (3) even after subtracting the mark. This is a fixed-floor obstruction to finite-time transfer, independently of any failure to control the late-time tail.

At decreasing floors there is a separate real inverse-spectrum obstruction. For example at $\tau=1/n,\ \epsilon=n^{-1/7}$, the [square hard-window comparison](parallel-half-modes-5.md#true-square-obstruction-including-moving-cutoffs) gives $\langle e,H^{-1}Q_\epsilon e\rangle\to4/3$, even though $\|Q_\epsilon e\|^2\le2\epsilon\to0$. The absolute inverse mass on this shrinking window is at least the absolute signed contribution. This does not assert failure of real inverse tightness at each fixed floor. The same two-limit distinction applies to spatial mass: at $\tau_q\downarrow0$ the square witness bounds $n^{-1/2}\sum_{\ell_i\ge\sqrt{\tau_q}} A_{+,i}\ll\sqrt{\tau_q}$ off the mark, where $A_+=(u+v)/2$. The complementary cap has vanishing density by the arcsine law and carries asymptotically all normalized plus mass.

## Finite replay

Using [weighted_iterate](../poisson_weights.py), [kernel_action](../smoothing.py), and the prime and square kernels, start $z_0=0$, accumulate $u_t,B_t$ and $8w_i\sinh^2((\gamma_i-\eta_{t,i})/2)$ before each averaged update, and evaluate the commutator as $\Pi K v-K\Pi v$. Eight orders $(173,13^2),(853,29^2),(9413,97^2),(37253,193^2)$ were checked at floors $0.05,0.005$, depths $32,128$, and caps $4,8,16$. The largest stationary residual was $1.0\cdot10^{-10}$; the global and capped telescopes agreed to $1.8\cdot10^{-11}$ and $3.7\cdot10^{-11}$. The first inequality of (2) and (4) through degree four held in these checks. Dense mean-zero diagonalization at the four smaller orders checked the half-angle column and (8) at widths $1/8,1/4,1/2$.

The following rows are at $\tau=0.05,\ T=128,\ M=8$. The moments shown are order zero of the signed word sequence, not $K_{00}$.

| $q$ | Omitted bulk density $r_M$ | $\|B-G_T\|_{2,n}^2$ | $\mathcal F_{M,T}$ | $a_0(B)$ | $a_0(G_T)$ |
| ---: | ---: | ---: | ---: | ---: | ---: |
| $9413$ | 0 | 0.001268 | $-9.63\cdot10^{-7}$ | 0.009216 | 0.008730 |
| $97^2$ | 0.010204 | 0.332064 | 1.064472 | −0.421487 | −0.034413 |
| $37253$ | 0 | 0.001132 | $-2.36\cdot10^{-7}$ | 0.002543 | 0.002621 |
| $193^2$ | 0.005155 | 0.385106 | 0.830546 | −0.432314 | −0.013476 |

These are floating-point diagnostics. The prime rows here have an empty omitted set at this cap. At $M=4$ the prime rows omit about $6\%$ and give $\mathcal F_{M,T}=0.599,0.563$ before subtracting the two slack terms in (1); small observed moment error need not give a small uncorrected flux at a prescribed cap. The square rows show why small omitted density does not certify (3). No estimate establishing (3) or (7) for all primes at small fixed floors is proved here.
