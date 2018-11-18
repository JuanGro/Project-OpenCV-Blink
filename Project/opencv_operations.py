path_face_xml = './haarcascade_frontalface_default.xml'
path_eye_xml = './haarcascade_eye.xml'

def is_there_a_face():
    face_cascade = opencv.CascadeClassifier(path_face_xml)
    try:
        img = opencv.imread(r'/Users/juan/anaconda3/lib/python3.7/site-packages/pyparrot/images/visionStream.jpg')
        if (img is not None):
            gray = opencv.cvtColor(img, 0)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            if len(faces) >= 1:
                return True
            else:
                return False
        else:
            print("Error when try to load image")
            return False
    except:
        print("Error when try to load image")
        return False

def is_there_a_blink():
    face_cascade = opencv.CascadeClassifier(path_face_xml)
    eye_cascade = opencv.CascadeClassifier(path_eye_xml)
    try:
        img = opencv.imread(r'/Users/juan/anaconda3/lib/python3.7/site-packages/pyparrot/images/visionStream.jpg')
        if (img is not None):
            gray = opencv.cvtColor(img, 0)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            # For each face
            for (x, y, w, h) in faces:
                eyes_number = 0
                roi_gray = gray[y:y+h, x:x+w]
                eyes = eye_cascade.detectMultiScale(roi_gray)
                for (ex, ey, ew, eh) in eyes:
                    # This is an adjustment to get only the eyes, not nose
                    if (ey + ey + eh) / 2 < (y + y + h) / 6:
                        eyes_number += 1
                if eyes_number == 1:
                    print("Blink")
                    return True
                elif eyes_number == 2:
                    print("Two eyes")
                    return False
                else:
                    print("Many eyes")
                    return False
            return False
        else:
            print("Error when try to load image")
            return False
    except:
        print("Error when try to load image")
        return False
