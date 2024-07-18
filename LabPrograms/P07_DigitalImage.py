import cv2

# Read the image
image = cv2.imread('Data/random-1574391.jpg')

# Get the dimensions of the image
height, width, channels = image.shape

# Split the image into four quadrants
up_quadrant = image[0:height//2, 0:width//2]
down_quadrant = image[height//2:height, 0:width//2]
right_quadrant = image[0:height//2, width//2:width]
left_quadrant = image[height//2:height, width//2:width]

# Display the original image
cv2.imshow('Original Image', image)

# Display the quadrants
cv2.imshow('Up Quadrant', up_quadrant)
cv2.imshow('Down Quadrant', down_quadrant)
cv2.imshow('Right Quadrant', right_quadrant)
cv2.imshow('Left Quadrant', left_quadrant)

# Wait for a key press to close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()