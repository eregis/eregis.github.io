import numpy as np
import matplotlib.pyplot as plt

# Create figure with two subplots side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Generate x values slightly beyond [0,1] to show the discontinuities
x = np.linspace(-0.2, 1.2, 1000)

# Create PDF values
pdf = np.where((x >= 0) & (x <= 1), 1, 0)

# Create CDF values
cdf = np.where(x < 0, 0, 
               np.where(x > 1, 1, x))

# Plot PDF
ax1.plot(x, pdf, 'b-', lw=2)
ax1.grid(True)
ax1.set_title('Uniform PDF')
ax1.set_xlabel('x')
ax1.set_ylabel('f(x)')
ax1.set_ylim(-0.1, 1.5)

# Add points to show discontinuities in PDF
ax1.plot([0, 0], [0, 1], 'b--', alpha=0.5)  # vertical line at x=0
ax1.plot([1, 1], [0, 1], 'b--', alpha=0.5)  # vertical line at x=1
ax1.plot(0, 1, 'bo')  # point at (0,1)
ax1.plot(0, 0, 'wo', markeredgecolor='b')  # open point at (0,0)
ax1.plot(1, 1, 'bo')  # point at (1,1)
ax1.plot(1, 0, 'wo', markeredgecolor='b')  # open point at (1,0)

# Plot CDF
ax2.plot(x, cdf, 'r-', lw=2)
ax2.grid(True)
ax2.set_title('Uniform CDF')
ax2.set_xlabel('x')
ax2.set_ylabel('F(x)')
ax2.set_ylim(-0.1, 1.1)

# Add points to show where CDF transitions
ax2.plot(0, 0, 'ro')  # point at (0,0)
ax2.plot(1, 1, 'ro')  # point at (1,1)

plt.tight_layout()
plt.show()
