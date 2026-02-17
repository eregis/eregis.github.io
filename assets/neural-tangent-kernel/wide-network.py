import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(12, 6))

# Layer configuration: (num_nodes, x_position, label)
# Hidden layer has many nodes to convey overparameterization
n_input = 3
n_hidden_shown = 16  # nodes actually drawn (8 on each side of ellipsis)
n_output = 1

layers_x = [0.0, 2.2, 4.4]
layer_labels = [r'Input $x$', r'Wide hidden layer ($m \gg n$)', 'Output']

node_radius = 0.13
node_color = '#4A90D9'
edge_color = '#BBBBBB'
spacing = 0.55

# Compute y positions for input and output layers (centered)
input_ys = np.linspace(-(n_input - 1) / 2 * spacing,
                       (n_input - 1) / 2 * spacing, n_input)
input_pos = [(layers_x[0], y) for y in input_ys]

output_pos = [(layers_x[2], 0.0)]

# Hidden layer: 8 nodes on top, ellipsis, 8 nodes on bottom
n_half = n_hidden_shown // 2
gap_for_ellipsis = 0.6  # extra vertical gap for the "..." region

# Total span: n_half nodes above gap, n_half nodes below gap
top_ys = np.linspace(gap_for_ellipsis / 2 + (n_half - 1) * spacing,
                     gap_for_ellipsis / 2, n_half)
bottom_ys = np.linspace(-gap_for_ellipsis / 2,
                        -gap_for_ellipsis / 2 - (n_half - 1) * spacing, n_half)

hidden_ys = np.concatenate([top_ys, bottom_ys])
hidden_pos = [(layers_x[1], y) for y in hidden_ys]

all_positions = [input_pos, hidden_pos, output_pos]

# Draw edges: input -> hidden
for (x1, y1) in input_pos:
    for (x2, y2) in hidden_pos:
        ax.plot([x1, x2], [y1, y2], color=edge_color, linewidth=0.5,
                zorder=1, alpha=0.6)

# Draw edges: hidden -> output
for (x1, y1) in hidden_pos:
    for (x2, y2) in output_pos:
        ax.plot([x1, x2], [y1, y2], color=edge_color, linewidth=0.5,
                zorder=1, alpha=0.6)

# Draw nodes for input layer
for (x, y) in input_pos:
    circle = plt.Circle((x, y), node_radius, color=node_color,
                         ec='#2C5F8A', linewidth=1.5, zorder=2)
    ax.add_patch(circle)

# Draw hidden layer nodes
for (x, y) in hidden_pos:
    circle = plt.Circle((x, y), node_radius, color=node_color,
                         ec='#2C5F8A', linewidth=1.5, zorder=2)
    ax.add_patch(circle)

# Draw ellipsis in the gap
ax.text(layers_x[1], 0.0, r'$\vdots$', ha='center', va='center',
        fontsize=20, color='#555555', zorder=3)

# Draw output node
for (x, y) in output_pos:
    circle = plt.Circle((x, y), node_radius, color=node_color,
                         ec='#2C5F8A', linewidth=1.5, zorder=2)
    ax.add_patch(circle)

# Draw layer labels below each layer
label_y_offsets = [-0.45, -0.45, -0.45]
for idx, (x_pos, label) in enumerate(zip(layers_x, layer_labels)):
    positions_for_layer = all_positions[idx]
    y_bottom = min(y for _, y in positions_for_layer) + label_y_offsets[idx]
    ax.text(x_pos, y_bottom, label, ha='center', va='top', fontsize=11,
            fontstyle='italic', color='#333333')

# Annotation: W, b between input and hidden
x_mid_1 = (layers_x[0] + layers_x[1]) / 2
y_top_1 = max(max(y for _, y in input_pos), max(y for _, y in hidden_pos))
ax.text(x_mid_1, y_top_1 + 0.35, r'$W, b$',
        ha='center', va='bottom', fontsize=12, color='#333333')

# Annotation: sigma above hidden layer
y_top_hidden = max(y for _, y in hidden_pos)
ax.text(layers_x[1], y_top_hidden + 0.35, r'$\sigma(\cdot)$',
        ha='center', va='bottom', fontsize=12, color='#B03A2E')

# Annotation: v between hidden and output
x_mid_2 = (layers_x[1] + layers_x[2]) / 2
y_top_2 = max(max(y for _, y in hidden_pos), max(y for _, y in output_pos))
ax.text(x_mid_2, y_top_2 + 0.35, r'$v$',
        ha='center', va='bottom', fontsize=12, color='#333333')

y_min = min(y for _, y in hidden_pos) - 1.0
y_max = max(y for _, y in hidden_pos) + 1.0
ax.set_xlim(-0.8, 5.2)
ax.set_ylim(y_min, y_max)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()
plt.savefig('assets/neural-tangent-kernel/wide-network.png',
            dpi=150, bbox_inches='tight', facecolor='white')
plt.show()
