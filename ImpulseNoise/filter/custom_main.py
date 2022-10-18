import numpy as np
import cv2
import matplotlib.pyplot as plt
import math
import os
import glob

import GlobalValue as g
import custom_random_rowcol

firsttext="01"
dirtext="./randomNoise/Set12/"
NoiseRatio="10"

os.chdir(dirtext)
str_imgs=glob.glob('*n')


f = open("result.txt","w")

for tex in range(len(str_imgs)):
    os.chdir(str_imgs[tex])
    print(str_imgs[tex])
    OrijinalImage = cv2.imread("orijinal.png",0)
    inputImage = cv2.imread("Noise"+NoiseRatio+"%.png",0)
    g.TruenoiseBinary = cv2.imread("noiseBinary"+NoiseRatio+"%.png",0)

    median_image = custom_random_rowcol.median_filter(inputImage,size=5)
    median_image = median_image.astype(np.uint8)
    print("PSNR:"+str(cv2.PSNR(OrijinalImage,median_image)))
    f.write(str_imgs[tex]+" &"+str(cv2.PSNR(OrijinalImage,median_image))+"\n")
    cv2.imwrite("custom_random_rowcol"+NoiseRatio+".png",median_image)

    print("\n")
    os.chdir("../")

print(str_imgs)

f.close()

'''
OrijinalImage = cv2.imread(dirtext+firsttext+"n/orijinal.png",0)
inputImage = cv2.imread(dirtext+firsttext+"n/Noise"+NoiseRatio+"%.png",0)
g.TruenoiseBinary = cv2.imread(dirtext+firsttext+"n/noiseBinary"+NoiseRatio+"%.png",0)
'''