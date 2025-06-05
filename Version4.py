from Version3 import *


class image_det(ABC):

    def __init__(self,*,image_path,objdet_path):
        self.image_path = image_path
        self.objdet_path = objdet_path

    def loading_img_and_loading_model(self):
        image = cv2.imread(self.image_path)
        model = YOLO(self.objdet_path)
        return image,model # tuple of image and model
     
    def results(self,cls):# HINT: return image,coordinates
        img = self.loading_img_and_loading_model()[0]
        model = self.loading_img_and_loading_model()[1]
        results = model.predict(img,classes=cls)
        coordinates = []
        if len(results)>=1:
            x1 = int(results[0].boxes.xyxy.numpy()[0][0])
            y1 = int(results[0].boxes.xyxy.numpy()[0][1])
            x2 = int(results[0].boxes.xyxy.numpy()[0][2])
            y2 = int(results[0].boxes.xyxy.numpy()[0][3])
            coordinates.append([x1,y1,x2,y2])
        x1,y1,x2,y2 = coordinates[0][0],coordinates[0][1],coordinates[0][2],coordinates[0][3]
        cv2.rectangle(img,(x1,y1),(x2,y2),(0,0,255),3)
        self.display_img(img)
        
    def display_img(self,image):
        cv2.imshow("window",image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()