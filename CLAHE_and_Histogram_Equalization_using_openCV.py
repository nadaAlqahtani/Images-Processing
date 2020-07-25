import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread(r"C:\Users\nadaa\Python  Project\Courses\Image Processing Spyder\b1.jpg", 0)

# Histogram Equalization
eq_img = cv2.equalizeHist(img)
plt.hist(eq_img.flat, bins=100, range=(0,255))


# Contast Limiting Adaptive Histogram Equalization

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl_img = clahe.apply(img)

plt.hist(cl_img.flat, bins=100, range=(0,255))

ret, thresh1 = cv2.threshold(cl_img, 190, 150, cv2.THRESH_BINARY)
#ret, thresh2 = cv2.threshold(cl_img, 190, 255, cv2.THRESH_BINARY_INV)

ret2, thresh2 = cv2.threshold(cl_img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)



cv2.imshow("Original Image" , img)
#cv2.imshow("Equalized Image" , eq_img)
#cv2.imshow("CLAHE Image" , cl_img)
cv2.imshow("Binary Threshold 1 " , thresh1)
#cv2.imshow("Binary Threshold 2 " , thresh2)
cv2.imshow("OTSU" , thresh2)
cv2.waitKey(0)
cv2.destroyAllWindows()

