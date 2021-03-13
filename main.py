# -*- coding: utf-8 -*-
# @Time : 2021/3/6 11:31
# @Author : XieXin
# @Email : 1324548879@qq.com
# @File : main.py
# @notice ：程序入口，ControllerWindow类


import sys

import cv2

from PyQt5 import QtGui
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication

from camera import Camera
from controllerWindow import Ui_MainWindow

from controlThread import ControlThread


class ControllerWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.camera = Camera(0)  # 初始化摄像头

        self.timer_camera = QTimer()  # 初始化定时器
        self.timer_camera.start(40)

        self.controlThread = None

        self.slot_init()

    def slot_init(self):
        self.connectButton.clicked.connect(self.connect_server)
        self.timer_camera.timeout.connect(self.show_camera)

    def connect_server(self):  # 连接服务器
        self.controlThread = ControlThread(self.userNameInput.text(), self.passwordInput.text(),
                                           self.ipInput.text(), int(self.portInput.text()), self.camera)
        self.controlThread.log_signal.connect(self.print_log)
        self.controlThread.connect_button_signal.connect(self.control_connect_button)
        self.controlThread.close_button_signal.connect(self.control_close_button)
        self.controlThread.start()

    def print_log(self, log_str):  # UI上打印日志
        self.log.append(log_str)

    def control_connect_button(self, b):  # 控制连接按钮
        if (self.connectButton.isEnabled() and not b) or (not self.connectButton.isEnabled() and b):
            self.connectButton.setEnabled(b)

    def control_close_button(self, b):  # 控制断开连接按钮
        if (self.closeButton.isEnabled() and not b) or (not self.closeButton.isEnabled() and b):
            self.closeButton.setEnabled(b)

    def show_camera(self):  # 显示一帧
        flag, frame = self.camera.cap.read()
        # print(type(frame))  # numpy.ndarray
        # # print(sys.getsizeof(frame))  # 921736
        # print(frame.shape)  # (480, 640, 3)
        show = cv2.resize(frame, (400, 300))
        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
        showImage = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
        self.cameraLabel.setPixmap(QPixmap.fromImage(showImage))

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:  # 关闭程序
        try:
            super().closeEvent(a0)
            # if self.camera:
            #     self.camera.close()
            if self.controlThread and self.controlThread.isRunning():
                self.controlThread.close()
        except BaseException as e:
            print(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = ControllerWindow()
    ui.show()
    sys.exit(app.exec_())
