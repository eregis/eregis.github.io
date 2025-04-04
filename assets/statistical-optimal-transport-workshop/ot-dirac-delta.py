import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

def plot_dirac_transport(x1, x2, height=1.0):
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Plot settings
    ax.set_xlim(min(x1, x2) - 1, max(x1, x2) + 1)
    ax.set_ylim(0, height + 0.5)
    ax.set_xlabel('x')
    ax.set_ylabel('Density')
    ax.set_title('Transport between Dirac Delta Measures')
    
    # Plot Dirac deltas as vertical lines
    ax.vlines(x1, 0, height, color='blue', label=f'δ(x-{x1})')
    ax.vlines(x2, 0, height, color='red', label=f'δ(x-{x2})')
    
    # Add arrow between the deltas
    arrow = FancyArrowPatch(
        (x1, height/2),
        (x2, height/2),
        arrowstyle='->',
        mutation_scale=20,
        color='green',
        label=f'Transport cost: {abs(x2-x1):.1f}'
    )
    ax.add_patch(arrow)
    
    # Add legend
    ax.legend()
    
    plt.grid(True, alpha=0.3)
    plt.show()

# Example usage
plot_dirac_transport(-1, 2)  # Transport from x=-1 to x=2
