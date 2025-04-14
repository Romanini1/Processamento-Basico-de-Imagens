import cv2

img = cv2.imread("original.jpg", 0)
edges = cv2.Canny(img, 100, 200)
cv2.imwrite("resultado.jpg", edges)