import cv2
import numpy as np
import math
import padding

def detect_reshape(inputImage,windowSize):
    Threshold=5
    print(windowSize)
    Direct_coordinates = np.empty([4,0])
    print(Direct_coordinates.shape)
    Direct_coordinates_list = Direct_coordinates.tolist()
    center = inputImage[int(windowSize/2)*windowSize + int(windowSize)]
    for i in range(windowSize):
        if i == int(windowSize/2):
            continue
        #print(i,i)
        #print(int(windowSize/2),i)
        print(windowSize-i-1,i)
        #print(i,int(windowSize/2))
        '''
        Direct_coordinates_list[0].append(inputImage[i,i])
        Direct_coordinates_list[1].append(inputImage[int(windowSize/2),i])
        Direct_coordinates_list[2].append(inputImage[windowSize-1-i,i])
        Direct_coordinates_list[3].append(inputImage[i,int(windowSize/2)])
        '''
        Direct_coordinates_list[0].append(inputImage[i*windowSize+i])
        Direct_coordinates_list[1].append(inputImage[int(windowSize/2)*windowSize + i])
        Direct_coordinates_list[2].append(inputImage[(windowSize-1-i)*windowSize + i])
        Direct_coordinates_list[3].append(inputImage[i*windowSize + int(windowSize/2)])
    Direct_coordinates = np.asarray(Direct_coordinates_list)
    print(Direct_coordinates)
    centers = np.tile(inputImage[int(windowSize/2)*windowSize + int(windowSize/2)],(Direct_coordinates.shape))

    directions = np.abs(Direct_coordinates - centers)
    sum_directions = np.tile(np.sum(directions,axis=1),(directions.shape[1],1)).T
    print(directions)
    print(sum_directions)
    print(sum_directions.shape)
    print(directions/sum_directions)
    print(directions/sum_directions * directions)
    sorted_direct = np.sort(directions/sum_directions * directions)
    print("\n")
    print(sorted_direct)
    print(sorted_direct[:,:-1])
    print(np.sum(sorted_direct[:,:-1], axis=1))
    sum_sorted_direct = np.sum(sorted_direct[:,:-1],axis=1)
    print(np.min(sum_sorted_direct))

    if np.min(sum_sorted_direct) <= Threshold:
        return 0

    return 1

def detect(inputImage,windowSize,Threshold=5):
    Direct_coordinates = np.empty([4,0])
    Direct_coordinates_list = Direct_coordinates.tolist()
    for i in range(windowSize):
        if i == int(windowSize/2):
            continue
        #print(i,i)
        #print(int(windowSize/2),i)
        #print(windowSize-i-1,i)
        #print(i,int(windowSize/2))
        Direct_coordinates_list[0].append(inputImage[i,i])
        Direct_coordinates_list[1].append(inputImage[int(windowSize/2),i])
        Direct_coordinates_list[2].append(inputImage[windowSize-1-i,i])
        Direct_coordinates_list[3].append(inputImage[i,int(windowSize/2)])

    Direct_coordinates = np.asarray(Direct_coordinates_list)
    centers = np.tile(inputImage[int(windowSize/2), int(windowSize/2)],(Direct_coordinates.shape))
    
    directions = np.abs(Direct_coordinates - centers)
    sum_directions = np.tile(np.sum(directions,axis=1),(directions.shape[1],1)).T
    sorted_direct = np.sort(directions/sum_directions * directions)
    sum_sorted_direct = np.sum(sorted_direct[:,:-1],axis=1)
    if np.min(sum_sorted_direct) <= Threshold:
        
        return 0
    if np.isnan(np.min(sum_sorted_direct)):
        return 0
    return 1


'''
#テスト用
asize=5

b = np.zeros((asize,asize))

for i in range(asize):
    for j in range(asize):
        b[i,j] = i*asize + j

b = np.array(([189,3,192,189,189],[189,80,192,189,190],[189,189,192,189,190],[189,80,192,189,190],[189,3,192,189,189]))

c = padding.pad_stride(b,np.zeros((asize,asize)))
detect(c[1,2],asize)
'''