# Python tools

This catalogue covers **318 Python files** from published snapshot [76b8dfc](https://github.com/lyw-ops/Paleygraph1/tree/76b8dfcf21e4276cb56320bf8f699215a0566ce3). It is built from Git objects, so uncommitted files are excluded.

## One entry point

Listing and inspecting tools use only the Python standard library. Use the project interpreter to run mathematical programs after installing [requirements.txt](../requirements.txt).

```sh
python3 scripts/paley.py list
python3 scripts/paley.py list --group response
python3 scripts/paley.py list --round 91
python3 scripts/paley.py show theta
.venv/bin/python -B scripts/paley.py run theta --certify 5 13 41
.venv/bin/python -B scripts/paley.py run research/real-two-marks-91-check.py
```

`list` shows the shared tools and maintenance utilities by default; `--all` includes the round archive. Tool selectors accept a catalogue path, or a unique filename or stem. `show` reads catalogue metadata without importing the selected program.

`run` uses the interpreter that invoked this entry point, executes the existing file from the repository root and adds that root to `PYTHONPATH`. Arguments, stdout, stderr and exit status belong to the selected program. Relative input/output paths are resolved from the repository root. A run uses this checkout, including any local modifications; the catalogue is not a frozen execution environment.

Original paths, imports and direct commands remain available. Some round scripts have fixed parameters and run immediately; use `show` to inspect their description before execution.

## Shared tools by function

### Theta and witnesses

The ordinary theta programs and explicit witness families.

| Source | Purpose |
| --- | --- |
| [theta.py](../theta.py) | Compute and certify ordinary theta for both Paley localization supports. |
| [witnesses.py](../witnesses.py) | Compare low-dimensional, edge-supported theta witness families. |

### Smoothing and signed iterates

Fourier smoothing, mixed feedback and signed drift.

| Source | Purpose |
| --- | --- |
| [feedback.py](../feedback.py) | Measure mixed correlations and fourth-update terms in Fourier smoothing. |
| [log_means.py](../log_means.py) | Probe the mean bulk logarithm along the Paley smoothing path. |
| [signed_drift.py](../signed_drift.py) | Compare signed iterate correlations with stationary and LP spectra. |
| [smoothing.py](../smoothing.py) | Probe the marked coordinate in complementary Fourier smoothing. |
| [square_control.py](../square_control.py) | Compare smoothing over prime and prime-square field orders. |

### Stationary response

Marked response, resolvents, stationary modes and sitewise changes.

| Source | Purpose |
| --- | --- |
| [coset_activation_probe.py](../coset_activation_probe.py) | Compare marked inverses after splitting the stationary diagonal by cosets. |
| [exterior_focus.py](../exterior_focus.py) | Compare an exterior chosen by Jacobi products with a stationary reference. |
| [response_shift.py](../response_shift.py) | Replay the marked response for a prescribed, nearly saturated frequency set. |
| [response_windows.py](../response_windows.py) | Compare signed resolvent windows and the mixed stationary tail at the mark. |
| [sensitivity.py](../sensitivity.py) | Measure the theta certificate's response to the marked smoothing weight. |
| [stationary_attenuation.py](../stationary_attenuation.py) | Check the weighted transfer identities for sitewise diagonal changes. |
| [stationary_defect_tail.py](../stationary_defect_tail.py) | Separate the low dissipation modes in the averaged half-angle tail. |
| [stationary_mark_constant.py](../stationary_mark_constant.py) | Compare marked and constant responses in each stationary sign block. |
| [stationary_modes.py](../stationary_modes.py) | Probe the coupling of a near-zero direction to the stationary Paley iterate. |
| [stationary_ordered.py](../stationary_ordered.py) | Replay the one-sided weighted bulk identities at a stationary pair. |
| [stationary_secant.py](../stationary_secant.py) | Compare a half-angle inverse and weighted trial residuals at Paley orders. |
| [subgroup_modes.py](../subgroup_modes.py) | Compare Paley subgroup compressions with the stationary marked response. |

### Witness repair

Point, coset and negative-part repairs of proposed witnesses.

| Source | Purpose |
| --- | --- |
| [bulk_caps.py](../bulk_caps.py) | Compare capped stationary Fourier mass with fixed-depth smoothing. |
| [coset_majorants.py](../coset_majorants.py) | Compare Fourier repairs that combine point and subgroup-coset witnesses. |
| [endpoint_mixture.py](../endpoint_mixture.py) | Combine projected reference trials and selected Fourier tests at the theta endpoint. |
| [iterate_majorants.py](../iterate_majorants.py) | Build Fourier certificates from averaged iterates and translated witnesses. |
| [negative_pairing.py](../negative_pairing.py) | Compare the projected-iterate negative pairing with stationary-free bounds. |

### Quadratic regularization

Regularized programs, energy bounds and one-sided penalties.

| Source | Purpose |
| --- | --- |
| [one_sided_penalty.py](../one_sided_penalty.py) | Measure and enclose marks at fixed inverse penalties along the one-sided path. |
| [quadratic_angle.py](../quadratic_angle.py) | Certify normalized sector energies using a single larger-width trial. |
| [quadratic_compression.py](../quadratic_compression.py) | Measure the two marked compression costs on the actual quadratic support. |
| [quadratic_fourth.py](../quadratic_fourth.py) | Enclose the reciprocal theta path's fourth moments and signed derivative. |
| [quadratic_gap.py](../quadratic_gap.py) | Bound one sign's energy at a width from a nonnegative larger-width trial. |
| [quadratic_theta.py](../quadratic_theta.py) | Evaluate reciprocal regularized Paley theta programs by FFT. |
| [rational_endpoint.py](../rational_endpoint.py) | Test rational rooted Paley spectra using exact primitive-layer resultants. |

### Endpoint geometry

Endpoint supports, tangents, extensions and exact finite checks.

| Source | Purpose |
| --- | --- |
| [endpoint_extension_certificate.py](../endpoint_extension_certificate.py) | Check an endpoint extension with a genuinely active nonnegativity constraint at p=97. |
| [endpoint_norm.py](../endpoint_norm.py) | Probe least-norm theta endpoints and marked support compressions. |
| [endpoint_tangent.py](../endpoint_tangent.py) | Compare the first one-sided penalty switch and its mark sensitivity. |
| [endpoint_tangent_certificate.py](../endpoint_tangent_certificate.py) | Certify the first one-sided switch on the larger theta side at p=809. |
| [parallel_kernel_11.py](../parallel_kernel_11.py) | Replay marked endpoint norm bounds using the paired-support linear programs. |
| [parallel_sampling_12.py](../parallel_sampling_12.py) | Replay folded support counts and centered leakage on Paley interval samples. |
| [square_endpoint_rank.py](../square_endpoint_rank.py) | Certify the finite cases in square-endpoint uniqueness by exact modular rank. |

### Cosets, ranks and sparse geometry

Subgroups, phase profiles, ranks and sparse frequency models.

| Source | Purpose |
| --- | --- |
| [coset_bands.py](../coset_bands.py) | Compare signed spectral gaps on unions of frequency cosets. |
| [coset_defects.py](../coset_defects.py) | Enumerate sign defects on self-inverse cosets at near-square prime orders. |
| [coset_phase_certificate.py](../coset_phase_certificate.py) | Exhaust the necessary Fourier profiles for a critical coset cover. |
| [coset_phase_check.py](../coset_phase_check.py) | Check difference cliques for cyclic sums of equally weighted characters. |
| [critical_sets.py](../critical_sets.py) | Search for critical-size frequency sets with small mean Jacobi deficit. |
| [face_ranks.py](../face_ranks.py) | Check the two-label rank integral for small Paley localizations. |
| [mobius_probe.py](../mobius_probe.py) | Count overlaps of subgroups under the Möbius map on square roots. |
| [neighbor_compression.py](../neighbor_compression.py) | Measure the largest signed additive Paley eigenvalue on common neighbors. |
| [parallel_sparse_check.py](../parallel_sparse_check.py) | Recheck the collision comparison and deterministic sparse square control. |
| [poisson_weights.py](../poisson_weights.py) | Probe random sparse frequency weights with the FFT log certificate. |
| [progression_boxes.py](../progression_boxes.py) | Compare critical-size frequency boxes, intervals, and subfield controls. |
| [rank_partitions.py](../rank_partitions.py) | Measure the exterior signs and localized eigenspaces at random weights. |
| [two_mark_frontier.py](../two_mark_frontier.py) | Enclose two-mark rank integrals using several linear Fourier LP costs. |
| [two_mark_geometry.py](../two_mark_geometry.py) | Compute the diagonal of the two-frequency projected Fourier polytopes. |

### Repository maintenance

Navigation, catalogue generation and maintenance tests.

| Source | Purpose |
| --- | --- |
| [research_index.py](../scripts/research_index.py) | Summarize acceptance records and maintain the research navigation page. |

## Research-round archive

Round labels below come from filenames. They do not establish acceptance or proof status; consult the [acceptance-record index](../research/README.md) and the associated notes.

| Round | Scripts |
| --- | --- |
| 92 | [astra-height-92-check.py](../research/astra-height-92-check.py), [astra-price-92-check.py](../research/astra-price-92-check.py), [astra-velocity-92-check.py](../research/astra-velocity-92-check.py), [cap-sweep-92-check.py](../research/cap-sweep-92-check.py) |
| 91 | [astra-contact-91-check.py](../research/astra-contact-91-check.py), [astra-discount-91-check.py](../research/astra-discount-91-check.py), [astra-fiber-91-check.py](../research/astra-fiber-91-check.py), [real-two-marks-91-check.py](../research/real-two-marks-91-check.py) |
| 90 | [astra-affine-90-check.py](../research/astra-affine-90-check.py), [astra-column-90-check.py](../research/astra-column-90-check.py), [astra-dual-90-check.py](../research/astra-dual-90-check.py), [clipped-signs-90-check.py](../research/clipped-signs-90-check.py) |
| 89 | [astra-linear-89-check.py](../research/astra-linear-89-check.py), [astra-quartic-89-check.py](../research/astra-quartic-89-check.py), [astra-tails-89-check.py](../research/astra-tails-89-check.py), [real-phase-projection-89-check.py](../research/real-phase-projection-89-check.py) |
| 88 | [astra-matched-88-check.py](../research/astra-matched-88-check.py), [astra-persistent-88-check.py](../research/astra-persistent-88-check.py), [astra-source-88-check.py](../research/astra-source-88-check.py), [physical-two-floor-88-check.py](../research/physical-two-floor-88-check.py) |
| 87 | [astra-diffuse-87-check.py](../research/astra-diffuse-87-check.py), [astra-forced-87-check.py](../research/astra-forced-87-check.py), [astra-terminal-87-check.py](../research/astra-terminal-87-check.py) |
| 86 | [astra-fibers-86-check.py](../research/astra-fibers-86-check.py), [astra-leverage-86-check.py](../research/astra-leverage-86-check.py), [astra-phase-86-check.py](../research/astra-phase-86-check.py) |
| 85 | [astra-compression-85-check.py](../research/astra-compression-85-check.py), [astra-cubic-85-check.py](../research/astra-cubic-85-check.py), [astra-overflow-85-check.py](../research/astra-overflow-85-check.py) |
| 84 | [astra-capacity-84-check.py](../research/astra-capacity-84-check.py), [astra-complement-84-check.py](../research/astra-complement-84-check.py), [astra-imaginary-84-check.py](../research/astra-imaginary-84-check.py) |
| 83 | [astra-average-83-check.py](../research/astra-average-83-check.py), [astra-direction-83-check.py](../research/astra-direction-83-check.py), [astra-direction-83-invariant.py](../research/astra-direction-83-invariant.py), [astra-split-83-check.py](../research/astra-split-83-check.py) |
| 82 | [astra-adjoint-82-check.py](../research/astra-adjoint-82-check.py), [astra-adjoint-82-homotopy-check.py](../research/astra-adjoint-82-homotopy-check.py), [astra-optimal-82-check.py](../research/astra-optimal-82-check.py) |
| 81 | [astra-cover-81-check.py](../research/astra-cover-81-check.py), [astra-mixed-81-check.py](../research/astra-mixed-81-check.py) |
| 80 | [astra-dissipation-80-check.py](../research/astra-dissipation-80-check.py), [astra-surviving-80-check.py](../research/astra-surviving-80-check.py) |
| 79 | [astra-excess-79-check.py](../research/astra-excess-79-check.py) |
| 78 | [astra-height-78-check.py](../research/astra-height-78-check.py) |
| 77 | [astra-newton-77-check.py](../research/astra-newton-77-check.py), [astra-schur-77-check.py](../research/astra-schur-77-check.py) |
| 76 | [astra-masked-76-check.py](../research/astra-masked-76-check.py), [astra-predictor-76-check.py](../research/astra-predictor-76-check.py) |
| 75 | [astra-fourth-75-check.py](../research/astra-fourth-75-check.py), [astra-quotient-75-check.py](../research/astra-quotient-75-check.py) |
| 74 | [astra-cap-74-check.py](../research/astra-cap-74-check.py) |
| 72 | [astra-arities-72-check.py](../research/astra-arities-72-check.py), [astra-face-72-check.py](../research/astra-face-72-check.py) |
| 71 | [astra-histories-71-check.py](../research/astra-histories-71-check.py), [astra-histories-71-escape.py](../research/astra-histories-71-escape.py), [translated-caps-71-check.py](../research/translated-caps-71-check.py) |
| 70 | [astra-direction-70-check.py](../research/astra-direction-70-check.py), [astra-new-sectors-70-check.py](../research/astra-new-sectors-70-check.py), [paired-windows-70-check.py](../research/paired-windows-70-check.py) |
| 69 | [astra-forced-69-check.py](../research/astra-forced-69-check.py), [astra-unary-69-base.py](../research/astra-unary-69-base.py), [astra-unary-69-check.py](../research/astra-unary-69-check.py), [astra-unary-69-prices.py](../research/astra-unary-69-prices.py), [astra-unary-69-sector.py](../research/astra-unary-69-sector.py), [timed-pinning-69-check.py](../research/timed-pinning-69-check.py) |
| 68 | [astra-nonlinear-68-check.py](../research/astra-nonlinear-68-check.py), [astra-nonlinear-68-periodic.py](../research/astra-nonlinear-68-periodic.py), [astra-nonlinear-68-probe.py](../research/astra-nonlinear-68-probe.py), [shifted-groups-68-check.py](../research/shifted-groups-68-check.py) |
| 67 | [astra-rank-six-67-check.py](../research/astra-rank-six-67-check.py), [astra-rank-six-67-linear.py](../research/astra-rank-six-67-linear.py) |
| 66 | [astra-shifted-66-check.py](../research/astra-shifted-66-check.py), [astra-shifted-66-collision.py](../research/astra-shifted-66-collision.py), [terminal-step-66-check.py](../research/terminal-step-66-check.py) |
| 65 | [astra-charged-65-check.py](../research/astra-charged-65-check.py), [astra-joint-65-check.py](../research/astra-joint-65-check.py) |
| 64 | [astra-coupling-64-check.py](../research/astra-coupling-64-check.py), [astra-joint-64-check.py](../research/astra-joint-64-check.py), [astra-joint-64-probe.py](../research/astra-joint-64-probe.py), [mean-energy-64-check.py](../research/mean-energy-64-check.py) |
| 63 | [astra-global-63-check.py](../research/astra-global-63-check.py), [astra-legendre-63-check.py](../research/astra-legendre-63-check.py), [astra-legendre-63-probe.py](../research/astra-legendre-63-probe.py), [true-spill-63-check.py](../research/true-spill-63-check.py) |
| 62 | [astra-primitive-62-check.py](../research/astra-primitive-62-check.py), [astra-weighted-62-check.py](../research/astra-weighted-62-check.py) |
| 61 | [astra-charged-61-check.py](../research/astra-charged-61-check.py), [astra-mixed-61-check.py](../research/astra-mixed-61-check.py), [astra-mixed-61-probe.py](../research/astra-mixed-61-probe.py) |
| 60 | [astra-halfturn-60-check.py](../research/astra-halfturn-60-check.py), [astra-rankeight-60-check.py](../research/astra-rankeight-60-check.py), [signed-compact-60-check.py](../research/signed-compact-60-check.py) |
| 59 | [astra-crossnode-59-check.py](../research/astra-crossnode-59-check.py), [astra-flow-59-check.py](../research/astra-flow-59-check.py), [compact-variance-59-check.py](../research/compact-variance-59-check.py), [two-node-groups-59-check.py](../research/two-node-groups-59-check.py) |
| 58 | [astra-jointface-58-check.py](../research/astra-jointface-58-check.py), [astra-ranknext-58-check.py](../research/astra-ranknext-58-check.py), [astra-ranknext-58-probe.py](../research/astra-ranknext-58-probe.py), [distinguished-positive-58-check.py](../research/distinguished-positive-58-check.py) |
| 57 | [astra-face-57-check.py](../research/astra-face-57-check.py), [astra-rankfour-57-check.py](../research/astra-rankfour-57-check.py), [astra-rankfour-57-probe.py](../research/astra-rankfour-57-probe.py), [weighted-arithmetic-57-check.py](../research/weighted-arithmetic-57-check.py), [weighted-positive-57-check.py](../research/weighted-positive-57-check.py) |
| 56 | [astra-rankthree-56-check.py](../research/astra-rankthree-56-check.py), [astra-rankthree-56-probe.py](../research/astra-rankthree-56-probe.py), [astra-tail-56-check.py](../research/astra-tail-56-check.py), [centered-positive-56-check.py](../research/centered-positive-56-check.py), [rank-four-arithmetic-56-check.py](../research/rank-four-arithmetic-56-check.py) |
| 55 | [astra-rankthree-55-check.py](../research/astra-rankthree-55-check.py), [astra-translated-55-check.py](../research/astra-translated-55-check.py), [rank-four-positive-55-check.py](../research/rank-four-positive-55-check.py) |
| 54 | [astra-face-54-check.py](../research/astra-face-54-check.py), [astra-signed-54-check.py](../research/astra-signed-54-check.py), [nested-positive-54-check.py](../research/nested-positive-54-check.py) |
| 53 | [astra-histogram-53-check.py](../research/astra-histogram-53-check.py), [astra-tail-53-check.py](../research/astra-tail-53-check.py), [marked-domain-53-check.py](../research/marked-domain-53-check.py) |
| 52 | [astra-feedback-52-check.py](../research/astra-feedback-52-check.py), [astra-transport-52-check.py](../research/astra-transport-52-check.py), [prime-increments-52-check.py](../research/prime-increments-52-check.py) |
| 51 | [astra-late-51-check.py](../research/astra-late-51-check.py), [astra-warm-51-check.py](../research/astra-warm-51-check.py), [marked-affinity-51-check.py](../research/marked-affinity-51-check.py) |
| 50 | [astra-coupling-50-check.py](../research/astra-coupling-50-check.py), [astra-ref-50-check.py](../research/astra-ref-50-check.py), [reference-curvature-50-check.py](../research/reference-curvature-50-check.py) |
| 49 | [astra-drift-49-check.py](../research/astra-drift-49-check.py), [astra-odd-49-check.py](../research/astra-odd-49-check.py), [paired-trial-49-check.py](../research/paired-trial-49-check.py) |
| 48 | [astra-coset-48-check.py](../research/astra-coset-48-check.py), [astra-stencil-48-check.py](../research/astra-stencil-48-check.py), [static-trial-48-check.py](../research/static-trial-48-check.py) |
| 47 | [astra-measure-47-check.py](../research/astra-measure-47-check.py), [astra-secant-47-check.py](../research/astra-secant-47-check.py), [seed-majorant-47-check.py](../research/seed-majorant-47-check.py) |
| 46 | [astra-face-46-check.py](../research/astra-face-46-check.py), [astra-pick-46-check.py](../research/astra-pick-46-check.py) |
| 45 | [astra-endpoint-45-check.py](../research/astra-endpoint-45-check.py), [astra-strip-45-check.py](../research/astra-strip-45-check.py), [astra-strip-45-loewner.py](../research/astra-strip-45-loewner.py), [astra-strip-45-pick.py](../research/astra-strip-45-pick.py), [endpoint-direction-45-check.py](../research/endpoint-direction-45-check.py) |
| 44 | [astra-critical-44-check.py](../research/astra-critical-44-check.py), [astra-curve-44-check.py](../research/astra-curve-44-check.py), [critical-shell-44-check.py](../research/critical-shell-44-check.py) |
| 43 | [astra-cold-43-check.py](../research/astra-cold-43-check.py), [astra-rooted-43-check.py](../research/astra-rooted-43-check.py), [generator-blocking-43-check.py](../research/generator-blocking-43-check.py) |
| 42 | [astra-witness-resume-42-check.py](../research/astra-witness-resume-42-check.py), [quadratic-mark-42-check.py](../research/quadratic-mark-42-check.py) |
| 41 | [astra-branch-41-check.py](../research/astra-branch-41-check.py), [astra-repair-41-check.py](../research/astra-repair-41-check.py), [twisted-lattice-defect-41-check.py](../research/twisted-lattice-defect-41-check.py) |
| 40 | [astra-completion-40-check.py](../research/astra-completion-40-check.py), [astra-scalar-40-check.py](../research/astra-scalar-40-check.py), [twisted-coset-defect-40-check.py](../research/twisted-coset-defect-40-check.py) |
| 39 | [astra-complex-39-check.py](../research/astra-complex-39-check.py), [astra-positive-39-check.py](../research/astra-positive-39-check.py), [twisted-coset-occupancy-39-check.py](../research/twisted-coset-occupancy-39-check.py) |
| 38 | [astra-prime-repair-38-thresholds.py](../research/astra-prime-repair-38-thresholds.py), [astra-prime-repair-38.py](../research/astra-prime-repair-38.py), [astra-surface-38-check.py](../research/astra-surface-38-check.py) |
| 37 | [astra-cold-37-monodromy.py](../research/astra-cold-37-monodromy.py), [astra-cold-37.py](../research/astra-cold-37.py), [astra-completion-37-check.py](../research/astra-completion-37-check.py), [astra-completion-37.py](../research/astra-completion-37.py), [picard-transfer-37-check.py](../research/picard-transfer-37-check.py) |
| 36 | [astra-averaged-positive-36.py](../research/astra-averaged-positive-36.py), [endpoint-stress-36.py](../research/endpoint-stress-36.py), [marked-pick-jets-36.py](../research/marked-pick-jets-36.py), [parallel-audit-36.py](../research/parallel-audit-36.py), [parallel-cold-complex-36.py](../research/parallel-cold-complex-36.py) |
| 35 | [astra-signed-repair-35.py](../research/astra-signed-repair-35.py), [averaged-mark-35.py](../research/averaged-mark-35.py), [parallel-audit-35.py](../research/parallel-audit-35.py), [parallel-complex-structure-35.py](../research/parallel-complex-structure-35.py) |
| 34 | [astra-conic-primal-34.py](../research/astra-conic-primal-34.py), [complex-branches-34.py](../research/complex-branches-34.py), [parallel-audit-34.py](../research/parallel-audit-34.py), [parallel-schur-response-34-audit.py](../research/parallel-schur-response-34-audit.py), [parallel-schur-response-34-certified.py](../research/parallel-schur-response-34-certified.py), [parallel-schur-response-34.py](../research/parallel-schur-response-34.py) |
| 33 | [astra-hardtail-33-actual.py](../research/astra-hardtail-33-actual.py), [astra-hardtail-33-audit.py](../research/astra-hardtail-33-audit.py), [astra-hardtail-33-certified.py](../research/astra-hardtail-33-certified.py), [astra-hardtail-33-exact.py](../research/astra-hardtail-33-exact.py), [astra-hardtail-33-explore.py](../research/astra-hardtail-33-explore.py), [complex-floor-33.py](../research/complex-floor-33.py), [parallel-audit-33.py](../research/parallel-audit-33.py), [parallel-prime-ui-33-conic.py](../research/parallel-prime-ui-33-conic.py), [parallel-prime-ui-33.py](../research/parallel-prime-ui-33.py) |
| 32 | [astra-prime-phase-32-check.py](../research/astra-prime-phase-32-check.py), [joint-law-32.py](../research/joint-law-32.py), [parallel-audit-32.py](../research/parallel-audit-32.py), [parallel-circulant-source-32.py](../research/parallel-circulant-source-32.py), [schur-mixing-32.py](../research/schur-mixing-32.py) |
| 31 | [astra-nested-moment-31.py](../research/astra-nested-moment-31.py), [nested-lift-31.py](../research/nested-lift-31.py), [nested-phase-31.py](../research/nested-phase-31.py), [parallel-coherent-source-31.py](../research/parallel-coherent-source-31.py) |
| 30 | [astra-arithmetic-coset-30-check.py](../research/astra-arithmetic-coset-30-check.py), [parallel-depth-window-30.py](../research/parallel-depth-window-30.py), [top-tail-transfer-30.py](../research/top-tail-transfer-30.py) |
| 29 | [astra-source-window-29.py](../research/astra-source-window-29.py), [parallel-source-pair-29.py](../research/parallel-source-pair-29.py), [root-coupled-tail-29.py](../research/root-coupled-tail-29.py) |
| 28 | [astra-broad-source-28-check.py](../research/astra-broad-source-28-check.py), [claude-fable-28-check.py](../research/claude-fable-28-check.py), [parallel-integrability-28.py](../research/parallel-integrability-28.py), [parallel-reciprocal-28.py](../research/parallel-reciprocal-28.py), [source-tail-28.py](../research/source-tail-28.py) |
| 27 | [astra-increments-27-check.py](../research/astra-increments-27-check.py), [harmonic-orbit-27.py](../research/harmonic-orbit-27.py), [parallel-rate-27-orbit-audit.py](../research/parallel-rate-27-orbit-audit.py), [parallel-rate-27.py](../research/parallel-rate-27.py), [parallel-transport-27.py](../research/parallel-transport-27.py) |
| 26 | [astra-extraction-26-check.py](../research/astra-extraction-26-check.py), [parallel-activation-26.py](../research/parallel-activation-26.py), [parallel-extrapolation-26.py](../research/parallel-extrapolation-26.py), [reciprocal-seed-26.py](../research/reciprocal-seed-26.py) |
| 25 | [astra-seed-25-check.py](../research/astra-seed-25-check.py), [parallel-cells-25-check.py](../research/parallel-cells-25-check.py), [parallel-random-circulant-25.py](../research/parallel-random-circulant-25.py), [scalar-seed-25.py](../research/scalar-seed-25.py) |
| 24 | [astra-dynamics-24-check.py](../research/astra-dynamics-24-check.py), [parallel-vacancy-24-audit.py](../research/parallel-vacancy-24-audit.py), [parallel-vacancy-24-check.py](../research/parallel-vacancy-24-check.py), [parallel-vacancy-24-square-check.py](../research/parallel-vacancy-24-square-check.py), [pinned-penalty-24.py](../research/pinned-penalty-24.py) |
| 23 | [astra-secant-23-check.py](../research/astra-secant-23-check.py), [mixed-shape-witness-23.py](../research/mixed-shape-witness-23.py), [parallel-directions-23-check.py](../research/parallel-directions-23-check.py), [parallel-graph-shapes-23.py](../research/parallel-graph-shapes-23.py) |
| 22 | [astra-transport-22.py](../research/astra-transport-22.py), [one-sided-quadratic-22.py](../research/one-sided-quadratic-22.py), [parallel-crossratio-22-check.py](../research/parallel-crossratio-22-check.py), [square-pinned-22.py](../research/square-pinned-22.py) |
| 21 | [astra-broad-21-check.py](../research/astra-broad-21-check.py), [parallel-crossratio-21-check.py](../research/parallel-crossratio-21-check.py), [soft-tail-21.py](../research/soft-tail-21.py) |
| 20 | [anchored-repair-20-square.py](../research/anchored-repair-20-square.py), [anchored-repair-20.py](../research/anchored-repair-20.py), [astra-signed-20.py](../research/astra-signed-20.py) |
| 19 | [astra-background-19-certificate.py](../research/astra-background-19-certificate.py), [astra-background-19.py](../research/astra-background-19.py), [threshold-repair-19-certificate.py](../research/threshold-repair-19-certificate.py), [threshold-repair-19.py](../research/threshold-repair-19.py) |
| 18 | [astra-low-layer-18.py](../research/astra-low-layer-18.py), [parallel-ratio-18.py](../research/parallel-ratio-18.py), [parallel-tail-18.py](../research/parallel-tail-18.py), [resolvent-repair-18.py](../research/resolvent-repair-18.py) |
| 17 | [astra-preimage-17.py](../research/astra-preimage-17.py), [parallel-repair-17.py](../research/parallel-repair-17.py) |
| 16 | [astra-source-16.py](../research/astra-source-16.py), [parallel-defect-16.py](../research/parallel-defect-16.py) |
| 15 | [astra-cuts-15.py](../research/astra-cuts-15.py), [parallel-transport-15.py](../research/parallel-transport-15.py) |
| 14 | [astra-sampling-14.py](../research/astra-sampling-14.py), [parallel-complexity-14.py](../research/parallel-complexity-14.py) |
| 13 | [astra-energy-13.py](../research/astra-energy-13.py) |
| 12 | [astra-fourth-12.py](../research/astra-fourth-12.py) |
| 11 | [astra-convolution-11.py](../research/astra-convolution-11.py) |

## Updating the catalogue

The machine-readable source is [scripts/python-tools.json](../scripts/python-tools.json). It records source hashes and static imports within the published Python files. Static imports omit dynamic loads and data dependencies.

After the intended research code is published, refresh from its published Git reference:

```sh
git fetch origin
python3 scripts/paley.py index --ref origin/main --write
python3 scripts/paley.py index --check
```

`index --check` compares the catalogue and this guide with their recorded source revision. It does not infer a newer published version or certify a mathematical result. Supplying `--ref` explicitly compares with that revision instead. No source program or acceptance record is rewritten.
