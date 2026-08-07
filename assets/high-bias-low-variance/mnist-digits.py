"""
One example of each MNIST digit, 0 through 9.

MNIST is the first of the three data sets that recur throughout Mehta et
al.'s notes -- used both for unsupervised tasks (clustering, dimensionality
reduction) and for the standard supervised task, digit classification. This
figure is just an establishing shot of the raw data itself: 70,000 images
of handwritten digits, each a 28x28 grayscale array.

Data: sklearn.datasets.fetch_openml('mnist_784', ...), version=1 -- the
standard OpenML mirror of the full 70,000-image MNIST set (the original
60k-train/10k-test split, combined into one array). Each row is a
flattened 784 = 28x28 image with pixel values in [0, 255]. The first call
downloads ~15 MB and sklearn caches it to disk under ~/scikit_learn_data,
so subsequent runs are fast. If OpenML is unreachable, we fall back to
downloading and parsing the raw IDX files directly (the same files LeCun's
original site pointed to; now mirrored on S3).

One example per digit is drawn with a seeded RNG choosing among all
instances of that digit in the data set, so the selection is reproducible
across runs.

Output: assets/high-bias-low-variance/mnist-digits.png
"""
import gzip
import os
import urllib.request

import numpy as np
import matplotlib.pyplot as plt

SEED = 42
IDX_BASE_URL = "https://ossci-datasets.s3.amazonaws.com/mnist/"


def _load_mnist_idx():
    """Fallback: download and parse the raw IDX files (60,000 training
    images), used only if fetch_openml can't reach OpenML."""
    cache_dir = os.path.join(os.path.expanduser("~"), ".cache", "mnist_idx")
    os.makedirs(cache_dir, exist_ok=True)

    def fetch(name):
        path = os.path.join(cache_dir, name)
        if not os.path.exists(path):
            urllib.request.urlretrieve(IDX_BASE_URL + name, path)
        return path

    images_path = fetch("train-images-idx3-ubyte.gz")
    labels_path = fetch("train-labels-idx1-ubyte.gz")

    with gzip.open(images_path, "rb") as f:
        f.read(16)  # magic, n_images, n_rows, n_cols
        images = np.frombuffer(f.read(), dtype=np.uint8).reshape(-1, 784)
    with gzip.open(labels_path, "rb") as f:
        f.read(8)  # magic, n_labels
        labels = np.frombuffer(f.read(), dtype=np.uint8).astype(int)

    return images, labels


def load_mnist():
    try:
        from sklearn.datasets import fetch_openml
        print("Fetching MNIST from OpenML (cached locally after first run)...")
        X, y = fetch_openml("mnist_784", version=1, as_frame=False,
                             return_X_y=True, parser="auto")
        return X.astype(np.uint8), y.astype(int)
    except Exception as exc:
        print(f"OpenML fetch failed ({exc!r}); falling back to raw IDX files.")
        return _load_mnist_idx()


X, y = load_mnist()

# One example per digit, chosen with a seeded RNG among all matching rows.
rng = np.random.default_rng(SEED)
examples = []
chosen_indices = []
for digit in range(10):
    candidates = np.flatnonzero(y == digit)
    choice = rng.choice(candidates)
    chosen_indices.append(int(choice))
    examples.append(X[choice].reshape(28, 28))

fig, axes = plt.subplots(2, 5, figsize=(10, 4.4))
for digit, (ax, img) in enumerate(zip(axes.flat, examples)):
    ax.imshow(img, cmap="gray_r", interpolation="nearest")
    ax.set_title(f"${digit}$", fontsize=14)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_aspect("equal")

fig.suptitle("One example of each MNIST digit", fontsize=15, y=0.99)
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig("assets/high-bias-low-variance/mnist-digits.png", dpi=150,
            bbox_inches="tight")
plt.close()

print("saved assets/high-bias-low-variance/mnist-digits.png")
print(f"seed={SEED}, chosen row index per digit 0-9: {chosen_indices}")
