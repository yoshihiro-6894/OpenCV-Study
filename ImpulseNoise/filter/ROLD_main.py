import numpy as np
import cv2
import matplotlib.pyplot as plt
import math
import os
import glob

import GlobalValue as g
import custom_random_rowcol
import ROLD

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

        os.chdir("../")