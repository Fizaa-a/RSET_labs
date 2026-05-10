import cv2
from matplotlib import pyplot as plt

imgpath=r"/Users/fiz/Desktop/parrot.png.avif"
img=cv2.imread(imgpath)

rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
rgbneg=255-rgb

gray=cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
grayneg=255-gray

_,binary=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
binaryneg=cv2.bitwise_not(binary)

plt.subplot(3,2,1)
plt.imshow(rgb)
plt.title("color image")
plt.axis("off")

plt.subplot(3,2,2)
plt.imshow(rgbneg)
plt.title("color negative image")
plt.axis("off")

plt.subplot(3,2,3)
plt.imshow(gray)
plt.title("gray image")
plt.axis("off")

plt.subplot(3,2,4)
plt.imshow(grayneg)
plt.title("gray image neg")
plt.axis("off")

plt.subplot(3,2,5)
plt.imshow(binary)
plt.title("binary image")
plt.axis("off")

plt.subplot(3,2,6)
plt.imshow(binaryneg)
plt.title("biary negative image")
plt.axis("off")

plt.show()