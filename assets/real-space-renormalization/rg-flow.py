import numpy as np
import matplotlib.pyplot as plt

# Set up the figure with minimal style
fig, ax = plt.subplots(figsize=(8, 6))

# Define K range
K = np.linspace(0, 2.5, 500)

# Define the RG transformation: K' = 1/2 * log(cosh(2K))
K_prime = 0.5 * np.log(np.cosh(2*K))

# Plot the two curves
ax.plot(K, K, 'k-', linewidth=1.5, label=r"$K' = K$")
ax.plot(K, K_prime, 'b-', linewidth=1.5, label=r"$K' = \frac{1}{2}\log(\cosh 2K)$")

# Starting point for RG flow visualization
K0 = 1.8
current_K = K0

# Store points for drawing the flow
flow_points_x = [current_K]
flow_points_y = [current_K]

# Perform 3 RG iterations
for i in range(3):
    # Calculate K' for current K
    K_new = 0.5 * np.log(np.cosh(2*current_K))
    
    # Down: from identity line to RG curve
    flow_points_x.append(current_K)
    flow_points_y.append(K_new)
    
    # Right: from RG curve to identity line (at new K value)
    flow_points_x.append(K_new)
    flow_points_y.append(K_new)
    
    current_K = K_new

# Draw the RG flow path with arrows
for i in range(0, len(flow_points_x)-1, 2):
    # Vertical segments (down)
    if i < len(flow_points_x)-1:
        ax.annotate('', xy=(flow_points_x[i], flow_points_y[i+1]), 
                   xytext=(flow_points_x[i], flow_points_y[i]),
                   arrowprops=dict(arrowstyle='->', color='red', lw=1.2))
    
    # Horizontal segments (right) - dashed
    if i+1 < len(flow_points_x)-1:
        ax.annotate('', xy=(flow_points_x[i+2], flow_points_y[i+1]), 
                   xytext=(flow_points_x[i+1], flow_points_y[i+1]),
                   arrowprops=dict(arrowstyle='->', color='red', lw=1.2, linestyle='--'))

# Mark the starting point
ax.plot(K0, K0, 'ro', markersize=6)

# Mark fixed points
ax.plot(0, 0, 'ko', markersize=8, markerfacecolor='white', markeredgewidth=2)
ax.text(0.05, -0.15, r'$K^* = 0$', fontsize=11)

# Set axis properties
ax.set_xlim(-0.1, 2.5)
ax.set_ylim(-0.2, 2.5)
ax.set_xlabel(r'$K$', fontsize=14)
ax.set_aspect('equal')

# Add grid for clarity
ax.grid(True, alpha=0.3, linestyle='--')

# Legend
ax.legend(loc='upper left', frameon=False, fontsize=11)

# Remove y-axis label as requested
ax.set_yticklabels([])

# Title
ax.set_title('RG Flow in the 1D Ising Model', fontsize=14, pad=15)

plt.tight_layout()
plt.show()
