import numpy as np
import padding

def LCI(image, size=(7, 7), space_sigma=10, pixel_sigma=2, boundary='reflect'):
  pad_image = np.pad(image, ((int(size[0] / 2),), (int(size[1] / 2),)), boundary)
  #print(pad_image)
  areas = np.lib.stride_tricks.as_strided(pad_image, image.shape + size, pad_image.strides * 2)
  #print(areas.shape)
  centers = np.tile(image.reshape(image.shape + (1, 1)), (1, 1) + size)
  #print(image.shape+(1,1))
  #print(((1, 1) + size))
  #print(centers.shape)
  dists = np.fromfunction(lambda y, x: (x - int(size[1] / 2)) ** 2 + (y - int(size[0] / 2)) ** 2, size)
  #print(dists)
  weights = np.exp(-dists / (2.0 * space_sigma * space_sigma)) * np.exp(-((centers - areas) ** 2) / (2.0 * pixel_sigma * pixel_sigma))
  #print(weights.shape)
  weight_sum = np.sum(weights, axis=(2, 3))
  #print(weight_sum)
  #print(np.where(weight_sum>=8, 1, 0))

  return Calculate_LCI(weight_sum, size=size)

def Calculate_LCI(inputarray,size,boundary='reflect'):
  pad = np.pad(inputarray,((int(size[0] / 2),), (int(size[1] / 2),)), boundary)
  areas = np.lib.stride_tricks.as_strided(pad, inputarray.shape + size, pad.strides * 2)
  w = np.mean(areas,axis=(2,3))
  d = inputarray / w

  retval = np.where(d >=2.5, 1, d/2.5)
  #print(retval)
  return retval

def detectNoise(image, size=(7, 7), space_sigma=10, pixel_sigma=2, boundary='reflect'):
  pad_image = np.pad(image, ((int(size[0] / 2),), (int(size[1] / 2),)), boundary)
  #print(pad_image)
  areas = np.lib.stride_tricks.as_strided(pad_image, image.shape + size, pad_image.strides * 2)
  print(areas.shape)
  print((padding.pad_stride(image,np.zeros(size),boundary=boundary)).shape)
  centers = np.tile(image.reshape(image.shape + (1, 1)), (1, 1) + size)
  dists = np.fromfunction(lambda y, x: (x - int(size[1] / 2)) ** 2 + (y - int(size[0] / 2)) ** 2, size)
  weights = np.exp(-dists / (2.0 * space_sigma * space_sigma)) * np.exp(-((centers - areas) ** 2) / (2.0 * pixel_sigma * pixel_sigma))
  weight_sum = np.sum(weights, axis=(2, 3))
  print(weight_sum.shape)
  return (np.where(weight_sum>=1, 1, 0))