import cv2
import numpy as np

try:
    img = cv2.imread("./Images/Lenna.bmp")
    
    if img is None:
        print("ファイルを読み込めません")
        import sys
        sys.exit()
        
    rows, cols = img.shape[:2]
    print(rows,cols)
    
    x0 = cols/4
    x1 = (cols*3)/4
    y0 = rows/4
    y1 = (rows*3)/4
    
    list_src = np.float32([[x0, y0], [x0, y1], [x1, y1], [x1, y0]])
    print(list_src)
    
    #pattern-0
    x_margin = cols/10
    y_margin = rows/10
    list_dsts = np.float32([[x0+x_margin,y0+y_margin],list_src[1],list_src[2],
                           [x1-x_margin,y0_margin]])
    
    
        
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except:
    import sys
    print("Error", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))