import cv2
import numpy as np
from matplotlib import pyplot as plt

imgpath=r"/Users/fiz/Desktop/parrot.png.avif"
image=cv2.imread(imgpath)
gray=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)

norm=gray/255.0
#linear
a=1.5
b=0.7
linear=a*norm+b
linear=np.clip(linear,0,1)
#log
c=2
logarithm=c*np.log(norm+1)
logs=logarithm/np.max(logarithm)
#gamma
g=0.6
gamma=norm**g

lin=np.uint8(linear*255)
log=np.uint8(logs*255)
gam=np.uint8(gamma*255)

plt.subplot(1,4,1)
plt.imshow(gray,cmap="gray")
plt.title("Gray")
plt.axis("off")

plt.subplot(1,4,2)
plt.imshow(lin,cmap="gray")
plt.title("Linear")
plt.axis("off")

plt.subplot(1,4,3)
plt.imshow(log,cmap="gray")
plt.title("Logarithm")
plt.axis("off")

plt.subplot(1,4,4)
plt.imshow(gam,cmap="gray")
plt.title("Gamma")
plt.axis("off")

plt.show()