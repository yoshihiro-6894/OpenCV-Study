
import numpy as np
import cv2
import matplotlib.pyplot as plt
import math
import os
import glob

import GlobalValue as g

import ASWM
import visual_hyouka
import hyouka

firsttext = "01"
dirtext = "./randomNoise/Set12/"
NoiseRatio = 10
filterSize = 5

os.chdir(dirtext)
str_imgs = glob.glob('*n')

g.count=0
print(str_imgs)
#str_imgs = ("02n","03n","08n","010n","012n")
#resultText = open("F_valueResult.txt","w")
#PSNRText = open("PSNR_Edge_Result.txt","w")
for i in range(6):
    NoiseRatio = (i+1)*10
    print("Noise:"+str(NoiseRatio)+"%")

    #resultText.write(str(NoiseRatio)+" & ")
    #PSNRText.write(str(NoiseRatio)+" & ")

    for tex in range(len(str_imgs)):
        os.chdir(str_imgs[tex])
        print(str_imgs[tex])
        OrijinalImage = cv2.imread("orijinal.png",0)
        inputImage = cv2.imread("Noise"+str(NoiseRatio)+"%.png",0)
        g.TruenoiseBinary = cv2.imread("noiseBinary"+str(NoiseRatio)+"%.png",0)
        g.img_binary = g.TruenoiseBinary.copy()

        alpha=20
        print("ASWM")
        print("1回目")
        median_image = ASWM.ASWMfilter(inputImage,alpha=alpha)
        median_image = median_image.astype(np.uint8)
        alpha=alpha*0.8
        print("PSNR : "+format(cv2.PSNR(OrijinalImage,median_image),'.2f'))
        cv2.imwrite("ASWM"+str(NoiseRatio)+"_1+times"+".png",median_image)
        g.baseBinary = g.img_binary.copy()
        hyouka.hyou(g.TruenoiseBinary,g.baseBinary)
        visual_hyouka.visual_fn_fp(g.TruenoiseBinary,g.img_binary,strNoiseRatio=str(NoiseRatio),methodName="ASWM_1")
        
        print("2回目")
        median_image = ASWM.ASWMfilter(median_image,alpha=alpha)
        median_image = median_image.astype(np.uint8)
        alpha=alpha*0.8
        print("PSNR : "+format(cv2.PSNR(OrijinalImage,median_image),'.2f'))
        cv2.imwrite("ASWM"+str(NoiseRatio)+"_2+times"+".png",median_image)
        g.baseBinary = hyouka.Update_imgBinary(baseBinary=g.baseBinary, addBinary=g.img_binary)
        hyouka.hyou(g.TruenoiseBinary,g.baseBinary)
        visual_hyouka.visual_fn_fp(g.TruenoiseBinary,g.img_binary,strNoiseRatio=str(NoiseRatio),methodName="ASWM_2")
        
        print("3回目")
        median_image = ASWM.ASWMfilter(median_image,alpha=alpha)
        median_image = median_image.astype(np.uint8)
        alpha=alpha*0.8
        print("PSNR : "+format(cv2.PSNR(OrijinalImage,median_image),'.2f'))
        cv2.imwrite("ASWM"+str(NoiseRatio)+"_3+times"+".png",median_image)
        g.baseBinary = hyouka.Update_imgBinary(baseBinary=g.baseBinary, addBinary=g.img_binary)
        hyouka.hyou(g.TruenoiseBinary,g.baseBinary)
        visual_hyouka.visual_fn_fp(g.TruenoiseBinary,g.img_binary,strNoiseRatio=str(NoiseRatio),methodName="ASWM_3")

        print("4回目")
        median_image = ASWM.ASWMfilter(median_image,alpha=alpha)
        median_image = median_image.astype(np.uint8)
        alpha=alpha*0.8
        print("PSNR : "+format(cv2.PSNR(OrijinalImage,median_image),'.2f'))
        cv2.imwrite("ASWM"+str(NoiseRatio)+"_4+times"+".png",median_image)
        g.baseBinary = hyouka.Update_imgBinary(baseBinary=g.baseBinary, addBinary=g.img_binary)
        hyouka.hyou(g.TruenoiseBinary,g.baseBinary)
        visual_hyouka.visual_fn_fp(g.TruenoiseBinary,g.img_binary,strNoiseRatio=str(NoiseRatio),methodName="ASWM_4")

        print("5回目")
        median_image = ASWM.ASWMfilter(median_image,alpha=alpha)
        median_image = median_image.astype(np.uint8)
        alpha=alpha*0.8
        print("PSNR : "+format(cv2.PSNR(OrijinalImage,median_image),'.2f'))
        cv2.imwrite("ASWM"+str(NoiseRatio)+"_5+times"+".png",median_image)
        g.baseBinary = hyouka.Update_imgBinary(baseBinary=g.baseBinary, addBinary=g.img_binary)
        hyouka.hyou(g.TruenoiseBinary,g.baseBinary)
        visual_hyouka.visual_fn_fp(g.TruenoiseBinary,g.img_binary,strNoiseRatio=str(NoiseRatio),methodName="ASWM_5")

        print("6回目")
        median_image = ASWM.ASWMfilter(median_image,alpha=alpha)
        median_image = median_image.astype(np.uint8)
        alpha=alpha*0.8
        print("PSNR : "+format(cv2.PSNR(OrijinalImage,median_image),'.2f'))
        cv2.imwrite("ASWM"+str(NoiseRatio)+"_6+times"+".png",median_image)
        g.baseBinary = hyouka.Update_imgBinary(baseBinary=g.baseBinary, addBinary=g.img_binary)
        hyouka.hyou(g.TruenoiseBinary,g.baseBinary)
        visual_hyouka.visual_fn_fp(g.TruenoiseBinary,g.img_binary,strNoiseRatio=str(NoiseRatio),methodName="ASWM_6")

        print("7回目")
        median_image = ASWM.ASWMfilter(median_image,alpha=alpha)
        median_image = median_image.astype(np.uint8)
        alpha=alpha*0.8
        print("PSNR : "+format(cv2.PSNR(OrijinalImage,median_image),'.2f'))
        cv2.imwrite("ASWM"+str(NoiseRatio)+"_7+times"+".png",median_image)
        g.baseBinary = hyouka.Update_imgBinary(baseBinary=g.baseBinary, addBinary=g.img_binary)
        hyouka.hyou(g.TruenoiseBinary,g.baseBinary)
        visual_hyouka.visual_fn_fp(g.TruenoiseBinary,g.img_binary,strNoiseRatio=str(NoiseRatio),methodName="ASWM_7")

        print("8回目")
        median_image = ASWM.ASWMfilter(median_image,alpha=alpha)
        median_image = median_image.astype(np.uint8)
        alpha=alpha*0.8
        print("PSNR : "+format(cv2.PSNR(OrijinalImage,median_image),'.2f'))
        cv2.imwrite("ASWM"+str(NoiseRatio)+"_8+times"+".png",median_image)
        g.baseBinary = hyouka.Update_imgBinary(baseBinary=g.baseBinary, addBinary=g.img_binary)
        hyouka.hyou(g.TruenoiseBinary,g.baseBinary)
        visual_hyouka.visual_fn_fp(g.TruenoiseBinary,g.img_binary,strNoiseRatio=str(NoiseRatio),methodName="ASWM_8")

        print("9回目")
        median_image = ASWM.ASWMfilter(median_image,alpha=alpha)
        median_image = median_image.astype(np.uint8)
        alpha=alpha*0.8
        print("PSNR : "+format(cv2.PSNR(OrijinalImage,median_image),'.2f'))
        cv2.imwrite("ASWM"+str(NoiseRatio)+"_9+times"+".png",median_image)
        g.baseBinary = hyouka.Update_imgBinary(baseBinary=g.baseBinary, addBinary=g.img_binary)
        hyouka.hyou(g.TruenoiseBinary,g.baseBinary)
        visual_hyouka.visual_fn_fp(g.TruenoiseBinary,g.img_binary,strNoiseRatio=str(NoiseRatio),methodName="ASWM_9")

        print("10回目")
        median_image = ASWM.ASWMfilter(median_image,alpha=alpha)
        median_image = median_image.astype(np.uint8)
        alpha=alpha*0.8
        print("PSNR : "+format(cv2.PSNR(OrijinalImage,median_image),'.2f'))
        cv2.imwrite("ASWM"+str(NoiseRatio)+"_10+times"+".png",median_image)
        g.baseBinary = hyouka.Update_imgBinary(baseBinary=g.baseBinary, addBinary=g.img_binary)
        hyouka.hyou(g.TruenoiseBinary,g.baseBinary)
        visual_hyouka.visual_fn_fp(g.TruenoiseBinary,g.img_binary,strNoiseRatio=str(NoiseRatio),methodName="ASWM_10")
        

        #visual_hyouka.visual_fn_fp(g.TruenoiseBinary,g.img_binary,strNoiseRatio=str(NoiseRatio),methodName="custom_random1")
        median_image = median_image.astype(np.uint8)
        #cv2.imwrite("custom1_median_output"+str(NoiseRatio)+".png",median_image)
        
        
        os.chdir("../")
        print("\n")
    #resultText.write("\n")
    #PSNRText.write("\n")



#resultText.close()
#PSNRText.close()
