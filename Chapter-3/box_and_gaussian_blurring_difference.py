import cv2
import numpy as np

def nothing(x):
    pass

def main():
    # Load an image
    #image_path = input("Enter path to image file: ")

    image_path = "potrait2.jpeg"
    
    original_image = cv2.imread(image_path)

    # Create windows
    cv2.namedWindow('Original Image')
    cv2.namedWindow('Box Blur')
    cv2.namedWindow('Gaussian Blur')

    # Create trackbars
    # For box blur - odd values from 1 to 51
    cv2.createTrackbar('Kernel Size', 'Box Blur', 1, 25, nothing)
    
    # For Gaussian blur - odd values from 1 to 51
    cv2.createTrackbar('Kernel Size', 'Gaussian Blur', 1, 25, nothing)
    # Standard deviation for Gaussian blur
    cv2.createTrackbar('Standard Deviation (σ)', 'Gaussian Blur', 1, 20, nothing)

    while True:
        # Get current positions of trackbars
        box_kernel = 2 * cv2.getTrackbarPos('Kernel Size', 'Box Blur') + 1
        gauss_kernel = 2 * cv2.getTrackbarPos('Kernel Size', 'Gaussian Blur') + 1
        sigma = cv2.getTrackbarPos('Standard Deviation (σ)', 'Gaussian Blur')
        if sigma == 0:  # Avoid division by zero
            sigma = 1

        # Apply blurs
        box_blurred = cv2.blur(original_image, (box_kernel, box_kernel))
        gaussian_blurred = cv2.GaussianBlur(original_image, (gauss_kernel, gauss_kernel), sigma)

        # Add text to images to show current kernel size
        box_text_img = box_blurred.copy()
        gauss_text_img = gaussian_blurred.copy()
        
        # Place text on images
        cv2.putText(box_text_img, f'Kernel Size: {box_kernel}x{box_kernel}', 
                    (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        
        cv2.putText(gauss_text_img, f'Kernel Size: {gauss_kernel}x{gauss_kernel}, Sigma: {sigma}', 
                    (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        # Display images
        cv2.imshow('Original Image', original_image)
        cv2.imshow('Box Blur', box_text_img)
        cv2.imshow('Gaussian Blur', gauss_text_img)

        # Break loop on ESC key
        key = cv2.waitKey(1) & 0xFF
        if key == 27:  # ESC key
            break

    # Clean up
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()