#pip install opencv-python

import cv2

img = cv2.imread(r"C:\Users\nadaa\Python  Project\Courses\Image Processing Spyder\RGBY.jpg", 1)

print(img.shape)

print("Top left", img[0,0])

#opencv read image as BGR not RGB

# 1

blue = img[:, :, 0]
green = img[:, :, 1]
red = img[:, :, 2]


cv2.imshow("Blue", blue)
cv2.imshow("Red", red)
cv2.imshow("Green", green)
cv2.waitKey(0)
cv2.destroyAllWindows()

# or 2

blue, green, red = cv2.split(img)


cv2.imshow("Blue", blue)
cv2.imshow("Red", red)
cv2.imshow("Green", green)
cv2.waitKey(0)
cv2.destroyAllWindows()

# or 3
img_merged = cv2.merge((blue,green, red))
cv2.imshow("Merge", img_merged)
cv2.waitKey(0)
cv2.destroyAllWindows()

#resize images

img = cv2.imread(r"C:\Users\nadaa\Python  Project\Courses\Image Processing Spyder\RGBY.jpg", 1)

# fx=2, fy=2  

resize_img = cv2.resize(img, None, fx=2, fy=2, interpolation = cv2.INTER_CUBIC)

cv2.imshow("Original Image", img)
cv2.imshow("Resized Image", resize_img)
cv2.waitKey(0)
cv2.destroyAllWindows()




