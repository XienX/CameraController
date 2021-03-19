# -*- coding: utf-8 -*-
# @Time : 2021/3/6 22:01
# @Author : XieXin
# @Email : 1324548879@qq.com
# @File : camera.py
# @notice ：Camera类

import cv2


class Camera:
    def __init__(self):
        self.cap = None
        self.servoPort = None

    def set_camera(self, camera_number):
        self.cap = cv2.VideoCapture(camera_number, cv2.CAP_DSHOW)
        if self.cap.isOpened():
            return True
        else:  # 回滚
            self.cap = None
            return False

    def set_servo(self, servo_port):
        self.servoPort = servo_port

    def get_frame(self):
        if self.cap is None:
            return None

        flag, frame = self.cap.read()
        if flag:
            return frame
        return None

    def move(self):
        pass

    def close(self):
        pass
        # self.cap.release()
        # print('release')


# if __name__ == '__main__':
    # cap = cv2.VideoCapture(0)
    # while 1:
    #     # get a frame
    #     ret, frame = cap.read()
    #     # show a frame
    #     cv2.imshow("capture", frame)
    #     if cv2.waitKey(40) & 0xFF == ord('q'):  # 25帧
    #         break
    # cap.release()
    # cv2.destroyAllWindows()
