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

    if (bebopVision.vision_running):
        #El drone se mantiene 6 segundos en el aire
        bebop.smart_sleep(6)
        #Actualiza la información de los sensores
        bebop.ask_for_state_update()
        print_drone_status(bebop)
        print("Finishing demo and stopping vision")
        bebopVision.close_video()
        #Termina la conexión con el drone
        bebop.disconnect()
