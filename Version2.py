from Version1 import *

# create a child class on the abstract class
class project(image_det):
    
    def __init__(self,*,image_path,objdet_path):
        self.image_path = image_path
        self.objdet_path = objdet_path

    def load_image(self):
        image = cv2.imread(self.image_path)
        return image
    
    def loading_objdet_model(self):
        model = YOLO(self.objdet_path)
        return model
   
    def passing_image_objdet_model(self,cls=0):# HINT: return image,coordinates
        results = self.loading_objdet_model().predict(self.load_image(),classes=cls)
        coordinates = []
        if len(results)>=1:
            x1 = int(results[0].boxes.xyxy.numpy()[0][0])
            y1 = int(results[0].boxes.xyxy.numpy()[0][1])
            x2 = int(results[0].boxes.xyxy.numpy()[0][2])
            y2 = int(results[0].boxes.xyxy.numpy()[0][3])
            coordinates.append([x1,y1,x2,y2])
        return coordinates

    def annotate_image(self):
        coords = self.passing_image_objdet_model()
        img = self.load_image()
        x1,y1,x2,y2 = coords[0][0],coords[0][1],coords[0][2],coords[0][3]
        cv2.rectangle(img,(x1,y1),(x2,y2),(0,0,255),3)
        self.display_img(image=img)
        
    def display_img(self,image): # what ever the image that you pass its going to display
        cv2.imshow("window",image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()