from PIL import Image
import os
import numpy as np
import matplotlib.pyplot as plt

path = r"imgs/原始图"
save_path = r"imgs/去污点图"

if not os.path.exists(save_path):
    os.makedirs(save_path)

imgs = os.listdir(path)
for i in imgs:
    diff = []
    for j in imgs:
        if i == j:
            continue
        a = plt.imread(os.path.join(path, i)).astype(np.double)
        b = plt.imread(os.path.join(path, j)).astype(np.double)
        dif = a - b
        dif[dif < 15] = 0
        diff.append(dif)
    diff = np.stack(diff, 2)
    new_img = np.max(diff, 2).astype(np.uint8)
    im = Image.fromarray(new_img)
    im.save(os.path.join(save_path, i[:-4]+"_kolf.tif"))
