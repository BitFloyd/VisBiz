import cv2
from classico.faces import FaceDetector as FD
import os

cap = cv2.VideoCapture(0)
fd = FD(face_cascade=os.path.join('..','data_folder','haarcascades','haarcascade_profileface.xml'),
        face_profile_cascade=os.path.join('..','data_folder','haarcascades','haarcascade_frontalface_default.xml'),
        eye_cascade=None,
        eyes=False)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    detect_frame = fd.detect_face_from_img(frame)
    # Display the resulting frame
    cv2.imshow('frame',detect_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()