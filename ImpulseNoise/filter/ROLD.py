import cv2
import numpy as np

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