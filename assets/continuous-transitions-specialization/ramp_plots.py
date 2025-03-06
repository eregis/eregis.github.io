import numpy as np
import matplotlib.pyplot as plt
from math import factorial

# Create data points
x = np.linspace(-2, 2, 1000)

# Plot 1: Simple ramp function
plt.figure(figsize=(10, 4))
y_ramp = np.maximum(0, x)
plt.plot(x, y_ramp)
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Ramp Function')

# Plot 2: Generalized ramp functions
plt.figure(figsize=(10, 4))
n_values = [1, 2, 3, 4]

for n in n_values:
    y = np.zeros_like(x)
    positive_mask = x > 0
    y[positive_mask] = x[positive_mask]**n / factorial(n)
    plt.plot(x, y, label=f'n={n}')

plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Generalized Ramp Functions')
plt.legend()

# Adjust layout and display plots
plt.tight_layout()
plt.show()
