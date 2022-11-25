import numpy as np
import cv2
import matplotlib.pyplot as plt
import math
import os
import glob

import GlobalValue as g
import testBilateral
import hyouka
import padding

firsttext = "01"
dirtext = "./randomNoise/Set12/"
NoiseRatio = 10
filterSize = 5

os.chdir(dirtext)
str_imgs=glob.glob('*n')

def cus_median(image,kernel):
  #numpy配列を生成し、リストに変更
  a = np.empty(0)
  a_list = a.tolist()
  
  for i in range(len(image)):
    if kernel[i] == 0:
      #a = np.append(a,image[i])
      a_list.append(image[i])
  #numpy配列に戻す
  a = np.asarray(a_list)
  
  if a.shape[0]<1:
    return image[math.floor(image.shape[0]/2)]
  return np.median(a)

for i in range(6):
    NoiseRatio = (i+1)*10
    print("Noise:"+str(NoiseRatio)+"%")
    for tex in range(len(str_imgs)):
        os.chdir(str_imgs[tex])
        print(str_imgs[tex])
        OrijinalImage = cv2.imread("orijinal.png",0)
        inputImage = cv2.imread("Noise"+str(NoiseRatio)+"%.png",0)
        g.TruenoiseBinary = cv2.imread("noiseBinary"+str(NoiseRatio)+"%.png",0)

        inp = padding.pad_stride_reshape(inputImage,np.zeros((5,5)))
        out = inputImage.copy()
        binary = padding.pad_stride_reshape(g.TruenoiseBinary,np.zeros((5,5)))
        print(binary.shape)

        for x in range(inputImage.shape[0]):
            for y in range(inputImage.shape[1]):
                if g.TruenoiseBinary[x,y] == 255:
                    out[x,y] = cus_median(inp[x,y], binary[x,y])
        
        out.astype(np.uint8)
        print(cv2.PSNR(OrijinalImage,cv2.medianBlur(inputImage,5)))
        print(cv2.PSNR(OrijinalImage,out))

        cv2.imwrite("perfect"+str(NoiseRatio)+".png",out)

        print("\n")
        os.chdir("../")


