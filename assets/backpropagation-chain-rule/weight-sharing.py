import matplotlib.pyplot as plt

# one inch per data unit, matching computational-graph.png
XLIM, YLIM = (-2.6, 8.7), (-5.0, 1.9)
fig, ax = plt.subplots(figsize=(XLIM[1] - XLIM[0], YLIM[1] - YLIM[0]))

node_radius = 0.13

# --- palette (shared with diagonal-network.py) -------------------------------
PARAM_FILL, PARAM_RIM = '#4A90D9', '#2C5F8A'   # parameters: the shared weight w
DATA_FILL, DATA_RIM = '#DDDDDD', '#888888'     # data: x1, x2, y
COMP_FILL, COMP_RIM = '#F2C14E', '#A67C00'     # computed: h1, h2, f, L
FWD_COLOR = '#444444'
BWD_COLOR = '#B03A2E'
LABEL_COLOR = '#333333'

C0, C1, C2, C3 = 0.0, 2.5, 5.0, 7.5
DY = 0.95                    # vertical offset of the two branches
Y_F, Y_B = 0.0, -3.4         # centre lines of the forward and backward rows
LABEL_OFFSET = 0.3


def node(x, y, fill, rim):
    ax.add_patch(plt.Circle((x, y), node_radius, color=fill, ec=rim,
                            linewidth=1.5, zorder=4))


def arrow(start, end, color, lw):
    ax.annotate('', xy=end, xytext=start,
                arrowprops=dict(arrowstyle='-|>', color=color, lw=lw,
                                shrinkA=14, shrinkB=14), zorder=2)


def label(x, y, s, va, color=LABEL_COLOR, size=13, ha='center'):
    ax.text(x, y, s, ha=ha, va=va, fontsize=size, color=color, zorder=5)


# --- forward row: one weight feeds two products --------------------------------
F = {'x1': (C0, Y_F + DY), 'w': (C0, Y_F), 'x2': (C0, Y_F - DY),
     'h1': (C1, Y_F + DY), 'h2': (C1, Y_F - DY),
     'f': (C2, Y_F), 'L': (C3, Y_F), 'y': (C3, Y_F + 1.25)}
style = {'x1': (DATA_FILL, DATA_RIM), 'w': (PARAM_FILL, PARAM_RIM),
         'x2': (DATA_FILL, DATA_RIM), 'h1': (COMP_FILL, COMP_RIM),
         'h2': (COMP_FILL, COMP_RIM), 'f': (COMP_FILL, COMP_RIM),
         'L': (COMP_FILL, COMP_RIM), 'y': (DATA_FILL, DATA_RIM)}

for a, b in [('x1', 'h1'), ('w', 'h1'), ('w', 'h2'), ('x2', 'h2'),
             ('h1', 'f'), ('h2', 'f'), ('f', 'L'), ('y', 'L')]:
    arrow(F[a], F[b], FWD_COLOR, 1.8)
for key, (fill, rim) in style.items():
    node(*F[key], fill, rim)

for key, s in [('x1', r'$x_1$'), ('w', r'$w$'), ('x2', r'$x_2$')]:
    label(F[key][0] - 0.28, F[key][1], s, 'center', ha='right')
label(F['h1'][0], F['h1'][1] + LABEL_OFFSET, r'$h_1 = w x_1$', 'bottom')
label(F['h2'][0], F['h2'][1] - LABEL_OFFSET, r'$h_2 = w x_2$', 'top')
label(F['f'][0], F['f'][1] - LABEL_OFFSET, r'$f = h_1 + h_2$', 'top')
label(F['L'][0], F['L'][1] - LABEL_OFFSET, r'$L = \frac{1}{2}(f - y)^2$', 'top')
label(F['y'][0], F['y'][1] + LABEL_OFFSET, r'$y$', 'bottom')

# --- backward row: the two branches converge on w and add ----------------------
B = {'w': (C0, Y_B), 'h1': (C1, Y_B + DY), 'h2': (C1, Y_B - DY),
     'f': (C2, Y_B), 'L': (C3, Y_B)}

for a, b, s, dx, dy, ha in [
        ('L', 'f', r'$\times\,(f - y)$', 0.0, 0.22, 'center'),
        ('f', 'h1', r'$\times\, 1$', 0.15, 0.12, 'left'),
        ('f', 'h2', r'$\times\, 1$', 0.15, -0.12, 'left'),
        ('h1', 'w', r'$\times\, x_1$', -0.15, 0.12, 'right'),
        ('h2', 'w', r'$\times\, x_2$', -0.15, -0.12, 'right')]:
    arrow(B[a], B[b], BWD_COLOR, 2.0)
    mx, my = (B[a][0] + B[b][0]) / 2, (B[a][1] + B[b][1]) / 2
    label(mx + dx, my + dy, s, 'center', BWD_COLOR, 12, ha=ha)
for key in B:
    node(*B[key], *style[key])   # nodes keep their forward-pass role colors

label(B['L'][0], B['L'][1] - LABEL_OFFSET, r'$\partial L/\partial L = 1$', 'top', size=12)
label(B['f'][0], B['f'][1] - LABEL_OFFSET, r'$\partial L/\partial f = f - y$', 'top', size=12)
label(B['h1'][0], B['h1'][1] + LABEL_OFFSET, r'$\partial L/\partial h_1 = f - y$',
      'bottom', size=12)
label(B['h2'][0], B['h2'][1] - LABEL_OFFSET, r'$\partial L/\partial h_2 = f - y$',
      'top', size=12)
label(B['w'][0] - 0.28, B['w'][1] + 0.14, r'$\partial L/\partial w = (f - y)\, x_1$',
      'bottom', size=12, ha='right')
label(B['w'][0] - 0.28, B['w'][1] - 0.14, r'$+\;(f - y)\, x_2$',
      'top', size=12, ha='right')

ax.set_xlim(*XLIM)
ax.set_ylim(*YLIM)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()
plt.savefig('assets/backpropagation-chain-rule/weight-sharing.png',
            dpi=150, bbox_inches='tight', facecolor='white')
