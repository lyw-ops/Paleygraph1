# Round 20: signed descent, support switching, and the omitted mark

This note derives exact finite-dimensional identities and a sufficient field-first criterion for the **actual** floor D. It does not prove the needed prime-uniform estimate. The replay is floating point, not an interval certificate. Notation and the actual reciprocal input are those of [Round 19](threshold-repair-19.md) and [Round 17](parallel-repair-17.md).

## 1. Exact signed descent without a positive comparison

Fix the orthogonal projection P=P_{-sigma}, 0<alpha<2, and omit only the mark: O={0}^c. Start at G_0=A+t1, where A is a clipped shadow of mean b and t>=0. Write m=b+t and

    r_k=D-G_k,  e_k=1_O(r_k)_+,  v_k=P e_k,
    G_{k+1}=G_k+alpha v_k.

This is gradient descent on F(G)=||1_O(D-G)_+||²/2 restricted to m1+im P. The statements below also hold for alpha=2 except where strict convergence is asserted.

For **any** target G_* in that affine space there is the exact identity

    ||G_{k+1}-G_*||²-||G_k-G_*||²
      = -2alpha ||e_k||² -2alpha <e_k,G_*-D> +alpha²||Pe_k||².       (1)

If G_*>=D on O, this gives Fejer decrease at least

    [2alpha-alpha² gamma_k] ||e_k||²,
    gamma_k=||Pe_k||²/||e_k||².

Unlike the crude coefficient alpha(2-alpha), this is useful as alpha tends to 2 whenever gamma stays below 1. But a uniform bound on the distance to such a target is **additional input**, and off-mark feasibility alone gives no bound on its marked deficit. Fejer monotonicity is therefore not itself the required theorem.

There is a sharper, exact residual formula. Put

    beta_k = 2/||e_k||² ∫_0^1 (1-u)
                ||1_{O∩{r_k-u alpha v_k>0}} v_k||² du.

Then

    ||e_{k+1}||²/||e_k||² = 1-2alpha gamma_k+alpha² beta_k.          (2)

The squared positive part is continuously differentiable; integrate its second derivative on each linear segment to prove (2). Kinks have measure zero, with identically zero segments contributing zero. In particular 0<=beta_k<=gamma_k, recovering ordinary descent. This equality retains all signed transfer and slack. It is a sharp one-step criterion, not a claim of an arithmetic estimate.

Support switching is explicit here. If S_k={i in O:r_{k,i}>0}, then positivity at any point of the segment implies membership in S_k union S_{k+1}. Consequently

    beta_k <= ||1_{S_k union S_{k+1}} Pe_k||²/||e_k||².             (3)

Dropping new entrants from this union is invalid. Conversely using all coordinates throws away precisely the additional decrease that survives when alpha is close to 2. On a fixed support, provided no coordinate crosses zero, e_{k+1}=(I-alpha P_SS)e_k. The relevant condition is the signed compression on the actual vector, not the Perron radius of (I-alpha P)_+.

## 2. A uniform criterion which pays for the mark

A stronger conclusion than mere residual convergence is needed. Suppose the actual orbit obeys

    sum_{k>=0} ||e_k||_2 <= C(s) ||e_0||_2                         (4)

uniformly on all sufficiently large primes and both signs, at each fixed s. For example (2) proves (4) with C(s)=1/(1-rho(s)) if its right-hand side is at most rho(s)^2<1 at every nonzero residual. A finite initial segment followed by this contraction is sufficient too; account for its norms in C(s). Thus support changes are allowed throughout.

By summability, G_k converges in Euclidean norm at each fixed field, and G_infinity>=D on O. Since e_k vanishes at the mark and (-P_{0i})_+<=omega,

    (D_0-(G_infinity)_0)_+/h
      <= (D_0-(G_0)_0)_+/h + alpha omega/h sum_k ||e_k||_1
      <= (D_0-(G_0)_0)_+/h
           + alpha omega sqrt(n-1)/h C(s)||e_0||_2.                (5)

No positivity of Z is used. Adding that deficit times the anchored nonnegative Jacobi kernel R produces a full majorant with mean m plus the left side of (5).

The energy estimate for the starting clipped shadow gives both

    ||e_0|| <= sqrt(ns(1-c²)),
    (D_0-(G_0)_0)_+/h <= sqrt(2s(1-c²)).

Using alpha omega h<=1 and n/h²<=2, the final mean is at most

    b+t + [sqrt(2)+2 C(s)] sqrt(s(1-c²)).                         (6)

This bound is independent of the depth and field order. In particular, if t<=t(s)->0, b<=1-c, and sqrt(s) C(s)->0, the endpoint pairing gives the desired asymptotic along primes, conditional on (4). The sufficient condition can be weakened by retaining the actual factor sqrt(1-c²). No tail-mass hypothesis and no bound on the number of active coordinates is required. A fixed contraction bounded away from one is enough. The unproved arithmetic task is now a **signed, actual-orbit summability estimate**, rather than a positive inverse or a gap for arbitrary sparse sets.

Equation (5) also explains why proving only e_k->0, with no uniform control on its accumulated mass, is insufficient. An arbitrarily slow orbit can transfer an order-one deficit to the omitted coordinate.

## 3. Exact dual certificates, including a missing mark

Every nonzero w>=0 with Pw=0 gives the lower bound

    mean(G) >= <w,D>/<w,1>                                      (7)

for every full affine-sector majorant G. This is the LP dual characterization of the minimum mean; finite-dimensional LP duality applies since a sufficiently large constant is strictly feasible and the mean is bounded below. At a fixed proposed mean m, off-mark feasibility instead tests nonnegative kernel vectors supported on O. Omitting the mark removes dual witnesses with positive marked mass from that test.

There is a simple **finite-iterate** full dual family which puts the mark back. For any lambda>=0 define

    u=e_k+lambda delta_0,
    delta=max(0, max_i(Pu-u)_i),
    w=u-Pu+delta 1.                                             (8)

Then w>=0 and Pw=0 exactly, so (7) applies whenever w is nonzero. There is no need to assert that a small ||Pe_k|| makes e_k itself dual feasible. Constant padding in (8) may have mass n delta and destroy sharpness: small relative Euclidean stationarity alone does not prevent this. Lambda can be optimized or tested on a finite grid; any resulting lower bound is valid with rigorous input/error control.

For an off-mark majorant G at mean m and any such w with w_0>0,

    (D_0-G_0)_+/h >= (<w,D>-m<w,1>)_+/(h w_0).                 (9)

This gives a quantitative obstruction to a cheap marked completion. It is valid even if the off-mark violation has vanished entirely. For w_0=0 a positive numerator is instead an obstruction to off-mark feasibility itself.

## 4. Square plus: convergence succeeds, uniform cheap completion fails

At q=ell², put h=(ell+1)/2 and I=(F_ell^times)^perp, with |I|=h. The exact square identities give P1_I=0, kappa=1/2, omega=1/[2(h-1)], and alpha=2(h-1)/h. On I, P has diagonal kappa and off-diagonal -omega.

Suppose an actual orbit has e_k=d_k 1_{I\{0}} and no entries outside this set become active. Then exactly

    d_{k+1}=(1-1/h)d_k,
    gamma_k=omega,
    beta_k=omega²,
    sum_{k>=0}||e_k||/||e_0||=h.                               (10)

Thus the residual converges at each field; the convergence is not uniform. The mark changes by

    G_{k+1,0}-G_{k,0}=-alpha kappa d_k,
    G_infinity,0-G_{0,0}=-(h-1)d_0.                            (11)

The marked charge tends to roughly d_0, not zero. The fixed-support hypothesis in (10) is conditional; the exact obstruction below is unconditional for every square shadow.

For e=d1_{I\{0}}, choosing lambda=d in (8) gives u=w=d1_I and delta=0: the missing mark exactly restores the subfield dual. Without that completion, the relative stationarity ||Pe||/||e||=sqrt(omega) tends to zero but the dual padding need not be negligible in mass. Applying (9) to 1_I yields

    m + (D_0-G_0)_+/h >= max(m, mean_I D)                      (12)

for every off-mark majorant. This is precisely the square obstruction from Round 19. Neither support omission nor signed convergence removes it. The exact square endpoint controls imply an order-one obstruction to the desired small total repair cost for small fixed width.

## 5. Diagnostics, separate from the identities

`astra-signed-20.py` replays the actual reciprocal floor at s=1/64, takes four ordinary clipped steps at b=3(1-c)/4, then runs 128 signed off-mark updates at half the translated cutoff. It asserts the switching remainder bounds and the Fejer equality numerically at every update. It saves energies, support changes, signed Rayleigh quotients, mark charge, translated finish, and four completed dual candidates. The input fixed point and arithmetic are floating point, so these are not certified lower bounds.

At p=153649, plus support grows from 4692 to 7062 by step four, while the squared residual ratio is about 0.283 at step zero and 0.459 at step four. The minus figures are 4394 to 6796 and ratios 0.262 and 0.445. Large support and support growth are therefore compatible with fast signed contraction on this actual data.

At 389² plus, the support is the 194 off-mark subfield sites. By step four the squared ratio is 0.9897698882=(194/195)². The completed dual with lambda=max(e) numerically gives mean_I D=0.426358, whereas omitting the completion and using only constant padding gives about 0.214510. The growing marked deficit and constant translated finish expose the cost transferred to the mark. The small discrepancy from exact subfield shape at step zero disappears numerically after the initial signed updates. The partial summability ratios through step 128 are 2.549 and 2.432 for the two p=153649 sides, versus 94.540 for 389² plus (whose fixed-support infinite ratio is 195). These partial sums are lower bounds on the infinite sums, not certified upper bounds. The prime padded duals are weak; this experiment supplies no prime obstruction.

Replay:

```sh
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python -B \
  research/astra-signed-20.py > research/astra-signed-20.jsonl
```

The new exact result is the route (2) -> (4) -> (6), together with the omitted-mark dual obstruction (8)-(12). The remaining prime claim is (4) at a cost C(s)=o(s^(-1/2)); the finite diagnostics do not establish it.
