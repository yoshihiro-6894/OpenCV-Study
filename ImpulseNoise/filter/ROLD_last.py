import numpy as np
import cv2
import matplotlib.pyplot as plt
import math
import os
import glob

import GlobalValue as g
import custom_random_rowcol
import ROLD
import hyouka
import visual_hyouka

firsttext = "01"
dirtext = "./randomNoise/Set12/"
NoiseRatio = 10
filterSize = 5

os.chdir(dirtext)
str_imgs=glob.glob('*n')
str_imgs = ("01n","02n","03n","04n","05n","06n","07n","08n","09n","010n","011n","012n")
print(str_imgs)
ddds = ("6","8","9","10","11","12")

for i in range(6):
    NoiseRatio = (i+1)*10
    print("Noise:"+str(NoiseRatio)+"%")


    for tex in range(len(str_imgs)):
        os.chdir(str_imgs[tex])
        print(str_imgs[tex]+"Noise:"+str(NoiseRatio)+"%")
        OrijinalImage = cv2.imread("orijinal.png",0)
        inputImage = cv2.imread("Noise"+str(NoiseRatio)+"%.png",0)
        g.TruenoiseBinary = cv2.imread("noiseBinary"+str(NoiseRatio)+"%.png",0)
        g.img_binary = g.TruenoiseBinary.copy()
        g.baseBinary = np.zeros(g.TruenoiseBinary.shape)
        baseBinary = cv2.imread("ROLD_Binary"+str(NoiseRatio)+"_"+ddds[i]+"+times.png",0)

        baseBinary = (np.where(baseBinary>0, 1, 0))

        sum_median_image = ROLD.median_filter(inputImage,baseBinary)
        print("Last"+format(cv2.PSNR(OrijinalImage,sum_median_image),'.2f'))
        cv2.imwrite("ROLD_Last"+str(NoiseRatio)+".png",sum_median_image)

        # sum_median_image = ROLD.median_filter(sum_median_image,baseBinary)
        # print("Last"+format(cv2.PSNR(OrijinalImage,sum_median_image),'.2f'))
        # cv2.imwrite("ROLD_Last2"+str(NoiseRatio)+".png",sum_median_image)

        sum_median_image = ROLD.weight_median_filter(inputImage,baseBinary)
        print("Last_Weight"+format(cv2.PSNR(OrijinalImage,sum_median_image),'.2f'))
        cv2.imwrite("ROLD_Last_Weight"+str(NoiseRatio)+".png",sum_median_image)
        print("\n")

        os.chdir("../")