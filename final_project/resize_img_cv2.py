import cv2
import numpy as np
img = cv2.imread('./ken_image.jpg')



# 행 : Height, 열:width
height, width = img.shape[:2]
# Manual Size지정
zoom1 = cv2.resize(img, (224, 224), interpolation=cv2.INTER_CUBIC)


cv2.imshow('h', zoom1)

cv2.imwrite('scaling.jpg', zoom1)