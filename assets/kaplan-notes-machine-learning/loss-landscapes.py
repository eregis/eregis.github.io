import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create figure with two subplots
fig = plt.figure(figsize=(14, 6))

# Create grid for plotting
x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)

# Subplot 1: Convex loss landscape (quadratic bowl)
ax1 = fig.add_subplot(121, projection='3d')
Z_convex = X**2 + Y**2  # Simple convex quadratic function

surf1 = ax1.plot_surface(X, Y, Z_convex, cmap='viridis', alpha=0.8, edgecolor='none')
ax1.set_xlabel('Parameter 1')
ax1.set_ylabel('Parameter 2')
ax1.set_zlabel('Loss')
ax1.set_title('Convex Loss Landscape', fontsize=14, fontweight='bold')
ax1.view_init(elev=25, azim=45)

# Subplot 2: Non-convex loss landscape (multiple local minima)
ax2 = fig.add_subplot(122, projection='3d')
# Create a non-convex function with multiple local minima
Z_nonconvex = (X**2 + Y**2) * 0.3 + np.sin(2*X) * np.cos(2*Y) * 2 + 5

surf2 = ax2.plot_surface(X, Y, Z_nonconvex, cmap='plasma', alpha=0.8, edgecolor='none')
ax2.set_xlabel('Parameter 1')
ax2.set_ylabel('Parameter 2')
ax2.set_zlabel('Loss')
ax2.set_title('Non-Convex Loss Landscape', fontsize=14, fontweight='bold')
ax2.view_init(elev=25, azim=45)

plt.tight_layout()
plt.savefig('loss_landscapes.png', dpi=300, bbox_inches='tight')
plt.show()

print("Figure saved as 'loss_landscapes.png'")
