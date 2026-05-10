import cv2
import numpy as np
from matplotlib import pyplot as plt

imgpath=r"/Users/fiz/Desktop/parrot.png.avif"
img=cv2.imread(imgpath)
gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

#salt and pepper
noise=gray.copy()
prob=0.2
ran=np.random.rand(*gray.shape)
noise[ran<prob]=0
noise[ran>1-prob]=255

mean=cv2.blur(noise,(3,3))
gaussian=cv2.GaussianBlur(noise,(3,3),0)
median=cv2.medianBlur(noise,3)

def mse(a,b):
    return np.mean((a-b)**2)
    
def psnr(a,b):
    m=mse(a,b)
    return 10*np.log10((255**2)/m)
    
print("Mean filter: mse-",mse(gray,mean),"  psnr-",psnr(gray,mean))
print("gaussian filter: mse-",mse(gray,gaussian),"  psnr-",psnr(gray,gaussian))
print("median filter: mse-",mse(gray,median),"  psnr-",psnr(gray,median))

plt.subplot(5,1,1)
plt.imshow(gray,cmap="gray")
plt.title("gray image")
plt.axis("off")

plt.subplot(5,1,2)
plt.imshow(noise,cmap="gray")
plt.title("noise image")
plt.axis("off")

plt.subplot(5,1,3)
plt.imshow(mean,cmap="gray")
plt.title("mean filter image")
plt.axis("off")

plt.subplot(5,1,4)
plt.imshow(gaussian,cmap="gray")
plt.title("gaussian filter image")
plt.axis("off")

plt.subplot(5,1,5)
plt.imshow(median,cmap="gray")
plt.title("median filter image")
plt.axis("off")

plt.show()
