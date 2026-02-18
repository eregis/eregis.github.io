import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(6, 3.5))

# Potential landscape V(x) = x^2
x = np.linspace(-2.5, 2.5, 300)
V = x**2

ax.plot(x, V, color="black", linewidth=2)

# Ball position (off-center, on the right slope)
x_ball = 1.4
y_ball = x_ball**2
ax.plot(x_ball, y_ball, "o", color="#2E86C1", markersize=14, zorder=5)

# Arrow pointing downhill (tangent direction, negative gradient)
# Gradient of V at x_ball is 2*x_ball, so force direction is (-1, -2*x_ball) (unnormalized)
grad = 2 * x_ball
tangent = np.array([-1, -grad])
tangent = tangent / np.linalg.norm(tangent)
arrow_len = 1.2

ax.annotate(
    "",
    xy=(x_ball + arrow_len * tangent[0], y_ball + arrow_len * tangent[1]),
    xytext=(x_ball, y_ball),
    arrowprops=dict(arrowstyle="->,head_width=0.3,head_length=0.15", color="#C0392B", lw=2.5),
    zorder=6,
)

# Label the arrow (positioned to the left of the arrow, not overlapping the ball)
label_pos = np.array([x_ball, y_ball]) + arrow_len * 0.5 * tangent + np.array([-0.55, 0.1])
ax.text(
    label_pos[0], label_pos[1],
    r"$F = -\nabla V$",
    fontsize=14, color="#C0392B", ha="right", va="bottom",
)

# Styling
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-0.3, 5.5)
ax.set_xlabel(r"$x$", fontsize=13)
ax.set_ylabel(r"$V(x)$", fontsize=13)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.tick_params(labelsize=11)
ax.set_xticks([])
ax.set_yticks([])

plt.savefig(
    "C:/Users/ericf/critical-points/assets/wasserstein-gradient/gradient-descent-landscape.png",
    dpi=300, bbox_inches="tight", facecolor="white",
)
plt.close()
print("Figure saved.")
