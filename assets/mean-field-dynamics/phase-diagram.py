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
that segment is a kernel method (red, the post's colour for NTK / lazy); only
the far endpoint learns features (blue, the post's colour for mean-field).
The stability boundary kinks from slope -2 to slope -1 at precisely that
endpoint, so mu-P is the corner where the segment dead-ends into instability
-- the edge of stability. Along the segment the output amplification
alpha = N^{1-a} shrinks from sqrt(N) (NTK) to 1 (mean-field).

Output: assets/mean-field-dynamics/phase-diagram.png
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# --- palette (shared with timeline.png / three-views.png) ----------------
BLUE   = "#2166ac"   # mean-field / feature learning
RED    = "#b2182b"   # NTK / kernel / lazy
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
    fraction `at` along it and pushed `dist` points off to its upper-right."""
    ang = seg_angle(ax, p0, p1)
    nx, ny = -np.sin(np.radians(ang)), np.cos(np.radians(ang))
    xy = (p0[0] + at * (p1[0] - p0[0]), p0[1] + at * (p1[1] - p0[1]))
    ax.annotate(s, xy=xy, xytext=(nx * dist, ny * dist),
                textcoords="offset points", rotation=ang,
                rotation_mode="anchor", ha="center", va="center", **kw)


fig, ax = plt.subplots(figsize=(9.2, 7.2))
ax.set_xlim(A_MIN, A_MAX)
ax.set_ylim(C_MIN, C_MAX)

# =========================================================================
# the two phases, as polygons bounded by the kinked stability line
# =========================================================================
unstable = [(A_MIN, C_MAX), (0.5, C_MAX), P_NTK, P_MF, (A_MAX, -A_MAX),
            (A_MAX, C_MIN), (A_MIN, C_MIN)]
trivial = [P_NTK, (0.5, C_MAX), (A_MAX, C_MAX), (A_MAX, -A_MAX), P_MF]
ax.add_patch(Polygon(unstable, closed=True, facecolor=RED, alpha=0.13,
                     edgecolor="none", zorder=0))
ax.add_patch(Polygon(trivial, closed=True, facecolor=GREY, alpha=0.15,
                     edgecolor="none", zorder=0))

# stability boundary where nothing lives: the wall a = 1/2, and the
# post-kink ray c = -a
ax.plot([0.5, 0.5], [0.0, C_MAX], color=RED, alpha=0.5, lw=1.4,
        ls=(0, (5, 3)), zorder=2)
ax.plot([1.0, A_MAX], [-1.0, -A_MAX], color=RED, alpha=0.5, lw=1.4,
        ls=(0, (5, 3)), zorder=2)

# =========================================================================
# the segment 2a + c = 1 : every stable, non-trivial limit
# =========================================================================
ax.plot([P_NTK[0], P_MF[0]], [P_NTK[1], P_MF[1]], color="white", lw=7.5,
        solid_capstyle="round", zorder=4)
ax.plot([P_NTK[0], P_MF[0]], [P_NTK[1], P_MF[1]], color=RED, lw=4.5,
        solid_capstyle="round", zorder=5)

# NTK: the top end of the segment, and the corner of the stable region
ax.scatter([P_NTK[0]], [P_NTK[1]], s=130, color=RED, edgecolor="white",
           linewidth=1.6, zorder=7)
# mean-field = muP: the far end, sitting in the kink of the boundary
ax.scatter([P_MF[0]], [P_MF[1]], s=1000, color=BLUE, alpha=0.15, zorder=6)
ax.scatter([P_MF[0]], [P_MF[1]], marker="*", s=460, color=BLUE,
           edgecolor="white", linewidth=1.2, zorder=7)

# =========================================================================
# axes
# =========================================================================
ax.set_xlabel(r"output exponent $a$      "
              r"($f = N^{-a}\sum_i v_i\,\sigma(w_i \cdot x)$)",
              fontsize=13, color=TEXT, labelpad=9)
ax.set_ylabel(r"learning-rate exponent $c$      "
              r"(step size $=\eta\,N^{-c}$)",
              fontsize=13, color=TEXT, labelpad=9)
ax.set_xticks([0.25, 0.50, 0.75, 1.00, 1.25])
ax.set_yticks([-1.5, -1.0, -0.5, 0.0, 0.5])
ax.tick_params(labelsize=11, colors=TEXT2, length=4, width=0.9)
for s in ax.spines.values():
    s.set_color(FRAME)
    s.set_linewidth(0.9)
# the coordinates of the two marked points, picked out on the axes
for lab, col in zip(ax.get_xticklabels(), [None, RED, None, BLUE, None]):
    if col:
        lab.set_color(col)
for lab, col in zip(ax.get_yticklabels(), [None, BLUE, None, RED, None]):
    if col:
        lab.set_color(col)

ax.set_title(r"Every stable, non-trivial limit lies on the line $2a + c = 1$",
             fontsize=14.5, color="#2a2a2a", pad=13)

fig.tight_layout()
fig.canvas.draw()          # fix the axes box before measuring screen angles

# =========================================================================
# region labels
# =========================================================================
ax.text(0.90, -1.30, "unstable", ha="center", va="center", fontsize=17,
        color=RED, zorder=8)
ax.text(0.90, -1.49, r"the updates blow up as $N\to\infty$", ha="center",
        va="center", fontsize=10.5, color=RED, alpha=0.85, style="italic",
        zorder=8)
ax.text(0.325, -0.30, "the output already diverges at initialization",
        ha="center", va="center", rotation=90, fontsize=10.5, color=RED,
        alpha=0.85, style="italic", zorder=8)

ax.text(1.03, 0.61, "stable but trivial", ha="center", va="center",
        fontsize=15, color="#4a4a4a", zorder=8)
ax.text(1.03, 0.45, "(the limit function never moves)", ha="center",
        va="center", fontsize=10.5, color=MUTED, style="italic", zorder=8)

# =========================================================================
# the segment, its two endpoints, the amplification running along it
# =========================================================================
label_along(ax, P_NTK, P_MF, "kernel regime (lazy training)", at=0.50,
            dist=45, fontsize=12.5, color=RED, zorder=8)
label_along(ax, P_NTK, P_MF, r"$\alpha = N^{1-a}:\ \ \sqrt{N}\ \to\ 1$",
            at=0.50, dist=16, fontsize=11, color=TEXT2, zorder=8)

ax.text(0.545, 0.26, "NTK parametrization", ha="left", va="center",
        fontsize=12.5, color=RED, zorder=8)
ax.text(0.545, 0.12, r"$(a, c) = (\frac{1}{2},\, 0)$", ha="left",
        va="center", fontsize=10.5, color=MUTED, zorder=8)

ax.plot([1.045, 1.022], [-0.92, -0.955], color=BLUE, alpha=0.55, lw=1.0,
        zorder=6)
ax.text(1.06, -0.45, "feature learning", ha="left", va="center",
        fontsize=13, color=BLUE, zorder=8)
ax.text(1.06, -0.60, r"mean-field$\,=\,\mu$P", ha="left", va="center",
        fontsize=12, color=BLUE, zorder=8)
ax.text(1.06, -0.74, r"$(a, c) = (1,\, -1)$", ha="left", va="center",
        fontsize=10.5, color=MUTED, zorder=8)
ax.text(1.06, -0.89, "the edge of stability", ha="left", va="center",
        fontsize=10.5, color=BLUE, style="italic", zorder=8)

# the boundary kinks exactly at muP: slope -2 above, slope -1 beyond
label_along(ax, P_MF, (A_MAX, -A_MAX),
            r"stability boundary $c = -a$", at=0.54, dist=13,
            fontsize=10.5, color=MUTED, zorder=8)

plt.savefig("assets/mean-field-dynamics/phase-diagram.png", dpi=150,
            bbox_inches="tight", facecolor="white")
plt.close()
print("saved assets/mean-field-dynamics/phase-diagram.png")
