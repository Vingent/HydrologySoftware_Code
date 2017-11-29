#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/20 9:30
# @Author  : Vincent.G.Woo
# @Site    : 
# @File    : PyFormTst05.py
# @Software: PyCharm Community Edition
# @Python_Version:3.5.2
# @Software_Version:PyCharm Community Edition 2017.3


# !/usr/bin/python
# sigslot.py
from PyQt5.QtWidgets import QApplication, QLCDNumber, QSlider, QVBoxLayout
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
import time


class SigSlot(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self)

        self.setWindowTitle('signal & slot')
        lcd = QLCDNumber(self)
        slider = QSlider(Qt.Horizontal, self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(slider)

        self.setLayout(vbox)
        slider.valueChanged.connect(lcd.display)
        self.resize(350, 300)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    qb = SigSlot()
    qb.show()
    sys.exit(app.exec_())









