import cv2
import numpy as np
from PIL import Image

# Black=1
#white=0
# [[
#     255,0,0
#     0,255,0
#     0,0,255
# ]]
# image=cv2.imread("./MG_4953.jpg")
# resized_img=cv2.resize(image,(550,700))

# # crop_img=resized_img[250:550,50:100]
# # Blur_IMG=cv2.blur(resized_img,(15,15))
# RGB_IMG=cv2.cvtColor(resized_img,cv2.COLOR_BGR2RGB)
# HSV_IMG=cv2.cvtColor(resized_img,cv2.COLOR_RGB2HSV)
# GREY_IMG=cv2.cvtColor(resized_img,cv2.COLOR_BGR2GRAY)
# Edge_detect=cv2.Canny(GREY_IMG,80,150)
# feature,threshold=cv2.threshold(GREY_IMG,60,150,cv2.THRESH_BINARY)
# THRESH_BLUR=cv2.blur(threshold,(10,10))
# feat_ure,thresh=cv2.threshold(THRESH_BLUR,60,150,cv2.THRESH_BINARY)
# line_draw=cv2.line(resized_img,(20,50),(300,50),(0,255,0),10)
# box_draw=cv2.rectangle(line_draw,(40,50),(400,300),(0,0,255),10)
# circle_draw=cv2.circle(box_draw,(225,350),50,(255,0,0),10)
# text_add=cv2.putText(circle_draw,"Hello Everyone",(45,450),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),10)
# contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# for cv in contours:
#     if cv2.contourArea(cv)>200:
#         cv2.drawContours(resized_img, cv, -1, (0,255,0), 3)

# cv2.imshow("model",resized_img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()


#----------VIDEO----------------

# capture=cv2.VideoCapture("./1900-151662242_small.mp4")
# car_cascade = cv2.CascadeClassifier("./haarcascade_car.xml")
# while True:
#     rlt,frame=capture.read()
#     grey_scale=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#     OBJ_DETECTION=car_cascade.detectMultiScale(grey_scale,scaleFactor=1.1,minNeighbors=3)
#     for x,y,wid,hei in OBJ_DETECTION:
#         box_object=cv2.rectangle(frame,(x,y),(wid,hei),(0,0,255),4)
#     cv2.imshow("VID",frame)
#     if not rlt:
#         break
#     if cv2.waitKey(60) & 0xff==ord('q'):
#         break
# capture.release()
# cv2.destroyAllWindows()


capture=cv2.VideoCapture(0)

while True:
    rlt,frame=capture.read()

    grey_scale=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower_blue = np.array([35, 50, 50])
    upper_blue = np.array([85, 255, 255])

    mask_one=cv2.inRange(grey_scale,lower_blue,upper_blue)

    mask_two=Image.fromarray(mask_one)

    entry=mask_two.getbbox()

    if entry is not None:
        x,y,wid,hei=entry
        box=cv2.rectangle(frame,(x,y),(wid,hei),(0,255,0),10)


    cv2.imshow("detect_obj",frame)

    if not rlt:
        break
    if cv2.waitKey(60) & 0xff==ord('q'):
        break


capture.release()
cv2.destroyAllWindows()