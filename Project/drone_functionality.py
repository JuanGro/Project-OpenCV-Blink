import numpy as np
import cv2 as opencv

def opencv_operations():
    print("OPENCV Welcome")
    face_cascade = opencv.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = opencv.CascadeClassifier('haarcascade_eye.xml')
    try:
        img = opencv.imread('/Users/juan/anaconda3/lib/python3.7/site-packages/pyparrot/images/visionStream.jpg')
        if (img is not None):
            gray = opencv.cvtColor(img, opencv.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            # For each face
            for (x, y, w, h) in faces:
                # Draw a black rectangle
                img = opencv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                roi_gray = gray[y : y + h, x : x + w]
                roi_color = img[y : y + h, x : x + w]
                eyes = eye_cascade.detectMultiScale(roi_gray)

                # For each eye
                for (ex, ey, ew, eh) in eyes:
                    if (ey + ey + eh) / 2 < (y + y + h) / 6:
                        # Draw a green rectangle
                        opencv.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
                        font = opencv.FONT_HERSHEY_SIMPLEX
                        print("EYE")

            # Display the resulting frame
            cv2.imshow('frame',img2)
            print("JA")
    except:
        pass

def print_drone_status(bebop):
    print("flying state is %s" % bebop.sensors.flying_state) #imprime el estado del drone
    print("Battery is %s" % bebop.sensors.battery)  #imprime el estado de la bateria
    print("DONE - disconnecting")

# Method to implement the drone work
def drone_functionality(bebopVision, args):
    bebop = args[0]
    print("Drone working")
    ''' No cambiar los valores de las siguientes 3 configuraciones !!!!!! '''
    #Establece la altitud máxima en 3 metros
    bebop.set_max_altitude(2)
    #Establece la velocidad máxima de movimientos angulares en 5°
    bebop.set_max_tilt(5)
    #Establece la velocidad máxima vertical en 0.5 m/s
    bebop.set_max_vertical_speed(0.5)
    opencv_operations()
    #Actualiza la información de los sensores
    bebop.ask_for_state_update()
    print_drone_status(bebop)
    print("Finishing demo and stopping vision")
    bebopVision.close_video()
    #Termina la conexión con el drone
    bebop.disconnect()
