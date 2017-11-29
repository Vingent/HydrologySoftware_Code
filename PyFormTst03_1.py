#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/9 16:53
# @Author  : Vincent.G.Woo
# @Site    : 
# @File    : PyFormTst03_1.py
# @Software: PyCharm Community Edition
# @Python_Version:3.5.2
# @Software_Version:PyCharm Community Edition 2017.3


import sys
from PyQt5 import QtWidgets
from PyFormTst03 import Ui_Form
# 该句调用Ui_Form类，本例中可以理解为调用Designer生成的GUI成果

class mywindow(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.myPrint)       #槽函数不用加括号

        #原出错原因：大小写区别
        # 抄写源代码中“PushButton”与本类继承的Ui_Form类中的“pushButton”首字母大小写不同
        #所以无法识别其Attribute

    def myPrint(self):                                      #定义槽
        print("Hello World")

if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    myshow=mywindow()
    myshow.show()
    sys.exit(app.exec_())

