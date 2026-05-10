import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("/Users/fiz/Desktop/parrot.png.avif",0)
_, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
kernel = np.ones((5, 5), np.uint8)

erosion = cv2.erode(binary, kernel, iterations=1)
dilation = cv2.dilate(binary, kernel, iterations=1)
opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
gradient = cv2.morphologyEx(binary, cv2.MORPH_GRADIENT, kernel)

titles = [
    "Original Image",
    "Binary Image",
    "Erosion",
    "Dilation",
    "Opening",
    "Closing",
    "Morphological Gradient"
]

images = [
    image,
    binary,
    erosion,
    dilation,
    opening,
    closing,
    gradient
]

plt.figure(figsize=(12, 10))
for i in range(len(images)):
    plt.subplot(3, 3, i + 1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')

plt.show()