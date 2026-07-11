# Simulation — Distributed Genius and the Generative Ratchet

An **illustrative** model of the three-frontier framework. It is not an empirical
result. Every parameter is stipulated to instantiate the paper's definitions
(production, competence, judgment, desirable difficulty, fading assistance); none
is measured from learners. What the model shows is that the framework's central
distinction is internally coherent and separates the cases it names.

## Run

```bash
uv run run_all.py        # -> output/results.json, output/figures/frontiers.png
```

Requires `numpy` and `matplotlib` (declared in `pyproject.toml`; `uv` resolves
them). Runtime is well under a second.

## What it computes

A learner carries a competence frontier `C` (what they can independently
generate and revise) and a judgment frontier `J` (what they can reliably
evaluate). Production is `P = C + a (kappa - C)`, so removing the tool (`a = 0`)
returns `P = C`: the honest test. Over 30 practice sessions, one update law moves
`C` and `J`; three regimes differ only in the interaction signals they supply:

- `no_tool` — the learner does all the work but faces the raw, unscaffolded gap;
- `finished_output` — high constant assistance, the tool does the work and
  supplies the answer (the unrestricted-chatbot case);
- `structured_fading` — high early assistance that fades to zero, the tool
  structures rather than supplies, demands prediction and evaluation, and holds
  the learner at the productive-difficulty gap (the scaffolded-tutor case).

Competence and judgment grow through a desirable-difficulty kernel that is zero
for a trivial (fully offloaded) task, peaks at a moderate managed gap, and decays
under unscaffolded overload.

## Headline numbers (`output/results.json`)

Both tools reach the same production frontier (about 0.87). Competence ends at
0.15 under the finished-output tool and 0.84 under the structured/fading tool.
Hand every regime the tool at a common strength and then remove it: finished
output collapses 83.1%, structured/fading 10.3%, no tool 23.9%. The
genuine-ratchet fraction (durable capability per unit of production advance) is
0.10 for finished output and 0.99 for structured/fading. A seeded sweep of 2000
parameter perturbations (+/-15%) preserves both orderings in every draw.

## Files

- `analyses.py` — the model, the three regimes, the tool-removal test, the
  seeded robustness sweep. `run()` returns the results dict.
- `figures.py` — the three-panel figure.
- `run_all.py` — orchestrator; writes `results.json` and the figure.
- `output/` — committed results and figure the paper cites.
