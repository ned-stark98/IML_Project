''''
 ==> image folder should save the faces of diffrent user in unique folder
 ==>
'''

import cv2
import numpy as np
import pil
from pil import Image
import os
from os import walk

# Path for face image database
current_directory = os.getcwd()
images_directory = os.path.join(current_directory, 'images')
# print(images_directory)
recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier('data/haarcascades/haarcascade_frontalface_default.xml');

#  function to get the dataset and label data

def getImagesAndLabels(path):
    imagePaths = [folder for folder in os.listdir(path)]
    print(imagePaths)

    for user_images in imagePaths:
        #print(user_images)
        user_image = os.path.join(path, user_images)
        for image in os.walk(user_image):
            print(image[2])
            PIL_img = Image.open(image).convert('L')  # convert it to grayscale


    #
    # faceSamples = []
    # ids = []
    #
    # for imagePath in imagePaths:
    #     PIL_img = Image.open(imagePath).convert('L') # convert it to grayscale
    #     img_numpy = np.array(PIL_img,'uint8')
    #     id = int(os.path.split(imagePath)[-1].split(".")[1])
    #     faces = detector.detectMultiScale(img_numpy)
    #     for (x,y,w,h) in faces:
    #         faceSamples.append(img_numpy[y:y+h,x:x+w])
    #         ids.append(id)

    #return faceSamples,ids

# print ("\n [INFO] Training faces. It will take a few seconds. Wait ...")
# faces,ids = getImagesAndLabels(path)
# recognizer.train(faces, np.array(ids))
#
# # Save the model into trainer/trainer.yml
# recognizer.write('trainer/trainer.yml') # recognizer.save() worked on Mac, but not on Pi
#
# # Print the numer of faces trained and end program
# print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))


getImagesAndLabels(images_directory)