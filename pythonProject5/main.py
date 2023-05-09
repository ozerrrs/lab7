import cv2
import numpy as np
image = cv2.imread('photo.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

blue_channel = image[:, :, 0]
green_channel = image[:, :, 1]
red_channel = image[:, :, 2]

cv2.imshow('Blue channel', blue_channel)
cv2.imshow('Green Channel', green_channel)
cv2.imshow('Red Channel', red_channel)

image[:, :, 1] = 0
image[:, :, 0] += 50
image[:, :, 2] += 50

image = np.clip(image, 0, 255)

image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

cv2.imshow('New jpg', image)

cv2.waitKey(0)


