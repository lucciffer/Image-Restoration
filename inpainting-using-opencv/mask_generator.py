import cv2
import numpy as np

#reading input image
img = cv2.imread(r'/home/lucciffer/WORK/Machine Learning/CVG/image restoration/restore_this/test_image1.jpeg', 0)
print(img.shape)

#generating mask
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if img[i, j] >= 225 and img[i, j] <= 255:
            img[i, j] = 255
        else:
            img[i, j] = 0
# cv2.imshow('test', img)
#saving mask image
cv2.imwrite('outputs/mask_test1.jpg', img)
cv2.waitKey(0)

