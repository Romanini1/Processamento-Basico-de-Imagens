import cv2
import numpy as np

img = cv2.imread("original_segmentada.jpg", 0)
kernel = np.ones((5, 5), np.uint8)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
cv2.imwrite("resultado.jpg", closing)