import numpy as np
import cv2
import math
import os

import GlobalValue as g
import custom_random_rowcol
import custom_random1
import padding
import get_LCI
import edgeDetection
import hyouka
import visual_hyouka
import W_median

def filter(img):
    img_cp = img.copy()
    img_binary = np.zeros(img.shape,dtype=np.uint8)

    size3,size5,size7,size9=(3,3),(5,5),(7,7),(9,9)
    strided_image3 = padding.pad_stride(img,np.zeros(size3))
    strided_image5 = padding.pad_stride(img,kernel=np.zeros(size5))
    strided_image7 = padding.pad_stride(img,np.zeros(size7))
    strided_image9 = padding.pad_stride(img,np.zeros(size9))
    strided_image_3 = padding.pad_stride_reshape(img,np.zeros(size3))
    strided_image_5 = padding.pad_stride_reshape(img,np.zeros(size5))
    strided_image_7 = padding.pad_stride_reshape(img,np.zeros(size7))
    print("検出")
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            img_binary[x,y] = custom_random_rowcol.rowcol(strided_image5[x,y])
    g.F_old=hyouka.hyou(g.TruenoiseBinary, img_binary)
    g.binary = visual_hyouka.visual(img_binary.copy())
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            if img_binary[x,y] >0:
                img_binary[x,y] = edgeDetection.detect(strided_image5[x,y], 5)
    g.F_new = hyouka.hyou(g.TruenoiseBinary, img_binary)
    g.binary_new = visual_hyouka.visual(img_binary.copy())
    binary_3 = padding.pad_stride_reshape(img_binary,np.zeros(size3))
    binary_5 = padding.pad_stride_reshape(img_binary,np.zeros(size5))
    binary_7 = padding.pad_stride_reshape(img_binary,np.zeros(size7))

    print("除去")
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            if img_binary[x][y] == 1:
                if np.count_nonzero(binary_3[x][y]==1) < 4:
                    #3*3
                    #img_cp[x][y] = np.median(strided_image3[x][y]) 
                    img_cp[x,y] = W_median.W_median(strided_image_3[x][y], ((binary_3[x][y]+1)*(np.ones(binary_3[x][y].shape)-binary_3[x][y])))
                elif np.count_nonzero(binary_5[x][y]==1) < 13:
                    #5*5
                    #img_cp[x][y] = np.median(strided_image5[x][y])
                    img_cp[x,y] = W_median.W_median(strided_image_5[x][y], ((binary_5[x,y]+1)*(np.ones(binary_5[x][y].shape)-binary_5[x][y])))
                else:
                    #img_cp[x][y] = np.median(strided_image7[x][y])
                    img_cp[x][y] = W_median.W_median(strided_image_7[x][y], ((binary_7[x,y]+1)*(np.ones(binary_7[x][y].shape)-binary_7[x][y])))

    g.img_binary = img_binary.copy()
    img_cp = img_cp.astype(np.uint8)
    return img_cp

def lcifilter(img,img_binary,trigger=False):
    if trigger:
        img_binary = np.ones(img.shape)
    img_cp = img.copy()
    size=(5,5)
    LCI = get_LCI.LCI(img)
    LCI_pad = padding.pad_stride_reshape(LCI*5, np.zeros(size))

    strided_image = padding.pad_stride_reshape(img,np.zeros(size))

    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            if img_binary[x,y]>0:
                img_cp[x,y] = custom_random1.W_median(strided_image[x,y], LCI_pad[x,y])

    return img_cp

def detecter(img):
    img_binary = np.zeros(img.shape)
    strided_image = padding.pad_stride(img,np.zeros((5,5)))
    img_cp = img.copy()

    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            img_binary[x,y] = custom_random_rowcol.rowcol(strided_image[x,y])
    
    g.img_binary=img_binary.copy()
    
    return lcifilter(img,img_binary)
