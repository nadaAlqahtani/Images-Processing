import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread(r"C:\Users\nadaa\Python  Project\Courses\Image Processing Spyder\b1.jpg", 0)
ret, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)



median = cv2.medianBlur(img, 3)
ret, thresh = cv2.threshold(median, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#plt.hist(img.flat, bins=100, range=(0,255))

kernal = np.ones((3,3),np.uint8)

erosion = cv2.erode(thresh, kernal, iterations=1)

dilation = cv2.dilate(erosion, kernal, iterations=2)

cv2.imshow("Original Image" , img)
cv2.imshow("thresh Image" , thresh)
cv2.imshow("Eroded Image" , erosion)
cv2.imshow("Dilation Image" , dilation)
cv2.imshow("Median Image" , dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()

