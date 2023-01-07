import cv2
import trimming_app
import os


camera = cv2.VideoCapture(0)

def save_photo(frame):

    cv2.imwrite('camera.jpg', frame)
    camera.release()
    cv2.destroyAllWindows()
while True:
    ret, frame = camera.read()
    if not ret:
      break

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
  
  # Escキーを入力されたら画面を閉じる
    if key == 27:
        save_photo(frame)
        trimming_app.trimming("camera.jpg")#これによってtrimmingappに移行
        break
'''----------------ここからインターフェイス--------------------'''
import sql
import userinterface








