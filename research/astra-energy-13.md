# A current-width source test for dispersed allowed energy

**Status: a finite-field reduction and a certified source test, not a uniform prime bound.** At a single width, the actual optimizer's allowed energy is, up to a bounded additive term, the sum of a support-density term and a **centered, regularized response**. The latter admits a signed trial certificate: a bounded trial with centered compressed forbidden error of order $r^2$ bounds the actual energy. Its signs need not be checked. Actual nonnegative optimality, on the **entire current positive support**, is what makes this possible.

The response also supplies a stronger necessary arithmetic condition for blow-up: a pure opposite-sector vector has unit marked/mean contrast, vanishing centered leakage on the actual support, and **global norm $o(1/r)$**. A prescribed supported preimage is part of this condition. An exact spectral integral and a dyadic test retain energy spread over many spectral scales. A concrete abstract compression has vanishing scaled mass in its lowest spectral window but divergent response; even a critical cumulative bound $F(t)=O(t^2)$, or the improvement $F(t)=O(t^2/\log(e/t))$, is insufficient. This example is not a Paley optimizer.

The square comparison is retained at positive width. For example, at $q=61^2,r=1/(4\sqrt q)$, the numerical actual plus support has 486 bulk coordinates out of 1859, while its centered response is about 43.57. Thus the endpoint square statement that its centered term is zero does **not** carry over to the current positive support.

Starting points: [quadratic fourth-moment certificates](quadratic-fourth.md), [reciprocal QP](quadratic-theta.md), [contact projection](astra-fourth-12.md), and [quadratic path secants](parallel-quadratic-limit-9.md). The [endpoint centered sampling test](parallel-kernel-11.md) and [current/terminal support distinction](parallel-quadratic-support-9.md) are related but do not give the current-width identity below. The [ETH statement](https://randomstrasse101.math.ethz.ch/posts/PaleyGraph/) was checked on 2026-11-17; its orders are primes. No new prime character-sum theorem is claimed here.

## 1. Center the actual positive support at the measured width

Fix a field, a sign $\sigma$, and $0<r<1$. Write

\[
 N=P_{-\sigma},\quad P=P_\sigma,\quad
 Q=J+rP+r^{-1}N,
 \qquad x=A_\sigma(r),\quad y=Qx=A_{-\sigma}(r).
\]

The normalized actual pair satisfies $x,y\ge0$, $x_0=a$, $y_0=a^{-1}$, $x_i y_i=0$ off zero, and $j^Tx=j^Ty=c\le1$. Put

\[
 I=\{i\ne0:x_i>0\},\quad m=|I|,\quad
 L=c\sqrt n-a,\quad \mu=L/m,\quad
 v=x_I-\mu\mathbf1_I,\quad D=\|v\|^2.
 \tag{1}
\]

For now $m>0$. Let $E_I$ extend by zero, let $\Pi=I_m-\mathbf1_I\mathbf1_I^T/m$, and work on $W=\mathbf1_I^\perp$. Define

\[
 C=(\Pi E_I^T N E_I\Pi)|_W,\quad
 z=a e_0+\mu E_I\mathbf1_I,\quad
 f=-\Pi E_I^T Nz,\quad
 \eta=\frac{r^2}{1-r^2}.
 \tag{2}
\]

Thus $0\le C\le I_W$. The two coefficients in $f$, including their cancellation, must be retained.

**Current-width identity.** With no assumption about support at other widths,

\[
 \boxed{(C+\eta I_W)v=f.} \tag{3}
\]

Indeed,

\[
 Q=rI+(r^{-1}-r)N+(1-r)J.
\]

On $I$, actual complementarity gives $(Qx)_I=0$. Project by $\Pi$, which kills $Jx$ and the constant part of $x_I$, and divide by $r^{-1}-r$. This proves (3). Equivalently, $v$ is the unique signed minimizer on $W$ of

\[
 \|N(z+E_I w)\|^2+\eta\|w\|^2. \tag{4}
\]

To explain the role of nonnegativity: every direction supported on $I$, with zero sum and zero root, can be followed for sufficiently small steps in **both** directions from $x$. Its first variation must therefore vanish. The signed minimizer in (4) is identified by these actual first-order equations. A signed competitor in (4) need not itself be a feasible nonnegative QP trial.

There is no forcing on the kernel:

\[
 f\perp\ker C,\qquad v\perp\ker C. \tag{5}
\]

For $w\in\ker C\subset W$, $0=w^TCw=\|NE_Iw\|^2$, so $w^Tf=-\langle NE_Iw,z\rangle=0$. Equation (3) then proves the assertion about $v$. This is exact and uses no numerical eigenvalue threshold.

Let $A=\|Px\|^2$ be the requested allowed energy and $B=\|Ny\|^2$. Parseval and $Nx=rNy$ give

\[
 \boxed{A=a^2+\frac{L^2}{m}+D-c^2-r^2B.} \tag{6}
\]

Also $r(A+B)=1-c^2\le1$, so

\[
 \frac{L^2}{m}+D-1-r\le A
 \le a^2+\frac{L^2}{m}+D. \tag{7}
\]

The Jacobi entry estimate bounds $a$ above and away from zero uniformly, as in the preceding QP notes. Therefore, along any sequence $r\to0$,

\[
 \boxed{A=O(1)\quad\Longleftrightarrow\quad L^2/m+D=O(1).} \tag{8}
\]

This is an exact current-width counterpart of the endpoint density/centering split. Positive support density suffices to bound $L^2/m$, since $L\le\sqrt n$, but is not required: the sharper quantity is $L^2/m$. If $m=0$, then $x=ae_0$ and $A\le a^2=O(1)$. If $m=1$, $W=\{0\}$ and $D=0$.

## 2. One signed arithmetic source certificate

For **any** $h\in W$, define its compressed source error

\[
 e=f-Ch=-\Pi E_I^TN(z+E_Ih).
\]

Equation (3) gives

\[
 v=(C+\eta I)^{-1}Ch+(C+\eta I)^{-1}e.
\]

Both operators have known norms: the first is at most one, and the second is at most $\eta^{-1}$. Hence

\[
 \boxed{
 \sqrt D\le\|h\|+\frac{\|\Pi E_I^TN(z+E_Ih)\|}{\eta}.}
 \tag{9}
\]

No positivity of $h$ or $z+E_Ih$, no spectral gap, and no endpoint solve is needed. In particular, the following **single-width arithmetic target** suffices on the larger-theta sign:

\[
 \frac{L_p^2}{m_p}=O(1),\qquad
 \|h_p\|=O(1),\qquad
 \|\Pi_p E_{I_p}^TN_p(z_p+E_{I_p}h_p)\|=O(r_p^2).
 \tag{10}
\]

Take $r_p=o(n^{-1/4})$, for example $p^{-1/3}$. Then (7), (9) give exactly the bounded allowed energy needed by the [one-width comparison](quadratic-fourth.md#a-one-sided-single-width-criterion). The [fixed-width proof](parallel-fixed-width-13.md) supplies its other input. At $r=p^{-1/3}$, the required compressed error is $O(p^{-2/3})$. The stronger power here is for the compressed source residual; the nonlinear fixed-point residual in that note has a different estimate.

This is also a necessary condition up to a factor two in the norm bound. Define

\[
 \mathcal K_\eta(f)=\inf_{h\in W}
       \left(\|h\|+\eta^{-1}\|f-Ch\|\right).
\]

Choosing $h=v$ in (3), and using (9), proves

\[
 \boxed{\sqrt D\le\mathcal K_\eta(f)\le2\sqrt D.} \tag{11}
\]

Thus a dispersed blow-up on a sequence where $L^2/m$ stays bounded forces failure of **every** bounded signed source approximation (10), on the actual full support. This is more specific than a small unweighted compressed eigenvalue or failure of rank. Restricting the error test to an arbitrary dense subset of $I$ is not justified.

For an approximate source $\widetilde f$, the certified version of (9) adds $\|f-\widetilde f\|/\eta$ to its right side. If only $a,\mu$ are approximated, the elementary bound is

\[
 \|f-\widetilde f\|\le |a-\widetilde a|+
                         \sqrt m\,|\mu-\widetilde\mu|.
 \tag{12}
\]

Actual support identification is still a separate requirement. A small residual does not certify which coordinates are strictly positive.

### Blow-up forces a globally controlled opposite-sector sampling failure

There is a useful dual necessary condition, with an additional global norm restriction that is absent from a bare rank or centered leakage test. Suppose $D>0$, and define

\[
 w=\frac{(C+\eta I)^{-1}v}{D}\in W,\qquad
 d=NE_Iw\in\operatorname{ran}N.
\]

Then, exactly,

\[
 \begin{aligned}
 -a d_0-\mu\sum_{i\in I}d_i&=f^Tw=1,\\
 \|\Pi d_I\|=\|Cw\|&\le D^{-1/2},\\
 \eta\|w\|&\le D^{-1/2},\\
 \sqrt\eta\,\|d\|&\le\frac1{2\sqrt D}.
 \end{aligned} \tag{12a}
\]

The first equality follows from $f=(C+\eta I)v$. For the next two, $C(C+\eta I)^{-1}$ and $\eta(C+\eta I)^{-1}$ are contractions. Finally,

\[
 \|d\|^2=w^TCw
 =D^{-2}v^T(C+\eta I)^{-1}C(C+\eta I)^{-1}v
 \le\frac1{4\eta D},
\]

using $\lambda/(\lambda+\eta)^2\le1/(4\eta)$. Thus a divergent centered energy at $r=p^{-1/3}$ forces a pure opposite direction with unit displayed contrast, centered leakage $o(1)$, and global norm $o(p^{1/3})$. It is not enough to construct an opposite direction with small samples but uncontrolled values elsewhere. The displayed contrast includes the sample mean; it must not be silently replaced by a unit root condition.

There is a finite convex test retaining the supported preimage. Set

\[
 \varepsilon_I=\inf_{\substack{w\in W\\ f^Tw=1}}
                \max\{\|Cw\|,\eta\|w\|\}.
\]

Both constraints in the maximum are Euclidean norms, so this is directly testable by a second-order cone program with the actual arithmetic compression. The preceding witness and Cauchy--Schwarz give

\[
 \boxed{\frac1{2\sqrt D}\le\varepsilon_I\le\frac1{\sqrt D}.} \tag{12b}
\]

For the lower bound use $1=f^Tw=v^TCw+\eta v^Tw\le2\sqrt D\max(\|Cw\|,\eta\|w\|)$. Hence $D\to\infty$ is equivalent to $\varepsilon_I\to0$. When $L^2/m$ is bounded, failure of the desired allowed-energy bound necessarily produces this quantitatively regularized sampling failure on the actual support. This is a test of the full centered response, not just its largest individual spectral contribution.

## 3. A multiscale condition that does not discard dispersed energy

Let $E_C$ be the spectral resolution on $W$, and set

\[
 F(t)=\|E_C([0,t])f\|^2,\quad 0\le t\le1.
\]

By (5), $F(0)=0$. Equation (3) and integration by parts yield the exact formulas

\[
 \boxed{
 D=\int_{(0,1]}\frac{dF(t)}{(t+\eta)^2}
  =\frac{F(1)}{(1+\eta)^2}
       +2\int_0^1\frac{F(t)}{(t+\eta)^3}\,dt.}
 \tag{13}
\]

For a finite dyadic version, use the disjoint spectral bands

\[
 B_k=\{\lambda\in[0,1]:2^k\eta\le\lambda+\eta<2^{k+1}\eta\},
 \quad
 T_\eta=\sum_{k\ge0}\frac{\|E_C(B_k)f\|^2}{(2^k\eta)^2}.
\]

Only finitely many terms are nonzero, and

\[
 \boxed{T_\eta/4\le D\le T_\eta.} \tag{14}
\]

Consequently (8) is equivalent to the **summed** arithmetic test $L^2/m+T_\eta=O(1)$. At $r=p^{-1/3}$ it contains $O(\log p)$ bands. A bound on each band separately does not bound their sum. Unbounded energy need not put unbounded mass in any one band.

For example, a uniform bound

\[
 F(t)\le C t^{2+\delta}\quad(0<t\le1),\quad\delta>0,
 \tag{15}
\]

bounds (13) independently of $\eta$. More generally $F(t)\le t^2\omega(t)$ suffices if $\int_0^1\omega(t)\,dt/t<\infty$. This is an actual forcing-measure estimate, not an eigenvalue counting estimate. It is essential that $f$ includes both the mark and the actual bulk mean.

### Why the critical exponent and a lowest-window test are insufficient

For an explicit **abstract** example, let

\[
 C_m=\operatorname{diag}(2^{-1},\ldots,2^{-m}),\quad
 (f_m)_j=2^{-j}/\sqrt j,\quad\eta_m=2^{-m}.
\]

For the corresponding cumulative measure,

\[
 F_m(2^{-k})=\sum_{j=k}^m\frac{4^{-j}}j
       \le\frac{4}{3k}\,4^{-k},\qquad
 \frac{F_m(\eta_m)}{\eta_m^2}=\frac1m\longrightarrow0.
 \tag{16}
\]

Nevertheless

\[
 \frac14\sum_{j=1}^m\frac1j
 \le\|(C_m+\eta_m I)^{-1}f_m\|^2
 \le\sum_{j=1}^m\frac1j,
 \tag{17}
\]

which diverges. Every individual summand is at most $1/j$. Also this example has the usual bounded source factorization: $f_m=C_m^{1/2}u_m$, with

\[
 \|u_m\|^2=\sum_{j=1}^m 2^{-j}/j<\log2.
\]

Every positive contraction is a compression of an orthogonal projection, for instance by the block projection with diagonal blocks $C_m,I-C_m$ and off-diagonal block $\sqrt{C_m(I-C_m)}$. Thus positivity of the compression, a bounded factorized source, and no kernel atom do not repair the missing summability. **No nonnegative Paley optimum is constructed by this example.** The failure is of these proposed scalar spectral estimates as a proof strategy; actual Paley positivity can impose additional restrictions.

## 4. Prime and square replay

[astra-energy-13.py](astra-energy-13.py) performs 76 numerical sign/width checks at 12 primes through 4001 and seven prime squares through $61^2$, at both $r=1/(4\sqrt q)$ and $r=q^{-1/3}$. It checks (3), (6), (9), and (14), using the previous NNLS/FFT actual-QP routines. Full numerical output is in [astra-energy-13-results.jsonl](astra-energy-13-results.jsonl). Support detection uses the explicitly numerical threshold $10^{-8}$; these rows do not certify their supports.

The largest checked identity discrepancy was $1.92\cdot10^{-10}$, and the largest reported QP residual was $1.76\cdot10^{-11}$. The selected rows below all use $r=1/(4\sqrt q)$; both prime signs are reported so no ordinary-theta side is inferred from the positive-width mark.

| $q,\sigma$ | Actual numerical bulk size | $L^2/m$ | $D$ | Allowed energy $A$ |
|---|---:|---:|---:|---:|
| $97,+$ | 22 | 1.40846 | 0.52703 | 2.05065 |
| $97,-$ | 25 | 1.24696 | 0.53563 | 1.86393 |
| $401,+$ | 100 | 1.62305 | 0.65887 | 2.31122 |
| $401,-$ | 99 | 1.63204 | 0.61891 | 2.33783 |
| $4001,+$ | 1004 | 1.86256 | 0.85420 | 2.73340 |
| $4001,-$ | 995 | 1.87900 | 0.76411 | 2.66911 |
| $7^2,+$ | 5 | 2.17509 | 1.43374 | 4.09819 |
| $13^2,+$ | 14 | 3.54435 | 4.70835 | 8.88632 |
| $31^2,+$ | 133 | 2.54597 | 19.90036 | 23.17680 |
| $61^2,+$ | 486 | 2.87197 | 43.56849 | 47.20534 |

At $q=61^2$, about 42.86 of $D=43.57$ comes from the band $2^8\eta\le\lambda+\eta<2^9\eta$, far above the lowest regularization window. On primes the contribution is spread over several bands; for $p=4001,+$, the largest single band contributes about 0.1642 to $D=0.8542$. These finite observations illustrate (14); they are not uniform estimates.

The $q^{-1/3}$ rows also pass the identities. For example, the two allowed energies at $p=4001$ are approximately 2.15538 and 2.17570, whereas the plus allowed energy at $q=61^2$ is 2.66069. These modest finite values do not establish an asymptotic bound at this wider scale. All 76 rows also verify the constructed sampling witness (12a) whenever $D>10^{-12}$.

### Separate interval certificates and rational source vectors

The `--certificate` mode uses 192-bit Arb to verify the complete strict orthants at $p=13,r=1/4$ and $q=49,r=1/28$. It checks every bulk sign and the marked condition $\lvert\gamma\rvert<1$, so these are the unique actual optimizers, not assumed supports. It then constructs a **separate rational** $h\in W$: solve $(C+\eta I/64)h\approx f$, round at denominator $10^{12}$, and center exactly. Formula (9) is evaluated with these rational coordinates and interval arithmetic, without a spectral cutoff or a sign check on $h$.

The resulting upper bounds for $D$, rounded upward here, are

| Order and sign | Actual $D$, for comparison | Source certificate upper bound |
|---|---:|---:|
| $13,+$ | 0.17482518 | 0.21752041 |
| $13,-$ | 0 | 0 |
| $49,+$ | 1.43373808 | 1.49546190 |
| $49,-$ | 0.22158027 | 0.23006058 |

The actual $D$ column is not used to evaluate the source bound. The scalar parameters $a,\mu$ and the complete support are certified by the orthant solve.

The same replay separately rounds centered sampling preimages $w$ to rational vectors and normalizes by their certified positive contrast. It certifies $\varepsilon_I<2.174230$ at $13,+$, $\varepsilon_I<0.830439$ at $49,+$, and $\varepsilon_I<2.117342$ at $49,-$. The case $13,-$ has $D=0$, so the unit-contrast sampling problem is not used there. These are upper certificates for the finite sampling problem, not the uniform lower bound that would bound prime energies.

Reproduce from the repository root:

```sh
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 \
  .venv/bin/python -B research/astra-energy-13.py --large
.venv/bin/python -B research/astra-energy-13.py --certificate
.venv/bin/python -B research/astra-energy-13.py --dispersed-model
```

## 5. Remaining prime input

This note does **not** establish $A_\sigma(r_p)=O(1)$ on the larger ordinary-theta sign, at $p^{-1/3}$ or another moving width. What it supplies is an exact current-support alternative that sees dispersed energy: construct the bounded signed source approximation (10), bound the regularized sampling constant $\varepsilon_I$ away from zero in (12b), or prove the summed forcing-measure estimate (13)/(14), while bounding $L^2/m$. Each needs a prime estimate for the actual larger-theta support and actual mark/mean combination. No estimate here permits substituting an arbitrary dense mask, omitting the sum over spectral scales, or replacing the ordinary-theta side by the sign of the positive-width mark.

Only this note, its uniquely named script, and its numerical JSONL were written. No ledger, README, shared script, or remote was changed.
