import cv2
import numpy as np

img = cv2.imread("noise.jpg",0)
print(type(img))

cv2.imshow("a",img)

dst = cv2.medianBlur(img,ksize=5)

cv2.imshow("dst",dst)

cv2.waitKey(0)
cv2.destroyAllWindows()