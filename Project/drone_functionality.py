# Method to implement the drone work
def drone_functionality(bebopVision, args):
    bebop = args[0]
    print("Drone working")

    # No cambiar los valores de las siguientes 3 configuraciones !!!!!!
    bebop.set_max_altitude(2)           #Establece la altitud máxima en 3 metros
    bebop.set_max_tilt(5)               #Establece la velocidad máxima de movimientos angulares en 5°
    bebop.set_max_vertical_speed(0.5)   #Establece la velocidad máxima vertical en 0.5 m/s

    if (bebopVision.vision_running):
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
        # Done
        print("Finishing demo and stopping vision")
        bebopVision.close_video()
        #Termina la conexión con el drone
        bebop.disconnect()
