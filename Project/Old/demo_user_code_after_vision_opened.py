def demo_user_code_after_vision_opened(bebopVision, args):
    bebop = args[0]
    print("Hola demo")
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
