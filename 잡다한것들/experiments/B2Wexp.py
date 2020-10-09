import cv2
import numpy as np
img = cv2.imread('color_img.png')
for each in np.array(img):
    for som in range(len(each)):
        each[som] = sum(each[som])
## too slow