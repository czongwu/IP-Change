# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from myWigets import MyLineEdit

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 461)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.FileDirLabel = QtWidgets.QLabel(self.centralwidget)
        self.FileDirLabel.setMinimumSize(QtCore.QSize(70, 25))
        self.FileDirLabel.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.FileDirLabel.setFont(font)
        self.FileDirLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.FileDirLabel.setObjectName("FileDirLabel")
        self.horizontalLayout_5.addWidget(self.FileDirLabel)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(60, 0))
        self.pushButton.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_5.addWidget(self.pushButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.No_1 = QtWidgets.QLabel(self.centralwidget)
        self.No_1.setMinimumSize(QtCore.QSize(25, 25))
        self.No_1.setMaximumSize(QtCore.QSize(25, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.No_1.setFont(font)
        self.No_1.setObjectName("No_1")
        self.verticalLayout.addWidget(self.No_1)
        self.No_2 = QtWidgets.QLabel(self.centralwidget)
        self.No_2.setMinimumSize(QtCore.QSize(25, 25))
        self.No_2.setMaximumSize(QtCore.QSize(25, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.No_2.setFont(font)
        self.No_2.setObjectName("No_2")
        self.verticalLayout.addWidget(self.No_2)
        self.No_3 = QtWidgets.QLabel(self.centralwidget)
        self.No_3.setMinimumSize(QtCore.QSize(25, 25))
        self.No_3.setMaximumSize(QtCore.QSize(25, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.No_3.setFont(font)
        self.No_3.setObjectName("No_3")
        self.verticalLayout.addWidget(self.No_3)
        self.No_4 = QtWidgets.QLabel(self.centralwidget)
        self.No_4.setMinimumSize(QtCore.QSize(25, 25))
        self.No_4.setMaximumSize(QtCore.QSize(25, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.No_4.setFont(font)
        self.No_4.setObjectName("No_4")
        self.verticalLayout.addWidget(self.No_4)
        self.No_5 = QtWidgets.QLabel(self.centralwidget)
        self.No_5.setMinimumSize(QtCore.QSize(25, 25))
        self.No_5.setMaximumSize(QtCore.QSize(25, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.No_5.setFont(font)
        self.No_5.setObjectName("No_5")
        self.verticalLayout.addWidget(self.No_5)
        self.No_6 = QtWidgets.QLabel(self.centralwidget)
        self.No_6.setMinimumSize(QtCore.QSize(25, 25))
        self.No_6.setMaximumSize(QtCore.QSize(25, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.No_6.setFont(font)
        self.No_6.setObjectName("No_6")
        self.verticalLayout.addWidget(self.No_6)
        self.No_7 = QtWidgets.QLabel(self.centralwidget)
        self.No_7.setMinimumSize(QtCore.QSize(25, 25))
        self.No_7.setMaximumSize(QtCore.QSize(25, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.No_7.setFont(font)
        self.No_7.setObjectName("No_7")
        self.verticalLayout.addWidget(self.No_7)
        self.No_8 = QtWidgets.QLabel(self.centralwidget)
        self.No_8.setMinimumSize(QtCore.QSize(25, 25))
        self.No_8.setMaximumSize(QtCore.QSize(25, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.No_8.setFont(font)
        self.No_8.setObjectName("No_8")
        self.verticalLayout.addWidget(self.No_8)
        self.No_9 = QtWidgets.QLabel(self.centralwidget)
        self.No_9.setMinimumSize(QtCore.QSize(25, 25))
        self.No_9.setMaximumSize(QtCore.QSize(25, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.No_9.setFont(font)
        self.No_9.setObjectName("No_9")
        self.verticalLayout.addWidget(self.No_9)
        self.No_10 = QtWidgets.QLabel(self.centralwidget)
        self.No_10.setMinimumSize(QtCore.QSize(25, 25))
        self.No_10.setMaximumSize(QtCore.QSize(25, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.No_10.setFont(font)
        self.No_10.setObjectName("No_10")
        self.verticalLayout.addWidget(self.No_10)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.FileDir_1 = MyLineEdit()
        # self.FileDir_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.FileDir_1.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.FileDir_1.setFont(font)
        self.FileDir_1.setObjectName("FileDir_1")
        self.verticalLayout_2.addWidget(self.FileDir_1)
        self.FileDir_2 = MyLineEdit()
        # self.FileDir_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.FileDir_2.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.FileDir_2.setFont(font)
        self.FileDir_2.setObjectName("FileDir_2")
        self.verticalLayout_2.addWidget(self.FileDir_2)
        self.FileDir_3 = MyLineEdit()
        # self.FileDir_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.FileDir_3.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.FileDir_3.setFont(font)
        self.FileDir_3.setObjectName("FileDir_3")
        self.verticalLayout_2.addWidget(self.FileDir_3)
        self.FileDir_4 = MyLineEdit()
        # self.FileDir_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.FileDir_4.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.FileDir_4.setFont(font)
        self.FileDir_4.setObjectName("FileDir_4")
        self.verticalLayout_2.addWidget(self.FileDir_4)
        self.FileDir_5 = MyLineEdit()
        # self.FileDir_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.FileDir_5.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.FileDir_5.setFont(font)
        self.FileDir_5.setObjectName("FileDir_5")
        self.verticalLayout_2.addWidget(self.FileDir_5)
        self.FileDir_6 = MyLineEdit()
        # self.FileDir_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.FileDir_6.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.FileDir_6.setFont(font)
        self.FileDir_6.setObjectName("FileDir_6")
        self.verticalLayout_2.addWidget(self.FileDir_6)
        self.FileDir_7 = MyLineEdit()
        # self.FileDir_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.FileDir_7.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.FileDir_7.setFont(font)
        self.FileDir_7.setObjectName("FileDir_7")
        self.verticalLayout_2.addWidget(self.FileDir_7)
        self.FileDir_8 = MyLineEdit()
        # self.FileDir_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.FileDir_8.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.FileDir_8.setFont(font)
        self.FileDir_8.setObjectName("FileDir_8")
        self.verticalLayout_2.addWidget(self.FileDir_8)
        self.FileDir_9 = MyLineEdit()
        # self.FileDir_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.FileDir_9.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.FileDir_9.setFont(font)
        self.FileDir_9.setObjectName("FileDir_9")
        self.verticalLayout_2.addWidget(self.FileDir_9)
        self.FileDir_10 = MyLineEdit()
        # self.FileDir_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.FileDir_10.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.FileDir_10.setFont(font)
        self.FileDir_10.setObjectName("FileDir_10")
        self.verticalLayout_2.addWidget(self.FileDir_10)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.DirChoiceBtn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.DirChoiceBtn_1.setMinimumSize(QtCore.QSize(50, 25))
        self.DirChoiceBtn_1.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.DirChoiceBtn_1.setFont(font)
        self.DirChoiceBtn_1.setObjectName("DirChoiceBtn_1")
        self.verticalLayout_3.addWidget(self.DirChoiceBtn_1)
        self.DirChoiceBtn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.DirChoiceBtn_2.setMinimumSize(QtCore.QSize(50, 25))
        self.DirChoiceBtn_2.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.DirChoiceBtn_2.setFont(font)
        self.DirChoiceBtn_2.setObjectName("DirChoiceBtn_2")
        self.verticalLayout_3.addWidget(self.DirChoiceBtn_2)
        self.DirChoiceBtn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.DirChoiceBtn_3.setMinimumSize(QtCore.QSize(50, 25))
        self.DirChoiceBtn_3.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.DirChoiceBtn_3.setFont(font)
        self.DirChoiceBtn_3.setObjectName("DirChoiceBtn_3")
        self.verticalLayout_3.addWidget(self.DirChoiceBtn_3)
        self.DirChoiceBtn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.DirChoiceBtn_4.setMinimumSize(QtCore.QSize(50, 25))
        self.DirChoiceBtn_4.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.DirChoiceBtn_4.setFont(font)
        self.DirChoiceBtn_4.setObjectName("DirChoiceBtn_4")
        self.verticalLayout_3.addWidget(self.DirChoiceBtn_4)
        self.DirChoiceBtn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.DirChoiceBtn_5.setMinimumSize(QtCore.QSize(50, 25))
        self.DirChoiceBtn_5.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.DirChoiceBtn_5.setFont(font)
        self.DirChoiceBtn_5.setObjectName("DirChoiceBtn_5")
        self.verticalLayout_3.addWidget(self.DirChoiceBtn_5)
        self.DirChoiceBtn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.DirChoiceBtn_6.setMinimumSize(QtCore.QSize(50, 25))
        self.DirChoiceBtn_6.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.DirChoiceBtn_6.setFont(font)
        self.DirChoiceBtn_6.setObjectName("DirChoiceBtn_6")
        self.verticalLayout_3.addWidget(self.DirChoiceBtn_6)
        self.DirChoiceBtn_7 = QtWidgets.QPushButton(self.centralwidget)
        self.DirChoiceBtn_7.setMinimumSize(QtCore.QSize(50, 25))
        self.DirChoiceBtn_7.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.DirChoiceBtn_7.setFont(font)
        self.DirChoiceBtn_7.setObjectName("DirChoiceBtn_7")
        self.verticalLayout_3.addWidget(self.DirChoiceBtn_7)
        self.DirChoiceBtn_8 = QtWidgets.QPushButton(self.centralwidget)
        self.DirChoiceBtn_8.setMinimumSize(QtCore.QSize(50, 25))
        self.DirChoiceBtn_8.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.DirChoiceBtn_8.setFont(font)
        self.DirChoiceBtn_8.setObjectName("DirChoiceBtn_8")
        self.verticalLayout_3.addWidget(self.DirChoiceBtn_8)
        self.DirChoiceBtn_9 = QtWidgets.QPushButton(self.centralwidget)
        self.DirChoiceBtn_9.setMinimumSize(QtCore.QSize(50, 25))
        self.DirChoiceBtn_9.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.DirChoiceBtn_9.setFont(font)
        self.DirChoiceBtn_9.setObjectName("DirChoiceBtn_9")
        self.verticalLayout_3.addWidget(self.DirChoiceBtn_9)
        self.DirChoiceBtn_10 = QtWidgets.QPushButton(self.centralwidget)
        self.DirChoiceBtn_10.setMinimumSize(QtCore.QSize(50, 25))
        self.DirChoiceBtn_10.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.DirChoiceBtn_10.setFont(font)
        self.DirChoiceBtn_10.setObjectName("DirChoiceBtn_10")
        self.verticalLayout_3.addWidget(self.DirChoiceBtn_10)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_4.addWidget(self.line)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.ico = QtWidgets.QLabel(self.centralwidget)
        self.ico.setMinimumSize(QtCore.QSize(60, 60))
        self.ico.setMaximumSize(QtCore.QSize(60, 60))
        self.ico.setObjectName("ico")
        self.horizontalLayout_4.addWidget(self.ico)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.NameLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.NameLabel.setFont(font)
        self.NameLabel.setObjectName("NameLabel")
        self.horizontalLayout_2.addWidget(self.NameLabel)
        self.NameEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.NameEdit.setMinimumSize(QtCore.QSize(0, 25))
        self.NameEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.NameEdit.setFont(font)
        self.NameEdit.setObjectName("NameEdit")
        self.horizontalLayout_2.addWidget(self.NameEdit)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.IpLabel = QtWidgets.QLabel(self.centralwidget)
        self.IpLabel.setMinimumSize(QtCore.QSize(80, 25))
        self.IpLabel.setMaximumSize(QtCore.QSize(50, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.IpLabel.setFont(font)
        self.IpLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.IpLabel.setObjectName("IpLabel")
        self.horizontalLayout_3.addWidget(self.IpLabel)
        self.IpChangeEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.IpChangeEdit.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.IpChangeEdit.setFont(font)
        self.IpChangeEdit.setObjectName("IpChangeEdit")
        self.horizontalLayout_3.addWidget(self.IpChangeEdit)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.IpChangeBtn = QtWidgets.QPushButton(self.centralwidget)
        self.IpChangeBtn.setMinimumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.IpChangeBtn.setFont(font)
        self.IpChangeBtn.setObjectName("IpChangeBtn")
        self.horizontalLayout_4.addWidget(self.IpChangeBtn)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.FileDirLabel.setText(_translate("MainWindow", "文件路径："))
        self.pushButton.setText(_translate("MainWindow", "清空所有"))
        self.No_1.setText(_translate("MainWindow", "1."))
        self.No_2.setText(_translate("MainWindow", "2."))
        self.No_3.setText(_translate("MainWindow", "3."))
        self.No_4.setText(_translate("MainWindow", "4."))
        self.No_5.setText(_translate("MainWindow", "5."))
        self.No_6.setText(_translate("MainWindow", "6."))
        self.No_7.setText(_translate("MainWindow", "7."))
        self.No_8.setText(_translate("MainWindow", "8."))
        self.No_9.setText(_translate("MainWindow", "9."))
        self.No_10.setText(_translate("MainWindow", "10."))
        self.DirChoiceBtn_1.setText(_translate("MainWindow", "选择"))
        self.DirChoiceBtn_2.setText(_translate("MainWindow", "选择"))
        self.DirChoiceBtn_3.setText(_translate("MainWindow", "选择"))
        self.DirChoiceBtn_4.setText(_translate("MainWindow", "选择"))
        self.DirChoiceBtn_5.setText(_translate("MainWindow", "选择"))
        self.DirChoiceBtn_6.setText(_translate("MainWindow", "选择"))
        self.DirChoiceBtn_7.setText(_translate("MainWindow", "选择"))
        self.DirChoiceBtn_8.setText(_translate("MainWindow", "选择"))
        self.DirChoiceBtn_9.setText(_translate("MainWindow", "选择"))
        self.DirChoiceBtn_10.setText(_translate("MainWindow", "选择"))
        self.ico.setText(_translate("MainWindow", "TextLabel"))
        self.NameLabel.setText(_translate("MainWindow", "服务器名："))
        self.IpLabel.setText(_translate("MainWindow", "IP地址："))
        self.IpChangeBtn.setText(_translate("MainWindow", "一键修改"))

