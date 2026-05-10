import cv2
import numpy as np
from matplotlib import pyplot as plt

imgpath=r"/Users/fiz/Desktop/parrot.png.avif"
img=cv2.imread(imgpath)
gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

dft=np.fft.fft2(gray)
dftshift=np.fft.fftshift(dft)
magnitude=np.log(1+np.abs(dftshift))

plt.subplot(1,2,1)
plt.imshow(gray,cmap="gray")
plt.title("Gray image")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(magnitude,cmap="gray")
plt.title("Dft shift")
plt.axis("off")

plt.show()