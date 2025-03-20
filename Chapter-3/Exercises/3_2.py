import cv2
import numpy as np
import matplotlib.pyplot as plt

# Define the transformation function
def intensity_transform(r, a, k):
    return 1 / (1 + np.exp(-a * (r - k)))

# Callback function for trackbar changes
def update(_):
    a = cv2.getTrackbarPos("Steepness (a)", "Control Panel") / 10  # Scale factor
    k = cv2.getTrackbarPos("Midpoint (k)", "Control Panel") / 255  # Normalize k to [0,1]

    # Generate the transformation curve
    r = np.linspace(0, 1, 400)  # Input values from 0 to 1
    s = intensity_transform(r, a, k)  # Compute output values

    # Plot the transformation function
    plt.figure(figsize=(5, 4))
    plt.plot(r, s, linewidth=2, color='b', label="T(r) = 1 / (1 + e^(-a (r - k)))")

    # Labels and titles
    plt.xlabel(r'$r$ (Input Intensity)', fontsize=12)
    plt.ylabel(r'$s = T(r)$ (Output Intensity)', fontsize=12)
    plt.title("Sigmoid-like Intensity Transformation", fontsize=14)

    # Add reference lines for midpoint
    plt.axvline(k, linestyle='dashed', color='black', alpha=0.6)
    plt.axhline(intensity_transform(k, a, k), linestyle='dashed', color='black', alpha=0.6)

    # Show plot
    plt.grid(True, linestyle='dotted', alpha=0.7)
    plt.legend()
    plt.show(block=False)
    plt.pause(0.1)

# Create OpenCV window
cv2.namedWindow("Control Panel")

# Create trackbars
cv2.createTrackbar("Steepness (a)", "Control Panel", 10, 500, update)  # Steepness factor
cv2.createTrackbar("Midpoint (k)", "Control Panel", 128, 255, update)  # Midpoint shift

# Show initial plot
update(0)

# Keep the window open
cv2.waitKey(0)
cv2.destroyAllWindows()
