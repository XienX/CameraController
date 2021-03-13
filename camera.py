# -*- coding: utf-8 -*-
# @Time : 2021/3/6 22:01
# @Author : XieXin
# @Email : 1324548879@qq.com
# @File : camera.py
# @notice ：Camera类

import cv2


class Camera:
    def __init__(self, camera_number):
        self.cap = cv2.VideoCapture(camera_number, cv2.CAP_DSHOW)

    def get(self):
        pass

    def move(self):
        pass

    def close(self):
        pass
        # self.cap.release()
        # print('release')


if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    while 1:
        # get a frame
        ret, frame = cap.read()
        # show a frame
        cv2.imshow("capture", frame)
        if cv2.waitKey(40) & 0xFF == ord('q'):  # 25帧
            break
    cap.release()
    cv2.destroyAllWindows()
