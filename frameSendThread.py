# -*- coding: utf-8 -*-
# @Time : 2021/3/22 16:06
# @Author : XieXin
# @Email : 1324548879@qq.com
# @File : frameSendThread.py
# @notice ：FrameSendThread类--帧发送线程

import io
import json
import socket
import time
from threading import Thread

import cv2
from PIL import Image


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
        # # flag, frame = self.camera.cap.read()
        # frame = self.camera.get_frame()
        # # print(frame)
        # frameData = frame.tobytes()
        # # print(len(frameData))  # 921600
        # self.connect.sendall(frameData)

        frame = self.camera.get_frame()
        if frame is not None:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # cv的BGR 转 PIL的RGB
            im = Image.fromarray(frame)
            imgByteArr = io.BytesIO()
            im.save(imgByteArr, format='JPEG')
            frameData = imgByteArr.getvalue()
            print(len(frameData))  # 29xxx - 34xxx

            # 先发送frame大小
            message = {'code': 500, 'frameLen': len(frameData)}
            self.connect.send(json.dumps(message).encode())

            # 发送实际frame
            self.connect.sendall(frameData)

    def close(self):  # 结束
        self.connect.close()
        self.isAlive = False

        print('FrameSendThread shutdown')
