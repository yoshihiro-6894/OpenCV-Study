import numpy as np
import cv2
import math

import GlobalValue as g

def pad_stride(image,kernel,boundary):
  pad_image = np.pad(image, ((int(kernel.shape[0] / 2),), (int(kernel.shape[1] / 2),)), boundary)
  shape = (pad_image.shape[0] - kernel.shape[0] + 1, pad_image.shape[1] - kernel.shape[1] + 1) + kernel.shape
  strides = pad_image.strides * 2
  # as_strided()でpad_imageをshapeの大きさの配列をスライドしたような配列を生成する
  return np.lib.stride_tricks.as_strided(pad_image, shape, strides).reshape(shape[0], shape[1], kernel.shape[0] * kernel.shape[1])


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
  return np.median(a)

def median_filter(image, boundary='reflect'):
    img_binary=np.zeros(image.shape)
    img_cp = image.copy()
    print("custom1")

    kernel_3=np.array([[1,2,1],[2,0,2],[1,2,1]])
    kernel_3_1=kernel_3.reshape(9,)
    kernel_5=np.array([[1,2,3,2,1],[2,4,5,4,2],[3,5,0,5,3],[2,4,5,4,2],[1,2,3,2,1]])
    kernel_5_1=kernel_5.reshape(kernel_5.shape[0]*kernel_5.shape[1])
    print(kernel_5)
    print(kernel_5_1)
    kernel_11=np.zeros((11,11))
    strided_image_3 = pad_stride(image,kernel_3,boundary)
    strided_image_5 = pad_stride(image,kernel_5,boundary)
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

    for i in range((image.shape[0])):
      for j in range((image.shape[1])):
        if (strided_image_3[i][j][4]==0) or (strided_image_3[i][j][4]==255):
          img_binary[i][j]=W(strided_image_11[i][j])
          #img_cp[i][j] = W(strided_image_11[i][j])

    binary_3 = pad_stride(img_binary,kernel_3,boundary)
    print(binary_3.shape)
    binary_5 = pad_stride(img_binary,kernel_5,boundary)
    binary_11 = pad_stride(img_binary,kernel_11,boundary)

    
    for i in range((image.shape[0])):
      for j in range((image.shape[1])):
        if img_binary[j][i] == 1:
          if np.count_nonzero(binary_3[j][i]==1) < 4:
            #3*3
            #print(binary_3[j][i])
            img_cp[j][i] = W_median(strided_image_3[j][i], (kernel_3_1*binary_3[j][i])) 
          elif np.count_nonzero(binary_5[j][i]==1) < 13:
            #5*5
            #print(binary_5[j][i])
            img_cp[j][i] = W_median(strided_image_5[j][i], (kernel_5_1*binary_5[j][i]))
          else:
            img_cp[j][i] = median(strided_image_11[j][i])

    
    

    return img_cp


    return np.apply_along_axis(lambda a: W(a),2,strided_image_11)

def median(image):
  a = np.median(image)
  return a