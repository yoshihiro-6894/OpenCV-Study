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


NoiseROAD_file = open(str(filterSize)+"ROAD_Noise_file.txt","w")
TrueROAD_file = open(str(filterSize)+"ROAD_True_file.txt","w")

for i in range(6):
    NoiseRatio = (i+1)*10
    print("Noise:"+str(NoiseRatio)+"%")
    NoiseROAD_file.write("Noise:"+str(NoiseRatio)+"%\n")
    TrueROAD_file.write("Noise:"+str(NoiseRatio)+"%\n")
    for tex in range(len(str_imgs)):
        os.chdir(str_imgs[tex])
        print(str_imgs[tex])
        OrijinalImage = cv2.imread("orijinal.png",0)
        inputImage = cv2.imread("Noise"+str(NoiseRatio)+"%.png",0)
        g.TruenoiseBinary = cv2.imread("noiseBinary"+str(NoiseRatio)+"%.png",0)
        
        NoiseROAD_file.write(str_imgs[tex]+"\n")
        TrueROAD_file.write(str_imgs[tex]+"\n")        
        noiseROAD=np.empty(0)
        trueROAD=np.empty(0)
        noiseROAD_list = noiseROAD.tolist()
        trueROAD_list = trueROAD.tolist()
        road = ROAD.ROAD(inputImage,size=(filterSize,filterSize))
        
        for i in range(road.shape[0]):
            for j in range(road.shape[1]):
                if g.TruenoiseBinary[i,j] > 0:
                    noiseROAD_list.append(road[i][j])
                    if road[i][j]==0:
                        print(i,j)
                else :
                    trueROAD_list.append(road[i][j])
        noiseROAD = np.asarray(noiseROAD_list)
        trueROAD = np.asarray(trueROAD_list)
        plt.hist(noiseROAD,bins=100,alpha=0.3,color="blue",label="noise",histtype="step")
        plt.hist(trueROAD,bins=100,alpha=0.3,color="red",label="free",histtype="step")
        plt.legend(loc="upper right", fontsize=12)
        plt.savefig(str_imgs[tex]+str(NoiseRatio)+"ROAD.png")
        plt.clf()
        print("\n")
        print("sort")
        print("\n")
        print(np.sort(noiseROAD))
        print(np.sort(trueROAD))

        NoiseROAD_file.write("max & "+str(np.max(noiseROAD))+"\n")
        NoiseROAD_file.write("min & "+str(np.min(noiseROAD))+"\n")
        NoiseROAD_file.write("med & "+str(np.median(noiseROAD))+"\n")
        NoiseROAD_file.write("avg & "+str(np.mean(noiseROAD))+"\n")
        TrueROAD_file.write("max & "+str(np.max(trueROAD))+"\n")
        TrueROAD_file.write("min & "+str(np.min(trueROAD))+"\n")
        TrueROAD_file.write("med & "+str(np.median(trueROAD))+"\n")
        TrueROAD_file.write("avg & "+str(np.mean(trueROAD))+"\n")

        print("\n")
        os.chdir("../")
    NoiseROAD_file.write("\n")
    TrueROAD_file.write("\n")

print(str_imgs)

NoiseROAD_file.close()
TrueROAD_file.close()
