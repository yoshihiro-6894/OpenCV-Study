# 2つの画像を加算する際にマスクを使用するプログラム

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
    
    height = img1.shape[0]
    width = img2.shape[1]
    
    img_mask = np.zeros((height, width), np.uint8)
    img_mask[height//4:height*3//4, width//4:width*3//4] = [255]
    
    cv2.imshow("mask",img_mask)

    dst = cv2.add(img1, img2, mask = img_mask)
    cv2.imwrite("addMask1.jpg",dst)
    cv2.imshow("dst1",dst)
    
    dst = cv2.add(img1, img2, dst = img1, mask = img_mask)
    cv2.imwrite("addMask2.jpg",dst)
    cv2.imshow("dst2",dst)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except:
    import sys
    print("Error", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))