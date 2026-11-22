import matplotlib.pyplot as plt

# one inch per data unit, matching computational-graph.png
XLIM, YLIM = (-1.3, 9.2), (-1.0, 2.0)
fig, ax = plt.subplots(figsize=(XLIM[1] - XLIM[0], YLIM[1] - YLIM[0]))

node_radius = 0.13

# --- palette: same node roles as diagonal-network-forward.py ------------------
PARAM_FILL, PARAM_RIM = '#4A90D9', '#2C5F8A'   # parameters
DATA_FILL, DATA_RIM = '#DDDDDD', '#888888'     # data
COMP_FILL, COMP_RIM = '#F2C14E', '#A67C00'     # computed values
BWD_COLOR = '#B03A2E'                          # the backward pass itself
LABEL_COLOR = '#333333'

# same node positions as the forward figure; the target y is not needed here
COL = {'x': 0.0, 'h': 2.7, 'f': 5.4, 'L': 8.1}
Y_SPINE, Y_SRC = 0.0, 1.25
LABEL_OFFSET = 0.3


def node(x, y, fill, rim):
    ax.add_patch(plt.Circle((x, y), node_radius, color=fill, ec=rim,
                            linewidth=1.5, zorder=4))


def arrow(start, end):
    ax.annotate('', xy=end, xytext=start,
                arrowprops=dict(arrowstyle='-|>', color=BWD_COLOR, lw=2.0,
                                shrinkA=14, shrinkB=14), zorder=2)


def label(x, y, s, va, color=LABEL_COLOR, size=12, ha='center'):
    ax.text(x, y, s, ha=ha, va=va, fontsize=size, color=color, zorder=5)


# every forward edge reversed, labeled by the local derivative it multiplies by
for a, b, s in [('L', 'f', r'$\times\,(f - y)$'),
                ('f', 'h', r'$\times\, w_2$'),
                ('h', 'x', r'$\times\, w_1$')]:
    arrow((COL[a], Y_SPINE), (COL[b], Y_SPINE))
    label((COL[a] + COL[b]) / 2, Y_SPINE + 0.15, s, 'bottom', BWD_COLOR)
for key, s in [('h', r'$\times\, x$'), ('f', r'$\times\, h$')]:
    arrow((COL[key], Y_SPINE), (COL[key], Y_SRC))
    label(COL[key] + 0.2, (Y_SPINE + Y_SRC) / 2, s, 'center', BWD_COLOR, ha='left')

# nodes keep their forward-pass colors; labels give each node's sensitivity
for key, fill, rim, s in [
        ('x', DATA_FILL, DATA_RIM, r'$\partial L/\partial x = (f-y)\,w_2 w_1$'),
        ('h', COMP_FILL, COMP_RIM, r'$\partial L/\partial h = (f-y)\,w_2$'),
        ('f', COMP_FILL, COMP_RIM, r'$\partial L/\partial f = f - y$'),
        ('L', COMP_FILL, COMP_RIM, r'$\partial L/\partial L = 1$')]:
    node(COL[key], Y_SPINE, fill, rim)
    label(COL[key], Y_SPINE - LABEL_OFFSET, s, 'top')
for key, s in [('h', r'$\partial L/\partial w_1 = (f-y)\,w_2 x$'),
               ('f', r'$\partial L/\partial w_2 = (f-y)\,h$')]:
    node(COL[key], Y_SRC, PARAM_FILL, PARAM_RIM)
    label(COL[key], Y_SRC + LABEL_OFFSET, s, 'bottom')

ax.set_xlim(*XLIM)
ax.set_ylim(*YLIM)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()
plt.savefig('assets/backpropagation-chain-rule/diagonal-network-backward.png',
            dpi=150, bbox_inches='tight', facecolor='white')
