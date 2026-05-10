
import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread("/Users/fiz/Desktop/parrot.png.avif", cv2.IMREAD_GRAYSCALE)

blurred = cv2.GaussianBlur(image, (5, 5), 0)
sobelx = cv2.Sobel(blurred, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(blurred, cv2.CV_64F, 0, 1, ksize=3)
sobel = cv2.magnitude(sobelx, sobely)
sobel = np.uint8(np.absolute(sobel))
kernelx = np.array([[ -1, 0, 1],
                    [ -1, 0, 1],
                    [ -1, 0, 1]])

kernely = np.array([[ 1, 1, 1],
                    [ 0, 0, 0],
                    [ -1,-1,-1]])


prewittx = cv2.filter2D(blurred, -1, kernelx)
prewitty = cv2.filter2D(blurred, -1, kernely)
prewitt = cv2.magnitude(np.float32(prewittx), np.float32(prewitty))
prewitt = np.uint8(np.absolute(prewitt))


canny = cv2.Canny(blurred, 100, 200)


lines = cv2.HoughLines(canny, 1, np.pi/180, 150)
hough_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)


if lines is not None:
    for rho, theta in lines[:10]: 
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv2.line(hough_image, (x1, y1), (x2, y2), (0, 0, 255), 2)


laplacian = cv2.Laplacian(blurred, cv2.CV_64F)
laplacian = np.uint8(np.absolute(laplacian))


plt.figure(figsize=(15, 10))
plt.subplot(3,3,1)
plt.title("Original Image")
plt.imshow(image, cmap='gray')
plt.axis("off")


plt.subplot(3,3,2)
plt.title("Gaussian Blur")
plt.imshow(blurred, cmap='gray')
plt.axis("off")


plt.subplot(3,3,3)
plt.title("Sobel Edge")
plt.imshow(sobel, cmap='gray')
plt.axis("off")
plt.subplot(3,3,4)
plt.title("Prewitt Edge")
plt.imshow(prewitt, cmap='gray')
plt.axis("off")


plt.subplot(3,3,5)
plt.title("Canny Edge")
plt.imshow(canny, cmap='gray')
plt.axis("off")


plt.subplot(3,3,6)
plt.title("Hough Line Detection")
plt.imshow(cv2.cvtColor(hough_image, cv2.COLOR_BGR2RGB))
plt.axis("off")


plt.subplot(3,3,7)
plt.title("Laplacian (Point Detection)")
plt.imshow(laplacian, cmap='gray')
plt.axis("off")


plt.tight_layout()
plt.show()