import numpy as np
import matplotlib.pyplot as plt

def rayleigh_pdf(x, sigma=1):
    """
    Compute the Rayleigh distribution PDF
    f(x) = (x/sigma^2) * exp(-x^2/(2*sigma^2))
    """
    return (x / (sigma**2)) * np.exp(-x**2 / (2*sigma**2))

# Create data points
x = np.linspace(0, 4, 200)

# Create the plot
plt.figure(figsize=(10, 6))

# Plot for different sigma values
sigmas = [0.5, 1.0, 1.5]
for sigma in sigmas:
    pdf = rayleigh_pdf(x, sigma)
    plt.plot(x, pdf, label=f'σ = {sigma}')

# Customize the plot
plt.title('Rayleigh Distribution PDF', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('Probability Density', fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend()

# Ensure non-negative x-axis
plt.xlim(0, max(x))
plt.ylim(0, None)

plt.show()
