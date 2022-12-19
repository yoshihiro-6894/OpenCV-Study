"""
DWMfilter
A new Directional Weighted Median Filter for Removal of Random-Valued Impulse Noise
の実装
2022-11-28
"""


import cv2
import numpy as np
import math

import padding
import GlobalValue as g


def DWM(image,size,Threshold):
    img_cp = image.copy()
    img_binary = np.zeros(image.shape,dtype=np.uint8)
    pad_image = padding.pad_stride_reshape(image,np.zeros((size,size)))

    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            img_binary[x,y] = detect(pad_image[x,y],size = size,Threshold=Threshold)

    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            if img_binary[x,y] > 0:
                img_cp[x,y] = np.median(pad_image[x,y])
    
    g.img_binary = img_binary.copy()

    return img_cp


def detect(input,size,Threshold=510):
    #print(input)
    #縦横斜めの全4種類分の保存する配列
    Direct_coordinates = np.empty([4,0])
    #print(Direct_coordinates.shape)
    Direct_coordinates_list = Direct_coordinates.tolist()
    for i in range(size):
        if i == int(size/2):
            continue
        #print(i,i)
        #print(int(size/2),i)
        #print(size-i-1,i)
        #print(i,int(size/2))
        '''
        Direct_coordinates_list[0].append(input[i,i])
        Direct_coordinates_list[1].append(input[int(size/2),i])
        Direct_coordinates_list[2].append(input[size-1-i,i])
        Direct_coordinates_list[3].append(input[i,int(size/2)])
        '''
        Direct_coordinates_list[0].append(input[i*size+i])
        Direct_coordinates_list[1].append(input[int(size/2)*size + i])
        Direct_coordinates_list[2].append(input[(size-1-i)*size + i])
        Direct_coordinates_list[3].append(input[i*size + int(size/2)])
    Direct_coordinates = np.asarray(Direct_coordinates_list)
        
    #print(Direct_coordinates)
    #print(Direct_coordinates.shape)

    centers = np.tile(input[int(size/2)*size+int(size/2)],(Direct_coordinates.shape))
    #print(centers)

    #print(np.abs(Direct_coordinates - centers))
    #print(np.sum((np.abs(Direct_coordinates - centers)),axis=1))
    dire = np.sum((np.abs(Direct_coordinates - centers)),axis=1)
    sum_dire = np.sum(dire)
    #print(sum_dire)
    #print(sum_dire > Threshold)
    if sum_dire > Threshold:
        return 1
    else:
        return 0
    print(np.min(np.sum((np.abs(Direct_coordinates - centers)),axis=1)))
    print(np.argmin(np.sum((np.abs(Direct_coordinates-centers)),axis=1)))


asize=5

b = np.zeros((asize,asize))

for i in range(asize):
    for j in range(asize):
        b[i,j] = i*asize + j

c = padding.pad_stride_reshape(b,np.zeros((asize,asize)))
detect(c[1,2],asize)


    