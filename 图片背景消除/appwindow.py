from PyQt6 import uic, QtWidgets
from PyQt6.QtWidgets import QApplication, QMessageBox
import sys
import cv2
import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)

        self.pushButton.clicked.connect(self.img_process)  # 绑定按钮的点击信号和对应的槽函数

    def img_process(self):  # 槽函数
        path = self.lineEdit.text()
        save_path = self.lineEdit_2.text()
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        remove_stains_path = os.path.join(save_path, "remove_stains")
        obj_save_path = os.path.join(save_path, "obj")
        water_save_path = os.path.join(save_path, "water")
        if not os.path.exists(remove_stains_path):
            os.makedirs(remove_stains_path)
        if not os.path.exists(obj_save_path):
            os.makedirs(obj_save_path)
        if not os.path.exists(water_save_path):
            os.makedirs(water_save_path)

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
            im.save(os.path.join(remove_stains_path, i[:-4] + "_kolf.tif"))

        imgs = os.listdir(remove_stains_path)
        for i in imgs:
            img = plt.imread(os.path.join(remove_stains_path, i)).astype(np.double)
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
        QMessageBox.about(self, "提示", "图片处理完成")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = MyApp()
    myapp.show()
    sys.exit(app.exec())
