import numpy as np
import matplotlib.pyplot as plt

def potential(x):
    """Potential function: x^2 / sqrt(1 + x^2)"""
    return x**2 / np.sqrt(1 + x**2)

def gradient(x):
    """Gradient of the potential"""
    sqrt_term = np.sqrt(1 + x**2)
    return 2*x / sqrt_term - x**3 / (sqrt_term**3)

def gradient_descent_step(x, eta):
    """One step of gradient descent"""
    return x - eta * gradient(x)

# Set up the problem
eta = 2.0  # Step size chosen so 2/eta = 2.0 (close to max curvature)
n_steps = 30  # Number of gradient descent steps

# Initial positions
x_flat_start = 1.5    # Start in flat region
x_curved_start = 0.5   # Start in curved region

# Run gradient descent
def run_gradient_descent(x_init, eta, n_steps):
    trajectory = [x_init]
    x = x_init
    for _ in range(n_steps):
        x = gradient_descent_step(x, eta)
        trajectory.append(x)
    return np.array(trajectory)

trajectory_flat = run_gradient_descent(x_flat_start, eta, n_steps)
trajectory_curved = run_gradient_descent(x_curved_start, eta, n_steps)

# Create the figure
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# X-axis for plotting the function
x_plot = np.linspace(-3, 3, 300)
y_plot = potential(x_plot)

# Plot for each scenario
scenarios = [
    (trajectory_flat, x_flat_start, "Start in flat region", axes[0]),
    (trajectory_curved, x_curved_start, "Start near center", axes[1])
]

for traj, x_start, title, ax in scenarios:
    # Plot the potential function
    ax.plot(x_plot, y_plot, 'b-', alpha=0.5, linewidth=2, 
            label='$f(x) = \\frac{x^2}{\\sqrt{1+x^2}}$')
    
    # Plot the trajectory points
    y_traj = potential(traj)
    ax.plot(traj, y_traj, 'ro-', markersize=6, alpha=0.7, linewidth=1)
    
    # Mark the starting point
    ax.plot(traj[0], y_traj[0], 'go', markersize=10, label='Start')
    
    # Add arrows to show the path (first 8 steps)
    for i in range(min(8, len(traj)-1)):
        ax.annotate('', xy=(traj[i+1], y_traj[i+1]), 
                   xytext=(traj[i], y_traj[i]),
                   arrowprops=dict(arrowstyle='->', color='red', alpha=0.5))
    
    # Set labels and title
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.set_title(f'{title}\n$x_0 = {x_start}$')
    ax.grid(True, alpha=0.3)
    ax.legend()
    
    # Fixed axis limits for both panels
    ax.set_xlim(-3, 3)
    ax.set_ylim(0, 2)

# Add main title
fig.suptitle(f'Gradient Descent on Varying Curvature Potential\n' + 
             f'Step size: $\\eta = {eta}$, Critical curvature: $2/\\eta = {2/eta}$', fontsize=14)

plt.tight_layout()
plt.show()

# Print analysis
print(f"Step size η = {eta}")
print(f"Critical curvature 2/η = {2/eta}")
print("\nScenario Analysis:")
print(f"1. Start in flat region (x = {x_flat_start}): Approaches center, curvature increases")
print(f"2. Start near center (x = {x_curved_start}): Repelled outward, curvature decreases")
print(f"\nFinal positions after {n_steps} steps:")
print(f"  Flat start: x = {trajectory_flat[-1]:.3f}")
print(f"  Curved start: x = {trajectory_curved[-1]:.3f}")
