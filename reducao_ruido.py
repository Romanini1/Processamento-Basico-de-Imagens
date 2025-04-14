import cv2

img = cv2.imread("original.jpg")
img_denoised = cv2.GaussianBlur(img, (5, 5), 0)
cv2.imwrite("resultado.jpg", img_denoised)