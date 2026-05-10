import cv2
import numpy as np
from matplotlib import pyplot as plt

imgpath=r"/Users/fiz/Desktop/parrot.png.avif"
img=cv2.imread(imgpath)
gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

f = np.fft.fft2(gray)
fshift = np.fft.fftshift(f)

rows, cols = gray.shape
crow, ccol = rows//2 , cols//2

# Step 3A: Low-pass filter (smoothing)
lpf = np.zeros((rows,cols),np.uint8)
r = 30
for i in range(rows):
    for j in range(cols):
        if (i-crow)**2 + (j-ccol)**2 <= r*r:
            lpf[i,j] = 1
smooth = fshift * lpf

# Step 3B: High-pass filter (sharpening)
hpf = 1 - lpf
sharp = fshift * hpf

# Step 4: Inverse FFT
smooth_img = np.fft.ifft2(np.fft.ifftshift(smooth))
smooth_img = np.abs(smooth_img)
sharp_img = np.fft.ifft2(np.fft.ifftshift(sharp))
sharp_img = np.abs(sharp_img)

plt.subplot(1,3,1)
plt.title("Original")
plt.imshow(img,cmap='gray')
plt.axis('off')

plt.subplot(1,3,2)
plt.title("Low Pass (Smooth)")
plt.imshow(smooth_img,cmap='gray')
plt.axis('off')

plt.subplot(1,3,3)
plt.title("High Pass (Sharp)")
plt.imshow(sharp_img,cmap='gray')
plt.axis('off')

plt.show()