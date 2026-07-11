"""Orchestrator: reproduces every number and the figure in the paper.

    cd simulation
    uv run run_all.py

Writes output/results.json and output/figures/frontiers.png. The three regimes
are integrated deterministically (a plain recursion of the update law); the only
randomness is the seeded robustness sweep, which draws 2000 parameter
perturbations under a fixed seed and is reported as a fraction. Every decimal the
paper cites is a key in results.json.

The model is ILLUSTRATIVE. Its parameters are stipulated to instantiate the
paper's definitions (production, competence, judgment, desirable difficulty,
fading assistance), not measured from learners. What it demonstrates is the
internal logic of the three-frontier framework, not an empirical fact about
teaching.
"""
from __future__ import annotations

import json
from pathlib import Path

from analyses import run
from figures import plot_frontiers

OUT = Path(__file__).parent / "output"


def main() -> None:
    (OUT / "figures").mkdir(parents=True, exist_ok=True)
    results = run()
    (OUT / "results.json").write_text(json.dumps(results, indent=2))
    plot_frontiers(results, str(OUT / "figures" / "frontiers.png"))

    reg, s, rb = results["regimes"], results["summary"], results["robustness"]
    for name in ("no_tool", "finished_output", "structured_fading"):
        r = reg[name]
        print(f"{name:18s} C={r['C_final']:.3f} J={r['J_final']:.3f} "
              f"P_frontier={r['P_frontier']:.3f} collapse={r['collapse_pct']}% "
              f"GRF={r['genuine_ratchet_fraction']:.3f}")
    print(f"contrast: competence gap structured-finished = "
          f"{s['competence_gap_structured_minus_finished']}; "
          f"collapse ratio finished/structured = "
          f"{s['collapse_ratio_finished_over_structured']}x")
    print(f"robustness: ordering holds in {rb['frac_both']} of {rb['n_draws']} "
          f"draws (+/-{rb['jitter_pct']}% jitter, seed {rb['seed']})")
    print("wrote", OUT / "results.json")


if __name__ == "__main__":
    main()
