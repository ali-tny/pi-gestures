import cv2
import numpy as np

class Cascade(object):
    
    def __init__(self, cascade_path):
        self.path = cascade_path
        self.classifier = cv2.CascadeClassifier(cascade_path)

    def detect(self, detect_img, draw_img):
        features = self.classifier.detectMultiScale(detect_img,1.3,5)
        for (x,y,w,h) in features:
            cv2.rectangle(draw_img,(x,y),(x+w,y+h),(255,0,0),2)
        return draw_img
