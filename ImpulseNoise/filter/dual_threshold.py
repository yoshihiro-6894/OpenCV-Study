'''
/conference/Image_de-noising_by_dual_threshold_median_filtering_for_random_valued_impulse_noise.pdf
'''


import numpy as np

A = np.array([[1,2,3],[4,5,6],[7,8,9]])


avc = np.mean(A,axis=1,dtype=np.float64)
avr = np.mean(A,axis=0,dtype=np.float64)
avdig = np.array([(A[0][0]+A[1][1]+A[2][2])/3.0, 
                  (A[2][0]+A[1][1]+A[0][2])/3.0])

N = np.concatenate([avc, avr, avdig])
sort_a = np.sort(N)

print(avr,avc)

print(avdig)

print(N.shape)

print(sort_a)
if sort_a[0] <= A[1][1] & A[1][1] <= sort_a[7]:
    print("A")
else:
    print("B")