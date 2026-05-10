import cv2, numpy as np, matplotlib.pyplot as plt
from scipy.fftpack import dct
import pywt
from scipy.linalg import hadamard

# Read + preprocess
img = cv2.imread("/Users/fiz/Desktop/parrot.png.avif", 0)  # directly grayscale
img = cv2.resize(img, (256, 256)).astype(np.float32)

# Transforms
H = hadamard(256)
had = H @ img @ H
dct_img = dct(dct(img.T, norm='ortho').T, norm='ortho')
haar = pywt.dwt2(img, 'haar')[0]  # LL only

# Display scaling
scale = lambda x: (np.log1p(np.abs(x)) / np.max(np.log1p(np.abs(x))) * 255).astype(np.uint8)

# Plot
titles = ["Original", "Hadamard", "Walsh", "DCT", "Haar"]
images = [img, had, had, dct_img, haar]

plt.figure(figsize=(10,6))
for i in range(5):
    plt.subplot(2,3,i+1)
    plt.title(titles[i])
    plt.imshow(images[i] if i==0 else scale(images[i]), cmap='gray')
    plt.axis('off')

plt.tight_layout()
plt.show()