# Coordinator records

One `round-N.json` records the proof-plan changes after acceptance and the rationale for proposed next calls. These files supplement the existing research records; they do not replace acceptance, certify mathematics or record an actual launch.

Start with [the field guide](../docs/ROUND_REVIEW.md) and [the research workflow](../docs/WORKFLOW.md). Run `python3 scripts/round_review.py status` to check the latest accepted round in this checkout.

The initial local `round-96.json` assessment was written retrospectively during implementation. It is based on local round-95/96 records and contains proposals, not past dispatches. Keep it with those source records when publishing. This tool reads existing research files without modifying them.
