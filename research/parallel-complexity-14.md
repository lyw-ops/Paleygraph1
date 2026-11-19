# Moving width: a marked loss bound and a smaller Mellin budget

Put `L = log₂* q` and `T = L − log₂* L − 4`. For all sufficiently large field orders `q ≡ 1 mod 4`, and either sign, the zero-floor quadratic value satisfies

$$
\boxed{\displaystyle
 |\log M_{q,\sigma}(r)|
 \le C_B T^{-B}+\frac{2}{\sqrt{\exp(4rT)-1}}
 \qquad (0<r\le1)
}\tag{1}
$$

for every fixed integer $B\ge1$ (the threshold on $q$ can depend on $B$). In particular the values balance uniformly down to any cutoff $s_q$ with $s_q\log_2^* q\to\infty$. For example, $s_q=\sqrt{\log L}/L$ improves the order $\log L/L$ in [slow-width.md](slow-width.md). At $s_q=\log T/T$ we recover the previous $O(T^{-2})$ error by taking $B=2$. Two separate changes give (1): use all the early marked values in a contraction loss identity, and use a weighted coefficient budget with a single exponential per arithmetic step. Both work over squares as well as primes.

## 1. The loss at the mark survives contraction

Use the notation of the [zero-floor quadratic program](quadratic-theta.md). Write $d=(1-r)/(1+r)$, $v_0=0$, $v_{t+1}=dK\Phi(v_t)$, and $z=dK\Phi(z)$ for the fixed point. In ordinary Euclidean norm, $K^2=I-jj^*$, with $j=\mathbf1/\sqrt n$, and $K=K^*$. Write

$$
m=\operatorname{arsinh}(z_0/2)=-\tfrac12\log M_{q,+}(r),\qquad
m_t=\operatorname{arsinh}((v_t)_0/2),\qquad w_t=z-v_t.
$$

The marked activation is $\Phi(u)_0=\sqrt{u_0^2+4}$, with $\Phi(u)_i=|u_i|$ elsewhere. At the mark the difference of the squared input and output discrepancies is

$$
 (z_0-(v_t)_0)^2-(\Phi(z)_0-\Phi(v_t)_0)^2
 =8(\cosh(m-m_t)-1)\ge4(m-m_t)^2.
$$

For $0<d<1$ the exact identity is

$$
\begin{aligned}
\|w_t\|^2-d^{-2}\|w_{t+1}\|^2
  ={}&8(\cosh(m-m_t)-1)
 +4\sum_{i\ne0:\ z_i(v_t)_i<0}|z_i(v_t)_i|\\
 &+|\langle j,\Phi(z)-\Phi(v_t)\rangle|^2.
\end{aligned}\tag{2}
$$

Indeed $d^{-1}w_{t+1}=K(\Phi(z)-\Phi(v_t))$. The last term is precisely the norm discarded by $K$; the middle term is the coordinatewise loss from opposite bulk signs.

Multiply (2) by $d^{-2t}$ and sum for $0\le t<T$. Let $W_T=\sum_{t<T}d^{-2t}=d^2(d^{-2T}-1)/(1-d^2)$ and $\bar m_T=W_T^{-1}\sum_{t<T}d^{-2t}m_t$. Since $w_0=z$ and the terminal term is nonnegative,

$$
 |m-\bar m_T|^2
 \le \frac{\|z\|^2}{4W_T}
 =\frac{1-c(r)^2}{d^{-2T}-1},\qquad
 c(r)=\tfrac12\langle j,\Phi(z)\rangle .
\tag{3}
$$

The last equality uses $\|\Phi(z)\|^2=4+\|z\|^2$ in the fixed point equation. Equivalently the bound controls the weighted mean square $W_T^{-1}\sum_{t<T}d^{-2t}(m-m_t)^2$, including the variance of the early marks, rather than just the error of their mean. The case $r=1$ is trivial. Dropping $c(r)^2$ and using $d\le e^{-2r}$ gives the width term in (1), with reciprocity for the other sign. The usual last-iterate norm bound costs $d^T/\sqrt r$; (3) has no such prefactor as $rT$ grows.

## 2. Charge the rank and the coefficient of each term together

Here are the geometric inputs checked against the originals. [Rojas-León, §2, Theorem 5.1 and Corollaries 5.7 and 5.9](https://arxiv.org/pdf/1106.1398) give the tame interior sign rule in the quotient by Kummer objects. [Katz, Chapters 2 and 4, particularly Corollary 4.2](https://web.math.princeton.edu/~nmk/mellin331.pdf) supply the middle convolution representative, purity, and the good-character tensor evaluation. We use the deductions in [the round 13 audit](parallel-fixed-width-13.md#1-local-sign-rules-with-the-convolution-representative-specified): even negative words are positive, odd negative words lack a geometric punctual summand at $1$, and the quadratic twist of a positive word after discarding its punctual parts is negative. For $D$ the convolution dimension and $R$ the generic rank, $D$ multiplies and $R(M\star N)\le R(M)D(N)+D(M)R(N)$. The latter is the two-drop tame Euler characteristic on the generic multiplication fiber, where the two singularities are distinct. We need these inequalities for each finite word, with the ranks and lengths explicit; we do not invoke a fixed-base equidistribution limit.

Let $\mathcal A(M)$ be the two-lift average of the Mellin trace over the full character group. Write a real negative expression as $F=\operatorname{Re}\sum_i c_i\mathcal A(M_i)$ and charge the chosen expression

$$
 \mathcal W(F)=\sum_i|c_i|\big(D(M_i)+R(M_i)\big)^{3/2}.
\tag{4}
$$

Use this as a certificate for the expression, with no minimization over representations. The everywhere bound $|\mathcal A(M)|\le D(M)$ gives $\|F\|_\infty\le \mathcal W(F)$. The same weight works for the convolution words before the twist, and it is submultiplicative on words by the rank inequality. If a positive object is twisted to a negative object as in round 13, the new dimension equals its new rank, which is the old generic rank. The weight thus increases by at most $2^{3/2}$.

For a word with factors of ranks $R_i$ and dimensions $D_i$, the Mellin product agrees with the convolution trace at every character good for the direct sum of the factors. Each expanded word has at most $2\sum_i R_i$ bad full characters, from the two tame boundaries. At any bad point the error is at most $2\prod_i D_i$. This also handles conjugation by using the convolution dual at good characters. The two-lift average is a contraction from normalized full-character $\ell_2$ to normalized $\ell_2$ on $\widehat Q$. Expand a product of lift averages by averaging over all choices of quadratic Kummer twist of the factors using a single common lift, then average over that lift. All these averages have total weight one; no factor exponential in the length is needed for the lifts or for expanding real parts.

For nonzero objects $D_i\ge1$. In particular

$$
 (\prod_i D_i)\sqrt{\textstyle\sum_i R_i}
 \le (\prod_i D_i)\sqrt{\textstyle\prod_i(1+R_i)}
 \le \prod_i(D_i+R_i)^{3/2}.
$$

Thus the word error is at most $Cq^{-1/2}$ times the product of its weights in normalized $\ell_2$. For an odd word the averaged trace at $1$ is at most $q^{-1/2}$ times the word's rank: the nonpunctual stalk has weights at most $-1$. The contribution of the bad characters to the mean is bounded by their $\ell_2$ error. These estimates depend on the coefficient sum, not on the unweighted number of objects appearing in the expression.

Set $x=\sqrt n K e_0$, a real negative expression of bounded weight, with $\|x\|_{2,n}\le1$. If $F$ is negative of weight at most $U$ and $P(u)=\sum_j p_j u^j$ is real and even, set $S_U(P)=\sum_j|p_j|U^j$. The word estimates give a real negative $G$ with

$$
 \mathcal W(G)\le 2^{3/2} S_U(P),\qquad
 \|KP(F)-G\|_{2,n}\le \frac{C S_U(P)}{\sqrt q},\qquad
 |\mathbb E_{\widehat Q} xP(F)|\le\frac{C S_U(P)}{\sqrt q}.
\tag{5}
$$

In the first two bounds the constant term is killed by $K$; for the last bound it is a one-factor odd word. Linearity includes complex coefficients by taking real parts after the convolution replacement.

### One exponential per step

On $[-U,U]$ use the Fourier series of $|\cos\theta|$ written as a Chebyshev polynomial:

$$
 P_{U,H}(u)=\frac{2U}{\pi}
 +\frac{4U}{\pi}\sum_{h=1}^{H}
     \frac{(-1)^{h+1}T_{2h}(u/U)}{4h^2-1}.
$$

Here $T_j(\cos\theta)=\cos(j\theta)$. The uniform error is at most $2U/[\pi(2H+1)]$. The monomial coefficient sum of $T_j$ is bounded by $(1+\sqrt 2)^j$ from $T_{j+1}=2uT_j-T_{j-1}$, so $S_U(P_{U,H})\le C U(1+\sqrt 2)^{2H}$. Taking $H=\lceil U/\epsilon\rceil$ costs $\exp(O(U/\epsilon))$ in both the new weight and the numerator of the arithmetic error in (5).

In detail, $Y_t=\sqrt n v_t$ satisfies $Y_{t+1}=d(b_t x+K|Y_t|)$ with $0\le b_t\le2$ by [the exact separation of the mark](parallel-fixed-width-13.md#3-direct-passage-through-absolute-value-with-the-marked-input-separated). Choose $\epsilon=T^{-(B+1)}$. Use $U_0=\max(C_0,1/\epsilon)$ and $U_{t+1}=2^{C U_t^2}$, with absolute constants large enough to absorb (5), the polynomial coefficient bound and the forcing. If $U_{T+1}\le q^{1/4}$, (5), $\|K\|\le1$ and the Lipschitz estimate for $|\cdot|$ prove inductively

$$
 \|Y_t-F_t\|_{2,n}\le t(\epsilon+q^{-1/4}),\qquad
 \mathcal W(F_t)\le U_t .
$$

To test the mark at the next step use $(v_{t+1})_0=d(b_t K_{00}+\mathbb E x|Y_t|)$, with $K_{00}=-1/n$. Replace $|Y_t|$ by $P_{U_t,H}(F_t)$ in the scalar product at cost at most $t(\epsilon+q^{-1/4})+\epsilon$, and then apply the odd bound in (5). Hence all $|m_t|$ for $0\le t\le T$ are $O(T^{-B}+Tq^{-1/4}+1/n)$, uniformly in $d$.

For the depth count take $V_0=(U_0+C+2)^4$ and $V_{j+1}=2^{V_j}$. Increase $C_0$ if necessary. If $U_j\le V_j^{1/4}$, then $C U_j^2\le C\sqrt{V_j}\le V_j/4$, proving $U_{j+1}\le V_{j+1}^{1/4}$. For fixed $B$ and sufficiently large $L$, $V_0\le 2^L$, so $\log_2^* V_0\le 1+\log_2^* L$. With $T=L-\log_2^* L-4$, one has $\log_2^*V_{T+1}\le L-2$ and therefore $V_{T+1}<q$. This yields the required $U_{T+1}<q^{1/4}$ and proves (1) by (3).

## 3. Where the absolute coefficient estimate loses information

There is an exponential obstruction to improving *this particular coefficient bound* by searching for a better monomial polynomial on the same interval. If $\sup_{|u|\le U}|P(u)-|u||\le\epsilon$, then, for $U/\epsilon$ sufficiently large,

$$
 S_U(P)\ge c\epsilon\exp(c U/\epsilon).
\tag{6}
$$

To see this, truncate at degree $m$. On $[-U/2,U/2]$ the omitted tail is bounded by $2^{-m-1}S_U(P)$. A degree-$m$ approximation on that inner interval gives a trigonometric approximation to $f(\theta)=(U/2)|\sin\theta|$ by substitution. Let $F_m$ denote the Fejér kernel with Fourier coefficients $(1-|k|/m)_+$, with normalized integral one. The functional $h\mapsto h(0)-[(2F_{2m}-F_m)*h](0)$ has norm at most four and annihilates degrees at most $m$. Its value on $f$ has magnitude at least the absolute Fourier tail beyond frequency $2m$: all its nonconstant cosine coefficients are negative, and the Fourier multiplier of the subtracted kernel lies in $[0,1]$. That tail sums to $U/[\pi(2m+1)]$. Thus any inner interval error is at least $U/[4\pi(2m+1)]$. Take $m=\lfloor U/(64\pi\epsilon)\rfloor\ge1$ and use $\epsilon+2^{-m-1}S_U(P)$ as the inner interval error. This proves (6). It does not lower-bound the actual sheaf weight after collecting like constituents, or obstruct approximation in a different norm or for a particular field distribution.

The first feedback shows how much (6) can overcount. For the base object $L_0=\mathcal L_{\chi(1-a)}(1/2)[1]$, a full good character has a unitary Mellin value $u=e^{i\theta}$ since $D(L_0)=1$. The quadratic Kummer twist exchanges $L_0$ and its convolution dual (invert $a$ and use $\chi(-1)=1$). Thus the two-lift average is $\cos\theta$, and $|x|=\sqrt{q/n}|\cos\theta|$ on the good lifts. Use the Fourier series directly: the $2h$ mode is the half-sum of the evaluations of $L_0^{\star 2h}$ and its dual. These objects have dimension one and rank at most $2h$ by the rank inequality; the constant is the unit object. Apply the positive-to-negative twist to each term and call the resulting real expression $G_H$. This yields

$$
 \mathcal W(G_H)=O(\sqrt H),\qquad
 \|K|x|-G_H\|_{2,n}=O(H^{-1}+q^{-1/2}).
\tag{7}
$$

Indeed the coefficient of the $2h$ mode is $O(h^{-2})$ and its twisted weight is $O(h^{3/2})$. All those words use the same two boundary exceptions on the full character group (trivial and quadratic), which project to just the mark; the error there before applying $K$ is bounded by the absolutely summable Fourier coefficients and the all-character dimension-one bound. Formula (7) also applies to the feedback on $Y_1=2d x$ by homogeneity. The same dimension-one reduction does not apply at the next stage: the twist now produces negative objects whose dimension equals the generic rank, which is $2h$ for the hypergeometric convolution powers here ([Katz, proof of Corollary 6.3](https://web.math.princeton.edu/~nmk/mellin331.pdf)). A useful target would be an analogue of (7) with a polynomial increase in the incoming budget, stable under the next twist. Neither (6) nor (7) supplies that estimate.

## 4. Consequence at the intermediate width

At $r_p=p^{-1/3}$, the unconditional error term in (3) cannot establish balance: $r_p T\to0$. Without further control of the stationary mass or norm, this bound needs a depth $T/p^{1/3}\to\infty$, whereas the universal budget here certifies only $T\sim\log_2^*p$. Even replacing the cost recurrence by a majorant $U_{t+1}=U_t^C$ with fixed $C>1$ would make its certified depth only $O(\log\log p)$ for the same cap. Also, summing step errors by Lipschitz contraction at $r_p$ would amplify them by $O(p^{1/3})$; this particular summation would suffice with uniform per-step errors $o(p^{-1/3})$. For a bound of the form $\epsilon+S/\sqrt p$ this asks for $\epsilon=o(p^{-1/3})$ and $S=o(p^{1/6})$. These are limits of the stated bounds, not lower bounds on the complexity of the orbit. The original [ETH Problem 26](https://randomstrasse101.math.ethz.ch/posts/PaleyGraph/) concerns ordinary theta, so even balance at this intermediate width would need an endpoint comparison.

Concretely, let $A=A_\sigma(r_p)$ be the actual allowed energy on the sign with the larger ordinary theta, as in the [one-sided two-width comparison](quadratic-fourth.md#a-one-sided-single-width-criterion). **It now suffices to prove $A=o(\log_2^*p)$.** If this holds, take $s_p=\log(T/(1+A))/T$. Then $s_p\ge r_p$ eventually, $s_pT\to\infty$, and $s_p A\to0$ by $u\log(1/u)\to0$ with $u=(1+A)/T$. Also $r_p n^{1/4}\sqrt A\to0$. In fact (1) gives an error $O(T^{-B}+u^2)$ at $s_p$, so the one-sided comparison bounds $1-\sqrt{M_\sigma(0)}$ by $O(T^{-B}+u\log(1/u)+p^{-1/12}\sqrt A)$. This removes a factor $\log\log_2^*p$ from the prior sufficient bound on the allowed energy. That bound on the actual prime optimizer is still open.

## 5. Local replay

Run `.venv/bin/python research/parallel-complexity-14.py`. The [independent experiment](parallel-complexity-14.py) checks (2) and the weighted mean-square bound in (3) for three widths and depths over each of $q=5,409,31^2$. The largest floating-point identity discrepancy is below $4\cdot10^{-14}$, with stationary residual below $5\cdot10^{-14}$ in every case. At $r=0.01$ and $T=32$, the weighted mean-square root is about $0.01182$ for $409$ and $0.11667$ for $31^2$, below their mass-sensitive bounds $0.13589$ and $0.29893$. The same script constructs the full-character phases over $p=97,1009,9413$ and checks the two-lift compression and Fourier tail for $H=8,32,128$. At $p=9413,H=128$ the good-character sup error is $0.001594$ rounded up, below the bound $0.003504$ rounded up. The harmonic replay inserts the exact value at the exceptional character to isolate the Fourier truncation error; it does not compute sheaf traces at that character or test the growing-depth assertion.
