import numpy as np
import cv2
import matplotlib.pyplot as plt
import math
import os
import glob

import GlobalValue as g
import hyouka
import DWMfilter


firsttext = "01"
dirtext = "./randomNoise/Set12/"
NoiseRatio = 10
filterSize = 5

os.chdir(dirtext)
str_imgs = glob.glob('*n')
str_imgs = ("01n","02n","03n","04n","05n","06n","07n","08n","09n","010n","011n","012n")

PSNRText = open("DWM_PSNR_Result.txt","w")
F_valueText = open("DWM_F_Result.txt","w")
PSNRText.write("10~30"+"\n")
F_valueText.write("10~30"+"\n")
for tex in range(len(str_imgs)):
    os.chdir(str_imgs[tex])
    print(str_imgs[tex])
    PSNRText.write(str_imgs[tex]+" & ")
    F_valueText.write(str_imgs[tex]+" & ")
    for i in range(3):
        NoiseRatio = (i+1)*10
        print("Noise:"+str(NoiseRatio)+"%")
        OrijinalImage = cv2.imread("orijinal.png",0)
        inputImage = cv2.imread("Noise"+str(NoiseRatio)+"%.png",0)
        g.TruenoiseBinary = cv2.imread("noiseBinary"+str(NoiseRatio)+"%.png",0)
        g.img_binary = g.TruenoiseBinary.copy()
        g.baseBinary = np.zeros(g.TruenoiseBinary.shape)

        Threshold = 510
        median_image = inputImage.copy()
        for k in range(10):
            print(str(k+1)+"回目")
            median_image = DWMfilter.DWM(median_image,size = 3,Threshold=Threshold)
            print("PSNR : "+format(cv2.PSNR(OrijinalImage,median_image),'.2f'))
            Threshold = Threshold * 0.8
            cv2.imwrite("DWM"+str(NoiseRatio)+str(k)+"times.png",median_image)
            g.baseBinary = hyouka.Update_imgBinary(baseBinary=g.baseBinary, addBinary=g.img_binary)
            hyouka.hyou(g.TruenoiseBinary,g.baseBinary)
            
        #median_image = DWMfilter.DWM(inputImage.copy())
        median_image=median_image.astype(np.uint8)
        print("PSNR : "+format(cv2.PSNR(OrijinalImage,median_image),'.2f'))
        PSNRText.write(format(cv2.PSNR(OrijinalImage,median_image),'.2f') + " & ")
        F_valueText.write(hyouka.hyou(g.TruenoiseBinary,g.img_binary)+" & ")

    PSNRText.write("\\\\"+"\n")
    F_valueText.write("\\\\"+"\n")
    os.chdir("../")

PSNRText.write("\n40~60"+"\n")
F_valueText.write("\n40~60"+"\n")
for tex in range(len(str_imgs)):
    os.chdir(str_imgs[tex])
    print(str_imgs[tex])
    PSNRText.write(str_imgs[tex]+" & ")
    F_valueText.write(str_imgs[tex]+" & ")
    for i in range(3):
        NoiseRatio = (i+4)*10
        print("Noise:"+str(NoiseRatio)+"%")
        OrijinalImage = cv2.imread("orijinal.png",0)
        inputImage = cv2.imread("Noise"+str(NoiseRatio)+"%.png",0)
        g.TruenoiseBinary = cv2.imread("noiseBinary"+str(NoiseRatio)+"%.png",0)
        g.img_binary = g.TruenoiseBinary.copy()
        g.baseBinary = np.zeros(g.TruenoiseBinary.shape)

        Threshold = 510
        median_image = inputImage.copy()
        for k in range(10):
            print(str(k+1)+"回目")
            median_image = DWMfilter.DWM(median_image,size = 5,Threshold=Threshold)
            print("PSNR : "+format(cv2.PSNR(OrijinalImage,median_image),'.2f'))
            Threshold = Threshold * 0.8
            cv2.imwrite("DWM"+str(NoiseRatio)+str(k)+"times.png",median_image)
            g.baseBinary = hyouka.Update_imgBinary(baseBinary=g.baseBinary, addBinary=g.img_binary)
            hyouka.hyou(g.TruenoiseBinary,g.baseBinary)
            
        #median_image = DWMfilter.DWM(inputImage.copy())
        median_image=median_image.astype(np.uint8)
        print("PSNR : "+format(cv2.PSNR(OrijinalImage,median_image),'.2f'))
        PSNRText.write(format(cv2.PSNR(OrijinalImage,median_image),'.2f') + " & ")
        F_valueText.write(hyouka.hyou(g.TruenoiseBinary,g.img_binary)+" & ")

    PSNRText.write("\\\\"+"\n")
    F_valueText.write("\\\\"+"\n")
    os.chdir("../")

PSNRText.close()
F_valueText.close()