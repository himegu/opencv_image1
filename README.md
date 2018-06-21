# opencv_image1
opencvでカメラの画像を表示

コードをいかに記す。

    import cv2

    capture=cv2.VideoCapture(1) # VideoCapture オブジェクトを取得
    capture.set(3,1280)
    capture.set(4,960)
    capture.set(5,15)   #取得した画像を表示するフレームの大きさを設定

    while(True):
      ret, frame = capture.read()   #カメラから1コマのデータを取得

      cv2.imshow('frame', frame)    #OSのフレーム(ウィンドウ)に画像を表示
      k=cv2.waitKey(1)	
      if k==27:   #Escキーをタイプするとループを抜ける
        break

    capture.release()   # キャプチャをリリース
    cv2.destroyAllWindows()   #ウィンドウをすべて閉じる


カメラから連続的に画像を取得するため、While文で繰り返し処理を行っている。
While文内ではまずカメラから1コマのデータを取得するためcapture.read()を呼び出し、取得した画像データは変数frameに代入。
cv2.imshow()は第1引数に開くフレームの名前を、第2引数にcapture.read()によって取得した画像データを指定する。
cv.2imshow()を呼び出すと自動的にフレームが立ち上がり画像を表示することができる。
