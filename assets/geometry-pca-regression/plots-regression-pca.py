import numpy as np
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# Generate data in standard normal units with correlation = 0.5
n_points = 250
X = np.random.normal(0, 1, n_points)
b = 0.5  # coefficient to achieve correlation of 0.5
epsilon = np.random.normal(0, np.sqrt(3)/2, n_points)  # variance adjusted to maintain unit variance in Y
Y = b * X + epsilon

# Transform to real heights (inches)
height_mean = 69  # 5'9" in inches
height_sd = 3     # standard deviation in inches
X_heights = X * height_sd + height_mean
Y_heights = Y * height_sd + height_mean

def fit_regression(x, y):
    """Returns slope and intercept for regression line"""
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    numerator = np.sum((x - x_mean) * (y - y_mean))
    denominator = np.sum((x - x_mean) ** 2)
    slope = numerator / denominator
    intercept = y_mean - slope * x_mean
    return slope, intercept

def get_pca_direction(x, y):
    """Returns the direction of the first principal component"""
    x_centered = x - np.mean(x)
    y_centered = y - np.mean(y)
    cov_matrix = np.array([
        [np.sum(x_centered * x_centered), np.sum(x_centered * y_centered)],
        [np.sum(x_centered * y_centered), np.sum(y_centered * y_centered)]
    ]) / (len(x) - 1)
    eigenvals, eigenvecs = np.linalg.eigh(cov_matrix)
    return eigenvecs[:, np.argmax(eigenvals)]

def get_point_and_projection(x, y, slope, intercept, method='y_on_x'):
    """Get a point in the fourth quadrant and its projection onto the line y = mx + b"""
    # Find points in fourth quadrant (x > 0, y < 0)
    fourth_quad_indices = np.where((x > 0) & (y < 0))[0]
    # Choose the point closest to x=1, y=-1 in the fourth quadrant
    distances = np.sqrt((x[fourth_quad_indices] - 1)**2 + (y[fourth_quad_indices] + 1)**2)
    chosen_idx = fourth_quad_indices[np.argmin(distances)]
    
    point = (x[chosen_idx], y[chosen_idx])
    
    if method == 'y_on_x':
        # Vertical projection: same x, y on line
        proj_x = point[0]
        proj_y = slope * proj_x + intercept
    elif method == 'x_on_y':
        # Horizontal projection: same y, x from line equation
        proj_y = point[1]
        proj_x = (proj_y - intercept) / slope
    
    return point, (proj_x, proj_y)

def setup_plot(x_data, y_data, x_label, y_label, plot_range=None):
    """Creates a new figure with consistent styling"""
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # Make axes more prominent
    ax.axhline(y=0, color='k', linestyle='-', linewidth=0.8)
    ax.axvline(x=0, color='k', linestyle='-', linewidth=0.8)
    
    ax.scatter(x_data, y_data, alpha=0.5, label='Data points')
    
    if plot_range:
        ax.set_xlim(plot_range)
        ax.set_ylim(plot_range)
    
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.2)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    return fig, ax

# Calculate all regression parameters once
slope_y_on_x, intercept_y_on_x = fit_regression(X, Y)
slope_x_on_y, intercept_x_on_y = fit_regression(Y, X)
slope_x_on_y_converted = 1/slope_x_on_y
intercept_x_on_y_converted = -intercept_x_on_y/slope_x_on_y

# Calculate PCA direction
pca_vector = get_pca_direction(X, Y)
pca_slope = pca_vector[1]/pca_vector[0]

# Define line ranges for plotting
x_line = np.array([-2.5, 2.5])
std_range = (-2.5, 2.5)
height_range = (height_mean - 3*height_sd, height_mean + 3*height_sd)

# Generate all regression lines once
y_pred_yx = slope_y_on_x * x_line + intercept_y_on_x
y_pred_xy = slope_x_on_y_converted * x_line + intercept_x_on_y_converted
pca_line = np.vstack([x_line, x_line * pca_slope])

# Get example points and their projections
point_yx, proj_yx = get_point_and_projection(X, Y, slope_y_on_x, intercept_y_on_x)
point_xy, proj_xy = get_point_and_projection(X, Y, slope_x_on_y_converted, intercept_x_on_y_converted)

# For PCA, projection is orthogonal
# Calculate orthogonal projection onto PCA line
pca_point = (X[42], Y[42])
pca_normal = np.array([-pca_slope, 1]) / np.sqrt(1 + pca_slope**2)
point_vec = np.array([pca_point[0], pca_point[1]])
proj_dist = np.dot(point_vec, pca_normal)
pca_proj = point_vec - proj_dist * pca_normal

# Calculate displacements for each method using the same point
point_yx, proj_yx = get_point_and_projection(X, Y, slope_y_on_x, intercept_y_on_x, method='y_on_x')
# Use same point for X on Y regression
point_xy = point_yx
proj_xy = get_point_and_projection(X, Y, slope_x_on_y_converted, intercept_x_on_y_converted, method='x_on_y')[1]

# For PCA, projection is orthogonal
pca_point = point_yx  # Use same point for consistency
pca_normal = np.array([-pca_slope, 1]) / np.sqrt(1 + pca_slope**2)
point_vec = np.array([pca_point[0], pca_point[1]])
proj_dist = np.dot(point_vec, pca_normal)
pca_proj = point_vec - proj_dist * pca_normal

# Define displacement specifications
yx_displacement = {
    'point': point_yx,
    'proj': proj_yx,
    'color': 'red',
    'style': 'vertical'
}

xy_displacement = {
    'point': point_xy,
    'proj': proj_xy,
    'color': 'green',
    'style': 'horizontal'
}

pca_displacement = {
    'point': (pca_point[0], pca_point[1]),
    'proj': (pca_proj[0], pca_proj[1]),
    'color': 'blue',
    'style': 'orthogonal'
}

# Create all plots
plots = [
    # Heights in real units
    {
        'data': (X_heights, Y_heights),
        'labels': ("Father's Height (inches)", "Son's Height (inches)"),
        'range': height_range,
        'title': f'Father-Son Height Relationships\nN = {n_points} pairs'
    },
    # Standard normal units plots
    {
        'data': (X, Y),
        'labels': ('X (standardized)', 'Y (standardized)'),
        'range': std_range,
        'title': f'Standardized Heights\nN = {n_points} points'
    },
    {
        'data': (X, Y),
        'labels': ('X (standardized)', 'Y (standardized)'),
        'range': std_range,
        'title': 'Y on X Regression\nMinimizes vertical distances',
        'lines': [((x_line, y_pred_yx), 'r-', 'Y on X regression')],
        'equation': f'Y = {slope_y_on_x:.3f}X + {intercept_y_on_x:.3f}',
        'displacement': {
            'point': point_yx,
            'proj': proj_yx,
            'color': 'red',
            'style': 'vertical'
        }
    },
    {
        'data': (X, Y),
        'labels': ('X (standardized)', 'Y (standardized)'),
        'range': std_range,
        'title': 'X on Y Regression\nMinimizes horizontal distances',
        'lines': [((x_line, y_pred_xy), 'g-', 'X on Y regression')],
        'equation': f'Y = {slope_x_on_y_converted:.3f}X + {intercept_x_on_y_converted:.3f}',
        'displacement': {
            'point': point_xy,
            'proj': proj_xy,
            'color': 'green',
            'style': 'horizontal'
        }
    },
    {
        'data': (X, Y),
        'labels': ('X (standardized)', 'Y (standardized)'),
        'range': std_range,
        'title': 'Both Regression Lines',
        'lines': [
            ((x_line, y_pred_yx), 'r-', 'Y on X'),
            ((x_line, y_pred_xy), 'g-', 'X on Y')
        ],
        'equation': (f'Y on X: Y = {slope_y_on_x:.3f}X + {intercept_y_on_x:.3f}\n'
                    f'X on Y: Y = {slope_x_on_y_converted:.3f}X + {intercept_x_on_y_converted:.3f}'),
        'displacements': [yx_displacement, xy_displacement]
    },
    {
        'data': (X, Y),
        'labels': ('X (standardized)', 'Y (standardized)'),
        'range': std_range,
        'title': 'PCA First Component\nDirection of maximum variance',
        'lines': [((pca_line[0], pca_line[1]), 'b-', 'PCA')],
        'equation': f'Y = {pca_slope:.3f}X',
        'displacement': {
            'point': (pca_point[0], pca_point[1]),
            'proj': (pca_proj[0], pca_proj[1]),
            'color': 'blue',
            'style': 'orthogonal'
        }
    },
    {
        'data': (X, Y),
        'labels': ('X (standardized)', 'Y (standardized)'),
        'range': std_range,
        'title': 'All Methods Compared',
        'lines': [
            ((x_line, y_pred_yx), 'r-', 'Y on X'),
            ((x_line, y_pred_xy), 'g-', 'X on Y'),
            ((pca_line[0], pca_line[1]), 'b-', 'PCA')
        ],
        'equation': (f'Y on X: Y = {slope_y_on_x:.3f}X + {intercept_y_on_x:.3f}\n'
                    f'X on Y: Y = {slope_x_on_y_converted:.3f}X + {intercept_x_on_y_converted:.3f}\n'
                    f'PCA: Y = {pca_slope:.3f}X'),
        'displacements': [yx_displacement, xy_displacement, pca_displacement]
    }
]

# Generate all plots
for plot_spec in plots:
    fig, ax = setup_plot(*plot_spec['data'], *plot_spec['labels'], plot_spec['range'])
    
    if 'lines' in plot_spec:
        for (x, y), style, label in plot_spec['lines']:
            ax.plot(x, y, style, label=label)
    
    if 'equation' in plot_spec:
        ax.text(0.95, 0.95, plot_spec['equation'], transform=ax.transAxes,
                bbox=dict(facecolor='white', alpha=0.8),
                horizontalalignment='right',
                verticalalignment='top')
    
    def plot_displacement(ax, d):
        point, proj = d['point'], d['proj']
        if d['style'] == 'vertical':
            ax.plot([point[0], point[0]], [point[1], proj[1]], 
                   color=d['color'], linestyle='--', alpha=0.7, linewidth=1.5)
        elif d['style'] == 'horizontal':
            ax.plot([point[0], proj[0]], [point[1], point[1]], 
                   color=d['color'], linestyle='--', alpha=0.7, linewidth=1.5)
        elif d['style'] == 'orthogonal':
            ax.plot([point[0], proj[0]], [point[1], proj[1]], 
                   color=d['color'], linestyle='--', alpha=0.7, linewidth=1.5)
        ax.plot(point[0], point[1], marker='o', color=d['color'], alpha=0.7)
        ax.plot(proj[0], proj[1], marker='x', color=d['color'], alpha=0.7)

    if 'displacement' in plot_spec:
        plot_displacement(ax, plot_spec['displacement'])
    
    if 'displacements' in plot_spec:
        for d in plot_spec['displacements']:
            plot_displacement(ax, d)
    
    ax.set_title(plot_spec['title'])
    ax.legend()
    plt.show()

# Print out the slopes for comparison
print(f"Y on X slope: {slope_y_on_x:.3f}")
print(f"X on Y slope (converted): {slope_x_on_y_converted:.3f}")
print(f"PCA direction slope: {pca_slope:.3f}")

# Verify correlation
print(f"\nActual correlation: {np.corrcoef(X, Y)[0,1]:.3f}")
