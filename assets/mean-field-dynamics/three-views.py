"""
Three descriptions of the same two-layer network, for the intro of
"Mean-Field Dynamics Explained".

    left   -> the network:            f(x) = sum_i v_i sigma(w_i . x)
    middle -> one long vector:        theta in R^{N(d+1)}, sliced along neurons
    right  -> a measure over neurons: mu_N = (1/N) sum_i delta_{theta_i}

The conceptual pivot of the post is that one stops tracking the long parameter
vector and instead tracks the empirical distribution over neurons. The figure
carries a single representative neuron i in the warm accent (red) across all
three panels -- one hidden node, one vector block, one particle -- so the reader
can trace it; everything else is in the primary blue. The two gutter arrows name
the moves: "stack the parameters" (bookkeeping) and "forget the ordering"
(exchangeability -- the output depends only on how many neurons sit where).

Output: assets/mean-field-dynamics/three-views.png
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, FancyArrowPatch

# --- palette (shared with timeline.png) ----------------------------------
BLUE      = "#2166ac"   # primary
NODE_FILL = "#4A90D9"   # blue node fill
NODE_EDGE = "#2C5F8A"   # blue node edge
BLOCK_FILL = "#dbe7f3"  # light-blue vector block
RED       = "#b2182b"   # accent: sigma + highlighted-neuron outline
HL_FILL   = "#d6604d"   # highlighted node / block fill
HL_CELL_V = "#f4a582"   # expanded v_i cell
HL_CELL_W = "#fbddcc"   # expanded w_i cells
DIVIDER   = "#BBBBBB"   # edges / dividers
AXISGREY  = "#8a8a8a"
TEXT      = "#333333"
TEXT2     = "#555555"
MUTED     = "#6b6b6b"

# --- panel / gutter centres in figure coords (kept consistent with the
#     subplots_adjust call below so fig.text and the arrows line up) --------
L, Rr, WSP = 0.015, 0.985, 0.22
_w = (Rr - L) / (3 + 2 * WSP)
_gap = WSP * _w
PC1 = L + 0.5 * _w
PC2 = L + 1.5 * _w + _gap
PC3 = L + 2.5 * _w + 2 * _gap
G1 = L + _w + 0.5 * _gap          # gutter 1 centre
G2 = L + 2 * _w + 1.5 * _gap      # gutter 2 centre


def draw_brace_v(ax, x, y0, y1, depth=0.18, color=TEXT2, lw=1.5):
    """A right-facing curly brace: vertical spine at x spanning [y0, y1],
    tip pointing to +x (toward the label)."""
    res = 201
    y = np.linspace(y0, y1, res)
    half = y[:res // 2 + 1]
    beta = 14.0 / (y1 - y0)
    curve = (1.0 / (1.0 + np.exp(-beta * (half - half[0])))
             + 1.0 / (1.0 + np.exp(-beta * (half - half[-1]))))
    curve = np.concatenate([curve, curve[-2::-1]])
    curve = curve - curve.min()
    curve = curve / curve.max()
    ax.plot(x + depth * curve, y, color=color, lw=lw,
            clip_on=False, solid_capstyle="round", zorder=6)


# =========================================================================
fig, axes = plt.subplots(1, 3, figsize=(14.5, 5.8))
fig.subplots_adjust(left=L, right=Rr, top=0.87, bottom=0.17, wspace=WSP)
ax1, ax2, ax3 = axes
for ax in axes:
    ax.set_aspect("equal")
    ax.axis("off")


# =========================================================================
# PANEL 1 -- the network
# =========================================================================
x_in, x_hid, x_out = 0.0, 1.6, 3.2
r = 0.17
in_y = np.array([0.8, 0.0, -0.8])
hid_y = np.array([1.6, 0.8, 0.0, -0.8, -1.6])     # slot 3 (idx 3) is the ellipsis
hid_is_node = np.array([True, True, True, False, True])
HL = 1                                            # highlighted hidden slot -> neuron i

hid_node_y = hid_y[hid_is_node]

# edges input -> hidden (grey; the highlighted neuron's own edges in red)
for yi in in_y:
    for j, yh in enumerate(hid_y):
        if not hid_is_node[j]:
            continue
        if j == HL:
            ax1.plot([x_in, x_hid], [yi, yh], color=HL_FILL, lw=1.6,
                     alpha=0.9, zorder=1)
        else:
            ax1.plot([x_in, x_hid], [yi, yh], color=DIVIDER, lw=0.8, zorder=1)

# edges hidden -> output
for j, yh in enumerate(hid_y):
    if not hid_is_node[j]:
        continue
    if j == HL:
        ax1.plot([x_hid, x_out], [yh, 0.0], color=HL_FILL, lw=1.6,
                 alpha=0.9, zorder=1)
    else:
        ax1.plot([x_hid, x_out], [yh, 0.0], color=DIVIDER, lw=0.8, zorder=1)

# input nodes
for yi in in_y:
    ax1.add_patch(Circle((x_in, yi), r, facecolor=NODE_FILL, edgecolor=NODE_EDGE,
                         linewidth=1.5, zorder=3))
# hidden nodes (+ vertical ellipsis in the empty slot)
for j, yh in enumerate(hid_y):
    if not hid_is_node[j]:
        ax1.text(x_hid, yh, r"$\vdots$", ha="center", va="center",
                 fontsize=16, color=AXISGREY, zorder=3)
        continue
    if j == HL:
        ax1.add_patch(Circle((x_hid, yh), r, facecolor=HL_FILL, edgecolor=RED,
                             linewidth=1.8, zorder=4))
    else:
        ax1.add_patch(Circle((x_hid, yh), r, facecolor=NODE_FILL,
                             edgecolor=NODE_EDGE, linewidth=1.5, zorder=3))
# output node
ax1.add_patch(Circle((x_out, 0.0), r, facecolor=NODE_FILL, edgecolor=NODE_EDGE,
                     linewidth=1.5, zorder=3))

# annotations
ax1.text(x_hid, 2.12, r"$\sigma$", ha="center", va="bottom", fontsize=15,
         color=RED)
ax1.text(0.72, 1.32, r"$w_i$", ha="center", va="center", fontsize=13, color=RED)
ax1.text(2.52, 0.72, r"$v_i$", ha="center", va="center", fontsize=13, color=RED)
ax1.text(x_out + 0.42, 0.0, r"$f$", ha="left", va="center", fontsize=14,
         color=TEXT)
ax1.text(x_in, -2.18, r"input $x\in\mathbb{R}^{d}$", ha="center", va="top",
         fontsize=12, color=TEXT2, style="italic")
ax1.text(x_hid, -2.18, r"$N$ neurons", ha="center", va="top",
         fontsize=12, color=TEXT2, style="italic")

ax1.set_xlim(-1.0, 4.0)
ax1.set_ylim(-2.6, 2.5)


# =========================================================================
# PANEL 2 -- one long vector (sliced along neurons)
# =========================================================================
col_cx, col_w = -1.45, 1.25
xl = col_cx - col_w / 2
xr = col_cx + col_w / 2

# block stack: (label, height, kind)  kind in {"blk","hl","dots"}
rows = [
    (r"$\theta_1$", 0.62, "blk"),
    (r"$\theta_2$", 0.62, "blk"),
    (None,          0.34, "dots"),
    (r"$\theta_i$", 0.62, "hl"),
    (None,          0.34, "dots"),
    (r"$\theta_N$", 0.62, "blk"),
]
total_h = sum(h for _, h, _ in rows)
y_top = total_h / 2.0
y = y_top
hl_top = hl_bot = None
for label, h, kind in rows:
    y0, y1 = y - h, y
    if kind == "dots":
        ax2.text(col_cx, 0.5 * (y0 + y1), r"$\vdots$", ha="center",
                 va="center", fontsize=15, color=AXISGREY)
    else:
        fill = HL_FILL if kind == "hl" else BLOCK_FILL
        edge = RED if kind == "hl" else NODE_EDGE
        ax2.add_patch(Rectangle((xl, y0), col_w, h, facecolor=fill,
                                edgecolor=edge, linewidth=1.6,
                                zorder=3 if kind == "hl" else 2))
        tcol = "white" if kind == "hl" else TEXT
        ax2.text(col_cx, 0.5 * (y0 + y1), label, ha="center", va="center",
                 fontsize=13.5, color=tcol,
                 fontweight="bold" if kind == "hl" else "normal", zorder=4)
        if kind == "hl":
            hl_top, hl_bot = y1, y0
    y = y0

# divider ticks: little stubs on each side to say "cut here, between neurons"
y = y_top
for _, h, _ in rows:
    for xx, dx in ((xl, -0.13), (xr, 0.13)):
        ax2.plot([xx, xx + dx], [y, y], color=AXISGREY, lw=1.2,
                 solid_capstyle="round", zorder=1)
    y -= h
for xx, dx in ((xl, -0.13), (xr, 0.13)):     # bottom edge
    ax2.plot([xx, xx + dx], [y, y], color=AXISGREY, lw=1.2,
             solid_capstyle="round", zorder=1)

ax2.text(col_cx, y_top + 0.30, r"$\theta\in\mathbb{R}^{N(d+1)}$", ha="center",
         va="bottom", fontsize=13, color=TEXT)

# --- expansion of the highlighted block --------------------------------
ex_cx, ex_w = 1.15, 1.05
ex_xl, ex_xr = ex_cx - ex_w / 2, ex_cx + ex_w / 2
cells = [
    (r"$v_i$",       HL_CELL_V),
    (r"$w_{i,1}$",   HL_CELL_W),
    (r"$w_{i,2}$",   HL_CELL_W),
    (r"$\vdots$",    HL_CELL_W),
    (r"$w_{i,d}$",   HL_CELL_W),
]
cell_h = 0.5
ex_top = len(cells) * cell_h / 2.0
# zoom cone from the source block to the expanded stack
ax2.fill([xr, ex_xl, ex_xl, xr], [hl_top, ex_top, -ex_top, hl_bot],
         color=HL_FILL, alpha=0.07, zorder=0, edgecolor="none")
ax2.plot([xr, ex_xl], [hl_top, ex_top], color=DIVIDER, lw=1.0, ls="--", zorder=1)
ax2.plot([xr, ex_xl], [hl_bot, -ex_top], color=DIVIDER, lw=1.0, ls="--", zorder=1)

yy = ex_top
for label, fill in cells:
    y0 = yy - cell_h
    if label == r"$\vdots$":
        ax2.add_patch(Rectangle((ex_xl, y0), ex_w, cell_h, facecolor=fill,
                                edgecolor=RED, linewidth=1.4, zorder=3))
        ax2.text(ex_cx, 0.5 * (y0 + yy), r"$\vdots$", ha="center", va="center",
                 fontsize=13, color=TEXT)
    else:
        ax2.add_patch(Rectangle((ex_xl, y0), ex_w, cell_h, facecolor=fill,
                                edgecolor=RED, linewidth=1.4, zorder=3))
        ax2.text(ex_cx, 0.5 * (y0 + yy), label, ha="center", va="center",
                 fontsize=12.5, color=TEXT, zorder=4)
    yy = y0

# brace spanning the d+1 cells
draw_brace_v(ax2, ex_xr + 0.10, -ex_top, ex_top, depth=0.16, color=TEXT2, lw=1.5)
ax2.text(ex_xr + 0.40, 0.0, r"$d+1$", ha="left", va="center", fontsize=12.5,
         color=TEXT)

ax2.text(ex_cx - 0.15, -ex_top - 0.30,
         r"$\theta_i=(v_i,w_i)\in\mathbb{R}^{d+1}$", ha="center", va="top",
         fontsize=12.5, color=TEXT)

ax2.set_xlim(-2.55, 2.55)
ax2.set_ylim(-2.6, 2.5)


# =========================================================================
# PANEL 3 -- a measure over neurons
# =========================================================================
rng = np.random.default_rng(7)
c1 = rng.normal(0.0, 1.0, (22, 2)) * np.array([0.45, 0.40]) + np.array([-0.62, 0.50])
c2 = rng.normal(0.0, 1.0, (18, 2)) * np.array([0.50, 0.42]) + np.array([0.66, -0.42])
pts = np.vstack([c1, c2])
pts = np.clip(pts, -1.5, 1.5)
hl_pt = np.array([-0.30, 1.02])            # the representative neuron i
pts_all = np.vstack([pts, hl_pt])

# soft density cloud: gaussian KDE, drawn as translucent filled contours
gx = np.linspace(-1.9, 1.9, 220)
gy = np.linspace(-1.9, 1.9, 220)
GX, GY = np.meshgrid(gx, gy)
h = 0.30
Z = np.zeros_like(GX)
for px, py in pts_all:
    Z += np.exp(-((GX - px) ** 2 + (GY - py) ** 2) / (2 * h * h))
levels = np.linspace(0.18 * Z.max(), Z.max(), 6)
ax3.contourf(GX, GY, Z, levels=levels, cmap="Blues", alpha=0.45, zorder=0)

# light parameter-space axes
ax3.annotate("", xy=(1.95, -1.75), xytext=(-1.85, -1.75),
             arrowprops=dict(arrowstyle="-|>", color=AXISGREY, lw=1.3))
ax3.annotate("", xy=(-1.85, 1.95), xytext=(-1.85, -1.75),
             arrowprops=dict(arrowstyle="-|>", color=AXISGREY, lw=1.3))
ax3.text(2.02, -1.75, r"$w$", ha="left", va="center", fontsize=13, color=TEXT2)
ax3.text(-1.85, 2.06, r"$v$", ha="center", va="bottom", fontsize=13, color=TEXT2)
ax3.text(1.75, 1.72, r"$\mathbb{R}^{d+1}$", ha="right", va="top", fontsize=12,
         color=MUTED)

# a few Dirac "spikes" to evoke point masses
spike_idx = [3, 12, 27, 35]
for k in spike_idx:
    p = pts[k]
    ax3.plot([p[0], p[0]], [p[1], p[1] + 0.30], color=BLUE, lw=1.0,
             alpha=0.45, zorder=4)
    ax3.plot(p[0], p[1] + 0.30, marker="o", ms=2.6, color=BLUE, alpha=0.55,
             zorder=4)

# particles
ax3.scatter(pts[:, 0], pts[:, 1], s=42, color=BLUE, edgecolor="white",
            linewidth=0.8, zorder=5)
# highlighted particle i (with a soft halo + its own taller spike)
ax3.scatter([hl_pt[0]], [hl_pt[1]], s=360, color=RED, alpha=0.16, zorder=5)
ax3.plot([hl_pt[0], hl_pt[0]], [hl_pt[1], hl_pt[1] + 0.42], color=RED, lw=1.4,
         alpha=0.7, zorder=6)
ax3.plot(hl_pt[0], hl_pt[1] + 0.42, marker="o", ms=3.2, color=RED, zorder=6)
ax3.scatter([hl_pt[0]], [hl_pt[1]], s=120, color=HL_FILL, edgecolor=RED,
            linewidth=1.4, zorder=7)
ax3.text(hl_pt[0] + 0.16, hl_pt[1] - 0.02, r"$\theta_i$", ha="left",
         va="center", fontsize=12.5, color=RED, zorder=7)

ax3.text(0.05, 2.62, r"$\mu_N=\dfrac{1}{N}\sum_{i=1}^{N}\delta_{\theta_i}$",
         ha="center", va="center", fontsize=14, color=BLUE)

ax3.set_xlim(-2.6, 2.4)
ax3.set_ylim(-2.4, 3.05)


# =========================================================================
# cross-panel connecting arrows + labels (figure coords)
# =========================================================================
arr_y = 0.515
for gx_c, x_pad in ((G1, 0.028), (G2, 0.028)):
    fig.add_artist(FancyArrowPatch((gx_c - x_pad, arr_y), (gx_c + x_pad, arr_y),
                                   transform=fig.transFigure, arrowstyle="-|>",
                                   mutation_scale=20, lw=2.0, color="#444444"))

fig.text(G1, arr_y + 0.075, "stack the", ha="center", va="center",
         fontsize=11.5, color=TEXT)
fig.text(G1, arr_y + 0.030, "parameters", ha="center", va="center",
         fontsize=11.5, color=TEXT)
fig.text(G1, arr_y - 0.070, "concatenate\ninto $\\theta$", ha="center",
         va="center", fontsize=9.5, color=MUTED, style="italic")

fig.text(G2, arr_y + 0.075, "forget the", ha="center", va="center",
         fontsize=11.5, color=TEXT)
fig.text(G2, arr_y + 0.030, "ordering", ha="center", va="center",
         fontsize=11.5, color=TEXT)
fig.text(G2, arr_y - 0.070, "neurons are\nexchangeable", ha="center",
         va="center", fontsize=9.5, color=MUTED, style="italic")

# --- per-panel formula band + italic sub-labels (aligned across panels) ---
fig.text(PC1, 0.115, r"$f(x)=\sum_{i=1}^{N} v_i\,\sigma(w_i\cdot x)$",
         ha="center", va="center", fontsize=14, color=TEXT)
fig.text(PC1, 0.045, "the network", ha="center", va="center", fontsize=13,
         color=MUTED, style="italic")
fig.text(PC2, 0.045, "one long vector", ha="center", va="center", fontsize=13,
         color=MUTED, style="italic")
fig.text(PC3, 0.045, "a measure over neurons", ha="center", va="center",
         fontsize=13, color=MUTED, style="italic")

fig.text(0.5, 0.955, "The same two-layer network, three descriptions",
         ha="center", va="center", fontsize=14.5, color="#2a2a2a")

plt.savefig("assets/mean-field-dynamics/three-views.png", dpi=150,
            bbox_inches="tight", facecolor="white")
plt.close()
print("saved assets/mean-field-dynamics/three-views.png")
