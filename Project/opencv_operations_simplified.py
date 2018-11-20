import cv2 as opencv

path_face_xml = './Resources/haarcascade_frontalface_default.xml'
path_eye_xml = './Resources/haarcascade_eye.xml'

def is_there_a_blink():
    face_cascade = opencv.CascadeClassifier(path_face_xml)
    eye_cascade = opencv.CascadeClassifier(path_eye_xml)
    try:
        i = 1
        face_found = 0
        while (i < 10):
            i += 1
            img = opencv.imread(r'/Users/juan/anaconda3/lib/python3.7/site-packages/pyparrot/images/visionStream.jpg')
            if (img is not None):
                gray = opencv.cvtColor(img, 0)
                faces = face_cascade.detectMultiScale(gray, 1.3, 5)
                if len(faces) >= 1:
                    face_found += 1
                    break
                    # For each face
                    # for (x, y, w, h) in faces:
                    #     eyes_number = 0
                    #     roi_gray = gray[y : y + h, x : x + w]
                    #     eyes = eye_cascade.detectMultiScale(roi_gray)
                    #     for (ex, ey, ew, eh) in eyes:
                    #         # This is an adjustment to get only the eyes, not nose
                    #         # if (ey + ey + eh) / 2 < (y + y + h) / 4:
                    #         eyes_number += 1
                    #     if eyes_number == 0:
                    #         print("No eyes")
                    #         return 'Face found'
                    #     elif eyes_number == 1:
                    #         print("Blink")
                    #         return 'Blink'
                    #     elif eyes_number == 2:
                    #         print("Two eyes")
                    #         return 'Face found'
                    #     else:
                    #         print("Many eyes")
                    #         return 'Face found'
        if face_found > 0:
            return 'Face found'
        else:
            return 'No face'
    except:
        return 'No face'

def follow(bebop):
    face_cascade = opencv.CascadeClassifier(path_face_xml)
    try:
        img = opencv.imread(r'/Users/juan/anaconda3/lib/python3.7/site-packages/pyparrot/images/visionStream.jpg')
        if (img is not None):
            gray = opencv.cvtColor(img, 0)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                w_min_size = 60
                w_max_size = 70
                print("W: ", w)
                #Estoy no centrado Izq der
                if (x + (w / 2)) > (856 / 2 + 40):
                    bebop.fly_direct(20, 0, 0, 0, 1)
                    bebop.ask_for_state_update()
                    bebop.smart_sleep(1)
                    print("der")
                elif (x + (w / 2)) < (856 / 2 - 40):
                    bebop.fly_direct(-20, 0, 0, 0, 1)
                    bebop.ask_for_state_update()
                    bebop.smart_sleep(1)
                    print("izq")
                #Estoy lejos
                if w < w_min_size:
                    bebop.fly_direct(0, 30, 0, 0, 1)
                    bebop.ask_for_state_update()
                    bebop.smart_sleep(1)
                    print("acercarse")
                elif w > w_max_size:
                    bebop.fly_direct(0, -30, 0, 0, 1)
                    bebop.ask_for_state_update()
                    bebop.smart_sleep(1)
                    print("alejarse")
                else:
                    bebop.smart_sleep(1)
                    print("Quieto")
    except:
        print("Leon se equivocó")
