"""
Standalone diagram of the two-layer network, for the top of "The Mean-Field
Theory of Two-Layer Neural Networks" -- placed right after the defining
equation

    f(x; theta) = sum_{i=1}^{N} v_i sigma(w_i . x)

and the numbered list of what each neuron does: (1) project x onto a
direction w_i, (2) apply a scalar nonlinearity sigma, (3) contribute to the
output with weight v_i. This is a single-panel cousin of panel 1 ("the
network") in three-views.py -- same palette and the same fully-connected,
ellipsis-in-a-slot geometry, just standing alone rather than sitting beside
the other two panels, and stretched wide (rather than tall) so it sits well
in a blog column. The input layer carries its own dedicated ellipsis slot
(mirroring the hidden layer's), and the three bottom captions are spaced
one per column instead of running together.

Colors: primary blue (NODE_FILL/NODE_EDGE) for the input, hidden, and output
nodes and their edges; the warm accent (RED/HL_FILL) singles out one
representative neuron i -- its incoming fan (the projection w_i . x, labeled
w_i), the node itself (fill color plus a small sigma marking the
nonlinearity -- sigma appears exactly once, inside that node), and its
outgoing edge (labeled v_i, the output weight). The numbered list right
above the figure in the post already spells out the three steps, so the
diagram itself stays close to panel 1's sparer register rather than
re-annotating each step in prose.

Output: assets/mean-field-dynamics/network.png
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# --- palette (shared with three-views.py / timeline.py) ------------------
BLUE      = "#2166ac"   # primary
NODE_FILL = "#4A90D9"   # blue node fill
NODE_EDGE = "#2C5F8A"   # blue node edge
RED       = "#b2182b"   # accent: sigma + highlighted-neuron outline
HL_FILL   = "#d6604d"   # highlighted node / edge fill
DIVIDER   = "#BBBBBB"   # edges / dividers
AXISGREY  = "#8a8a8a"
TEXT      = "#333333"
TEXT2     = "#555555"
MUTED     = "#6b6b6b"

fig, ax = plt.subplots(figsize=(7.6, 4.8))
fig.subplots_adjust(left=0.03, right=0.98, top=0.97, bottom=0.14)
ax.set_aspect("equal")
ax.axis("off")

x_in, x_hid, x_out = 0.0, 2.3, 4.6
r = 0.15

# input column: 3 real nodes + a dedicated ellipsis slot, same spacing idiom
# as the hidden column (mirrors panel 1's hid_y pattern rather than jamming
# the dots against a neighboring node).
in_y = np.array([0.975, 0.325, -0.325, -0.975])
in_is_node = np.array([True, True, False, True])
in_labels = [r"$x_1$", r"$x_2$", None, r"$x_d$"]

# hidden column: same relative layout as panel 1 of three-views.py, scaled
# down slightly to keep the whole figure compact.
hid_y = np.array([1.3, 0.65, 0.0, -0.65, -1.3])   # slot 3 (idx 3) is the ellipsis
hid_is_node = np.array([True, True, True, False, True])
HL = 1                                             # highlighted hidden slot -> neuron i
hl_y = hid_y[HL]

in_node_y = in_y[in_is_node]
hid_node_y = hid_y[hid_is_node]

# edges input -> hidden (grey; the highlighted neuron's own edges in red)
for yi in in_node_y:
    for j, yh in enumerate(hid_y):
        if not hid_is_node[j]:
            continue
        if j == HL:
            ax.plot([x_in, x_hid], [yi, yh], color=HL_FILL, lw=1.8,
                    alpha=0.9, zorder=1)
        else:
            ax.plot([x_in, x_hid], [yi, yh], color=DIVIDER, lw=0.8, zorder=1)

# edges hidden -> output
for j, yh in enumerate(hid_y):
    if not hid_is_node[j]:
        continue
    if j == HL:
        ax.plot([x_hid, x_out], [yh, 0.0], color=HL_FILL, lw=1.8,
                alpha=0.9, zorder=1)
    else:
        ax.plot([x_hid, x_out], [yh, 0.0], color=DIVIDER, lw=0.8, zorder=1)

# input nodes (+ vertical ellipsis in its own slot)
for j, yi in enumerate(in_y):
    if not in_is_node[j]:
        ax.text(x_in, yi, r"$\vdots$", ha="center", va="center",
                fontsize=14, color=AXISGREY, zorder=3)
        continue
    ax.add_patch(Circle((x_in, yi), r, facecolor=NODE_FILL, edgecolor=NODE_EDGE,
                        linewidth=1.5, zorder=3))
    ax.text(x_in - 0.30, yi, in_labels[j], ha="right", va="center",
            fontsize=12, color=TEXT)

# hidden nodes (+ vertical ellipsis in the empty slot)
for j, yh in enumerate(hid_y):
    if not hid_is_node[j]:
        ax.text(x_hid, yh, r"$\vdots$", ha="center", va="center",
                fontsize=15, color=AXISGREY, zorder=3)
        continue
    if j == HL:
        ax.add_patch(Circle((x_hid, yh), r, facecolor=HL_FILL, edgecolor=RED,
                            linewidth=1.8, zorder=4))
        ax.text(x_hid, yh, r"$\sigma$", ha="center", va="center", fontsize=10,
                color="white", zorder=5)
    else:
        ax.add_patch(Circle((x_hid, yh), r, facecolor=NODE_FILL,
                            edgecolor=NODE_EDGE, linewidth=1.5, zorder=3))

# output node
ax.add_patch(Circle((x_out, 0.0), r, facecolor=NODE_FILL, edgecolor=NODE_EDGE,
                    linewidth=1.5, zorder=3))

# --- labels, kept to panel 1's sparer register --------------------------
ax.text(0.95, 1.15, r"$w_i$", ha="center", va="center", fontsize=13,
        color=RED)
ax.text(3.45, 0.62, r"$v_i$", ha="center", va="center", fontsize=13,
        color=RED)
ax.text(x_out + 0.34, 0.0, r"$f(x)$", ha="left", va="center", fontsize=14,
        color=TEXT)

# --- bottom register: one caption per column, same baseline ---------------
y_cap = -1.65
ax.text(x_in, y_cap, r"input $x\in\mathbb{R}^{d}$", ha="center", va="top",
        fontsize=12, color=TEXT2, style="italic")
ax.text(x_hid, y_cap, r"$N$ neurons", ha="center", va="top",
        fontsize=12, color=TEXT2, style="italic")
ax.text(x_out, y_cap, r"output $f(x)$", ha="center", va="top",
        fontsize=12, color=TEXT2, style="italic")

ax.set_xlim(-1.0, 5.35)
ax.set_ylim(-2.05, 1.65)

fig.text(0.5, 0.05, r"$f(x)=\sum_{i=1}^{N} v_i\,\sigma(w_i\cdot x)$",
         ha="center", va="center", fontsize=14.5, color=TEXT)

plt.savefig("assets/mean-field-dynamics/network.png", dpi=150,
            bbox_inches="tight", facecolor="white")
plt.close()
print("saved assets/mean-field-dynamics/network.png")
