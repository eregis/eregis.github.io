import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(12, 6))

# Layer configuration: (num_nodes, x_position, label)
layers = [
    (3, 0.0, r'Input  $h^{(0)} = x$'),
    (5, 1.8, r'Hidden  $h^{(1)}$'),
    (4, 3.6, r'Hidden  $h^{(2)}$'),
    (1, 5.4, r'Output  $f(x;\theta)$'),
]

node_radius = 0.13
node_color = '#4A90D9'
edge_color = '#BBBBBB'
spacing = 0.55

# Compute y positions for each layer (centered vertically)
positions = []
for n_nodes, x, label in layers:
    ys = np.linspace(-(n_nodes - 1) / 2 * spacing, (n_nodes - 1) / 2 * spacing, n_nodes)
    positions.append([(x, y) for y in ys])

# Draw edges between consecutive layers
for i in range(len(layers) - 1):
    for (x1, y1) in positions[i]:
        for (x2, y2) in positions[i + 1]:
            ax.plot([x1, x2], [y1, y2], color=edge_color, linewidth=0.8, zorder=1)

# Draw nodes
for layer_pos in positions:
    for (x, y) in layer_pos:
        circle = plt.Circle((x, y), node_radius, color=node_color,
                             ec='#2C5F8A', linewidth=1.5, zorder=2)
        ax.add_patch(circle)

# Draw layer labels below each layer
for idx, (n_nodes, x, label) in enumerate(layers):
    y_bottom = min(y for _, y in positions[idx]) - 0.45
    ax.text(x, y_bottom, label, ha='center', va='top', fontsize=11,
            fontstyle='italic', color='#333333')

# Annotation: W^(1), b^(1) between input and h^(1)
x_mid_1 = (layers[0][1] + layers[1][1]) / 2
y_top_1 = max(max(y for _, y in positions[0]), max(y for _, y in positions[1]))
ax.text(x_mid_1, y_top_1 + 0.35, r'$W^{(1)}, b^{(1)}$',
        ha='center', va='bottom', fontsize=12, color='#333333')

# Annotation: sigma above h^(1)
y_top_h1 = max(y for _, y in positions[1])
ax.text(layers[1][1], y_top_h1 + 0.35, r'$\sigma(\cdot)$',
        ha='center', va='bottom', fontsize=12, color='#B03A2E')

# Annotation: W^(2), b^(2) between h^(1) and h^(2)
x_mid_2 = (layers[1][1] + layers[2][1]) / 2
y_top_2 = max(max(y for _, y in positions[1]), max(y for _, y in positions[2]))
ax.text(x_mid_2, y_top_2 + 0.35, r'$W^{(2)}, b^{(2)}$',
        ha='center', va='bottom', fontsize=12, color='#333333')

# Annotation: sigma above h^(2)
y_top_h2 = max(y for _, y in positions[2])
ax.text(layers[2][1], y_top_h2 + 0.35, r'$\sigma(\cdot)$',
        ha='center', va='bottom', fontsize=12, color='#B03A2E')

# Annotation: v (readout) between h^(2) and output
x_mid_3 = (layers[2][1] + layers[3][1]) / 2
y_top_3 = max(max(y for _, y in positions[2]), max(y for _, y in positions[3]))
ax.text(x_mid_3, y_top_3 + 0.35, r'$v$',
        ha='center', va='bottom', fontsize=12, color='#333333')

ax.set_xlim(-0.9, 6.3)
ax.set_ylim(-2.1, 1.85)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()
plt.savefig('assets/backpropagation-chain-rule/mlp-architecture.png',
            dpi=150, bbox_inches='tight', facecolor='white')
