# 2つの画像をブレンドするプログラム

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
    
    dst = cv2.addWeighted(img1, 0.3, img2, 0.7, 0.0)
    cv2.imwrite("blend0307.jpg", dst)
    cv2.imshow("dst1",dst)
    
    dst = cv2.addWeighted(img1, 0.6, img2, 0.4, 0.0)
    cv2.imwrite("blend0604.jpg", dst)
    cv2.imshow("dst2",dst)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except:
    import sys
    print("Error", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))