import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Set up the x-axis
x = np.linspace(-5, 5, 1000)

# Create three normal distributions with different means
mu1, mu2, mu3 = -1, 0, 2
sigma = 1

# Plot the distributions
plt.figure(figsize=(10, 6))
plt.plot(x, norm.pdf(x, mu1, sigma), label=f'μ = {mu1}')
plt.plot(x, norm.pdf(x, mu2, sigma), label=f'μ = {mu2}')
plt.plot(x, norm.pdf(x, mu3, sigma), label=f'μ = {mu3}')

# Customize the plot
plt.title('Normal Distributions with Different Location Parameters (μ)')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True, alpha=0.3)

# Add caption
plt.figtext(0.5, -0.05, 'μ is a location parameter for normal distributions', 
            ha='center', fontsize=10)

# Save the plot
plt.savefig('normal_distributions.png', dpi=300, bbox_inches='tight')
plt.close()

print("The plot has been saved as 'normal_distributions.png'")
