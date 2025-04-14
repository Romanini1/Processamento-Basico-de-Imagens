import cv2

img = cv2.imread("original.jpg")
img_enhanced = cv2.convertScaleAbs(img, alpha=1.5, beta=30)
cv2.imwrite("resultado.jpg", img_enhanced)