# A positive inverse for thresholded Fourier repair

The [bulk transfer recurrence](parallel-tail-18.md) has a source term from updating defects below the final cutoff. Applying the Fourier projection only to defects above that cutoff yields a different repair with no such source. A monotone active-set computation gives a sufficient test. A character-sum bound limits its support to order $\sqrt q$. The resulting field-first criterion needs a spectral gap on the terminal active set and a cutoff tending to zero. It does not require a separate estimate of the starting tail mass.

## Repair above the final cutoff

Use the scaled positive floor $D=\sqrt n(-H)_+$ and affine shadow $A\in U_{-\sigma}$ of mean $b$ from the [clipped projection](parallel-repair-17.md). Put $P=P_{-\sigma}$, $Z=I-\alpha P$, and let $h$ and $R$ be the height and normalized positive Jacobi kernel from that construction. In particular every off-diagonal entry of $Z$ is at most $\alpha\omega\le1/h$. At cutoff $t\in\mathbb R$ write $f=D-A-t\mathbf1$. Reserve a set $J$ of exceptional sites, including the mark, and let $O=J^c$. Let $B=(Z_{OO})_+$ with positive part taken entrywise.

If $w$ is nonnegative on $O$ and satisfies

$$w\ge f_O+B w,\tag{1}$$

extend it by zero on $J$. The one-shot repair $G=A+t\mathbf1+\alpha P w$ dominates $D$ on $O$. Indeed $D-G=f-(I-Z)w$ and $Zw\le Bw$ on $O$. Its mean is $b+t$. The omitted sites can be filled by adding $R*u$, where $u_i=(D_i-G_i)_+$ on $J$ and zero elsewhere. The resulting correction has mean $b+t+h^{-1}\sum_{i\in J}u_i$ and dominates $D$ everywhere.

Alternatively let $W_0=0$ and at every step add $E_k=(f-\alpha P W_k)_+$ on $O$, with zero values on $J$. Then $W_{k+1}=\max(W_k,f+ZW_k)$ on $O$. If (1) holds, induction gives $0\le W_k\le w$ at all steps. Also $(E_{k+1})_O\le B(E_k)_O$, since the signed negative slack at each site is retained by the thresholded iteration. This is where updating only above the final cutoff removes the background injection. The signed iterates can also be stopped early and finished with one translated Jacobi correction at their optimal cutoff.

## Solve the nonnegative comparison exactly

Start with $S=\varnothing$, $w=0$. At each step add all sites outside $S$ where $f_O+Bw>0$, obtaining $S'$. If $\rho(B_{S'S'})<1$, solve $(I-B_{S'S'})w'_{S'}=f_{S'}$, setting other entries to zero. The residual of the old solution in this new equation vanishes on $S$ and is positive on $S'\setminus S$. The Neumann inverse is nonnegative, so $w'\ge w$. Any global nonnegative supersolution of (1) dominates $w'$ by restriction and the same inverse inequality.

If $\rho(B_{S'S'})\ge1$, there is no nonnegative supersolution of (1). A Perron component of spectral radius at least one must meet $S'\setminus S$, since the previous block had radius below one. For a putative supersolution $v\ge w$, restrict the new residual inequality for $v-w$ to this component. Its positive left Perron vector turns the left side into a nonpositive quantity and the right side into a strictly positive one. If no new sites enter, the current $w$ is the least supersolution of (1). This exact characterization is for the entrywise positive comparison. The signed repair problem can still have a feasible solution when (1) fails.

There is a direct bound on the cost of the omitted sites from the final block. Suppose $t\ge0$ and $A$ comes from any number of the original clipped projections, starting at the constant $b\ge0$. Set $L=|J|$ and $\rho=\rho(B_{SS})<1$ at termination. The [reciprocal energy estimate](parallel-tail-18.md#1-separate-the-exceptional-entries-at-no-field-dependent-cost) gives $\|(D-A)_+\|_2\le\sqrt{ns(1-c^2)}$ at reference width $s$. Also $\|w\|_2\le \|(D-A)_+\|_2/(1-\rho)$, either by the nonnegative inverse or by pairing (1) at equality on $S$ with $w$. Each omitted-site increase of the residual is at most $\alpha\omega\|w\|_1$. Therefore

$$\frac1h\sum_{i\in J}u_i
 \le \sqrt{2s(1-c^2)}\left(\sqrt L+\frac{L\sqrt{|S|}}{h(1-\rho)}\right).\tag{2}$$

In the empty-block case the second term is zero. This inequality uses $h\ge\sqrt q/2$ for $q\ge9$ and $\alpha\omega\le1/h$ as in the clipped repair. It allows much larger initial $\ell_1$ load than a transfer bound requiring $\|(D-A-t)_+\|_1/h=O_s(1)$.

## A support barrier from a cubic character sum

Let $\lambda_i=nK_{i0}$ be the Jacobi coefficients and set $C=K\circ K$, the entrywise square. The constant eigenvalue of $C$ is $1-1/n$, since $K^2=I-J_{\rm const}$. At any nonidentity positional label $a\in Q$, its eigenvalue is

$$\frac1n\sum_{x\in Q}\chi((1-x)(x-a)).$$

To see this, the Fourier transform of the squared column of $K$ is $n^{-1}$ times the multiplicative convolution of the sign mask with itself. Replacing $\chi((1-x)(1-a/x))$ by the displayed summand uses $\chi(x)=1$ on $Q$. Inserting the square indicator writes the sum as half the quadratic sum $-1$ and half the cubic sum for $\chi(x(1-x)(x-a))$. The roots $0,1,a$ are distinct and the cubic magnitude is at most $2\sqrt q$ by the Hasse bound on its elliptic curve. Thus every nonconstant eigenvalue of $C$ is at least $-(\sqrt q+1/2)/n$.

The diagonal and constant terms of $Z=(1-\alpha/2)I+(\alpha/2)J_{\rm const}+(\alpha\sigma/2)K$ are nonnegative. The Jacobi bound $|K_{ij}|\le\sqrt q/n$ and $x_+\ge(x+x^2)/2$ on $[-1,1]$ give the entrywise comparison

$$B\ge \frac{\alpha}{4}\left(\sigma K_{OO}+\frac{n}{\sqrt q}C_{OO}\right).$$

For any nonempty set $S\subset O$ with $m=|S|$, test $B_{SS}$ on its constant vector. Using $K\mathbf1=0$, $\|K\|_{2\to2}\le1$, and the last bound on $C$ gives

$$\rho(B_{SS})\ge \frac\alpha4\left[(1-1/n)\frac{m}{\sqrt q}-\left(2+\frac{1}{2\sqrt q}\right)(1-m/n)\right].\tag{3}$$

Since $\alpha\to2$, every subcritical block has size at most $(4+o(1))\sqrt q$, uniformly in the field and the sign. If $f$ starts positive on a set larger than $(4+\epsilon)\sqrt q$, (1) is impossible at that cutoff for all sufficiently large fields. The calculation applies also to a later active set in the algorithm. This explains why choosing a cutoff below the bulk range can defeat the positive comparison even though exact signed updates still reduce the residual.

## A field-first criterion and the square obstruction

For each sufficiently small fixed $s>0$, suppose that on all sufficiently large primes and both signs there is a clipped shadow at some depth, a cutoff $0\le t\le t(s)$, and at most $L(s)$ omitted sites, such that the positive active-set algorithm terminates at a block of spectral radius below one with $(1-\rho)\sqrt h\to\infty$ as $p\to\infty$ at fixed $s$. Assume $t(s)\to0$ and $sL(s)\to0$. By (3), $|S|=O(h)$, so the second term in (2) tends to zero at fixed $s$. The remaining exceptional cost tends to zero as $s\downarrow0$. Taking $b\le1-c$ and using the [endpoint pairing](parallel-repair-17.md#setup-and-explicit-formula) gives a normalized endpoint lower bound at least $a/(1+t+\sum u_i/h)$ on each sign, where $a=H_0\to1/(1+s)$ at fixed width. Hence this criterion would prove the asymptotic via reciprocity. Even a width-dependent positive gap would suffice. Neither termination at sufficiently small cutoffs nor the terminal gap has been proved uniformly on primes.

At a plus square, let $I$ be the subfield annihilator of size $h$. If no sites of $I$ are omitted, $B_{II}=\mathbf1_I\mathbf1_I^\mathsf T/h$. When $b+t< h^{-1}\sum_I D$, summing (1) over $I$ is impossible. If only the mark is omitted, $I'=I\setminus\{0\}$ has spectral radius $1-1/h$. Any solution of (1) has $h^{-1}\sum_{I'} w\ge\sum_{I'} f$. Regardless of the comparison method, a true off-mark correction $G$ must satisfy $G_0\le h(b+t)-\sum_{I'}D$ by the subfield sum identity. Filling its marked deficit recovers the lower bound $h^{-1}\sum_I D$ on the resulting mean. The omitted mark therefore changes the spectrum of the comparison but retains the exact square obstruction to a small total cost.

## Replays

The [replay](threshold-repair-19.py) compares the original translated finish with the positive inverse at four cutoffs. An optional comparison uses 32 signed Fourier updates at three fixed thresholds, followed by one translated finish chosen for the resulting shadow. Floating-point active-set stops and spectral radii diagnose the positive comparison. For selected completed repairs the existing interval replay checks the reference error, rounds the correction in its sector, and supplies an ordinary theta certificate.

The [main sweep](threshold-repair-19-certified.jsonl) has 288 diagnostic rows and 68 interval lower bounds. At each order, width and sign the code certifies the baseline and the candidate with the least numerical repair mean. The best signed iteration improves the certified baseline on all 20 sampled prime settings. The values below are rounded downward. The side $\sigma=-$ provides the lower bound for $\vartheta(\overline H)/\sqrt n$.

| Order and sign | Reference width | Four-step translated lower bound | Signed threshold lower bound |
|---|---:|---:|---:|
| $153649,+$ | $1/16$ | $0.94997195$ | $0.96292556$ |
| $153649,-$ | $1/16$ | $0.94781941$ | $0.96072629$ |
| $1000033,+$ | $1/16$ | $0.94563799$ | $0.96015280$ |
| $1000033,-$ | $1/16$ | $0.94753762$ | $0.96179695$ |
| $1000033,+$ | $1/64$ | $0.98362630$ | $0.98857411$ |
| $1000033,-$ | $1/64$ | $0.98521773$ | $0.99019865$ |

At width $1/64$ both million-order translated baselines exceed the mean reserve by about $0.00022$. The [signed certificates at the same width](threshold-repair-19-small-million-certified.jsonl) leave more than $0.00478$ of reserve on either side. In the [128-step check](threshold-repair-19-small-deeper.jsonl) there is less than $10^{-9}$ further numerical gain at the three tested cutoffs. The [broader small-width run](threshold-repair-19-small.jsonl) gives floating-point comparisons with primes and square controls. At $389^2,+$ the positive inverse at the original cutoff can terminate with radius $194/195$, and the completed lower bound is still at the subfield ceiling.

The [support certificate](threshold-repair-19-certificate.py) encloses the actual four-step shadow at $p=153649$, $s=1/16$. The cutoff is the exact binary value of half the translated threshold in each sign. Projecting a rounded reciprocal vector gives a scaled floor within Euclidean error $\sqrt n\epsilon$, with $\epsilon$ certified by the contraction. After subtracting the respective initial means, the effective floor error is at most $7\sqrt n\epsilon/4$. The nonexpansive shadow update then gives residual error at most $(1+4\alpha)7\sqrt n\epsilon/4$. Both signs have at least 2000 strictly positive off-mark entries at the selected cutoff. Formula (3) yields a spectral radius greater than $1.5685$ on those entries, proving that the positive comparison fails at the same thresholds used by the successful signed candidates. [Two interval records](threshold-repair-19-obstruction-certified.jsonl)

Separately, 112 dense linear programs agreed with the active-set comparison, including 82 infeasible cases. The squared-column and spectral lower-bound formulas were checked on six prime and four square fields.

```sh
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python -B \
  research/threshold-repair-19.py --signed-steps 32 --certify-max-order 1000033
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python -B \
  research/threshold-repair-19.py --signed-steps 32 --width .015625 --fixed-only \
  --primes 9413 37253 153649 1000033 --square-roots 97 193 389
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python -B \
  research/threshold-repair-19.py --signed-steps 32 --width .015625 --fixed-only \
  --primes 1000033 --square-roots --certify-max-order 1000033
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python -B \
  research/threshold-repair-19-certificate.py
```

For the 128-step diagnostic, use the third command with `--signed-steps 128` and omit `--certify-max-order 1000033`. The [Jacobi transfer note](parallel-cap-19.md) gives a separate obstruction to a uniform gap for arbitrary weighted peaks. The [Picard comparison](astra-background-19.md) shows why controlling the background in global Euclidean norm is insufficient at the tail scale. Uniform control of either the positive inverse at small cutoffs or the genuinely signed threshold iteration through primes remains open.
