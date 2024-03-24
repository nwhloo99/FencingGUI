from ultralytics import YOLO
import os
import cv2
from matplotlib import pyplot as plt
import pandas as pd

def scoreboardDetection(folder):
    model = YOLO('./train17/weights/last.pt')
    mycwd = os.getcwd()
    os.chdir(folder)

    source = "./masked.mp4"
    results = model(source, stream=True)

    boxes = []

    for r in results:
        try:
            boxes.append(r.boxes.xyxy[0].tolist())
        except:
            boxes.append(boxes[-1])
            
    boxes_df = pd.DataFrame(boxes)
    boxes_df = boxes_df.astype('int')
    boxes_df.to_csv('boxes.csv', index=False, header=False)
    
    os.chdir(mycwd)