# 画像の収縮を行う

import cv2
import numpy as np

try:
    #img = cv2.imread("./Images/Lenna.bmp")
    img = cv2.imread("./Images/Lenna.bmp",cv2.IMREAD_GRAYSCALE)
    
    if img is None:
        print("ファイルを読み込めません")
        import sys
        sys.exit()

    cv2.imshow("img",img)
    
    kernel = np.ones((3,3),np.uint8)
    dst = cv2.erode(img,kernel)
    cv2.imwrite("erode.jpg",dst)
    cv2.imshow("dst1",dst)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except:
    import sys
    print("Error", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))