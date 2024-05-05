import cv2
import numpy as np

# Load the image
image = cv2.imread('/Users/thebiggestnutcase/Documents/VSCode/21CSL66_CG_Lab/SimplePrograms/example.png')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Edge Detection
edges = cv2.Canny(gray, 100, 200)
cv2.imshow('Edges', edges)

# Texture Detection
kernel = np.ones((5, 5), np.float32) / 25
texture = cv2.filter2D(gray, -1, kernel)
cv2.imshow('Texture', texture)

# Gaussian Blur
blur = cv2.GaussianBlur(gray, (5, 5), 0)
cv2.imshow('Gaussian Blur', blur)

# Median Blur
median = cv2.medianBlur(gray, 5)
cv2.imshow('Median Blur', median)

# Bilateral Filter
bilateral = cv2.bilateralFilter(gray, 9, 75, 75)
cv2.imshow('Bilateral Filter', bilateral)

# Display the original image
cv2.imshow('Original Image', image)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
