from skimage import io, img_as_float
from scipy import ndimage as nd
from matplotlib import pyplot as plt
from skimage.restoration import denoise_nl_means, estimate_sigma
import numpy as np

img = img_as_float(io.imread(r"C:\Users\nadaa\Python  Project\Courses\Image Processing Spyder\m1.JPG"))

gaussian_img = nd.gaussian_filter(img, sigma=3)

plt.imsave(r"C:\Users\nadaa\Python  Project\Courses\Image Processing Spyder\images\guassian_m1.jpg", gaussian_img)

median_img = nd.median_filter(img, size=3)

plt.imsave(r"C:\Users\nadaa\Python  Project\Courses\Image Processing Spyder\images\median_m1.jpg", median_img)


# Non-local means denoising for preserving textures

sigma_est = np.mean(estimate_sigma(img, multichannel=True))
# slow algorithm
nlm = denoise_nl_means(img, h=1.15 * sigma_est, fast_mode=True,patch_size=5,patch_distance=6,multichannel=True)

plt.imsave(r"C:\Users\nadaa\Python  Project\Courses\Image Processing Spyder\images\nlm_m1.jpg", nlm)
