# -*- coding: utf-8 -*-
import sys, base64
from PyQt5.QtCore import QTranslator, QTimer
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon, QPixmap
from function import Function
# from ico import logo
from smile_96px import image
import chuanqi


# 窗口显示和参数及动作大类
class ShowFunc(Function):
    def __init__(self):
        Function.__init__(self)
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())  # 禁止窗口拉伸和最大化
        self.setWindowTitle('批量修改工具')
        # self.setWindowIcon(QIcon(QPixmap('./lib/img/smile_96px.png')))
        self.setWindowIcon(self.smileLogo())
        # self.pix = QPixmap('./res/img/long60x60.png')
        self.ico.setPixmap(self.chuanLogo())
        self.DirChoiceBtn_1.clicked.connect(self.SelectFile_1)
        self.DirChoiceBtn_2.clicked.connect(self.SelectFile_2)
        self.DirChoiceBtn_3.clicked.connect(self.SelectFile_3)
        self.DirChoiceBtn_4.clicked.connect(self.SelectFile_4)
        self.DirChoiceBtn_5.clicked.connect(self.SelectFile_5)
        self.DirChoiceBtn_6.clicked.connect(self.SelectFile_6)
        self.DirChoiceBtn_7.clicked.connect(self.SelectFile_7)
        self.DirChoiceBtn_8.clicked.connect(self.SelectFile_8)
        self.DirChoiceBtn_9.clicked.connect(self.SelectFile_9)
        self.DirChoiceBtn_10.clicked.connect(self.SelectFile_10)
        self.time = QTimer()  # 初始化计时器
        self.time.setInterval(6000)  # 设置计时器时间为6秒，一秒为1000毫秒
        self.IpChangeBtn.clicked.connect(self.change_func)  # 按钮激活计时开始，修改按钮文本
        self.time.timeout.connect(self.referch)  # 计时结束还原按钮文本
        self.pushButton.clicked.connect(self.clear_all)
        self.init_view_info()

    def smileLogo(self):
        icon = QIcon()
        image_smile = base64.b64decode(image)
        pixmap = QPixmap()
        pixmap.loadFromData(image_smile)
        icon.addPixmap(pixmap, QIcon.Normal, QIcon.On)
        return icon

    def chuanLogo(self):
        chuanqi_image = base64.b64decode(chuanqi.image)
        pixmap = QPixmap()
        pixmap.loadFromData(chuanqi_image)
        return pixmap

    def change_func(self):
        self.ChangeBtn()
        self.time.start()  # 计时开始

    def referch(self):
        self.time.stop()  # 计时结束
        self.IpChangeBtn.setText('一键修改')


# 汉化
def translator():
    SetTranslator = QTranslator()
    SetTranslator.load('./lib/qt_zh_CN.qm')
    return SetTranslator


if __name__ == '__main__':
    app = QApplication(sys.argv)
    translatorLoad = translator()
    app.installTranslator(translatorLoad)
    view = ShowFunc()
    view.show()
    sys.exit(app.exec_())
