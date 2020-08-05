
import cv2
import numpy as np
import sys
import os
import fnmatch

def resize(fname, width, height):
    image = cv2.imread(fname)
    cv2.imshow('Original', image)
    cv2.waitKey(0)
    org_h, org_w = image.shape[0:2]
    print("width: ", org_w)
    print("height:", org_h)

    if org_w >= org_h:
        new_image = cv2.resize(image, (width, height))
    else:
        new_image = cv2.resize(image, (height, width))

    return fname, new_image

def blur(image):
    kernels = [3, 5, 9, 13]
    for idx, k in enumerate(kernels):
        image_bl = cv2.blur(image, ksize=(k, k))
        cv2.imshow(str(k), image_bl)
        cv2.waitKey(0)
    return

def sharpen(image):
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    new_image = cv2.filter2D(image, -1, kernel)
    cv2.imshow('Sharpend', new_image)
    cv2.waitKey(0)
    return new_image


"""

#resize('cat_in_iran.jpg',500,500)
#resize the image
filename, new_image =resize ('cat_in_iran.jpg',500,500)
#show resized image
cv2.imshow('resized image', new_image)
cv2.waitKey(0)
#show blur image for different-different kernels
#blur(new_image)

# show sharpen image
image=sharpen(new_image)
"""

listOfIles = os.listdir('.')
pattern = "*.jpg"
n = len(sys.argv)
if n == 3:
    width = int(sys.argv[1])
    height = int(sys.argv[2])
else:
    width = 1280
    height = 960
if not os.path.exists('nf'):
    os.makedirs('nf')

for fname in listOfIles:
    if fnmatch.fnmatch(fname, pattern):
        fname, new_image = resize(fname, width, height)
        cv2.imwrite("nf\\"+fname, new_image)
