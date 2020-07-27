#Harris Corner Detection


import cv2
import numpy as np

img = cv2.imread(r"C:\Users\nadaa\Python  Project\Courses\Image Processing Spyder\b1.jpg")


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)

harris = cv2.cornerHarris(gray, 2, 3, 0.04)

img[harris>0.01*harris.max()] = [255, 0, 0]

cv2.imshow("Harris" , img)

cv2.waitKey(0)
cv2.destroyAllWindows()




#Shi-Tomasi Corner Detector & Good Features to Track


import cv2
import numpy as np

img = cv2.imread(r"C:\Users\nadaa\Python  Project\Courses\Image Processing Spyder\b1.jpg")


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray,25,0.01,10)
corners = np.int0(corners)

for i in corners:
    x,y = i.ravel()
    #print(x,y)
    cv2.circle(img,(x,y),3,255,-1)

cv2.imshow("Corners", img)
cv2.waitKey(0)
cv2.destroyAllWindows()



#FAST Algorithm for Corner Detection(Features from Accelerated Segment Test)


import cv2
import numpy as np

img = cv2.imread(r"C:\Users\nadaa\Python  Project\Courses\Image Processing Spyder\b1.jpg", 0)

detector = cv2.FastFeatureDetector_create(50)   #Detects 50 points

kp = detector.detect(img, None)

img2 = cv2.drawKeypoints(img, kp, None, flags=0)

cv2.imshow('Corners',img2)
cv2.waitKey(0)



#ORB (Oriented FAST and Rotated BRIEF)

#FAST = Detector

#BRIEF = Descriptor


import cv2
import numpy as np

img = cv2.imread(r"C:\Users\nadaa\Python  Project\Courses\Image Processing Spyder\b1.jpg", 0)

orb = cv2.ORB_create(50)

kp, des = orb.detectAndCompute(img, None)


img2 = cv2.drawKeypoints(img, kp, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow('ORB',img2)
cv2.waitKey(0)





