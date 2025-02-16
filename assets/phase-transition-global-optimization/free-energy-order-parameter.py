import numpy as np
import matplotlib.pyplot as plt

# Define parameters
t = -4.0  # Keep same parameter
c = 1.0   # Keep same parameter
bias_values = [0.5, 0, -0.5]  # Market bias values (favors English, neutral, favors Math)

# Create fraction values for study time allocation
fraction = np.linspace(-2, 2, 1000)

# Create figure with three subplots
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))
axes = [ax1, ax2, ax3]

# Plot for each value of bias
for ax, bias in zip(axes, bias_values):
    # Calculate expected income (negative of original function to maximize)
    income = -(t * fraction**2 + c * fraction**4 - bias * fraction)
    
    # Create the plot
    ax.plot(fraction, income, 'b-', linewidth=2)
    ax.grid(True, alpha=0.3)
    
    # Add labels
    ax.set_xlabel('Study Balance (Math ← → English)', fontsize=10)
    ax.set_ylabel('Expected Lifetime Income', fontsize=10)
    ax.set_title(f'Market Bias = {bias}', fontsize=12)
    
    # Add horizontal and vertical lines at origin
    ax.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    ax.axvline(x=0, color='k', linestyle='-', alpha=0.3)

# Add overall title
plt.figtext(0.5, 0.95, 'Expected Income vs Study Choice\n(Math ← → English)', 
            fontsize=14, ha='center')

# Adjust layout with extra space for title
plt.tight_layout(rect=[0, 0, 1, 0.93])
plt.show()
