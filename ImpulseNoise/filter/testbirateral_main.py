import numpy as np
import cv2
import matplotlib.pyplot as plt
import math
import os
import glob

import GlobalValue as g
import testBilateral
import hyouka

firsttext = "01"
dirtext = "./randomNoise/Set12/"
NoiseRatio = 10
filterSize = 5

os.chdir(dirtext)
str_imgs=glob.glob('*n')


PSNR_file = open("Size"+"testBilateral"+"PSNRresult.txt","w")
#NoiseROAD_file = open("LCI_Noise_file.txt","w")
#TrueROAD_file = open("LCI_True_file.txt","w")

for i in range(6):
    NoiseRatio = (i+1)*10
    print("Noise:"+str(NoiseRatio)+"%")
    PSNR_file.write("Noise:"+str(NoiseRatio)+"%\n")
    #NoiseROAD_file.write("Noise:"+str(NoiseRatio)+"%\n")
    #TrueROAD_file.write("Noise:"+str(NoiseRatio)+"%\n")
    for tex in range(len(str_imgs)):
        os.chdir(str_imgs[tex])
        print(str_imgs[tex])
        OrijinalImage = cv2.imread("orijinal.png",0)
        inputImage = cv2.imread("Noise"+str(NoiseRatio)+"%.png",0)
        g.TruenoiseBinary = cv2.imread("noiseBinary"+str(NoiseRatio)+"%.png",0)

        #NoiseROAD_file.write(str_imgs[tex]+"\n")
        #TrueROAD_file.write(str_imgs[tex]+"\n")        
        noiseROAD=np.empty(0)
        trueROAD=np.empty(0)
        noiseROAD_list = noiseROAD.tolist()
        trueROAD_list = trueROAD.tolist()
        road = testBilateral.bilateral_filter(inputImage)
        #road = road.astype(np.uint8)
        #print(np.round(cv2.PSNR(OrijinalImage,road),decimals=2))
        #PSNR_file.write(str_imgs[tex]+" &"+str(np.round(cv2.PSNR(OrijinalImage,road),decimals=2))+"\n")
        #cv2.imwrite("testBilateral"+str(NoiseRatio)+".png",road)

        #binary = np.where(road<0.3,1,0)

        #hyouka.hyou(g.TruenoiseBinary,binary)
        
        
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
        #NoiseROAD_file.write("max & "+str(np.max(noiseROAD))+"\n")
        #NoiseROAD_file.write("min & "+str(np.min(noiseROAD))+"\n")
        #NoiseROAD_file.write("med & "+str(np.median(noiseROAD))+"\n")
        #NoiseROAD_file.write("avg & "+str(np.mean(noiseROAD))+"\n")
        #NoiseROAD_file.write("std & "+str(np.std(noiseROAD))+"\n")
        #TrueROAD_file.write("max & "+str(np.max(trueROAD))+"\n")
        #TrueROAD_file.write("min & "+str(np.min(trueROAD))+"\n")
        #TrueROAD_file.write("med & "+str(np.median(trueROAD))+"\n")
        #TrueROAD_file.write("avg & "+str(np.mean(trueROAD))+"\n")
        #TrueROAD_file.write("std & "+str(np.std(trueROAD))+"\n")

        plt.xlabel("statistic",fontsize=9)
        plt.ylabel("frequency",fontsize=9)
        plt.hist(noiseROAD,bins=100,alpha=0.3,color="blue",label="noise",histtype="step")
        plt.hist(trueROAD,bins=100,alpha=0.3,color="red",label="free",histtype="step")
        plt.legend(loc="upper right", fontsize=12)

        plt.savefig(str_imgs[tex]+str(NoiseRatio)+".png")

        plt.clf()
        

        '''画像復元
        median_image = testBilateral.custom(inputImage)
        median_image = median_image.astype(np.uint8)
        print("PSNR:"+str(cv2.PSNR(OrijinalImage,median_image)))
        print(np.round(cv2.PSNR(OrijinalImage,median_image),decimals=2))
        PSNR_file.write(str_imgs[tex]+" &"+str(np.round(cv2.PSNR(OrijinalImage,median_image),decimals=2))+"\n")
        cv2.imwrite("testBilateral"+str(NoiseRatio)+".png",median_image)
        '''

        print("\n")
        os.chdir("../")
    PSNR_file.write("\n")
    #NoiseROAD_file.write("\n")
    #TrueROAD_file.write("\n")

print(type(str_imgs))

PSNR_file.close()
#NoiseROAD_file.close()
#TrueROAD_file.close()

