import os
import cv2
import numpy as np
from IPython.display import Image
import matplotlib.pyplot as plt

# Image(filename="assets/checkerboard_18x18.png")

cb_img = cv2.imread("assets/coca-cola-logo.png", 1)
cb_img_fuzzy = cv2.imread("assets/checkerboard_fuzzy_18x18.jpg", 1)
img_NZ_bgr = cv2.imread("assets/New_Zealand_Lake.jpg", cv2.IMREAD_COLOR)
b, g, r = cv2.split(img_NZ_bgr)
imgMerged = cv2.merge((b, g, r))
cv2.imwrite("New_Zealand_Lake_SAVED.png", b)
cv2.imwrite("New_Zealand_Lake_SAVED.png", img_NZ_bgr)

img_NZ_bgr_saved = cv2.imread("New_Zealand_Lake_SAVED.png", cv2.IMREAD_COLOR)

# print("Image size (H, W) ", cb_img.shape)
# print("Data type of image ", cb_img.dtype)
# print(cb_img_fuzzy)
print(img_NZ_bgr)
print("Channel b")
print(b)

# cv2.imshow('coca cola logo', cb_img)
# cv2.imshow('cheker board', cb_img_fuzzy)
# cv2.imshow('channel one', b)
# cv2.imshow('channel two', g)
# cv2.imshow('channel three', r)
# cv2.imshow('mergerd output', imgMerged)
cv2.imshow('colored image', img_NZ_bgr_saved)

cv2.waitKey(0)