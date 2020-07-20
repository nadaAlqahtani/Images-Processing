from skimage import io, img_as_float
import matplotlib.pyplot as plt
import numpy as np
from skimage.restoration import denoise_nl_means, estimate_sigma

img = img_as_float(io.imread(r"C:\Users\nadaa\Python  Project\Courses\Image Processing Spyder\b1.jpg"))

plt.hist(img.flat, bins=100, range=(0,1))


sigma_est = np.mean(estimate_sigma(img, multichannel=True))


patch_kw = dict(patch_size=5,      # 5x5 patches
                patch_distance=6,  # 13x13 search area
                multichannel=True)

# slow algorithm
denoise = denoise_nl_means(img, h=1.15 * sigma_est, fast_mode=True,
                           **patch_kw)


from skimage import exposure

eq_image = exposure.equalize_adapthist(denoise)



plt.hist(eq_image.flat, bins=100, range=(0,1))

#plt.imshow(eq_image, cmap='gray')


markers = np.zeros(img.shape, dtype=np.uint)

markers[(eq_image > 0.0) & (eq_image < 0.1)] = 1
markers[(eq_image > 0.2) & (eq_image < 0.4)] = 2
markers[(eq_image > 0.4) & (eq_image < 1.0)] = 1




plt.imshow(markers)


from skimage.segmentation import random_walker

labels = random_walker(eq_image, markers, beta=10, mode='bf')
plt.imsave("images/markers.jpg", markers)
segm1 = (labels == 1)
segm2 = (labels == 2)
all_segments = np.zeros((eq_image.shape[0], eq_image.shape[1], 3)) #nothing but denoise img size but blank

all_segments[segm1] = (1,0,0)
all_segments[segm2] = (0,1,0)

#plt.imshow(all_segments)

from scipy import ndimage as nd

segm1_closed = nd.binary_closing(segm1, np.ones((3,3)))
segm2_closed = nd.binary_closing(segm2, np.ones((3,3)))

all_segments_cleaned = np.zeros((eq_image.shape[0], eq_image.shape[1], 3)) 

all_segments_cleaned[segm1_closed] = (1,0,0)
all_segments_cleaned[segm2_closed] = (0,1,0)

plt.imshow(all_segments_cleaned) 
plt.imsave("images/random_walker.jpg", all_segments_cleaned)






