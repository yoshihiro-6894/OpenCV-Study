import numpy as np
import cv2
import matplotlib.pyplot as plt
import math
import os
import glob

import GlobalValue as g
import testBilateral
import hyouka
import visual_hyouka
import get_LCI
import padding
import custom_random1
import custom_random_rowcol

firsttext = "01"
dirtext = "./randomNoise/Set12/"
NoiseRatio = 10
filterSize = 5

os.chdir(dirtext)
str_imgs = glob.glob('*n')

PSNRText = open("Custom1_PSNR_Result.txt","w")
F_valueText = open("Custom1_F_Result.txt","w")
PSNRText.write("10~30"+"\n")
F_valueText.write("10~30"+"\n")
for tex in range(len(str_imgs)):
    os.chdir(str_imgs[tex])
    print(str_imgs[tex])
    PSNRText.write(str_imgs[tex]+" & ")
    F_valueText.write(str_imgs[tex]+" & ")
    for i in range(3):
        NoiseRatio = (i+1)*10
        print(NoiseRatio)
        OrijinalImage = cv2.imread("orijinal.png",0)
        inputImage = cv2.imread("Noise"+str(NoiseRatio)+"%.png",0)
        g.TruenoiseBinary = cv2.imread("noiseBinary"+str(NoiseRatio)+"%.png",0)
        g.img_binary = g.TruenoiseBinary.copy()

        median_image = custom_random1.median_filter(inputImage.copy())
        median_image=median_image.astype(np.uint8)
        print("PSNR : "+format(cv2.PSNR(OrijinalImage,median_image),'.2f'))
        PSNRText.write(format(cv2.PSNR(OrijinalImage,median_image),'.2f') + " & ")
        F_valueText.write(hyouka.hyou(g.TruenoiseBinary,g.img_binary)+" & ")


    PSNRText.write("\\\\"+"\n")
    F_valueText.write("\\\\"+"\n")
    os.chdir("../")
PSNRText.write("\n"+"4~60"+"\n")
F_valueText.write("\n"+"4~60"+"\n")
for tex in range(len(str_imgs)):
    os.chdir(str_imgs[tex])
    print(str_imgs[tex])
    PSNRText.write(str_imgs[tex]+" & ")
    F_valueText.write(str_imgs[tex]+" & ")
    for i in range(3):
        NoiseRatio = (i+4)*10
        print(NoiseRatio)
        OrijinalImage = cv2.imread("orijinal.png",0)
        inputImage = cv2.imread("Noise"+str(NoiseRatio)+"%.png",0)
        g.TruenoiseBinary = cv2.imread("noiseBinary"+str(NoiseRatio)+"%.png",0)
        g.img_binary = g.TruenoiseBinary.copy()

        median_image = custom_random1.median_filter(inputImage.copy())
        median_image=median_image.astype(np.uint8)
        print("PSNR : "+format(cv2.PSNR(OrijinalImage,median_image),'.2f'))
        PSNRText.write(format(cv2.PSNR(OrijinalImage,median_image),'.2f') + " & ")
        F_valueText.write(hyouka.hyou(g.TruenoiseBinary,g.img_binary)+" & ")


    PSNRText.write("\\\\"+"\n")
    F_valueText.write("\\\\"+"\n")
    os.chdir("../")

PSNRText.close()
F_valueText.close()



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
        #print(cv2.PSNR(OrijinalImage,perfect))


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



