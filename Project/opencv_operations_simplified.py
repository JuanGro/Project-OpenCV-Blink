import cv2 as opencv

path_face_xml = './Resources/haarcascade_frontalface_default.xml'
path_eye_xml = './Resources/haarcascade_eye.xml'

def is_there_a_blink():
    face_cascade = opencv.CascadeClassifier(path_face_xml)
    eye_cascade = opencv.CascadeClassifier(path_eye_xml)
    try:
        img = opencv.imread(r'/Users/juan/anaconda3/lib/python3.7/site-packages/pyparrot/images/visionStream.jpg')
        if (img is not None):
            gray = opencv.cvtColor(img, 0)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            if len(faces) >= 1:
                # For each face
                for (x, y, w, h) in faces:
                    eyes_number = 0
                    roi_gray = gray[y : y + h, x : x + w]
                    eyes = eye_cascade.detectMultiScale(roi_gray)
                    for (ex, ey, ew, eh) in eyes:
                        # This is an adjustment to get only the eyes, not nose
                        if (ey + ey + eh) / 2 < (y + y + h) / 4:
                            eyes_number += 1
                    if eyes_number == 0:
                        print("No eyes")
                        return 'Face found'
                    elif eyes_number == 1:
                        print("Blink")
                        return 'Blink'
                    elif eyes_number == 2:
                        print("Two eyes")
                        return 'Face found'
                    else:
                        print("Many eyes")
                        return 'Face found'
            else:
                return 'No face'
        else:
            return 'No face'
    except:
        return 'No face'
