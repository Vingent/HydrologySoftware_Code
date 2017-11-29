#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/3 16:31
# @Author  : Vincent.G.Woo
# @Site    : 
# @File    : blogtest2.py
# @Software: PyCharm Community Edition
# @Python_Version:
# @Software_Version:

import sys
from blog import Ui_MainWindow
from PyQt5 import QtWidgets


class mywindow(QtWidgets.QWidget, Ui_MainWindow):
    global mStr

    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.pushButton_3.clicked.connect(self.addText)

    def getText(self):
        global mStr
        mStr = self.textEdit.toHtml()

    def setText(self):
        global mStr
        self.textBrowser.append(mStr)

    def addText(self):
        self.getText()
        self.setText()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myshow = mywindow()
    myshow.show()
    sys.exit(app.exec_())
