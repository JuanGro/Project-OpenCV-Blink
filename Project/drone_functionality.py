import numpy as np
import cv2 as opencv
from opencv_operations import *
from follow import *

def print_drone_status(bebop):
    #imprime el estado del drone
    print("flying state is %s" % bebop.sensors.flying_state)
    #imprime el estado de la bateria
    print("Battery is %s" % bebop.sensors.battery)

# Method to implement the drone work
def drone_functionality(bebopVision, args):
    bebop = args[0]
    ''' No cambiar los valores de las siguientes 3 configuraciones !!!!!! '''
    #Establece la altitud máxima en 3 metros
    bebop.set_max_altitude(2)
    #Establece la velocidad máxima de movimientos angulares en 5°
    bebop.set_max_tilt(5)
    #Establece la velocidad máxima vertical en 0.5 m/s
    bebop.set_max_vertical_speed(0.5)
    #Actualiza la información de los sensores
    bebop.ask_for_state_update()
    print_drone_status(bebop)
    # Start
    print("sleeping")
    #Realiza una pausa en el programa
    bebop.smart_sleep(4)
    #Despega el drone
    bebop.safe_takeoff(10)
    print("flying state is %s" % bebop.sensors.flying_state) #imprime el estado del drone

    while(True):
        if is_there_a_blink():
            print("Blink")
            #break because there is a LAND
        elif is_there_a_face():
            print("Should follow the person")
            #follow(bebop)
        else:
            #Looking for a person
            bebop.fly_direct(0, 0, 10, 0, 1)
            bebop.ask_for_state_update()
            bebop.smart_sleep(1)

    #Land
    bebop.smart_sleep(4)
    bebop.safe_land(10)
    print("Finishing demo and stopping vision")
    bebopVision.close_video()
    bebop.disconnect()
