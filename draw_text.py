import cv2
import sys

try:
    if(len(sys.argv) != 2):
        print('引数に読み込む画像を指定する必要があります')
        sys.exit()
    
    img = cv2.imread(sys.argv[1])
    
    if img is None:
        print('ファイルを読み込めません')
        import sys
        sys.exit()
        
    
    cv2.putText(img, 'Hello OpenCV', (50,50),cv2.FONT_HERSHEY_SIMPLEX, 0.8, (50,60,80),2)
    
    cv2.imwrite('./puttext.jpg', img)
    
    cv2.imshow('img',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except:
    import sys
    print("Error",sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))