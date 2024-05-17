import cv2
import numpy as np

# Load an image from file
image = cv2.imread('/Users/thebiggestnutcase/Documents/VSCode/21CSL66_CG_Lab/SimplePrograms/random-1574391.jpg')

# Ensure the image was loaded
if image is None:
    print("Error: Could not load image.")
    exit()

# Function to translate an image
def translate(image, tx, ty):
    height, width = image.shape[:2]
    translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])
    translated_image = cv2.warpAffine(image, translation_matrix, (width, height))
    return translated_image

# Function to rotate an image
def rotate(image, angle, scale=1.0):
    height, width = image.shape[:2]
    center = (width // 2, height // 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
    return rotated_image

# Function to scale an image
def scale(image, scale_x, scale_y):
    height, width = image.shape[:2]
    scaled_image = cv2.resize(image, (int(width * scale_x), int(height * scale_y)))
    return scaled_image

# Perform translations, rotations, and scalings
translated_image = translate(image, 100, 50)  # Translate right by 100 pixels and down by 50 pixels
rotated_image = rotate(image, 45)             # Rotate by 45 degrees
scaled_image = scale(image, 1.5, 1.5)         # Scale by 1.5 times

# Display the results
cv2.imshow('Original Image', image)
cv2.imshow('Translated Image', translated_image)
cv2.imshow('Rotated Image', rotated_image)
cv2.imshow('Scaled Image', scaled_image)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
