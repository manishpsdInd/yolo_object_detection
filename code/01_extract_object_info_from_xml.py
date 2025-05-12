from glob import glob
import pandas as pd
from xml.etree import ElementTree as et
from config import region
import os
from glob import glob
from ultralytics import YOLO as yolo

import cv2
import pandas as pd
import numpy as np
from functools import reduce
from xml.etree import ElementTree as et
from config import region
from shutil import move
# Testing for multiple images
import random
from IPython.display import Image, display


src_path = region + '/data/data_images'
jpg_image_list = glob(src_path + '/*.jpg')

random_items = random.sample(jpg_image_list, 10)

for image_file in random_items:
    image = cv2.imread(image_file)
    output_filename = os.path.basename(image_file)

    row, col, d = image.shape
    max_rc = max(row, col)

    input_image = np.zeros((max_rc, max_rc, 3), dtype=np.uint8)
    input_image[0:row, 0:col] = image

    INPUT_WIDTH_YOLO = 640
    blob = cv2.dnn.blobFromImage(input_image, 1/255, (INPUT_WIDTH_YOLO,INPUT_WIDTH_YOLO), swapRB=True, crop=False)

    model = yolo('yolov8n.pt')
    results = model(image)

#########

    for result in results:
        boxes = result.boxes.cpu().numpy()
        names = result.names

        for box in boxes:
            xyxy = box.xyxy.astype(int)[0]
            confidence = box.conf[0]
            class_id = box.cls[0]
            class_name = names[class_id]

            cv2.rectangle(image, (xyxy[0], xyxy[1]), (xyxy[2], xyxy[3]), (0, 255, 0), 2)

            label = f'{class_name}: {confidence:.2f}'
            cv2.putText(image, label, (xyxy[0], xyxy[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    #output_file = 'detected_image_000035.jpg'
    #cv2.imwrite(output_file, image)
    display(Image(image))

    #cv2.imwrite(output_file, image)
    #display(Image(filename = imageName))
