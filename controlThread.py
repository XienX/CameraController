# -*- coding: utf-8 -*-
# @Time : 2021/3/13 15:43
# @Author : XieXin
# @Email : 1324548879@qq.com
# @File : controlThread.py
# @notice ：

import json
import socket
import time

from PyQt5 import QtCore
from PyQt5.QtCore import *


class ControlThread(QtCore.QThread):
    #  通过类成员对象定义信号对象
    log_signal = pyqtSignal(str)
    connect_button_signal = pyqtSignal(bool)
    close_button_signal = pyqtSignal(bool)

    def __init__(self, user_name, password, ip, port, camera):
        super().__init__()
        self.user_name = user_name
        self.password = password
        self.ip = ip
        self.port = port

        self.camera = camera

        self.frameLen = 0

        self.connect = socket.socket()  # 创建 socket 对象

        self.isAlive = True

    def run(self):
        try:
            self.connect_button_signal.emit(False)
            self.close_button_signal.emit(True)

            self.connect.connect((self.ip, self.port))

            message = {'code': 100, 'userName': self.user_name, 'password': self.password}  # 登录
            self.connect.send(json.dumps(message).encode())

            jsonMessage = self.connect.recv(1024).decode()
            message = json.loads(jsonMessage)
            print(message)

            if message['code'] == 300:
                self.log_signal.emit('登录成功，推流中')
                self.send_frame_len()

                while self.isAlive:
                    self.send_frame()
                    time.sleep(0.1)

            elif message['code'] == 301:
                self.log_signal.emit('用户名或密码错误')
            else:
                self.log_signal.emit(f'非预期的code {message["code"]}')

        except BaseException as e:
            self.log_signal.emit(f'连接错误: {e}')

        self.connect_button_signal.emit(True)
        self.close_button_signal.emit(False)

    def send_frame_len(self):  # 发送帧数据大小
        flag, frame = self.camera.cap.read()
        lenMessage = {'code': 500, 'data': len(frame.tobytes())}  # 帧数据大小
        self.connect.send(json.dumps(lenMessage).encode())

    def send_frame(self):  # 发送一帧数据
        flag, frame = self.camera.cap.read()
        # print(frame)
        frameData = frame.tobytes()
        # print(len(frameData))  # 921600
        self.connect.sendall(frameData)

    def close(self):  # 结束
        self.isAlive = False
        # self.connect.shutdown(2)
        print('shutdown')
        self.connect.close()
