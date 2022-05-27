# Sobelフィルタを用いたエッジ検出

import cv2

try:
    #img = cv2.imread("./Images/Lenna.bmp")
    img = cv2.imread("./Images/Lenna.bmp",cv2.IMREAD_GRAYSCALE)
    #img = cv2.imread("./D-Textureless/train/model_03.png")
    
    if img is None:
        print("ファイルを読み込めません")
        import sys
        sys.exit()

    cv2.imshow("img",img)
    
    dst = cv2.Sobel(img, -1, 0, 1)
    cv2.imwrite("sobel.jpg",dst)
    cv2.imshow("dst1",dst)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except:
    import sys
    print("Error", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))