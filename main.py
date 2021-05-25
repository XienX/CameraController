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

        self.camera = Camera()  # 初始化摄像头
        # self.camera.set_camera(0)

        self.timer_camera = QTimer()  # 初始化定时器
        self.timer_camera.start(40)

        self.controlThread = None

        self.slot_init()

        self.cameraNumInput.setValue(1)
        self.servoInput.addItems(self.camera.servoList)

    def slot_init(self):
        self.connectButton.clicked.connect(self.connect_server)
        self.closeButton.clicked.connect(self.close_connect)
        self.cameraNumInput.valueChanged.connect(self.change_camera)
        self.servoInput.currentIndexChanged[str].connect(self.change_servo)  # 条目发生改变，发射信号，传递条目内容

        self.moveLeftButton.clicked.connect(lambda: self.move_servo('4'))
        self.moveRightButton.clicked.connect(lambda: self.move_servo('6'))
        self.moveUpButton.clicked.connect(lambda: self.move_servo('8'))
        self.moveDownButton.clicked.connect(lambda: self.move_servo('2'))

        self.timer_camera.timeout.connect(self.show_camera)

    def connect_server(self):  # 连接服务器
        self.controlThread = ControlThread(self.userNameInput.text(), self.passwordInput.text(),
                                           self.ipInput.text(), int(self.portInput.text()), self.camera)
        self.controlThread.log_signal.connect(self.print_log)
        self.controlThread.enabled_signal.connect(self.control_enabled)
        self.controlThread.move_signal.connect(self.move_servo)
        self.controlThread.start()

    def print_log(self, log_str):  # UI上打印日志
        self.log.append(log_str)

    def control_enabled(self, b):  # 控制是否禁用
        self.connectButton.setEnabled(b)
        self.closeButton.setEnabled(not b)
        self.userNameInput.setEnabled(b)
        self.passwordInput.setEnabled(b)
        self.ipInput.setEnabled(b)
        self.portInput.setEnabled(b)
        self.cameraNumInput.setEnabled(b)
        self.servoInput.setEnabled(b)

    def change_camera(self):  # 改变摄像头
        self.cameraNumInput.setEnabled(False)
        if not self.camera.set_camera(int(self.cameraNumInput.text())):
            self.log.append('无效的摄像头编号')
        self.cameraNumInput.setEnabled(True)

    def change_servo(self, port):  # 设置舵机端口
        # print('c')
        if not self.camera.set_servo(port):
            self.log.append('云台连接失败')

    def move_servo(self, direction):  # 控制云台
        if not self.camera.move(direction):
            self.log.append('云台错误')

    def show_camera(self):  # 显示一帧
        # flag, frame = self.camera.cap.read()
        # print(type(frame))  # numpy.ndarray
        # # print(sys.getsizeof(frame))  # 921736
        # print(frame.shape)  # (480, 640, 3)

        frame = self.camera.get_frame()
        if frame is not None:
            show = cv2.resize(frame, (480, 360))
            show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
            showImage = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
            self.cameraLabel.setPixmap(QPixmap.fromImage(showImage))

    def close_connect(self):  # 断开连接
        self.controlThread.close()

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
