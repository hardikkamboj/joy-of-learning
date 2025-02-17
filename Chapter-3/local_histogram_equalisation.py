import cv2
import numpy as np
import matplotlib.pyplot as plt

def local_histogram_equalization(img, tile_size=5):
    if len(img.shape) == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    h, w = img.shape
    img_equalized = np.zeros_like(img)
    step_h = h // tile_size
    step_w = w // tile_size
    
    for i in range(0, h, step_h):
        for j in range(0, w, step_w):
            tile = img[i:i+step_h, j:j+step_w]
            img_equalized[i:i+step_h, j:j+step_w] = cv2.equalizeHist(tile)
    
    return img_equalized

def update_trackbar(val):
    tile_size = max(val, 1)
    img_equalized = local_histogram_equalization(img, tile_size)
    cv2.imshow('Tile Size', img_equalized)

def main():
    global img
    img_path = "../images/Fig0326(a)(embedded_square_noisy_512).tif"
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    
    cv2.namedWindow('Local Histogram Equalization')
    cv2.createTrackbar('Tile Size', 'Local Histogram Equalization', 8, 32, update_trackbar)
    
    update_trackbar(8)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
