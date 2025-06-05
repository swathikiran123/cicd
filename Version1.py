from abc import ABC,abstractmethod
import cv2
from ultralytics import YOLO

class image_det(ABC):

    def __init__(self,*,image_path,objdet_path):
        pass

    @abstractmethod
    def load_image(self):
        pass
    
    @abstractmethod
    def loading_objdet_model(self):
        pass
   
    @abstractmethod 
    def passing_image_objdet_model(self,cls):# HINT: return image,coordinates
        pass

    @abstractmethod
    def annotate_image(self):
        pass
        
    @abstractmethod
    def display_img(self,image):
        pass