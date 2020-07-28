
import cv2
import numpy as np

img1 = cv2.imread(r"C:\Users\nadaa\Python  Project\Courses\Image Processing Spyder\mon1.jpg") #registered image

img2 = cv2.imread(r"C:\Users\nadaa\Python  Project\Courses\Image Processing Spyder\mon2.jpg") #refrence image


img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

#ORB (Oriented FAST and Rotated BRIEF)
orb = cv2.ORB_create(50)

kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)


matcher = cv2.DescriptorMatcher.create(cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING)

#Match descriptors

matches = matcher.match(des1, des2, None)

matches = sorted(matches, key=lambda x:x.distance)


points1 = np.zeros((len(matches), 2), dtype=np.float32)
points2 = np.zeros((len(matches), 2), dtype=np.float32)

for i, match in enumerate(matches):
    points1[i, :] = kp1[match.queryIdx].pt
    points2[i, :] = kp2[match.queryIdx].pt



h, mask = cv2.findHomography(points1, points2, cv2.RANSAC)

#use homography

height, width = img2.shape

img1Reg = cv2.warpPerspective(img1, h, (width, height))

#flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS or 0
img3 = cv2.drawMatches(img1, kp1,img2, kp2, matches[:], None)
#img4 = cv2.drawKeypoints(img2, kp2, None, flags=0)


cv2.imshow('Keypoint Matches', img3)
cv2.imshow('Registered Image', img1Reg)

cv2.waitKey(0)
#cv2.destroyAllWindows()
