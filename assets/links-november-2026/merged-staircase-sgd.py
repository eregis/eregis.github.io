"""
The merged staircase: online SGD learns z1 + z1 z2 + z1 z2 z3 one coordinate at a
time, and is still stuck on z1 z2 z3 alone when the first has long since finished.

Setting (Abbe, Boix-Adsera & Misiakiewicz 2022, "The merged-staircase property",
arXiv 2202.08658): inputs x uniform on {+-1}^d, a two-layer network trained by
online SGD in the mean-field scaling, targets that depend on only the first 3
coordinates z = (x_1, x_2, x_3). Two targets with the same degree and support:

    h2(z) = z1 + z1 z2 + z1 z2 z3     (merged staircase: each monomial adds ONE new coordinate)
    h1(z) = z1 z2 z3                  (leap 3: three new coordinates at once)

Model and training
  - f(x) = (1/N) sum_i a_i softplus(w_i . x + b_i), N = 500 neurons, d = 100 inputs
    (97 of them irrelevant to both targets).
  - Squared loss 0.5 (f - y)^2. Every step draws a fresh batch of 16 inputs
    (online SGD: no sample is ever reused), and takes one plain SGD step on all of
    (a, W, b) jointly. Mean-field scaling: the 1/N in f is cancelled by using the
    per-neuron step size LR (not LR / N) in the update, so each neuron moves O(1)
    over O(1/LR) steps regardless of N.
  - Init: a_i ~ N(0, 1), b_i ~ N(0, 1), w_i ~ N(0, W_INIT^2 / d) per coordinate with
    W_INIT = 0.1 (so ||w_i|| ~ 0.1: weights start small and the network is not in the
    lazy regime). Same init seed and hyperparameters for both targets.
  - Tracked quantity: the Fourier-Walsh coefficient fhat(S) = E_x[f(x) chi_S(x)],
    chi_S = prod_{i in S} x_i, for S = {1}, {1,2}, {1,2,3}, estimated on a fixed
    held-out batch of 5000 inputs (standard error about 0.014), every 100 steps.
    Targets: h2 has fhat = 1 on all three; h1 has fhat({1,2,3}) = 1 and 0 on the
    other two.

Result (seed 0, d = 100, budget 20000 steps = 320000 samples)
  h2: the coefficients cross 0.5 in the order {1}, {1,2}, {1,2,3} (printed below),
  each plateau being the time the next monomial waits on the previous one.
  h1: fhat({1,2,3}) stays at noise level for the entire budget.
  Longer run for h1 (one-off, seed 0, not part of this script): fhat({1,2,3}) first
  crosses 0.5 at step 124000 for d = 100 (about 18x the 6800 steps h2 needs to get
  there, and 6x this figure's budget) and at 80000 for d = 30. So h1 does
  escape, much later, and that escape time is noisy and grows only weakly with d
  between these two (one seed each): this experiment does NOT demonstrate the
  d^2-type scaling, only the gap between the two targets.

What was tuned (exploratory runs; d = 30-300, N = 200-500, B = 16-256, 1-3 seeds)
  - Activation. This is the main knob, and it is a deviation from the paper (see
    below). Whether h1 stays stuck depends strongly on it:
      * ReLU (b ~ N(0,1)): h2 shows a clean staircase, but h1 escapes at 9000 /
        11500 / 15000 steps for d = 50 / 100 / 200, barely later than h2 finishes
        (about 7000-8500). The kink at 0 gives neurons with |w.x + b| small a
        gradient that does not need the small product w_2 w_3 to break symmetry.
        Not a usable contrast.
      * tanh: h1 time scales close to linearly in d (4500 / 11500 / 29000 for
        d = 30 / 100 / 300 at LR = 0.01), but the {1,2} and {1,2,3} coefficients of h2
        rise together (both cross 0.5 at the same step), so there are no stairs.
      * sigmoid: same merging as tanh.
      * softplus (used): clean three-step staircase for h2 and h1 stuck for 60000
        steps at both d = 50 and d = 100 (max |fhat({1,2,3})| = 0.002).
  - W_INIT. With ReLU/tanh, W_INIT from 0.3 down to 0.05 changed the h1 escape time
    by only ~1.2x, because SGD noise (not the init) sets the size of the
    w_2, w_3 products that seed the escape. (Not re-tested with softplus.) 0.1 was kept.
  - LR. LR = 0.003 stretches the stairs over thousands of steps so the three
    plateaus can be resolved; at LR = 0.01 the same staircase is present but compressed
    into ~2500 steps. The budget is 20000 steps, about 2x the time h2 needs to reach
    fhat > 0.8 on all three coefficients.
  - d. d = 100 rather than 30: h1 is stuck for longer (124000 vs 80000 steps) at the
    same per-step cost. d = 300 was not needed.

Robustness: seeds 1 and 2 (also 3, in an earlier run: same picture) (init, SGD noise, held-out batch all re-drawn) are re-run
below with the same hyperparameters; the ordering of the h2 crossings and the stuck
h1 coefficient are checked on each and printed. The figure shows seed 0 only,
which was fixed before any seed comparison.

Deviations from the paper's exact setting
  - Activation: softplus, chosen empirically (see above); I did not check it against the
    paper's assumptions on the activation, and I did not try to reproduce the paper's
    scaling of step size and init with d.
  - Joint training of all three layers' parameters (a, W, b), constant step size, no
    layerwise or projected scheme, no step-size schedule, no weight decay.
  - Biases are trained, with init b ~ N(0, 1).
  - Mini-batches of 16 instead of single samples; fixed N = 500 and d = 100 rather than
    the N, d -> infinity limit. The theory predicts the time-scales in d, so I
    only claim the qualitative picture here: h2 finishes in a few thousand steps at
    d = 100, and h1 is stuck over a budget a few times longer.
  - The stairs are soft, not sharp: the neurons are in different stages at any time,
    and fhat({1}) overshoots 1 on the way before settling back to 1.

Run from the repository root (about 3 minutes: two targets x three seeds).
Output: assets/links-november-2026/merged-staircase-sgd.png
"""
import time
import numpy as np
import matplotlib.pyplot as plt

SEED = 0
CHECK_SEEDS = [1, 2]

# --- Experiment settings ---
D = 100            # input dimension (only the first 3 coordinates matter)
N = 500            # neurons
BATCH = 16         # fresh samples per SGD step
LR = 0.003         # per-neuron step size (mean-field scaling: not divided by N)
W_INIT = 0.1       # ||w_i|| at init
B_INIT = 1.0       # std of biases at init
STEPS = 20000      # shared budget
EVAL_EVERY = 100
N_EVAL = 5000      # held-out inputs for fhat and test MSE
THRESH = 0.5       # crossing level for the h2 stairs
STUCK_MAX = 0.2    # h1 must stay below this


def h2(X):
    return X[:, 0] + X[:, 0] * X[:, 1] + X[:, 0] * X[:, 1] * X[:, 2]


def h1(X):
    return X[:, 0] * X[:, 1] * X[:, 2]


def softplus(u):
    return np.logaddexp(0.0, u)


def sigmoid(u):
    return 1.0 / (1.0 + np.exp(-u))


def train(target, seed):
    """Online SGD from the seeded init. Returns steps, fhat (3 columns) and test MSE
    at every EVAL_EVERY steps."""
    rng = np.random.default_rng(seed)
    W = rng.standard_normal((N, D)) * W_INIT / np.sqrt(D)
    b = rng.standard_normal(N) * B_INIT
    a = rng.standard_normal(N)
    X_ev = rng.choice([-1.0, 1.0], size=(N_EVAL, D))
    y_ev = target(X_ev)
    chi = np.stack([X_ev[:, 0], X_ev[:, 0] * X_ev[:, 1],
                    X_ev[:, 0] * X_ev[:, 1] * X_ev[:, 2]], axis=1)   # N_EVAL x 3

    steps, fhat, mse = [], [], []
    for t in range(STEPS + 1):
        if t % EVAL_EVERY == 0:
            f = softplus(X_ev @ W.T + b) @ a / N
            steps.append(t)
            fhat.append(chi.T @ f / N_EVAL)
            mse.append(np.mean((f - y_ev) ** 2))
        X = rng.choice([-1.0, 1.0], size=(BATCH, D))
        U = X @ W.T + b                      # BATCH x N
        S = softplus(U)
        r = (S @ a / N - target(X))[:, None]   # residual, BATCH x 1
        G = r * sigmoid(U) * a                 # d loss / d preactivation, times N
        a -= LR * (r * S).mean(axis=0)
        W -= LR * G.T @ X / BATCH
        b -= LR * G.mean(axis=0)
    return np.array(steps), np.array(fhat), np.array(mse)


def first_cross(steps, y, level):
    idx = np.flatnonzero(y > level)
    return int(steps[idx[0]]) if len(idx) else None


t0 = time.time()
steps, f2, mse2 = train(h2, SEED)
_, f1, mse1 = train(h1, SEED)

# --- Figure ---
COLORS = ['#1f77b4', '#ff7f0e', '#d62728']
LABELS = [r'$\hat f(\{1\})$', r'$\hat f(\{1,2\})$', r'$\hat f(\{1,2,3\})$']

fig, axes = plt.subplots(1, 2, figsize=(14, 5.5), sharey=True)
for ax, F, title in [
    (axes[0], f2, r'$h_2 = z_1 + z_1 z_2 + z_1 z_2 z_3$  (merged staircase)'),
    (axes[1], f1, r'$h_1 = z_1 z_2 z_3$  (no staircase)'),
]:
    for j in range(3):
        ax.plot(steps, F[:, j], color=COLORS[j], linewidth=2.4, label=LABELS[j])
    ax.axhline(1.0, color='0.35', linestyle='--', linewidth=1.5, zorder=1)
    ax.set_xlim(0, STEPS)
    ax.set_ylim(-0.15, 1.35)
    ax.set_xlabel('SGD steps (fresh batch of %d samples per step)' % BATCH, fontsize=13)
    ax.set_title(title, fontsize=14)
    ax.grid(True, alpha=0.3)
axes[0].set_ylabel(r'Learned Fourier coefficient $\hat f(S)$', fontsize=13)
axes[0].legend(fontsize=11, loc='lower right', framealpha=0.9)

fig.suptitle(rf'Online SGD on a mean-field two-layer network ($d = {D}$, $N = {N}$ neurons)',
             fontsize=15, y=1.02)
plt.tight_layout()
plt.savefig('assets/links-november-2026/merged-staircase-sgd.png',
            dpi=150, bbox_inches='tight')

# --- Summary / checks ---
def report(tag, steps, f2, f1, mse2, mse1):
    cross = [first_cross(steps, f2[:, j], THRESH) for j in range(3)]
    stuck = np.abs(f1[:, 2]).max()
    print(f"[{tag}] h2: first step with fhat > {THRESH}: "
          f"{{1}} = {cross[0]}, {{1,2}} = {cross[1]}, {{1,2,3}} = {cross[2]}")
    print(f"[{tag}] h1: max |fhat({{1,2,3}})| over {STEPS} steps = {stuck:.3f} "
          f"(threshold {STUCK_MAX}); final fhat({{1}}), fhat({{1,2}}) = "
          f"{f1[-1, 0]:.3f}, {f1[-1, 1]:.3f}")
    print(f"[{tag}] final test MSE: h2 = {mse2[-1]:.4f}, h1 = {mse1[-1]:.4f} "
          f"(h1 predicting 0 would give 1.0)")
    assert None not in cross and cross[0] < cross[1] < cross[2], f"{tag}: stairs out of order {cross}"
    assert stuck < STUCK_MAX, f"{tag}: h1 escaped (max {stuck:.3f})"

print(f"d = {D}, N = {N}, batch = {BATCH}, lr = {LR}, budget = {STEPS} steps "
      f"({STEPS * BATCH} samples)")
report(f"seed {SEED}", steps, f2, f1, mse2, mse1)
for s in CHECK_SEEDS:
    _, g2, m2 = train(h2, s)
    _, g1, m1 = train(h1, s)
    report(f"seed {s}", steps, g2, g1, m2, m1)
print(f"runtime: {time.time() - t0:.0f} s")
