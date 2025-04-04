import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Set up the figure and axis
plt.figure(figsize=(8, 5))

# Define the y range for plotting - expanded to show the full uniform distribution
y = np.linspace(-8, 8, 1000)

# Plot Dirac delta at y=0 (epsilon = 0)
plt.axvline(x=0, color='#2C3E50', linestyle='-', linewidth=2, label="ε = 0")

# Plot standard Gaussian for finite epsilon - more concentrated
sigma = 0.7  # Made narrower to contrast with uniform
pdf = norm.pdf(y, loc=0, scale=sigma)
plt.plot(y, pdf, color='#E74C3C', linestyle='--', linewidth=2, label="Finite ε")

# Plot uniform distribution for epsilon = infinity
# Much wider uniform distribution to show order of magnitude difference
uniform_width = 10.0  # from -5 to 5
uniform_height = 1/uniform_width  # 1/(upper_bound - lower_bound)
uniform_y = np.zeros_like(y)
uniform_y[(y >= -5) & (y <= 5)] = uniform_height
plt.plot(y, uniform_y, color='#3498DB', linestyle='-.', linewidth=2, label="ε → ∞")

# Set labels and title
plt.xlabel('y', fontsize=11)
plt.ylabel('p(y|x=0)', fontsize=11)
plt.title('Conditional Distribution p(y|x=0) for Different ε Values', fontsize=12)
plt.legend(loc='upper right')
plt.grid(True, alpha=0.2)

# Set y-axis limit to better show the distributions
plt.ylim(0, 0.6)

# Add x-axis ticks
plt.xticks(np.arange(-6, 7, 2))

plt.tight_layout()
plt.show()
