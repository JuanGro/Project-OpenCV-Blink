from pyparrot.Bebop import Bebop
from pyparrot.DroneVisionGUI import DroneVisionGUI
import threading, cv2, time, sys, os

isAlive = False

# Method to implement the drone work
def drone_functionality():
    print("connecting")
    success = bebop.connect(10) #Verifica la conexión
    print(success)

    # No cambiar los valores de las siguientes 3 configuraciones !!!!!!
    bebop.set_max_altitude(2)           #Establece la altitud máxima en 3 metros
    bebop.set_max_tilt(5)               #Establece la velocidad máxima de movimientos angulares en 5°
    bebop.set_max_vertical_speed(0.5)   #Establece la velocidad máxima vertical en 0.5 m/s

    if (success):
        print("sleeping")
        bebop.smart_sleep(4)            #Realiza una pausa en el programa
        bebop.safe_takeoff(10)          #Despega el drone
        bebop.ask_for_state_update()    #Actualiza la información de los sensores
        print("flying state is %s" % bebop.sensors.flying_state) #imprime el estado del drone
        bebop.smart_sleep(4)            #El drone se mantiene 4 segundos en el aire
        bebop.fly_direct(0,0,-65,0,5)
        bebop.ask_for_state_update()    #Actualiza la información de los sensores
        print("flying state is %s" % bebop.sensors.flying_state) #imprime el estado del drone
        bebop.smart_sleep(6)            #El drone se mantiene 4 segundos en el aire
        bebop.fly_direct(0,35,0,0,10)
        bebop.ask_for_state_update()    #Actualiza la información de los sensores
        print("flying state is %s" % bebop.sensors.flying_state) #imprime el estado del drone
        bebop.smart_sleep(6)            #El drone se mantiene 4 segundos en el aire
        bebop.safe_land(10)             #Aterriza el drone
        bebop.ask_for_state_update()    #Actualiza la información de los sensores
        print("flying state is %s" % bebop.sensors.flying_state) #imprime el estado del drone
        print("Battery is %s" % bebop.sensors.battery)  #imprime el estado de la bateria
        print("DONE - disconnecting")
        bebop.disconnect()              #Termina la conexión con el drone

class UserVision:
    def __init__(self, vision):
        self.index = 0
        self.vision = vision

def demo_user_code_after_vision_opened(bebopVision, args):
    bebop = args[0]
    print("Hola  jejeje")
    # takeoff
    bebop.safe_takeoff(5)
    if (bebopVision.vision_running):
        print("Moving the camera using velocity")
        bebop.pan_tilt_camera_velocity(pan_velocity=0, tilt_velocity=-2, duration=4)
        bebop.smart_sleep(5)
        # land
        bebop.safe_land(5)
        print("Finishing demo and stopping vision")
        bebopVision.close_video()

    # disconnect nicely so we don't need a reboot
    print("disconnecting")
    bebop.disconnect()

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
        bebopVision.open_video()
        print("Hola")

        # If no emergency call, execute this (control-c)
        try:
            drone_functionality()
        # If emergency call
        except KeyboardInterrupt:
            # Shown in terminal the emergency
            print('Interrupted')
            try:
                # Wait two seconds
                bebop.smart_sleep(2)
                # Land
                bebop.safe_land(10)
                print("flying state is %s" % bebop.sensors.flying_state) #imprime el estado del drone
                print("Battery is %s" % bebop.sensors.battery)  #imprime el estado de la bateria
                print("DONE - disconnecting")
                bebop.disconnect()
                sys.exit(0)
            except SystemExit:
                # Wait two seconds
                bebop.smart_sleep(2)
                # Land
                bebop.safe_land(10)
                print("flying state is %s" % bebop.sensors.flying_state) #imprime el estado del drone
                print("Battery is %s" % bebop.sensors.battery)  #imprime el estado de la bateria
                print("DONE - disconnecting")
                bebop.disconnect()
                os._exit(0)

    else:
        print("Error connecting to bebop.  Retry")
