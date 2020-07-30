
#Downscale with resize
#Decrease the size of the image
import cv2
import numpy as np

img = cv2.imread(r"C:\Users\nadaa\Python  Project\Courses\Image Processing Spyder\mon.jpg")


scale_percent = 40 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)


cv2.imwrite( r"C:\Users\nadaa\Python  Project\Courses\Image Processing Spyder\mon1.jpg",resized)
cv2.imshow('orginal',img)
cv2.imshow('resize',resized)
cv2.waitKey(0)