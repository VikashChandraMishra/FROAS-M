import pyautogui
import os
import cv2 as cv
import numpy as np
import time
from .models import Student, Class

def train():

    DIR = r'E:\Python\django Projects\Minor Project\FROAS-2\FROAS\tau\samples'
    students = os.listdir(DIR)
    haar_cascade = cv.CascadeClassifier(r'E:\Python\django Projects\Minor Project\FROAS-2\FROAS\tau\haar_face.xml')

    features = []
    labels = []
    
    for student in students:
        path = os.path.join(DIR, student)
        label = students.index(student)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, 1.1, minNeighbors=4)

            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)




    features = np.array(features, dtype='object')
    labels = np.array(labels)


    face_recognizer = cv.face.LBPHFaceRecognizer_create()

    # Train the Recognizer on the features list and the labels list
    face_recognizer.train(features,labels)


    face_recognizer.save('face_trained.yml')
    np.save('features.npy', features)
    np.save('labels.npy', labels)

    print('Training Done  ..........................................')

    
    
def record_screen(id):
    
    timeout = time.time() + 30*1 
    
    output = r'E:\Python\django Projects\Minor Project\FROAS-2\FROAS\videos\\' + str(id) + ".mp4"
    img = pyautogui.screenshot()
    img = cv.cvtColor(np.array(img), cv.COLOR_RGB2BGR)
    height, width, type = img.shape

    fourcc = cv.VideoWriter_fourcc(*'mp4v')
    out = cv.VideoWriter(output, fourcc, 20.0, (width, height))

    while(time.time() < timeout):
        try:

            img = pyautogui.screenshot()
            image = cv.cvtColor(np.array(img), cv.COLOR_RGB2BGR)
            out.write(image)
            StopIteration(0.5)

        except KeyboardInterrupt:
            break

    out.release()
    
    cv.destroyAllWindows()
    
    
def record_attendance(id):
    timeout = time.time() + 16*1 

    capture = cv.VideoCapture(r'E:\Python\django Projects\Minor Project\FROAS-2\FROAS\videos\\' + str(id) + '.mp4')

    face_recognizer = cv.face.LBPHFaceRecognizer_create()
    face_recognizer.read(r'E:\Python\django Projects\Minor Project\FROAS-2\FROAS\face_trained.yml')
    haar_cascade = cv.CascadeClassifier(r'E:\Python\django Projects\Minor Project\FROAS-2\FROAS\tau\haar_face.xml')

    labels = set({})
    attendance = ""
    students = []
    for student in Student.objects.values('id'):
        students.append(student)
        
        
    while (time.time() < timeout):
        isTrue, img = capture.read()

        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        faces_rect = haar_cascade.detectMultiScale(gray, 1.1, minNeighbors=4)

        for (x,y,w,h) in faces_rect:
            faces_roi = gray[y:y+h, x:x+w]
            label, confidence = face_recognizer.predict(faces_roi)
            
            if confidence <= 100:
                labels.add(label)

            print(f'Label = {students[label]} with a confidence of {confidence}')

    capture.release() 
    cv.destroyAllWindows()
    cv.waitKey(0)
    
    for label in labels:
        student = students[label]
        attendance = attendance + ',' + str(student['id'])
        
    try:
        c = Class.objects.get(id=id)
        c.attendance = attendance
        c.save()
    except:
        pass

    print(attendance)