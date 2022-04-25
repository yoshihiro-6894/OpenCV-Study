#画像に円を描画する

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
    
    #cv2.circle(対象配列(画像),中心座標,円の半径,円の色,太さ(-の場合は塗りつぶす))
    cv2.circle(img, (50, 50), 40, (0, 255, 0), 2)
    cv2.circle(img, (150, 150), 80, (255, 255, 0), 6)
    cv2.circle(img, (200, 200), 50, (0, 255, 255), -1)
    
    cv2.imwrite('./CirclesOnImage.jpg', img)
    
    cv2.imshow('img',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except:
    import sys
    print("Error",sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))