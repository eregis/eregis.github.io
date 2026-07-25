"""
Timeline of the mean-field limit of two-layer neural networks.

Seven arXiv v1 submissions, spring 2018 to late 2020. The visual point is the
burst at the start: four mean-field papers (blue) landed in a five-week window
in April-May 2018, describing the same object -- the gradient flow of the
network's empirical measure of neurons -- from four angles. Weeks later the
neural tangent kernel (red) offered a rival large-width description, and the
tension between the two was reconciled over the next two years by lazy training
and the muP / feature-learning framework (green).

The four concurrent papers are drawn as a stacked callout in the upper left,
with thin converging leader lines running down to their (nearly coincident)
markers on the time axis; a shaded stripe marks the five-week window. The later,
sparse events sit directly on the axis with short stems.

Output: assets/mean-field-dynamics/timeline.png
"""
import datetime
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


def dnum(y, m, d):
    """Date -> matplotlib-friendly ordinal day number (1 unit = 1 day)."""
    return datetime.date(y, m, d).toordinal()


# --- palette -------------------------------------------------------------
BLUE  = "#2166ac"   # A: the mean-field limit
RED   = "#b2182b"   # B: the neural tangent kernel (the rival description)
GREEN = "#1b7837"   # C: the reconciliation
MUTED = "#6b6b6b"
AXIS  = "#8a8a8a"

GROUP_COLOR = {"A": BLUE, "B": RED, "C": GREEN}

# --- the seven papers: (date, surnames, descriptor, group, date label) ---
papers = [
    (dnum(2018,  4, 18), "Mei, Montanari & Nguyen",   "distributional dynamics",   "A", "18 Apr"),
    (dnum(2018,  5,  2), "Rotskoff & Vanden-Eijnden", "interacting particles",     "A", "2 May"),
    (dnum(2018,  5,  2), "Sirignano & Spiliopoulos",  "law of large numbers",      "A", "2 May"),
    (dnum(2018,  5, 24), "Chizat & Bach",             "global convergence",        "A", "24 May"),
    (dnum(2018,  6, 20), "Jacot, Gabriel & Hongler",  "neural tangent kernel",     "B", "20 Jun 2018"),
    (dnum(2018, 12, 19), "Chizat, Oyallon & Bach",    "lazy training",             "C", "19 Dec 2018"),
    (dnum(2020, 11, 30), "Yang & Hu",                 r"$\mu$P / feature learning", "C", "30 Nov 2020"),
]

fig, ax = plt.subplots(figsize=(11.5, 5.2))

# --- the time axis -------------------------------------------------------
x_start, x_end = dnum(2018, 1, 1), dnum(2021, 1, 31)
ax.plot([x_start, x_end], [0, 0], color=AXIS, lw=1.8, zorder=1,
        solid_capstyle="round")
ax.annotate("", xy=(x_end + 26, 0), xytext=(x_end, 0),
            arrowprops=dict(arrowstyle="-|>", color=AXIS, lw=1.8))

# year ticks
for yr in range(2018, 2022):
    xt = dnum(yr, 1, 1)
    ax.plot([xt, xt], [-0.14, 0.14], color=AXIS, lw=1.3, zorder=2)
    ax.text(xt, -0.52, str(yr), ha="center", va="top", fontsize=11,
            color="#555555")

# --- the five-week window (Group A) --------------------------------------
band_lo, band_hi = dnum(2018, 4, 18), dnum(2018, 5, 24)
ax.axvspan(band_lo, band_hi, color=BLUE, alpha=0.10, zorder=0)

# a slim bracket over the window, captioned
y_br = 4.18
ax.plot([band_lo, band_hi], [y_br, y_br], color=BLUE, lw=1.2, alpha=0.75, zorder=3)
ax.plot([band_lo, band_lo], [y_br - 0.12, y_br], color=BLUE, lw=1.2, alpha=0.75, zorder=3)
ax.plot([band_hi, band_hi], [y_br - 0.12, y_br], color=BLUE, lw=1.2, alpha=0.75, zorder=3)
ax.text((band_lo + band_hi) / 2, y_br + 0.08, "four papers in five weeks",
        ha="center", va="bottom", fontsize=12, color=BLUE, style="italic")

# --- Group A: stacked callout in the upper left, converging leaders -------
x_dot_A = dnum(2018, 3, 12)          # column where the four callout dots sit
A_levels = [1.05, 1.95, 2.85, 3.75]  # earliest lowest -> latest highest (no crossings)
pad = 9                              # text gap from the dot, in days

for (xm, auth, desc, grp, ds), lvl in zip(papers[:4], A_levels):
    ax.plot([xm, x_dot_A], [0, lvl], color=BLUE, lw=1.0, alpha=0.55, zorder=2,
            solid_capstyle="round")
    ax.scatter([x_dot_A], [lvl], s=26, color=BLUE, zorder=5,
               edgecolor="white", linewidth=0.8)
    ax.text(x_dot_A - pad, lvl + 0.19, auth, ha="right", va="center",
            fontsize=12, color=BLUE)
    ax.text(x_dot_A - pad, lvl - 0.19, f"{desc} · {ds}", ha="right",
            va="center", fontsize=10, color=MUTED, style="italic")

# --- Group B: below the axis (the rival description, opposite side) -------
xB = papers[4][0]
ax.plot([xB, xB], [0, -0.92], color=RED, lw=1.0, alpha=0.55, zorder=2)
ax.scatter([xB], [-0.92], s=26, color=RED, zorder=5,
           edgecolor="white", linewidth=0.8)
ax.text(xB, -1.08, papers[4][1], ha="center", va="top", fontsize=12, color=RED)
ax.text(xB, -1.44, f"{papers[4][2]} · {papers[4][4]}", ha="center",
        va="top", fontsize=10, color=MUTED, style="italic")

# --- Group C: above the axis, short stems --------------------------------
lvl_C = 1.05
# C1 (lazy training): text extends right
xC1, aC1, dC1, _, sC1 = papers[5]
ax.plot([xC1, xC1], [0, lvl_C], color=GREEN, lw=1.0, alpha=0.55, zorder=2)
ax.scatter([xC1], [lvl_C], s=26, color=GREEN, zorder=5,
           edgecolor="white", linewidth=0.8)
ax.text(xC1 + pad, lvl_C + 0.19, aC1, ha="left", va="center",
        fontsize=12, color=GREEN)
ax.text(xC1 + pad, lvl_C - 0.19, f"{dC1} · {sC1}", ha="left",
        va="center", fontsize=10, color=MUTED, style="italic")

# C2 (muP / feature learning): near the right edge, text extends left
xC2, aC2, dC2, _, sC2 = papers[6]
ax.plot([xC2, xC2], [0, lvl_C], color=GREEN, lw=1.0, alpha=0.55, zorder=2)
ax.scatter([xC2], [lvl_C], s=26, color=GREEN, zorder=5,
           edgecolor="white", linewidth=0.8)
ax.text(xC2 - pad, lvl_C + 0.19, aC2, ha="right", va="center",
        fontsize=12, color=GREEN)
ax.text(xC2 - pad, lvl_C - 0.19, f"{dC2} · {sC2}", ha="right",
        va="center", fontsize=10, color=MUTED, style="italic")

# --- markers on the axis (drawn last, on top) ----------------------------
for xm, auth, desc, grp, ds in papers:
    ax.scatter([xm], [0], s=80, color=GROUP_COLOR[grp], zorder=6,
               edgecolor="white", linewidth=1.4)

# --- small colour key ----------------------------------------------------
handles = [
    Line2D([0], [0], marker="o", linestyle="none", markerfacecolor=BLUE,
           markeredgecolor="white", markersize=9, label="mean-field limit"),
    Line2D([0], [0], marker="o", linestyle="none", markerfacecolor=RED,
           markeredgecolor="white", markersize=9, label="neural tangent kernel"),
    Line2D([0], [0], marker="o", linestyle="none", markerfacecolor=GREEN,
           markeredgecolor="white", markersize=9, label="reconciliation"),
]
ax.legend(handles=handles, loc="lower right", frameon=False, fontsize=10.5,
          handletextpad=0.4, labelspacing=0.55, borderaxespad=1.2)

# --- cosmetics -----------------------------------------------------------
ax.set_xlim(dnum(2017, 8, 1), dnum(2021, 5, 1))
ax.set_ylim(-2.05, 4.95)
for s in ax.spines.values():
    s.set_visible(False)
ax.set_xticks([])
ax.set_yticks([])
ax.set_title("The mean-field limit of two-layer networks", fontsize=14,
             color="#2a2a2a", pad=12)

plt.tight_layout()
plt.savefig("assets/mean-field-dynamics/timeline.png", dpi=150,
            bbox_inches="tight", facecolor="white")
plt.close()
print("saved assets/mean-field-dynamics/timeline.png")
