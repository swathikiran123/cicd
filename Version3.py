from abc import ABC,abstractmethod
import cv2
from ultralytics import YOLO

class image_det(ABC):

    def __init__(self,*,image_path,objdet_path):
        pass

    @abstractmethod
    def loading_img_and_loading_model(self):
        pass
    
    @abstractmethod 
    def results(self,cls):
        # it should processs the image to the model
        # it should collect the coordinates
        pass
        
    @abstractmethod
    def display_img(self,image):
        pass