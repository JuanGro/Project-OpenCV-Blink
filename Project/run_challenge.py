from pyparrot.Bebop import Bebop
from pyparrot.DroneVisionGUI import DroneVisionGUI
import threading, cv2, time, sys, os
from drone_functionality import *

isAlive = False

if __name__ == "__main__":
    # make my bebop object
    bebop = Bebop(drone_type="Bebop2")
    # connect to the bebop
    success = bebop.connect(5)

    if (success):
        # start up the video
        bebopVision = DroneVisionGUI(bebop, is_bebop=True, user_code_to_run=drone_functionality,
                                     user_args=(bebop, ))
        bebopVision.open_video()
    else:
        print("Error connecting to bebop. Retry")
