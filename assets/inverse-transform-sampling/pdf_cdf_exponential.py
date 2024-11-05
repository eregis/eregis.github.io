import numpy as np
import matplotlib.pyplot as plt

# Create figure with two subplots side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Generate x values
x = np.linspace(0, 5, 1000)

# Calculate PDF: f(x) = e^(-x) for λ=1
pdf = np.exp(-x)

# Calculate CDF: F(x) = 1 - e^(-x) for λ=1
cdf = 1 - np.exp(-x)

# Plot PDF
ax1.plot(x, pdf, 'b-', lw=2)
ax1.plot(0, 1, 'bo')  # Mark starting point
ax1.grid(True)
ax1.set_title('Exponential PDF (λ=1)')
ax1.set_xlabel('x')
ax1.set_ylabel('f(x)')
ax1.set_ylim(-0.1, 1.2)

# Plot CDF
ax2.plot(x, cdf, 'r-', lw=2)
ax2.plot(0, 0, 'ro')  # Mark starting point
ax2.grid(True)
ax2.set_title('Exponential CDF (λ=1)')
ax2.set_xlabel('x')
ax2.set_ylabel('F(x)')
ax2.set_ylim(-0.1, 1.1)

plt.tight_layout()
plt.show()
