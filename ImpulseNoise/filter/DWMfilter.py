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


def DWM(image,size):
    img_cp = image.copy()
    img_binary = np.zeros(image.shape,dtype=np.uint8)
    pad_image = padding.pad_stride_reshape(image,np.zeros((size,size)))


def detect(input,size):
    print(input)
    #縦横斜めの全4種類分の保存する配列
    Direct_coordinates = np.empty([4,0])
    print(Direct_coordinates.shape)
    Direct_coordinates_list = Direct_coordinates.tolist()
    for i in range(size):
        #print(i,i)
        #print(int(size/2),i)
        print(size-i-1,i)
        #print(i,int(size/2))

        Direct_coordinates_list[0].append(input[i,i])
        Direct_coordinates_list[1].append(input[int(size/2),i])
        Direct_coordinates_list[2].append(input[size-1-i,i])
        Direct_coordinates_list[3].append(input[i,int(size/2)])
    Direct_coordinates = np.asarray(Direct_coordinates_list)
        
    print(Direct_coordinates)
    print(Direct_coordinates.shape)

    centers = np.tile(input[int(size/2),int(size/2)],(Direct_coordinates.shape))
    print(centers)

    print(np.abs(Direct_coordinates - centers))
    print(np.sum((np.abs(Direct_coordinates - centers)),axis=1))
    print(np.min(np.sum((np.abs(Direct_coordinates - centers)),axis=1)))


asize=5

b = np.zeros((asize,asize))

for i in range(asize):
    for j in range(asize):
        b[i,j] = i*asize + j

c = padding.pad_stride(b,np.zeros((asize,asize)))
detect(c[1,2],asize)


    