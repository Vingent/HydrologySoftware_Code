#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/7 16:21
# @Author  : Vincent.G.Woo
# @Site    : 
# @File    : PyQt01.py
# @Software: PyCharm Community Edition
# @Python_Version:
# @Software_Version:

import sys
from PyQt5 import QtCore,QtGui
from testButton import Ui_Form

class MyForm():
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui=Ui_Form()
        self.ui.setupUi(self)

if __name__=='__main__':
    app=QtGui.QApplication(sys.argv)
    myapp=MyForm()
    myapp.show()
    sys.exit(app.exec_())