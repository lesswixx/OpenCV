import cv2
def img_proc():
    cap = cv2.VideoCapture('cam_video.mp4')
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray,(21,21),0)
        ret, thresh = cv2.threshold(gray, 105, 255, cv2.THRESH_BINARY_INV)

        contours, hierachy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        if len(contours) > 0:
            c=max(contours,key= cv2.contourArea)
            x, y, w, h = cv2.boundingRect(c)
            cv2.circle(frame, (x+15, y+15 ) , 15 , (0,24,255),3 ,2 )


        cv2.imshow('frame',frame)
        cv2.waitKey(1)


if __name__=='__main__':
    img_proc()

cv2.waitKey(1)
