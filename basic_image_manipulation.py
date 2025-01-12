import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

cb_img = cv2.imread("assets/checkerboard_18x18.png", 0)
cb_img_copy = cb_img.copy()
img_NZ_bgr = cv2.imread("assets/New_Zealand_Lake.jpg", 1)
img_NZ_rgb = img_NZ_bgr[:, :, ::-1]
cropped_region = img_NZ_rgb[200:400, 300:600]

desired_width = 1200
aspect_ratio = desired_width / cropped_region.shape[1]
desired_height = int(cropped_region.shape[0] * aspect_ratio)
dim = (desired_width, desired_height)
resized_cropped_region = cv2.resize(img_NZ_bgr, dsize=dim)
# cv2.imshow('Checker board', cb_img)

print(cb_img)
print(cb_img[0, 0])
print(cb_img[6, -1])
cb_img_copy[2, 2] = 200
cb_img_copy[2, 3] = 200
cb_img_copy[3, 2] = 200
cb_img_copy[3, 3] = 200

# cv2.imshow('Modified image' ,cb_img_copy)
cv2.imshow('Newzealand boat', img_NZ_bgr)
cv2.imshow('Cropped', cropped_region)
cv2.imshow('Resized image', resized_cropped_region)
print(cb_img_copy)

cv2.waitKey(0)