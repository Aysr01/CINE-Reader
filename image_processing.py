import os
import cv2
from PIL import Image
import numpy as np 


class Processor:
    def __init__(self):
        pass

    def load(self, path):
        image = Image.open(path)
        array_image = np.array(image)
        image.close()
        return array_image

    def correct(self, boxes):
        cls = boxes.cls.numpy()
        num4 = (cls == 4).sum()
        if num4 > 0:
            cls = list(cls)
            try:
               output = {4.0 : cls.index(4.0), 3.0: cls.index(3.0)}
            except:
               output = {4.0 : cls.index(4.0)}
            return output

        n = len(cls)
        output = {}
        for i in range(n):
            try:
               output[cls[i]]
            except:
               output[cls[i]] = i
        return output
    
    def xy_to_image(self, xyxy, image):
        x1, y1, x2, y2 = xyxy.cpu().numpy().astype("int")
        out = image[y1:y2,x1:x2]
        return out

    def effect(self, image):
        image = cv2.bilateralFilter(image, 7, 4, 4)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return image
    
    def split_image(self, image):
        n = image.shape[0]
        return image[:n//2], image[n//2 +1 :]
    
    def rotate(self, image, degree):
        degree %= 360
        if degree == 90:
           image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
        elif degree == 180 :
           image = cv2.rotate(image, cv2.ROTATE_180)
        elif degree == 270 :
           image = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
        return image