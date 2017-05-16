import unittest
import sys, os
import numpy as np
import cv2
sys.path.append(os.path.abspath(sys.path[0]) + '/../')
from pi_gesture.cascade import Cascade

class CascadeTest(unittest.TestCase):
    
        def setUp(self):
            cascade1 = Cascade('fake_path')       
            cascade1.features = ()
            cascade1.features_detected = True
            cascade2 = Cascade('fake_path')       
            cascade2.features = np.array([[50,50,20,10]])
            cascade2.features_detected = True
            cascade3 = Cascade('fake_path')       
            self.cascade1 = cascade1
            self.cascade2 = cascade2
            self.cascade3 = cascade3
            self.draw_img = np.zeros((100,100,3), np.uint8)
            zoom_img = np.zeros((100,100,3), np.uint8)
            center = np.zeros((30,30,3), np.uint8)
            center.fill(255)
            zoom_img[40:70,45:75,:] = center
            self.zoom_img = zoom_img

        def test_draw_rectangles(self):
            cascade1 = self.cascade1
            draw_img = self.draw_img
            cascade2 = self.cascade2
            new_img = cascade1.draw_rectangles(draw_img)
            self.assertEquals(new_img[50,50,0], 0)
            new_img = cascade2.draw_rectangles(draw_img)
            self.assertEquals(new_img[50,50,0], 255)

        def test_draw_rectangles_exception_no_features(self):
            with self.assertRaises(Exception) as cm:
                self.cascade3.draw_rectangles(self.draw_img)
            msg = cm.exception.message
            self.assertEquals(msg, 'Detect features before drawing')

        def test_zoom_on_feature(self):
            cascade1 = self.cascade1
            cascade2 = self.cascade2
            zoom_img = self.zoom_img
            new_img, success = cascade1.zoom_on_feature(zoom_img)
            self.assertEquals(success, False)
            self.assertEquals(len(new_img[:,0,0]),100)
            self.assertEquals(len(new_img[0,:,0]),100)

            new_img, success = cascade2.zoom_on_feature(zoom_img)
            self.assertEquals(success, True)
            self.assertEquals(len(new_img[:,0,0]),30)
            self.assertEquals(len(new_img[0,:,0]),30)
            self.assertEquals(new_img[0,0,0], 255)
            self.assertEquals(new_img[0,0,1], 255)
            self.assertEquals(new_img[0,0,2], 255)
            self.assertEquals(new_img[29,29,0], 255)
            self.assertEquals(new_img[29,29,1], 255)
            self.assertEquals(new_img[29,29,2], 255)

        def test_zoom_on_feature_exception_no_features(self):
            with self.assertRaises(Exception) as cm: 
                self.cascade3.zoom_on_feature(self.draw_img)
            msg = cm.exception.message
            self.assertEquals(msg, 'Detect features before zooming')
