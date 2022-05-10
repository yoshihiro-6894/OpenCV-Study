# 2つの画像を減算するプログラム

import cv2
import numpy as np

try:
    img1 = cv2.imread("./Images/Lenna.bmp")
    img2 = cv2.imread("./Images/Parrots.bmp")
    
    
    if img1 is None or img2 is None:
        print("ファイルを読み込めません")
        import sys
        sys.exit()

    cv2.imshow("img1",img1)
    cv2.imshow("img2",img2)
    
    dst = cv2.absdiff(img1, img2)
    cv2.imwrite("absdiff.jpg",dst)
    cv2.imshow("dst1",dst)
    
    height = img1.shape[0]
    width = img1.shape[1]
    blue = np.zeros((height, width,3),np.uint8)
    blue[:,:] = [128,0,0]
    
    dst = cv2.absdiff(img1, blue)
    cv2.imwrite("absdiffScalar.jpg",dst)
    cv2.imshow("dst2",dst)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except:
    import sys
    print("Error", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))