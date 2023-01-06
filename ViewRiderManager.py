# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ViewRiderman.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(0, 177, 171);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMinimumSize(QtCore.QSize(100, 0))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 180))
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setMinimumSize(QtCore.QSize(600, 0))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_7 = QtWidgets.QFrame(self.frame_4)
        self.frame_7.setMaximumSize(QtCore.QSize(16777215, 45))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_5 = QtWidgets.QFrame(self.frame_7)
        self.frame_5.setMinimumSize(QtCore.QSize(450, 0))
        self.frame_5.setMaximumSize(QtCore.QSize(450, 16777215))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_3.setContentsMargins(-1, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_2 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.frame_5)
        self.frame_9 = QtWidgets.QFrame(self.frame_7)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_2.addWidget(self.frame_9)
        self.verticalLayout_2.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.frame_4)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_11 = QtWidgets.QFrame(self.frame_8)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_3.addWidget(self.frame_11)
        self.frame_10 = QtWidgets.QFrame(self.frame_8)
        self.frame_10.setMinimumSize(QtCore.QSize(0, 125))
        self.frame_10.setMaximumSize(QtCore.QSize(16777215, 125))
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_13 = QtWidgets.QFrame(self.frame_10)
        self.frame_13.setMaximumSize(QtCore.QSize(70, 16777215))
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_3.addWidget(self.frame_13)
        self.frame_14 = QtWidgets.QFrame(self.frame_10)
        self.frame_14.setMinimumSize(QtCore.QSize(600, 0))
        self.frame_14.setMaximumSize(QtCore.QSize(900, 100))
        self.frame_14.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.frame_14.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_14)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_18 = QtWidgets.QFrame(self.frame_14)
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.verticalLayout_4.addWidget(self.frame_18)
        self.frame_17 = QtWidgets.QFrame(self.frame_14)
        self.frame_17.setMinimumSize(QtCore.QSize(0, 90))
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_17)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, -1)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_19 = QtWidgets.QFrame(self.frame_17)
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.horizontalLayout_4.addWidget(self.frame_19)
        self.frame_20 = QtWidgets.QFrame(self.frame_17)
        self.frame_20.setMinimumSize(QtCore.QSize(80, 72))
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_20)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_34 = QtWidgets.QFrame(self.frame_20)
        self.frame_34.setMinimumSize(QtCore.QSize(0, 62))
        self.frame_34.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_34.setObjectName("frame_34")
        self.btnviewemployee = QtWidgets.QPushButton(self.frame_34)
        self.btnviewemployee.setGeometry(QtCore.QRect(0, 0, 71, 61))
        self.btnviewemployee.setMinimumSize(QtCore.QSize(0, 61))
        self.btnviewemployee.setStyleSheet("*{\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"border: 1px solid #6a6a6a;\n"
"border-radius:20px;\n"
"background-size: 100% 100%;\n"
"box-shadow:0px 30px 60px #22dbe4;\n"
"}")
        self.btnviewemployee.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Images/Images/Project Imgs/viewemp-removebg-preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnviewemployee.setIcon(icon)
        self.btnviewemployee.setIconSize(QtCore.QSize(70, 70))
        self.btnviewemployee.setObjectName("btnviewemployee")
        self.verticalLayout_5.addWidget(self.frame_34)
        self.frame_24 = QtWidgets.QFrame(self.frame_20)
        self.frame_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_24)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_3 = QtWidgets.QLabel(self.frame_24)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)
        self.verticalLayout_5.addWidget(self.frame_24)
        self.horizontalLayout_4.addWidget(self.frame_20)
        self.frame_29 = QtWidgets.QFrame(self.frame_17)
        self.frame_29.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_29.setObjectName("frame_29")
        self.horizontalLayout_4.addWidget(self.frame_29)
        self.frame_21 = QtWidgets.QFrame(self.frame_17)
        self.frame_21.setMinimumSize(QtCore.QSize(80, 0))
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_21)
        self.gridLayout_6.setContentsMargins(-1, 0, 0, 0)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.frame_27 = QtWidgets.QFrame(self.frame_21)
        self.frame_27.setMinimumSize(QtCore.QSize(80, 72))
        self.frame_27.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_27.setObjectName("frame_27")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_27)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_35 = QtWidgets.QFrame(self.frame_27)
        self.frame_35.setMinimumSize(QtCore.QSize(0, 62))
        self.frame_35.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_35.setObjectName("frame_35")
        self.btnviewrider = QtWidgets.QPushButton(self.frame_35)
        self.btnviewrider.setGeometry(QtCore.QRect(0, 0, 71, 61))
        self.btnviewrider.setMinimumSize(QtCore.QSize(0, 61))
        self.btnviewrider.setMaximumSize(QtCore.QSize(16777215, 50))
        self.btnviewrider.setStyleSheet("*{\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"border: 1px solid #6a6a6a;\n"
"border-radius:20px;\n"
"background-size: 100% 100%;\n"
"box-shadow:0px 30px 60px #22dbe4;\n"
"}")
        self.btnviewrider.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Images/Images/Project Imgs/rider-removebg-preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnviewrider.setIcon(icon1)
        self.btnviewrider.setIconSize(QtCore.QSize(75, 75))
        self.btnviewrider.setObjectName("btnviewrider")
        self.verticalLayout_6.addWidget(self.frame_35)
        self.frame_36 = QtWidgets.QFrame(self.frame_27)
        self.frame_36.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_36.setObjectName("frame_36")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_36)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_4 = QtWidgets.QLabel(self.frame_36)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_5.addWidget(self.label_4, 0, 0, 1, 1)
        self.verticalLayout_6.addWidget(self.frame_36)
        self.gridLayout_6.addWidget(self.frame_27, 0, 0, 1, 1)
        self.horizontalLayout_4.addWidget(self.frame_21)
        self.frame_30 = QtWidgets.QFrame(self.frame_17)
        self.frame_30.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_30.setObjectName("frame_30")
        self.horizontalLayout_4.addWidget(self.frame_30)
        self.frame_31 = QtWidgets.QFrame(self.frame_17)
        self.frame_31.setMinimumSize(QtCore.QSize(80, 0))
        self.frame_31.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_31.setObjectName("frame_31")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_31)
        self.gridLayout_8.setContentsMargins(-1, 0, 0, 0)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.frame_37 = QtWidgets.QFrame(self.frame_31)
        self.frame_37.setMinimumSize(QtCore.QSize(80, 72))
        self.frame_37.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_37.setObjectName("frame_37")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_37)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_38 = QtWidgets.QFrame(self.frame_37)
        self.frame_38.setMinimumSize(QtCore.QSize(0, 62))
        self.frame_38.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_38.setObjectName("frame_38")
        self.btnapprovals = QtWidgets.QPushButton(self.frame_38)
        self.btnapprovals.setGeometry(QtCore.QRect(0, 0, 71, 61))
        self.btnapprovals.setMinimumSize(QtCore.QSize(0, 61))
        self.btnapprovals.setStyleSheet("*{\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"border: 1px solid #6a6a6a;\n"
"border-radius:20px;\n"
"background-size: 100% 100%;\n"
"box-shadow:0px 30px 60px #22dbe4;\n"
"}")
        self.btnapprovals.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Images/Images/Project Imgs/approval-removebg-preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnapprovals.setIcon(icon2)
        self.btnapprovals.setIconSize(QtCore.QSize(50, 50))
        self.btnapprovals.setObjectName("btnapprovals")
        self.verticalLayout_7.addWidget(self.frame_38)
        self.frame_39 = QtWidgets.QFrame(self.frame_37)
        self.frame_39.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_39.setObjectName("frame_39")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_39)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_5 = QtWidgets.QLabel(self.frame_39)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_7.addWidget(self.label_5, 0, 0, 1, 1)
        self.verticalLayout_7.addWidget(self.frame_39)
        self.gridLayout_8.addWidget(self.frame_37, 0, 0, 1, 1)
        self.horizontalLayout_4.addWidget(self.frame_31)
        self.frame_22 = QtWidgets.QFrame(self.frame_17)
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.horizontalLayout_4.addWidget(self.frame_22)
        self.frame_32 = QtWidgets.QFrame(self.frame_17)
        self.frame_32.setMinimumSize(QtCore.QSize(80, 0))
        self.frame_32.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_32.setObjectName("frame_32")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.frame_32)
        self.gridLayout_11.setContentsMargins(-1, 0, 0, 0)
        self.gridLayout_11.setSpacing(0)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.frame_40 = QtWidgets.QFrame(self.frame_32)
        self.frame_40.setMinimumSize(QtCore.QSize(80, 72))
        self.frame_40.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_40.setObjectName("frame_40")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_40)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_43 = QtWidgets.QFrame(self.frame_40)
        self.frame_43.setMinimumSize(QtCore.QSize(0, 62))
        self.frame_43.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_43.setObjectName("frame_43")
        self.btnviewthreshold = QtWidgets.QPushButton(self.frame_43)
        self.btnviewthreshold.setGeometry(QtCore.QRect(0, 0, 71, 61))
        self.btnviewthreshold.setMinimumSize(QtCore.QSize(0, 61))
        self.btnviewthreshold.setStyleSheet("*{\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"border: 1px solid #6a6a6a;\n"
"border-radius:20px;\n"
"background-size: 100% 100%;\n"
"box-shadow:0px 30px 60px #22dbe4;\n"
"}")
        self.btnviewthreshold.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Images/Images/Project Imgs/threshold-removebg-preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnviewthreshold.setIcon(icon3)
        self.btnviewthreshold.setIconSize(QtCore.QSize(60, 60))
        self.btnviewthreshold.setObjectName("btnviewthreshold")
        self.verticalLayout_9.addWidget(self.frame_43)
        self.frame_44 = QtWidgets.QFrame(self.frame_40)
        self.frame_44.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_44.setObjectName("frame_44")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.frame_44)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label_7 = QtWidgets.QLabel(self.frame_44)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_10.addWidget(self.label_7, 0, 0, 1, 1)
        self.verticalLayout_9.addWidget(self.frame_44)
        self.gridLayout_11.addWidget(self.frame_40, 0, 0, 1, 1)
        self.horizontalLayout_4.addWidget(self.frame_32)
        self.frame_23 = QtWidgets.QFrame(self.frame_17)
        self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.horizontalLayout_4.addWidget(self.frame_23)
        self.frame_25 = QtWidgets.QFrame(self.frame_17)
        self.frame_25.setMinimumSize(QtCore.QSize(80, 0))
        self.frame_25.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_25.setObjectName("frame_25")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_25)
        self.verticalLayout_12.setContentsMargins(-1, 0, 0, 0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.frame_45 = QtWidgets.QFrame(self.frame_25)
        self.frame_45.setMinimumSize(QtCore.QSize(0, 62))
        self.frame_45.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_45.setObjectName("frame_45")
        self.btnviewanalytics = QtWidgets.QPushButton(self.frame_45)
        self.btnviewanalytics.setGeometry(QtCore.QRect(0, 0, 69, 61))
        self.btnviewanalytics.setMinimumSize(QtCore.QSize(0, 61))
        self.btnviewanalytics.setStyleSheet("*{\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"border: 1px solid #6a6a6a;\n"
"border-radius:20px;\n"
"background-size: 100% 100%;\n"
"box-shadow:0px 30px 60px #22dbe4;\n"
"}")
        self.btnviewanalytics.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Images/Images/Project Imgs/analytics-removebg-preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnviewanalytics.setIcon(icon4)
        self.btnviewanalytics.setIconSize(QtCore.QSize(90, 90))
        self.btnviewanalytics.setObjectName("btnviewanalytics")
        self.verticalLayout_12.addWidget(self.frame_45)
        self.frame_50 = QtWidgets.QFrame(self.frame_25)
        self.frame_50.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_50.setObjectName("frame_50")
        self.label_10 = QtWidgets.QLabel(self.frame_50)
        self.label_10.setGeometry(QtCore.QRect(10, 0, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_12.addWidget(self.frame_50)
        self.horizontalLayout_4.addWidget(self.frame_25)
        self.frame_33 = QtWidgets.QFrame(self.frame_17)
        self.frame_33.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_33.setObjectName("frame_33")
        self.horizontalLayout_4.addWidget(self.frame_33)
        self.frame_26 = QtWidgets.QFrame(self.frame_17)
        self.frame_26.setMinimumSize(QtCore.QSize(80, 0))
        self.frame_26.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_26.setObjectName("frame_26")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_26)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.frame_51 = QtWidgets.QFrame(self.frame_26)
        self.frame_51.setMinimumSize(QtCore.QSize(0, 62))
        self.frame_51.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_51.setObjectName("frame_51")
        self.btnlogout = QtWidgets.QPushButton(self.frame_51)
        self.btnlogout.setGeometry(QtCore.QRect(0, 0, 69, 61))
        self.btnlogout.setMinimumSize(QtCore.QSize(0, 61))
        self.btnlogout.setStyleSheet("*{\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"border: 1px solid #6a6a6a;\n"
"border-radius:20px;\n"
"background-size: 100% 100%;\n"
"box-shadow:0px 30px 60px #22dbe4;\n"
"}")
        self.btnlogout.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/Images/Images/Project Imgs/logout-removebg-preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnlogout.setIcon(icon5)
        self.btnlogout.setIconSize(QtCore.QSize(80, 80))
        self.btnlogout.setObjectName("btnlogout")
        self.verticalLayout_14.addWidget(self.frame_51)
        self.frame_54 = QtWidgets.QFrame(self.frame_26)
        self.frame_54.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_54.setObjectName("frame_54")
        self.label_12 = QtWidgets.QLabel(self.frame_54)
        self.label_12.setGeometry(QtCore.QRect(10, 0, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_14.addWidget(self.frame_54)
        self.horizontalLayout_4.addWidget(self.frame_26)
        self.frame_28 = QtWidgets.QFrame(self.frame_17)
        self.frame_28.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_28.setObjectName("frame_28")
        self.horizontalLayout_4.addWidget(self.frame_28)
        self.verticalLayout_4.addWidget(self.frame_17)
        self.frame_16 = QtWidgets.QFrame(self.frame_14)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.verticalLayout_4.addWidget(self.frame_16)
        self.horizontalLayout_3.addWidget(self.frame_14)
        self.frame_15 = QtWidgets.QFrame(self.frame_10)
        self.frame_15.setMaximumSize(QtCore.QSize(70, 16777215))
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_3.addWidget(self.frame_15)
        self.verticalLayout_3.addWidget(self.frame_10)
        self.frame_12 = QtWidgets.QFrame(self.frame_8)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_3.addWidget(self.frame_12)
        self.verticalLayout_2.addWidget(self.frame_8)
        self.horizontalLayout.addWidget(self.frame_4)
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setMinimumSize(QtCore.QSize(170, 170))
        self.frame_6.setMaximumSize(QtCore.QSize(180, 180))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_2.setContentsMargins(-1, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.frame_6)
        self.label.setMaximumSize(QtCore.QSize(170, 16777215))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/Images/Images/Project Imgs/manager-removebg-preview.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.frame_6)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_42 = QtWidgets.QFrame(self.frame_3)
        self.frame_42.setMinimumSize(QtCore.QSize(0, 45))
        self.frame_42.setMaximumSize(QtCore.QSize(16777215, 45))
        self.frame_42.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_42.setObjectName("frame_42")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_42)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_47 = QtWidgets.QFrame(self.frame_42)
        self.frame_47.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_47.setObjectName("frame_47")
        self.horizontalLayout_5.addWidget(self.frame_47)
        self.frame_48 = QtWidgets.QFrame(self.frame_42)
        self.frame_48.setMaximumSize(QtCore.QSize(230, 50))
        self.frame_48.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_48.setObjectName("frame_48")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_48)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_52 = QtWidgets.QFrame(self.frame_48)
        self.frame_52.setMaximumSize(QtCore.QSize(30, 16777215))
        self.frame_52.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_52.setObjectName("frame_52")
        self.label_6 = QtWidgets.QLabel(self.frame_52)
        self.label_6.setGeometry(QtCore.QRect(0, 10, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.frame_52)
        self.frame_53 = QtWidgets.QFrame(self.frame_48)
        self.frame_53.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_53.setObjectName("frame_53")
        self.txtSearchbyIdViewRider = QtWidgets.QLineEdit(self.frame_53)
        self.txtSearchbyIdViewRider.setGeometry(QtCore.QRect(0, 10, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.txtSearchbyIdViewRider.setFont(font)
        self.txtSearchbyIdViewRider.setStyleSheet("*{\n"
"border: 1px solid #000000;\n"
"border-radius:10px;\n"
"}")
        self.txtSearchbyIdViewRider.setObjectName("txtSearchbyIdViewRider")
        self.horizontalLayout_6.addWidget(self.frame_53)
        self.horizontalLayout_5.addWidget(self.frame_48)
        self.frame_49 = QtWidgets.QFrame(self.frame_42)
        self.frame_49.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_49.setObjectName("frame_49")
        self.horizontalLayout_5.addWidget(self.frame_49)
        self.verticalLayout_8.addWidget(self.frame_42)
        self.frame_41 = QtWidgets.QFrame(self.frame_3)
        self.frame_41.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_41.setObjectName("frame_41")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_41)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame_55 = QtWidgets.QFrame(self.frame_41)
        self.frame_55.setMaximumSize(QtCore.QSize(20, 16777215))
        self.frame_55.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_55.setObjectName("frame_55")
        self.horizontalLayout_7.addWidget(self.frame_55)
        self.frame_56 = QtWidgets.QFrame(self.frame_41)
        self.frame_56.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_56.setObjectName("frame_56")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame_56)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.tableWidgetViewRider = QtWidgets.QTableWidget(self.frame_56)
        self.tableWidgetViewRider.setObjectName("tableWidgetViewRider")
        self.tableWidgetViewRider.setColumnCount(0)
        self.tableWidgetViewRider.setRowCount(0)
        self.gridLayout_9.addWidget(self.tableWidgetViewRider, 0, 0, 1, 1)
        self.horizontalLayout_7.addWidget(self.frame_56)
        self.frame_57 = QtWidgets.QFrame(self.frame_41)
        self.frame_57.setMaximumSize(QtCore.QSize(20, 16777215))
        self.frame_57.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_57.setObjectName("frame_57")
        self.horizontalLayout_7.addWidget(self.frame_57)
        self.verticalLayout_8.addWidget(self.frame_41)
        self.frame_46 = QtWidgets.QFrame(self.frame_3)
        self.frame_46.setMaximumSize(QtCore.QSize(16777215, 20))
        self.frame_46.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_46.setObjectName("frame_46")
        self.verticalLayout_8.addWidget(self.frame_46)
        self.verticalLayout.addWidget(self.frame_3)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ViewRider"))
        self.label_2.setText(_translate("MainWindow", "Manager\'s Dashboard"))
        self.label_3.setText(_translate("MainWindow", "View Employee"))
        self.label_4.setText(_translate("MainWindow", "View Riders"))
        self.label_5.setText(_translate("MainWindow", "Approvals"))
        self.label_7.setText(_translate("MainWindow", "View Threshold"))
        self.label_10.setText(_translate("MainWindow", "Analytics"))
        self.label_12.setText(_translate("MainWindow", "Logout"))
        self.label_6.setText(_translate("MainWindow", "ID"))
        self.txtSearchbyIdViewRider.setPlaceholderText(_translate("MainWindow", "Search"))
import TermProjectImages


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
