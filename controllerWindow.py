# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'controllerWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(-1, -1, 0, 20)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.formLayout.setContentsMargins(40, 5, 40, 0)
        self.formLayout.setHorizontalSpacing(20)
        self.formLayout.setVerticalSpacing(5)
        self.formLayout.setObjectName("formLayout")
        self.IP = QtWidgets.QLabel(self.centralwidget)
        self.IP.setObjectName("IP")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.IP)
        self.ipInput = QtWidgets.QLineEdit(self.centralwidget)
        self.ipInput.setObjectName("ipInput")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.ipInput)
        self.PORT = QtWidgets.QLabel(self.centralwidget)
        self.PORT.setObjectName("PORT")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.PORT)
        self.portInput = QtWidgets.QLineEdit(self.centralwidget)
        self.portInput.setObjectName("portInput")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.portInput)
        self.CAMERA = QtWidgets.QLabel(self.centralwidget)
        self.CAMERA.setObjectName("CAMERA")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.CAMERA)
        self.cameraNumInput = QtWidgets.QSpinBox(self.centralwidget)
        self.cameraNumInput.setObjectName("cameraNumInput")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.cameraNumInput)
        self.USERNAME = QtWidgets.QLabel(self.centralwidget)
        self.USERNAME.setObjectName("USERNAME")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.USERNAME)
        self.userNameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.userNameInput.setObjectName("userNameInput")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.userNameInput)
        self.PASSWORD = QtWidgets.QLabel(self.centralwidget)
        self.PASSWORD.setObjectName("PASSWORD")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.PASSWORD)
        self.passwordInput = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordInput.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordInput.setObjectName("passwordInput")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.passwordInput)
        self.SERVO = QtWidgets.QLabel(self.centralwidget)
        self.SERVO.setObjectName("SERVO")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.SERVO)
        self.servoInput = QtWidgets.QComboBox(self.centralwidget)
        self.servoInput.setObjectName("servoInput")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.servoInput)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setContentsMargins(40, 0, 40, 30)
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.connectButton = QtWidgets.QPushButton(self.centralwidget)
        self.connectButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connectButton.sizePolicy().hasHeightForWidth())
        self.connectButton.setSizePolicy(sizePolicy)
        self.connectButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.connectButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.connectButton.setAutoDefault(False)
        self.connectButton.setObjectName("connectButton")
        self.horizontalLayout_3.addWidget(self.connectButton)
        self.closeButton = QtWidgets.QPushButton(self.centralwidget)
        self.closeButton.setEnabled(False)
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout_3.addWidget(self.closeButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.log = QtWidgets.QTextBrowser(self.centralwidget)
        self.log.setObjectName("log")
        self.horizontalLayout_2.addWidget(self.log)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.cameraLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cameraLabel.sizePolicy().hasHeightForWidth())
        self.cameraLabel.setSizePolicy(sizePolicy)
        self.cameraLabel.setMinimumSize(QtCore.QSize(400, 300))
        self.cameraLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cameraLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.cameraLabel.setObjectName("cameraLabel")
        self.horizontalLayout_4.addWidget(self.cameraLabel)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(20, 20, 20, 20)
        self.gridLayout.setSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        self.moveRightButton = QtWidgets.QPushButton(self.centralwidget)
        self.moveRightButton.setMinimumSize(QtCore.QSize(60, 60))
        self.moveRightButton.setMaximumSize(QtCore.QSize(60, 60))
        self.moveRightButton.setObjectName("moveRightButton")
        self.gridLayout.addWidget(self.moveRightButton, 1, 2, 1, 1)
        self.moveDownButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.moveDownButton.sizePolicy().hasHeightForWidth())
        self.moveDownButton.setSizePolicy(sizePolicy)
        self.moveDownButton.setMinimumSize(QtCore.QSize(60, 60))
        self.moveDownButton.setMaximumSize(QtCore.QSize(60, 60))
        self.moveDownButton.setObjectName("moveDownButton")
        self.gridLayout.addWidget(self.moveDownButton, 2, 1, 1, 1)
        self.moveUpButton = QtWidgets.QPushButton(self.centralwidget)
        self.moveUpButton.setMinimumSize(QtCore.QSize(60, 60))
        self.moveUpButton.setMaximumSize(QtCore.QSize(60, 60))
        self.moveUpButton.setObjectName("moveUpButton")
        self.gridLayout.addWidget(self.moveUpButton, 0, 1, 1, 1)
        self.moveLeftButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.moveLeftButton.sizePolicy().hasHeightForWidth())
        self.moveLeftButton.setSizePolicy(sizePolicy)
        self.moveLeftButton.setMinimumSize(QtCore.QSize(60, 60))
        self.moveLeftButton.setMaximumSize(QtCore.QSize(60, 60))
        self.moveLeftButton.setObjectName("moveLeftButton")
        self.gridLayout.addWidget(self.moveLeftButton, 1, 0, 1, 1)
        self.horizontalLayout_4.addLayout(self.gridLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.ipInput, self.portInput)
        MainWindow.setTabOrder(self.portInput, self.connectButton)
        MainWindow.setTabOrder(self.connectButton, self.closeButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CameraController"))
        self.IP.setText(_translate("MainWindow", "服务器IP"))
        self.ipInput.setText(_translate("MainWindow", "127.0.0.1"))
        self.PORT.setText(_translate("MainWindow", "Port"))
        self.portInput.setText(_translate("MainWindow", "9800"))
        self.CAMERA.setText(_translate("MainWindow", "Camera"))
        self.USERNAME.setText(_translate("MainWindow", "用户名"))
        self.userNameInput.setText(_translate("MainWindow", "test"))
        self.PASSWORD.setText(_translate("MainWindow", "密码"))
        self.passwordInput.setText(_translate("MainWindow", "123456"))
        self.SERVO.setText(_translate("MainWindow", "云台端口"))
        self.connectButton.setText(_translate("MainWindow", "连接"))
        self.closeButton.setText(_translate("MainWindow", "断开"))
        self.cameraLabel.setText(_translate("MainWindow", "摄像头画面"))
        self.moveRightButton.setText(_translate("MainWindow", "右"))
        self.moveDownButton.setText(_translate("MainWindow", "下"))
        self.moveUpButton.setText(_translate("MainWindow", "上"))
        self.moveLeftButton.setText(_translate("MainWindow", "左"))
