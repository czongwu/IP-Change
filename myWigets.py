# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QLineEdit


# 重构一个LineEdit控件
class MyLineEdit(QLineEdit):
    def __init__(self, *args, **kwargs):
        super(MyLineEdit, self).__init__(*args, **kwargs)
        self.setAcceptDrops(True)

    # 定义拖动事件
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    # 文件路径传递
    def dropEvent(self, event):
        path = event.mimeData().text().replace('file:///', '')
        self.setText(path)
