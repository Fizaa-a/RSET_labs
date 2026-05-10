import cv2
import numpy as np
from matplotlib import pyplot as plt

imgpath=r"/Users/fiz/Desktop/parrot.png.avif"
img=cv2.imread(imgpath)
gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

#sampling
f=8
sampled=gray[::f,::f]

#quantisation
q=32
normalised=gray/255.0
quantprime=np.round(normalised*(q-1))
quantimg=quantprime*(255/(q-1))
quant=quantimg.astype(np.uint8)

plt.subplot(1,3,1)
plt.imshow(gray,cmap="gray")
plt.title("gray img")
plt.axis("off")

plt.subplot(1,3,2)
plt.imshow(sampled,cmap="gray")
plt.title("sampled")
plt.axis("off")

plt.subplot(1,3,3)
plt.imshow(quant,cmap="gray")
plt.title("quantised")
plt.axis("off")

plt.show()