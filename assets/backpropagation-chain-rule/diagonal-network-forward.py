import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# one inch per data unit, matching computational-graph.png
XLIM, YLIM = (-0.8, 9.0), (-1.5, 1.9)
fig, ax = plt.subplots(figsize=(XLIM[1] - XLIM[0], YLIM[1] - YLIM[0]))

node_radius = 0.13

# --- palette: nodes are colored by role, identically in every graph figure ---
PARAM_FILL, PARAM_RIM = '#4A90D9', '#2C5F8A'   # parameters: what training adjusts
DATA_FILL, DATA_RIM = '#DDDDDD', '#888888'     # data: fixed inputs x and target y
COMP_FILL, COMP_RIM = '#F2C14E', '#A67C00'     # computed: values the forward pass produces
FWD_COLOR = '#444444'
LABEL_COLOR = '#333333'

COL = {'x': 0.0, 'h': 2.7, 'f': 5.4, 'L': 8.1}
Y_SPINE, Y_SRC = 0.0, 1.25
LABEL_OFFSET = 0.3


def node(x, y, fill, rim):
    ax.add_patch(plt.Circle((x, y), node_radius, color=fill, ec=rim,
                            linewidth=1.5, zorder=4))


def arrow(start, end):
    ax.annotate('', xy=end, xytext=start,
                arrowprops=dict(arrowstyle='-|>', color=FWD_COLOR, lw=1.8,
                                shrinkA=14, shrinkB=14), zorder=2)


def label(x, y, s, va):
    ax.text(x, y, s, ha='center', va=va, fontsize=13, color=LABEL_COLOR, zorder=5)


spine = [('x', DATA_FILL, DATA_RIM, r'$x$'),
         ('h', COMP_FILL, COMP_RIM, r'$h = w_1 x$'),
         ('f', COMP_FILL, COMP_RIM, r'$f = w_2 h$'),
         ('L', COMP_FILL, COMP_RIM, r'$L = \frac{1}{2}(f - y)^2$')]
sources = [('h', PARAM_FILL, PARAM_RIM, r'$w_1$'),
           ('f', PARAM_FILL, PARAM_RIM, r'$w_2$'),
           ('L', DATA_FILL, DATA_RIM, r'$y$')]

for a, b in [('x', 'h'), ('h', 'f'), ('f', 'L')]:
    arrow((COL[a], Y_SPINE), (COL[b], Y_SPINE))
for key, *_ in sources:
    arrow((COL[key], Y_SRC), (COL[key], Y_SPINE))

for key, fill, rim, s in spine:
    node(COL[key], Y_SPINE, fill, rim)
    label(COL[key], Y_SPINE - LABEL_OFFSET, s, 'top')
for key, fill, rim, s in sources:
    node(COL[key], Y_SRC, fill, rim)
    label(COL[key], Y_SRC + LABEL_OFFSET, s, 'bottom')

legend = [Line2D([], [], marker='o', ls='', markersize=11, markerfacecolor=fill,
                 markeredgecolor=rim, markeredgewidth=1.5, label=name)
          for fill, rim, name in [(PARAM_FILL, PARAM_RIM, 'parameter'),
                                  (DATA_FILL, DATA_RIM, 'data'),
                                  (COMP_FILL, COMP_RIM, 'computed')]]
ax.legend(handles=legend, loc='lower center', bbox_to_anchor=(0.5, 0.0), ncol=3,
          frameon=False, fontsize=12, handletextpad=0.3, columnspacing=1.8)

ax.set_xlim(*XLIM)
ax.set_ylim(*YLIM)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()
plt.savefig('assets/backpropagation-chain-rule/diagonal-network-forward.png',
            dpi=150, bbox_inches='tight', facecolor='white')
