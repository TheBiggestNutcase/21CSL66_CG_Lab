import cv2

def main():
    # Load an image
    image = cv2.imread('example.png')

    if image is None:
        print("Error: Could not open or find the image.")
        return

    # Display the image
    cv2.imshow('Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
