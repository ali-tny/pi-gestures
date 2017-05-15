import sys, os
import cv2
import numpy as np
sys.path.append(os.path.abspath(sys.path[0]) + '/../')
from pi_gesture.cascade import Cascade

hand_cascade = Cascade('haarcascades/haarcascade_hand.xml')
close_palm_cascade = Cascade('haarcascades/haarcascade_closed_frontal_palm.xml')
fist_cascade = Cascade('haarcascades/haarcascade_fist.xml')
palm_cascade = Cascade('haarcascades/haarcascade_palm.xml')
cascades = [hand_cascade, close_palm_cascade, fist_cascade, palm_cascade]
cap = cv2.VideoCapture(0)
while (cap.isOpened()):
    ret,img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    blue = cv2.GaussianBlur(gray,(5,5),0)
    for cascade in cascades:
        img = cascade.detect(gray,img)
    cv2.imshow('img', img)
    k = cv2.waitKey(10)
    if k == 27:
        break
