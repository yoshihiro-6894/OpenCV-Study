'''
Random-valued impulse noise removal using adaptive dual threshold
median filter

'''


import numpy as np
import cv2
import math
import time

import GlobalValue as g
import hyouka

def pad_stride(image,kernel,boundary):
  pad_image = np.pad(image, ((int(kernel.shape[0] / 2),), (int(kernel.shape[1] / 2),)), boundary)
  shape = (pad_image.shape[0] - kernel.shape[0] + 1, pad_image.shape[1] - kernel.shape[1] + 1) + kernel.shape
  strides = pad_image.strides * 2
  # as_strided()でpad_imageをshapeの大きさの配列をスライドしたような配列を生成する
  return np.lib.stride_tricks.as_strided(pad_image, shape, strides).reshape(shape[0], shape[1], kernel.shape[0] , kernel.shape[1])

def median_filter(image,size,boundary="reflect"):
    img_binary = np.zeros(image.shape,dtype=np.uint8)
    img_cp = image.copy()
    print("custom_random_rowcol")

    kernel = np.ones((size,size))

    strided_image = pad_stride(image,kernel,boundary)

    '''
    kernel_3=np.ones((3,3))
    kernel_3_1=kernel_3.reshape(9,)
    kernel_5=np.ones((5,5))
    kernel_5_1=kernel_5.reshape(kernel_5.shape[0]*kernel_5.shape[1])
    kernel_7=np.ones((7,7))

    strided_image_3 = pad_stride(image,kernel_3,boundary)
    strided_image_5 = pad_stride(image,kernel_5,boundary)
    strided_image_7 = pad_stride(image,kernel_7,boundary)
    '''
    

    for i in range((image.shape[0])):
      for j in range((image.shape[1])):
        img_binary[i][j] = rowcol(strided_image[i][j])

    binary_stride = pad_stride(img_binary,kernel,boundary)

    '''
    binary_3 = pad_stride(img_binary,kernel_3,boundary)
    binary_5 = pad_stride(img_binary,kernel_5,boundary)
    binary_7 = pad_stride(img_binary,kernel_7,boundary)
    '''

    for i in range((image.shape[0])):
      for j in range((image.shape[1])):
        if img_binary[i][j]==1:
            img_cp[i][j]=np.median(strided_image[i][j])
            #img_cp[i][j] = W_median(strided_image[i][j], kernel = (kernel*(np.ones(binary_stride[i][j].shape)-binary_stride[i][j])))

    hyouka.hyou(g.TruenoiseBinary,img_binary)

    return img_cp

def rowcol(image):
    forcus = image[int(image.shape[0] / 2)][int(image.shape[1] / 2)]
    Average_rows = np.mean(image,axis=0)
    Average_cols = np.mean(image,axis=1)
    concatenate = np.concatenate([Average_rows,Average_cols])
    Th_max = np.max(concatenate)
    Th_min = np.min(concatenate)
    if (forcus<Th_min) or (Th_max<forcus):
        return 1
    else:
        return 0

def W_median(image,kernel):
  kernel_reshape = kernel.reshape(kernel.shape[0]*kernel.shape[1])
  a = np.empty(0)
  for i in range(len(image)):
    for j in range(int(kernel_reshape[i])):
      a = np.append(a,image[i])
  if a.shape[0]<1:
    return image[math.floor(image.shape[0]/2)]
  return np.median(a)