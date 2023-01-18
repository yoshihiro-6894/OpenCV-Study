import cv2
import numpy as np
import padding
import GlobalValue as g
import edgeDetection
import hyouka
import visual_hyouka

import W_median

def ROLD(image, size=(5, 5),boundary='reflect'):
  pad_image = np.pad(image, ((int(size[0] / 2),), (int(size[1] / 2),)), boundary)
  #print(pad_image)
  areas = np.lib.stride_tricks.as_strided(pad_image, image.shape + size, pad_image.strides * 2)
  #print(areas.shape)
  centers = np.tile(image.reshape(image.shape + (1, 1)), (1, 1) + size)
  
  #Dst = np.abs(centers-areas).reshape(centers.shape[0], centers.shape[1],centers.shape[2]*centers.shape[3])
  with np.errstate(divide="ignore"):
    Dst = np.log2((np.abs(centers-areas)).reshape(centers.shape[0], centers.shape[1],centers.shape[2]*centers.shape[3]))
  #print(Dst)
  #print(Dst.shape)
  d_b = np.tile(-5, Dst.shape)
  D_st = 1+np.maximum(Dst,d_b)/5
  #print(D_st)
  #print(np.maximum(Dst,d_b)/5)
  sort_Dst = np.sort(D_st)
  #print(sort_Dst)
  #print(sort_Dst[:,:,:int((size[0]*size[1]+1)/2)].sum(axis=2))
  return sort_Dst[:,:,:int((size[0]*size[1]+1)/2)].sum(axis=2)
  #sort_b = np.sort(np.abs((centers-areas).reshape(centers.shape[0], centers.shape[1],centers.shape[2]*centers.shape[3])))
  #print(sort_b)
  #print(int((size[0]*size[1]+1)/2))
  #print(int((size[0]*size[1]+1)/2))
  #print(sort_b[:,:,:int((size[0]*size[1]+1)/2)].sum(axis=2))
  return sort_b[:,:,:int((size[0]*size[1]+1)/2)].sum(axis=2)

'''
inputArray = np.arange(1,37).reshape(6,6)
print(inputArray)
out = ROLD(inputArray)
'''

def ROLD_filter(image,size=(5,5),boundary="reflect",Threshold=30):
    img_cp = image.copy()
    img_binary = np.zeros(image.shape,dtype=np.uint8)
    pad_image = padding.pad_stride(image,kernel=np.zeros(size),boundary=boundary)
    _RoldValue = ROLD(image,size=size,boundary=boundary)

    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            if _RoldValue[x,y] > Threshold:
                img_binary[x,y] = 1
                img_cp[x,y] = np.median(pad_image[x,y])

    
    g.img_binary = img_binary.copy()
    g.baseBinary = hyouka.Update_imgBinary(baseBinary=g.baseBinary, addBinary=g.img_binary)

    return img_cp

def ROLD_edge_filter(image,size=(5,5),boundary="reflect",Threshold=30,edgeThreshold=5):
    print(str(Threshold)+":"+str(edgeThreshold)+":"+str(size))
    counter = 0
    img_cp = image.copy()
    img_binary = np.zeros(image.shape,dtype=np.uint8)
    pad_image = padding.pad_stride(image,kernel=np.zeros(size),boundary=boundary)
    _RoldValue = ROLD(image,size=size,boundary=boundary)
    pad_image_9 = padding.pad_stride(image,kernel=np.zeros((9,9)),boundary=boundary)

    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            if _RoldValue[x,y] > Threshold:
                counter = counter + 1
                img_binary[x,y] = edgeDetection.detect(pad_image[x,y],size[0],Threshold=edgeThreshold)
                if img_binary[x,y]>0:
                    counter = counter -1
                    img_cp[x,y] = np.median(pad_image[x,y])

    g.img_binary = img_binary.copy()
    g.baseBinary = hyouka.Update_imgBinary(baseBinary=g.baseBinary, addBinary=g.img_binary)
    print("カウント"+str(counter))

    # for x in range(image.shape[0]):
    #     for y in range(image.shape[1]):
    #         if g.img_binary[x,y] > 0:
    #             img_cp[x,y] = np.median(pad_image[x,y])

    return img_cp

def median_filter(image,detectbinary,size=(5,5),boundary="reflect"):
    img_cp = image.copy()
    pad_image = padding.pad_stride(image,kernel=np.zeros(size),boundary=boundary)

    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            if detectbinary[x,y] > 0:
                img_cp[x,y] = np.median(pad_image[x,y])

    return img_cp

def weight_median_filter(image,detectbinary,size=(5,5),boundary="reflect"):
    img_cp = image.copy()
    pad_image = padding.pad_stride_reshape(image,kernel=np.zeros(size),boundary=boundary)
    detect = np.where(detectbinary>0,1,2)
    pad_binary = padding.pad_stride_reshape(detect,kernel=np.zeros(size),boundary=boundary)

    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            if detectbinary[x,y] > 0:
                # img_cp[x,y] = W_median.W_median(pad_image[x,y], kernel = 2*np.ones(pad_binary[x,y].shape) - pad_binary[x,y])
                img_cp[x,y] = W_median.W_median(pad_image[x,y], kernel = pad_binary[x,y])

    return img_cp

def adaptive_median_filter(image,detectbinary,boundary="reflect"):
    img_cp = image.copy()
    strided_image_3 = padding.pad_stride(image,kernel=np.zeros((3,3)),boundary=boundary)
    strided_image_5 = padding.pad_stride(image,kernel=np.zeros((5,5)),boundary=boundary)
    strided_image_7 = padding.pad_stride(image,kernel=np.zeros((7,7)),boundary=boundary)
    binary_3 = padding.pad_stride(detectbinary,kernel=np.zeros((3,3)),boundary=boundary)
    binary_5 = padding.pad_stride(detectbinary,kernel=np.zeros((5,5)),boundary=boundary)
    binary_7 = padding.pad_stride(detectbinary,kernel=np.zeros((7,7)),boundary=boundary)

    for i in range((image.shape[0])):
      for j in range((image.shape[1])):
        if img_binary[i][j] == 1:
          if np.count_nonzero(binary_3[i][j]==1) < 4:
            #3*3
            #img_cp[i][j] = W_median(strided_image_3[i][j],kernel_3_1) 
            img_cp[i,j] = np.median(strided_image_3[i,j])
          elif np.count_nonzero(binary_5[i][j]==1) < 13:
            #5*5
            #img_cp[i][j] = W_median(strided_image_5[i][j],kernel_5_1)
            img_cp[i,j] = np.median(strided_image_5[i,j])
          else:
            #img_cp[i][j] = W_median(strided_image_7[i][j],kernel_7_1)
            img_cp[i,j] = np.median(strided_image_7[i,j])

    return img_cp