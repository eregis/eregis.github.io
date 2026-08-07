"""
The classical cartoon of a spin, as introduced in Mehta et al.'s Ising-model
section: "at each lattice site there is a little particle spin; imagine it
spinning on its axis."

The Hamiltonian only ever talks about s_i in {+1, -1}, but the mnemonic every
student is handed for that variable is a tiny rotating sphere: the sense of
rotation generates a magnetic moment along the rotation axis via the
right-hand rule, so counterclockwise viewed from above pairs with a moment
pointing up and clockwise pairs with a moment pointing down. The rotation is
drawn as an equatorial ring seen in slight perspective, so the moment arrow
visibly runs along the rotation axis, perpendicular to the plane of rotation.
Two particles, mirror images of each other, are enough to carry both the
picture and the notation.

Output: spin-up-spin-down.png -- left: counterclockwise rotation (viewed
from above), moment pointing up, "spin up" / s_i = +1. Right: the mirror
image, clockwise rotation, moment pointing down, "spin down" / s_i = -1.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Ellipse

BLUE, RED = "#2166ac", "#b2182b"
SPHERE_FILL, SPHERE_EDGE = "#c7cdd4", "#5b6472"
TEXT = "#222222"

PR = 0.55         # particle radius
RR = 0.85         # equatorial rotation-ring radius
FLAT = 0.32       # perspective foreshortening of the ring (screen y = FLAT * y)
TIP = RR + 0.40   # moment-arrow tip, measured from the particle centre


def ring_point(cx, r, phi_deg):
    """Screen position of the equatorial-ring point at azimuth phi (degrees,
    counterclockwise viewed from above). The ring lies in the horizontal
    plane through the particle centre; seen from slightly above, it projects
    to an ellipse flattened by FLAT, with the far half on top."""
    phi = np.deg2rad(phi_deg)
    return cx + r * np.cos(phi), FLAT * r * np.sin(phi)


def rotation_ring(ax, cx, r, ccw, color, lw=2.1):
    """The rotation drawn as a ring around the particle's equator. The far
    half passes behind the sphere (fainter, lower zorder); the near half
    passes in front and carries the arrowhead. ccw is the sense of rotation
    viewed from above, i.e. looking down the moment-up axis."""
    xs, ys = ring_point(cx, r, np.linspace(0, 180, 120))
    ax.plot(xs, ys, color=color, lw=lw * 0.8, alpha=0.45,
            solid_capstyle="round", zorder=2)
    # near half, sampled in the direction of motion so the arrowhead leads
    theta = np.linspace(180, 340, 160) if ccw else np.linspace(360, 200, 160)
    xs, ys = ring_point(cx, r, theta)
    ax.plot(xs, ys, color=color, lw=lw, solid_capstyle="round", zorder=5)
    ax.annotate("", xy=(xs[-1], ys[-1]), xytext=(xs[-5], ys[-5]),
                arrowprops=dict(arrowstyle="-|>", color=color, lw=lw,
                                 mutation_scale=19, shrinkA=0, shrinkB=0),
                zorder=5)


def draw_spin(ax, cx, up, word, math_label):
    """One particle. up=True: counterclockwise spin (viewed from above),
    moment up ("spin up"). up=False: the mirror image, moment down."""
    sign = 1 if up else -1

    rotation_ring(ax, cx, RR, ccw=up, color=BLUE)

    # the particle itself, with a soft highlight so it reads as a little ball
    ax.add_patch(Circle((cx, 0), PR, facecolor=SPHERE_FILL, edgecolor=SPHERE_EDGE,
                         linewidth=1.8, zorder=3))
    ax.add_patch(Ellipse((cx - 0.16, 0.18), 0.32, 0.20, angle=25,
                          facecolor="white", edgecolor="none", alpha=0.45, zorder=4))

    # the magnetic moment: along the rotation axis, out through the pole
    ax.annotate("", xy=(cx, sign * TIP), xytext=(cx, 0),
                arrowprops=dict(arrowstyle="-|>", color=RED, lw=2.8,
                                 mutation_scale=20), zorder=6)

    # labels, on a shared baseline so the two cards read as a matched pair
    ax.text(cx, -1.55, word, ha="center", va="top", fontsize=15,
            color=TEXT, fontweight="bold")
    ax.text(cx, -1.90, math_label, ha="center", va="top", fontsize=14, color=RED)


fig, ax = plt.subplots(figsize=(8, 5))

draw_spin(ax, -1.9, True, "spin up", r"$s_i = +1$")
draw_spin(ax, 1.9, False, "spin down", r"$s_i = -1$")

ax.set_xlim(-3.3, 3.3)
ax.set_ylim(-2.25, 1.65)
ax.set_aspect("equal")
ax.axis("off")

plt.tight_layout()
plt.savefig("assets/high-bias-low-variance/spin-up-spin-down.png",
            dpi=150, bbox_inches="tight", facecolor="white")
plt.close()
print("saved assets/high-bias-low-variance/spin-up-spin-down.png")
