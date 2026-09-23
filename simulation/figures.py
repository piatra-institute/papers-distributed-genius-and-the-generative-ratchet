"""Publication figure for *Distributed Genius and the Generative Ratchet*.
Reads trajectories and scalars from the results dict; deterministic, no seed.

Three panels tell the framework's central claim:
  A  a finished-output tool opens a wide, durable gap between production and
     competence (false ratcheting);
  B  a structured, fading tool lets production and competence rise together and
     the gap closes as assistance withdraws (genuine ratcheting);
  C  the tool-removal test: hand every regime the tool at a common strength, then
     take it away, and read how much displayed production was really the learner's.
"""
from __future__ import annotations

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

INK = "#1e1e2e"
MUTED = "#6c7086"
ACCENT = "#8839ef"
WARM = "#d20f39"
COOL = "#1e66f5"
GREEN = "#40a02b"


def _panel_regime(ax, reg, title, gap_color, close_note):
    P = np.array(reg["traj_P"])
    C = np.array(reg["traj_C"])
    t = np.arange(len(P))
    ax.fill_between(t, C, P, color=gap_color, alpha=0.18, zorder=1,
                    label="production–competence gap")
    ax.plot(t, P, color=ACCENT, lw=2.2, zorder=3, label="production frontier $P$")
    ax.plot(t, C, color=INK, lw=2.0, ls=(0, (5, 2)), zorder=3,
            label="competence frontier $C$")
    ax.set_xlim(0, len(P) - 1)
    ax.set_ylim(0, 1.0)
    ax.set_xlabel("practice session", fontsize=9)
    ax.set_title(title, fontsize=10, color=INK)
    ax.spines[["top", "right"]].set_visible(False)
    ax.text(0.97, 0.06, close_note, transform=ax.transAxes, ha="right",
            va="bottom", fontsize=8, color=MUTED)
    ax.legend(fontsize=7.5, frameon=False, loc="center right")


def plot_frontiers(results, path):
    reg = results["regimes"]
    fin, stru, base = (reg["finished_output"], reg["structured_fading"],
                       reg["no_tool"])
    fig, (axA, axB, axC) = plt.subplots(1, 3, figsize=(13.5, 4.4))

    _panel_regime(
        axA, fin, "Finished-output tool (constant assistance)", WARM,
        f"final competence {fin['C_final']:.2f}")
    axA.set_ylabel("frontier level", fontsize=9)

    _panel_regime(
        axB, stru, "Structured tool, assistance faded to zero", GREEN,
        f"final competence {stru['C_final']:.2f}")

    # --- Panel C: the tool-removal test ---
    order = ["finished_output", "structured_fading", "no_tool"]
    labels = ["finished\noutput", "structured\nfading", "no\ntool"]
    assisted = [reg[k]["p_assisted_eval"] for k in order]
    unaided = [reg[k]["p_unassisted_eval"] for k in order]
    collapse = [reg[k]["collapse_pct"] for k in order]
    xs = np.arange(len(order))
    w = 0.36
    axC.bar(xs - w / 2, assisted, w, color=COOL, label="with the tool ($a{=}0.9$)")
    axC.bar(xs + w / 2, unaided, w, color=INK, label="tool removed ($a{=}0$)")
    for i, (a, u, c) in enumerate(zip(assisted, unaided, collapse)):
        axC.annotate("", xy=(i + w / 2, u), xytext=(i + w / 2, a),
                     arrowprops=dict(arrowstyle="->", color=WARM, lw=1.3))
        axC.text(i + w / 2 + 0.04, (a + u) / 2, f"-{c:.0f}%",
                 fontsize=8, color=WARM, va="center")
    axC.set_xticks(xs)
    axC.set_xticklabels(labels, fontsize=8.5)
    axC.set_ylim(0, 1.2)
    axC.set_ylabel("output on a fresh task", fontsize=9)
    axC.set_title("Output with and without the tool at course end", fontsize=10, color=INK)
    axC.spines[["top", "right"]].set_visible(False)
    axC.legend(fontsize=7.5, frameon=False, loc="upper center", ncol=2)

    fig.tight_layout()
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
