import cv2
import numpy as np
import math
import os


dirtext = "./randomNoise/Set12/08n/"

os.chdir(dirtext)

input_img = cv2.imread("orijinal.png",0)

print(input_img.shape)

outimg= cv2.resize(input_img,dsize=(256,256))

print(outimg.shape)


cv2.imwrite("orijinal512.png",input_img)
cv2.imwrite("orijinal.png",outimg)