def is_face(w):
    if w > 50:
        return True
    else:
        return False

def get_width_of_first_face(faces):
    # For each face
    for (x, y, w, h) in faces:
        return w
    return 'No face'

def follow(bebop):
    face_cascade = opencv.CascadeClassifier(path_face_xml)
    try:
        img = opencv.imread(r'/Users/juan/anaconda3/lib/python3.7/site-packages/pyparrot/images/visionStream.jpg')
        if (img is not None):
            gray = opencv.cvtColor(img, 0)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            if is_face(get_width_of_first_face(faces)):
                #Estoy no centrado Izq der
                if (x + (w / 2)) > (856 / 2 + 20):
                    bebop.fly_direct(20, 0, 0, 0, 1)
                    bebop.ask_for_state_update()
                    bebop.smart_sleep(1)
                elif (x + (w / 2)) < (856 / 2 - 20):
                    bebop.fly_direct(-20, 0, 0, 0, 1)
                    bebop.ask_for_state_update()
                    bebop.smart_sleep(1)
                #Estoy no centrado Arriba abajo
                if (y + (h / 2)) > (480 / 2 + 20):
                    bebop.fly_direct(0, 0, 0, -1, 1)
                    bebop.ask_for_state_update()
                    bebop.smart_sleep(1)
                elif (y + (h / 2)) < (480 / 2 - 20):
                    bebop.fly_direct(0, 0, 0, 1, 1)
                    bebop.ask_for_state_update()
                    bebop.smart_sleep(1)
                #Estoy lejos
                if w < 120:
                    bebop.fly_direct(0, 20, 0, 0, 1)
                    bebop.ask_for_state_update()
                    bebop.smart_sleep(1)
                elif w > 140:
                    bebop.fly_direct(0, -20, 0, 0, 1)
                    bebop.ask_for_state_update()
                    bebop.smart_sleep(1)
            else:
                bebop.fly_direct(0, 0, 10, 0, 1)
                bebop.ask_for_state_update()
                bebop.smart_sleep(1)
    except:
        print("Leon se equivocó")
