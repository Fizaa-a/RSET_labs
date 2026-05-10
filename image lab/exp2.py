import cv2
from matplotlib import pyplot as plt

imgpath=r"/Users/fiz/Desktop/parrot.png.avif"
img=cv2.imread(imgpath)

gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

#SPATIAL RESOLUTION
img1=cv2.resize(gray,(512,512))
img2=cv2.resize(gray,(256,256))
img3=cv2.resize(gray,(128,128))

#INTENSITY RESOLUTION
res128=(gray//2)*2
res64=(gray//4)*4
res32=(gray//8)*8

plt.subplot(2,3,1)
plt.imshow(img1,cmap="gray")
plt.title("resized to 512")
plt.axis("off")

plt.subplot(2,3,2)
plt.imshow(img2,cmap="gray")
plt.title("resized to 256")
plt.axis("off")

plt.subplot(2,3,3)
plt.imshow(img3,cmap="gray")
plt.title("resized to 128")
plt.axis("off")

plt.subplot(2,3,4)
plt.imshow(res128,cmap="gray")
plt.title("intensity to 128")
plt.axis("off")

plt.subplot(2,3,5)
plt.imshow(res64,cmap="gray")
plt.title("intensity to 64")
plt.axis("off")

plt.subplot(2,3,6)
plt.imshow(res32,cmap="gray")
plt.title("intensity to 32")
plt.axis("off")

plt.show()