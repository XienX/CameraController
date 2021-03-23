# -*- coding: utf-8 -*-
# @Time : 2021/3/22 16:06
# @Author : XieXin
# @Email : 1324548879@qq.com
# @File : frameSendThread.py
# @notice ：FrameSendThread类--帧发送线程

import socket
import time
from threading import Thread


class FrameSendThread(Thread):  # 视频帧的发送线程
    def __init__(self, camera, ip, port):
        super().__init__()

        self.camera = camera

        self.ip = ip
        self.port = port

        self.isAlive = True

        self.connect = socket.socket()

    def run(self):
        try:
            self.connect.connect((self.ip, self.port))

            while self.isAlive:
                self.send_frame()
                time.sleep(0.1)

        except BaseException as e:
            print(e)

        print('FrameSendThread end')

    def send_frame(self):  # 发送一帧数据
        # flag, frame = self.camera.cap.read()
        frame = self.camera.get_frame()
        # print(frame)
        frameData = frame.tobytes()
        # print(len(frameData))  # 921600
        self.connect.sendall(frameData)

    def close(self):  # 结束
        self.connect.close()
        self.isAlive = False

        print('FrameSendThread shutdown')
