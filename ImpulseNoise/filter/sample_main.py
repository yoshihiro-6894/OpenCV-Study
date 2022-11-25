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
import custom_try

firsttext = "01"
dirtext = "./randomNoise/Set12/"
NoiseRatio = 10
filterSize = 5

os.chdir(dirtext)
str_imgs = glob.glob('*n')

g.count=0


for i in range(6):
    NoiseRatio = (i+1)*10
    print("Noise:"+str(NoiseRatio)+"%")

    for tex in range(len(str_imgs)):
        os.chdir(str_imgs[tex])
        print(str_imgs[tex])
        OrijinalImage = cv2.imread("orijinal.png",0)
        inputImage = cv2.imread("Noise"+str(NoiseRatio)+"%.png",0)
        g.TruenoiseBinary = cv2.imread("noiseBinary"+str(NoiseRatio)+"%.png",0)
        g.img_binary = g.TruenoiseBinary.copy()

        '''
        median_image = custom_random1.median_filter(inputImage)
        visual_hyouka.visual_fn_fp(g.TruenoiseBinary,g.img_binary,strNoiseRatio=str(NoiseRatio),methodName="custom_random1")
        median_image = median_image.astype(np.uint8)
        cv2.imwrite("custom1_median_output"+str(NoiseRatio)+".png",median_image)


        median_image = custom_random_rowcol.median_filter(inputImage,size=5)
        visual_hyouka.visual_fn_fp(g.TruenoiseBinary,g.img_binary,strNoiseRatio=str(NoiseRatio),methodName="rowcol")
        median_image=median_image.astype(np.uint8)
        cv2.imwrite("custom_random_rowcol"+str(NoiseRatio)+".png",median_image)
        '''

        '''
        g.img_binary = get_LCI.detectNoise(inputImage)
        visual_hyouka.visual_fn_fp(g.TruenoiseBinary,g.img_binary,strNoiseRatio=str(NoiseRatio),methodName="testBi")
        hyouka.hyou(g.TruenoiseBinary,g.img_binary)
        '''

        median_image = custom_try.detecter(inputImage)
        cv2.imwrite("custom_tryLCIrowcol"+str(NoiseRatio)+".png",median_image)
        print(cv2.PSNR(OrijinalImage,median_image))
        hyouka.hyou(g.TruenoiseBinary,g.img_binary)


        
        os.chdir("../")
        print("\n")




