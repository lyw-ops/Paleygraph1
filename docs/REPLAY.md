# Replaying computations

Run commands from the repository root. The pinned dependencies are in [requirements.txt](../requirements.txt).

## A small first check

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -B theta.py --certify 5 13 41
```

This certifies finite theta bounds for the listed primes. The asymptotic conjecture requires a separate proof.

## Unified Python entry point

The [Python catalogue](PYTHON.md) groups the published scripts and provides a common runner:

```sh
python3 scripts/paley.py list --group quadratic
python3 scripts/paley.py show real-two-marks-91-check
.venv/bin/python -B scripts/paley.py run theta --certify 5 13 41
.venv/bin/python -B scripts/paley.py run research/real-two-marks-91-check.py
```

The runner uses the invoking interpreter, runs from the repository root and supplies that root on `PYTHONPATH`. It preserves the selected script's arguments, output and exit status. Listing and inspection do not execute the selected script. Its catalogue comes from a published Git snapshot; new local scripts can still be run directly at their original paths.

## Replaying an accepted record

1. Run `python3 scripts/research_index.py` to locate the latest acceptance record in this checkout.
2. Read its scope, replay instructions, input paths and dependency hashes. The detailed commands may live in the linked proof notes or checker headers.
3. Run the selected checker from the repository root with the recorded precision and saved input. `PYTHONPATH=.` makes root-level modules available to scripts in `research/`.
4. Compare the output with the named JSONL file. Keep new output outside the canonical evidence files while checking it.

For example, the following replays one checker from round 91:

```sh
PYTHONPATH=. OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 \
  .venv/bin/python -B research/real-two-marks-91-check.py \
  > /tmp/paley-real-two-marks-91-checks.jsonl
cmp research/real-two-marks-91-checks.jsonl /tmp/paley-real-two-marks-91-checks.jsonl
```

To compare the latest record's explicit file-hash maps and its previous-record pointer with local bytes:

```sh
python3 scripts/research_index.py --verify-latest
```

The hash check verifies only those recorded references. It does not replay computations, establish mathematical correctness, or certify a complete dependency closure.

## Historical command catalogue

The following commands and descriptions were carried over from the original README. They cover different experiments and scales; select the ones relevant to the note being examined. A full run of this catalogue is not a required check.

```sh
uv venv --python 3.12 .venv
uv pip install --python .venv/bin/python -r requirements.txt
.venv/bin/python theta.py --certify 5 13 41 101 401 809 1997
.venv/bin/python witnesses.py 1997 10009 50021 200009
.venv/bin/python feedback.py 10009 200009 1000033
.venv/bin/python feedback.py 401 10009 50021 200009 1000033 --fourth 0.001 0.05 1 4
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python smoothing.py 1997 10009 50021 200009
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python smoothing.py 10009 50021 200009 1000033 --tau 0.05 0.01 --norms
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python smoothing.py 200009 --tau 0.001 --max-steps 5000 --tolerance 1e-9 --certify
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python square_control.py 11 23 47 97 193 389 --prime-orders 113 521 2213 9413 37253 151337 --max-steps 4000
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python square_control.py 97 193 389 --prime-orders 9413 37253 151337 1000033 --max-steps 4000 --translations
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python sensitivity.py 9413 37253 151337 --square-characteristics 97 193 389
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python sensitivity.py 151337 --square-characteristics 389 --tau 0.2 0.5 1 2 --widths 0.0025 0.01 0.05
.venv/bin/python mobius_probe.py 401 10009 37253 50021 100049 1000033 1000000009 --square-characteristics 97 193 389 31627
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python subgroup_modes.py 401 10009 37253 50021 100049 1000033 --square-characteristics 97 193 389
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python critical_sets.py 401 9413 10009 37253 50021 100049 151337 1000033 --square-characteristics 97 193 389
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python progression_boxes.py 9413 37253 151337 1000033 --square-characteristics 97 193 389 997
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python response_shift.py 9413 37253 151337 1000033 --square-characteristics 97 193 389
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python response_shift.py 9601 37633 153649 --square-characteristics 97 193 389 --compare-cosets
.venv/bin/python coset_defects.py 8000 --max-offset 8
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python coset_bands.py 41 101 401 9601 37633 153649 --square-characteristics 7 11 23 97 193 389
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python stationary_modes.py 9413 37253 151337 --square-characteristics 97 193 389
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python response_windows.py 9413 37253 151337 --square-characteristics 97 193 389
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python response_windows.py 9413 37253 151337 --square-characteristics 97 193 389 --diagonal-damping
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python bulk_caps.py 9413 37253 151337 500209 1000033 --square-characteristics 97 193 389
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python log_means.py 9413 37253 151337 --square-characteristics 97 193 389 --count 33
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python signed_drift.py 401 1009 1997 9413 37253 151337 --square-characteristics 23 31 43 97 193 389
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python iterate_majorants.py 9413 37253 151337 500209 1000033 --square-characteristics 97 193 389 --certify-max-order 160000
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python iterate_majorants.py 151337 1000033 --square-characteristics 97 193 389 997 1999 --tau 0.05 --depths 2 4 8 16 32
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python coset_majorants.py 9601:96 37633:192 153649:388 1000033:947 --square-characteristics 97 193 389 --certify-max-order 160000 --quotient-lp-max-order 40000
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python face_ranks.py 5 13 17 29 37 41 --square-characteristics 3 5
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python rank_partitions.py 13 29 41 101 401 --square-characteristics 3 5 11 19 --samples 48
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python poisson_weights.py 9413 37253 --square-characteristics 97 193 --samples 32
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python poisson_weights.py 9413 37253 --square-characteristics 97 193 --samples 32 --counts 1 4 16 64 256 --law size-biased-poisson
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python two_mark_geometry.py 13 41 101 401 1009 1997 --square-characteristics 5 7 11 19 31 43 --shifts 24
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python two_mark_frontier.py 41 101 401 1009 1997 --square-characteristics 5 11 19 31 43 --shifts 12 --divisions 16
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python parallel_sparse_check.py
.venv/bin/python coset_phase_check.py
.venv/bin/python coset_phase_check.py --ranks 6 7 8 9 10 11 12 --orders 30 36 60 72 90 120 150 180 210 240 360 --samples 384
.venv/bin/python coset_phase_certificate.py 6 7 8
.venv/bin/python coset_phase_certificate.py --symmetric --small-primes-only 8 9 10 11
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python coset_activation_probe.py 9413 37253 153649 --square-characteristics 97 193 389
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python stationary_attenuation.py 9413 37253 153649 --square-characteristics 97 193 389 --tau 0.05 0.01 0.002
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python stationary_ordered.py 9413 37253 153649 --square-characteristics 97 193 389 --tau 0.05 0.005 0.0005
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python stationary_secant.py 401 9413 37253 153649 --square-characteristics 19 97 193 389 --tau 0.05 0.01 --depths 16 64 256 1024
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python stationary_defect_tail.py 401 9413 37253 --square-characteristics 19 97 193 --eta-scale 0.1 --tau 0.01 0.0005 --times 32 128 512
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python stationary_mark_constant.py 9413 37253 153649 --square-characteristics 97 193 389 --tau 0.01 0.0005 --alpha 0.5 1
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python stationary_mark_constant.py 1008001 --tau 0.0005 --alpha 0.5 1
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python stationary_mark_constant.py 1000033 --tau 0.0005 --alpha 1
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python neighbor_compression.py --primes 5 13 401 9413 37253 153649 --square-bases 3 19 97 193 389
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python neighbor_compression.py --primes 1000033 --square-bases 997
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python negative_pairing.py 101 401 1997 9413 37253 153649 --square-characteristics 11 19 43 97 193 389 --tau 0.005 0.0005
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python negative_pairing.py 101 401 1997 9413 37253 153649 --square-characteristics 11 19 43 97 193 389 --tau 0 --certify-max-order 10000
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python negative_pairing.py 1000033 --square-characteristics 997 --tau 0 0.0005
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python quadratic_theta.py 13 101 401 9413 37253 153649 --square-characteristics 3 11 19 97 193 389 --widths 1 0.25 0.05 0.01 --scaled-widths 2 1 0.25 0.0625
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python quadratic_theta.py 13 101 401 9413 --square-characteristics 3 11 19 97 --widths 0.25 0.05 --scaled-widths 1 0.25 --rounds 32 --certify-max-order 10000
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python endpoint_norm.py 5 13 17 41 61 97 101 173 401 809 1009 1997 --square-characteristics 3 5 7 11 13 19 23 31 43 --certify-max-order 1009
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python endpoint_norm.py 4001 6257 9413 --square-characteristics 61 79 97
.venv/bin/python endpoint_extension_certificate.py
.venv/bin/python square_endpoint_rank.py
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python endpoint_tangent.py 5 13 17 41 61 97 101 173 401 809 1009 1997 4001 6257 9413 --square-characteristics 3 5 7 11 13 19 23 31 43 61 79 97 --check-max-order 401
.venv/bin/python endpoint_tangent_certificate.py
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python one_sided_penalty.py 401 809 1997 9413 --square-characteristics 19 43 97 --certify-max-order 9413
.venv/bin/python parallel_kernel_11.py --certify-p97-gap
.venv/bin/python -B research/astra-convolution-11.py --certificate
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python quadratic_fourth.py 61 401 1997 9413 37253 153649 --square-characteristics 7 19 43 97 193 389 --widths .25 .0625 .015625 --scaled-widths .25 1 4 --certify-max-order 153649
.venv/bin/python parallel_sampling_12.py --certify-p29
.venv/bin/python -B research/astra-fourth-12.py --certificate
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python quadratic_compression.py 13 61 97 401 1997 9413 --square-characteristics 7 11 19 43 97 --certify-max-order 401
.venv/bin/python -B research/astra-energy-13.py --certificate
.venv/bin/python research/parallel-complexity-14.py
.venv/bin/python -B research/astra-sampling-14.py --certificate
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python quadratic_gap.py 13 61 97 401 1997 9413 37253 153649 1000033 --square-characteristics 7 11 19 43 97 193 389 997 --certify-max-order 1000033
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python quadratic_angle.py 61 401 1997 9413 37253 153649 --square-characteristics 7 19 43 97 193 389 --width-factors 1.02 1.5 4 --reference-widths .5 --certify-max-order 153649
.venv/bin/python -B research/astra-cuts-15.py --certificate
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python -B research/parallel-transport-15.py
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python -B research/parallel-defect-16.py --certificate
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python -B research/astra-source-16.py
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python endpoint_mixture.py 1009 1997 4001 9413 --certify-max-order 9413 --budget 80 --gauge residual
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python rational_endpoint.py 29 173 509 1109 2693 9533 --square-characteristics 11 43 97 --one-fraction
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python -B research/parallel-repair-17.py --certify-max-order 1000033
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python -B research/astra-preimage-17.py --certificate
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python exterior_focus.py 9413 37253 153649 --square-characteristics 97 193 389
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python -B research/one-sided-quadratic-22.py 1000033 --steps 256 --certify-max-order 1000033
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python -B research/square-pinned-22.py
```

`theta.py` solves both LPs independently. With `--certify` it uses rational cosine intervals to make the rounded Fourier rows feasible and reports lower and upper bounds as exact fractions. `smoothing.py --certify` obtains larger-instance certificates by checking rounded FFT candidates with FLINT/Arb. The plain LPs, restricted witnesses, and smoothing diagnostics report floating-point results. See [data](../data/) for the recorded runs.

`square_control.py` constructs the sign masks over quadratic extensions by taking norms to the prime field. It compares smoothing at $r^2$ and nearby prime orders and records how much of the iterate lies on frequencies trivial on the subfield clique. The `--translations` run measures the [translation deficit and subgroup-coset mass](../research/translation.md).

`sensitivity.py` computes the [marked response](../research/marked-response.md) using the symmetric linearization of the smoothing equation. The `--widths` run also measures the regularized inverse entry and the corresponding filtered spectral mass. The output includes the residuals of the solves.

`mobius_probe.py` counts exact intersections of subgroups at the square-root scale under the [Möbius conjugation](../research/mobius.md). The square-order controls use the closed subfield formula.

`subgroup_modes.py` compares the [subgroup compression](../research/subgroup-modes.md) with the actual marked response. It obtains the eigenvalues of each cyclic compression directly from the sign sums on positional cosets.

`critical_sets.py` searches for frequency supports at the [smallest scale allowed for a slow mode](../research/critical-sets.md). It records the mean deficit from the squared Jacobi bound, additive energy, and signed compression norm for random sets, intervals, exact-size subgroups, and greedy and swap candidates.

`progression_boxes.py` compares two families of [rank-two frequency boxes](../research/progression-boxes.md) with intervals and square subfield supports.

`response_shift.py` compares prescribed saturating diagonals using the [exact marked-response formula](../research/response-locality.md). The `--compare-cosets` run [tests the effect of translating a subgroup support](../research/coset-response.md). For the unshifted support, [the positional coset sums give a closed formula](../research/unshifted-cosets.md).

`coset_defects.py` enumerates exact quadratic sign sums on the self-inverse cosets at near-square prime orders. The [bounded-defect notes](../research/coset-defects.md) compare the scan with exact correlations and cyclotomic constraints.

`coset_bands.py` compares the [one-sided spectral bounds](../research/signed-coset-bands.md) for unions of one, two, and three frequency cosets at the numerical stationary diagonal. Small orders also report the actual spectral gaps from a dense mean-zero solve.

`stationary_modes.py` probes [the actual stationary linearization](../research/stationary-tails.md) by marked inverse iteration and reports the coupling, residuals, and mass of the high set.

`response_windows.py` compares the positive and negative contributions to the regularized response and checks the [stationary resolvent sum rule and the signed cutoff identity](../research/resolvent-sum-rule.md). With `--diagonal-damping` it uses [the real damped inverse and its stationary pairing](../research/diagonal-damping.md).

`bulk_caps.py` compares [capped Fourier mass and the two high sets](../research/bulk-caps.md) at fixed Picard depths and near stationarity. It reports the capped feedback, the excess above each cap, and the density of the difference set of the two high sets.

`log_means.py` checks the mixed-product identities at pairs of smoothing weights and measures [the signed bulk logarithmic mean](../research/bulk-logarithm.md) that determines the theta value by integration.

`signed_drift.py` compares [the one-sided iterate correlations](../research/signed-drift.md) against the stationary spectra and against the two Fourier LPs with the iterates as costs.

`iterate_majorants.py` repairs averaged iterate spectra with [translated Fourier witnesses](../research/iterate-majorants.md). It compares scalar and translated repairs and optionally certifies the resulting theta bounds with interval Fourier transforms.

`coset_majorants.py` adds [frequency-coset mass bounds and quotient Fourier constraints](../research/coset-majorants.md) to the point repair. It compares a prescribed coset plateau with the actual iterate costs.

`face_ranks.py` checks the two-label term of the [rank expansion over random frequency weights](../research/random-weight-ranks.md) against the ordinary theta LPs and a separate integration of the log objectives.

`rank_partitions.py` measures the [exterior sign partition and localized eigenspace dimensions](../research/rank-partitions.md) at randomly sampled weights and compares them to projected polytope ranks at small orders.

`poisson_weights.py` computes [signed log intervals](../research/poisson-smoothing.md) by projecting FFT iterates onto the two Fourier spaces. It reports the interval width and the Monte Carlo standard error for fixed and size-biased Poisson label counts.

`two_mark_geometry.py` computes the [two-frequency diagonal heights and bounds on the first rank term](../research/sparse-mark-geometry.md) from the Fourier LPs with midpoint reflection.

`two_mark_frontier.py` adds [off-diagonal linear costs](../research/two-mark-support.md), which give inner and outer polygons for the two-frequency normalized projection and narrow the bounds on the same rank term.

`parallel_sparse_check.py` checks the [sparse Poisson comparison and deterministic mass profiles](../research/parallel-sparse.md) against scalar quadrature and square-order FFT intervals.

`coset_phase_check.py` checks the cyclic difference problem from the [critical coset phase reduction](../research/critical-coset-phases.md) by exact cyclotomic division and clique search.

`coset_phase_certificate.py` exhausts the possible cyclic phase profiles for six through eight critical cosets and extends the check to eleven when the spectrum is even.

`coset_activation_probe.py` measures the [interaction in the marked response](../research/coset-activation.md) between selected frequency cosets and the rest of the stationary diagonal.

`exterior_focus.py` compares a [bounded centered exterior](../research/exterior-column.md) designed to concentrate the marked column on two frequencies with an exterior obtained from the stationary diagonal.

`stationary_attenuation.py` replays the [weighted transfer under sitewise changes](../research/stationary-attenuation.md) for deletions and partial attenuation at the actual stationary diagonal.

`stationary_ordered.py` replays the [exact opposite-spectrum pairing and weighted norm law](../research/stationary-ordered.md) under one-sided changes of the stripped stationary diagonal.

`stationary_secant.py` checks the [half-angle marked inverse and midpoint residual bound](../research/stationary-secant.md), including the weighted residual costs on small fields.

`stationary_defect_tail.py` computes the [averaged half-angle tail and its signed low-mode part](../research/stationary-defect-tail.md).

`stationary_mark_constant.py` checks the [two-dimensional defect relation](../research/stationary-mark-constant.md) between the marked and constant sources of each one-sign block.

`neighbor_compression.py` compares the [extreme signed eigenvalues of the additive Paley operator on two-vertex sign sets](../research/additive-neighbor-compression.md) over prime and prime-square orders. It also measures the mean and norm of the image of the normalized constant vector.

`negative_pairing.py` compares the [negative cost of an exactly projected iterate](../research/negative-pairing.md) against the stationary opposite spectrum, the worst feasible opposite spectrum, and point-cap upper bounds. With `--tau 0` it omits the stationary solve. The translated negative-part repair can be certified with interval arithmetic.

`quadratic_theta.py` solves the [reciprocal quadratic regularization](../research/quadratic-theta.md) numerically and reports both sides of its residual bracket. The interval mode certifies the regularized quadratic value using rational rounded trials and two Fourier energy bounds.

`endpoint_norm.py` compares the [least-norm endpoints and their marked compression spectra](../research/endpoint-norm.md). The separate `endpoint_extension_certificate.py` checks the nonnegative extension cost at $p=97$ over the cyclotomic field, and `square_endpoint_rank.py` certifies the finite cases in [square endpoint uniqueness](../research/square-endpoint-uniqueness.md).

`endpoint_tangent.py` compares [the first support changes and their mark sensitivity](../research/endpoint-tangent.md) for the one-sided penalty. The separate `endpoint_tangent_certificate.py` uses Arb to certify the first change and subsequent mark loss on the larger-theta side at $p=809$.

`one_sided_penalty.py` encloses [marks along the same penalty path](../data/one-sided-penalty.csv) from a feasible repair and a quadratic primal–dual gap, with interval arithmetic independent of the support.

`quadratic_fourth.py` certifies [allowed energies, fourth moments and the signed width derivative](../research/quadratic-fourth.md) from two rounded positive trials. The proof also gives the one-sided reduction from a single moving width.

`quadratic_compression.py` compares the [mean and centered mark costs on actual quadratic supports](../research/quadratic-compression.md). It reconstructs both supports at the sampled widths and can certify their strict optimality conditions with Arb.

`quadratic_gap.py` certifies [upper bounds for the allowed energy](../research/quadratic-gap.md) from a single larger-width trial per sign. With `--skip-target-solve`, the target-width solve used for the floating-point comparison is omitted.

`quadratic_angle.py` uses [two reference inner products](../research/quadratic-angle.md) to enclose normalized allowed energy and the signed width derivative. The [signed cut notes](../research/astra-cuts-15.md) and [dual repair notes](../research/parallel-transport-15.md) give two arithmetic targets for the prime limit.

`endpoint_mixture.py` combines [projected references and selected Fourier tests](../research/endpoint-mixture.md) to certify ordinary theta endpoint bounds. The [positive repair replay](../research/parallel-defect-16.md) tests the available mass reserve at prime and square orders.

`rational_endpoint.py` checks [cyclotomic lower bounds on forbidden energy](../research/rational-endpoint.md) for rational and single-fraction endpoint candidates. The [four-step repair](../research/parallel-repair-17.md) and [localized source response](../research/astra-preimage-17.md) give explicit tests for the two remaining uniform estimates.

The [ratio and resolvent replays](../research/parallel-ratio-18.md) compare three finishes of the four-step repair and certify their ordinary theta bounds. The [bulk-tail recurrence](../research/parallel-tail-18.md) tests peak transfer and background injection on primes and square controls. The [low-layer certificates](../research/astra-low-layer-18.md) test how much signed root response a small primal layer can carry. Each note includes its replay commands and saved data.

The [thresholded repair](../research/threshold-repair-19.md) compares a positive active-set inverse and signed Fourier iteration. The [Jacobi rectangle analysis](../research/parallel-cap-19.md) gives an obstruction for arbitrary source weights and a constraint for actual near-unit runs. The [Picard reference comparison](../research/astra-background-19.md) gives exact finite-prime tail certificates and prime-square diagnostics.

The [fixed-mark repair](../research/anchored-repair-20.md) certifies both Fourier sectors, gives the exact defect dual, and uses the [prime coset gap](../research/parallel-rectangle-20.md) to prove signed contraction for high-energy defects near critical effective size. [The signed descent replay](../research/astra-signed-20.md) tracks support changes and the marked charge when the mark is omitted.

The [quadratically smoothed repair tail](../research/soft-tail-21.md) isolates broad dual witnesses and includes finite interval bounds. [The actual-reference penalty](../research/astra-broad-21.md) and the [twisted cross-ratio tests](../research/parallel-crossratio-21.md) identify the missing tail and correlation estimates.
