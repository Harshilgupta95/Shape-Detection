import cv2

cap = cv2.VideoCapture(0)

while True:
    ret,img= cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    edged = cv2.Canny(gray, 170, 255)
    # cv2.imshow('edged',edged)
    # cv2.waitKey(0)
    ret,thresh = cv2.threshold(gray,170,255,cv2.THRESH_BINARY)
# cv2.imshow('thresh',thresh)
# cv2.waitKey(0)
    (contours,_) = cv2.findContours(edged,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
# print(contours)
# c=cv2.drawContours(img,contours,3,(0,255,255),3)


    def detectShape(c):
        shape = 'unknown'
        peri=cv2.arcLength(cnt,True)
        vertices = cv2.approxPolyDP(cnt, 0.02 * peri, True)
        sides = len(vertices)
        global x,y
        x = vertices.ravel()[0]
        y = vertices.ravel()[1]

        if (sides == 3):
            shape='triangle'
        elif(sides==4):
            x,y,w,h=cv2.boundingRect(cnt)
            aspectratio=float(w)/h
            if (aspectratio==1):
                shape='square'
            else:
                shape="rectangle"
        elif(sides==5):
            shape='pentagon'
        elif(sides==6):
            shape='hexagon'
        elif(sides==8):
            shape='octagon'
        elif(sides==10):
            shape='star'
        else:
            shape='circle'
        return shape

    for cnt in contours:
        moment=cv2.moments(cnt)
        # if(moment['m00']==0):
        #     break
        # else:
        # cx = int(moment['m10'] / moment['m00'])
        # cy = int(moment['m01'] / moment['m00'])
        shape=detectShape(cnt)

        cv2.drawContours(img,[cnt],-1,(0,255,0),2)
        cv2.putText(img,shape,(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)
    cv2.imshow('sd',img)
    if cv2.waitKey(1) == 27:
        break
cap.release()
cv2.destroyAllWindows()