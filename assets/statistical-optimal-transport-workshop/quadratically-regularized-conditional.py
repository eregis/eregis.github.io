import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Set plotting parameters
plt.style.use('seaborn-v0_8-whitegrid')
plt.figure(figsize=(10, 6))

# Create domain for visualization
x = np.linspace(-3, 3, 1000)

def truncated_parabola(x, x0=0, width=1.5):
    """
    Compute the truncated parabola distribution for quadratically-regularized OT.
    This is the conditional distribution form where the density is:
    (constant - ||x-x0||^2) where positive, and zero elsewhere.
    """
    # The parabola is centered at x0 with a width determined by the regularization strength
    density = 1.0 - ((x - x0) / width) ** 2
    # Truncate at zero (Radon derivative cannot be negative)
    density[density < 0] = 0
    # Normalize to make it a valid probability density
    if np.sum(density) > 0:
        density = density / np.trapz(density, x)
    return density

def gaussian(x, x0=0, sigma=0.5):
    """Compute a Gaussian distribution for comparison."""
    return norm.pdf(x, loc=x0, scale=sigma)

# Compute distributions centered at zero
quadratic_dist = truncated_parabola(x, x0=0, width=1.5)
gaussian_dist = gaussian(x, x0=0, sigma=0.5)

# Plot both distributions for comparison
plt.plot(x, quadratic_dist, label='Quadratically-regularized OT', color='#1f77b4', linewidth=2.5)
plt.plot(x, gaussian_dist, label='Entropic OT (Gaussian)', color='#d62728', linewidth=2.5)

# Add vertical lines to show where the quadratic distribution becomes zero
nonzero_indices = np.where(quadratic_dist > 0)[0]
if len(nonzero_indices) > 0:
    left_edge = x[nonzero_indices[0]]
    right_edge = x[nonzero_indices[-1]]
    plt.axvline(left_edge, color='#1f77b4', linestyle='--', alpha=0.7)
    plt.axvline(right_edge, color='#1f77b4', linestyle='--', alpha=0.7)
    plt.fill_between(x, quadratic_dist, 0, where=(x >= left_edge) & (x <= right_edge), 
                    color='#1f77b4', alpha=0.2)
    
    # Add direct labels to the curves instead of an arrow
    plt.text(0, 0.7*max(quadratic_dist), "Quadratically-regularized OT\n(Finite Support)", 
            ha='center', color='#1f77b4', fontweight='bold')
    plt.text(1.5, 0.4*max(gaussian_dist), "Entropic OT\n(Infinite Support)", 
            ha='center', color='#d62728', fontweight='bold')

# Fill Gaussian curve with light color
plt.fill_between(x, gaussian_dist, 0, color='#d62728', alpha=0.1)

plt.show()
