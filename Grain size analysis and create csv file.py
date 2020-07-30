
import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy import ndimage
from skimage import io, color, measure

#Read image and define pixel size

img = cv2.imread(r"C:\Users\nadaa\Python  Project\Courses\Image Processing Spyder\g1.jpg", 0)
pixels_to_um = 0.5

#cropped_img = img[0:300, :]

#threshold image

#plt.hist(img.flat, bins=100, range=(0,255))

ret, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

#Clean up image
kernel=np.ones((3,3),np.uint8)
eroded = cv2.erode(thresh, kernel,iterations=1)
dilated = cv2.dilate(eroded, kernel,iterations=1)

#convert image to punary image
mask = dilated == 255
#io.imshow(mask[250:280, 250:280])

#Label grains

s = [[1,1,1], [1,1,1], [1,1,1]]
label_mask, num_labels = ndimage.label(mask, structure=s)

#Add color
img2 = color.label2rgb(label_mask, bg_label=0)


cv2.imshow("threshold image", thresh)
cv2.imshow("dilated image", dilated)
cv2.imshow("color image", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()



#Measure the properties of each grain

clusters = measure.regionprops(label_mask,img)

#Output results into a csv file

propList = ['Area',
            'equivalent_diameter', 
            'orientation', 
            'MajorAxisLength',
            'MinorAxisLength',
            'Perimeter',
            'MinIntensity',
            'MeanIntensity',
            'MaxIntensity']    
   
 
output_file = open(r"C:\Users\nadaa\Python  Project\Courses\Image Processing Spyder\image_measurement.csv",'w')   

output_file.write(","+",".join(propList)+"\n")


for cluster_props in clusters:
    #output cluster properties to the excel file
    output_file.write(str(cluster_props['Label']))
    for i,prop in enumerate(propList):
        if(prop == 'Area'): 
            to_print = cluster_props[prop]*pixels_to_um**2   #Convert pixel square to um square
        elif(prop == 'orientation'): 
            to_print = cluster_props[prop]*57.2958  #Convert to degrees from radians
        elif(prop.find('Intensity') < 0):          # Any prop without Intensity in its name
            to_print = cluster_props[prop]*pixels_to_um
        else: 
            to_print = cluster_props[prop]     #Reamining props, basically the ones with Intensity in its name
        output_file.write(',' + str(to_print))
    output_file.write('\n')
output_file.close() 





