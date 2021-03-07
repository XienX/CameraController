# -*- coding: utf-8 -*-
# @Time : 2021/3/6 11:31
# @Author : XieXin
# @Email : 1324548879@qq.com
# @File : main.py
# @notice ：程序入口，ControllerWindow类

import sys

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow, QApplication

from camera import Camera
from window import Ui_MainWindow


class ControllerWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.timer_camera = QTimer()  # 初始化定时器
        self.camera = Camera(0)  # 初始化摄像头


    def show_camera(self):  # 显示
        flag, image = self.camera.cap.read()
        # show = cv2.resize(self.image, (480, 320))
        # show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
        # showImage = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
        # self.cameraLabel.setPixmap(QPixmap.fromImage(showImage))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = ControllerWindow()
    ui.show()
    sys.exit(app.exec_())