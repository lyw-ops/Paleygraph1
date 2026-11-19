# A larger-prime failure of the saved averaged repair trial

Round 36, ordinary theta. At prime $p=7340033$, the saved rational
Fourier proposal generated at depth $128$, floor $\tau=1/20$, and
clipping reserve $\kappa=1/1000$ has a strictly negative repaired
minus coordinate. Arb128 proves

$$
(\widehat z_-)_{2136334}<
-0.0002282579562724539.
$$

Its plus row is strictly positive. This is a finite failure of the
specified **exact saved-input repair** on an actual prime. It does
not disprove another completion, the eventual large-prime assertion,
or ETH26. The floating generator is not an interval-enclosed exact
Picard orbit, so this result must not be promoted to a certified
failure of the unrounded mathematical Picard proposal.

## 1. The same proposal can be generated with one Picard FFT per step

Use the true-orbit notation and projected averages of
[averaged marks 35](averaged-mark-35.md). For $t=1,\ldots,T$ put

$$
S_\phi=\sum_{t=1}^T(\phi_t+\phi_{t-1}),\qquad
S_v=\sum_{t=1}^T(v_t+v_{t-1}),\qquad
F_T=v_T+v_{T+1}-v_1.
$$

The exact endpoint identity in
[Astra 35, Section 7](astra-signed-repair-35.md) is equivalently

$$
\boxed{\quad
X_{\sigma,T}=
\frac{\mu_T-\mu_0}{2T}1+
\frac{S_\phi+\sigma(S_v+F_T)}{4T}.
\quad}                                                     \tag{1}
$$

Indeed $S_v+F_T=\sum_{t=1}^T(v_t+v_{t+1})$, because $v_0=0$.
Together with $Kv_t=(I-J)\phi_{t-1}$, this is the direct projected
average formula. An implementation only needs the transform
$v_{t+1}=K\phi_t$ per orbit step, rather than separately projecting
both raw sign rows. A few final transforms still form the repair.

The [generator](endpoint-stress-36.py) checks this implementation
against direct projections at primes $13,9413$, and its $9413$
and $1000033$ results agree with the previously recorded floating
averaged trials. These comparisons check implementation, not an
outward-rounded orbit error. Equation (1) is a mathematical identity;
the generated finite arrays remain floating proposals.

## 2. Exact input and the negative certificate

The generator rounds normalized Fourier coefficients to integers
divided by $2^{90}$, sets the DC coefficient exactly to one, makes
them exactly even, and sets forbidden coefficients exactly to zero.
The resulting rows are therefore exact mean-one affine-sector
rows. Their positivity is not assumed.

The saved input is
[endpoint-stress-36-p7340033-t128-input.json.gz](endpoint-stress-36-p7340033-t128-input.json.gz).
Its uncompressed SHA-256 is

    f1e99a29831f9bf717d167ae31dcf9bf4c5248e17842f72042c72f7b3b47c24e

It uses the schema of the
[round-36 positivity verifier](astra-averaged-positive-36.py).
Replay starts with these exact integers, not with a numerical claim
about their generating orbit. Arb decides all clipping branches,
applies the actual pinned Paley projection

$$
d_0=0,\quad d_i=(2\kappa-z_i)_+,\quad
L_\sigma=P_\sigma-\ell_\sigma\ell_\sigma^T/a_\sigma,\quad
\widehat z=z+2L_\sigma d,
$$

and encloses all repaired coordinates. The exact projector identities
prove preservation of mean, sector, evenness and mark; interval
Fourier checks and the reflection-energy equality cross-check them.
The negative coordinate is proved by its **upper** endpoint, not
merely by a lower minimum enclosure.

The [Arb128 output](endpoint-stress-36-negative-certified.jsonl)
proves the following outward bounds:

| sign | result | relevant rigorous bound |
|---|---|---|
| plus | every coordinate strictly positive | minimum $>.00013312807090234$ |
| minus | coordinate $2136334$ strictly negative | value $<-.0002282579562724539$ |

Both rows retain their exact marks and means. A failed minus row
does not provide the complementary feasible theta bound. There is
no assertion that the minus affine space has no other positive
completion; the stronger square obstruction of round 35 is a
different result and does not apply to this prime.

## 3. Comparison with the smaller-prime trials

At the same floor, reserve and depth, the separately saved inputs
certified by Astra 36 give:

| prime | repaired plus minimum | repaired minus minimum | pair status |
|---:|---:|---:|---|
| $9413$ | $>.0006806378966$ | $>.0009350215157$ | strictly positive |
| $1000033$ | $>.00004737707156$ | $>.0002321502056$ | strictly positive |
| $7340033$ | $>.00013312807090234$ | negative coordinate $<-.0002282579562724539$ | failed trial |

These are strict outcomes for their respective saved rational inputs.
The numerical minima are not monotone in the prime. Two positive
examples do not establish a uniform rule; this negative example
does not rule out an eventual threshold beyond it. Changing depth,
weights, reserve or completion can produce different proposals.
No asymptotic conclusion is inferred from the finite table.

## 4. Reproduction and evidence classification

Generation and strict replay:

    OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python -B \
      research/endpoint-stress-36.py --primes 7340033 --save-input \
      > research/endpoint-stress-36-negative-proposal.jsonl
    OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python -B \
      research/astra-averaged-positive-36.py --precision 128 --replay \
      research/endpoint-stress-36-p7340033-t128-input.json.gz \
      > research/endpoint-stress-36-negative-certified.jsonl

The input is already saved, so the second command is sufficient to
replay the strict result. A second full interval replay was compared
byte-for-byte with the canonical certificate and is identical.
Regenerating a floating proposal on another implementation may create
different integers and requires its own interval verification.

The small and large generator outputs are labelled floating diagnostics.
The saved-input line is provenance, not a numerical certificate. The
one rigorous negative record is interval arithmetic on the exact input.
None encloses the exact large Picard prefix or its averaged mark budget.
The remaining target is prime-uniform positive completion with the
required marked control, not a declaration of success or failure
based on these three finite cases.
