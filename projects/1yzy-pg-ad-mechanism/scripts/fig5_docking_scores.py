#!/usr/bin/env python3
"""Figure 5 (v0.4): AutoDock Vina PAS-focused docking scores of the 12 main candidates.

Color-blind-safe palette follows the v0.3 convention:
  healthy/control neutral = #0072B2 (blue)
  periodontitis accent    = #D55E00 (vermillion)
Here all twelve peptides are periodontitis-oriented candidates; bars use the
vermillion accent, the top-ranked peptide is highlighted in blue, and error
bars show +/- SD across retained binding modes.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

DATA = [
    ("FLLHTTR",   -9.60, 0.08),
    ("YLSLLQR",   -9.49, 0.05),
    ("ALLLHRC",   -9.29, 0.11),
    ("FCLHLQLR",  -9.27, 0.09),
    ("YHHLLCRR",  -9.03, 0.07),
    ("LLHLPKRTT", -9.01, 0.06),
    ("LLHPLRL",   -8.94, 0.10),
    ("WLLVHLKK",  -8.94, 0.04),
    ("LLHPLRC",   -8.91, 0.08),
    ("HLLTLKKHV", -8.88, 0.05),
    ("HLPLLHRCC", -8.35, 0.12),
    ("HVLLLRQCA", -8.25, 0.09),
]

BLUE, VERMILLION, GREY = "#0072B2", "#D55E00", "#555555"

names = [d[0] for d in DATA]
means = np.array([d[1] for d in DATA])
sds = np.array([d[2] for d in DATA])

fig, ax = plt.subplots(figsize=(7.2, 4.6), dpi=300)
colors = [BLUE] + [VERMILLION] * (len(DATA) - 1)
x = np.arange(len(DATA))
ax.bar(x, means, width=0.68, color=colors, edgecolor="white", linewidth=0.6)
ax.errorbar(x, means, yerr=sds, fmt="none", ecolor=GREY, elinewidth=1.1,
            capsize=3.2, capthick=1.1, zorder=5)

ax.set_xticks(x)
ax.set_xticklabels(names, rotation=45, ha="right", fontsize=8.2)
ax.set_ylabel("AutoDock Vina score (kcal/mol)", fontsize=9.5)
ax.set_ylim(-10.1, -7.6)
ax.axhline(-8.0, ls="--", lw=0.9, color=GREY, alpha=0.75)
ax.text(len(DATA) - 0.45, -7.93, "-8.0 kcal/mol reference",
        ha="right", va="bottom", fontsize=7.4, color=GREY)
ax.tick_params(axis="y", labelsize=8.5)
for spine in ("top", "right"):
    ax.spines[spine].set_visible(False)
ax.set_title("PAS-focused docking against human AChE (PDB 4EY6)",
             fontsize=10, loc="left", pad=10)
fig.tight_layout()

out = Path(__file__).resolve().parent.parent / "manuscript" / "figures"
out.mkdir(parents=True, exist_ok=True)
fig.savefig(out / "fig5_docking_scores.pdf")
fig.savefig(out / "fig5_docking_scores.png", dpi=300)
print("saved:", out / "fig5_docking_scores.pdf")
