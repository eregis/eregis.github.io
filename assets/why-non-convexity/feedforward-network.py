import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(12, 6))

# Layer configuration: (num_nodes, x_position, label)
layers = [
    (3, 0.0, 'Input'),
    (5, 1.2, 'Learned\nfeatures'),
    (4, 2.4, 'Learned\nfeatures'),
    (4, 3.6, 'Learned\nfeatures'),
    (3, 4.8, 'Learned\nfeatures'),
    (1, 6.0, 'Linear\ncombination'),
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

# Draw activation function annotations between layers (not after last hidden)
for i in range(len(layers) - 2):
    x_mid = (layers[i][1] + layers[i + 1][1]) / 2
    y_top = max(max(y for _, y in positions[i]), max(y for _, y in positions[i + 1]))
    ax.text(x_mid, y_top + 0.35, r'$\sigma(\cdot)$',
            ha='center', va='bottom', fontsize=12, color='#B03A2E')

ax.set_xlim(-0.6, 6.6)
ax.set_ylim(-2.0, 1.8)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()
plt.savefig('assets/why-non-convexity/feedforward-network.png',
            dpi=150, bbox_inches='tight', facecolor='white')
plt.show()
