#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/2 18:16
# @Author  : Vincent.G.Woo
# @Site    : 
# @File    : PyQtEx1.py
# @Software: PyCharm Community Edition

import sys
from PyQt5 import QtWidgets

# pyqt窗口必须在QApplication方法中使用
app = QtWidgets.QApplication(sys.argv)

label = QtWidgets.QLabel("<p style='color: red; margin-left: 20px'><b>hell world</b></p>")  # qt支持html标签，强大吧
# 有了实例，就需要用show()让他显示
label.show()

sys.exit(app.exec_())  # 消息结束的时候，进程结束，并返回0，接着调用sys.exit(0)退出程序