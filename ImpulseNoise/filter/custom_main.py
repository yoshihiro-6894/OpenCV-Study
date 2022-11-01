import numpy as np
import cv2
import matplotlib.pyplot as plt
import math
import os
import glob

import GlobalValue as g
import custom_random_rowcol
import ROAD

firsttext = "01"
dirtext = "./randomNoise/Set12/"
NoiseRatio = 10
filterSize = 5

os.chdir(dirtext)
str_imgs=glob.glob('*n')


PSNR_file = open("Size"+str(filterSize)+"PSNRresult.txt","w")


for i in range(6):
    NoiseRatio = (i+1)*10
    print("Noise:"+str(NoiseRatio)+"%")
    PSNR_file.write("Noise:"+str(NoiseRatio)+"%\n")
    for tex in range(len(str_imgs)):
        os.chdir(str_imgs[tex])
        print(str_imgs[tex])
        OrijinalImage = cv2.imread("orijinal.png",0)
        inputImage = cv2.imread("Noise"+str(NoiseRatio)+"%.png",0)
        g.TruenoiseBinary = cv2.imread("noiseBinary"+str(NoiseRatio)+"%.png",0)
        
        median_image = custom_random_rowcol.median_filter(inputImage,size=filterSize)
        median_image = median_image.astype(np.uint8)
        print("PSNR:"+str(cv2.PSNR(OrijinalImage,median_image)))
        print(np.round(cv2.PSNR(OrijinalImage,median_image),decimals=2))
        PSNR_file.write(str_imgs[tex]+" &"+str(np.round(cv2.PSNR(OrijinalImage,median_image),decimals=2))+"\n")
        cv2.imwrite("custom_random_rowcol"+str(NoiseRatio)+".png",median_image)


        print("\n")
        os.chdir("../")
    PSNR_file.write("\n")

print(str_imgs)

PSNR_file.close()
