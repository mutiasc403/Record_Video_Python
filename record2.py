import cv2
import datetime

cam = cv2.VideoCapture(1)

frame_width = int(cam.get(3))
frame_height = int(cam.get(4))

out = cv2.VideoWriter('videos/p_record_1.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width, frame_height))

while 1:
    ret, jendela = cam.read()

    edge = cv2.Canny(jendela,50, 50)

    gray = cv2.cvtColor(jendela, cv2.COLOR_BGR2GRAY)
    h,w = jendela.shape[:2]
    print(w,h)

    cv2.line(gray, (0,int(h/2)),(w,int(h/2)), (0,255,255), 1)
    cv2.line(gray, (int(w/2),0),(int(w/2),h), (0,255,255), 1)
    cv2.rectangle(gray, (int(w/2)-350, int(h/2)-175), (int(w/2)+350, int(h/2)+175), (0, 255, 0), 2)

    cv2.imshow("save", jendela)
    cv2.imshow("frame", gray)

    if ret == True:
        out.write(jendela)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    else:
        break
cam.release()
out.release()
cv2.destroyAllWindows()