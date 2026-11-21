# Working on Paley

Read [docs/WORKFLOW.md](docs/WORKFLOW.md) before continuing mathematical research. Existing research notes, saved inputs, certificates and local drafts keep their paths and bytes unless the assigned research task specifically changes them. Preserve unrelated working-tree and staged changes.

## Round changes and next missions

After accepting a round, prepare its separate coordinator record using `python3 scripts/round_review.py init`. Fill the before/after assessment, precise remaining obligations and proposed next calls in `coordination/round-N.json`. Identify the author accurately; an agent assessment is not human acceptance or mathematical certification. Recording an unchanged proof plan is valid.

Before exporting a new research assignment, run `python3 scripts/round_review.py check --current`, then `python3 scripts/round_review.py mission --call CALL_ID`. Use the exported proposal and the existing role/file-ownership instructions for the call. The export does not start a session and is not evidence that a past call occurred. This is a workflow check, not a request for additional user permission.

Record a shared estimate once under its `cand:` ID in the coordinator plan’s `shared_candidates`. Use that ID in mission exports and in a synthesis checkpoint when reassessing the plan. For an automatic research batch, use the [shared-obligation dispatch hook](coordination/shared-obligations/README.md#hook-for-automatic-dispatch) with the selected call IDs before the first request. Bind its output in the existing inflight manifest and use the closeout hook after the dependency review. Record unknown timing or an unassessed comparison as unknown when classifying an overlap without a recorded ID.

A changed source or newer acceptance requires a current assessment. Do not edit a proof, acceptance record or stored hash merely to clear a coordination check. Follow the existing review process for mathematical changes. A new coordinator record must preserve the exact hypotheses and distinguish finite evidence, conditional criteria and proof of the original target.

The root HANDOFF.md and BRAIN_PROMPT.md are historical round-36 snapshots. Recover current state from the latest acceptance and coordinator record. Retain coordinator versions used for missions in Git or as explicitly named corrections; the tool checks source bytes and structure, not append-only history or scientific judgment.

## Maintenance checks

For changes to these tools, run `python3 -B -m unittest discover -s tests -p 'test_*.py'`. Keep maintenance changes separate from research drafts. Updating navigation or coordination does not renew a mathematical review.
