import imageio as iio
import cv2
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
img = iio.imread("/apple.jpg")
# write it in a new format
iio.imwrite("apple.png")
iio.imwrite("apple.PDF")
iio.imwrite("apple.jpeg")



# Save image in set directory
# Read RGB image
# img = cv2.imread('apple.png')




# Output img with window name as 'image'
# cv2.imshow('image', img)
# cv2.waitKey(0)

# Destroying present windows on screen
# cv2.destroyAllWindows()

# Output Images
# plt.imshow(img)