import numpy as np
import cv2
import math

import GlobalValue as g


def W(image):
  sort_R = np.sort(image)
  diff_D = np.diff(sort_R)
  argsort = np.argsort(diff_D)
  maxs = argsort[-4:]
  p = np.min(maxs)
  t = np.max(maxs)
  w_min = sort_R[p+1]
  w_max = sort_R[t]
  forcus = image[math.floor(len(image)/2)]
  if (forcus<w_min) or (w_max<forcus):
    g.count= g.count+1
    #return 255
    return np.median(sort_R)
  else:
    #return 0
    return forcus
  print(maxs)
  print(len(image))
  print(math.ceil(len(image)/2))

  return np.median(sort_R)

def median_filter(image, boundary='reflect'):
    img_binary=np.zeros(image.shape)
    img_cp = image.copy()
    print("custom1")

    kernel_3=np.array([[1,2,1],[2,0,2],[1,2,1]])
    pad_image = np.pad(image, ((int(kernel_3.shape[0] / 2),), (int(kernel_3.shape[1] / 2),)), boundary)
    shape = (pad_image.shape[0] - kernel_3.shape[0] + 1, pad_image.shape[1] - kernel_3.shape[1] + 1) + kernel_3.shape
    strides = pad_image.strides * 2
    # as_strided()でpad_imageをshapeの大きさの配列をスライドしたような配列を生成する
    strided_image_3 = np.lib.stride_tricks.as_strided(pad_image, shape, strides).reshape(shape[0], shape[1], kernel_3.shape[0] * kernel_3.shape[1])

    kernel_5=np.array([[1,2,3,2,1],[2,4,5,4,2],[3,5,0,5,3],[2,4,5,4,2],[1,2,3,2,1]])
    pad_image = np.pad(image, ((int(kernel_5.shape[0] / 2),), (int(kernel_5.shape[1] / 2),)), boundary)
    shape = (pad_image.shape[0] - kernel_5.shape[0] + 1, pad_image.shape[1] - kernel_5.shape[1] + 1) + kernel_5.shape
    strides = pad_image.strides * 2
    # as_strided()でpad_imageをshapeの大きさの配列をスライドしたような配列を生成する
    strided_image_5 = np.lib.stride_tricks.as_strided(pad_image, shape, strides).reshape(shape[0], shape[1], kernel_5.shape[0] * kernel_5.shape[1])


    kernel_11=np.zeros((11,11))
    pad_image = np.pad(image, ((int(kernel_11.shape[0] / 2),), (int(kernel_11.shape[1] / 2),)), boundary)
    shape = (pad_image.shape[0] - kernel_11.shape[0] + 1, pad_image.shape[1] - kernel_11.shape[1] + 1) + kernel_11.shape
    strides = pad_image.strides * 2
    # as_strided()でpad_imageをshapeの大きさの配列をスライドしたような配列を生成する
    strided_image_11 = np.lib.stride_tricks.as_strided(pad_image, shape, strides).reshape(shape[0], shape[1], kernel_11.shape[0] * kernel_11.shape[1])
    print(strided_image_11.shape)

    for i in range((image.shape[0])):
      for j in range((image.shape[1])):
        if (strided_image_3[i][j][4]==0) or (strided_image_3[i][j][4]==255):
          #img_binary[i][j]=W(strided_image_11[i][j])
          img_cp[i][j] = W(strided_image_11[i][j])


        

    return img_cp


    return np.apply_along_axis(lambda a: W(a),2,strided_image_11)