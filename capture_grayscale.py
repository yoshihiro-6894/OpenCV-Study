# 接続されているカメラから映像を取り出しグレイスケールにした後画面に表示するプログラム

import cv2

try:
    capture = cv2.VideoCapture(0)
    
    #cv2.VideoCapture(index)
    #index -> 使用するカメラの番号カメラが一台しか接続されていない場合は0を指定する
    #戻り値　VideoCapture vobj
    #VideoCaptureオブジェクト vobjが戻り値である
    
    while(True):
        ret, frame = capture.read()
        #read
        #次のフレームを読み込みエンコードする
        #戻り値 bool retval, numpy.ndarray image
        #retval 次のフレームが取得可能か(映像が続いているか)を示す審議値
        #image 取得した配列(画像)
        if ret == False:
            print('カメラから映像を取得できませんでした。')
            break
       
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("f",gray)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    capture.release()
    cv2.destroyAllWindows()
except:
    import sys
    print("Error", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))