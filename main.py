# -*- coding: utf-8 -*-
# @Time : 2021/3/6 11:31
# @Author : XieXin
# @Email : 1324548879@qq.com
# @File : main.py
# @notice ：程序入口，ControllerWindow类
import socket
import sys
import json
import time

import cv2
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication

from camera import Camera
from window import Ui_MainWindow


class ControllerWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.camera = Camera(0)  # 初始化摄像头
        self.timer_camera = QTimer()  # 初始化定时器
        self.timer_camera.start(40)

        self.connect = socket.socket()  # 创建 socket 对象

        self.slot_init()

    def slot_init(self):
        self.connectButton.clicked.connect(self.connect_server)
        self.timer_camera.timeout.connect(self.show_camera)

    def connect_server(self):  # 连接服务器
        ip = self.ipInput.text()
        port = int(self.portInput.text())
        self.connect.connect((ip, port))

        message = {'code': 100}  # len = 13
        self.connect.send(json.dumps(message).encode())

        message = self.connect.recv(1024).decode()
        LoginCode = json.loads(message)['code']
        print(LoginCode)

        self.send_frame()

    def send_frame(self):  # 发送一帧数据
        flag, frame = self.camera.cap.read()
        frameData = {'code': 101, 'data': frame.tolist()}
        print(len(frameData))

        frameJsonData = json.dumps(frameData)
        print(len(frameJsonData))

        lenMessage = {'code': 500, 'data': len(frameJsonData)}  # 帧数据大小  ## 48xxxxx 4.6MB+
        self.connect.send(json.dumps(lenMessage).encode())

        print(len(frameJsonData.encode()))

        try:
            print(self.connect.sendall(frameJsonData.encode()))
        except BaseException as e:
            print(e)


    def show_camera(self):  # 显示一帧
        flag, frame = self.camera.cap.read()  # 640*480
        show = cv2.resize(frame, (400, 300))
        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
        showImage = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
        self.cameraLabel.setPixmap(QPixmap.fromImage(showImage))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = ControllerWindow()
    ui.show()

    ui.show_camera()

    sys.exit(app.exec_())
