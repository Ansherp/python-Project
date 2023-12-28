import cv2
from PIL import Image
import os
import numpy as np
import matplotlib.pyplot as plt

path = r"imgs/去污点图"
obj_save_path = r"imgs/obj"
water_save_path = r"imgs/water"

if not os.path.exists(obj_save_path):
    os.makedirs(obj_save_path)
if not os.path.exists(water_save_path):
    os.makedirs(water_save_path)

imgs = os.listdir(path)
for i in imgs:
    img = plt.imread(os.path.join(path, i)).astype(np.double)
    se = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    img_e = cv2.morphologyEx(img, cv2.MORPH_OPEN, se).astype(np.uint8)
    img_e = cv2.medianBlur(img_e, 7)
    ret, bw_e = cv2.threshold(img_e, 0, 1, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    bw_e = cv2.dilate(bw_e, se)
    img_object = img * bw_e
    img_water = img * (1 - bw_e)

    im = Image.fromarray(img_object.astype(np.uint8))
    im.save(os.path.join(obj_save_path, i[:-4] + "_obj.tif"))
    im = Image.fromarray(img_water.astype(np.uint8))
    im.save(os.path.join(water_save_path, i[:-4] + "_water.tif"))
