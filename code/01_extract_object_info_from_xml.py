from glob import glob
import pandas as pd
from xml.etree import ElementTree as et


xml_list = glob('/Users/manis/workspace/py/data/data_images/*.xml')
len(xml_list)

parser1=[]
for img_details in xml_list:
    tree1 = et.parse(img_details)
    root1 = tree1.getroot()
    objs1 = root1.findall('object')
    image_name1 = root1.find('filename').text
    width1 = root1.find('size').find('width').text
    height1 = root1.find('size').find('height').text
    for obj1 in objs1:
        name1 = obj1.find('name').text
        bndbox1 = obj1.find('bndbox')
        xmin1 = bndbox1.find('xmin').text
        xmax1 = bndbox1.find('xmax').text
        ymin1 = bndbox1.find('ymin').text
        ymax1 = bndbox1.find('ymax').text
        parser1.append([image_name1, width1, height1, name1, xmin1, ymin1, xmax1, ymax1])
df = pd.DataFrame(parser1, columns=['filename', 'width', 'height', 'name', 'xmin', 'ymin', 'xmax', 'ymax'])

df.shape
df.head(10)
