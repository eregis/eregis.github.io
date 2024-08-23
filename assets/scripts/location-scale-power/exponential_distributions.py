import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon

# Set up the x-axis
x = np.linspace(0, 10, 1000)

# Create three exponential distributions with different scale parameters (tau)
tau1, tau2, tau3 = 0.5, 1, 2

# Plot the distributions
plt.figure(figsize=(10, 6))
plt.plot(x, expon.pdf(x, scale=tau1), label=f'τ = {tau1}')
plt.plot(x, expon.pdf(x, scale=tau2), label=f'τ = {tau2}')
plt.plot(x, expon.pdf(x, scale=tau3), label=f'τ = {tau3}')

# Customize the plot
plt.title('Exponential Distributions with Different Scale Parameters (τ)')
plt.xlabel('t')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True, alpha=0.3)

# Add caption
plt.figtext(0.5, -0.05, 'τ is a scale parameter for exponential distributions', 
            ha='center', fontsize=10)

# Save the plot
plt.savefig('exponential_distributions.png', dpi=300, bbox_inches='tight')
plt.close()

print("The plot has been saved as 'exponential_distributions.png'")
