# Measuring missed shared obligations

The prospective sample starts with the first new research batch after the November 20, 2026 setup. Round 131 had already launched when this was set up. The [round-91 retrospective](../../research/round-91-shared-obligation-audit.md) is background for the pilot.

## Before launching a batch

In `round-N-before.json`, record the coordinator reference, capture time in UTC, and the precise obligation of every route about to be launched or still active in the comparison. Give each route an unambiguous ID, such as `r132/cold-response`, and retain its scope, hypotheses and quantifiers. Review the routes together and record any shared obligation by `cand:` ID. Also record which routes were reviewed as independent, with the reason. Deliberate parallel work on a known dependency counts as recognized.

Keep the saved bytes and preserve evidence that they existed before launch. Use the normal pre-dispatch record or version history to bind the SHA-256 before the call. Keep using the existing dispatch manifest or receipt for the actual call IDs and start time. If there is a second independent batch in the same round, use `round-N-b2` for the two filenames, and likewise for any later batch.

```json
{
  "captured_at_utc": "2026-11-20T01:00:00Z",
  "prepared_by": "Coordinator name",
  "coordinator": "coordination/round-131.json#next_calls",
  "routes": {
    "r132/example-a": "Precise estimate and hypotheses for the first route",
    "r132/example-b": "Precise estimate and hypotheses for the second route"
  },
  "known_shared": [],
  "comparison": "Which route comparisons were made, what was already shared, and why the others were treated independently"
}
```

Use entries with `id` and `routes` in `known_shared` for any identified group. The examples here are format illustrations.

### Hook for automatic dispatch

Once the launcher has selected its actual calls and checked the current coordinator record, run the capture command before making the first request. Pass only the calls selected for this batch.

```sh
python3 scripts/shared_obligations.py capture \
  --batch round-134 --coordinator coordination/round-133.json \
  --call first-call-id --call second-call-id \
  --assessment /tmp/paley-dependency-comparison.json
```

The optional assessment supplies `prepared_by`, `comparison` and any `active_routes` from earlier launches. The command copies the selected questions, scopes, remaining obligations and [shared `cand:` IDs](../../docs/ROUND_REVIEW.md#keep-one-id-for-a-shared-estimate) from the coordinator plan. Use `known_shared` in the assessment to record a link with an earlier active call, under the same ID where the estimate is already named. The output contains `path` and `sha256`. Include that object as `shared_obligations_before` in the ordinary inflight manifest. Keep the coordinator hash and use `time.time()` for each `started_utc_epoch` so launch times retain enough precision for a capture made in the same second. A capture without an assessment preserves the known IDs from the plan with other route comparisons marked unassessed.

## At closeout

Save `round-N-after.json` after comparing the actual dispatched routes with one another and with routes that were active at dispatch. Review completed batches even when there are no matches. Exclude unlaunched proposals and intentional audit or reviewer repetition. Count a group once, when its paired work first overlapped, and reference that record if the same obligation comes up again. Use the same statement, scope and `cand:` ID when it recurs. Assign a new ID only for a materially different obligation.

Give a mathematical explanation of the overlap. Cite the identity or reductions to a genuinely shared estimate at the same hypotheses and scale. Sharing a broad objective, reusing a tool, and deliberately dualizing an existing formulation do not by themselves establish a missed dependency.

| `classification` | Evidence required |
| --- | --- |
| `recognized` | The preserved pre-dispatch comparison already identifies the connection between the routes. |
| `missed` | The preserved comparison gives affirmative evidence that the two routes were treated as independent. The later comparison establishes the shared dependency. |
| `unknown` | The chronology or pre-dispatch judgment is unclear. Use this when a missing entry is the only evidence of a miss. |

Record `dispatch_effect` as `change` only if there is a concrete case for merging, rewriting or delaying a named call. State what would change and why. Use `same` if the calls would still make sense as dispatched and `unknown` if the counterfactual is uncertain.

Set `before_sha256` to the pre-dispatch digest when its provenance is usable. Use `null` and `unknown` for the classification when that provenance is unavailable. Report the first actual launch time of the batch from the dispatch evidence, using UTC. The reporting script checks the saved bytes and their declared time order. Source review is how the coordinator establishes the chronology and mathematical equivalence.

```json
{
  "reviewed_by": "Coordinator name",
  "dispatch": "coordination/round-132-inflight.json",
  "launched_at_utc": "2026-11-20T01:01:00Z",
  "before_sha256": null,
  "groups": [
    {
      "id": "cand:example-estimate",
      "routes": ["r132/example-a", "r132/example-b"],
      "classification": "unknown",
      "math_evidence": "Accepted note and equation establishing the shared estimate",
      "prior_evidence": "Reason that the state at dispatch is unclear",
      "dispatch_effect": "unknown",
      "effect_reason": "Reason that the effect on dispatch is unclear"
    }
  ]
}
```

For a batch with a launch manifest, the coordinator can supply `reviewed_by`, `comparison` and `groups` as the assessment and let the tool fill in the dispatch reference, actual call IDs, earliest launch time and bound before hash.

```sh
python3 scripts/shared_obligations.py closeout \
  --batch round-134 --assessment /tmp/paley-overlap-review.json
```

This checks the before hash against the actual manifest and compares the two times. An overlap already listed by ID at dispatch can be recorded as recognized under that ID. When the rest of the before comparison is absent or unassessed, subsequent discoveries carry `unknown`. The commands reuse identical records on retry and refuse to replace different saved records.

## Read the counts

Run `python3 scripts/shared_obligations.py` from the repository root. The report gives the number of reviewed batches and calculates `missed / (recognized + missed)`. It reports unknown groups separately, with the number of confirmed misses that would have changed dispatch. A batch with an empty `groups` list still counts as reviewed. An empty denominator gives no rate. Before-only files indicate that a snapshot lacks a closeout; actual launches remain documented in dispatch records.
