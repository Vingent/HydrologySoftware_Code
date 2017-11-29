#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/3 13:29
# @Author  : Vincent.G.Woo
# @Site    : 
# @File    : blog_test.py
# @Software: PyCharm Community Edition
# @Python_Version:
# @Software_Version:

import sys
from blog import Ui_MainWindow
from PyQt5 import QtWidgets

class mywindows(QtWidgets.QWidget,Ui_MainWindow):
    def __init__(self):
        super(mywindows,self).__init__()
        self.setupUi(self)

if __name__=='__main__':
    app=QtWidgets.QApplication(sys.argv)
    myshow=mywindows()
    myshow.show()
    sys.exit(app.exec_())
