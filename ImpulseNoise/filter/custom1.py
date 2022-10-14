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
  return np.lib.stride_tricks.as_strided(pad_image, shape, strides).reshape(shape[0], shape[1], kernel.shape[0] * kernel.shape[1])

def detect(image):
  forcus = image[4]
  if((forcus==np.min(image))or(forcus==np.max(image))):
    return True
  else:
    return False

def W(image):
  sort_R = np.sort(image)
  diff_D = np.diff(sort_R)
  argsort = np.argsort(diff_D)
  maxs = argsort[-4:]
  p = np.min(maxs)
  t = np.max(maxs)
  w_min = sort_R[p+1]+1
  w_max = sort_R[t]
  forcus = image[math.floor(len(image)/2)]
  if (forcus<w_min) or (w_max<forcus):
    g.count= g.count+1
    return 1
    return np.median(sort_R)
  else:
    return 0
    return forcus
  print(maxs)
  print(len(image))
  print(math.ceil(len(image)/2))

  return np.median(sort_R)

def W_median(image,kernel):
  a = np.empty(0)
  for i in range(len(image)):
    for j in range(int(kernel[i])):
      a = np.append(a,image[i])
  if a.shape[0]<1:
    return image[math.floor(image.shape[0]/2)]
  return np.median(a)

def median_filter(image, boundary='reflect'):
    img_binary=np.zeros(image.shape,dtype=np.uint8)
    img_cp = image.copy()
    print("custom1")

    kernel_3=np.array([[1,2,1],[2,0,2],[1,2,1]])
    kernel_3_1=kernel_3.reshape(9,)
    kernel_5=np.array([[1,2,3,2,1],[2,4,5,4,2],[3,5,0,5,3],[2,4,5,4,2],[1,2,3,2,1]])
    kernel_5_1=kernel_5.reshape(kernel_5.shape[0]*kernel_5.shape[1])
    kernel_7=np.array([[1,2,3,4,3,2,1],[2,4,5,6,5,4,2],[3,5,7,8,7,5,3],[4,6,8,0,8,6,4],[3,5,7,8,7,5,3],[2,4,5,6,5,4,2],[1,2,3,4,3,2,1]])
    kernel_7_1=kernel_7.reshape(kernel_7.shape[0]*kernel_7.shape[1])
    kernel_11=np.zeros((11,11))
    strided_image_3 = pad_stride(image,kernel_3,boundary)
    strided_image_5 = pad_stride(image,kernel_5,boundary)
    strided_image_7 = pad_stride(image,kernel_7,boundary)
    strided_image_11 = pad_stride(image,kernel_11,boundary)

    '''
    pad_image = np.pad(image, ((int(kernel_3.shape[0] / 2),), (int(kernel_3.shape[1] / 2),)), boundary)
    shape = (pad_image.shape[0] - kernel_3.shape[0] + 1, pad_image.shape[1] - kernel_3.shape[1] + 1) + kernel_3.shape
    strides = pad_image.strides * 2
    # as_strided()でpad_imageをshapeの大きさの配列をスライドしたような配列を生成する
    strided_image_3 = np.lib.stride_tricks.as_strided(pad_image, shape, strides).reshape(shape[0], shape[1], kernel_3.shape[0] * kernel_3.shape[1])

    pad_image = np.pad(image, ((int(kernel_5.shape[0] / 2),), (int(kernel_5.shape[1] / 2),)), boundary)
    shape = (pad_image.shape[0] - kernel_5.shape[0] + 1, pad_image.shape[1] - kernel_5.shape[1] + 1) + kernel_5.shape
    strides = pad_image.strides * 2
    # as_strided()でpad_imageをshapeの大きさの配列をスライドしたような配列を生成する
    strided_image_5 = np.lib.stride_tricks.as_strided(pad_image, shape, strides).reshape(shape[0], shape[1], kernel_5.shape[0] * kernel_5.shape[1])

    pad_image = np.pad(image, ((int(kernel_11.shape[0] / 2),), (int(kernel_11.shape[1] / 2),)), boundary)
    shape = (pad_image.shape[0] - kernel_11.shape[0] + 1, pad_image.shape[1] - kernel_11.shape[1] + 1) + kernel_11.shape
    strides = pad_image.strides * 2
    # as_strided()でpad_imageをshapeの大きさの配列をスライドしたような配列を生成する
    strided_image_11 = np.lib.stride_tricks.as_strided(pad_image, shape, strides).reshape(shape[0], shape[1], kernel_11.shape[0] * kernel_11.shape[1])
    '''

    print(strided_image_11.shape)

    print("ノイズ検出")
    t=time.time()
    for i in range((image.shape[0])):
      for j in range((image.shape[1])):
        #if detect(strided_image_3[i][j]==True):
        img_binary[i][j]=W(strided_image_11[i][j])
          #img_cp[i][j] = W(strided_image_11[i][j])
    tt=time.time()
    print("時間")
    print(tt-t)

    

    binary_3 = pad_stride(img_binary,kernel_3,boundary)
    binary_5 = pad_stride(img_binary,kernel_5,boundary)
    binary_7 = pad_stride(img_binary,kernel_7,boundary)
    binary_11 = pad_stride(img_binary,kernel_11,boundary)

    print("ノイズ除去")
    t=time.time()
    for i in range((image.shape[0])):
      for j in range((image.shape[1])):
        if img_binary[i][j] == 1:
          if np.count_nonzero(binary_3[i][j]==1) < 4:
            #3*3
            img_cp[i][j] = W_median(strided_image_3[i][j], (kernel_3_1*(np.ones(binary_3[i][j].shape)-binary_3[i][j]))) 
          elif np.count_nonzero(binary_5[i][j]==1) < 13:
            #5*5
            img_cp[i][j] = W_median(strided_image_5[i][j], (kernel_5_1*(np.ones(binary_5[i][j].shape)-binary_5[i][j])))
          else:
            img_cp[i][j] = W_median(strided_image_7[i][j], (kernel_7_1*(np.ones(binary_7[i][j].shape)-binary_7[i][j])))
    tt=time.time()
    print("時間")
    print(tt-t)
    hyouka.hyou(g.TruenoiseBinary,img_binary)

    return img_cp

    return np.apply_along_axis(lambda a: W(a),2,strided_image_11)

def median(image):
  a = np.median(image)
  return a