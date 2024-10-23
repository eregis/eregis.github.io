import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon

# Set random seed for reproducibility
np.random.seed(42)

# Create figure with three subplots
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 4))
fig.suptitle("Visualization of Markov's Inequality Proof")

# Parameters
lambda_param = 1  # Rate parameter for exponential distribution
a = 2  # Threshold
x = np.linspace(0, 6, 1000)
y = expon.pdf(x, scale=1/lambda_param)

# Calculate probabilities
P_less_than_a = expon.cdf(a, scale=1/lambda_param)
P_greater_than_a = 1 - P_less_than_a

# Calculate maximum y value for consistent scaling
max_y = max(max(y), P_less_than_a, P_greater_than_a) * 1.1  # Add 10% padding

# First plot: Original distribution with colored regions
ax1.plot(x, y, 'k-', alpha=0.5, label='PDF')
ax1.fill_between(x[x < a], y[x < a], color='blue', alpha=0.3, label='x < a')
ax1.fill_between(x[x >= a], y[x >= a], color='red', alpha=0.3, label='x ≥ a')
ax1.axvline(x=a, color='gray', linestyle='--', label='x = a')
ax1.set_title('Original Distribution')
ax1.set_xlabel('x')
ax1.set_ylabel('Probability Density')
ax1.legend()
ax1.set_xlim(0, 6)
ax1.set_ylim(0, max_y)

# Second plot: Mass ≥ a moved to point a
ax2.plot(x[x < a], y[x < a], 'k-', alpha=0.5)
ax2.fill_between(x[x < a], y[x < a], color='blue', alpha=0.3)
# Add spike at x = a
ax2.vlines(a, 0, P_greater_than_a, color='red', alpha=0.7)
ax2.plot(a, P_greater_than_a, 'ro', markersize=10)
ax2.axvline(x=a, color='gray', linestyle='--')
ax2.set_title('Mass ≥ a Moved to x = a')
ax2.set_xlabel('x')
ax2.set_ylabel('Probability Density')
ax2.set_xlim(0, 6)
ax2.set_ylim(0, max_y)

# Third plot: Mass < a moved to 0, mass ≥ a at a
ax3.vlines(0, 0, P_less_than_a, color='blue', alpha=0.7)
ax3.vlines(a, 0, P_greater_than_a, color='red', alpha=0.7)
ax3.plot(0, P_less_than_a, 'bo', markersize=10)
ax3.plot(a, P_greater_than_a, 'ro', markersize=10)
ax3.axvline(x=a, color='gray', linestyle='--')
ax3.set_title('Final Distribution')
ax3.set_xlabel('x')
ax3.set_ylabel('Probability Mass')
ax3.set_xlim(0, 6)
ax3.set_ylim(0, max_y)

# Adjust layout and display
plt.tight_layout()
plt.show()

# Print probabilities for verification
print(f"P(X < {a}) = {P_less_than_a:.3f}")
print(f"P(X ≥ {a}) = {P_greater_than_a:.3f}")
print(f"Sum of probabilities = {P_less_than_a + P_greater_than_a:.3f}")
