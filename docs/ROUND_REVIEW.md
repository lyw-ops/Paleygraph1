# Round assessments and proposed missions

The coordinator needs to answer two questions: what changed in the proof plan after this round, and why the next agent call is worth making. These answers live in `coordination/round-N.json`, separately from mathematical notes and acceptance records.

This is a coordinator assessment with explicit sources. A `ready` record means the required fields and references are present; it does not certify mathematics, measure research value, or record an actual dispatch.

## After a round is accepted

```sh
python3 scripts/round_review.py init
```

This selects the latest acceptance in the checkout, links its previous acceptance and records their SHA-256 values. It creates a draft with source-note references and the first recorded next-test suggestion. It does not write mathematical conclusions. It refuses to overwrite an existing coordinator record.

Fill the draft, identify the preparing person or agent, and set `record_status` to `ready` after completing the assessment. For a selected historical round, use `init --round N`; `--baseline PATH` selects an earlier acceptance when needed. A current acceptance's explicit previous pointer remains authoritative when checking the record.

Each item under `changes` contains:

| Field | What the coordinator records |
| --- | --- |
| `id`, `route` | A short identifier and the route being assessed; reuse an identifier when the same obligation continues. |
| `effect` | `removed`, `weakened`, `new_obstruction`, `reformulated`, `evidence_only` or `unchanged`. |
| `before`, `after` | What the previous record required and what the new result changes, with its hypotheses and quantifiers. |
| `remaining` | The precise estimate, construction or implication still needed. |
| `evidence` | Repository-relative paths and SHA-256 values for the relevant sources. |

`unchanged` is a valid result and may use identical before/after descriptions. A new sufficient criterion can be a reformulation even if the hard estimate is still open. A finite certificate remains finite evidence. Choose the effect based on the mathematics, not the count of files or checks.

Evidence must match the current bytes and be explicitly bound by either linked acceptance record: the acceptance itself, or one of its file-hash maps. This is a limited reference check, not a complete dependency-closure verification. An older acceptance with no relevant file-hash map can itself be cited; do not add hashes to historical records to satisfy this tool.

## Before the next agent call

Use `decision: continue` with one or more `next_calls`, or `decision: hold` with no proposed calls and a concrete `decision_reason`. This records the coordinator's decision; it does not change an app goal or pause a running task.

Each proposed call contains:

| Field | Purpose |
| --- | --- |
| `id`, `priority`, `change_id` | Identify and rank the proposal and connect it to one assessed route. |
| `question` | The specific uncertainty this call should address. |
| `why_now` | Why the current evidence makes this test useful now. |
| `scope` | Required hypotheses, quantifiers, normalizations and exclusions. |
| `if_yes`, `if_no`, `if_inconclusive` | What each possible outcome would change about the next decision. |
| `inputs` | Source paths and hashes the researcher should read; use the same reference rules as evidence. |

Then run:

```sh
python3 scripts/round_review.py check --current
python3 scripts/round_review.py show
python3 scripts/round_review.py mission --call CALL_ID > /tmp/paley-next-mission.md
```

Export refuses a draft, empty rationale, stale source, unknown route link or an assessment superseded by a newer acceptance. The prompt includes the coordinator-record hash, question, remaining obligation, scope, source paths and outcome-dependent decisions. Add the existing role instructions and file ownership when assigning it.

The tool does not intercept every possible agent-launch API. The coordinator follows this workflow, and actual launches are recorded through the existing dispatch process. Proposed mission text is never evidence that an agent was launched.

## Keep one ID for a shared estimate

When two proposed calls genuinely need the same estimate, put one entry in the coordinator record’s optional `shared_candidates` list. Record its precise `statement`, its stable `cand:` `id` and the proposed call IDs in `calls`. Check the hypotheses, normalization and quantifiers before reusing an ID. Two calls can cite the same candidate and still deserve separate missions if their outcomes would give different evidence.

```json
{
  "shared_candidates": [
    {
      "id": "cand:example-bound",
      "statement": "The exact shared bound, with its objects, hypotheses and scale",
      "calls": ["first-call-id", "second-call-id"]
    }
  ]
}
```

Mission export and automatic dispatch capture copy this same ID. The closeout reuses it for the recognized overlap. The same estimate keeps its ID in later coordinator records and checkpoints.

```sh
python3 scripts/round_review.py checkpoint
```

This prints a draft in the four synthesis-checkpoint sections for the accepted round. It uses the coordinator IDs in *What resists* and carries the ranked mission, outcome branches and reading path into *Proposed next step*. Before handing it off, finish the evidence labels and the reasons for setting routes aside, state the exact open target, and complete any missing sources. When working inside the upstream template, introduce a new candidate in the checkpoint front matter once and cite its ID in later checkpoints. An unchanged plan is a valid result when the checkpoint explains what was learned.

## Recovering a session

```sh
python3 scripts/research_index.py
python3 scripts/round_review.py status
```

`status` requires a ready coordinator record for the latest acceptance. If a later round has been accepted, it reports the missing or incomplete assessment rather than silently reusing an older plan. `show --round N` and `check --round N` can inspect a historical assessment; a historical record cannot export a new current mission.

The initial local `coordination/round-96.json` record is a retrospective synthesis prepared while implementing this workflow. It compares the local round-95 and round-96 acceptance records and contains proposed calls only. It is not a reconstruction of earlier dispatch intent. Its sources may still be unpublished; publish a coordinator record together with the source records it references.

## Source changes and corrections

After an underlying result changes, complete the existing mathematical review process before updating the coordinator assessment. `init` never overwrites a record. A coordinator may edit a draft; keep versions used for exported missions in Git, or retain an explicitly named correction. The tool does not enforce historical immutability or establish reviewer independence.

Run the maintenance checks with:

```sh
python3 -B -m unittest discover -s tests -p 'test_*.py'
```
