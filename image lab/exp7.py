import cv2
import numpy as np
from matplotlib import pyplot as plt

imgpath=r"/Users/fiz/Desktop/parrot.png.avif"
img=cv2.imread(imgpath)
gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

hist=cv2.equalizeHist(gray)

plt.subplot(1,2,1)
plt.imshow(gray,cmap="gray")
plt.title("Gray image")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(hist,cmap="gray")
plt.title("Histogram")
plt.axis("off")

plt.show()