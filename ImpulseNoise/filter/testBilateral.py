import cv2
import numpy as np

#10,2

def bilateral_filter(image, size=(5, 5), space_sigma=2, pixel_sigma=6.7, boundary='reflect'):
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
  weights = np.exp(-dists / (2.0 * space_sigma * space_sigma)) * np.exp(-((centers - areas) ** 2) / (2.0 * pixel_sigma * pixel_sigma * 2.0))
  #print(weights.shape)
  weight_sum = np.sum(weights, axis=(2, 3))
  #print(weight_sum)
  #print(np.where(weight_sum>=8, 1, 0))

  lci = GetLCI(weight_sum)

  pad_lci = np.pad(lci, ((int(size[0]/2),), (int(size[1]/2,),)),boundary)
  lci_area = np.lib.stride_tricks.as_strided(pad_lci,lci.shape+size,pad_lci.strides*2)
  print(lci_area.shape)

  #return np.einsum('ijkl,ijkl->ij',areas,lci_area**2) / np.sum(lci_area**2,axis=(2,3))

  return GetLCI(weight_sum)

  #return np.where(weight_sum >= 8, 1, 0)

  #バイラテラルフィルタをするときはこれをリターンする
  return np.einsum('ijkl,ijkl->ij', weights, areas) / weight_sum


def custom(image, size=(3, 3), boundary='reflect'):
    g = bilateral_filter(image, size=(5, 5), boundary='reflect')
    img_cp=image.copy()
    pad_image = np.pad(image, ((int(size[0] / 2),), (int(size[1] / 2),)), boundary)
    areas = np.lib.stride_tricks.as_strided(pad_image, image.shape + size, pad_image.strides * 2)
    print(areas.shape)

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if g[i][j]==1:
                img_cp[i][j]=np.median(areas[i][j])
    return img_cp


def GetLCI(inputarray,size=(5,5),boundary='reflect'):
    pad = np.pad(inputarray,((int(size[0] / 2),), (int(size[1] / 2),)), boundary)
    areas = np.lib.stride_tricks.as_strided(pad, inputarray.shape + size, pad.strides * 2)
    w = np.mean(areas,axis=(2,3))
    d = inputarray / w
    retval = np.where(d >=2.5, 1, d/2.5)
    print(retval)
    return retval

def testbilateral(image, size=(5, 5), space_sigma=10, pixel_sigma=6.7, boundary='reflect'):
  pad_image = np.pad(image, ((int(size[0] / 2),), (int(size[1] / 2),)), boundary)
  #print(pad_image)
  areas = np.lib.stride_tricks.as_strided(pad_image, image.shape + size, pad_image.strides * 2)
  centers = np.tile(image.reshape(image.shape + (1, 1)), (1, 1) + size)
  dists = np.fromfunction(lambda y, x: (x - int(size[1] / 2)) ** 2 + (y - int(size[0] / 2)) ** 2, size)
  weights = np.exp(-dists / (2.0 * space_sigma * space_sigma)) * np.exp(-((centers - areas) ** 2) / (2.0 * pixel_sigma * pixel_sigma * 2.0))
  weight_sum = np.sum(weights, axis=(2, 3))
  return np.einsum('ijkl,ijkl->ij', weights, areas) / weight_sum

'''
input = np.array([[141, 141, 35, 6, 52, 139, 34, 138, 9, 138, 138],\
[141,196,140, 34, 0,12,102,140,139,138,175],\
[141,69,141,47,137,180,142,0,0,11,139],\
[141,142,31,210,142,140,143,103,143,143,139],\
[147,142,144,144,140,141,141,140,144,30,71],\
[140,255,141,141,255,142,143,1,189,192,142],\
[103,160,144,242,75,146,165,142,144,22,139],\
[145,0,143,142,84,141,55,143,143,3,255],\
[139,139,143,143,143,145,142,140,190,0,255],\
[138,34,197,146,146,144,141,139,117,163,142],\
[140,0,139,129,143,142,141,137,136,138,141]])

print(np.round(bilateral_filter(input),decimals=1))

'''