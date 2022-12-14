import numpy as np
import cv2
import matplotlib.pyplot as plt
import math
import os
import glob

firsttext = "01"
dirtext = "./randomNoise/Set12/"
NoiseRatio = 10
filterSize = 5

os.chdir(dirtext)
str_imgs = glob.glob('*n')




for i in range(6):
    NoiseRatio = (i+1)*10
    print("Noise:"+str(NoiseRatio)+"%")

    for tex in range(len(str_imgs)):
        os.chdir(str_imgs[tex])
        print(str_imgs[tex])
        OrijinalImage = cv2.imread("orijinal.png",0)
        inputImage = cv2.imread("Noise"+str(NoiseRatio)+"%.png",0)
        PSNRs = np.empty(0)

        perfect = cv2.imread("perfect" + str(NoiseRatio) + ".png",0)
        print(cv2.PSNR(OrijinalImage,perfect))


        '''
        median_image = cv2.imread("custom1_median_output"+str(NoiseRatio)+".png",0)
        print(cv2.PSNR(OrijinalImage,median_image))
        a = cv2.PSNR(OrijinalImage,median_image)
        PSNRs = np.append(PSNRs,a)

        median_image = cv2.imread("custom_random_rowcol"+str(NoiseRatio)+".png",0)
        print(cv2.PSNR(OrijinalImage,median_image))
        a = cv2.PSNR(OrijinalImage,median_image)
        PSNRs = np.append(PSNRs,a)

        median_image = cv2.imread("custom_try"+str(NoiseRatio)+".png",0)
        print(cv2.PSNR(OrijinalImage,median_image))
        a = cv2.PSNR(OrijinalImage,median_image)
        PSNRs = np.append(PSNRs,a)
        
        median_image = cv2.imread("custom_tryLCI"+str(NoiseRatio)+".png",0)
        print(cv2.PSNR(OrijinalImage,median_image))
        a = cv2.PSNR(OrijinalImage,median_image)
        PSNRs = np.append(PSNRs,a)

        median_image = cv2.imread("custom_tryLCIrowcol"+str(NoiseRatio)+".png",0)
        print(cv2.PSNR(OrijinalImage,median_image))
        a = cv2.PSNR(OrijinalImage,median_image)
        PSNRs = np.append(PSNRs,a)
        '''


        os.chdir("../")
        print("\n")




