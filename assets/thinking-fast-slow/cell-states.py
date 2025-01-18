import numpy as np
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# Define cell types and their approximate positions
# x: differentiation progress
# y: relative expression of myeloid vs lymphoid transcription factors
cell_types = {
    'HSC':  (0.5, 0.5),    # Multipotent stem cell - balanced expression
    'CMP':  (1.5, 0.8),    # Common Myeloid Progenitor - high myeloid factors
    'CLP':  (1.5, 0.2),    # Common Lymphoid Progenitor - high lymphoid factors
    'GMP':  (2.0, 0.7),    # Granulocyte-Macrophage Progenitor
    'BCell': (2.0, 0.1),   # B Cell precursor
}

# Colors for different cell types
colors = {
    'HSC':  '#FFB6C1',    # Light pink
    'CMP':  '#FF6B6B',    # Red
    'CLP':  '#98FB98',    # Pale green
    'GMP':  '#87CEFA',    # Light blue
    'BCell': '#9370DB',   # Purple
}

# Create multiple points around each position to show state clusters
n_points = 5
points = {}
for cell_type, (x, y) in cell_types.items():
    points[cell_type] = {
        'x': np.random.normal(x, 0.05, n_points),
        'y': np.random.normal(y, 0.05, n_points)
    }

# Create the plot
plt.figure(figsize=(10, 8))

# Plot each cell type
for cell_type in cell_types:
    plt.scatter(points[cell_type]['x'], points[cell_type]['y'],
               c=colors[cell_type],
               label=cell_type,
               s=100,
               alpha=0.6)

# Customize the plot
plt.xlabel('Differentiation Progress', fontsize=12)
plt.ylabel('Myeloid vs Lymphoid Factor Expression', fontsize=12)
plt.title('Cell Types in Differentiation Space', fontsize=14)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=10)
plt.grid(True, alpha=0.3)

# Set axis limits
plt.xlim(0.2, 2.3)
plt.ylim(0, 1)

plt.tight_layout()
plt.show()
