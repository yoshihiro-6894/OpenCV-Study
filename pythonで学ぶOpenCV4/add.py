# 2つの画像を加算するプログラム

import cv2

try:
    img1 = cv2.imread("./Images/Lenna.bmp")
    #img1 = cv2.imread("./Images/Lenna.bmp",cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread("./Images/Parrots.bmp")
    #img2 = cv2.imread("./Images/Parrots.bmp",cv2.IMREAD_GRAYSCALE)
    
    
    if img1 is None or img2 is None:
        print("ファイルを読み込めません")
        import sys
        sys.exit()

    cv2.imshow("img1",img1)
    cv2.imshow("img2",img2)

    dst = cv2.add(img1, img2)
    cv2.imwrite("add.jpg",dst)
    
    cv2.imshow("dst",dst)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except:
    import sys
    print("Error", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))