from scipy import misc
from scipy import ndimage
import numpy as np
from matplotlib import pyplot as plt

img1 = misc.imread(r"C:\Users\nadaa\Python  Project\Courses\Image Processing Spyder\1.jpg")

#print(type(img1))

'''
`imread` is deprecated in SciPy 1.0.0, and will be removed in 1.2.0.
Use ``imageio.imread`` instead.

'''
from skimage import io, img_as_ubyte

img = img_as_ubyte(io.imread
                   (r"C:\Users\nadaa\Python  Project\Courses\Image Processing Spyder\1.jpg", as_gray=True))

print(type(img))

print(img.dtype)

print(img.shape)

print(img)

#print pixel value

print(img[10:15, 20:25])

mean_vlaue = img.mean()
max_value = img.max()
min_value = img.min()

print("mean,max,min=" , mean_vlaue,max_value,min_value)

#flip image

#flip L2R
flip_LR = np.fliplr(img)
#flip U2D
flip_UD = np.flipud(img)

plt.subplot(2, 1, 1)
plt.imshow(img, cmap="Greys")
plt.subplot(2, 2, 3)
plt.imshow(flip_LR, cmap="Blues")
plt.subplot(2, 2, 4)
plt.imshow(flip_UD, cmap="hsv")


# rotation iamge

rotate_img = ndimage.rotate(img1, 45, reshape=False)
plt.imshow(rotate_img)


#filters image

uniform_filter = ndimage.uniform_filter(img1,size=20)
plt.imshow(uniform_filter)


Gaussian_filter = ndimage.gaussian_filter(img1, sigma=11)
plt.imshow(Gaussian_filter)

Median_filter = ndimage.median_filter(img1, 20)
plt.imshow(Median_filter)

sobel_img = ndimage.sobel(img, axis=0)
plt.imshow(sobel_img)
