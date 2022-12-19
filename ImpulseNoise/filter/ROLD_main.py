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

def plot_fig(inputImage, times=1):
    noiseROLD=np.empty(0)
    trueROLD=np.empty(0)
    noiseROLD_list = noiseROLD.tolist()
    trueROLD_list = trueROLD.tolist()

    rold = ROLD.ROLD(inputImage)

    for i in range(rold.shape[0]):
        for j in range(rold.shape[1]):
            if g.TruenoiseBinary[i,j] > 0:
                noiseROLD_list.append(rold[i][j])
            else :
                trueROLD_list.append(rold[i][j])
    noiseROLD = np.asarray(noiseROLD_list)
    trueROLD = np.asarray(trueROLD_list)

    plt.hist(noiseROLD,bins=100,alpha=0.3,color="blue",label="noise",histtype="step")
    plt.hist(trueROLD,bins=100,alpha=0.3,color="red",label="free",histtype="step")
    plt.legend(loc="upper right", fontsize=12)
    plt.savefig(str_imgs[tex]+str(NoiseRatio)+"ROLD"+ str(times)+".png")
    plt.clf()

firsttext = "01"
dirtext = "./randomNoise/Set12/"
NoiseRatio = 10
filterSize = 5

os.chdir(dirtext)
str_imgs=glob.glob('*n')

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

        noiseROLD=np.empty(0)
        trueROLD=np.empty(0)
        noiseROLD_list = noiseROLD.tolist()
        trueROLD_list = trueROLD.tolist()

        rold = ROLD.ROLD(inputImage)

        for i in range(rold.shape[0]):
            for j in range(rold.shape[1]):
                if g.TruenoiseBinary[i,j] > 0:
                    noiseROLD_list.append(rold[i][j])
                else :
                    trueROLD_list.append(rold[i][j])
        noiseROLD = np.asarray(noiseROLD_list)
        trueROLD = np.asarray(trueROLD_list)

        plt.hist(noiseROLD,bins=100,alpha=0.3,color="blue",label="noise",histtype="step")
        plt.hist(trueROLD,bins=100,alpha=0.3,color="red",label="free",histtype="step")
        plt.legend(loc="upper right", fontsize=12)
        plt.savefig(str_imgs[tex]+str(NoiseRatio)+"ROLD.png")
        plt.clf()


        median_image = ROLD.ROLD_edge_filter(inputImage,Threshold=28)
        print("PSNR : "+format(cv2.PSNR(OrijinalImage,median_image),'.2f'))
        g.baseBinary = g.img_binary.copy()
        hyouka.hyou(g.TruenoiseBinary,g.baseBinary)
        cv2.imwrite("ROLD_FPFN"+str(NoiseRatio)+"_1+times"+".png",visual_hyouka.visual_sabun_fpfn(g.baseBinary))
        cv2.imwrite("ROLD"+str(NoiseRatio)+"_1+times"+".png",median_image)
        plot_fig(median_image)

        median_image = ROLD.ROLD_edge_filter(median_image,Threshold=27)
        print("PSNR : "+format(cv2.PSNR(OrijinalImage,median_image),'.2f'))
        g.baseBinary = hyouka.Update_imgBinary(baseBinary=g.baseBinary, addBinary=g.img_binary)
        hyouka.hyou(g.TruenoiseBinary,g.baseBinary)
        cv2.imwrite("ROLD_FPFN"+str(NoiseRatio)+"_2+times"+".png",visual_hyouka.visual_sabun_fpfn(g.baseBinary))
        cv2.imwrite("ROLD"+str(NoiseRatio)+"_2+times"+".png",median_image)
        plot_fig(median_image,times=2)

        median_image = ROLD.ROLD_edge_filter(median_image,Threshold=26)
        print("PSNR : "+format(cv2.PSNR(OrijinalImage,median_image),'.2f'))
        g.baseBinary = hyouka.Update_imgBinary(baseBinary=g.baseBinary, addBinary=g.img_binary)
        hyouka.hyou(g.TruenoiseBinary,g.baseBinary)
        cv2.imwrite("ROLD_FPFN"+str(NoiseRatio)+"_3+times"+".png",visual_hyouka.visual_sabun_fpfn(g.baseBinary))
        cv2.imwrite("ROLD"+str(NoiseRatio)+"_3+times"+".png",median_image)
        plot_fig(median_image,times=3)
        
        median_image = ROLD.ROLD_edge_filter(median_image,Threshold=24)
        print("PSNR : "+format(cv2.PSNR(OrijinalImage,median_image),'.2f'))
        g.baseBinary = hyouka.Update_imgBinary(baseBinary=g.baseBinary, addBinary=g.img_binary)
        hyouka.hyou(g.TruenoiseBinary,g.baseBinary)
        cv2.imwrite("ROLD_FPFN"+str(NoiseRatio)+"_4+times"+".png",visual_hyouka.visual_sabun_fpfn(g.baseBinary))
        cv2.imwrite("ROLD"+str(NoiseRatio)+"_4+times"+".png",median_image)
        plot_fig(median_image,times=4)

        median_image = ROLD.ROLD_edge_filter(median_image,Threshold=22)
        print("PSNR : "+format(cv2.PSNR(OrijinalImage,median_image),'.2f'))
        g.baseBinary = hyouka.Update_imgBinary(baseBinary=g.baseBinary, addBinary=g.img_binary)
        hyouka.hyou(g.TruenoiseBinary,g.baseBinary)
        cv2.imwrite("ROLD_FPFN"+str(NoiseRatio)+"_5+times"+".png",visual_hyouka.visual_sabun_fpfn(g.baseBinary))
        cv2.imwrite("ROLD"+str(NoiseRatio)+"_5+times"+".png",median_image)
        plot_fig(median_image,times=5)

        median_image = ROLD.ROLD_edge_filter(median_image,Threshold=20)
        print("PSNR : "+format(cv2.PSNR(OrijinalImage,median_image),'.2f'))
        g.baseBinary = hyouka.Update_imgBinary(baseBinary=g.baseBinary, addBinary=g.img_binary)
        hyouka.hyou(g.TruenoiseBinary,g.baseBinary)
        cv2.imwrite("ROLD_FPFN"+str(NoiseRatio)+"_6+times"+".png",visual_hyouka.visual_sabun_fpfn(g.baseBinary))
        cv2.imwrite("ROLD"+str(NoiseRatio)+"_6+times"+".png",median_image)
        plot_fig(median_image,times=6)



        print("\n")

        os.chdir("../")

