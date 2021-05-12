# -*- coding: utf-8 -*-
# @Time : 2021/3/13 15:43
# @Author : XieXin
# @Email : 1324548879@qq.com
# @File : controlThread.py
# @notice ：ControlThread类--连接控制线程

import json
import socket

import cv2
from PyQt5 import QtCore
from PyQt5.QtCore import *

from frameSendThread import FrameSendThread


class ControlThread(QtCore.QThread):
    #  通过类成员对象定义信号对象
    log_signal = pyqtSignal(str)
    enabled_signal = pyqtSignal(bool)
    move_signal = pyqtSignal(str)

    def __init__(self, user_name, password, ip, port, camera):
        super().__init__()
        self.user_name = user_name
        self.password = password
        self.ip = ip
        self.port = port

        self.camera = camera
        # self.frameLen = 0

        self.connect = socket.socket()  # 创建 socket 对象
        # self.isAlive = True

        self.frameSendThread = None

    def run(self):
        try:
            if self.camera.cap is None:
                return

            self.enabled_signal.emit(False)

            self.connect.connect((self.ip, self.port))

            message = {'code': 100, 'userName': self.user_name, 'password': self.password}  # 登录
            self.connect.send(json.dumps(message).encode())

            jsonMessage = self.connect.recv(1024).decode()
            message = json.loads(jsonMessage)
            print(message)

            if message['code'] == 300:
                self.log_signal.emit('登录成功')

                # self.send_preview_frame()

                while 1:
                    operation = json.loads(self.connect.recv(1024).decode())
                    print(operation)

                    if operation['code'] == 320:  # 请求视频流
                        self.frameSendThread = FrameSendThread(self.camera, self.ip, operation['port'])
                        self.frameSendThread.setDaemon(True)
                        self.frameSendThread.start()
                    elif operation['code'] == 510:  # 清晰度设置
                        self.frameSendThread.definition = operation['definition']
                        self.connect.send(json.dumps({'code': 530}).encode())  # 成功

                    elif operation['code'] == 511:  # 帧数设置
                        pass
                    elif operation['code'] == 520:  # 遥控指令
                        self.move_signal.emit(operation['move'])

                    # 忽略 340 心跳包

            elif message['code'] == 301:
                self.log_signal.emit('用户名或密码错误')
            else:
                self.log_signal.emit(f'非预期的code {message["code"]}')

        except BaseException:
            self.log_signal.emit(f'连接已断开')

        self.enabled_signal.emit(True)

    def send_preview_frame(self):  # 发送预览图
        frame = self.camera.get_frame()
        if frame is not None:
            frame = cv2.resize(frame, (160, 120))
            frameData = frame.tobytes()
            # print(len(frameData))
            self.connect.sendall(frameData)

    # def send_frame_len(self):  # 发送帧数据大小
    #     # flag, frame = self.camera.cap.read()
    #     frame = self.camera.get_frame()
    #     lenMessage = {'code': 500, 'data': len(frame.tobytes())}  # 帧数据大小
    #     self.connect.send(json.dumps(lenMessage).encode())
    #

    def close(self):  # 结束
        # self.isAlive = False
        # self.connect.shutdown(2)

        if self.frameSendThread is not None and self.frameSendThread.is_alive():
            self.frameSendThread.close()

        self.connect.close()
        print('shutdown')
