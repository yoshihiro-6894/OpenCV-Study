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

def save_b(binary):
    cp_b = binary.copy()
    for x in range(binary.shape[0]):
        for y in range(binary.shape[1]):
            if binary[x,y] > 0:
                cp_b[x,y] = 255

    return cp_b

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
    plt.xlabel("ROLD")
    plt.ylabel("number of pixels")
    plt.legend(loc="upper right", fontsize=12)
    plt.savefig(str_imgs[tex]+str(NoiseRatio)+"ROLD"+ str(times)+".png")
    plt.clf()

firsttext = "01"
dirtext = "./randomNoise/Set12/"
NoiseRatio = 10
filterSize = 5
F_valueText = open("F_Result_maximum.txt","w")
PSNR_valueText = open("PSNR_Result_maximum.txt","w")

os.chdir(dirtext)
str_imgs=glob.glob('*n')
str_imgs = ("01n","02n","03n","04n","05n","06n","07n","08n","09n","010n","011n","012n")
#print(str_imgs)


for i in range(6):
    NoiseRatio = (i+1)*10
    print("Noise:"+str(NoiseRatio)+"%")
    F_valueText.write(str(NoiseRatio)+"\n")
    PSNR_valueText.write(str(NoiseRatio)+"\n")

    for tex in range(len(str_imgs)):
        os.chdir(str_imgs[tex])
        print(str_imgs[tex]+"Noise:"+str(NoiseRatio)+"%")
        OrijinalImage = cv2.imread("orijinal.png",0)
        inputImage = cv2.imread("Noise"+str(NoiseRatio)+"%.png",0)
        g.TruenoiseBinary = cv2.imread("noiseBinary"+str(NoiseRatio)+"%.png",0)
        g.img_binary = g.TruenoiseBinary.copy()
        g.baseBinary = np.zeros(g.TruenoiseBinary.shape)

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
        plt.xlabel("ROLD")
        plt.ylabel("number of pixels")
        plt.legend(loc="upper right", fontsize=12)
        plt.savefig(str_imgs[tex]+str(NoiseRatio)+"ROLD.png")
        plt.clf()
        #strnot = "trymethod"

        _threshold= 30
        _diff_threshold = 1
        _edgeThreshold = 10
        filSize=(5,5)
        f_values = np.empty(0)
        f_valueslist = f_values.tolist()
        PSNR_values = np.empty(0)
        PSNR_valueslist = PSNR_values.tolist()

        median_image = ROLD.ROLD_edge_filter(inputImage,size=filSize,Threshold=_threshold,edgeThreshold=_edgeThreshold)
        median_image = ROLD.ROLD_filter(inputImage,size=filSize,Threshold=_threshold)
        print("PSNR : "+format(cv2.PSNR(OrijinalImage,median_image),'.2f'))
        #g.baseBinary = g.img_binary.copy()
        f_valueslist.append(hyouka.hyou(g.TruenoiseBinary,g.baseBinary))
        PSNR_valueslist.append(format(cv2.PSNR(OrijinalImage,median_image),'.2f'))
        
        #sum_median_image = ROLD.median_filter(inputImage,detectbinary=g.baseBinary)
        #print("PSNR : "+format(cv2.PSNR(OrijinalImage,sum_median_image),'.2f')+"\n")
        #cv2.imwrite("ROLD_FPFN_notedge"+str(NoiseRatio)+"_1+times"+".png",visual_hyouka.visual_sabun_fpfn(g.baseBinary))
        cv2.imwrite("ROLD"+str(NoiseRatio)+"_1+times"+".png",median_image)
        cv2.imwrite("ROLD_Binary"+str(NoiseRatio)+"_1"+"+times"+".png",save_b(g.baseBinary))
        #cv2.imwrite("ROLD"+strnot+str(NoiseRatio)+"_1+times"+".png",sum_median_image)
        plot_fig(median_image)



        for _threValue in range(14):
            print(str(_threValue+2)+"回目")
            _threshold = _threshold -_diff_threshold
            median_image = ROLD.ROLD_edge_filter(median_image,size=filSize,Threshold=_threshold,edgeThreshold=_edgeThreshold)
            # median_image = ROLD.ROLD_filter(median_image,size=filSize,Threshold=_threshold)
            print("PSNR : "+format(cv2.PSNR(OrijinalImage,median_image),'.2f'))
            g.baseBinary = hyouka.Update_imgBinary(baseBinary=g.baseBinary, addBinary=g.img_binary)
            f_valueslist.append(hyouka.hyou(g.TruenoiseBinary,g.baseBinary))
            PSNR_valueslist.append(format(cv2.PSNR(OrijinalImage,median_image),'.2f'))

            #EdgeDetect
            cv2.imwrite("ROLD_Binary"+str(NoiseRatio)+"_"+str(_threValue+2)+"+times"+".png",save_b(g.baseBinary))
            cv2.imwrite("ROLD_FPFN"+str(NoiseRatio)+"_"+str(_threValue+2)+"+times"+".png",visual_hyouka.visual_sabun_fpfn(g.baseBinary))
            cv2.imwrite("ROLD"+str(NoiseRatio)+"_"+ str(_threValue+2)+"+times"+".png",median_image)
            
            #notEdge
            # cv2.imwrite("ROLD_Binary_notedge"+str(NoiseRatio)+"_"+str(_threValue+2)+"+times"+".png",save_b(g.baseBinary))
            # cv2.imwrite("ROLD_FPFN_notedge"+str(NoiseRatio)+"_"+str(_threValue+2)+"+times"+".png",visual_hyouka.visual_sabun_fpfn(g.baseBinary))
            # cv2.imwrite("ROLD_notedge"+str(NoiseRatio)+"_"+ str(_threValue+2)+"+times"+".png",median_image)

            plot_fig(median_image,times=_threshold+2)
            sum_median_image = ROLD.median_filter(inputImage,g.baseBinary)
            print("累計"+format(cv2.PSNR(OrijinalImage,sum_median_image),'.2f'))
            cv2.imwrite("ROLD_Sum"+str(_threValue+2)+str(NoiseRatio)+".png",sum_median_image)

        f_values = np.asarray(f_valueslist)
        PSNR_values = np.asarray(PSNR_valueslist)
        print("最大F値:"+str(np.nanargmax(f_values)+1 ))
        # print("最大F値:"+str(np.nanmax(f_values))+":"+ str(np.nanargmax(f_values)+1 ))

        F_valueText.write(str_imgs[tex] + " & "+str(np.nanargmax(f_values)+1)+"\n")
        PSNR_valueText.write(str_imgs[tex] + " & "+str(np.nanargmax(PSNR_values)+1)+"\n")

        '''
        median_image = ROLD.ROLD_edge_filter(median_image,Threshold=27)
        print("PSNR : "+format(cv2.PSNR(OrijinalImage,median_image),'.2f'))
        g.baseBinary = hyouka.Update_imgBinary(baseBinary=g.baseBinary, addBinary=g.img_binary)
        hyouka.hyou(g.TruenoiseBinary,g.baseBinary)
        #sum_median_image = ROLD.median_filter(inputImage,detectbinary=g.baseBinary)
        #print("PSNR : "+format(cv2.PSNR(OrijinalImage,sum_median_image),'.2f')+"\n")
        #cv2.imwrite("ROLD_FPFN_notedge"+str(NoiseRatio)+"_2+times"+".png",visual_hyouka.visual_sabun_fpfn(g.baseBinary))
        cv2.imwrite("ROLD"+str(NoiseRatio)+"_2+times"+".png",median_image)
        #cv2.imwrite("ROLD"+strnot+str(NoiseRatio)+"_2+times"+".png",sum_median_image)
        plot_fig(median_image,times=2)

        median_image = ROLD.ROLD_edge_filter(median_image,Threshold=26)
        print("PSNR : "+format(cv2.PSNR(OrijinalImage,median_image),'.2f'))
        g.baseBinary = hyouka.Update_imgBinary(baseBinary=g.baseBinary, addBinary=g.img_binary)
        hyouka.hyou(g.TruenoiseBinary,g.baseBinary)
        #sum_median_image = ROLD.median_filter(inputImage,detectbinary=g.baseBinary)
        #print("PSNR : "+format(cv2.PSNR(OrijinalImage,sum_median_image),'.2f')+"\n")
        #cv2.imwrite("ROLD_FPFN_notedge"+str(NoiseRatio)+"_3+times"+".png",visual_hyouka.visual_sabun_fpfn(g.baseBinary))
        cv2.imwrite("ROLD"+str(NoiseRatio)+"_3+times"+".png",median_image)
        #cv2.imwrite("ROLD"+strnot+str(NoiseRatio)+"_3+times"+".png",sum_median_image)
        plot_fig(median_image,times=3)
        
        median_image = ROLD.ROLD_edge_filter(median_image,Threshold=24)
        print("PSNR : "+format(cv2.PSNR(OrijinalImage,median_image),'.2f'))
        g.baseBinary = hyouka.Update_imgBinary(baseBinary=g.baseBinary, addBinary=g.img_binary)
        hyouka.hyou(g.TruenoiseBinary,g.baseBinary)
        #sum_median_image = ROLD.median_filter(inputImage,detectbinary=g.baseBinary)
        #print("PSNR : "+format(cv2.PSNR(OrijinalImage,sum_median_image),'.2f')+"\n")
        #cv2.imwrite("ROLD_FPFN_notedge"+str(NoiseRatio)+"_4+times"+".png",visual_hyouka.visual_sabun_fpfn(g.baseBinary))
        cv2.imwrite("ROLD"+str(NoiseRatio)+"_4+times"+".png",median_image)
        #cv2.imwrite("ROLD"+strnot+str(NoiseRatio)+"_4+times"+".png",sum_median_image)
        plot_fig(median_image,times=4)

        median_image = ROLD.ROLD_edge_filter(median_image,Threshold=22)
        print("PSNR : "+format(cv2.PSNR(OrijinalImage,median_image),'.2f'))
        g.baseBinary = hyouka.Update_imgBinary(baseBinary=g.baseBinary, addBinary=g.img_binary)
        hyouka.hyou(g.TruenoiseBinary,g.baseBinary)
        #sum_median_image = ROLD.median_filter(inputImage,detectbinary=g.baseBinary)
        #print("PSNR : "+format(cv2.PSNR(OrijinalImage,sum_median_image),'.2f')+"\n")
        #cv2.imwrite("ROLD_FPFN_notedge"+str(NoiseRatio)+"_5+times"+".png",visual_hyouka.visual_sabun_fpfn(g.baseBinary))
        cv2.imwrite("ROLD"+str(NoiseRatio)+"_5+times"+".png",median_image)
        #cv2.imwrite("ROLD"+strnot+str(NoiseRatio)+"_5+times"+".png",sum_median_image)
        plot_fig(median_image,times=5)

        median_image = ROLD.ROLD_edge_filter(median_image,Threshold=20)
        print("PSNR : "+format(cv2.PSNR(OrijinalImage,median_image),'.2f'))
        g.baseBinary = hyouka.Update_imgBinary(baseBinary=g.baseBinary, addBinary=g.img_binary)
        hyouka.hyou(g.TruenoiseBinary,g.baseBinary)
        #sum_median_image = ROLD.median_filter(inputImage,detectbinary=g.baseBinary)
        #print("PSNR : "+format(cv2.PSNR(OrijinalImage,sum_median_image),'.2f')+"\n")
        #cv2.imwrite("ROLD_FPFN_notedge"+str(NoiseRatio)+"_6+times"+".png",visual_hyouka.visual_sabun_fpfn(g.baseBinary))
        cv2.imwrite("ROLD"+str(NoiseRatio)+"_6+times"+".png",median_image)
        #cv2.imwrite("ROLD"+strnot+str(NoiseRatio)+"_6+times"+".png",sum_median_image)
        plot_fig(median_image,times=6)
        '''

        sum_median_image = ROLD.median_filter(inputImage,g.baseBinary)
        print("Last"+format(cv2.PSNR(OrijinalImage,sum_median_image),'.2f'))
        cv2.imwrite("ROLD_Last"+str(NoiseRatio)+".png",sum_median_image)

        # sum_median_image = ROLD.weight_median_filter(inputImage,g.baseBinary)
        # print("Last_Weight"+format(cv2.PSNR(OrijinalImage,sum_median_image),'.2f')+"\n")
        # cv2.imwrite("ROLD_Last_Weight"+str(NoiseRatio)+".png",sum_median_image)
        print("\n")

        os.chdir("../")

F_valueText.close()
PSNR_valueText.close()