import cv2
import imutils

cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    ret, frame = cap.read()

    frame = imutils.resize(frame, width=1000, height=300)
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()