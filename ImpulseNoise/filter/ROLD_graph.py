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
#dirtext = "./randomNoise/BSD68/"
NoiseRatio = 10
filterSize = 5

os.chdir(dirtext)
str_imgs=glob.glob('*n')
#str_imgs = ("01n","02n","03n","04n","05n","06n","07n","08n","09n","010n","011n","012n")
colors=("b","g","r","c","m","y")
#print(str_imgs)

# noiseROLD=np.empty((6,0))
# trueROLD=np.empty((6,0))
# print(noiseROLD.shape)
# noiseROLD_list = noiseROLD.tolist()
# trueROLD_list = trueROLD.tolist()

for k in range(6):
    NoiseRatio = (k+1)*10
    print("Noise:"+str(NoiseRatio)+"%")
    noiseROLD=np.empty(0)
    trueROLD=np.empty(0)
    noiseROLD_list = noiseROLD.tolist()
    trueROLD_list = trueROLD.tolist()

    for tex in range(len(str_imgs)):
        os.chdir(str_imgs[tex])
        print(str_imgs[tex]+"Noise:"+str(NoiseRatio)+"%")
        OrijinalImage = cv2.imread("orijinal.png",0)
        inputImage = cv2.imread("Noise"+str(NoiseRatio)+"%.png",0)
        g.TruenoiseBinary = cv2.imread("noiseBinary"+str(NoiseRatio)+"%.png",0)
        g.img_binary = g.TruenoiseBinary.copy()
        g.baseBinary = np.zeros(g.TruenoiseBinary.shape)

        #noiseROLD=np.empty(0)
        #trueROLD=np.empty(0)
        #noiseROLD_list = noiseROLD.tolist()
        #trueROLD_list = trueROLD.tolist()

        rold = ROLD.ROLD(inputImage,size=(5,5))

        for i in range(rold.shape[0]):
            for j in range(rold.shape[1]):
                if g.TruenoiseBinary[i,j] > 0:
                    noiseROLD_list.append(rold[i][j])
                else :
                    trueROLD_list.append(rold[i][j])
        # noiseROLD = np.asarray(noiseROLD_list)
        # trueROLD = np.asarray(trueROLD_list)

        # plt.hist(noiseROLD,bins=100,alpha=0.3,color="blue",label="noise",histtype="step")
        # plt.hist(trueROLD,bins=100,alpha=0.3,color="red",label="free",histtype="step")
        # plt.xlabel("ROLD")
        # plt.ylabel("number of pixels")
        # plt.legend(loc="upper right", fontsize=12)
        # plt.savefig(str_imgs[tex]+str(NoiseRatio)+"ROLD_sum.png")
        # plt.clf()

        _threshold= 21
        _edgeThreshold = 5

        #median_image = ROLD.ROLD_edge_filter(inputImage,Threshold=_threshold,edgeThreshold=_edgeThreshold)
        #print("PSNR : "+format(cv2.PSNR(OrijinalImage,median_image),'.2f'))
        #g.baseBinary = g.img_binary.copy()
        #hyouka.hyou(g.TruenoiseBinary,g.baseBinary)

        os.chdir("../")

    noiseROLD=np.asarray(noiseROLD_list)
    print(np.mean(noiseROLD))
    #trueROLD=np.asarray(trueROLD_list)
    plt.hist(noiseROLD,bins=300,alpha=0.3,color=colors[k],label=str(NoiseRatio)+"%",histtype="step")


# plt.hist(noiseROLD,bins=100,alpha=0.3,color="blue",label="noise",histtype="step")
# plt.hist(trueROLD,bins=100,alpha=0.3,color="red",label="free",histtype="step")
# plt.xlabel("ROLD")
# plt.ylabel("number of pixels")
# plt.legend(loc="upper right", fontsize=12)
# plt.savefig("ROLD_sum.png")
# plt.clf()


#plt.hist(noiseROLD[0],bins=100,alpha=0.3,color="blue",label="10%",histtype="step")
# plt.hist(noiseROLD[1],bins=100,alpha=0.3,color="green",label="20%",histtype="step")
# plt.hist(noiseROLD[2],bins=100,alpha=0.3,color="red",label="30%",histtype="step")
# plt.hist(noiseROLD[3],bins=100,alpha=0.3,color="black",label="40%",histtype="step")
# plt.hist(noiseROLD[4],bins=100,alpha=0.3,color="Yellow",label="50%",histtype="step")
# plt.hist(noiseROLD[5],bins=100,alpha=0.3,color="Cyan",label="60%",histtype="step")
plt.xlabel("ROLD")
plt.ylabel("number of pixels")
#plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0, fontsize=18)
plt.legend(loc="upper left", fontsize=11)
plt.savefig("ROLD_sum.png")
plt.clf()