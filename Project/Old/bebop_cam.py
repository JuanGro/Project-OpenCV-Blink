"""
Demo of the Bebop vision using DroneVisionGUI (relies on libVLC).  It is a different
multi-threaded approach than DroneVision
Author: Amy McGovern
"""
from pyparrot.Bebop import Bebop
from pyparrot.DroneVisionGUI import DroneVisionGUI
import threading
import cv2
import time

face_cascade = cv2.CascadeClassifier(r'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(r'haarcascade_eye.xml')
isAlive = False

class UserVision:
    def __init__(self, vision):
        self.index = 0
        self.vision = vision

    def save_pictures(self, args):
        #print("saving picture")
        img = self.vision.get_latest_valid_picture()
        #img2 = cv2.imread(r'C:\ProgramData\Anaconda3\Lib\site-packages\pyparrot\images\visionStream.jpg')
        #cv2.imshow('image',img2)
        if (img is not None):
            filename = "test_image_%06d.jpg" % self.index
            #img2 = cv2.imread(filename)
            #cv2.imshow('image',img2)
            self.index +=1


def demo_user_code_after_vision_opened(bebopVision, args):
    bebop = args[0]

    print("Vision successfully started!")
    #removed the user call to this function (it now happens in open_video())
    #bebopVision.start_video_buffering()
    bebop.ask_for_state_update()    #Actualiza la información de los sensores
    print("flying state is %s" % bebop.sensors.flying_state) #imprime el estado del drone
    print("Battery is %s" % bebop.sensors.battery)  #imprime el estado de la bateria
    while(True):
        try:
            img2 = cv2.imread(r'/Users/juan/anaconda3/lib/python3.7/site-packages/pyparrot/images/visionStream.jpg')
            if (img2 is not None):
                """gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
                cv2.imshow('frame',gray)"""

                # Our operations on the frame come here
                gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

                faces = face_cascade.detectMultiScale(gray, 1.3, 5)
                for (x,y,w,h) in faces:
                    img2 = cv2.rectangle(img2,(x,y),(x+w,y+h),(255,0,0),2)
                    roi_gray = gray[y:y+h, x:x+w]
                    roi_color = img2[y:y+h, x:x+w]
                    eyes = eye_cascade.detectMultiScale(roi_gray)
                    for (ex,ey,ew,eh) in eyes:
                        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
                #time.sleep(1.0) # Sleep for 1 second minus elapsed time
        except:
            pass
    print("DONE - disconnecting")
    bebop.disconnect()              #Termina la conexión con el drone

if __name__ == "__main__":
    # make my bebop object
    bebop = Bebop(drone_type="Bebop2")

    # connect to the bebop
    success = bebop.connect(5)

    if (success):
        # start up the video
        bebopVision = DroneVisionGUI(bebop, is_bebop=True, user_code_to_run=demo_user_code_after_vision_opened,
                                     user_args=(bebop, ))

        userVision = UserVision(bebopVision)
        bebopVision.set_user_callback_function(userVision.save_pictures, user_callback_args=None)
        bebopVision.open_video()

    else:
        print("Error connecting to bebop.  Retry")
