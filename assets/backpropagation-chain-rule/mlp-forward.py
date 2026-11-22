import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import FancyBboxPatch

# Layer-level forward graph of an MLP with N = 3 layers (two hidden + output).
# Each vector-valued node is drawn as a boxed column of circles, one per neuron.
# One inch per data unit, matching the diagonal-network figures.
XLIM, YLIM = (-0.6, 14.9), (-2.2, 3.7)
fig, ax = plt.subplots(figsize=(XLIM[1] - XLIM[0], YLIM[1] - YLIM[0]))

r = 0.1           # neuron radius
GAP = 0.3         # vertical spacing between neurons in a column
PAD = 0.12        # box padding around a column

# --- palette: nodes are colored by role, identically in every graph figure ---
PARAM_FILL, PARAM_RIM = '#4A90D9', '#2C5F8A'   # parameters: what training adjusts
DATA_FILL, DATA_RIM = '#DDDDDD', '#888888'     # data: fixed inputs x and target y
COMP_FILL, COMP_RIM = '#F2C14E', '#A67C00'     # computed: values the forward pass produces
FWD_COLOR = '#444444'
LABEL_COLOR = '#333333'
BOX_EDGE = '#999999'

DX = 2.15
order = ['x', 'z1', 'h1', 'z2', 'h2', 'f', 'L']
COL = {k: 0.2 + i * DX for i, k in enumerate(order)}
Y_SPINE, Y_SRC = 0.0, 1.25
SRC_SPREAD = 0.6

# number of neurons in each layer, matching mlp-architecture.png: input 3, hidden 5, hidden 4, output 1
SIZE = {'x': 3, 'z1': 5, 'h1': 5, 'z2': 4, 'h2': 4, 'f': 1, 'L': 1}


def column(x, y, n, fill, rim):
    """Draw n neurons stacked around (x, y); return the half-height of the drawn group."""
    half = (n - 1) / 2 * GAP
    for k in range(n):
        ax.add_patch(plt.Circle((x, y - half + k * GAP), r, color=fill, ec=rim,
                                linewidth=1.3, zorder=4))
    if n > 1:
        ax.add_patch(FancyBboxPatch((x - r - PAD, y - half - r - PAD),
                                    2 * (r + PAD), 2 * (half + r + PAD),
                                    boxstyle='round,pad=0,rounding_size=0.12',
                                    fc='none', ec=BOX_EDGE, lw=1.0, zorder=3))
        return half + r + PAD
    return r


def arrow(start, end):
    ax.annotate('', xy=end, xytext=start,
                arrowprops=dict(arrowstyle='-|>', color=FWD_COLOR, lw=1.8,
                                shrinkA=0, shrinkB=0), zorder=2)


def label(x, y, s, va):
    ax.text(x, y, s, ha='center', va=va, fontsize=13, color=LABEL_COLOR, zorder=5)


spine = [('x', DATA_FILL, DATA_RIM, r'$x$'),
         ('z1', COMP_FILL, COMP_RIM, r'$z^{(1)}$'),
         ('h1', COMP_FILL, COMP_RIM, r'$h^{(1)} = \sigma(z^{(1)})$'),
         ('z2', COMP_FILL, COMP_RIM, r'$z^{(2)}$'),
         ('h2', COMP_FILL, COMP_RIM, r'$h^{(2)} = \sigma(z^{(2)})$'),
         ('f', COMP_FILL, COMP_RIM, r'$f = z^{(3)}$'),
         ('L', COMP_FILL, COMP_RIM, r'$L = \frac{1}{2}(f - y)^2$')]

# each pre-activation has two parameter parents: one weight vector and one bias per neuron
sources = []
for key, layer in [('z1', 1), ('z2', 2), ('f', 3)]:
    n = SIZE[key]
    w_lab = rf'$w_i^{{({layer})}}$' if n > 1 else rf'$w^{{({layer})}}$'
    b_lab = rf'$b_i^{{({layer})}}$' if n > 1 else rf'$b^{{({layer})}}$'
    sources.append((COL[key] - SRC_SPREAD, key, n, PARAM_FILL, PARAM_RIM, w_lab))
    sources.append((COL[key] + SRC_SPREAD, key, n, PARAM_FILL, PARAM_RIM, b_lab))
sources.append((COL['L'], 'L', 1, DATA_FILL, DATA_RIM, r'$y$'))

half = {}
for key, fill, rim, s in spine:
    half[key] = column(COL[key], Y_SPINE, SIZE[key], fill, rim)
    label(COL[key], Y_SPINE - half[key] - 0.15, s, 'top')

def side(key):
    """Half-width of a node: the box edge for columns, the circle for single neurons."""
    return r + PAD if SIZE[key] > 1 else r


for a, b in zip(order[:-1], order[1:]):
    arrow((COL[a] + side(a) + 0.05, Y_SPINE), (COL[b] - side(b) - 0.05, Y_SPINE))

for xs, key, n, fill, rim, s in sources:
    # bottom-align the parameter columns so their arrows all start at the same height
    extent = (n - 1) / 2 * GAP + (r + PAD if n > 1 else r)
    y_c = Y_SRC + extent
    column(xs, y_c, n, fill, rim)
    label(xs, y_c + extent + 0.12, s, 'bottom')
    arrow((xs, Y_SRC - 0.05), (COL[key], Y_SPINE + half[key] + 0.05))

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
plt.savefig('assets/backpropagation-chain-rule/mlp-forward.png',
            dpi=150, bbox_inches='tight', facecolor='white')
