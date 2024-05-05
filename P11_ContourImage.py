import cv2
import numpy as np

# Load the image
image = cv2.imread('SimplePrograms/random-1574391.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Apply Canny edge detection
edges = cv2.Canny(blurred, 50, 150)

# Find contours in the binary image
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Create a copy of the original image for drawing contours
contour_image = image.copy()

# Draw contours on the image
cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 2)

# Display the original image and the image with contours
cv2.imshow('Original Image', image)
cv2.imshow('Contours', contour_image)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()