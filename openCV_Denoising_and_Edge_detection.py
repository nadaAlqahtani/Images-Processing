import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread(r"C:\Users\nadaa\Python  Project\Courses\Image Processing Spyder\m1.jpg", 1)

kernel = np.ones((3,3), np.float32)/9


filter_2d = cv2.filter2D(img, -1, kernel)


blur = cv2.blur(img,(3,3))

cv2.imshow("original image", img)
cv2.imshow("2D custom filter", filter_2d)
cv2.imshow("blur filter", blur)

cv2.waitKey(0)
cv2.destroyAllWindows()

#Edge detection

img = cv2.imread(r"C:\Users\nadaa\Python  Project\Courses\Image Processing Spyder\m1.jpg", 0)

edges = cv2.Canny(img, 100, 200)

cv2.imshow("Edges",edges)

cv2.waitKey(0)
cv2.destroyAllWindows()

