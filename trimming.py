# トリミング
import cv2

try:
    img = cv2.imread("./Images/Lenna.bmp")
    
    if img is None:
        print("ファイルを読み込めません")
        import sys
        sys.exit()
        
    height = img.shape[0]
    width = img.shape[1]
    
    dst = img[40:height, 100:width]
    cv2.imwrite("./Trimming.jpg",dst)
    
    cv2.imshow("dst",dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except:
    import sys
    print("Error", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))