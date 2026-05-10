import cv2
import numpy as np
from matplotlib import pyplot as plt

imgpath=r"/Users/fiz/Desktop/parrot.png.avif"
img=cv2.imread(imgpath)
gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

#smoothening
mean=cv2.blur(gray,(5,5))
gaussian=cv2.GaussianBlur(gray,(5,5),0)
median=cv2.medianBlur(gray,5)
#sharpening
lap=cv2.Laplacian(gray,cv2.CV_64F)
unsharp=cv2.addWeighted(gray,1.5,gaussian,-0.5,0)

plt.subplot(1,6,1)
plt.imshow(gray,cmap="gray")
plt.title("Gray image")
plt.axis("off")

plt.subplot(1,6,2)
plt.imshow(mean,cmap="gray")
plt.title("mean filter image")
plt.axis("off")

plt.subplot(1,6,3)
plt.imshow(gaussian,cmap="gray")
plt.title("gaussian filter image")
plt.axis("off")

plt.subplot(1,6,4)
plt.imshow(median,cmap="gray")
plt.title("median filter image")
plt.axis("off")

plt.subplot(1,6,5)
plt.imshow(lap ,cmap="gray")
plt.title("laplacian filter image")
plt.axis("off")

plt.subplot(1,6,6)
plt.imshow(unsharp,cmap="gray")
plt.title("unsharp filter image")
plt.axis("off")

plt.show()