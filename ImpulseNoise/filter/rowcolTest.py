import custom_random_rowcol
import cv2
import numpy as np


a = np.array([[121,0,255],[255,129,0],[0,253,142]])
b = np.array([[121,0,255],[255,255,0],[0,253,142]])

imagea = cv2.imread("C:/Users/dqxre/Documents/GitHub/OpenCV-Study/ImpulseNoise/Images/Airplane.bmp",1)
imageb = cv2.imread("C:/Users/dqxre/Documents/GitHub/OpenCV-Study/ImpulseNoise/Images/Girl.bmp",1)

cv2.imshow("dst1",imagea)

cv2.imshow("dst2",imageb)


cv2.waitKey(0)

cv2.destroyAllWindows()