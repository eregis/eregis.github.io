import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Set up the figure
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Plot the statistical manifold
ax1.set_xlim(0, 5)
ax1.set_ylim(0, 5)
ax1.set_xlabel('Mean (μ)')
ax1.set_ylabel('Variance (σ²)')
ax1.set_title('Statistical Manifold')

# Define two points
point1 = (2, 1)  # (mean, variance)
point2 = (3, 3)  # (mean, variance)

# Plot points on the statistical manifold
ax1.scatter(*point1, color='red', s=100, label='Distribution 1')
ax1.scatter(*point2, color='blue', s=100, label='Distribution 2')
ax1.legend()

# Plot the normal distributions
x = np.linspace(-5, 10, 1000)
y1 = norm.pdf(x, point1[0], np.sqrt(point1[1]))
y2 = norm.pdf(x, point2[0], np.sqrt(point2[1]))

ax2.plot(x, y1, color='red', label=f'μ={point1[0]}, σ²={point1[1]}')
ax2.plot(x, y2, color='blue', label=f'μ={point2[0]}, σ²={point2[1]}')
ax2.set_xlabel('x')
ax2.set_ylabel('Probability Density')
ax2.set_title('Normal Distributions')
ax2.legend()

plt.tight_layout()

# Save the figure
plt.savefig('statistical_manifold_and_distributions.png', dpi=300, bbox_inches='tight')

print("The graph has been saved as 'statistical_manifold_and_distributions.png'")

# If you want to display the plot as well, uncomment the next line
# plt.show()
