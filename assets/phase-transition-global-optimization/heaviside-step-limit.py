import numpy as np
import matplotlib.pyplot as plt

def tanh_approximation(x, k):
    """
    Creates a hyperbolic tangent approximation to the Heaviside step function.
    k controls the steepness of the transition
    """
    return 0.5 * (1 + np.tanh(k * x))

def heaviside(x):
    """
    Heaviside step function
    """
    return np.where(x < 0, 0, 1)

# Create x values
x = np.linspace(-5, 5, 1000)

# Create figure and axis
plt.figure(figsize=(12, 8))

# Plot approximations with different steepness
k_values = [1, 2, 5, 10]
for k in k_values:
    plt.plot(x, tanh_approximation(x, k), 
             label=f'tanh approximation (k={k})', 
             linewidth=2)

# Plot the true Heaviside function
plt.plot(x, heaviside(x), 'k--', 
         label='Heaviside step function', 
         linewidth=2)

# Customize the plot
plt.grid(True, alpha=0.3)
plt.legend(fontsize=10)
plt.title('Approximating the Heaviside Step Function\nusing hyperbolic tangent functions', 
          fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)

# Set y-axis limits with some padding
plt.ylim(-0.1, 1.1)

# Show the plot
plt.tight_layout()
plt.show()
