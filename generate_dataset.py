#Import the libraries
import time
from cv2 import cv2

def capture_image(number_of_images):

    #Connects to the webcam
    cap = cv2.VideoCapture(0)
    time.sleep(3)

    for i in range(number_of_images):

        ret, frame = cap.read()
        img_name = '.\\image\\all\\{}.jpg'.format(str(i))
        cv2.imwrite(img_name, frame)
        cv2.imshow('frame', frame)
        time.sleep(1)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()