import numpy as np
import cv2

cap = cv2.VideoCapture('rtsp://admin:88888888abc@192.168.111.198:554/user=admin_password=1b4vojqw_channel=1_stream=0.sdp')

while(True):

    ret, frame = cap.read()
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()