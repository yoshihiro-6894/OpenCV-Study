import cv2
import numpy as np
import math
import hyouka
import GlobalValue as g

def pad_stride(image,kernel,boundary='reflect'):
  pad_image = np.pad(image, ((int(kernel.shape[0] / 2),), (int(kernel.shape[1] / 2),)), boundary)
  shape = (pad_image.shape[0] - kernel.shape[0] + 1, pad_image.shape[1] - kernel.shape[1] + 1) + kernel.shape
  strides = pad_image.strides * 2
  # as_strided()でpad_imageをshapeの大きさの配列をスライドしたような配列を生成する
  return np.lib.stride_tricks.as_strided(pad_image, shape, strides)

def detect(image):
    center = image[math.floor(image.shape[0]/2)][math.floor(image.shape[1]/2)]
    A = np.empty(0)
    windowA = A.tolist()

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if i == math.floor(image.shape[0]/2) and j == math.floor(image.shape[1]/2):
                continue
            windowA.append(image[i,j])
    A = np.asarray(windowA)
    meanA = np.mean(A)
    stdA = np.std(A)

    meanAs = np.tile(meanA, A.shape)
    absolute_P = np.abs(meanAs - A)
    
    threshold_1 = np.mean(absolute_P) + np.std(absolute_P)

    centers = np.tile(center, A.shape)
    absolute_q = np.abs(centers - A)
    NS = np.mean(absolute_q)
    
    if NS >= threshold_1:
        g.A1 = g.A1 +1
        return 1
    
    threshold_2min = meanA - 0.5 * stdA
    threshold_2max = meanA + 0.5 * stdA
    
    if center <= threshold_2min or center >= threshold_2max:
        g.A2 = g.A2 + 1
        return 1
    
    threshold_3max, threshold_3min = np.percentile(A, [75 ,25])

    if center <= threshold_3min or center >= threshold_3max:
        g.A3 = g.A3 +1
        return 1

    return 0

def filter(image):
    img_binary=np.zeros(image.shape,dtype=np.uint8)
    img_cp = image.copy()
    print("custom_tripleThreshold")

    pad_img_5 = pad_stride(image,np.zeros([5,5]))

    g.A1=0
    g.A2=0
    g.A3=0

    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            img_binary[x][y] = detect(pad_img_5[x][y])

    

    hyouka.hyou(g.TruenoiseBinary,img_binary)
    print(g.A1)
    print(g.A2)
    print(g.A3)


