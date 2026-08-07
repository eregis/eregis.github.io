"""
The moving average as a box-filter convolution.

Mehta's example for what a convolution "does": with f(t) the value of a
noisy time series and

    g(t) = (1 / 2c) * Theta(c - |t|)

the box function of half-width c, the convolution (f * g)(t) is exactly the
average of f over the sliding window [t - c, t + c]. This script builds a
synthetic "stock price" f(t) -- a slow random-walk trend plus per-step noise,
in the spirit of the classic random-walk-plus-noise model of asset prices --
and convolves it with two box filters, a narrow one and a wide one, to make
visible the sentence Mehta states in words: widen the box and you smooth
more aggressively; narrow it and you keep more of the fluctuation.

Boundary handling: the box filter is implemented as convolution with a
reflect-padded copy of the series (mode='valid' on the padded array), rather
than plain 'same'-mode convolution. Plain 'same' mode implicitly zero-pads
the series, which drags the moving average toward zero over the last c
points at each end -- a visible dip/spike that has nothing to do with the
data. Reflecting the series before convolving keeps the boundary behavior
sensible (and the output the same length as the input) without that artifact.

Output: assets/high-bias-low-variance/moving-average-convolution.png
"""
import numpy as np
import matplotlib.pyplot as plt

SEED = 7
rng = np.random.default_rng(SEED)

N = 500            # trading days (~2 years)
START = 100.0      # starting price
DRIFT = 0.04       # mean daily change in the underlying trend
TREND_STD = 0.35   # random-walk step size of the underlying trend
NOISE_STD = 1.6    # per-step noise layered on top (e.g. market microstructure)

WINDOW_NARROW = 11  # c = 5
WINDOW_WIDE = 51    # c = 25


def box_filter_average(f, window):
    """Convolve f with a normalized box kernel of the given (odd) width.
    The series is reflect-padded before convolving so the output covers the
    full length of f with no zero-padding artifacts at the boundary."""
    assert window % 2 == 1, "use an odd window so the kernel is centered"
    kernel = np.ones(window) / window
    pad = window // 2
    padded = np.pad(f, pad, mode="reflect")
    return np.convolve(padded, kernel, mode="valid")


t = np.arange(N)
trend = START + np.cumsum(rng.normal(DRIFT, TREND_STD, size=N))
noise = rng.normal(0.0, NOISE_STD, size=N)
price = trend + noise

ma_narrow = box_filter_average(price, WINDOW_NARROW)
ma_wide = box_filter_average(price, WINDOW_WIDE)

fig, ax = plt.subplots(figsize=(10, 5.5))

ax.plot(t, price, color="0.65", linewidth=0.9, alpha=0.9, zorder=1,
        label="Raw series $f(t)$")
ax.plot(t, ma_narrow, color="#1f77b4", linewidth=2.0, zorder=3,
        label=f"Narrow window ({WINDOW_NARROW} days)")
ax.plot(t, ma_wide, color="#d62728", linewidth=2.4, zorder=4,
        label=f"Wide window ({WINDOW_WIDE} days)")

ax.set_xlabel("$t$ (trading day)", fontsize=13)
ax.set_ylabel("$f(t)$ (price)", fontsize=13)
ax.set_title("Widen the box filter and you smooth more aggressively", fontsize=14)
ax.legend(fontsize=10.5, loc="upper left", framealpha=0.9)
ax.grid(True, alpha=0.3)
ax.set_xlim(t[0], t[-1])

# Extra headroom above the data so the legend box never crowds the series.
y_min = min(price.min(), ma_narrow.min(), ma_wide.min())
y_max = max(price.max(), ma_narrow.max(), ma_wide.max())
span = y_max - y_min
ax.set_ylim(y_min - 0.08 * span, y_max + 0.35 * span)

plt.tight_layout()
plt.savefig("assets/high-bias-low-variance/moving-average-convolution.png",
            dpi=150, bbox_inches="tight")

print(f"price range: [{price.min():.2f}, {price.max():.2f}]")
print(f"narrow MA range: [{ma_narrow.min():.2f}, {ma_narrow.max():.2f}]")
print(f"wide MA range: [{ma_wide.min():.2f}, {ma_wide.max():.2f}]")
