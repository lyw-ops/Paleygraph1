# Testing the rooted quotient after deleting the true signed high blocks

The signed flat test of [round 98](astra-quotient-98.md) has a sufficient test that needs only the locations of the largest positive block means. At a cutoff $J^2/\log J$, at most a fraction $2(\log J)^2/J^3$ of quotient characters must be deleted. The test asks whether the original prescribed root is still attainable. Failure gives an opposite-sign trigonometric majorant of the root whose pointwise defects all lie on the deleted characters. There is an exact interpolation formula for testing any allowed positional clique against this sparse set.

Use the same prime $p\equiv1\pmod4$, $n=(p-1)/2$, full horizon $J=\lfloor D(p)/8\rfloor$, actual cold zero start, scalar and masks as in round 98. On its prefiltered bounded list $L=K\cup C$, $m=|L|\asymp\sqrt n$, $m/|C|\le2$, $|\lambda|\le\kappa_*<1$, $B=L^\perp$ and $b=|B|=n/m$. Let $R\in\widehat B=G/L$ index a block, with $R=0$ denoting the original $L$. In the companion sign $\sigma$, write $\mathcal P$ for the nonnegative probabilities $u$ on $\widehat B$ whose Fourier transform is supported on the identity and $\{z\in B:s(z)=\sigma\}$. Their uniform lifts are the genuine block laws. Keep the prescribed floor $w_*>0$ on $u_0$, including the case of equality. The size and root filters are those of [rounds 95](astra-recur-95.md) and [97](astra-prefix-97.md).

For any permitted round-95 erasures $A_j\subset L^c$, $|A_j|\le H_p^2$ at time $j$, put
\[
 v_0=0,\qquad
 v_R=\frac{\sigma}{Jm}\sum_{0\le j<J}\sum_{i\in R\setminus A_j}Y_j(i)
       \quad(R\ne0),\qquad S_t=\{R:v_R>t\},\quad t>0.
\]
Only the measurement erases sites. The true update still applies $\mathsf K$ to $|Y_j|+\beta_j\sqrt n e_0$ and uses its genuine $g_j$. For a trial $u$, the signed flat term before the factor $2/(J-1)$ in round 98 is exactly $\sum_R u_R v_R/u_0$.

## A sparse deletion test and its opposite-sector obstruction

For $S\subset\widehat B\setminus\{0\}$ define $C(S)$ as the maximum possible $u_0$ among laws in $\mathcal P$ vanishing on $S$, or zero if there is none. Then
\[
 \frac{|S_t|}{b}\le \min\{1/t,\ 2(J-1)/t^2\},\qquad
 C(S_t)\ge w_*\quad\Longrightarrow\quad
 \inf_{u\in\mathcal P:\,u_0\ge w_*}\frac{\sum_R u_Rv_R}{u_0}
      \le (w_*^{-1}-1)t .                                           \tag{1}
\]
In fact $\mathbb E_GY_j=0$ and $\mathbb E_G(\sigma Y_j)_+=\mathbb E_G|Y_j|/2\le g_j$. The exact zero-start energy telescope gives $\sum_{j<J}g_j\le J$ and $\mathbb E_GY_j^2\le4j$. Jensen on each block and in time, treating each erased entry as zero with the *original* denominator, gives $b^{-1}\sum_R(v_R)_+\le1$ and $b^{-1}\sum_R v_R^2\le 2(J-1)$. Markov gives both size bounds simultaneously for every permitted erasure. For the price use an attaining law, retain $v_0=0$, and bound all its nonroot contributions above by $t(1-u_0)$. Negative values of any magnitude are permitted.

In particular take $t=J^2/\log J$ for $J\ge3$. If the same genuine recurrence obstruction of round 98 persists while its one-sided triangular transform is $o(J)$, then eventually $C(S_t)<w_*$. Indeed otherwise (1) supplies the forbidden signed $o(J^2)$ trial on that subsequence. The triangular input can use an independent permitted erasure. More generally (1) works with any positive $t=o(J^2)$. This is a sufficient trial construction. The signed optimum may be cheap even when exact avoidance fails.

The capacity has the finite dual description
\[
 C(S)=\min\{d:\ d\ge0,\quad P(R)=d+f(R)\ge1_{R=0}
          \quad(R\notin S),\quad f\in V_{-\sigma}(B)\}.                \tag{2}
\]
Here $V_{-\sigma}(B)$ denotes the real mean-zero functions on $\widehat B$ with Fourier support in the *opposite* positional sign within $B$. Both sine and cosine directions are allowed. To see (2), maximize the root over nonnegative rows supported off $S$, with total mass at most one and all opposite moments zero. The zero row is always feasible, and normalizing any nonzero positive-root row increases its root if the mass is below one. The mass inequality has multiplier $d\ge0$ and the Fourier equalities have unrestricted real multipliers. Finite linear programming duality gives (2), including attainment. Consequently failure in (1) at its original floor is equivalent to the existence of such a $P$ with mean strictly below $w_*$. Every full qualified law must pay on its *actual defects*:
\[
      \sum_{R\in S}u_R(-P(R))_+\ \ge\ u_0-d .
\]
This follows by testing $P$ against $u$, whose opposite moments vanish. Thus a way to prove the sufficient upper is to rule out this sparse opposite-frequency majorant for the measured set. Its negative depths on $S$ are unrestricted.

## An explicit trial without the capacity LP

Let $D\subset B$ have all nonidentity pair quotients of sign $\sigma$. For coefficients $a\in\mathbb C^D\setminus\{0\}$ take
\[
 u_R=\frac{|\sum_{z\in D}a_z\overline{R(z)}|^2}{b\sum_{z\in D}|a_z|^2}.
\]
Character orthogonality gives mass one, and expanding the square gives the required Fourier support. Let $M=(\overline{R(z)})_{R\in S,z\in D}$ and let $P_0$ be orthogonal projection onto $\ker M$. The largest root attainable by these trials vanishing on $S$ is
\[
                    \frac{\|P_0\mathbf1_D\|^2}{b}.                    \tag{3}
\]
When the kernel is zero take this value to be zero. In fact the numerator before division by $b$ is the maximum of $|\langle\mathbf1_D,a\rangle|^2/\|a\|^2$ on that kernel. If (3) reaches $w_*$, its projected constant vector gives the required trial directly. If $D$ is an allowed subgroup of order at least $bw_*$, it suffices that $S_t$ miss its annihilator, by the constant coefficient trial. Thus a surviving small-triangular branch must have its true sparse head intersect the annihilator of every such subgroup, and must fail (3) for every allowed clique. The test does not assume an allowed clique of the required size exists.

## Finite outward replay

At $p=769$, $m=8$, $J=16$, $\sigma=+1$, use the same signed erasure $A_j=\{2+2j\}$ and the same floor $1/8$ as round 98. The actual head above $1.3$ is $\{10,38\}$. The order-six positional subgroup of $B$ is an allowed clique. Its Fourier square is uniform on the eight multiples of six in $\mathbb Z/48$, so it avoids this head with root exactly $1/8$. Its signed charge before dividing by the root is in $[0.485880624,0.485880625]$. At cutoff $1.2$ the actual head becomes $\{10,12,36,38\}$. A trigonometric majorant of type (2) proves $C(S_{1.2})<0.076456$, below the prescribed root for **all** laws. These finite facts show why an influence estimate from the size of the deleted set alone cannot simply presume retention of the floor.

The [checker](astra-quotient-99-check.py) uses 384-bit Arb on the genuine marked trajectory and strictly separates all 48 costs from each cutoff. The clique support and its root are exact group identities. A floating LP proposes coefficients for the four-block majorant. Rounding them to rational values, raising the constant by $10^{-8}$ and checking every required inequality with Arb supplies the reported upper. [Replay record](astra-quotient-99-checks.jsonl)

1. On the true filtered list, test the original root capacity after deleting the signed head at $t=J^2/\log J$. Equation (3) supplies a sufficient arithmetic trial. Equation (2) specifies precisely the sparse sign-restricted certificate a failure would require. No capacity lower uniform through primes is proved.
2. Bound the round-98 opposite-sign triangular sum on the original identity fiber from below by $-o(nJ)$, or couple a large triangular sum with the defect sites of (2). The sparse deletion criterion changes only the signed flat obligation. The escaped branch and the ordinary theta limit remain open.
