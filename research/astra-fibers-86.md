# Signed displacement-fiber cancellation on quadratic images of intermediate modes

Let $q,r$ be any actual complementary optimal probabilities at the same mark, of signs $s,-s$. Fix $0<\tau<1$. For either endpoint choose **any** subset $S_\sigma$ of its nonidentity positional coefficients of modulus at least $\tau$, in sector $\sigma$. The map
\[
                       T(x)=(1-2x)^2
\]
transports this subset into the same sector. Drop a zero image. Uniformly through the eligible primes, the actual marked cubic on the image is
\[
 pE(f_{T(S_\sigma)}UV)
      =\frac{\sigma |S_\sigma|}{\sqrt p}+O_\tau(p^{-1/1056}).                  \tag{1}
\]
Here $f_L=\operatorname{Re}k_L$ is the real, even partial Jacobi column, so sets need not be inversion-stable. In particular two opposite heads of equal cardinality have a union of image masks with signed cubic $O_\tau(p^{-1/1056})$. This is a bound for the true signed correlation after centering each distinct-center displacement, with both axis prices retained in (9) below. Large individual images can contribute order one with opposite signs. The argument allows negative or complex intermediate coefficients of ordinary theta.

## Actual conditional law at each positional output

Use $Q=\mathbb F_p^{\times 2}$, $G=\widehat Q$ written additively, $n=|Q|=(p-1)/2$, $d(x)=\chi(1-x)$, $E=n^{-1}\sum_{i\in G}$, and $k(i)=p^{-1/2}\sum_{x\in Q}d(x)i(x)$. Write $F(x)=\sum_iq_i i(x)$, $R(x)=\sum_ir_i i(x)$, $a=q_0$, $b=r_0$, $U=(nq-1)/\sqrt p$, $V=(nr-1)/\sqrt p$. The optimal point caps give $a,b\ll p^{-1/2}$, $nab=1$, and $nq_ir_i=\mathbf1_{i=0}$. Extending $F,R$ by zero off $Q$ is convenient for affine maps. The functions on $Q$ need not be real. [Endpoint conditions and marked cubic](astra-complement-84.md)

The conditional displacement probability gives, for every $t\in G$ and $x\in Q$,
\[
 M_x(t)=n\sum_iq_i r_{i+t}i(x)
         =\sum_{v\in Q} F(x/v)R(v)\,\overline{t(v)},\qquad |M_x(t)|\le1,\quad M_x(0)=1.
\]
Expand $r_{i+t}$ by multiplicative Fourier inversion. Its normalizing $1/n$ cancels the prefactor. For $x\ne1$, remove the two axes $v=1,x$. The remaining exact Fourier support is contained in $V_x=\{v:d(v)=-s,\ d(x/v)=s\}$ where the displacement multiplier $d(v)d(x/v)$ equals $-1$. In particular,
\[
 \sum_{v\in V_x}F(x/v)R(v)=1-F(x)-R(x),\qquad
 \sum_{v\in V_x}|F(x/v)R(v)|^2\le1-|F(x)|^2-|R(x)|^2.                  \tag{2}
\]
The inequality follows by Parseval in $t$. Every pair of input heads above $\tau$ has at most $\tau^{-4}$ joint decompositions of any fixed output $x\ne1$. The sign of the weighted sum in (2) remains to be estimated. By $v\leftrightarrow x/v$,
\[
 |V_x|=\tfrac14[n-2-(d*d)(x)]=n/4+O(\sqrt p).
\]
Here $d*d$ is the ordinary counting convolution on $Q$. Its nonidentity values are $(\sum_u\chi(u(u-1)(u-x))-2)/2$ by expanding the square indicator, and the cubic character sum has absolute value at most $2\sqrt p$. Thus replacing the signed weights on this joint sector by its size loses the output information in (2). [Legendre sum evaluation](parallel-witness-6.md#the-four-coordinates-have-independent-limiting-support)

## A prime-field incidence bound for the intermediate spectra

For either probability $w$ with characteristic function $W$, let $H_w(\tau)=\{x\in Q:|W(x)|\ge\tau\}$. In fact the following input uses only positivity, normalization and the point cap $n\|w\|_\infty\le C\sqrt p$. Parseval gives
\[
 |H_w(\tau)|\le \tau^{-2}n\sum_iw_i^2\le C\tau^{-2}\sqrt p .
\]
For **every** subset $X\subset H_w(\tau)$, choose complex units $e_x$ so $e_xW(x)=|W(x)|$. Jensen and character orthogonality give the hereditary bound on multiplicative energy
\[
 (\tau |X|)^4\le \sum_i w_i\left|\sum_{x\in X}e_x i(x)\right|^4
    \le n\|w\|_\infty E_\times(X),
 \qquad E_\times(X)=\#\{x_1x_2=x_3x_4:x_j\in X\}.                       \tag{3}
\]
The last inequality expands the fourth power after replacing the probability by its point cap and bounds each surviving phase in modulus by one.

Fix $L(x)=c x+h$, $ch\ne0$, and let $P(x)=L(x)^e$ with $e=1$ or $2$. For any two of the endpoint probabilities $w,z$, including the same one twice, uniformly in $c,h$,
\[
 \#\{x\in H_w(\tau):P(x)\in H_z(\eta)\}
       \ll_{\tau,C}\sqrt p\min(1,\eta^{-2}p^{-1/528}),\qquad 0<\eta\le1.        \tag{4}
\]
To prove this, put $N=\sqrt p$ and start with a subset $X$ of the displayed intersection of size $m=\min(\lfloor N\rfloor,\#\text{intersection})$, $\nu=m/N$. The empty case is immediate. Its energy fraction by (3) is $\gg_{\tau,C}\nu$. The polynomial Balog–Szemerédi–Gowers theorem gives $X_1\subset X$ with
\[
 |X_1|\gg_{\tau,C}\nu^2 N,\qquad |X_1X_1|\ll_{\tau,C}\nu^{-5}|X_1|.
\]
The version used gives size $\gg\kappa |X|$ and doubling $\ll\kappa^{-5}$ when energy is at least $\kappa |X|^3$. Put $Y_1=P(X_1)$, which has size at least $|X_1|/2$. Apply (3) and the same theorem to $Y_1\subset H_z(\eta)$. Its energy fraction is at least $c_C\eta^4|Y_1|/N\gg_{\tau,C}\eta^4\nu^2$. Choose one preimage in $X_1$ of each member of the resulting subset $Y_2$, giving $X_2$ with
\[
 |X_2|=|Y_2|\gg_C\eta^4 |Y_1|^2/N\gg_{\tau,C}\eta^4\nu^4N,\qquad
 |Y_2Y_2|\ll_{\tau,C}\eta^{-20}\nu^{-10}|Y_2|.
\]
The multiplicative doubling of $X_2$ is at most $O_{\tau,C}(\eta^{-4}\nu^{-7})$, using $|X_1X_1|$ and $|X_1|/|X_2|\ll_C N/(\eta^4|X_1|)$. Moreover $|L(X_2)L(X_2)|\le2|Y_2Y_2|$, since raising to the first or second power has fibers of size at most two on nonzero field elements. Zhelezov's prime-field shift theorem with $d=h/c\ne0$, $A=B=X_2$, $C'=X_2+d$, now gives
\[
 |X_2|^{1/26}\ll \max(|X_2X_2|,|L(X_2)L(X_2)|)/|X_2|
                 \ll_{\tau,C}\eta^{-20}\nu^{-10}.
\]
Its size hypothesis $|X_2|\le\sqrt p$ holds by the initial cutoff. Scaling by $c$ does not affect product cardinality. Substitution gives $\nu^{264}\ll_{\tau,C}\eta^{-524}/N$, hence $\nu\ll_{\tau,C}\eta^{-131/66}p^{-1/528}$. If the initial cutoff occurred, then $\nu\gg1$, and the trivial head bound $O_{\tau,C}(N)$ restores the full intersection with an adjusted constant. This gives (4) also when $\eta$ shrinks. Both the shift theorem and the stated BSG form appear as Theorems 1 and 6 in [D. Zhelezov, *On additive shifts of multiplicative almost-subgroups in finite fields*](https://arxiv.org/pdf/1507.05548).

Integrating (4) in $0<\eta<1$ gives the actual absolute-price estimate, uniformly over arbitrary subsets $S\subset H_w(\tau)$,
\[
 \sum_{y\in P(S)\cap Q}|Z(y)|
 \le \sum_{x\in S}|Z(P(x))|\ll_{\tau,C}\sqrt p\,p^{-1/1056}.             \tag{5}
\]
Indeed the integral of $\min(1,A\eta^{-2})$ is at most $2\sqrt A$ for $0<A\le1$. The independent use of (3) on a subset of the *second* actual head is essential.

## From the quadratic image to the true fiber price

For $x\in Q\setminus\{1\}$, $1-T(x)=4x(1-x)$. Thus $T(x)\in Q$ has the same $d$-sign whenever $x\ne1/2$. Its only possible collision is $x,1-x$. For $d(x)=-1$ the latter is outside $Q$, and $1/2$ cannot be in that sector of $Q$. The finite map on $D_-$ is consequently a permutation. On either actual $\tau$-head, (4) with $L(x)=1-x,e=1,z=w,\eta=\tau$ bounds the input collision set by $O_\tau(p^{1/2-1/528})$. With a zero image removed this gives
\[
 |T(S_\sigma)\cap Q|=|S_\sigma|+O_\tau(p^{1/2-1/528}+1).                \tag{6}
\]
Equation (5) with $L=1-2x,e=2$ bounds the sum of the absolute values of the same-sector coefficients on this image, including arbitrarily small coefficients. The opposite endpoint vanishes there by exact sector support. For every $L_0\subset Q\setminus\{1\}$ and $f_{L_0}(i)=p^{-1/2}\sum_{x\in L_0}d(x)\operatorname{Re}i(x)$, the real part of the exact output formula is
\[
 pE(f_{L_0}UV)=p^{-1/2}\sum_{x\in L_0}d(x)[1-\operatorname{Re}F(x)-\operatorname{Re}R(x)].       \tag{7}
\]
Apply (5)–(6) to (7) to get (1). In particular the difference between the marked cubic on the image and on its original head is $\sigma p^{-1/2}\sum_{x\in S_\sigma}\operatorname{Re}W(x)+O_\tau(p^{-1/1056})$. This keeps the signed intermediate input price and the deterministic output count. [Partial Jacobi column](astra-cubic-85.md#resolve-the-cubic-by-its-output-character)

For any of these real even masks $f$, put
\[
 C_f(i,j)=E_z f(z)k(z-i)k(z-j),\quad A_f(t)=E_z f(z)k(z)k(z-t),\quad
 B_f=s\sqrt p\,[a\Delta_r(f)-b\Delta_q(f)]+pab E(fk^2),
\]
where $\Delta_w(f)=w(fk)-E(fk)$. As $Ef=0$, summing $C_f(i,i+t)$ over all $i$ gives zero. The two deleted terms are $A_f(t)=A_f(-t)$. Expanding the exterior product using the sector equations gives $pE(fUV)=B_f-p\sum_{i,j\ne0}q_ir_j C_f(i,j)$. Further $q(A_f)=s\Delta_q(f)/\sqrt p, r(A_f)=-s\Delta_r(f)/\sqrt p, \sum_t A_f(t)=0$. Thus the true exterior displacement masses $d_t=1/n-ar_t-bq_{-t}+ab\mathbf1_{t=0}$ pay exactly $-2B_f/(n-2)$ for their conditional uniform means. With
\[
 Z_f=p\sum_{i,j\ne0,\ i\ne j}q_i r_j
     \left[C_f(i,j)+\frac{2A_f(j-i)}{n-2}\right],
 \qquad pE(fUV)=\frac{n}{n-2}B_f-Z_f,                                   \tag{8}
\]
take $f=f_{T(S_+)\cup T(S_-)}$ (discard zero). The images lie in different sectors, so
\[
 Z_f=\frac{n}{n-2}B_f-\frac{|S_+|-|S_-|}{\sqrt p}+O_\tau(p^{-1/1056}).   \tag{9}
\]
This keeps the original $q,r$ and the two signed one-law prices of the masked cubic. The prime step estimates the signed sum over displacements after removing the uniform mean on **each** individual displacement.

At a square order $u^2$ with $u$ an odd prime the true plus row has $F=\mathbf1_{\mathbb F_u^\times}$. Take $S=\mathbb F_u^\times\setminus\{1,1/2\}$. Its image consists of the $(u-3)/2$ nonidentity squares of the subfield and $F=1$ there. The image cubic is exactly zero by (7), whereas $|S|/u\to1$. This shows the prime distinction even with both genuine endpoints in the tested cubic. [True square endpoint](square-endpoint-uniqueness.md)

## Replay and two remaining tests

The [384-bit checker](astra-fibers-86-check.py) reconstructs true even complementary optima at $53,101,257,409,769$, and compares both ways of evaluating all 207840 conditional output/displacement coefficients with $x\ne1$. It verifies (2), the counts and sign rules, the actual image prices, and (8) by direct FFT arithmetic on every distinct displacement for both signs at threshold $1/20$. At $257$ the plus input includes 3 negative coefficients among 57, with 31 image modes. Its image cubic lies in $(1.621831375,1.621831376)$. At $769$ the minus image includes 140 modes and its distinct-center sum lies in $(4.553767006,4.553767007)$. These finite-size checks test the exact identities. The asymptotic constants come from the two theorems. [Interval records](astra-fibers-86-checks.jsonl)

1. For equally sized subsets of the opposite $\tau$-heads, write $f_{\rm rem}=k-f_{T(S_+)\cup T(S_-)}$. The original conjecture is equivalent to $Z_{f_{\rm rem}}=nB_{f_{\rm rem}}/(n-2)+o(1)$. Test this residual using (2) on the *remaining* output fibers. In particular a sequence with both fixed-threshold heads of size $o(\sqrt p)$ leaves the entire diffuse signed obstruction. The uniform joint-support count or absolute representation bound in (2) alone does not compare the two sector prices at the required scale.
2. Test whether a signed comparison of successive images holds for the surviving diffuse part. On the minus sector $T$ is a permutation, so the total sum is invariant, while (5) quantifies the first image of every fixed-threshold head. A bound on $\sum_x |W(x)W(Tx)|$ by the same $o(\sqrt p)$ scale does not follow from (5) by merely sending the threshold to zero, since there are order $p$ small coefficients. An estimate there must keep the linear signs and the opposite-sector price to reach the all-prime target.
