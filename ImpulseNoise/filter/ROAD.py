import cv2
import numpy as np

def ROAD(image, size=(5, 5),boundary='reflect'):
  pad_image = np.pad(image, ((int(size[0] / 2),), (int(size[1] / 2),)), boundary)
  #print(pad_image)
  areas = np.lib.stride_tricks.as_strided(pad_image, image.shape + size, pad_image.strides * 2)
  #print(areas.shape)
  centers = np.tile(image.reshape(image.shape + (1, 1)), (1, 1) + size)
  #print(image.shape+(1,1))
  #print(((1, 1) + size))
  #print(centers.shape)
  #print((centers-areas).shape)
  b = np.sort(np.abs((centers-areas).reshape(centers.shape[0], centers.shape[1],centers.shape[2]*centers.shape[3])))
  #print(int((size[0]*size[1]+1)/2))
  #print(b[:,:,:int((size[0]*size[1]+1)/2)].sum(axis=2))
  return b[:,:,:int((size[0]*size[1]+1)/2)].sum(axis=2)

'''
inputArray = np.arange(1,37).reshape(6,6)
print(inputArray)
out = ROAD(inputArray)
'''