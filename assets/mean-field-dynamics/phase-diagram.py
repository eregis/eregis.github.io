"""
Phase diagram of the two-layer network in the abc-parametrization, after
Yang & Hu (2020), arXiv:2011.14522 (Theorems 3.3-3.4 and Table 1).

    f(x) = N^{-a} sum_i v_i sigma(w_i . x),   both layers at O(1) init,
    trained by gradient descent with step size eta * N^{-c}.

The plane is (a, c). Two exponents, three outcomes:

    a < 1/2                     -> the output already diverges at init
    c < max(1 - 2a, -a)         -> the updates blow up
    otherwise                   -> stable, but the limit function never moves
    2a + c = 1, 1/2 <= a <= 1   -> the only stable, non-trivial limits

So the interesting set is not a region but a *line segment*: the piece of
2a + c = 1 running from the NTK point (1/2, 0) to the mean-field point
(1, -1), sitting exactly on the stability boundary. Every interior point of
that segment is a kernel method (red, the post's colour for the lazy regime;
the NTK endpoint a deeper shade of it); only
the far endpoint learns features (blue, the post's colour for mean-field).
The stability boundary kinks from slope -2 to slope -1 at precisely that
endpoint, so mu-P is the corner where the segment dead-ends into instability.
The unstable phase is amber, not red, so that red means lazy and nothing else.

Design notes (September 2026 revision, after reader feedback that the first
version was busy): the model and the update rule sit in one setup box; the
output amplification alpha = N^{1-a}, which depends on a alone, is a second
x-axis along the top instead of a label along the segment; the three pieces
of the stability boundary each carry their equation in the same small grey
type; the endpoints carry names only, their coordinates being picked out by
the coloured tick labels.

Output: assets/mean-field-dynamics/phase-diagram.png
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# --- palette (shared with timeline.png / three-views.png) ----------------
BLUE   = "#2166ac"   # mean-field / feature learning
RED    = "#b2182b"   # kernel / lazy regime
NTKRED = "#7a0f1c"   # the NTK endpoint: a deeper shade of the same red
AMBER  = "#d9832b"   # the unstable phase (kept distinct from the lazy red)
AMBER2 = "#a85e10"   # its label
GREY   = "#9a9a9a"   # the trivial phase
TEXT   = "#333333"
TEXT2  = "#555555"
MUTED  = "#6b6b6b"
FRAME  = "#bbbbbb"

# --- view window and the two distinguished parametrizations --------------
A_MIN, A_MAX = 0.15, 1.45
C_MIN, C_MAX = -1.75, 0.85
P_NTK = (0.5, 0.0)     # NTK parametrization
P_MF = (1.0, -1.0)     # mean-field = muP


def seg_angle(ax, p0, p1):
    """Screen-space angle (degrees) of the data segment p0 -> p1."""
    (x0, y0), (x1, y1) = ax.transData.transform([p0, p1])
    return np.degrees(np.arctan2(y1 - y0, x1 - x0))


def label_along(ax, p0, p1, s, at, dist, **kw):
    """Text set parallel to the segment p0 -> p1, anchored at the point a
    fraction `at` along it and pushed `dist` points off to its upper-right
    (negative `dist`: lower-left)."""
    ang = seg_angle(ax, p0, p1)
    nx, ny = -np.sin(np.radians(ang)), np.cos(np.radians(ang))
    xy = (p0[0] + at * (p1[0] - p0[0]), p0[1] + at * (p1[1] - p0[1]))
    ax.annotate(s, xy=xy, xytext=(nx * dist, ny * dist),
                textcoords="offset points", rotation=ang,
                rotation_mode="anchor", ha="center", va="center", **kw)


fig, ax = plt.subplots(figsize=(9.2, 7.4))
ax.set_xlim(A_MIN, A_MAX)
ax.set_ylim(C_MIN, C_MAX)

# =========================================================================
# the two phases, as polygons bounded by the kinked stability line
# =========================================================================
unstable = [(A_MIN, C_MAX), (0.5, C_MAX), P_NTK, P_MF, (A_MAX, -A_MAX),
            (A_MAX, C_MIN), (A_MIN, C_MIN)]
trivial = [P_NTK, (0.5, C_MAX), (A_MAX, C_MAX), (A_MAX, -A_MAX), P_MF]
ax.add_patch(Polygon(unstable, closed=True, facecolor=AMBER, alpha=0.16,
                     edgecolor="none", zorder=0))
ax.add_patch(Polygon(trivial, closed=True, facecolor=GREY, alpha=0.15,
                     edgecolor="none", zorder=0))

# stability boundary where nothing lives: the wall a = 1/2, and the
# post-kink ray c = -a
ax.plot([0.5, 0.5], [0.0, C_MAX], color=AMBER, alpha=0.7, lw=1.4,
        ls=(0, (5, 3)), zorder=2)
ax.plot([1.0, A_MAX], [-1.0, -A_MAX], color=AMBER, alpha=0.7, lw=1.4,
        ls=(0, (5, 3)), zorder=2)

# =========================================================================
# the segment 2a + c = 1 : every stable, non-trivial limit
# =========================================================================
ax.plot([P_NTK[0], P_MF[0]], [P_NTK[1], P_MF[1]], color="white", lw=7.5,
        solid_capstyle="round", zorder=4)
ax.plot([P_NTK[0], P_MF[0]], [P_NTK[1], P_MF[1]], color=RED, lw=4.5,
        solid_capstyle="round", zorder=5)

# NTK: the top end of the segment, and the corner of the stable region
ax.scatter([P_NTK[0]], [P_NTK[1]], s=150, color=NTKRED, edgecolor="white",
           linewidth=1.6, zorder=7)
# mean-field = muP: the far end, sitting in the kink of the boundary
ax.scatter([P_MF[0]], [P_MF[1]], marker="*", s=460, color=BLUE,
           edgecolor="white", linewidth=1.2, zorder=7)

# =========================================================================
# axes
# =========================================================================
ax.set_xlabel(r"output exponent $a$", fontsize=13, color=TEXT, labelpad=9)
ax.set_ylabel(r"learning-rate exponent $c$", fontsize=13, color=TEXT,
              labelpad=9)
ax.set_xticks([0.25, 0.50, 0.75, 1.00, 1.25])
ax.set_yticks([-1.5, -1.0, -0.5, 0.0, 0.5])
ax.tick_params(labelsize=11, colors=TEXT2, length=4, width=0.9)
for s in ax.spines.values():
    s.set_color(FRAME)
    s.set_linewidth(0.9)
# the coordinates of the two marked points, picked out on the axes
for lab, col in zip(ax.get_xticklabels(), [None, NTKRED, None, BLUE, None]):
    if col:
        lab.set_color(col)
for lab, col in zip(ax.get_yticklabels(), [None, BLUE, None, NTKRED, None]):
    if col:
        lab.set_color(col)

# the output amplification alpha = N^{1-a} depends on a alone, so it is a
# second horizontal axis rather than a label along the segment
top = ax.secondary_xaxis("top")
top.set_xticks([0.25, 0.50, 0.75, 1.00, 1.25])
top.set_xticklabels([r"$N^{3/4}$", r"$\sqrt{N}$", r"$N^{1/4}$", r"$1$",
                     r"$N^{-1/4}$"])
top.tick_params(labelsize=11, colors=TEXT2, length=4, width=0.9)
top.spines["top"].set_color(FRAME)
top.spines["top"].set_linewidth(0.9)
top.set_xlabel(r"output amplification $\alpha = N^{1-a}$"
               r"  (relative to mean-field)", fontsize=12, color=TEXT2,
               labelpad=8)
for lab, col in zip(top.get_xticklabels(), [None, NTKRED, None, BLUE, None]):
    if col:
        lab.set_color(col)

fig.suptitle(r"Every stable, non-trivial limit lies on the line $2a + c = 1$",
             fontsize=14.5, color="#2a2a2a", y=0.985)

fig.tight_layout(rect=(0, 0, 1, 0.965))
fig.canvas.draw()          # fix the axes box before measuring screen angles

# =========================================================================
# the system under study, in one box
# =========================================================================
ax.text(0.19, -1.67,
        r"$f(x) = N^{-a}\sum_{i=1}^{N} v_i\,\sigma(w_i \cdot x)$" "\n"
        r"$\theta \leftarrow \theta - \eta\,N^{-c}\,\nabla_\theta L$"
        r",$\quad$ $w_i, v_i = O(1)$ at init",
        ha="left", va="bottom", fontsize=11, color=TEXT, zorder=9,
        linespacing=1.7,
        bbox=dict(boxstyle="round,pad=0.55", facecolor="white",
                  edgecolor=FRAME, linewidth=0.9))

# =========================================================================
# region labels
# =========================================================================
ax.text(1.0, -1.42, "unstable", ha="center", va="center", fontsize=17,
        color=AMBER2, zorder=8)
ax.text(1.03, 0.60, "stable but trivial", ha="center", va="center",
        fontsize=15, color="#4a4a4a", zorder=8)
ax.text(1.03, 0.45, "(the limit function never moves)", ha="center",
        va="center", fontsize=10.5, color=MUTED, style="italic", zorder=8)

# =========================================================================
# the three pieces of the stability boundary, each with its equation
# =========================================================================
ax.text(0.475, 0.55, r"$a = 1/2$", ha="center", va="center",
        rotation=90, fontsize=10.5, color=MUTED, zorder=8)
label_along(ax, P_NTK, P_MF, r"$2a + c = 1$", at=0.42, dist=-14,
            fontsize=10.5, color=MUTED, zorder=8)
label_along(ax, P_MF, (A_MAX, -A_MAX), r"$c = -a$", at=0.55, dist=13,
            fontsize=10.5, color=MUTED, zorder=8)

# =========================================================================
# the segment and its two endpoints
# =========================================================================
label_along(ax, P_NTK, P_MF, "kernel regime (lazy training)", at=0.50,
            dist=16, fontsize=12.5, color=RED, zorder=8)

ax.text(0.545, 0.12, "NTK parametrization", ha="left", va="center",
        fontsize=12.5, color=NTKRED, zorder=8)

ax.text(1.06, -0.60, "feature learning", ha="left", va="center",
        fontsize=13, color=BLUE, zorder=8)
ax.text(1.06, -0.76, r"mean-field$\,=\,\mu$P", ha="left", va="center",
        fontsize=12, color=BLUE, zorder=8)

plt.savefig("assets/mean-field-dynamics/phase-diagram.png", dpi=150,
            bbox_inches="tight", facecolor="white")
plt.close()
print("saved assets/mean-field-dynamics/phase-diagram.png")
