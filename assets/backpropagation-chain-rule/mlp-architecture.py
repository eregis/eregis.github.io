import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(12, 6))

# --- palette: nodes are colored by role, as in the computational-graph figures ---
DATA_FILL, DATA_RIM = '#DDDDDD', '#888888'     # data: the input x
COMP_FILL, COMP_RIM = '#F2C14E', '#A67C00'     # computed: neurons the forward pass evaluates
LABEL_COLOR = '#333333'

# Layer configuration: (num_nodes, x_position, label, fill, rim)
layers = [
    (3, 0.0, r'Input  $h^{(0)} = x$', DATA_FILL, DATA_RIM),
    (5, 1.8, r'Hidden  $h^{(1)}$', COMP_FILL, COMP_RIM),
    (4, 3.6, r'Hidden  $h^{(2)}$', COMP_FILL, COMP_RIM),
    (1, 5.4, r'Output  $f$', COMP_FILL, COMP_RIM),
]

node_radius = 0.13
edge_color = '#BBBBBB'
spacing = 0.55

# Compute y positions for each layer (centered vertically)
positions = []
for n_nodes, x, *_ in layers:
    ys = np.linspace(-(n_nodes - 1) / 2 * spacing, (n_nodes - 1) / 2 * spacing, n_nodes)
    positions.append([(x, y) for y in ys])

# Draw edges between consecutive layers
for i in range(len(layers) - 1):
    for (x1, y1) in positions[i]:
        for (x2, y2) in positions[i + 1]:
            ax.plot([x1, x2], [y1, y2], color=edge_color, linewidth=0.8, zorder=1)

# Draw nodes
for layer_pos, (*_, fill, rim) in zip(positions, layers):
    for (x, y) in layer_pos:
        ax.add_patch(plt.Circle((x, y), node_radius, color=fill,
                                ec=rim, linewidth=1.5, zorder=2))

# Draw layer labels below each layer
for idx, (n_nodes, x, label, *_) in enumerate(layers):
    y_bottom = min(y for _, y in positions[idx]) - 0.45
    ax.text(x, y_bottom, label, ha='center', va='top', fontsize=11,
            fontstyle='italic', color=LABEL_COLOR)


def top(idx):
    return max(y for _, y in positions[idx])


# Parameters of each layer, written above the connections that feed it
for idx, s in [(1, r'$w_i^{(1)}, b_i^{(1)}$'),
               (2, r'$w_i^{(2)}, b_i^{(2)}$'),
               (3, r'$w^{(3)}, b^{(3)}$')]:
    x_mid = (layers[idx - 1][1] + layers[idx][1]) / 2
    ax.text(x_mid, max(top(idx - 1), top(idx)) + 0.35, s,
            ha='center', va='bottom', fontsize=12, color=LABEL_COLOR)

# Activation function above each hidden layer
for idx in (1, 2):
    ax.text(layers[idx][1], top(idx) + 0.35, r'$\sigma(\cdot)$',
            ha='center', va='bottom', fontsize=12, color=LABEL_COLOR)

ax.set_xlim(-0.9, 6.3)
ax.set_ylim(-2.1, 1.85)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()
plt.savefig('assets/backpropagation-chain-rule/mlp-architecture.png',
            dpi=150, bbox_inches='tight', facecolor='white')
