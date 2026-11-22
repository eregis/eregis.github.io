import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

# Backward pass on the layer-level MLP graph of mlp-forward.py (N = 3 layers).
# Same node positions and colors as the forward figure; red marks only the backward
# arrows, each labeled by the local derivative it multiplies by, and each node is
# labeled by its sensitivity. As in diagonal-network-backward.py, the target y is dropped.
XLIM, YLIM = (-1.0, 14.9), (-1.6, 3.9)
fig, ax = plt.subplots(figsize=(XLIM[1] - XLIM[0], YLIM[1] - YLIM[0]))

r = 0.1           # neuron radius
GAP = 0.3         # vertical spacing between neurons in a column
PAD = 0.12        # box padding around a column

# --- palette: same node roles as mlp-forward.py -------------------------------
PARAM_FILL, PARAM_RIM = '#4A90D9', '#2C5F8A'   # parameters
DATA_FILL, DATA_RIM = '#DDDDDD', '#888888'     # data
COMP_FILL, COMP_RIM = '#F2C14E', '#A67C00'     # computed values
BWD_COLOR = '#B03A2E'                          # the backward pass itself
LABEL_COLOR = '#333333'
BOX_EDGE = '#999999'

DX = 2.15
order = ['x', 'z1', 'h1', 'z2', 'h2', 'f', 'L']
COL = {k: 0.2 + i * DX for i, k in enumerate(order)}
Y_SPINE, Y_SRC = 0.0, 1.25
SRC_SPREAD = 0.6

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


def side(key):
    """Half-width of a node: the box edge for columns, the circle for single neurons."""
    return r + PAD if SIZE[key] > 1 else r


def arrow(start, end):
    ax.annotate('', xy=end, xytext=start,
                arrowprops=dict(arrowstyle='-|>', color=BWD_COLOR, lw=2.0,
                                shrinkA=0, shrinkB=0), zorder=2)


def label(x, y, s, va, color=LABEL_COLOR, size=12, ha='center'):
    ax.text(x, y, s, ha=ha, va=va, fontsize=size, color=color, zorder=5)


# nodes keep their forward-pass colors; labels give each node's sensitivity
spine = [('x', DATA_FILL, DATA_RIM, r'$\partial L/\partial x$'),
         ('z1', COMP_FILL, COMP_RIM, r'$\partial L/\partial z^{(1)}$'),
         ('h1', COMP_FILL, COMP_RIM, r'$\partial L/\partial h^{(1)}$'),
         ('z2', COMP_FILL, COMP_RIM, r'$\partial L/\partial z^{(2)}$'),
         ('h2', COMP_FILL, COMP_RIM, r'$\partial L/\partial h^{(2)}$'),
         ('f', COMP_FILL, COMP_RIM, r'$\partial L/\partial f = f - y$'),
         ('L', COMP_FILL, COMP_RIM, r'$\partial L/\partial L = 1$')]
half = {}
for key, fill, rim, s in spine:
    half[key] = column(COL[key], Y_SPINE, SIZE[key], fill, rim)
    label(COL[key], Y_SPINE - half[key] - 0.15, s, 'top')

# every forward spine edge reversed, labeled by the local derivative it multiplies by;
# edges out of a pre-activation fan back in from every neuron, so they carry a sum
spine_edges = [('L', 'f', r'$\times\,(f - y)$'),
               ('f', 'h2', r'$\times\, w^{(3)}$'),
               ('h2', 'z2', r"$\times\, \sigma'(z_i^{(2)})$"),
               ('z2', 'h1', r'$\sum_i \times w_i^{(2)}$'),
               ('h1', 'z1', r"$\times\, \sigma'(z_i^{(1)})$"),
               ('z1', 'x', r'$\sum_i \times w_i^{(1)}$')]
for a, b, s in spine_edges:
    arrow((COL[a] - side(a) - 0.05, Y_SPINE), (COL[b] + side(b) + 0.05, Y_SPINE))
    label((COL[a] + COL[b]) / 2, Y_SPINE + 0.12, s, 'bottom', BWD_COLOR)

# side branches to each layer's parameters
for key, layer, prev in [('z1', 1, 'x'), ('z2', 2, r'h^{(1)}'), ('f', 3, r'h^{(2)}')]:
    n = SIZE[key]
    sub = '_i' if n > 1 else ''
    for dx, name, deriv, ha in [(-SRC_SPREAD, 'w', prev, 'right'), (SRC_SPREAD, 'b', '1', 'left')]:
        xs = COL[key] + dx
        extent = (n - 1) / 2 * GAP + (r + PAD if n > 1 else r)
        y_c = Y_SRC + extent
        column(xs, y_c, n, PARAM_FILL, PARAM_RIM)
        label(xs, y_c + extent + 0.12, rf'$\partial L/\partial {name}{sub}^{{({layer})}}$', 'bottom')
        start = (COL[key] + (dx * 0.12), Y_SPINE + half[key] + 0.05)
        end = (xs, Y_SRC - 0.05)
        arrow(start, end)
        mx, my = start[0] + 0.4 * (end[0] - start[0]), start[1] + 0.4 * (end[1] - start[1])
        label(mx + (-0.2 if ha == 'right' else 0.2), my, rf'$\times\, {deriv}$',
              'center', BWD_COLOR, ha=ha)

ax.set_xlim(*XLIM)
ax.set_ylim(*YLIM)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()
plt.savefig('assets/backpropagation-chain-rule/mlp-backward.png',
            dpi=150, bbox_inches='tight', facecolor='white')
