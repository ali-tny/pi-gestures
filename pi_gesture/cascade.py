import cv2
import numpy as np

class Cascade(object):
    
    def __init__(self, cascade_path, zoom_coeff_x=1.5, zoom_coeff_y=3):
        self.path = cascade_path
        self.classifier = cv2.CascadeClassifier(cascade_path)
        self.zoom_coeff_x = zoom_coeff_x
        self.zoom_coeff_y = zoom_coeff_y
        self.features = None
        self.features_detected = False

    def detect(self, detect_img):
        """Detect features in an image and store them in self.features"""
        features = self.classifier.detectMultiScale(detect_img,1.3,5)
        self.features = features
        self.features_detected = True

    def draw_rectangles(self, draw_img):
        """Draw rectangles around features found in an image"""
        if not self.features_detected:
            raise Exception('Detect features before drawing')
        for (x,y,w,h) in self.features:
            cv2.rectangle(draw_img,(x,y),(x+w,y+h),(255,0,0),2)
        return draw_img

    def zoom_on_feature(self, draw_img):
        """Zoom into an area around the first feature found. Area will be larger
        than the feature by a factor of self.zoom_coeff"""
        if not self.features_detected:
            raise Exception('Detect features before zooming')
        inflate_x = self.zoom_coeff_x
        inflate_y = self.zoom_coeff_y
        for (x,y,w,h) in self.features:
            size_coeff_x = 0.5*(inflate_x-1)
            size_coeff_y = 0.5*(inflate_y-1)
            x_l = max(int(x-size_coeff_x*w),0)
            x_r = min(int(x+(size_coeff_x+1)*w), len(draw_img[:,0]))
            y_b = max(int(y-size_coeff_y*h),0)
            y_t = min(int(y+(size_coeff_y+1)*h), len(draw_img[0,:]))
            draw_img = draw_img[y_b:y_t,x_l:x_r,:]
            return draw_img, True
        return draw_img, False
