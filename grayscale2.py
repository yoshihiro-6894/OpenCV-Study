# グレースケール画像へ変換する
import cv2

try:
    img = cv2.imread("./Images/Lenna.bmp")
    
    if img is None:
        print("ファイルを読み込めません")
        import sys
        sys.exit()
        
    dst = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    cv2.imwrite("./grayscale.jpg",img)
    
    cv2.imshow("img",img)
    cv2.imshow("dst",dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except:
    import sys
    print("Error", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))