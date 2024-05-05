import cv2
import numpy as np

# Load the image
image = cv2.imread('/Users/thebiggestnutcase/Documents/VSCode/21CSL66_CG_Lab/SimplePrograms/example.png')

# Get the image dimensions
height, width = image.shape[:2]

# Define rotation parameters
rotation_angle = 30  # Degrees
rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), rotation_angle, 1)

# Define scaling parameters
scaling_factor = 1.5
scaling_matrix = np.array([[scaling_factor, 0, 0], [0, scaling_factor, 0]])

# Define translation parameters
translation_x = 100.0  # Convert to float
translation_y = 50.0   # Convert to float
translation_matrix = np.array([[1, 0, translation_x], [0, 1, translation_y]], dtype=np.float32)

# Rotation
rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
cv2.imshow('Rotated Image', rotated_image)

# Scaling
scaled_image = cv2.warpAffine(image, scaling_matrix, (int(width * scaling_factor), int(height * scaling_factor)))
cv2.imshow('Scaled Image', scaled_image)

# Translation
translated_image = cv2.warpAffine(image, translation_matrix, (width, height))
cv2.imshow('Translated Image', translated_image)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()