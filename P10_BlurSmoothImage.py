import cv2
import numpy as np

# Load the image
image = cv2.imread('SimplePrograms/random-1574391.jpg')

# Gaussian Blur
gaussian_blur = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow('Gaussian Blur', gaussian_blur)

# Median Blur
median_blur = cv2.medianBlur(image, 5)
cv2.imshow('Median Blur', median_blur)

# Bilateral Filter
bilateral_filter = cv2.bilateralFilter(image, 9, 75, 75)
cv2.imshow('Bilateral Filter', bilateral_filter)

# Averaging Blur
averaging_blur = cv2.blur(image, (5, 5))
cv2.imshow('Averaging Blur', averaging_blur)

# Box Filter
box_filter = cv2.boxFilter(image, -1, (5, 5))
cv2.imshow('Box Filter', box_filter)

# Display the original image
cv2.imshow('Original Image', image)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()