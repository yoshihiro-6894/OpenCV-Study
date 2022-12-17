import cv2
import numpy as np
import math

import padding
import GlobalValue as g
import hyouka

def ASWMfilter(image,alpha=20,delta=0.1,epsilon=0.01,windowSize=3):
    img_cp = image.copy()
    img_binary = np.zeros(image.shape,dtype=np.uint8)
    pad_image = padding.pad_stride_reshape(image,np.zeros((windowSize,windowSize)))
    
    weighted_value = np.ones(pad_image.shape)
    Weighted_average_value = np.ones(image.shape)

    #np.apply_along_axis(lambda a:ASWMs(a),axis=2,pad_image)

    #print("aswm")

    '''
    x=1
    y=1

    while True:
        before_W_average_value = Weighted_average_value[x,y].copy()

        weighted_value[x,y] = 1/ (np.abs(pad_image[x,y]-Weighted_average_value[x,y]) + delta)

        Weighted_average_value[x,y] = np.sum(weighted_value[x,y] * pad_image[x,y]) / np.sum(weighted_value[x,y])

        if np.abs(before_W_average_value - Weighted_average_value[x,y]) < epsilon:
            break
    
    tile_MW = np.tile(Weighted_average_value[x,y],weighted_value[x,y].shape)
    #print(pad_image[x,y]-tile_MW)
    #print(np.square(pad_image[x,y]-tile_MW))
    sigma = np.sqrt( np.sum(weighted_value * np.square(pad_image[x,y]-tile_MW)) /  np.sum(weighted_value[x,y])  )
    #print(sigma.shape)

    if np.abs(np.median(pad_image[x,y]) - image[x,y]) > alpha*sigma:
        #print("B")
        img_cp[x,y] = np.median(pad_image[x,y])
    else:
        #print(str(np.abs(np.median(pad_image[x,y]) - image[x,y]))+"    "+str(alpha*sigma))
    '''
    
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            while True:
                before_W_average_value = Weighted_average_value[x,y].copy()

                weighted_value[x,y] = 1/ (np.abs(pad_image[x,y]-Weighted_average_value[x,y]) + delta)

                Weighted_average_value[x,y] = np.sum(weighted_value[x,y] * pad_image[x,y]) / np.sum(weighted_value[x,y])

                if np.abs(before_W_average_value - Weighted_average_value[x,y]) < epsilon:
                    break
            
            tile_MW = np.tile(Weighted_average_value[x,y],weighted_value[x,y].shape)
            #print(pad_image[x,y]-tile_MW)
            #print(np.square(pad_image[x,y]-tile_MW))
            
            sigma = np.sqrt( np.sum(weighted_value[x,y] * np.square(pad_image[x,y]-tile_MW)) /  np.sum(weighted_value[x,y])  )
            #print(sigma)

            if np.abs(np.median(pad_image[x,y]) - image[x,y]) > alpha*sigma:
                img_binary[x,y] = 1
                img_cp[x,y] = np.median(pad_image[x,y])

    g.img_binary = img_binary.copy()
    return img_cp

            

'''
asize=5

b = np.zeros((asize,asize))

for i in range(asize):
    for j in range(asize):
        b[i,j] = i*asize + j

ASWMfilter(b)

'''

def ASWMs(pad_image,alpha=20):
    weighted_value = np.ones(pad_image.shape)
    Weighted_average_value = np.ones(image.shape)

    while True:
        before_W_average_value = Weighted_average_value.copy()

        weighted_value = 1/ (np.abs(pad_image-Weighted_average_value) + 0.1)

        Weighted_average_value = np.sum(weighted_value * pad_image) / np.sum(weighted_value)

        if np.abs(before_W_average_value - Weighted_average_value) < 0.1:
            break
            
    tile_MW = np.tile(Weighted_average_value,weighted_value.shape)
    sigma = np.sqrt( np.sum(weighted_value * np.square(pad_image-tile_MW)) /  np.sum(weighted_value)  )

    if np.abs(np.median(pad_image) - image) > alpha*sigma:
        img_cp = np.median(pad_image)

