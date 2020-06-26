from PIL import Image

img = Image.open(r"C:\Users\nadaa\Python  Project\Courses\Image Processing Spyder\1.jpg")

print(img.format)
print(img.mode)
print(img.size)

#resize image

small_img = img.resize((200,300))

small_img.save(r"C:\Users\nadaa\Python  Project\Courses\Image Processing Spyder\resize_img_small.jpg")

img.thumbnail((200,300))

img.save(r"C:\Users\nadaa\Python  Project\Courses\Image Processing Spyder\resize_img_small_thumbnail.jpg")
print(img.size)

#make image larger

'''
you can't use thumbnail to resize image to  larger than original image.

'''

large_img = img.resize((1500,900))

large_img.save(r"C:\Users\nadaa\Python  Project\Courses\Image Processing Spyder\resize_img_large.jpg")
print(large_img.size)


#crop image

cropped_img = img.crop((0, 0, 300, 300))

cropped_img.save(r"C:\Users\nadaa\Python  Project\Courses\Image Processing Spyder\crop_img.jpg")
print(cropped_img.size)

#copy part from one image to another 

img1 = Image.open(r"C:\Users\nadaa\Python  Project\Courses\Image Processing Spyder\1.jpg")
img2 = Image.open(r"C:\Users\nadaa\Python  Project\Courses\Image Processing Spyder\2.png")
print(img1.size)
print(img2.size)

img2.thumbnail((150,200))


img1_copy = img1.copy()
img1_copy.paste(img2, (100, 100))

img1_copy.save(r"C:\Users\nadaa\Python  Project\Courses\Image Processing Spyder\copy_img.jpg")
































