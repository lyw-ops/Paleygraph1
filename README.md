# Paley graph 1-localization

Let $p\equiv1\pmod4$ be prime, $H$ the Paley graph induced on the nonzero squares, and $n=(p-1)/2$. The target is $\vartheta(\overline H)/\sqrt n\to1$, where $\vartheta$ is ordinary Lovász theta. This is [Randomstrasse101 Conjecture 26](https://randomstrasse101.math.ethz.ch/posts/PaleyGraph/). **The target remains open.**

This repository records one researcher's AI-assisted search: mathematical arguments, parallel route investigations, computations, failed approaches and the evidence supporting each round.

## Start here

| To… | Read… |
| --- | --- |
| Find the latest recorded acceptance and its route notes | [Research index](research/README.md) |
| Compare approaches and locate unresolved estimates | [Research ledger](research/ledger.md) |
| Understand the early constructions and milestones | [Research background](docs/RESEARCH.md) |
| Install dependencies and replay computations | [Replay guide](docs/REPLAY.md) |
| Browse Python tools by function or research round | [Python tool catalogue](docs/PYTHON.md) |
| Continue a route or prepare a new coordinating session | [Research workflow](docs/WORKFLOW.md) |
| Record what changed and justify the next research call | [Round assessments and missions](docs/ROUND_REVIEW.md) |

The index is generated from acceptance records in the local checkout. For a live summary:

```sh
python3 scripts/research_index.py
```

A record states what the research session accepted and which evidence it examined. It is not a claim of human review or Lean kernel verification. Read its hypotheses, proof scope and open bounds before reusing a conclusion.

## A small first computation

Run from the repository root:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -B theta.py --certify 5 13 41
```

This checks finite theta bounds. The [replay guide](docs/REPLAY.md) explains how to select a recorded round and compare its output with the saved evidence.

## Python tools

The [Python catalogue](docs/PYTHON.md) groups the published tools by function and research round. Browse descriptions without importing or running mathematical code:

```sh
python3 scripts/paley.py list
python3 scripts/paley.py list --round 91
python3 scripts/paley.py show smoothing
```

Use the project interpreter to run a tool through the common entry point:

```sh
.venv/bin/python -B scripts/paley.py run theta --certify 5 13 41
```

Existing direct commands and source paths remain available. The catalogue covers its recorded published snapshot; the research index also includes local acceptance records.

## Repository map

| Location | Contents |
| --- | --- |
| Root `*.py` files | Shared mathematical routines and experiment entry points, including [theta.py](theta.py) and [smoothing.py](smoothing.py) |
| [`research/`](research/README.md) | Proof notes, route-specific checkers, acceptance records, saved inputs and JSONL outputs |
| [data/](data/) | CSV experiment tables; their generating commands are described in the replay guide |
| [docs/](docs/) | Background, replay instructions and research workflow |
| [scripts/](scripts/) | Navigation, the Python catalogue and common runner, and maintenance tools |
| [tests/](tests/) | Checks for catalogue scope and command forwarding |
| [HANDOFF.md](HANDOFF.md), [BRAIN_PROMPT.md](BRAIN_PROMPT.md) | Historical handoff and coordinator prompt after round 36 |

Existing mathematical files retain their paths so imports, saved replay commands and recorded hashes continue to refer to the same artifacts. The round-36 handoff files are historical snapshots; use the research index for later records.
