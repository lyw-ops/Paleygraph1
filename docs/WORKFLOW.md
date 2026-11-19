# Continuing the research

The target is the ordinary Lovász theta limit stated in the [repository overview](../README.md). A conditional criterion, a finite computation or a refutation of one construction leaves that target open unless a proof or refutation of the full statement is supplied.

## Recover the current state

From the repository root, run:

```sh
python3 scripts/research_index.py
```

Read the latest acceptance record it names, its `proof_scope`, `failed_paths_and_open_bounds` and `main_ranked_closeout`, then the relevant route notes and latest ledger entries. The [generated index](../research/README.md) links the available acceptance records. The root handoff and coordinator prompt describe round 36 and are useful historical context.

Check `git status --short` to see which material is still local. A later filename or an agent's completion message alone gives a draft no acceptance status. The acceptance records describe the project's review and computation process; this navigation layer does not independently certify it.

## Work on a route

- Give parallel investigations separate file prefixes and specific mathematical questions. Preserve unrelated work in progress.
- State what would change the proof plan: a removed hypothesis, a smaller remaining estimate, an obstruction to a construction, or a test distinguishing two possibilities. Record an unchanged plan honestly.
- Retain hypotheses, normalizations and quantifiers when carrying a result forward. Fixed-depth results need a new argument at growing depth. Square-order controls test field-general shortcuts and are not counterexamples to the prime-order target.
- Separate ordinary mathematical arguments, exact or outward interval computations, and floating-point diagnostics. State whether a certificate concerns saved rounded input or an exact mathematical orbit.

Keep existing proof notes, scripts and saved evidence at their current paths. Their imports, replay instructions and acceptance records may refer to those locations. Historical hashes describe the examined bytes; a documentation reorganization does not renew an earlier review.

## Close a round and prepare the next session

Record the result, scope, review, saved inputs, replay commands and remaining estimates in the route notes and acceptance record. The coordinator consolidates overlapping proposals and records ranked next tests in the ledger and acceptance record. For each proposed mission, say what its possible outcomes would decide.

After creating or updating an acceptance record, refresh the navigation page:

```sh
python3 scripts/research_index.py --verify-latest
python3 scripts/research_index.py --write
python3 scripts/research_index.py --check
```

The verification option checks the latest record's explicit file-hash maps and previous-record hash. It does not establish review independence, replay output, mathematical correctness or a complete dependency closure. Use the record's own scope and the [replay guide](REPLAY.md) for those checks.

A handoff should name the exact acceptance record and relevant files, list the remaining proof obligations and explain the next proposed test. Keep historical handoffs as snapshots; link the new checkpoint rather than rewriting the old history. Navigation updates and research acceptance are separate changes and can be reviewed separately.

## Maintain the published Python catalogue

The [Python catalogue](PYTHON.md) is generated from a chosen published Git revision. It covers both shared tools and round-specific scripts, while retaining their original paths. Local drafts are excluded until they are part of the chosen revision.

```sh
git fetch origin
python3 scripts/paley.py index --ref origin/main --write
python3 scripts/paley.py index --check
python3 -B -m unittest discover -s tests -p 'test_python_tools.py'
```

The check compares the generated catalogue and guide with the recorded source revision. Refreshing it changes navigation metadata only. A tool launched through the common runner executes the current checkout version, so its source snapshot and relevant evidence still need to be checked for a mathematical replay.
