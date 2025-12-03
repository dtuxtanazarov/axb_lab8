import cv2
import numpy as np

image = cv2.imread('togrey2.jpg')

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#Hello
R = image[:, :, 0].astype(np.float32)
G = image[:, :, 1].astype(np.float32)
B = image[:, :, 2].astype(np.float32)

sum_rgb = R + G + B
#5-yuklash
sum_rgb[sum_rgb == 0] = 1e-6

r = R / sum_rgb
g = G / sum_rgb
b = B / sum_rgb

T = r * R + g * G + b * B

gray_image = T.astype(np.uint8)

cv2.imshow('Custom Grayscale', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('kulrang_natiija.jpg', gray_image)
