import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

fig, ax = plt.subplots(figsize=(10, 6.5))

# Layout: two paths from "Data" on the left to "Similarity" on the right
# Path 1 (top):    Data -> Feature map Phi(x) -> Inner product -> Similarity
# Path 2 (bottom): Data -> Kernel K(x,x')                     -> Similarity

# Box positions (center_x, center_y, width, height)
boxes = {
    'data':       (0.5, 0.5, 1.6, 0.6),
    'feature':    (3.5, 1.1, 2.2, 0.5),
    'inner':      (6.8, 1.1, 2.2, 0.5),
    'kernel':     (5.15, -0.1, 2.2, 0.5),
    'similarity': (9.5, 0.5, 1.8, 0.6),
}

box_labels = {
    'data':       'Data\n$(x, x\')$',
    'feature':    'Feature map\n$\\Phi(x), \\Phi(x\')$',
    'inner':      'Inner product\n$\\Phi(x) \\cdot \\Phi(x\')$',
    'kernel':     'Kernel\n$K(x, x\')$',
    'similarity': 'Similarity\nscore',
}

box_colors = {
    'data':       '#E8F0FE',
    'feature':    '#FFF3E0',
    'inner':      '#FFF3E0',
    'kernel':     '#E8F5E9',
    'similarity': '#E8F0FE',
}

edge_colors = {
    'data':       '#4A90D9',
    'feature':    '#E67E22',
    'inner':      '#E67E22',
    'kernel':     '#27AE60',
    'similarity': '#4A90D9',
}

# Draw boxes
for key, (cx, cy, w, h) in boxes.items():
    rect = mpatches.FancyBboxPatch(
        (cx - w/2, cy - h/2), w, h,
        boxstyle='round,pad=0.08',
        facecolor=box_colors[key],
        edgecolor=edge_colors[key],
        linewidth=1.8,
        zorder=2
    )
    ax.add_patch(rect)
    ax.text(cx, cy, box_labels[key], ha='center', va='center',
            fontsize=11, color='#333333', zorder=3)

# Arrow style
arrow_props_top = dict(
    arrowstyle='->', color='#E67E22', linewidth=1.8,
    connectionstyle='arc3,rad=0.0'
)
arrow_props_bottom = dict(
    arrowstyle='->', color='#27AE60', linewidth=1.8,
    connectionstyle='arc3,rad=0.0'
)
arrow_props_equiv = dict(
    arrowstyle='<->', color='#888888', linewidth=1.5,
    connectionstyle='arc3,rad=0.0',
    linestyle='dashed'
)

# Top path arrows: Data -> Feature map -> Inner product -> Similarity
ax.annotate('', xy=(2.4, 1.1), xytext=(1.3, 0.75),
            arrowprops=arrow_props_top)
ax.annotate('', xy=(5.7, 1.1), xytext=(4.6, 1.1),
            arrowprops=arrow_props_top)
ax.annotate('', xy=(8.6, 0.75), xytext=(7.9, 1.1),
            arrowprops=arrow_props_top)

# Bottom path arrows: Data -> Kernel -> Similarity
ax.annotate('', xy=(4.04, 0.0), xytext=(1.3, 0.25),
            arrowprops=arrow_props_bottom)
ax.annotate('', xy=(8.6, 0.25), xytext=(6.26, 0.0),
            arrowprops=arrow_props_bottom)

# Equivalence arrow between feature map path and kernel
ax.annotate('', xy=(5.15, 0.83), xytext=(5.15, 0.17),
            arrowprops=arrow_props_equiv)
ax.text(5.75, 0.50, 'equivalent', ha='left', va='center',
        fontsize=10, color='#888888', fontstyle='italic')

# Path labels
ax.text(1.85, 1.55, 'Path 1: explicit features', fontsize=9,
        color='#E67E22', fontstyle='italic')
ax.text(2.5, -0.48, 'Path 2: kernel trick', fontsize=9,
        color='#27AE60', fontstyle='italic')

ax.set_xlim(-0.3, 10.8)
ax.set_ylim(-0.5, 1.5)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()
plt.savefig('assets/neural-tangent-kernel/feature-kernel-duality.png',
            dpi=150, bbox_inches='tight', facecolor='white')
plt.show()
