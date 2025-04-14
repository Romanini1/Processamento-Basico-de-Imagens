import cv2

img = cv2.imread("original.jpg")
resized = cv2.resize(img, (300, 300))
cv2.imwrite("resultado.jpg", resized)