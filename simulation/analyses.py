"""Distributed Genius and the Generative Ratchet -- an illustrative model of the
three-frontier framework.

This is NOT an empirical result. It is a deterministic model built to instantiate
the paper's definitions and show that they are internally coherent and separate
the cases the framework names. Every parameter is stipulated to express a
definition, not measured from data. What the model demonstrates is a claim about
the framework's logic: under one common learning dynamics, three interaction
architectures (a finished-output tool, a structured/fading tool, and no tool)
drive the production frontier and the competence/judgment frontiers apart by
different amounts, and the gap is revealed exactly when the tool is removed.

State per learner, over T practice sessions:

    C_t  competence frontier -- what the learner can independently generate/revise
    J_t  judgment frontier   -- what the learner can reliably evaluate/select
    P_t  production frontier  -- best output achievable WITH the tool at hand

Production is an algebraic function of competence and the tool:

    P_t = C_t + a_t (kappa - C_t)_+          (kappa = tool ceiling, a_t = assistance)

so removing the tool (a = 0) returns P = C exactly: the honest test.

Competence and judgment move by ONE update law for every regime; the regimes
differ only in the per-session interaction signals they supply:

    dC_t = etaC * w_t * f_t * Lambda(g_eff,t) * (1 - C_t)
    dJ_t = etaJ * x_t * (beta + (1-beta) C_t) * (1 - J_t)

    w_t      learner's share of the generative work actually done (not offloaded)
    f_t      feedback / error-correction quality of the interaction
    x_t      evaluative engagement demanded (predict, contrast, critique, select)
    Lambda   desirable-difficulty kernel, peaked at an effective gap g* (ZPD):
             too-easy (tool did it) and too-hard (unscaffolded overload) both
             learn little; a moderate managed gap learns most
    g_eff,t  the challenge the learner personally faces, set by the regime
    beta     the part of judgment reachable without understanding; the rest of
             judgment requires competence (you cannot reliably judge what you
             cannot generate)

The regimes:
  no_tool          a=0; the learner does all the work but faces the raw,
                   unscaffolded gap (Sweller overload early, then enters the zone)
  finished_output  a high and constant; the tool does the work (w low), gives the
                   answer not the operations (f low), and is accepted uncritically
                   (x low) -- the Bastani et al. (2024) unrestricted-GPT case
  structured_fading  a high early then faded to zero; the tool STRUCTURES rather
                   than supplies (w high), gives real feedback (f high), demands
                   evaluation (x high), and holds the learner at the productive
                   gap g* -- the Kestin et al. (2025) scaffolded-tutor case

    cd simulation && uv run run_all.py
"""
from __future__ import annotations

import math

import numpy as np

# --------------------------------------------------------------------------- #
# Stipulated constants. These express the definitions; they are not fitted.
# --------------------------------------------------------------------------- #
T = 30                # practice sessions in the course
KAPPA = 0.95          # tool ceiling: the output level the tool can lift toward
D_TASK = 0.75         # intrinsic difficulty of the practised task
G_STAR = 0.30         # desirable-difficulty peak: the productive gap above competence
ETA_C = 0.11          # competence learning rate
ETA_J = 0.10          # judgment learning rate
BETA = 0.35           # judgment reachable without competence; 1-BETA needs it
LAMBDA_J = 0.5        # weight of judgment in the incorporation ratio
C0 = 0.10             # novice competence at intake
J0 = 0.10             # novice judgment at intake
A_EVAL = 0.90         # common assistance level for the tool-removal test

# Assistance profile of the finished-output tool (constant) and the fading tool.
A_FINISHED = 0.90
A_FADE_START = 0.90


def _kernel(g: float) -> float:
    """Desirable-difficulty kernel: a one-humped bump in the effective gap g,
    (g/g*) * exp(1 - g/g*). It is zero at g = 0 (a trivial, fully offloaded task
    teaches nothing), rises to 1 at the productive gap g* (the zone of proximal
    development), and decays for g >> g* (unscaffolded overload). This is the
    desirable-difficulty / productive-failure shape made into a single curve."""
    g = max(g, 0.0)
    if G_STAR <= 0:
        return 0.0
    r = g / G_STAR
    return r * math.exp(1.0 - r)


def _production(c: float, a: float) -> float:
    """Production frontier at competence c with assistance a."""
    return c + a * max(KAPPA - c, 0.0)


def _regime_signals(name: str, t: int):
    """Per-session interaction signals (a, w, f, x, g_eff_mode) for a regime.
    g_eff_mode is a function competence -> effective gap the learner faces."""
    frac = t / (T - 1)  # 0 -> 1 across the course

    if name == "no_tool":
        a = 0.0
        w, f, x = 1.0, 0.42, 0.45
        g_eff = lambda c: D_TASK - c                      # raw, unscaffolded gap
    elif name == "finished_output":
        a = A_FINISHED
        w, f, x = 0.10, 0.35, 0.12
        offload = 0.90
        g_eff = lambda c: (1.0 - offload) * (D_TASK - c)  # tool did the work
    elif name == "structured_fading":
        a = A_FADE_START * (1.0 - frac)                   # fade to zero
        w, f, x = 0.85, 1.00, 0.85
        # scaffolding holds the learner at g* early; as assistance fades the
        # learner is handed the authentic gap. phi is the fade progress.
        phi = frac
        g_eff = lambda c: (1.0 - phi) * G_STAR + phi * (D_TASK - c)
    else:
        raise ValueError(name)
    return a, w, f, x, g_eff


def run_regime(name: str) -> dict:
    """Integrate one regime over the course. Deterministic; a plain recursion."""
    c, j = C0, J0
    Ps, Cs, Js, gaps = [], [], [], []
    a_last = 0.0
    for t in range(T):
        a, w, f, x, g_eff = _regime_signals(name, t)
        a_last = a
        p = _production(c, a)
        Ps.append(p); Cs.append(c); Js.append(j); gaps.append(p - c)
        # update
        dc = ETA_C * w * f * _kernel(g_eff(c)) * (1.0 - c)
        dj = ETA_J * x * (BETA + (1.0 - BETA) * c) * (1.0 - j)
        c = min(c + dc, 1.0)
        j = min(j + dj, 1.0)

    c_final, j_final = c, j
    p_train_final = Ps[-1]
    p_frontier = max(Ps)                         # production frontier: best shown

    # tool-removal test at a COMMON assistance level, applied at course end:
    # give every regime the tool at A_EVAL, then take it away.
    p_assisted = _production(c_final, A_EVAL)
    p_unassisted = c_final                       # a = 0 -> P = C exactly
    collapse = (p_assisted - p_unassisted) / p_assisted

    # gap statistics over the course (production minus competence)
    gaps_arr = np.array(gaps)
    mean_gap = float(gaps_arr.mean())
    peak_gap = float(gaps_arr.max())
    end_gap = float(gaps[-1])

    # genuine-ratchet fraction: of the production advance the tool bought over the
    # novice floor, how much became durable capability (competence, and judgment
    # weighted by lambda). Bounded ~[0,1]; near 0 is false ratcheting, near 1 is
    # genuine. This is the seed's incorporation ratio, normalized by the frontier.
    dC = c_final - C0
    dJ = j_final - J0
    dP_advance = p_frontier - C0
    grf = (dC + LAMBDA_J * dJ) / ((1.0 + LAMBDA_J) * dP_advance) if dP_advance > 1e-9 else float("nan")

    return {
        "name": name,
        "C_final": round(c_final, 3),
        "J_final": round(j_final, 3),
        "P_train_final": round(p_train_final, 3),
        "P_frontier": round(p_frontier, 3),
        "a_final": round(a_last, 3),
        "mean_gap": round(mean_gap, 3),
        "peak_gap": round(peak_gap, 3),
        "end_gap": round(end_gap, 3),
        "p_assisted_eval": round(p_assisted, 3),
        "p_unassisted_eval": round(p_unassisted, 3),
        "collapse_on_removal": round(collapse, 3),
        "collapse_pct": round(100.0 * collapse, 1),
        "retained_fraction": round(p_unassisted / p_assisted, 3),
        "genuine_ratchet_fraction": round(grf, 3),
        "delta_C": round(dC, 3),
        "delta_J": round(dJ, 3),
        "traj_P": [round(v, 4) for v in Ps],
        "traj_C": [round(v, 4) for v in Cs],
        "traj_J": [round(v, 4) for v in Js],
        "traj_gap": [round(v, 4) for v in gaps],
    }


def robustness_sweep(n: int = 2000, seed: int = 20260711) -> dict:
    """Seeded parameter-perturbation check: is the qualitative ordering an
    artifact of one parameter set, or stable under jitter? We perturb the global
    constants by +/-15% (uniform, fixed seed) and record, per draw, whether the
    two ordering claims hold:
      (i)  finished_output competence stays below structured competence, and
      (ii) finished_output collapses more on removal than structured does.
    Reports the fraction of draws in which each holds. Seeded for reproducibility.
    """
    rng = np.random.default_rng(seed)
    global KAPPA, D_TASK, G_STAR, ETA_C, ETA_J, BETA
    base = dict(KAPPA=KAPPA, D_TASK=D_TASK, G_STAR=G_STAR,
                ETA_C=ETA_C, ETA_J=ETA_J, BETA=BETA)
    comp_ok = 0
    collapse_ok = 0
    both_ok = 0
    for _ in range(n):
        jitter = {k: base[k] * (1.0 + rng.uniform(-0.15, 0.15)) for k in base}
        KAPPA, D_TASK, G_STAR = jitter["KAPPA"], jitter["D_TASK"], jitter["G_STAR"]
        ETA_C, ETA_J, BETA = jitter["ETA_C"], jitter["ETA_J"], jitter["BETA"]
        fin = run_regime("finished_output")
        stru = run_regime("structured_fading")
        c_ok = fin["C_final"] < stru["C_final"]
        x_ok = fin["collapse_on_removal"] > stru["collapse_on_removal"]
        comp_ok += c_ok
        collapse_ok += x_ok
        both_ok += (c_ok and x_ok)
    # restore
    KAPPA, D_TASK, G_STAR, ETA_C, ETA_J, BETA = (
        base["KAPPA"], base["D_TASK"], base["G_STAR"],
        base["ETA_C"], base["ETA_J"], base["BETA"])
    return {
        "n_draws": n,
        "seed": seed,
        "jitter_pct": 15,
        "frac_competence_ordering": round(comp_ok / n, 3),
        "frac_collapse_ordering": round(collapse_ok / n, 3),
        "frac_both": round(both_ok / n, 3),
    }


def run() -> dict:
    regimes = {name: run_regime(name)
               for name in ("no_tool", "finished_output", "structured_fading")}

    fin = regimes["finished_output"]
    stru = regimes["structured_fading"]
    base = regimes["no_tool"]

    # headline contrasts the prose cites
    summary = {
        "competence_gap_structured_minus_finished": round(stru["C_final"] - fin["C_final"], 3),
        "collapse_ratio_finished_over_structured": round(
            fin["collapse_on_removal"] / stru["collapse_on_removal"], 2)
        if stru["collapse_on_removal"] > 1e-9 else None,
        "production_finished_frontier": fin["P_frontier"],
        "competence_finished_final": fin["C_final"],
        "competence_structured_final": stru["C_final"],
        "judgment_structured_final": stru["J_final"],
        "competence_no_tool_final": base["C_final"],
        "grf_finished": fin["genuine_ratchet_fraction"],
        "grf_structured": stru["genuine_ratchet_fraction"],
        "grf_no_tool": base["genuine_ratchet_fraction"],
    }

    return {
        "params": {
            "T": T, "kappa": KAPPA, "d_task": D_TASK, "g_star": G_STAR,
            "eta_C": ETA_C, "eta_J": ETA_J, "beta": BETA,
            "lambda_J": LAMBDA_J, "C0": C0, "J0": J0, "a_eval": A_EVAL,
        },
        "regimes": regimes,
        "summary": summary,
        "robustness": robustness_sweep(),
        # External literature values the paper quotes as decimals, recorded here
        # so the claims gate can reconcile them. These are NOT model outputs; they
        # are the reported figures of the cited studies, attributed in the prose.
        "external_anchors": {
            "kestin_2025_effect_low_sd": 0.73,   # Kestin et al. (2025), lower bound
            "kestin_2025_effect_high_sd": 1.3,    # Kestin et al. (2025), upper bound
        },
    }


if __name__ == "__main__":
    import json
    print(json.dumps(run(), indent=2))
