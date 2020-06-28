from skimage import io

from matplotlib import pyplot as plt

img = io.imread(r"C:\Users\nadaa\Python  Project\Courses\Image Processing Spyder\1.jpg", as_gray=True)

from skimage.transform import rescale, resize, downscale_local_mean

rescale_img = rescale(img, 1.0/4.0, anti_aliasing=True)

resize_img = resize(img, (200,200)) 

downscale_img = downscale_local_mean(img, (4,3))

plt.imshow(img)
plt.imshow(rescale_img)
plt.imshow(resize_img)
plt.imshow(downscale_img)


#Edge filtering or Edge detection 
from skimage.filters import roberts, sobel, scharr, prewitt

edge_roberts = roberts(img)
plt.imshow(edge_roberts, cmap='gray')

edge_sobel = sobel(img)
plt.imshow(edge_sobel, cmap='gray')

edge_scharr = scharr(img)
plt.imshow(edge_scharr, cmap='gray')

edge_prewitt = prewitt(img)
plt.imshow(edge_prewitt, cmap='gray')

from skimage.feature import canny

edge_canny = canny(img, sigma=4)
plt.imshow(edge_canny)

#
from skimage import restoration

import numpy as np

psf = np.ones((3,3)) / 9

deconvoled, _ = restoration.unsupervised_wiener(img, psf)

plt.imsave(r"C:\Users\nadaa\Python  Project\Courses\Image Processing Spyder\deconvoled_img.jpg",
           deconvoled, cmap='gray')



####################################
#Entropy

#https://scikit-image.org/docs/stable/auto_examples/

from skimage import io, restoration
from skimage.filters.rank import entropy
from skimage.morphology import disk

img1 = io.imread(r"C:\Users\nadaa\Python  Project\Courses\Image Processing Spyder\3.jpg", as_gray=True)

entr_img = entropy(img1, disk(3))

plt.imshow(entr_img, cmap='gray')


from skimage.filters import try_all_threshold

fig, ax = try_all_threshold(entr_img, figsize=(10,8), verbose=False)

plt.show()



