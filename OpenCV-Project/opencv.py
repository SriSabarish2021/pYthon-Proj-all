import cv2


# image=cv2.imread("./4W8A1967.JPG")
# size_reduce=cv2.resize(image,(1000,700))
# grey_img=cv2.cvtColor(size_reduce,cv2.COLOR_BGR2GRAY)
# ret,THRESHOLG=cv2.threshold(grey_img,80,200,cv2.THRESH_BINARY_INV)
# contours, hierarchy = cv2.findContours(THRESHOLG, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# # croped_img=size_reduce[50:100, 100:150]
# # CLR_CHANGE=cv2.cvtColor(size_reduce,cv2.COLOR_BGR2RGB)
# # blur_img=cv2.medianBlur(size_reduce,7)
# # ret,threshold=cv2.threshold(size_reduce,85,255,cv2.THRESH_BINARY_INV)
# # edge_img=cv2.Canny(liner,100,100)
# # liner=cv2.line(size_reduce,(30,50),(300,200),(0,0,255),5)
# # boxer=cv2.rectangle(size_reduce,(30,50),(300,400),(255,0,0),2)
# # circle=cv2.circle(size_reduce,(250,250),100,(255,0,0),-1)
# for cv in contours:
    
#     cont_val=cv2.contourArea(cv)
#     if cont_val>200:
#         cv2.drawContours(size_reduce,cv,-1,(0,255,0),5)
# cv2.imshow("My_image",size_reduce)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



#   VIDEOOOO

# capture=cv2.VideoCapture(0)

# while True:
#     rlt,frame=capture.read()
#     cv2.imshow("vid",frame)
#     if cv2.waitKey(40) &  0xFF==ord("q"):
#         break
        
# capture.release()
# cv2.destroyAllWindows()


import cv2

# Load car detection model
car_cascade = cv2.CascadeClassifier("./haarcascade_car.xml")

# Load video (use 0 for webcam)
cap = cv2.VideoCapture("./1900-151662242_small.mp4")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect cars
    cars = car_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=3
    )

    # Draw rectangles around cars
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Car Detection", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC key
        break

cap.release()
cv2.destroyAllWindows()
