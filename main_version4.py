from Version4 import *


import argparse

if __name__ =="__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('--image_path',type=str,required=True)
    parser.add_argument('--model_path',type=str,required=False,default="yolov8n.pt")

    args = parser.parse_args()
    
    image_path = args.image_path
    model_path = args.model_path

    obj1 = image_det(image_path=image_path,objdet_path=model_path)
    obj1.results(cls=0)