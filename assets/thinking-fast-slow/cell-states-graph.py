import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from scipy.spatial.distance import pdist, squareform

# Set random seed for reproducibility
np.random.seed(42)

# Define cell types and their positions
cell_types = {
    'HSC':  (0.5, 0.5),
    'CMP':  (1.5, 0.8),
    'CLP':  (1.5, 0.2),
    'GMP':  (2.0, 0.7),
    'BCell': (2.0, 0.1),
}

colors = {
    'HSC':  '#FFB6C1',
    'CMP':  '#FF6B6B',
    'CLP':  '#98FB98',
    'GMP':  '#87CEFA',
    'BCell': '#9370DB',
}

# Generate points and store their cell type
n_points = 5
all_points = []
point_colors = []
point_labels = []

for cell_type, (x, y) in cell_types.items():
    for _ in range(n_points):
        px = np.random.normal(x, 0.05)
        py = np.random.normal(y, 0.05)
        all_points.append([px, py])
        point_colors.append(colors[cell_type])
        point_labels.append(cell_type)

all_points = np.array(all_points)

# Create a graph
G = nx.Graph()

# Add nodes
for i, (point, label) in enumerate(zip(all_points, point_labels)):
    G.add_node(i, pos=point, color=point_colors[i], label=label)

# Connect points within each cell type cluster
# Calculate pairwise distances
distances = squareform(pdist(all_points))

# Connect points that are close and of the same type
threshold = 0.15  # Adjust this to change connectivity density
for i in range(len(all_points)):
    for j in range(i+1, len(all_points)):
        if (distances[i,j] < threshold and 
            point_labels[i] == point_labels[j]):
            G.add_edge(i, j)

# Create the plot
plt.figure(figsize=(10, 8))

# Draw edges first
pos = nx.get_node_attributes(G, 'pos')
nx.draw_networkx_edges(G, pos, alpha=0.2, width=1)

# Draw nodes
node_colors = list(nx.get_node_attributes(G, 'color').values())
nx.draw_networkx_nodes(G, pos, node_color=node_colors, 
                      node_size=100, alpha=0.6)

# Customize the plot
plt.xlabel('Differentiation Progress', fontsize=12)
plt.ylabel('Myeloid vs Lymphoid Factor Expression', fontsize=12)
plt.title('Connected States in Differentiation Space', fontsize=14)

# Add legend
legend_elements = [plt.scatter([], [], c=color, label=cell_type, alpha=0.6)
                  for cell_type, color in colors.items()]
plt.legend(handles=legend_elements, bbox_to_anchor=(1.05, 1), 
          loc='upper left', fontsize=10)

# Set axis limits
plt.xlim(0.2, 2.3)
plt.ylim(0, 1)

plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
