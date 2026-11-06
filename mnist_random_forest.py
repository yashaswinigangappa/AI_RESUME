# MNIST Random Forest Classification Demo
# This script downloads the MNIST dataset, visualises samples, trains a RandomForest
# classifier using scikit‑learn, evaluates it, and provides interactive visualisations.

# @title Imports and dataset download
#@param {type:"string"} data_url="https://storage.googleapis.com/tensorflow/tf-keras-datasets/mnist.npz"

import os
import urllib.request
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, ConfusionMatrixDisplay

# Ensure reproducibility
RANDOM_STATE = 42

# ---------------------------------------------------------------------------
# 1. Download the .npz file (if not already present)
# ---------------------------------------------------------------------------
cache_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), "data")
os.makedirs(cache_dir, exist_ok=True)
npz_path = os.path.join(cache_dir, "mnist.npz")
if not os.path.isfile(npz_path):
    print(f"Downloading MNIST dataset to {npz_path} …")
    urllib.request.urlretrieve(data_url, npz_path)
else:
    print(f"Dataset already cached at {npz_path}")

# ---------------------------------------------------------------------------
# 2. Load the dataset with NumPy
# ---------------------------------------------------------------------------
with np.load(npz_path) as f:
    x_train = f["x_train"]  # shape (60000, 28, 28)
    y_train = f["y_train"]
    x_test = f["x_test"]    # shape (10000, 28, 28)
    y_test = f["y_test"]

print("Training images:", x_train.shape[0])
print("Test images:", x_test.shape[0])

# ---------------------------------------------------------------------------
# 3. Visualise the first 10 training images (2 rows × 5 columns)
# ---------------------------------------------------------------------------
fig, axes = plt.subplots(2, 5, figsize=(10, 5))
for i, ax in enumerate(axes.flat):
    ax.imshow(x_train[i], cmap="gray")
    ax.set_title(str(y_train[i]))
    ax.axis("off")
plt.suptitle("First 10 training images")
plt.tight_layout()
plt.show()

# ---------------------------------------------------------------------------
# 4. Prepare flattened data for the RandomForest
# ---------------------------------------------------------------------------
# Take the first 10,000 training images and flatten each 28×28 image to a 784‑dim vector
X_train = x_train[:10_000].reshape(10_000, -1)
labels_train = y_train[:10_000]

# Flatten the entire test set
X_test = x_test.reshape(x_test.shape[0], -1)

print("Each picture now has", X_train.shape[1], "features (pixels).")

# ---------------------------------------------------------------------------
# 5. Train RandomForestClassifier
# ---------------------------------------------------------------------------
model = RandomForestClassifier(random_state=RANDOM_STATE, n_jobs=-1)
model.fit(X_train, labels_train)

# ---------------------------------------------------------------------------
# 6. Predict on the test set and report accuracy
# ---------------------------------------------------------------------------
guesses = model.predict(X_test)
accuracy = accuracy_score(y_test, guesses) * 100
print(f"Test accuracy: {accuracy:.2f}%")

# ---------------------------------------------------------------------------
# 7. Visualise the first 10 test images with model predictions
#    – title colour: green if correct, red if wrong
# ---------------------------------------------------------------------------
fig, axes = plt.subplots(2, 5, figsize=(10, 5))
for i, ax in enumerate(axes.flat):
    img = x_test[i]
    pred = guesses[i]
    true = y_test[i]
    correct = pred == true
    colour = "green" if correct else "red"
    ax.imshow(img, cmap="gray")
    ax.set_title(str(pred), color=colour)
    ax.axis("off")
plt.suptitle("First 10 test images – model predictions")
plt.tight_layout()
plt.show()

# ---------------------------------------------------------------------------
# 8. Confusion matrix (no colour bar, Blues colormap)
# ---------------------------------------------------------------------------
disp = ConfusionMatrixDisplay.from_predictions(y_test, guesses, cmap=plt.cm.Blues)
plt.title("Confusion Matrix – RandomForest on MNIST")
# Remove the colour bar – the display object adds one by default, so we delete it
if disp.im_.colorbar is not None:
    disp.im_.colorbar.remove()
plt.show()

# ---------------------------------------------------------------------------
# 9. Interactive Colab widget: slider to inspect any test image
# ---------------------------------------------------------------------------
#@title Interactive inspection (Colab only) { display-mode: "form" }
#@param {type:"slider", min:0, max:9999, step:1} image_number = 0

img = x_test[image_number]
probabilities = model.predict_proba([X_test[image_number]])[0]
pred_label = guesses[image_number]
pred_confidence = probabilities[pred_label] * 100
true_label = y_test[image_number]

plt.figure(figsize=(3, 3))
plt.imshow(img, cmap="gray")
plt.title(
    f"Pred: {pred_label} ({pred_confidence:.1f}%) – True: {true_label}",
    fontsize=12,
)
plt.axis("off")
plt.show()

# End of script
