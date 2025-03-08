import cv2
import numpy as np

# Load the image
img_path = "images/Fig0340(a)(dipxe_text).tif"

image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)  # Convert to grayscale

# Apply Gaussian Blur
blurred = cv2.GaussianBlur(image, (31, 31), 5)

# Callback function for trackbar
def update_sharpness(strength):
    strength = strength / 10.0  # Scale strength to a suitable range
    sharpened = cv2.addWeighted(image, 1.0 + strength, blurred, -strength, 0)

    # Stack original and sharpened images side by side for comparison
    combined = np.hstack((image, sharpened))
    
    # Show updated result
    cv2.imshow("Unsharp Masking (Left: Original, Right: Sharpened)", combined)

# Create window
cv2.namedWindow("Unsharp Masking (Left: Original, Right: Sharpened)")

# Create trackbar (values from 0 to 50, mapped to 0.0 to 5.0)
cv2.createTrackbar("Strength", "Unsharp Masking (Left: Original, Right: Sharpened)", 10, 50, update_sharpness)

# Initialize display
update_sharpness(10)  # Default strength

cv2.waitKey(0)
cv2.destroyAllWindows()
