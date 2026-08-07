import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(12, 4.5))

node_radius = 0.13

# --- palette --------------------------------------------------------------
ACT_FILL, ACT_RIM = '#4A90D9', '#2C5F8A'       # x, h^(1), h^(2): activation-type
PRE_FILL, PRE_RIM = '#4FA8A6', '#2D6E6C'       # z^(1), z^(2): pre-activation
NEUT_FILL, NEUT_RIM = '#DDDDDD', '#888888'     # f, L: neutral
DELTA_FILL, DELTA_RIM = '#E8AFA8', '#B03A2E'   # delta^(1), delta^(2): backward pass
FWD_COLOR = '#444444'
BWD_COLOR = '#B03A2E'
SIGMA_COLOR = '#B03A2E'
LABEL_COLOR = '#333333'
DASH_COLOR = '#AAAAAA'

OP_OFFSET = 0.32       # forward operation labels, above the top row
NODE_LABEL_OFFSET = 0.62   # node symbol labels, further above the top row
DELTA_LABEL_OFFSET = 0.45  # delta symbol labels, below the bottom row
RECURSION_OFFSET = 0.32    # recursion labels, above the bottom row

# --- top row (forward pass), y = 0 -----------------------------------------
Y_TOP = 0.0
top_order = ['x', 'z1', 'h1', 'z2', 'h2', 'f', 'L']
top_x = {'x': 0.0, 'z1': 1.5, 'h1': 3.0, 'z2': 4.5, 'h2': 6.0, 'f': 7.5, 'L': 9.0}
top_label = {
    'x': r'$x$', 'z1': r'$z^{(1)}$', 'h1': r'$h^{(1)}$', 'z2': r'$z^{(2)}$',
    'h2': r'$h^{(2)}$', 'f': r'$f$', 'L': r'$L$',
}
top_style = {
    'x': (ACT_FILL, ACT_RIM), 'z1': (PRE_FILL, PRE_RIM), 'h1': (ACT_FILL, ACT_RIM),
    'z2': (PRE_FILL, PRE_RIM), 'h2': (ACT_FILL, ACT_RIM),
    'f': (NEUT_FILL, NEUT_RIM), 'L': (NEUT_FILL, NEUT_RIM),
}

# --- bottom row (backward pass), y = Y_BOT ----------------------------------
Y_BOT = -2.2
bot_order = ['d2', 'd1']
bot_x = {'d2': top_x['z2'], 'd1': top_x['z1']}
bot_label = {'d2': r'$\delta^{(2)}$', 'd1': r'$\delta^{(1)}$'}

# --- forward edges: (source, target, label, label color) -------------------
fwd_edges = [
    ('x',  'z1', r'$W^{(1)}, b^{(1)}$', LABEL_COLOR),
    ('z1', 'h1', r'$\sigma$',           SIGMA_COLOR),
    ('h1', 'z2', r'$W^{(2)}, b^{(2)}$', LABEL_COLOR),
    ('z2', 'h2', r'$\sigma$',           SIGMA_COLOR),
    ('h2', 'f',  r'$v$',                LABEL_COLOR),
    ('f',  'L',  'loss',                LABEL_COLOR),
]

for src, dst, label, color in fwd_edges:
    x1, x2 = top_x[src], top_x[dst]
    ax.annotate('', xy=(x2, Y_TOP), xytext=(x1, Y_TOP),
                arrowprops=dict(arrowstyle='-|>', color=FWD_COLOR, lw=1.8,
                                 shrinkA=14, shrinkB=14), zorder=2)
    ax.text((x1 + x2) / 2, Y_TOP + OP_OFFSET, label, ha='center', va='bottom',
            fontsize=12, color=color)

# dashed connectors: the backward pass reuses stored forward values
for key in ['z1', 'z2']:
    x = top_x[key]
    ax.plot([x, x], [Y_TOP - node_radius - 0.05, Y_BOT + node_radius + 0.05],
            linestyle=(0, (4, 3)), color=DASH_COLOR, linewidth=1.1, zorder=1)

# backward arrow: the loss seeds the recursion, entering at delta^(2)
ax.annotate('', xy=(bot_x['d2'], Y_BOT), xytext=(top_x['L'], Y_TOP),
            arrowprops=dict(arrowstyle='-|>', color=BWD_COLOR, lw=2.0,
                             shrinkA=14, shrinkB=14), zorder=3)

# backward arrow: delta^(2) -> delta^(1), the layer-error recursion
ax.annotate('', xy=(bot_x['d1'], Y_BOT), xytext=(bot_x['d2'], Y_BOT),
            arrowprops=dict(arrowstyle='-|>', color=BWD_COLOR, lw=2.0,
                             shrinkA=14, shrinkB=14), zorder=3)

x_near_d2 = bot_x['d2'] - 0.75
x_near_d1 = bot_x['d1'] + 0.75
ax.text(x_near_d2, Y_BOT + RECURSION_OFFSET, r'$(W^{(2)})^\top$',
        ha='center', va='bottom', fontsize=12, color=BWD_COLOR)
ax.text(x_near_d1, Y_BOT + RECURSION_OFFSET, r'$\odot\,\sigma^\prime$',
        ha='center', va='bottom', fontsize=12, color=BWD_COLOR)

# --- draw nodes (top row) ---------------------------------------------------
for key in top_order:
    x = top_x[key]
    fill, rim = top_style[key]
    circle = plt.Circle((x, Y_TOP), node_radius, color=fill, ec=rim,
                         linewidth=1.5, zorder=4)
    ax.add_patch(circle)
    ax.text(x, Y_TOP + NODE_LABEL_OFFSET, top_label[key], ha='center', va='bottom',
            fontsize=13, color=LABEL_COLOR, zorder=5)

# --- draw nodes (bottom row) -------------------------------------------------
for key in bot_order:
    x = bot_x[key]
    circle = plt.Circle((x, Y_BOT), node_radius, color=DELTA_FILL, ec=DELTA_RIM,
                         linewidth=1.5, zorder=4)
    ax.add_patch(circle)
    ax.text(x, Y_BOT - DELTA_LABEL_OFFSET, bot_label[key], ha='center', va='top',
            fontsize=13, color=LABEL_COLOR, zorder=5)

ax.set_xlim(-0.8, 9.8)
ax.set_ylim(-3.2, 1.2)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()
plt.savefig('assets/backpropagation-chain-rule/computational-graph.png',
            dpi=150, bbox_inches='tight', facecolor='white')
