"""
Class-conditional feature distributions from the SUSY data set (Baldi,
Sadowski, and Whiteson 2014), standing in for "[Image of SUSY dataset]" in
the Mehta review. SUSY events aren't pictures -- each one is an
18-dimensional vector of kinematic and derived features -- so the natural
"picture" of the data set is how those features are distributed, signal
against background.

Two of the 8 low-level features (read directly off the simulated detector)
and two of the 10 high-level features (functions of the low-level ones,
hand-engineered by physicists to target the supersymmetric-decay signature)
are shown here:

    low-level:  lepton 1 pT, missing energy magnitude
    high-level: M_TR_2, M_Delta_R

None of the four cleanly separates the classes with a hard cut -- that's
the point the surrounding prose makes about this being a subtle task, not
a trivial one. Signal sits at systematically higher values in every
low-level panel too, so the low/high split isn't "no signal vs. all the
signal" -- it's a difference of degree. M_Delta_R (bottom right) is the
clearest example of what hand-engineering bought here: background keeps
the same peaked-and-decaying shape it has elsewhere, but signal goes
nearly flat across a wide range, which is a harder pattern to get from a
single low-level feature.

Data: N_SAMPLE rows read off the head of the UCI SUSY.csv.gz stream
(https://archive.ics.uci.edu/dataset/279/susy; 5,000,000 rows, 19 columns
total, no missing values). The gzip HTTP response is decompressed on the
fly and handed to pandas with nrows=N_SAMPLE, so only the compressed bytes
covering that many rows are ever pulled over the wire -- tens of MB, not
the full ~880 MB file. The data is otherwise unshuffled from its source
order, which is already effectively random with respect to class (the UCI
page notes the *last* 500,000 rows are reserved as a test split, which
only makes sense if class doesn't correlate with row order); the class
balance printed below confirms the head of the file is not, e.g., all
background followed by all signal.

Column order -- class label, then the 8 low-level features, then the 10
high-level features, in the order below -- is copied verbatim from the
"Additional Variable Information" section of the UCI dataset page. The
sample is cached locally after the first run so reruns don't re-download.

Output: assets/high-bias-low-variance/susy-features.png
Cache:  assets/high-bias-low-variance/susy-sample.npz
"""
import gzip
import os
import sys
import urllib.request

import numpy as np
import matplotlib.pyplot as plt

N_SAMPLE = 100_000
SUSY_URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/00279/SUSY.csv.gz"
CACHE_PATH = "assets/high-bias-low-variance/susy-sample.npz"

# Class label, then 8 low-level features, then 10 high-level features --
# verbatim order from the UCI SUSY "Additional Variable Information".
COLUMNS = [
    "class",
    "lepton1_pT", "lepton1_eta", "lepton1_phi",
    "lepton2_pT", "lepton2_eta", "lepton2_phi",
    "missing_energy_magnitude", "missing_energy_phi",
    "MET_rel", "axial_MET", "M_R", "M_TR_2", "R", "MT2", "S_R",
    "M_Delta_R", "dPhi_r_b", "cos_theta_r1",
]
COL = {name: i for i, name in enumerate(COLUMNS)}


def download_sample(n_rows, attempts=3):
    """Stream the first n_rows rows of SUSY.csv.gz: decompress the HTTP
    response on the fly and let pandas' C parser stop after n_rows lines,
    so only the compressed bytes covering that prefix of the ~880 MB file
    are ever downloaded."""
    import pandas as pd

    last_err = None
    for attempt in range(1, attempts + 1):
        try:
            print(f"Downloading first {n_rows:,} rows of SUSY.csv.gz from "
                  f"UCI (attempt {attempt}/{attempts})...")
            response = urllib.request.urlopen(SUSY_URL, timeout=120)
            with gzip.GzipFile(fileobj=response) as gz:
                df = pd.read_csv(gz, header=None, nrows=n_rows)
            if df.shape[1] != len(COLUMNS):
                raise ValueError(
                    f"expected {len(COLUMNS)} columns, got {df.shape[1]}")
            return df.to_numpy(dtype=np.float32)
        except Exception as exc:  # retry on anything; report the last failure
            last_err = exc
            print(f"  attempt {attempt} failed: {exc!r}")
    raise RuntimeError(
        f"Could not download the SUSY data set from {SUSY_URL} after "
        f"{attempts} attempts. Refusing to fabricate substitute data. "
        f"Last error: {last_err!r}"
    )


if os.path.exists(CACHE_PATH):
    data = np.load(CACHE_PATH)["data"]
    print(f"Loaded cached SUSY sample from {CACHE_PATH}: {data.shape}")
else:
    try:
        data = download_sample(N_SAMPLE)
    except RuntimeError as exc:
        print(f"FATAL: {exc}", file=sys.stderr)
        sys.exit(1)
    os.makedirs(os.path.dirname(CACHE_PATH), exist_ok=True)
    np.savez_compressed(CACHE_PATH, data=data)
    print(f"Cached SUSY sample to {CACHE_PATH}: {data.shape}")

labels = data[:, COL["class"]]
is_signal = labels == 1
is_bkg = labels == 0
print(f"n = {len(labels):,}   signal = {is_signal.sum():,} "
      f"({is_signal.mean():.1%})   background = {is_bkg.sum():,} "
      f"({is_bkg.mean():.1%})")

BLUE, RED = "#1f77b4", "#d62728"  # background, signal


def clipped_bins(x, lo_pct=0.5, hi_pct=99.5, n_bins=60):
    """Percentile-based clip so a handful of extreme-tail events (this is
    collider data; tails run long) don't compress the interesting bulk of
    the distribution into a few pixels."""
    lo, hi = np.percentile(x, [lo_pct, hi_pct])
    return lo, hi, np.linspace(lo, hi, n_bins + 1)


# (column, panel title, x-axis label, low-level/high-level)
PANELS = [
    ("lepton1_pT", "Lepton 1 $p_T$", "$p_T$ (lepton 1)", "low-level"),
    ("missing_energy_magnitude", "Missing energy magnitude",
     r"$E_T^{\rm miss}$", "low-level"),
    ("M_TR_2", "$M_{TR2}$", "$M_{TR2}$", "high-level"),
    ("M_Delta_R", r"$M_{\Delta R}$", r"$M_{\Delta R}$", "high-level"),
]

fig, axes = plt.subplots(2, 2, figsize=(11, 8.5))

for ax, (col, title, xlabel, level) in zip(axes.flat, PANELS):
    x = data[:, COL[col]]
    lo, hi, bins = clipped_bins(x)

    ax.hist(x[is_bkg], bins=bins, density=True, histtype="stepfilled",
            color=BLUE, alpha=0.55, edgecolor=BLUE, linewidth=1.1,
            label="Background")
    ax.hist(x[is_signal], bins=bins, density=True, histtype="stepfilled",
            color=RED, alpha=0.55, edgecolor=RED, linewidth=1.1,
            label="Signal")

    ax.set_xlim(lo, hi)
    ax.set_xlabel(xlabel, fontsize=13)
    ax.set_ylabel("Density", fontsize=13)
    ax.set_title(f"{title} ({level} feature)", fontsize=13.5)
    ax.legend(fontsize=10, loc="upper right", framealpha=0.9)
    ax.grid(True, alpha=0.3)
    print(f"  {col:26s} clipped to [{lo:.3g}, {hi:.3g}]")

fig.suptitle(
    "SUSY events: signal (supersymmetric) vs. background across "
    "low-level and high-level features",
    fontsize=14.5, y=1.0,
)

plt.tight_layout()
plt.savefig("assets/high-bias-low-variance/susy-features.png",
            dpi=150, bbox_inches="tight")
plt.close()
print("saved assets/high-bias-low-variance/susy-features.png")
